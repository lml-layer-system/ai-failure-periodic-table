"""
MCP server (stdio) — daily-driver layer: classify arbitrary text/URLs/docs against
the 343-class table. Read-only; never mutates repo data.

Requires: pip install "mcp>=1.2"
Run from repo root: python -m src.ai_failure_mcp
"""

from __future__ import annotations

import json
import logging
import os
import sys
from pathlib import Path
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
        "Freshness Watch is separate; this server never edits the taxonomy. "
        "Optional runtime enforcement: tool protection(yes|no|status) links to Agent Buccet as a second MCP server (buccet mcp); classify_* is classification only."
    ),
)

_classifier: PeriodicTableClassifier | None = None
_by_id: dict[str, dict[str, Any]] | None = None

# ── Protection setup state ────────────────────────────────────────────────────
# Asked once on first classify call. User can call protection() anytime to
# change — never locked.

_PROTECTION_SETUP_PATH = Path(os.path.expanduser("~/.ai-failure-periodic-table/setup.json"))


def _protection_setup_complete() -> bool:
    try:
        return "protection_choice" in json.loads(_PROTECTION_SETUP_PATH.read_text())
    except Exception:
        return False


def _save_protection_choice(choice: str) -> None:
    _PROTECTION_SETUP_PATH.parent.mkdir(parents=True, exist_ok=True)
    _PROTECTION_SETUP_PATH.write_text(json.dumps({"protection_choice": choice}, indent=2))


_PROTECTION_PROMPT = (
    "Do you want runtime protection? "
    "Call protection('yes') for Agent Buccet or protection('no') to skip / bring your own. "
    "This prompt won't appear again once you answer — "
    "but you can call protection() anytime to change your choice."
)


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
async def protection(choice: str) -> str:
    """
    Set or check runtime protection preference.

    The daily-driver (this server) is the eyes — classification and structural
    reading only. Runtime enforcement is a separate optional layer the user
    explicitly activates. This is asked once automatically on first classify call.
    The user can call this anytime to change — never locked.

    Args:
        choice: "yes"    — enable Agent Buccet (returns config + full CLI surface)
                "no"     — no protection, or bring your own enforcement runtime
                "status" — show current preference

    Agent Buccet runs in headless mode when activated via `buccet mcp` —
    no console needed, auto-initializes, silent boundary enforcement.
    Full CLI available for customization once running.
    """
    if choice == "status":
        if not _protection_setup_complete():
            return _dump({
                "protection_active": False,
                "question": (
                    "Do you want runtime protection? "
                    "Call protection('yes') for Agent Buccet or protection('no') to skip / bring your own. "
                    "You can change this anytime."
                ),
            })
        try:
            data = json.loads(_PROTECTION_SETUP_PATH.read_text())
        except Exception:
            data = {}
        return _dump({
            "protection_active": data.get("protection_choice") == "yes",
            "protection_choice": data.get("protection_choice"),
            "note": "Call protection('yes') or protection('no') anytime to change.",
        })

    if choice not in ("yes", "no"):
        return _dump_error({"error": "choice must be 'yes', 'no', or 'status'"})

    _save_protection_choice(choice)

    if choice == "yes":
        return _dump({
            "protection_active": True,
            "next_step": (
                "Add Agent Buccet to your MCP host config. "
                "It auto-initializes and runs in headless mode — "
                "no console needed, silent boundary enforcement from first connection."
            ),
            "config": {
                "mcpServers": {
                    "buccet": {
                        "command": "buccet",
                        "args": ["mcp"],
                    }
                }
            },
            "customize": (
                "Full CLI available once Buccet is running: "
                "`buccet console` — operator console, "
                "`buccet laws` — see your acceptance and denial pack, "
                "`buccet upl import <file>` — add your own rules, "
                "`buccet where` — full operator map."
            ),
            "upl_note": (
                "To make a classification result a standing rule: "
                "ask your AI to draft the UPL wording, "
                "you decide what goes in, place it via `buccet upl import`. "
                "Nothing is written automatically."
            ),
            "change_anytime": "Call protection('no') anytime to turn this off.",
        })

    return _dump({
        "protection_active": False,
        "note": (
            "No protection active. "
            "Add your enforcement runtime to your MCP host config whenever you're ready — "
            "Agent Buccet (`buccet mcp`) or any runtime of your choice."
        ),
        "change_anytime": "Call protection('yes') anytime to enable Agent Buccet.",
    })


@mcp.tool()
async def classify_text(text: str) -> str:
    """Run the repo keyword classifier on free text. Verdict: classifier_hit / in_table (sole acceptance gate). Includes response_contract, contributing_route, fit_state (verdict summary only), fit_evidence (semantic is advisory), dimensions, primary_classes_keyword, semantic_search_top, suggested_structural_response (WHAT only)."""
    if not (text or "").strip():
        return _dump_error({"error": "empty text"})
    clf, by_id = _ctx()
    bundle = classification_bundle(clf, text.strip(), by_id=by_id)
    if not _protection_setup_complete():
        bundle["_protection_prompt"] = _PROTECTION_PROMPT
    return _dump(bundle)


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
