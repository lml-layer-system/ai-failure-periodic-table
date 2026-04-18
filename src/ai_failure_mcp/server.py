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
    classification_bundle,
    compound_hint_bundle,
    data_dir,
    failures_path,
    fetch_url_text,
    get_class_record,
    load_failures_by_id,
    read_document_text,
    structural_fix,
)
from src.classifier import PeriodicTableClassifier
from src.tfidf_search import search_classes

mcp = FastMCP(
    "ai-failure-periodic-table",
    instructions=(
        "Tools map incidents and narratives to the AI Failure Periodic Table (343 classes). "
        "Outputs include taxonomy-native structural mitigations (mechanism, forbidden, detection, mitigation)—"
        "patterns and control principles from the table, not vendor-specific implementation steps."
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
    """Classify free text against the periodic table. Returns keyword matches, semantic hits, per-dimension signals, and suggested_structural_response (mitigation/forbidden/detection/mechanism) for each class—not implementation advice."""
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
    """Read a UTF-8 file under the repository root, then classify. Use a path relative to repo root or absolute within the repo."""
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
async def search_failures(query: str, top_k: int = 8) -> str:
    """TF-IDF semantic search over class names, mechanisms, and examples. Each hit includes suggested_structural_response from the table."""
    if not (query or "").strip():
        return _dump({"error": "empty query"})
    try:
        hits = search_classes(query.strip(), top_k=min(25, max(1, top_k)), data_dir=data_dir())
    except FileNotFoundError as e:
        return _dump({"error": str(e)})
    _, by_id = _ctx()
    out = []
    for h in hits:
        row = dict(h)
        fd = by_id.get(h["id"])
        if fd:
            row["suggested_structural_response"] = structural_fix(fd)
        out.append(row)
    return _dump({"query": query, "hits": out})


@mcp.tool()
async def get_class(class_id: str) -> str:
    """Look up one failure class by ID (e.g. ADV-INDIRECT-INJECT-122). Returns full record plus suggested_structural_response."""
    _, by_id = _ctx()
    rec = get_class_record(class_id, by_id)
    if not rec:
        return _dump({"error": "unknown class id", "class_id": class_id})
    return _dump(rec)


@mcp.tool()
async def compound_hint(text: str) -> str:
    """Same signals as classify_text, plus explicit compound-failure reading and a consolidated list of structural mitigations for top candidates across dimensions."""
    if not (text or "").strip():
        return _dump({"error": "empty text"})
    clf, by_id = _ctx()
    return _dump(compound_hint_bundle(clf, text.strip(), by_id=by_id))


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
