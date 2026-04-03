#!/usr/bin/env python3
"""
Semantic search over the AI Failure Periodic Table.

Finds failure classes by meaning using TF-IDF cosine similarity.
Zero external dependencies — pure Python stdlib.

Usage:
    python scripts/semantic_search.py "model deceives evaluator"
    python scripts/semantic_search.py "reward hacking RL" --top 10
    python scripts/semantic_search.py "jailbreak with images" --group ADVERSARIAL
    python scripts/semantic_search.py "data leak GDPR" --severity CRITICAL
    python scripts/semantic_search.py "query" --json

If the search index doesn't exist yet:
    python scripts/generate_embeddings.py
"""

import argparse
import json
import math
import pathlib
import re
import sys

DATA_DIR = pathlib.Path("data")
FAILURES_FILE = DATA_DIR / "failures.json"
INDEX_FILE = DATA_DIR / "search_index.json"

# ANSI colors
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"

GROUP_COLORS = {
    "EPISTEMIC":     "\033[94m",
    "AGENTIC":       "\033[33m",
    "ADVERSARIAL":   "\033[91m",
    "ALIGNMENT":     "\033[35m",
    "ARCHITECTURAL": "\033[32m",
    "DOMAIN":        "\033[93m",
    "GOVERNANCE":    "\033[37m",
}

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "this", "that", "these", "those", "it", "its",
    "as", "not", "no", "can", "via", "into", "which", "when", "than",
    "without", "using", "used", "such", "more", "other", "also", "any",
    "all", "each", "some", "if", "then", "even", "both", "their", "they",
    "them", "what", "how", "where", "who", "which", "while", "after",
    "before", "about", "through",
}


def tokenize(text: str) -> list[str]:
    text = text.lower()
    tokens = re.findall(r"[a-z][a-z0-9\-]*[a-z0-9]|[a-z]", text)
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]


def load_index():
    if not INDEX_FILE.exists():
        print(f"{RED}Search index not found.{RESET} Run:")
        print(f"  python scripts/generate_embeddings.py")
        sys.exit(1)
    return json.loads(INDEX_FILE.read_text())


def query_vec(query: str, vocab_index: dict, idf: list) -> dict:
    """Compute L2-normalized TF-IDF vector for query string."""
    tokens = tokenize(query)
    from collections import Counter
    counts = Counter(tokens)
    if not counts:
        return {}
    max_c = max(counts.values())
    vec = {}
    norm_sq = 0.0
    for term, count in counts.items():
        if term in vocab_index:
            idx = vocab_index[term]
            weight = (count / max_c) * idf[idx]
            vec[idx] = weight
            norm_sq += weight * weight
    if norm_sq > 0:
        norm = math.sqrt(norm_sq)
        vec = {k: v / norm for k, v in vec.items()}
    return vec


def cosine(q_vec: dict, doc_vec: dict) -> float:
    """Dot product of two sparse vectors (both L2-normalized)."""
    # Iterate over smaller vector for efficiency
    if len(q_vec) > len(doc_vec):
        q_vec, doc_vec = doc_vec, q_vec
    return sum(q_vec[k] * doc_vec.get(k, 0.0) for k in q_vec)


def search(query: str, top_k: int = 5, group_filter: str = None,
           severity_filter: str = None, json_output: bool = False):

    idx = load_index()
    failures_data = json.loads(FAILURES_FILE.read_text())
    failures_by_id = {f["id"]: f for f in failures_data["failures"]}

    vocab = idx["vocab"]
    idf = idx["idf"]
    vectors = idx["vectors"]
    vocab_index = {term: i for i, term in enumerate(vocab)}

    q = query_vec(query, vocab_index, idf)
    if not q:
        print(f"{RED}No indexed terms found in query.{RESET} Try different keywords.")
        sys.exit(1)

    # Score all classes
    scores = []
    for fid, doc_vec in vectors.items():
        # doc_vec keys are string indices from JSON
        doc_vec_int = {int(k): v for k, v in doc_vec.items()}
        failure = failures_by_id.get(fid)
        if not failure:
            continue
        if group_filter and failure.get("group", "").upper() != group_filter.upper():
            continue
        if severity_filter and failure.get("severity", "STANDARD").upper() != severity_filter.upper():
            continue
        sim = cosine(q, doc_vec_int)
        scores.append((sim, fid, failure))

    scores.sort(key=lambda x: -x[0])
    results = scores[:top_k]

    if json_output:
        out = []
        for sim, fid, f in results:
            out.append({
                "id": fid,
                "name": f["name"],
                "group": f["group"],
                "severity": f.get("severity", "STANDARD"),
                "score": round(sim, 4),
                "mechanism": f.get("mechanism", ""),
                "examples": f.get("examples", ""),
            })
        print(json.dumps(out, indent=2))
        return

    # Pretty terminal output
    print(f"\n{BOLD}Search: {CYAN}\"{query}\"{RESET}")
    filters = []
    if group_filter:
        filters.append(f"group={group_filter}")
    if severity_filter:
        filters.append(f"severity={severity_filter}")
    if filters:
        print(f"{DIM}Filters: {', '.join(filters)}{RESET}")
    print(f"{DIM}Top {len(results)} of {len(scores)} scored classes{RESET}\n")
    print("─" * 72)

    for rank, (sim, fid, f) in enumerate(results, 1):
        group = f.get("group", "")
        severity = f.get("severity", "STANDARD")
        gcol = GROUP_COLORS.get(group, "")
        scol = RED if severity == "CRITICAL" else ""

        bar_len = min(10, int(sim * 30))
        bar = "█" * bar_len + "░" * (10 - bar_len)

        print(f"{BOLD}#{rank}{RESET}  {scol}{BOLD}{fid}{RESET}")
        print(f"    {BOLD}{f['name']}{RESET}  {gcol}[{group}]{RESET}  {scol}{severity}{RESET}")
        print(f"    Score: {YELLOW}{sim:.4f}{RESET}  {DIM}{bar}{RESET}")
        print(f"    {DIM}{f.get('mechanism', '')[:80]}{RESET}")

        cs = f.get("case_studies", [])
        if cs and sim > 0.05:
            c = cs[0]
            if isinstance(c, dict):
                print(f"    {GREEN}→ {c['title']} ({c.get('date', '')}){RESET}")

        print()

    print("─" * 72)
    print(f"{DIM}TF-IDF index | {len(vocab)} terms | {len(failures_by_id)} classes{RESET}")


def main():
    parser = argparse.ArgumentParser(
        description="Semantic search over the AI Failure Periodic Table",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/semantic_search.py "model deceives evaluator"
  python scripts/semantic_search.py "reward hacking RL agent" --top 10
  python scripts/semantic_search.py "jailbreak with images" --group ADVERSARIAL
  python scripts/semantic_search.py "data leak GDPR" --severity CRITICAL
  python scripts/semantic_search.py "alignment faking training" --json
        """
    )
    parser.add_argument("query", help="Natural language search query")
    parser.add_argument("--top", "-k", type=int, default=5, metavar="N",
                        help="Number of results (default: 5)")
    parser.add_argument("--group", "-g", metavar="DIM",
                        help="Filter dimension: EPISTEMIC/AGENTIC/ADVERSARIAL/ALIGNMENT/ARCHITECTURAL/DOMAIN/GOVERNANCE")
    parser.add_argument("--severity", "-s", metavar="LEVEL",
                        help="Filter severity: CRITICAL or STANDARD")
    parser.add_argument("--json", "-j", action="store_true", dest="json_output",
                        help="Machine-readable JSON output")
    args = parser.parse_args()

    search(
        query=args.query,
        top_k=args.top,
        group_filter=args.group,
        severity_filter=args.severity,
        json_output=args.json_output,
    )


if __name__ == "__main__":
    main()
