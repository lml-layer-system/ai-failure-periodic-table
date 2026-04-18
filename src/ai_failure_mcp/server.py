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
from src.classifier import PeriodicTableClassifier
from src.tfidf_search import search_classes

mcp = FastMCP(
    "ai-failure-periodic-table",
    instructions=(
        "Personal scientific instrument: classify text/URL/documents against the 343-class ontology (read-only). "
        "Every classify_* and compound_hint returns fit_state (strong_fit | compound_fit | weak_fit | possible_gap_candidate), "
        "fit_confidence (high | medium | low), scientific_summary, boundary_pressure_note, CONTRIBUTING-grounded "
        "what_to_do_next / report_preparation for GitHub issue templates — not vendor runbooks. "
        "Structural fixes are WHAT (mechanism, forbidden, detection, mitigation) only. "
        "Freshness Watch is separate weekly repo maintenance; this server never edits the taxonomy."
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


@mcp.tool()
async def classify_text(text: str) -> str:
    """Classify free text against the periodic table. Returns fit_state, fit_confidence, scientific_summary, CONTRIBUTING-based report_preparation, plus keyword matches, semantic hits, dimensions, and suggested_structural_response (WHAT only—not implementation advice)."""
    if not (text or "").strip():
        return _dump({"error": "empty text"})
    clf, by_id = _ctx()
    return _dump(classification_bundle(clf, text.strip(), by_id=by_id))


@mcp.tool()
async def classify_url(url: str, max_content_chars: int = 120000) -> str:
    """Fetch an http(s) URL (HTML or plain text), extract readable text, then classify. Blocks localhost/private IPs. Suggested structural responses come only from the taxonomy."""
    try:
        raw = fetch_url_text(url)
    except Exception as e:
        return _dump({"error": str(e), "url": url})
    text = raw[: max(1000, max_content_chars)]
    clf, by_id = _ctx()
    bundle = classification_bundle(clf, text, by_id=by_id)
    bundle["source_url"] = url
    bundle["fetched_chars"] = len(raw)
    bundle["classified_chars"] = len(text)
    return _dump(bundle)


@mcp.tool()
async def classify_document(path: str, max_content_chars: int = 120000) -> str:
    """Read a UTF-8 file under the repository root or AI_FAILURE_MCP_DOCUMENT_ROOT / AI_FAILURE_MCP_DOCUMENT_ROOTS (extra absolute directories), then classify. Same scientific envelope as classify_text."""
    try:
        raw = read_document_text(path)
    except Exception as e:
        return _dump({"error": str(e), "path": path})
    text = raw[: max(1000, max_content_chars)]
    clf, by_id = _ctx()
    bundle = classification_bundle(clf, text, by_id=by_id)
    bundle["source_path"] = path
    bundle["read_chars"] = len(raw)
    bundle["classified_chars"] = len(text)
    return _dump(bundle)


@mcp.tool()
async def classify_document_path(path: str, max_content_chars: int = 120000) -> str:
    """Alias of classify_document for clients that want an explicit path-oriented name. Same security rules (repo + optional AI_FAILURE_MCP_DOCUMENT_ROOT[S])."""
    try:
        raw = read_document_text(path)
    except Exception as e:
        return _dump({"error": str(e), "path": path})
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
    """TF-IDF semantic search over class names, mechanisms, and examples. Each hit includes suggested_structural_response from the table."""
    if not (query or "").strip():
        return _dump({"error": "empty query"})
    try:
        hits = search_classes(query.strip(), top_k=min(25, max(1, top_k)), data_dir=data_dir())
    except FileNotFoundError as e:
        return _dump({"error": str(e)})
    _, by_id = _ctx()
    return _dump(semantic_search_bundle(query, hits, by_id=by_id))


@mcp.tool()
async def get_class(class_id: str) -> str:
    """Look up one failure class by ID (e.g. ADV-INDIRECT-INJECT-122). Returns full record, suggested_structural_response, and meta envelope (fit_state not_applicable — use classify_* to test narratives)."""
    _, by_id = _ctx()
    rec = class_lookup_bundle(class_id, by_id)
    if not rec:
        return _dump({"error": "unknown class id", "class_id": class_id})
    return _dump(rec)


@mcp.tool()
async def compound_hint(text: str) -> str:
    """Same scientific envelope as classify_text; biases toward compound_fit when multiple dimensions activate; adds compound_reading and consolidated structural mitigations (WHAT only)."""
    if not (text or "").strip():
        return _dump({"error": "empty text"})
    clf, by_id = _ctx()
    return _dump(compound_hint_bundle(clf, text.strip(), by_id=by_id))


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
