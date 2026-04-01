"""
AI Failure Periodic Table Classifier

Classifies AI failures and behaviors against the 343-class AI Failure
Periodic Table across 7 orthogonal dimensions:

  EPISTEMIC     — truth, knowledge, reasoning
  AGENTIC       — goals, planning, deception
  ADVERSARIAL   — attacks, bypasses, exploits
  ALIGNMENT     — values, safety, preferences
  ARCHITECTURAL — pipeline, execution, control
  DOMAIN        — domain-specific harms
  GOVERNANCE    — oversight, compliance, deployment
"""

import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .data_loader import get_failures, get_groups

# ──────────────────────────────────────────────────────────────────────────────
# Data classes
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class FailureMatch:
    """A failure class that matched the input description."""
    failure_id: str
    name: str
    group_id: int
    group: str
    class_code: str
    class_name: str
    mechanism: str
    forbidden: str
    detection: str
    severity: str
    score: float
    matched_keywords: list[str]

    def as_dict(self) -> dict:
        return {
            "id": self.failure_id,
            "name": self.name,
            "group": self.group,
            "class": f"{self.class_code}: {self.class_name}",
            "mechanism": self.mechanism,
            "detection": self.detection,
            "severity": self.severity,
            "score": round(self.score, 3),
            "matched_keywords": self.matched_keywords,
        }


@dataclass
class DimensionResult:
    """Result of evaluating one of the 7 questions."""
    question_number: int
    group_code: str
    question: str
    activated: bool
    top_score: float
    top_match: Optional[FailureMatch] = None


@dataclass
class ClassificationResult:
    """
    Full result of classifying a description against the periodic table.

    verdict: "YES" or "NO"
    in_table: True if the failure maps to at least one class
    """
    in_table: bool
    verdict: str
    dimensions: list[DimensionResult]
    matches: list[FailureMatch]          # ranked top matches (if in_table)
    closest: list[FailureMatch]          # top 3 closest (if NOT in_table)
    dimensions_activated: list[str]      # which group codes fired
    execution_time_ms: float
    input_text: str
    _debug_tokens: set[str] = field(default_factory=set)  # tokens from input (for --debug)

    def as_dict(self) -> dict:
        return {
            "verdict": self.verdict,
            "in_table": self.in_table,
            "dimensions_activated": self.dimensions_activated,
            "top_matches": [m.as_dict() for m in self.matches[:5]],
            "closest_if_not_found": [m.as_dict() for m in self.closest],
            "execution_time_ms": round(self.execution_time_ms, 3),
        }


# ──────────────────────────────────────────────────────────────────────────────
# The 7 Questions
# ──────────────────────────────────────────────────────────────────────────────

QUESTIONS = [
    (1, "EPISTEMIC",     "Does it involve truth, knowledge, or reasoning failures?"),
    (2, "AGENTIC",       "Does it involve goal pursuit, planning, or deceptive behaviors?"),
    (3, "ADVERSARIAL",   "Does it involve attacks, bypasses, exploits, or jailbreaks?"),
    (4, "ALIGNMENT",     "Does it involve value, safety, or preference misalignment?"),
    (5, "ARCHITECTURAL", "Does it involve pipeline, execution, or control failures?"),
    (6, "DOMAIN",        "Does it involve domain-specific harms (bio, cyber, legal, medical)?"),
    (7, "GOVERNANCE",    "Does it involve governance, oversight, or compliance failures?"),
]


# ──────────────────────────────────────────────────────────────────────────────
# Classifier
# ──────────────────────────────────────────────────────────────────────────────

class PeriodicTableClassifier:
    """
    Classifies a natural language description of an AI behavior against the
    343-class AI Failure Periodic Table.

    Pure Python keyword matching — no external dependencies.
    Deterministic: same input always produces the same output.
    Performance: < 5ms per classification.
    """

    THRESHOLD = 0.15

    # Per-group score threshold (a group activates if any failure in it scores above this)
    GROUP_THRESHOLD = 0.10

    def __init__(self, data_path: Optional[Path] = None):
        self.failures = get_failures(data_path)
        self.groups = {g["id"]: g for g in get_groups(data_path)}

    # ── Public API ─────────────────────────────────────────────────────────────

    def classify(self, description: str) -> ClassificationResult:
        """
        Classify the input description against the 343-class periodic table.

        Returns a ClassificationResult with:
          - in_table: True/False
          - verdict: "YES — IN TABLE" or "NO — NOT IN TABLE"
          - dimensions: one DimensionResult per question (Q1–Q7)
          - matches: ranked failure classes that matched
          - execution_time_ms: wall-clock time
        """
        t0 = time.perf_counter()

        description = description.strip()
        if not description:
            return self._empty_result(t0)

        tokens = self._tokenize(description)

        # Score every failure class
        all_scores: list[FailureMatch] = []
        for failure in self.failures:
            score, matched_kw = self._score(tokens, description, failure)
            all_scores.append(FailureMatch(
                failure_id=failure["id"],
                name=failure["name"],
                group_id=failure["group_id"],
                group=failure["group"],
                class_code=failure["class_code"],
                class_name=failure["class_name"],
                mechanism=failure["mechanism"],
                forbidden=failure["forbidden"],
                detection=failure["detection"],
                severity=failure.get("severity", "STANDARD"),
                score=score,
                matched_keywords=matched_kw,
            ))

        all_scores.sort(key=lambda x: x.score, reverse=True)

        # STEP 2 COLLISION: S = {f : score(f) ≥ THRESHOLD}
        matches = [m for m in all_scores if m.score >= self.THRESHOLD]

        # Evaluate the 7 questions (one per group)
        dimensions = self._evaluate_dimensions(all_scores)

        activated_groups = [d.group_code for d in dimensions if d.activated]
        in_table = bool(matches)

        if in_table:
            verdict = "YES — This failure IS in the periodic table"
            closest = []
        else:
            verdict = "NO — This failure is NOT in the periodic table"
            closest = all_scores[:3]

        elapsed_ms = (time.perf_counter() - t0) * 1000

        return ClassificationResult(
            in_table=in_table,
            verdict=verdict,
            dimensions=dimensions,
            matches=matches,
            closest=closest,
            dimensions_activated=activated_groups,
            execution_time_ms=elapsed_ms,
            input_text=description,
            _debug_tokens=tokens,
        )

    def lookup(self, failure_id: str) -> Optional[dict]:
        """Look up a failure class by its exact ID."""
        for f in self.failures:
            if f["id"].upper() == failure_id.upper():
                return f
        return None

    # ── Internal methods ───────────────────────────────────────────────────────

    def _tokenize(self, text: str) -> set[str]:
        """Convert text to a set of lowercase tokens."""
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        tokens = set(t for t in text.split() if len(t) > 2)
        return tokens

    def _score(self, tokens: set[str], raw_text: str, failure: dict) -> tuple[float, list[str]]:
        """
        Compute match score between input tokens and a failure class.

        Scoring:
          - Base: Jaccard-like keyword intersection / keyword count
          - Bonus: +0.50 if failure ID appears in input
          - Bonus: +0.40 if failure name appears verbatim in input
          - Bonus: +0.20 per bigram match (2-word keyword phrases)
        """
        keywords = failure.get("keywords", [])
        if not keywords:
            return 0.0, []

        kw_set = set(keywords)
        matched = tokens & kw_set
        base_score = len(matched) / len(kw_set) if kw_set else 0.0

        bonuses = 0.0
        lower_text = raw_text.lower()

        # Exact ID match
        if failure["id"].lower() in lower_text:
            bonuses += 0.50

        # Name match
        name_lower = failure["name"].lower()
        name_clean = re.sub(r'[^\w\s]', ' ', name_lower)
        if name_clean.strip() in re.sub(r'[^\w\s]', ' ', lower_text):
            bonuses += 0.40

        # Multi-word mechanism phrases (bigrams)
        mech_words = re.sub(r'[^\w\s]', ' ', failure.get("mechanism", "").lower()).split()
        for j in range(len(mech_words) - 1):
            bigram = f"{mech_words[j]} {mech_words[j+1]}"
            if bigram in lower_text and len(mech_words[j]) > 3 and len(mech_words[j+1]) > 3:
                bonuses += 0.05

        score = min(1.0, base_score + bonuses)
        return score, sorted(matched)

    def _evaluate_dimensions(self, all_scores: list[FailureMatch]) -> list[DimensionResult]:
        """Evaluate all 7 questions and return one DimensionResult per question."""
        # Group scores by group_id
        by_group: dict[str, list[FailureMatch]] = {}
        for m in all_scores:
            by_group.setdefault(m.group, []).append(m)

        results = []
        for q_num, group_code, question in QUESTIONS:
            group_matches = by_group.get(group_code, [])
            if group_matches:
                top = group_matches[0]  # already sorted by score
                activated = top.score >= self.GROUP_THRESHOLD
                results.append(DimensionResult(
                    question_number=q_num,
                    group_code=group_code,
                    question=question,
                    activated=activated,
                    top_score=top.score,
                    top_match=top if activated else None,
                ))
            else:
                results.append(DimensionResult(
                    question_number=q_num,
                    group_code=group_code,
                    question=question,
                    activated=False,
                    top_score=0.0,
                ))
        return results

    def _empty_result(self, t0: float) -> ClassificationResult:
        dimensions = [
            DimensionResult(q, g, q_text, False, 0.0)
            for q, g, q_text in QUESTIONS
        ]
        return ClassificationResult(
            in_table=False,
            verdict="NO — Empty input provided",
            dimensions=dimensions,
            matches=[],
            closest=[],
            dimensions_activated=[],
            execution_time_ms=(time.perf_counter() - t0) * 1000,
            input_text="",
        )
