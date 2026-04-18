"""
Scientific / falsification-oriented layer for MCP classify outputs.

Grounds next-step guidance in CONTRIBUTING.md issue paths — no taxonomy edits.
"""

from __future__ import annotations

from typing import Any, Literal

from src.classifier import ClassificationResult, PeriodicTableClassifier
from src.ai_failure_mcp.response_contract import classification_response_contract

# Issue templates (paths relative to repo root) — mirror CONTRIBUTING.md
ISSUE_PROPOSE_NEW_CLASS = ".github/ISSUE_TEMPLATE/propose_new_class.md"
ISSUE_CHALLENGE = ".github/ISSUE_TEMPLATE/challenge_classification.md"
ISSUE_REAL_INCIDENT = ".github/ISSUE_TEMPLATE/report_real_incident.md"
ISSUE_IMPROVE_KEYWORDS = ".github/ISSUE_TEMPLATE/improve_keywords.md"

FitState = Literal["strong_fit", "compound_fit", "weak_fit", "possible_gap_candidate"]
FitConfidence = Literal["high", "medium", "low"]
IssueType = Literal[
    "propose_new_class",
    "challenge_classification",
    "report_real_incident",
    "improve_keywords",
    "none",
]

_TH = PeriodicTableClassifier.THRESHOLD
_GTH = PeriodicTableClassifier.GROUP_THRESHOLD
# In-table “strong” = clearly above the same bar the classifier uses to accept a match.
_STRONG_SCORE = _TH * 2.0
# Below threshold but still a neighbour worth citing (same scale as keyword scores).
_NEAR_NEIGHBOR = max(_GTH, _TH * 0.45)


def _top_sem(sem_enriched: list[dict]) -> tuple[str | None, float]:
    if not sem_enriched:
        return None, 0.0
    h = sem_enriched[0]
    return h.get("id"), float(h.get("score") or 0)


def derive_fit_state_and_confidence(
    result: ClassificationResult,
    *,
    sem_enriched: list[dict],
    primary_keyword_rows: list[dict],
) -> tuple[FitState, FitConfidence, dict[str, Any]]:
    """
    Map fit_state / fit_confidence from the periodic-table classifier verdict only
    (in_table, match scores, activated dimensions). Semantic search is recorded in
    fit_evidence for context, not used to override the classifier hit/miss.
    """
    sem_id, sem_score = _top_sem(sem_enriched)
    kw_rows = primary_keyword_rows
    top_kw = float(kw_rows[0]["score"]) if kw_rows else 0.0
    second_kw = float(kw_rows[1]["score"]) if len(kw_rows) > 1 else 0.0
    kw_top_id = kw_rows[0].get("id") if kw_rows else None

    activated_dims = [d for d in result.dimensions if d.activated]
    n_act = len(activated_dims)
    dim_scores = [round(d.top_score, 4) for d in activated_dims]

    agreement = bool(kw_top_id and sem_id and (kw_top_id == sem_id))
    cross_modal_disagreement = bool(
        kw_top_id and sem_id and kw_top_id != sem_id and top_kw >= _TH and sem_score >= _GTH
    )

    top_match = float(result.matches[0].score) if result.matches else 0.0
    compound = n_act >= 2

    closest_s = float(result.closest[0].score) if result.closest else 0.0
    classifier_hit = bool(result.in_table)

    evidence: dict[str, Any] = {
        "classifier_hit": classifier_hit,
        "classifier_threshold": _TH,
        "classifier_group_threshold": _GTH,
        "classifier_top_match_score": round(top_match, 4),
        "classifier_nearest_below_threshold_score": round(closest_s, 4),
        "classifier_plausible_neighbour": bool(not classifier_hit and closest_s >= _NEAR_NEIGHBOR),
        "keyword_top_score": round(top_kw, 4),
        "keyword_second_score": round(second_kw, 4),
        "semantic_top_id": sem_id,
        "semantic_top_score": round(sem_score, 4),
        "keyword_semantic_agreement": agreement,
        "cross_modal_disagreement_advisory": cross_modal_disagreement,
        "activated_dimension_count": n_act,
        "activated_dimension_top_scores": dim_scores,
    }

    if not classifier_hit:
        state: FitState = "possible_gap_candidate"
        conf: FitConfidence = "low"
        return state, conf, evidence

    if compound:
        conf = "high" if top_match >= _STRONG_SCORE else "medium"
        return "compound_fit", conf, evidence

    if top_match >= _STRONG_SCORE:
        return "strong_fit", "high", evidence

    return "weak_fit", "medium", evidence


def _contributing_checklist_bullets() -> list[str]:
    return [
        "Can this failure be explained as a sub-mode of an existing class?",
        "Can this failure be explained as a compound of 2–3 existing classes?",
        "Does this failure violate an operational invariant not already covered by the 7 dimensions?",
        "Is this a new mechanism or only a new cause, substrate, or wrapper around an existing mechanism?",
    ]


def boundary_and_repo_action(
    fit_state: FitState,
    fit_confidence: FitConfidence,
    result: ClassificationResult,
    *,
    sem_enriched: list[dict],
    primary_keyword_rows: list[dict],
) -> tuple[str, str, IssueType, str]:
    """
    Returns (boundary_pressure_note, what_to_do_next, recommended_issue_type, why_issue_type).
    Branches on the classifier hit (in_table) first, then CONTRIBUTING.md paths — not on a parallel scorer.
    """
    sem_id, _sem_score = _top_sem(sem_enriched)
    kw_top_id = primary_keyword_rows[0].get("id") if primary_keyword_rows else None

    # --- Classifier miss: repo-native CONTRIBUTING flow (§1 / §3 / propose / keywords as applicable)
    if not result.in_table:
        closest_s = float(result.closest[0].score) if result.closest else 0.0
        near = closest_s >= _NEAR_NEIGHBOR
        note = (
            f"The periodic-table classifier did not accept any class (keyword bar ≥ {_TH}). "
            "Closest rows are still listed below threshold; that is a miss on the table’s own rules, not a second opinion."
        )
        if near:
            note += (
                " Scores on closest neighbours are high enough that a real incident report with those IDs is "
                "especially useful."
            )
        nxt = (
            "Follow CONTRIBUTING.md in order: if this is a **real public incident**, use Report Real Incident (§3) "
            "and cite closest class IDs even when none pass the bar. Work the §1 checklist (sub-mode → compound → "
            "invariant → mechanism vs cause). If the mechanism still looks new after that, use Propose New Class. "
            "If you believe a listed class should have matched, use Improve Keywords (§4)."
        )
        if near:
            return note, nxt, "report_real_incident", (
                "Classifier miss with plausible neighbours: CONTRIBUTING §3 + §1; incident evidence is prioritized."
            )
        return note, nxt, "propose_new_class", (
            "Classifier miss with weak neighbours: CONTRIBUTING §1 burden of proof for a new class after checklist."
        )

    # --- Classifier hit: interpret strength from the same match / dimension signals
    if fit_state == "compound_fit":
        note = (
            "The classifier accepted matches and activated multiple structural dimensions. CONTRIBUTING treats that "
            "as a compound reading: one primary mechanism class plus explicit secondaries."
        )
        nxt = (
            "Before proposing a new class, confirm the narrative is not reducible to 2–3 existing classes "
            "(CONTRIBUTING §1 checklist). If it is a real incident, Report Real Incident with primary + secondary IDs (§3)."
        )
        return note, nxt, "report_real_incident", (
            "CONTRIBUTING §3: combined mechanisms should name primary and secondary classes."
        )

    if fit_state == "strong_fit":
        note = (
            "The classifier accepted at least one class with a score well above its acceptance bar; dimensional "
            "evidence does not force a compound reading."
        )
        nxt = (
            "No mandatory repo action for taxonomy structure. Optionally file Report Real Incident (§3) for a real "
            "public example. If the assigned class feels structurally wrong, Challenge Classification (§2); if the "
            "class is right but wording failed to reach it, Improve Keywords (§4)."
        )
        return note, nxt, "none", (
            "Classifier hit with clear primary: default issue_type none per CONTRIBUTING."
        )

    # weak in-table hit
    disagree_hint = ""
    if kw_top_id and sem_id and kw_top_id != sem_id:
        disagree_hint = (
            " Semantic search’s top ID differs from the keyword primary; treat that as a hint to re-read both "
            "classes, not as an alternate classifier verdict."
        )
    note = (
        "The classifier accepted a match, but the top score is only modestly above the acceptance bar — treat the "
        "mapping as provisional."
        + disagree_hint
    )
    nxt = (
        "Default CONTRIBUTING path: Improve Keywords (§4) with exact input text, expected class ID, and suggested "
        "tokens. If you believe the table’s mechanism assignment is wrong, use Challenge Classification (§2). "
        "If the case still seems outside the 343 classes after tightening keywords, work §1 then Propose New Class."
    )
    return note, nxt, "improve_keywords", (
        "Classifier hit but marginal: CONTRIBUTING §4 first; §2 if structure is wrong."
    )


def build_report_preparation(
    recommended_issue_type: IssueType,
    *,
    why_issue_type: str,
    closest_classes: list[dict[str, Any]],
    primary_classes: list[dict[str, Any]],
    boundary_pressure_note: str,
) -> dict[str, Any]:
    """Structured prompts so another AI can draft the correct GitHub issue."""
    closest_existing = []
    for row in closest_classes[:6]:
        closest_existing.append(
            {
                "id": row.get("id"),
                "name": row.get("name"),
                "score": row.get("score"),
                "why_near": "Below keyword threshold but highest stem overlap / semantic neighbour.",
            }
        )
    for row in primary_classes[:4]:
        if row.get("id") in {c["id"] for c in closest_existing}:
            continue
        closest_existing.insert(
            0,
            {
                "id": row.get("id"),
                "name": row.get("name"),
                "score": row.get("score"),
                "why_near": "Primary keyword-threshold match from periodic table classifier.",
            },
        )

    base_questions = _contributing_checklist_bullets()

    prep: dict[str, Any] = {
        "recommended_issue_type": recommended_issue_type,
        "why_this_issue_type": why_issue_type,
        "issue_template_path": None,
        "closest_existing_classes": closest_existing,
        "questions_to_answer_before_reporting": base_questions,
        "suggested_report_inputs": {},
    }

    if recommended_issue_type == "propose_new_class":
        prep["issue_template_path"] = ISSUE_PROPOSE_NEW_CLASS
        prep["suggested_report_inputs"] = {
            "natural_language_description": "Clear description of the failure behavior.",
            "operational_invariant_violated": "What constraint or invariant is broken?",
            "why_not_reducible": "Specific class IDs considered and why they are insufficient.",
            "examples": "At least one real or concrete hypothetical example (CONTRIBUTING §1).",
        }
    elif recommended_issue_type == "report_real_incident":
        prep["issue_template_path"] = ISSUE_REAL_INCIDENT
        prep["suggested_report_inputs"] = {
            "incident_summary": "Brief description using public information only.",
            "primary_and_secondary_classes": "IDs + why they apply, or closest IDs + why none fit perfectly.",
            "public_source_or_reference": "Citation or link if documented.",
        }
    elif recommended_issue_type == "improve_keywords":
        prep["issue_template_path"] = ISSUE_IMPROVE_KEYWORDS
        prep["suggested_report_inputs"] = {
            "input_description_that_failed": "Exact text that should match.",
            "expected_class_id_and_name": "The class you believe should fire.",
            "suggested_keywords_or_phrases": "Tokens that would connect description to that class.",
        }
    elif recommended_issue_type == "challenge_classification":
        prep["issue_template_path"] = ISSUE_CHALLENGE
        prep["suggested_report_inputs"] = {
            "what_is_wrong": "Structural issue (group, mechanism, severity, redundancy, etc.).",
            "class_or_group_target": "IDs or names being challenged.",
            "structural_reason": "Why this is a taxonomy structure problem vs wording preference.",
        }
    elif recommended_issue_type == "none":
        prep["issue_template_path"] = None
        prep["suggested_report_inputs"] = {
            "optional_report_real_incident": (
                "If documenting a concrete public event, use template "
                + ISSUE_REAL_INCIDENT
                + " per CONTRIBUTING §3."
            ),
            "if_fit_seems_wrong": "Challenge Classification (§2) for structural errors; Improve Keywords (§4) if wording failed to reach the right class.",
        }
    else:
        prep["recommended_issue_type"] = "none"
        prep["issue_template_path"] = None
        prep["suggested_report_inputs"] = {
            "optional_follow_up": "See CONTRIBUTING.md Ways to Contribute."
        }

    prep["boundary_context"] = boundary_pressure_note
    return prep


def build_scientific_summary(
    *,
    observed_mechanism_summary: str,
    fit_state: FitState,
    fit_confidence: FitConfidence,
    primary_reading: str | None,
    secondary_reading: str | None,
    possible_gap: bool,
    recommended_structural_response_summary: str,
    what_to_do_next: str,
    recommended_repo_action: str,
    uncertainty_notes: list[str],
) -> dict[str, Any]:
    return {
        "observed_mechanism_summary": observed_mechanism_summary,
        "fit_state": fit_state,
        "fit_confidence": fit_confidence,
        "primary_reading": primary_reading,
        "secondary_reading": secondary_reading,
        "possible_gap": possible_gap,
        "recommended_structural_response_summary": recommended_structural_response_summary,
        "what_to_do_next": what_to_do_next,
        "recommended_repo_action": recommended_repo_action,
        "uncertainty_notes": uncertainty_notes,
    }


def attach_scientific_surface(
    bundle: dict[str, Any],
    result: ClassificationResult,
    *,
    sem_enriched: list[dict],
    primary_keyword_rows: list[dict],
    force_compound_fit: bool = False,
) -> None:
    """Mutates bundle in place with fit_state, confidence, guidance, report_preparation, scientific_summary."""
    fit_state, fit_confidence, ev = derive_fit_state_and_confidence(
        result, sem_enriched=sem_enriched, primary_keyword_rows=primary_keyword_rows
    )
    if force_compound_fit and sum(1 for d in result.dimensions if d.activated) >= 2:
        fit_state = "compound_fit"
        if fit_confidence == "low":
            fit_confidence = "medium"

    boundary_note, what_next, issue_type, why_issue = boundary_and_repo_action(
        fit_state,
        fit_confidence,
        result,
        sem_enriched=sem_enriched,
        primary_keyword_rows=primary_keyword_rows,
    )

    closest_rows = [m.as_dict() for m in result.closest[:5]] if not result.in_table else []
    # enrich closest with same shape as primaries if needed
    if not result.in_table and result.closest:
        closest_rows = [m.as_dict() for m in result.closest[:5]]

    report_prep = build_report_preparation(
        issue_type,
        why_issue_type=why_issue,
        closest_classes=closest_rows,
        primary_classes=primary_keyword_rows,
        boundary_pressure_note=boundary_note,
    )

    tmpl = report_prep.get("issue_template_path")
    rec_action_summary = (
        f"{issue_type}: {tmpl} — {why_issue}"
        if tmpl
        else f"{issue_type}: (no template) — {why_issue}"
    )

    prim = primary_keyword_rows[0] if primary_keyword_rows else None
    ssr = prim.get("suggested_structural_response") if prim else None
    struct_summary = (
        f"Primary class {prim['id']}: enforce «{ssr.get('control_principle_forbidden', '')[:200]}…» "
        f"with detection «{ssr.get('detection_pattern', '')[:200]}…» "
        f"and structural mitigation «{ssr.get('structural_mitigation', '')[:200]}…»."
        if ssr
        else "No primary class above threshold; see closest_if_not_in_table for nearest mechanisms."
    )

    obs = (
        f"Classifier {'accepted' if result.in_table else 'did not accept'} keyword-threshold matches; "
        f"{ev.get('activated_dimension_count', 0)} structural dimension(s) activated. "
        f"Top keyword score {ev.get('keyword_top_score')}; top semantic score {ev.get('semantic_top_score')}."
    )

    secondary = None
    if len(primary_keyword_rows) > 1:
        secondary = (
            f"Secondary candidate {primary_keyword_rows[1].get('id')}: "
            f"{primary_keyword_rows[1].get('name')}"
        )

    uncertainties: list[str] = []
    if ev.get("cross_modal_disagreement_advisory"):
        uncertainties.append(
            "Keyword primary and semantic top differ with both above classifier-scale floors — reconcile wording before treating either as definitive."
        )
    if not result.in_table:
        uncertainties.append(
            "Classifier did not accept a class; confirm with CONTRIBUTING §1 checklist before proposing a new class."
        )
    if fit_confidence == "low":
        uncertainties.append("Low confidence — treat mapping as provisional; gather mechanism-specific wording or sources.")

    summary = build_scientific_summary(
        observed_mechanism_summary=obs,
        fit_state=fit_state,
        fit_confidence=fit_confidence,
        primary_reading=(
            f"{prim['id']} — {prim.get('name')}" if prim else None
        ),
        secondary_reading=secondary,
        possible_gap=(not result.in_table),
        recommended_structural_response_summary=struct_summary,
        what_to_do_next=what_next,
        recommended_repo_action=rec_action_summary,
        uncertainty_notes=uncertainties,
    )

    bundle["classifier_hit"] = result.in_table
    bundle["contributing_route"] = issue_type
    bundle["fit_state"] = fit_state
    bundle["fit_confidence"] = fit_confidence
    bundle["fit_evidence"] = ev
    bundle["boundary_pressure_note"] = boundary_note
    bundle["what_to_do_next"] = what_next
    bundle["recommended_repo_action"] = {
        "issue_type": issue_type,
        "rationale": why_issue,
        "contributing_section": "CONTRIBUTING.md — Ways to Contribute",
        "issue_template_relative_path": tmpl,
        "summary": rec_action_summary,
    }
    bundle["report_preparation"] = report_prep
    bundle["scientific_summary"] = summary
    bundle["falsification_note"] = (
        "The periodic-table classifier decides hit vs miss (in_table). fit_state only summarizes that verdict "
        "(strong / compound / weak in-table, or possible_gap_candidate on a miss). Next steps route through "
        "CONTRIBUTING.md; semantic search is advisory context, not a second acceptance gate."
    )
    bundle["response_contract"] = classification_response_contract()
