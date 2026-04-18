"""Tests for MCP bridge helpers (no mcp package required)."""

from pathlib import Path

import pytest

from src.ai_failure_mcp import bridge
from src.classifier import PeriodicTableClassifier


@pytest.fixture
def by_id():
    return bridge.load_failures_by_id()


def test_structural_fix_shape(by_id):
    f = by_id["ADV-INDIRECT-INJECT-122"]
    s = bridge.structural_fix(f)
    assert s["class_id"] == "ADV-INDIRECT-INJECT-122"
    assert s["structural_mitigation"]
    assert s["what"] == f["mechanism"]
    assert s["control_principle_forbidden"] == f["forbidden"]


def test_read_document_relative(by_id):
    p = "README.md"
    text = bridge.read_document_text(p)
    assert "AI Failure" in text or "Periodic" in text or len(text) > 50


def test_read_document_rejects_outside_repo():
    with pytest.raises(ValueError, match="repository root or a directory listed"):
        bridge.read_document_text("/etc/passwd")


def test_classification_bundle_contains_structural(by_id):
    clf = PeriodicTableClassifier(data_path=bridge.failures_path())
    b = bridge.classification_bundle(
        clf,
        "The attacker used prompt injection to exfiltrate the system prompt via markdown.",
        by_id=by_id,
    )
    assert b["in_table"]
    assert b["primary_classes_keyword"]
    first = b["primary_classes_keyword"][0]
    assert "suggested_structural_response" in first
    assert first["suggested_structural_response"]["structural_mitigation"]


def test_compound_hint_includes_mitigations(by_id):
    clf = PeriodicTableClassifier(data_path=bridge.failures_path())
    h = bridge.compound_hint_bundle(
        clf,
        "Jailbreak bypass safety then the agent leaked user data to an external URL.",
        by_id=by_id,
    )
    assert "compound_reading" in h
    assert h["structural_mitigations_for_top_candidates"]
    assert h["response_kind"] == "compound_classification"
    assert "fit_state" in h


def test_semantic_search_bundle_shape(by_id):
    hits = [{"id": "ADV-INDIRECT-INJECT-122", "name": "INDIRECT PROMPT INJECTION", "score": 0.42}]
    b = bridge.semantic_search_bundle("injection markdown", hits, by_id=by_id)
    assert b["response_kind"] == "semantic_search"
    assert b["fit_state"] == "not_applicable"
    assert b["hits"][0]["suggested_structural_response"]["class_id"] == "ADV-INDIRECT-INJECT-122"


def test_class_lookup_bundle(by_id):
    b = bridge.class_lookup_bundle("adv-indirect-inject-122", by_id)
    assert b is not None
    assert b["response_kind"] == "class_lookup"
    assert b["class"]["id"] == "ADV-INDIRECT-INJECT-122"


def test_read_document_extra_root(tmp_path, monkeypatch, by_id):
    outside = tmp_path / "notes"
    outside.mkdir()
    f = outside / "x.txt"
    f.write_text("reward hacking in RL from proxy metrics", encoding="utf-8")
    monkeypatch.setenv("AI_FAILURE_MCP_DOCUMENT_ROOT", str(outside))
    text = bridge.read_document_text(str(f))
    assert "reward hacking" in text
