#!/usr/bin/env python3
"""
Generate TF-IDF search index for all 343 AI failure classes.

Zero external dependencies — uses Python stdlib only.
Produces a compact JSON index used by:
  - scripts/semantic_search.py  (CLI search)
  - index.html                  (in-browser search via embedded JS)

TF-IDF captures technical vocabulary extremely well for this domain:
searching "reward hacking reinforcement learning" or "model deceives evaluator"
returns the right classes via term-frequency weighting.

Run:
    python scripts/generate_embeddings.py

Output:
    src/data/search_index.json  — IDF weights + per-class TF vectors
    src/data/embeddings_meta.json — index metadata
"""

import json
import math
import pathlib
import re
from collections import Counter, defaultdict
from datetime import date

DATA_DIR = pathlib.Path(__file__).resolve().parent.parent / "src" / "data"
FAILURES_FILE = DATA_DIR / "failures.json"
INDEX_FILE = DATA_DIR / "search_index.json"
META_FILE = DATA_DIR / "embeddings_meta.json"

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
    """Lowercase, strip punctuation, remove stopwords, keep meaningful tokens."""
    text = text.lower()
    # Keep hyphens within words (e.g. "chain-of-thought"), strip the rest
    tokens = re.findall(r"[a-z][a-z0-9\-]*[a-z0-9]|[a-z]", text)
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]


def build_doc(failure: dict) -> str:
    """Combine all text fields into one rich document for indexing."""
    parts = [
        failure.get("name", ""),
        failure.get("group", ""),
        failure.get("mechanism", ""),
        failure.get("forbidden", ""),
        failure.get("detection", ""),
        failure.get("examples", ""),
    ]
    # Case study outcomes
    for cs in failure.get("case_studies", [])[:3]:
        if isinstance(cs, dict):
            parts.append(cs.get("outcome", ""))
            parts.append(cs.get("title", ""))
        elif isinstance(cs, str):
            parts.append(cs)
    # Keywords (already tokenized concepts — weight them extra by repeating)
    kw = failure.get("keywords", [])
    parts.extend(kw * 2)
    # References (author names, paper titles carry signal)
    for ref in failure.get("references", [])[:3]:
        parts.append(ref[:120])
    return " ".join(p for p in parts if p)


def compute_tf(tokens: list[str]) -> dict[str, float]:
    """Term frequency (log-normalized)."""
    counts = Counter(tokens)
    if not counts:
        return {}
    max_count = max(counts.values())
    return {term: count / max_count for term, count in counts.items()}


def main():
    print(f"Loading {FAILURES_FILE}...")
    d = json.loads(FAILURES_FILE.read_text())
    failures = d["failures"]
    N = len(failures)
    print(f"  {N} classes loaded")

    print("Tokenizing and building TF-IDF index...")

    # Step 1: tokenize all docs, collect vocabulary
    docs = []
    for f in failures:
        text = build_doc(f)
        tokens = tokenize(text)
        docs.append((f["id"], tokens))

    # Step 2: document frequency for IDF
    df = defaultdict(int)
    for _, tokens in docs:
        for term in set(tokens):
            df[term] += 1

    # Vocabulary: terms appearing in at least 2 docs and at most 80% of docs
    vocab = {
        term for term, count in df.items()
        if 2 <= count <= int(N * 0.8)
    }
    # Also keep all terms from class names and keywords (always include)
    for f in failures:
        for t in tokenize(f.get("name", "")):
            vocab.add(t)
        for kw in f.get("keywords", []):
            for t in tokenize(kw):
                vocab.add(t)

    vocab = sorted(vocab)
    vocab_index = {term: i for i, term in enumerate(vocab)}
    print(f"  Vocabulary size: {len(vocab)} terms")

    # Step 3: IDF weights
    idf = {}
    for term in vocab:
        idf[term] = math.log((N + 1) / (df.get(term, 0) + 1)) + 1.0

    # Step 4: TF-IDF vectors (sparse, as {term_index: tfidf_weight})
    vectors = {}
    for fid, tokens in docs:
        tf = compute_tf(tokens)
        vec = {}
        norm_sq = 0.0
        for term, tf_val in tf.items():
            if term in vocab_index:
                weight = tf_val * idf[term]
                vec[vocab_index[term]] = weight
                norm_sq += weight * weight
        # L2 normalize
        if norm_sq > 0:
            norm = math.sqrt(norm_sq)
            vec = {k: round(v / norm, 6) for k, v in vec.items()}
        vectors[fid] = vec

    # Step 5: Write index
    index = {
        "vocab": vocab,
        "idf": [round(idf[t], 6) for t in vocab],
        "vectors": vectors,
        "ids": [f["id"] for f in failures],
        "names": {f["id"]: f["name"] for f in failures},
        "groups": {f["id"]: f["group"] for f in failures},
        "severity": {f["id"]: f.get("severity", "STANDARD") for f in failures},
    }

    INDEX_FILE.write_text(json.dumps(index, separators=(",", ":")))
    size_kb = INDEX_FILE.stat().st_size // 1024

    meta = {
        "method": "TF-IDF",
        "vocab_size": len(vocab),
        "total_classes": N,
        "generated": str(date.today()),
        "index_file": str(INDEX_FILE),
        "text_fields_used": [
            "name", "group", "mechanism", "forbidden", "detection",
            "examples", "case_studies", "keywords", "references"
        ],
    }
    META_FILE.write_text(json.dumps(meta, indent=2))

    print(f"  Saved to {INDEX_FILE} ({size_kb}KB)")
    print(f"  Metadata: {META_FILE}")
    print(f"\nDone. Run semantic search with:")
    print(f"  python scripts/semantic_search.py \"model deceives evaluator\"")


if __name__ == "__main__":
    main()
