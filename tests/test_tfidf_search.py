"""Smoke tests for TF-IDF search module."""

from pathlib import Path

from src.tfidf_search import search_classes, tokenize


def test_tokenize_drops_stopwords():
    assert "the" not in tokenize("the model hallucinates")


def test_search_jailbreak_returns_hits():
    """Uses repo data/search_index.json from test fixtures."""
    root = Path(__file__).resolve().parent.parent
    dd = root / "data"
    hits = search_classes("jailbreak prompt injection bypass", top_k=3, data_dir=dd)
    assert len(hits) >= 1
    assert all("id" in h and "score" in h for h in hits)
