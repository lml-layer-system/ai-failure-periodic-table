"""
TF-IDF semantic search over failure classes (shared by CLI and Freshness Watch).

Pure stdlib. Default data paths use bundled `src/data` (git checkout or wheel).
"""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any

from src.taxonomy_paths import bundled_data_dir

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "this", "that", "these", "those", "it", "its",
    "as", "not", "no", "can", "via", "into", "which", "when", "than",
    "without", "using", "used", "such", "more", "other", "also", "any",
    "all", "each", "some", "if", "then", "even", "both", "their", "they",
    "them", "what", "how", "where", "who", "while", "after",
    "before", "about", "through",
}


def tokenize(text: str) -> list[str]:
    text = text.lower()
    tokens = re.findall(r"[a-z][a-z0-9\-]*[a-z0-9]|[a-z]", text)
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]


def _query_vec(
    query: str, vocab_index: dict[str, int], idf: list[float]
) -> dict[int, float]:
    tokens = tokenize(query)
    counts = Counter(tokens)
    if not counts:
        return {}
    max_c = max(counts.values())
    vec: dict[int, float] = {}
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


def _cosine(q_vec: dict[int, float], doc_vec: dict[int, float]) -> float:
    if len(q_vec) > len(doc_vec):
        q_vec, doc_vec = doc_vec, q_vec
    return sum(q_vec[k] * doc_vec.get(k, 0.0) for k in q_vec)


def load_search_index(data_dir: Path | None = None) -> dict[str, Any]:
    root = data_dir or bundled_data_dir()
    path = root / "search_index.json"
    if not path.exists():
        raise FileNotFoundError(
            f"search_index.json not found at {path}. Run: python scripts/generate_embeddings.py"
        )
    return json.loads(path.read_text(encoding="utf-8"))


def search_classes(
    query: str,
    top_k: int = 8,
    data_dir: Path | None = None,
    group_filter: str | None = None,
    severity_filter: str | None = None,
) -> list[dict[str, Any]]:
    """
    Return top_k failure classes by TF-IDF cosine similarity to `query`.
    Empty list if the query matches no indexed vocabulary terms.
    """
    root = data_dir or bundled_data_dir()
    idx = load_search_index(root)
    failures_path = root / "failures.json"
    failures_data = json.loads(failures_path.read_text(encoding="utf-8"))
    failures_by_id = {f["id"]: f for f in failures_data["failures"]}

    vocab = idx["vocab"]
    idf = idx["idf"]
    vectors = idx["vectors"]
    vocab_index = {term: i for i, term in enumerate(vocab)}

    q = _query_vec(query, vocab_index, idf)
    if not q:
        return []

    scores: list[tuple[float, str, dict]] = []
    for fid, doc_vec in vectors.items():
        doc_vec_int = {int(k): v for k, v in doc_vec.items()}
        failure = failures_by_id.get(fid)
        if not failure:
            continue
        if group_filter and failure.get("group", "").upper() != group_filter.upper():
            continue
        if (
            severity_filter
            and failure.get("severity", "STANDARD").upper() != severity_filter.upper()
        ):
            continue
        sim = _cosine(q, doc_vec_int)
        scores.append((sim, fid, failure))

    scores.sort(key=lambda x: -x[0])
    out: list[dict[str, Any]] = []
    for sim, fid, f in scores[:top_k]:
        out.append(
            {
                "id": fid,
                "name": f["name"],
                "group": f["group"],
                "severity": f.get("severity", "STANDARD"),
                "score": round(sim, 4),
                "mechanism": f.get("mechanism", ""),
            }
        )
    return out
