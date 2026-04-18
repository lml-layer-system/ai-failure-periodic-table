"""
MCP server (stdio) — daily-driver layer: classify arbitrary text/URLs/docs against
the 343-class table. Read-only; never mutates repo data.

Requires: pip install "mcp>=1.2"
Run from repo root: python -m src.ai_failure_mcp
"""

from __future__ import annotations

import json
import logging
import sys
from typing import Any

# Stdio transport must not write to stdout (JSON-RPC uses it).
logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
log = logging.getLogger(__name__)

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as e:  # pragma: no cover
    raise SystemExit(
        "The 'mcp' package is required. Install with: pip install 'mcp>=1.2'\n"
        f"Original error: {e}"
    ) from e

from src.ai_failure_mcp.bridge import (
    class_lookup_bundle,
    classification_bundle,
    compound_hint_bundle,
    data_dir,
    failures_path,
    fetch_url_text,
    load_failures_by_id,
    read_document_text,
    semantic_search_bundle,
)
from src.ai_failure_mcp.response_contract import error_response_contract
from src.classifier import PeriodicTableClassifier
from src.tfidf_search import search_classes

mcp = FastMCP(
    "ai-failure-periodic-table",
    instructions=(
        "Read-only scientific instrument: classify narratives against the 343-class periodic table. "
        "Authoritative ontology verdict: periodic_table_keyword_classifier only — classifier_hit equals in_table. "
        "TF-IDF / semantic_search_top and fit_evidence semantic fields are advisory; they never override classifier_hit. "
        "Every JSON payload includes response_contract (schema_version, verdict_applicable, roles of fit_state and semantic paths). "
        "classify_* and compound_hint: contributing_route + CONTRIBUTING-grounded report_preparation. "
        "search_failures and get_class: verdict_applicable false — run classify_* on your narrative for a verdict. "
        "Structural fields are WHAT (mechanism, forbidden, detection, mitigation) only. "
        "Freshness Watch is separate; this server never edits the taxonomy."
    ),
)

_classifier: PeriodicTableClassifier | None = None
_by_id: dict[str, dict[str, Any]] | None = None


def _ctx() -> tuple[PeriodicTableClassifier, dict[str, dict[str, Any]]]:
    global _classifier, _by_id
    if _classifier is None:
        _classifier = PeriodicTableClassifier(data_path=failures_path())
    if _by_id is None:
        _by_id = load_failures_by_id()
    return _classifier, _by_id


def _dump(obj: Any) -> str:
    return json.dumps(obj, indent=2)


def _dump_error(payload: dict[str, Any]) -> str:
    """Errors still carry response_contract so clients never misread a failed call as a verdict."""
    body = dict(payload)
    body.setdefault("response_contract", error_response_contract())
    return json.dumps(body, indent=2)


@mcp.tool()
async def classify_text(text: str) -> str:
    """Run the repo keyword classifier on free text. Verdict: classifier_hit / in_table (sole acceptance gate). Includes response_contract, contributing_route, fit_state (verdict summary only), fit_evidence (semantic is advisory), dimensions, primary_classes_keyword, semantic_search_top, suggested_structural_response (WHAT only)."""
    if not (text or "").strip():
        return _dump_error({"error": "empty text"})
    clf, by_id = _ctx()
    return _dump(classification_bundle(clf, text.strip(), by_id=by_id))


@mcp.tool()
async def classify_url(url: str, max_content_chars: int = 120000) -> str:
    """Fetch http(s) public URL, extract readable text, classify with the same bundle as classify_text. Blocks localhost/private IPs; structural fields from taxonomy only."""
    try:
        raw = fetch_url_text(url)
    except Exception as e:
        return _dump_error({"error": str(e), "url": url})
    text = raw[: max(1000, max_content_chars)]
    clf, by_id = _ctx()
    bundle = classification_bundle(clf, text, by_id=by_id)
    bundle["source_url"] = url
    bundle["fetched_chars"] = len(raw)
    bundle["classified_chars"] = len(text)
    return _dump(bundle)


@mcp.tool()
async def classify_document(path: str, max_content_chars: int = 120000) -> str:
    """Read UTF-8 file under repo root and/or AI_FAILURE_MCP_DOCUMENT_ROOT(S), then classify. Same envelope as classify_text (response_contract, classifier_hit, contributing_route)."""
    try:
        raw = read_document_text(path)
    except Exception as e:
        return _dump_error({"error": str(e), "path": path})
    text = raw[: max(1000, max_content_chars)]
    clf, by_id = _ctx()
    bundle = classification_bundle(clf, text, by_id=by_id)
    bundle["source_path"] = path
    bundle["read_chars"] = len(raw)
    bundle["classified_chars"] = len(text)
    return _dump(bundle)


@mcp.tool()
async def classify_document_path(path: str, max_content_chars: int = 120000) -> str:
    """Alias of classify_document. Same security rules and full classification response_contract."""
    try:
        raw = read_document_text(path)
    except Exception as e:
        return _dump_error({"error": str(e), "path": path})
    text = raw[: max(1000, max_content_chars)]
    clf, by_id = _ctx()
    bundle = classification_bundle(clf, text, by_id=by_id)
    bundle["source_path"] = path
    bundle["read_chars"] = len(raw)
    bundle["classified_chars"] = len(text)
    bundle["tool"] = "classify_document_path"
    return _dump(bundle)


@mcp.tool()
async def search_failures(query: str, top_k: int = 8) -> str:
    """TF-IDF retrieval over indexed class text — similarity only, not a keyword-classifier verdict. response_contract.verdict_applicable is false; run classify_* on your narrative for classifier_hit and contributing_route. Hits include suggested_structural_response (WHAT)."""
    if not (query or "").strip():
        return _dump_error({"error": "empty query"})
    try:
        hits = search_classes(query.strip(), top_k=min(25, max(1, top_k)), data_dir=data_dir())
    except FileNotFoundError as e:
        return _dump_error({"error": str(e)})
    _, by_id = _ctx()
    return _dump(semantic_search_bundle(query, hits, by_id=by_id))


@mcp.tool()
async def get_class(class_id: str) -> str:
    """Lookup one class record by ID. response_contract.verdict_applicable is false — no narrative was classified. Use classify_* to obtain classifier_hit for your text."""
    _, by_id = _ctx()
    rec = class_lookup_bundle(class_id, by_id)
    if not rec:
        return _dump_error({"error": "unknown class id", "class_id": class_id})
    return _dump(rec)


@mcp.tool()
async def compound_hint(text: str) -> str:
    """Same classification pipeline and response_contract as classify_text; when multiple dimensions activate, encourages compound_fit and adds compound_reading plus consolidated structural mitigations (WHAT only). classifier_hit remains the keyword classifier verdict."""
    if not (text or "").strip():
        return _dump_error({"error": "empty text"})
    clf, by_id = _ctx()
    return _dump(compound_hint_bundle(clf, text.strip(), by_id=by_id))


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
