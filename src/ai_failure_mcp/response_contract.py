"""
Stable, machine-readable contract for MCP JSON payloads.

Clients should treat `verdict_applicable` and `verdict_authority` before interpreting
semantic / TF-IDF fields as ontology acceptance.
"""

from __future__ import annotations

from typing import Any, Literal

SCHEMA_VERSION = "1"

NonVerdictKind = Literal["semantic_search", "class_lookup"]


def classification_response_contract() -> dict[str, Any]:
    """Returned on classify_* and compound_hint (full narrative classification)."""
    return {
        "schema_version": SCHEMA_VERSION,
        "verdict_applicable": True,
        "verdict_authority": "periodic_table_keyword_classifier",
        "verdict_boolean_fields": ["classifier_hit", "in_table"],
        "verdict_field_equivalence": "classifier_hit is identical to in_table",
        "fit_state_role": "classifier_verdict_summary_only",
        "fit_confidence_role": "coarse_layer_on_classifier_verdict",
        "semantic_evidence_advisory_only": True,
        "advisory_semantic_paths": [
            "semantic_search_top",
            "fit_evidence.semantic_top_id",
            "fit_evidence.semantic_top_score",
            "fit_evidence.keyword_semantic_agreement",
            "fit_evidence.cross_modal_disagreement_advisory",
        ],
        "contributing_route_field": "contributing_route",
        "contributing_routing_ground": "CONTRIBUTING.md and .github/ISSUE_TEMPLATE/",
    }


def non_verdict_response_contract(*, response_kind: NonVerdictKind) -> dict[str, Any]:
    """Returned on search_failures and get_class — no keyword-classifier run on a narrative."""
    return {
        "schema_version": SCHEMA_VERSION,
        "verdict_applicable": False,
        "response_kind": response_kind,
        "instruction": (
            "Run classify_text, classify_url, or classify_document on the incident narrative "
            "to obtain classifier_hit, contributing_route, and fit_state."
        ),
    }


def error_response_contract() -> dict[str, Any]:
    """Attached to tool error payloads (empty input, I/O failure, unknown ID, etc.)."""
    return {
        "schema_version": SCHEMA_VERSION,
        "verdict_applicable": False,
        "error_response": True,
        "instruction": "Fix the error field; no classification verdict is present.",
    }
