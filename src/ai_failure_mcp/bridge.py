"""
Read-only helpers for the AI Failure Periodic Table MCP server.

Surfaces taxonomy fields as structural mitigations (what / control principle / pattern),
not implementation or vendor-specific runbooks.
"""

from __future__ import annotations

import ipaddress
import socket
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from src.classifier import FailureMatch, PeriodicTableClassifier
from src.data_loader import load_data
from src.freshness_feed import strip_html
from src.tfidf_search import search_classes

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def data_dir() -> Path:
    return REPO_ROOT / "data"


def failures_path() -> Path:
    return data_dir() / "failures.json"


def structural_fix(f: dict[str, Any]) -> dict[str, Any]:
    """
    Taxonomy-native structural response: mechanism, constraints, detection pattern,
    and mitigation as stored in failures.json (no stack-specific how-to).
    """
    return {
        "class_id": f["id"],
        "name": f["name"],
        "group": f["group"],
        "severity": f.get("severity", "STANDARD"),
        "what": f.get("mechanism", ""),
        "control_principle_forbidden": f.get("forbidden", ""),
        "detection_pattern": f.get("detection", ""),
        "structural_mitigation": f.get("mitigation", ""),
        **(
            {"mitigation_domain": f["mit_domain"]}
            if f.get("mit_domain")
            else {}
        ),
    }


def enrich_match(m: FailureMatch, by_id: dict[str, dict]) -> dict[str, Any]:
    row = m.as_dict()
    fd = by_id.get(m.failure_id)
    if fd:
        row["suggested_structural_response"] = structural_fix(fd)
    return row


def classification_bundle(
    classifier: PeriodicTableClassifier,
    text: str,
    *,
    by_id: dict[str, dict],
) -> dict[str, Any]:
    result = classifier.classify(text)
    sem = []
    try:
        sem = search_classes(text, top_k=8, data_dir=data_dir())
    except FileNotFoundError:
        sem = []

    primaries = [enrich_match(m, by_id) for m in result.matches[:8]]
    secondaries_kw = [enrich_match(m, by_id) for m in result.matches[1:6]]
    closest = [enrich_match(m, by_id) for m in result.closest[:3]]

    sem_enriched = []
    for h in sem[:8]:
        fd = by_id.get(h["id"])
        entry = dict(h)
        if fd:
            entry["suggested_structural_response"] = structural_fix(fd)
        sem_enriched.append(entry)

    dims_out = []
    for d in result.dimensions:
        block: dict[str, Any] = {
            "question_number": d.question_number,
            "group_code": d.group_code,
            "question": d.question,
            "activated": d.activated,
            "top_score": round(d.top_score, 4),
        }
        if d.top_match:
            block["top_class"] = enrich_match(d.top_match, by_id)
        dims_out.append(block)

    return {
        "in_table": result.in_table,
        "verdict": result.verdict,
        "dimensions": dims_out,
        "primary_classes_keyword": primaries,
        "secondary_classes_keyword": secondaries_kw,
        "semantic_search_top": sem_enriched,
        "closest_if_not_in_table": closest,
        "execution_time_ms": round(result.execution_time_ms, 3),
        "note": (
            "Suggested structural response fields come from the periodic table only "
            "(mechanism, forbidden, detection, mitigation). They describe what to enforce "
            "and at what layer—not vendor-specific implementation steps."
        ),
    }


def compound_hint_bundle(
    classifier: PeriodicTableClassifier,
    text: str,
    *,
    by_id: dict[str, dict],
) -> dict[str, Any]:
    """Highlight multi-dimension / multi-class readings with structural mitigations."""
    base = classification_bundle(classifier, text, by_id=by_id)
    activated = [d for d in base["dimensions"] if d["activated"]]
    act_groups = [d["group_code"] for d in activated]

    per_dim_top: list[dict[str, Any]] = []
    for d in activated:
        if d.get("top_class"):
            per_dim_top.append(d["top_class"])

    # Unique class IDs preserving order
    seen: set[str] = set()
    unique_structural: list[dict[str, Any]] = []
    for item in per_dim_top + base["primary_classes_keyword"]:
        cid = item.get("id") or item.get("class_id")
        if not cid or cid in seen:
            continue
        seen.add(cid)
        ssr = item.get("suggested_structural_response")
        if ssr:
            unique_structural.append(ssr)

    reading_parts = []
    if len(act_groups) >= 2:
        reading_parts.append(
            f"Multiple structural dimensions score above threshold ({', '.join(act_groups)}). "
            "Treat as a compound failure: one primary mechanism class for reporting, "
            "plus explicit secondary classes for each additional dimension that fires strongly."
        )
    elif len(base["primary_classes_keyword"]) >= 2:
        reading_parts.append(
            "Several classes exceed the keyword threshold; prefer the highest-scoring as primary "
            "and list others as secondaries if the narrative clearly combines mechanisms."
        )
    else:
        reading_parts.append(
            "Single-dimension signal dominant; use primary class from keyword matches unless "
            "semantic search strongly disagrees—in that case, reconcile by re-reading mechanism text."
        )

    return {
        **base,
        "compound_reading": " ".join(reading_parts),
        "activated_dimension_count": len(activated),
        "structural_mitigations_for_top_candidates": unique_structural[:12],
    }


def _host_blocked(host: str) -> bool:
    h = host.lower().strip(".")
    if h in ("localhost", "127.0.0.1", "::1", "0.0.0.0"):
        return True
    try:
        for res in socket.getaddrinfo(host, None):
            ip_str = res[4][0]
            ip = ipaddress.ip_address(ip_str)
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                return True
    except (OSError, ValueError):
        pass
    return False


def fetch_url_text(url: str, *, max_bytes: int = 500_000, timeout: int = 25) -> str:
    p = urlparse(url.strip())
    if p.scheme not in ("http", "https"):
        raise ValueError("Only http(s) URLs are allowed.")
    host = p.hostname
    if not host or _host_blocked(host):
        raise ValueError("URL host is not allowed (localhost / private / link-local).")

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "AIFailurePeriodicTable-MCP/1.0 (+read-only classifier)",
            "Accept": "text/html,application/xhtml+xml,text/plain;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read(max_bytes + 1)
        charset = resp.headers.get_content_charset() or "utf-8"
    if len(raw) > max_bytes:
        raw = raw[:max_bytes]
    text = raw.decode(charset, errors="replace")
    return strip_html(text)


def read_document_text(path_str: str) -> str:
    """Read a UTF-8 document; path must resolve inside the repository root."""
    p = Path(path_str).expanduser()
    if not p.is_absolute():
        p = (REPO_ROOT / p).resolve()
    else:
        p = p.resolve()
    root = REPO_ROOT.resolve()
    try:
        p.relative_to(root)
    except ValueError:
        raise ValueError(
            f"Path must be inside repository root {root}. "
            "Copy the document into the workspace or use a relative path from repo root."
        ) from None
    if not p.is_file():
        raise ValueError(f"Not a file: {p}")
    return p.read_text(encoding="utf-8", errors="replace")


def load_failures_by_id() -> dict[str, dict]:
    data = load_data(failures_path())
    return {f["id"]: f for f in data["failures"]}


def get_class_record(class_id: str, by_id: dict[str, dict]) -> dict[str, Any] | None:
    key = class_id.strip().upper()
    for fid, f in by_id.items():
        if fid.upper() == key:
            out = {
                "class": f,
                "suggested_structural_response": structural_fix(f),
            }
            return out
    return None
