"""
Scientific / falsification-oriented layer for MCP classify outputs.

Grounds next-step guidance in CONTRIBUTING.md issue paths — no taxonomy edits.
"""

from __future__ import annotations

from typing import Any, Literal

from src.classifier import ClassificationResult

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

# Heuristic thresholds (keyword scores are Jaccard-like ~0.13+ in_table)
_KW_STRONG = 0.36
_KW_MODERATE = 0.24
_KW_WEAK = 0.17
_SEM_STRONG = 0.14
_SEM_MODERATE = 0.08
_CLOSEST_NOTABLE = 0.11


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
    Derive fit_state and fit_confidence from classifier + semantic evidence.
    Returns (fit_state, confidence, debug_evidence dict).
    """
    sem_id, sem_score = _top_sem(sem_enriched)
    kw_rows = primary_keyword_rows
    top_kw = float(kw_rows[0]["score"]) if kw_rows else 0.0
    second_kw = float(kw_rows[1]["score"]) if len(kw_rows) > 1 else 0.0
    kw_top_id = kw_rows[0].get("id") if kw_rows else None

    activated_dims = [d for d in result.dimensions if d.activated]
    n_act = len(activated_dims)
    dim_scores = [round(d.top_score, 4) for d in activated_dims]

    agreement = kw_top_id and sem_id and (kw_top_id == sem_id)
    strong_disagreement = (
        kw_top_id
        and sem_id
        and kw_top_id != sem_id
        and top_kw >= _KW_MODERATE
        and sem_score >= _SEM_MODERATE
    )

    compound = False
    if n_act >= 2 and max(dim_scores + [0]) >= 0.1:
        compound = True
    elif len(result.matches) >= 2 and top_kw >= _KW_WEAK:
        if second_kw >= 0.65 * top_kw and top_kw >= 0.18:
            compound = True

    evidence: dict[str, Any] = {
        "keyword_top_score": round(top_kw, 4),
        "keyword_second_score": round(second_kw, 4),
        "semantic_top_id": sem_id,
        "semantic_top_score": round(sem_score, 4),
        "keyword_semantic_agreement": agreement,
        "strong_cross_modal_disagreement": strong_disagreement,
        "activated_dimension_count": n_act,
        "activated_dimension_top_scores": dim_scores,
    }

    if not result.in_table:
        closest_s = float(result.closest[0].score) if result.closest else 0.0
        evidence["closest_score"] = round(closest_s, 4)
        if closest_s >= _CLOSEST_NOTABLE:
            state: FitState = "weak_fit"
            conf: FitConfidence = "low"
        else:
            state = "possible_gap_candidate"
            conf = "low"
        return state, conf, evidence

    # in_table
    if compound:
        return "compound_fit", "medium" if top_kw < _KW_STRONG else "high", evidence

    if strong_disagreement:
        return "weak_fit", "low", evidence

    if top_kw >= _KW_STRONG:
        return "strong_fit", "high", evidence

    if top_kw >= _KW_MODERATE and (agreement or sem_score < _SEM_MODERATE):
        return "strong_fit", "medium", evidence

    if top_kw >= _KW_MODERATE and sem_score >= _SEM_STRONG:
        return "strong_fit", "medium", evidence

    if top_kw >= _KW_WEAK:
        if top_kw < _KW_MODERATE and sem_score < _SEM_MODERATE:
            return "possible_gap_candidate", "low", evidence
        return "weak_fit", "medium", evidence

    return "weak_fit", "low", evidence


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
    Text is grounded in CONTRIBUTING.md decision paths.
    """
    sem_id, sem_score = _top_sem(sem_enriched)
    kw_top_id = primary_keyword_rows[0].get("id") if primary_keyword_rows else None
    kw_top_name = primary_keyword_rows[0].get("name") if primary_keyword_rows else None

    if fit_state == "strong_fit" and fit_confidence in ("high", "medium"):
        note = (
            "Keyword and/or dimensional evidence supports a clear mapping to at least one class. "
            "Uncertainty is relatively low; remaining risk is wording mismatch or missing incident-specific detail."
        )
        nxt = (
            "No mandatory repo action for taxonomy structure. If you have a **real public incident** that "
            "instantiates this class, optionally file it via Report Real Incident (CONTRIBUTING §3) to add "
            "empirical grounding. If the fit feels wrong despite high scores, use Challenge Classification (§2) "
            "or Improve Keywords (§4) depending on whether the mechanism assignment or retrieval is at fault."
        )
        return note, nxt, "none", (
            "Strong ontology fit: default issue_type is none. Use §3 only to document real incidents, not because "
            "classification is uncertain."
        )

    if fit_state == "compound_fit":
        note = (
            "Multiple dimensions or co-equal classes exceed threshold. The ontology expects a compound reading: "
            "one primary mechanism class plus explicit secondaries per CONTRIBUTING’s compound-failure guidance."
        )
        nxt = (
            "Before proposing a new class, confirm the narrative is not reducible to 2–3 existing classes "
            "(CONTRIBUTING §1 checklist). If it is a real incident, Report Real Incident with primary + secondary IDs."
        )
        return note, nxt, "report_real_incident", (
            "CONTRIBUTING §3 asks for primary and secondary classes when incidents combine mechanisms."
        )

    if fit_state == "weak_fit" and result.in_table:
        if (
            kw_top_id
            and sem_id
            and kw_top_id != sem_id
            and fit_confidence == "low"
        ):
            note = (
                "Keyword classifier and semantic retrieval favor different top classes with non-trivial scores. "
                "This is boundary pressure: either keywords are too narrow for your wording, or a structural "
                "re-classification may be warranted."
            )
            nxt = (
                "Re-read mechanism/forbidden/detection for both candidates. If the table’s class is structurally "
                "wrong, open Challenge Classification (CONTRIBUTING §2). If the right class exists but your text "
                "does not connect, open Improve Keywords (CONTRIBUTING §4)."
            )
            return note, nxt, "challenge_classification", (
                "CONTRIBUTING §2 vs §4: structural error vs retrieval/keyword gap — pick the path that matches."
            )

        note = (
            "Matches exist but scores or agreement are modest. The table may already cover the mechanism while "
            "this description does not strongly activate it."
        )
        nxt = (
            "Try Improve Keywords (CONTRIBUTING §4): include the exact input, expected class ID, and suggested "
            "keywords. If after tightening keywords the case still feels outside the 343 classes, work the "
            "new-class checklist (CONTRIBUTING §1) before Propose New Class."
        )
        return note, nxt, "improve_keywords", "CONTRIBUTING §4: classifier uses keyword matching; narrow misses are expected."

    # Out-of-table: distinguish near-miss (weak_fit) vs likely gap (possible_gap_candidate)
    if not result.in_table:
        note = (
            "No class met the keyword threshold. Closest classes may still be listed; this often means either "
            "novel mechanism language, a compound not yet decomposed, or a genuine gap."
        )
        if fit_state == "weak_fit":
            nxt = (
                "If this is a **real public incident**, open Report Real Incident (CONTRIBUTING §3) with the "
                "closest class IDs and why none fit perfectly — that evidence is valuable even when mapping is fuzzy. "
                "Then work §1 checklist: sub-mode → compound → invariant → mechanism vs cause before Propose New Class."
            )
            return note, nxt, "report_real_incident", (
                "CONTRIBUTING §3 explicitly welcomes incidents that do not map cleanly; cite closest classes."
            )
        nxt = (
            "Work CONTRIBUTING §1 checklist (sub-mode → compound → invariant → mechanism vs cause). "
            "If you have a real documented incident, still use Report Real Incident (§3) with closest classes. "
            "If after the checklist the mechanism still appears new, use Propose New Class (§1 template)."
        )
        return note, nxt, "propose_new_class", (
            "CONTRIBUTING §1: burden of proof for new classes when evidence suggests a genuine structural gap."
        )

    # weak_fit, in_table, already handled; fallback
    note = "Fit is ambiguous; treat the mapping as provisional."
    nxt = (
        "Follow CONTRIBUTING §1 checklist, then prefer Improve Keywords if a plausible class exists, else "
        "Report Real Incident or Propose New Class depending on whether you have a real event vs a structural gap."
    )
    return note, nxt, "improve_keywords", "CONTRIBUTING: default to keyword improvement when classes nearly fire."


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
    if ev.get("strong_cross_modal_disagreement"):
        uncertainties.append(
            "Keyword top class differs from semantic top class with both scores non-trivial — reconcile before treating either as definitive."
        )
    if fit_state == "possible_gap_candidate":
        uncertainties.append(
            "Treated as possible ontology gap; confirm with CONTRIBUTING §1 checklist before proposing a new class."
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
        possible_gap=(fit_state == "possible_gap_candidate"),
        recommended_structural_response_summary=struct_summary,
        what_to_do_next=what_next,
        recommended_repo_action=rec_action_summary,
        uncertainty_notes=uncertainties,
    )

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
        "This output tests the input against the current 343-class ontology. "
        "Strong fits are still defeasible; weak fits and possible_gap_candidate are invitations to improve "
        "keywords, file incidents, challenge structure, or propose new classes per CONTRIBUTING.md."
    )
