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
import pathlib
import sys

# Repo root on path (same pattern as src.cli)
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.tfidf_search import search_classes  # noqa: E402

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

DATA_DIR = ROOT / "src" / "data"


def search(
    query: str,
    top_k: int = 5,
    group_filter: str | None = None,
    severity_filter: str | None = None,
    json_output: bool = False,
):
    try:
        results = search_classes(
            query,
            top_k=top_k,
            data_dir=DATA_DIR,
            group_filter=group_filter,
            severity_filter=severity_filter,
        )
    except FileNotFoundError as e:
        print(f"{RED}{e}{RESET}", file=sys.stderr)
        sys.exit(1)

    if not results:
        print(f"{RED}No indexed terms found in query.{RESET} Try different keywords.")
        sys.exit(1)

    if json_output:
        # Match previous CLI shape (examples field)
        enriched = []
        failures_data = json.loads((DATA_DIR / "failures.json").read_text(encoding="utf-8"))
        by_id = {f["id"]: f for f in failures_data["failures"]}
        for r in results:
            row = dict(r)
            row["examples"] = by_id.get(r["id"], {}).get("examples", "")
            enriched.append(row)
        print(json.dumps(enriched, indent=2))
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
    print(f"{DIM}Top {len(results)} results{RESET}\n")
    print("─" * 72)

    failures_data = json.loads((DATA_DIR / "failures.json").read_text(encoding="utf-8"))
    by_id = {f["id"]: f for f in failures_data["failures"]}

    for rank, r in enumerate(results, 1):
        fid = r["id"]
        f = by_id[fid]
        group = f.get("group", "")
        severity = f.get("severity", "STANDARD")
        gcol = GROUP_COLORS.get(group, "")
        scol = RED if severity == "CRITICAL" else ""
        sim = r["score"]

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

    idx = json.loads((DATA_DIR / "search_index.json").read_text(encoding="utf-8"))
    print("─" * 72)
    print(
        f"{DIM}TF-IDF index | {len(idx['vocab'])} terms | "
        f"{len(by_id)} classes{RESET}"
    )


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
        """,
    )
    parser.add_argument("query", help="Natural language search query")
    parser.add_argument(
        "--top",
        "-k",
        type=int,
        default=5,
        metavar="N",
        help="Number of results (default: 5)",
    )
    parser.add_argument(
        "--group",
        "-g",
        metavar="DIM",
        help="Filter dimension: EPISTEMIC/AGENTIC/ADVERSARIAL/ALIGNMENT/"
        "ARCHITECTURAL/DOMAIN/GOVERNANCE",
    )
    parser.add_argument(
        "--severity",
        "-s",
        metavar="LEVEL",
        help="Filter severity: CRITICAL or STANDARD",
    )
    parser.add_argument(
        "--json",
        "-j",
        action="store_true",
        dest="json_output",
        help="Machine-readable JSON output",
    )
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
