"""
Read-only helpers for the AI Failure Periodic Table MCP server.

Surfaces taxonomy fields as structural mitigations (what / control principle / pattern),
not implementation or vendor-specific runbooks.
"""

from __future__ import annotations

import ipaddress
import os
import socket
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from src.classifier import FailureMatch, PeriodicTableClassifier
from src.data_loader import load_data
from src.freshness_feed import strip_html
from src.ai_failure_mcp.scientific_envelope import (
    ISSUE_CHALLENGE,
    ISSUE_IMPROVE_KEYWORDS,
    attach_scientific_surface,
)
from src.tfidf_search import search_classes

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def data_dir() -> Path:
    return REPO_ROOT / "data"


def failures_path() -> Path:
    return data_dir() / "failures.json"


def allowed_document_roots() -> list[Path]:
    """
    Repository root plus optional extra directories (absolute) from env:
    - AI_FAILURE_MCP_DOCUMENT_ROOT — single directory
    - AI_FAILURE_MCP_DOCUMENT_ROOTS — multiple paths, ':' or ';' separated
    Files passed to classify_document must resolve under one of these roots.
    """
    roots: list[Path] = [REPO_ROOT.resolve()]
    single = os.environ.get("AI_FAILURE_MCP_DOCUMENT_ROOT", "").strip()
    if single:
        p = Path(single).expanduser().resolve()
        if p.is_dir() and p not in roots:
            roots.append(p)
    multi = os.environ.get("AI_FAILURE_MCP_DOCUMENT_ROOTS", "").strip()
    if multi:
        sep = ";" if ";" in multi else ":"
        for part in multi.split(sep):
            q = Path(part.strip()).expanduser().resolve()
            if q.is_dir() and q not in roots:
                roots.append(q)
    return roots


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
    force_compound_hint: bool = False,
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

    out: dict[str, Any] = {
        "response_kind": "classification",
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
    attach_scientific_surface(
        out,
        result,
        sem_enriched=sem_enriched,
        primary_keyword_rows=primaries,
        force_compound_fit=force_compound_hint,
    )
    return out


def compound_hint_bundle(
    classifier: PeriodicTableClassifier,
    text: str,
    *,
    by_id: dict[str, dict],
) -> dict[str, Any]:
    """Highlight multi-dimension / multi-class readings with structural mitigations."""
    base = classification_bundle(classifier, text, by_id=by_id, force_compound_hint=True)
    base["response_kind"] = "compound_classification"
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
    """Read a UTF-8 document; path must resolve under repo root or AI_FAILURE_MCP_DOCUMENT_ROOT(S)."""
    p = Path(path_str).expanduser()
    if not p.is_absolute():
        p = (REPO_ROOT / p).resolve()
    else:
        p = p.resolve()
    roots = allowed_document_roots()
    allowed = False
    for root in roots:
        try:
            p.relative_to(root)
            allowed = True
            break
        except ValueError:
            continue
    if not allowed:
        raise ValueError(
            "Path must resolve inside the repository root or a directory listed in "
            "AI_FAILURE_MCP_DOCUMENT_ROOT or AI_FAILURE_MCP_DOCUMENT_ROOTS (absolute paths only there). "
            f"Checked roots: {[str(r) for r in roots]}"
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


def semantic_search_bundle(query: str, hits: list[dict], *, by_id: dict[str, dict]) -> dict[str, Any]:
    """Wrap TF-IDF search with the same meta fields as classify tools (where applicable)."""
    out_rows = []
    for h in hits:
        row = dict(h)
        fd = by_id.get(h["id"])
        if fd:
            row["suggested_structural_response"] = structural_fix(fd)
        out_rows.append(row)

    summary_txt = (
        "Semantic (TF-IDF) retrieval over class names, mechanisms, keywords, and examples — "
        "not a keyword-classifier verdict and not a fit_state for an incident description."
    )
    return {
        "response_kind": "semantic_search",
        "query": query,
        "hits": out_rows,
        "fit_state": "not_applicable",
        "fit_confidence": "not_applicable",
        "boundary_pressure_note": (
            "Use classify_text (or URL/document) to obtain fit_state / falsification against an input narrative. "
            "Search ranks classes by cosine similarity of indexed text."
        ),
        "what_to_do_next": (
            "Run classify_text on your incident narrative. If the classifier misses but search finds the right class, "
            "follow Improve Keywords (CONTRIBUTING §4). If the mechanism in the class record seems wrong, use Challenge Classification (§2)."
        ),
        "recommended_repo_action": {
            "issue_type": "none",
            "rationale": "Search-only response; pick a follow-up path after running full classification.",
            "contributing_section": "CONTRIBUTING.md — Ways to Contribute",
            "issue_template_relative_path": None,
            "summary": "none: run classify_* on your text, then use §2–§4 as needed.",
        },
        "report_preparation": {
            "recommended_issue_type": "none",
            "why_this_issue_type": "Semantic search does not decide ontology fit for a concrete input.",
            "issue_template_path": None,
            "closest_existing_classes": [
                {"id": r.get("id"), "name": r.get("name"), "score": r.get("score"), "why_near": "TF-IDF similarity"}
                for r in out_rows[:8]
            ],
            "questions_to_answer_before_reporting": [
                "Have you run classify_text on the same narrative?",
                "Is the miss a keyword problem (§4) or a structural class problem (§2)?",
            ],
            "suggested_report_inputs": {
                "next_step": "Use classify_text, then open Improve Keywords or Challenge Classification based on the gap.",
            },
            "boundary_context": summary_txt,
        },
        "scientific_summary": {
            "observed_mechanism_summary": summary_txt,
            "fit_state": "not_applicable",
            "fit_confidence": "not_applicable",
            "primary_reading": out_rows[0]["id"] + " — " + out_rows[0].get("name", "") if out_rows else None,
            "secondary_reading": None,
            "possible_gap": False,
            "recommended_structural_response_summary": (
                "Top hit structural pattern (WHAT): see first hit suggested_structural_response — "
                "mechanism, forbidden, detection, mitigation from the table only."
                if out_rows
                else "No hits."
            ),
            "what_to_do_next": "Run full classification on your source text for fit_state and CONTRIBUTING-guided next steps.",
            "recommended_repo_action": "none until classify_* is run on the incident narrative.",
            "uncertainty_notes": [],
        },
        "falsification_note": (
            "Search results are similarity-ranked candidates. A scientific test of the ontology requires classify_* "
            "on the same evidence you care about."
        ),
    }


def class_lookup_bundle(class_id: str, by_id: dict[str, dict]) -> dict[str, Any] | None:
    """Lookup one class with scientific/meta envelope (not a classification verdict)."""
    raw = get_class_record(class_id, by_id)
    if not raw:
        return None
    f = raw["class"]
    cid, name = f["id"], f["name"]
    ssr = raw["suggested_structural_response"]
    return {
        **raw,
        "response_kind": "class_lookup",
        "fit_state": "not_applicable",
        "fit_confidence": "not_applicable",
        "fit_evidence": {"mode": "direct_id_lookup", "class_id": cid},
        "boundary_pressure_note": (
            "This is a taxonomy record lookup — no free-text incident was classified. "
            "Structural fields describe the class as stored, not whether your scenario matches."
        ),
        "what_to_do_next": (
            "To test a scenario, use classify_text / classify_url / classify_document. "
            "If the stored mechanism/forbidden/detection for this ID is wrong, open Challenge Classification "
            f"({ISSUE_CHALLENGE}, CONTRIBUTING §2). If keywords fail to reach this ID from your wording, use Improve Keywords (§4)."
        ),
        "recommended_repo_action": {
            "issue_type": "none",
            "rationale": "Lookup only; challenge or keyword issues require a concrete incident description.",
            "contributing_section": "CONTRIBUTING.md — Ways to Contribute",
            "issue_template_relative_path": None,
            "summary": f"none: classify your narrative, then §2 ({ISSUE_CHALLENGE}) or §4 ({ISSUE_IMPROVE_KEYWORDS}) as appropriate.",
        },
        "report_preparation": {
            "recommended_issue_type": "none",
            "why_this_issue_type": "No input narrative classified.",
            "issue_template_path": None,
            "closest_existing_classes": [
                {
                    "id": cid,
                    "name": name,
                    "why_near": "Explicit ID lookup",
                }
            ],
            "questions_to_answer_before_reporting": [
                "What incident text are you testing?",
                "Does the mismatch concern keywords (§4) or the class definition itself (§2)?",
            ],
            "suggested_report_inputs": {
                "challenge_classification": (
                    f"If the class record is structurally wrong: {ISSUE_CHALLENGE} — what_is_wrong, class_or_group_target, structural_reason."
                ),
                "improve_keywords": (
                    f"If retrieval misses this ID: {ISSUE_IMPROVE_KEYWORDS} — input, expected ID, suggested keywords."
                ),
            },
            "boundary_context": f"Looked up {cid} ({name}).",
        },
        "scientific_summary": {
            "observed_mechanism_summary": f"Record for {cid}: {f.get('mechanism', '')[:280]}",
            "fit_state": "not_applicable",
            "fit_confidence": "not_applicable",
            "primary_reading": f"{cid} — {name}",
            "secondary_reading": None,
            "possible_gap": False,
            "recommended_structural_response_summary": (
                f"WHAT: {ssr.get('what', '')[:200]}…; forbidden principle; detection; mitigation — see suggested_structural_response."
            ),
            "what_to_do_next": "Classify incident text to test fit; use §2/§4 only with a concrete narrative.",
            "recommended_repo_action": f"none — or §2 / §4 after classify_* on your text.",
            "uncertainty_notes": [],
        },
        "falsification_note": (
            "A class record is not evidence that your scenario instantiates it — run classify_* on the scenario text."
        ),
    }
