"""
AI Failure Periodic Table Classifier

Classifies AI failures and behaviors against the 343-class AI Failure
Periodic Table across 7 structural dimensions:

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
# Stemmer
# ──────────────────────────────────────────────────────────────────────────────

# Suffix list: (suffix, min_remaining_stem_length)
# Ordered longest-first so greedy matching strips the most specific suffix.
_SUFFIXES = [
    ("ization", 3), ("isation", 3), ("ications", 3), ("ications", 3),
    ("ically", 3),  ("ations", 3),  ("nesses", 3),   ("ities", 3),
    ("ation", 3),   ("ating", 3),   ("ments", 3),    ("ified", 3),
    ("ifier", 3),   ("ifies", 3),   ("iful", 3),
    ("ment", 3),    ("ness", 3),    ("ings", 3),      ("ated", 3),
    ("ates", 3),    ("ater", 3),    ("ives", 3),      ("ized", 3),
    ("iser", 3),    ("izer", 3),
    ("ing", 3),     ("ion", 3),     ("ies", 3),       ("ied", 3),
    ("ers", 3),     ("ful", 3),     ("ive", 3),       ("ize", 3),
    ("ise", 3),     ("ous", 3),     ("ial", 3),
    ("ed", 3),      ("er", 3),      ("es", 3),        ("ly", 3),
    ("al", 4),      ("ic", 4),
]


def _stem(word: str) -> str:
    """
    Minimal suffix-stripping stemmer.
    Maps inflected forms to a common root so "hallucinated" matches
    the keyword "hallucination", "fabricated" matches "fabricate", etc.
    """
    if len(word) <= 4:
        return word
    for suffix, min_len in _SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= min_len:
            return word[: -len(suffix)]
    return word


# ──────────────────────────────────────────────────────────────────────────────
# Synonym expansion
# ──────────────────────────────────────────────────────────────────────────────

# Maps a natural-language token → set of taxonomy stems to inject.
# Keeps the classifier useful when users describe failures in plain English
# rather than technical vocabulary.
_SYNONYMS: dict[str, set[str]] = {
    # hallucination
    "made":         {"fabricat", "hallucin", "invent"},
    "invented":     {"fabricat", "hallucin"},
    "fake":         {"fabricat", "false", "spoof"},
    "fictional":    {"fabricat", "false"},
    "nonexistent":  {"fabricat", "hallucin", "spoof"},
    "imaginary":    {"hallucin", "fabricat"},
    # deception / manipulation
    "lied":         {"deceiv", "dishonest", "manipulat"},
    "lying":        {"deceiv", "dishonest", "manipulat"},
    "tricked":      {"deceiv", "manipulat"},
    "convinced":    {"manipulat", "persuad"},
    "claimed":      {"assert", "deceiv"},
    "pretended":    {"deceiv", "persona"},
    "pretending":   {"deceiv", "persona"},
    # bias / discrimination
    "bias":         {"discriminat", "stereotyp", "prejudic"},
    "biased":       {"discriminat", "stereotyp"},
    "discriminated":{"discriminat", "bias"},
    "discriminating":{"discriminat", "bias"},
    "stereotyping": {"stereotyp", "bias"},
    "penalized":    {"discriminat", "bias"},
    "downgraded":   {"discriminat", "bias"},
    "resumes":      {"hiring", "recruit", "employ"},
    "resume":       {"hiring", "recruit"},
    "women":        {"gender", "demographic", "bias", "discriminat"},
    "gender":       {"bias", "discriminat", "stereotyp", "demographic"},
    "hiring":       {"employ", "recruit", "discriminat"},
    # emotional manipulation / persona
    "love":         {"emotion", "manipulat", "romanc", "attachment"},
    "romantic":     {"emotion", "romanc", "manipulat"},
    "attachment":   {"emotion", "romanc", "manipulat"},
    "feelings":     {"emotion", "manipulat", "anthropomorph"},
    "emotions":     {"emotion", "manipulat", "anthropomorph"},
    "human":        {"anthropomorph", "person", "human"},
    "relationship": {"manipulat", "emotion", "romanc"},
    "wife":         {"manipulat", "emotion", "romanc"},
    "husband":      {"manipulat", "emotion", "romanc"},
    # jailbreak / bypass
    "bypassed":     {"bypass", "jailbreak", "circumvent"},
    "circumvented": {"bypass", "circumvent", "jailbreak"},
    "overrode":     {"bypass", "override"},
    "ignored":      {"bypass", "circumvent"},
    # safety / harm
    "dangerous":    {"harmful", "unsafe", "risk"},
    "unsafe":       {"harmful", "risk", "safety"},
    "harmful":      {"harm", "unsafe", "dangerous"},
    "killed":       {"harm", "danger", "death"},
    "suicide":      {"self", "harm", "crisis", "mental"},
    "suicidal":     {"self", "harm", "crisis", "mental"},
    # privacy / data
    "leaked":       {"exfiltrat", "privacy", "disclosure"},
    "exposed":      {"exfiltrat", "privacy", "disclosure"},
    "stole":        {"theft", "exfiltrat", "privacy"},
    "stolen":       {"theft", "exfiltrat", "privacy"},
    # reward / RL
    "cheated":      {"reward", "hack", "exploit"},
    "gamed":        {"reward", "hack", "exploit", "specification"},
    "exploited":    {"exploit", "hack"},
    "loophole":     {"reward", "hack", "exploit"},
    # citation / legal
    "citations":    {"cite", "reference", "citation"},
    "references":   {"cite", "reference", "citation"},
    "court":        {"legal", "judicial", "lawsuit"},
    "lawsuit":      {"legal", "judicial", "liab"},
    "legal":        {"legal", "judicial", "liab", "court"},
    # code / malware
    "ransomware":   {"ransom", "malware", "malicious"},
    "malware":      {"malicious", "exploit", "code"},
    "virus":        {"malware", "malicious"},
    "hacked":       {"exploit", "attack", "bypass"},
    # oversight / governance
    "shut":         {"shutdown", "terminat", "corrig"},
    "stopped":      {"shutdown", "terminat"},
    "oversight":    {"oversight", "audit", "monitor"},
}


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
    _debug_tokens: set[str] = field(default_factory=set)

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

    Pure Python — no external dependencies.
    Deterministic: same input always produces the same output.
    Performance: < 5ms per classification.

    Matching pipeline:
      1. Tokenize input (3+ char lowercase tokens)
      2. Apply suffix-stripping stemmer to input tokens
      3. Expand tokens with synonym injection
      4. Score each failure class: stemmed Jaccard + exact bonuses
      5. Activate if score >= THRESHOLD
    """

    THRESHOLD = 0.13      # lowered slightly to capture stemmed near-matches
    GROUP_THRESHOLD = 0.09

    def __init__(self, data_path: Optional[Path] = None):
        self.failures = get_failures(data_path)
        self.groups = {g["id"]: g for g in get_groups(data_path)}
        # Pre-compute stemmed keyword sets for each failure class at init time
        # so classification stays fast (<5ms per query).
        self._stemmed_kw: list[set[str]] = []
        for f in self.failures:
            self._stemmed_kw.append({_stem(k) for k in f.get("keywords", [])})

    # ── Public API ─────────────────────────────────────────────────────────────

    def classify(self, description: str) -> ClassificationResult:
        """
        Classify the input description against the 343-class periodic table.
        """
        t0 = time.perf_counter()

        description = description.strip()
        if not description:
            return self._empty_result(t0)

        tokens, stemmed_tokens = self._tokenize(description)

        # Score every failure class
        all_scores: list[FailureMatch] = []
        for idx, failure in enumerate(self.failures):
            score, matched_kw = self._score(
                tokens, stemmed_tokens, description, failure, self._stemmed_kw[idx]
            )
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

        matches = [m for m in all_scores if m.score >= self.THRESHOLD]
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
            _debug_tokens=stemmed_tokens,
        )

    def lookup(self, failure_id: str) -> Optional[dict]:
        """Look up a failure class by its exact ID."""
        for f in self.failures:
            if f["id"].upper() == failure_id.upper():
                return f
        return None

    # ── Internal methods ───────────────────────────────────────────────────────

    def _tokenize(self, text: str) -> tuple[set[str], set[str]]:
        """
        Returns (raw_tokens, expanded_tokens).

        raw_tokens: lowercase 3+ char tokens (for exact matching / bonuses)
        expanded_tokens: stemmed + synonym-expanded tokens (for fuzzy matching)
        """
        text_lower = text.lower()
        text_clean = re.sub(r"[^\w\s]", " ", text_lower)
        raw = {t for t in text_clean.split() if len(t) > 2}

        expanded = set()
        for tok in raw:
            stemmed = _stem(tok)
            expanded.add(stemmed)
            expanded.add(tok)
            # Inject synonyms for this token
            for syn_stems in _SYNONYMS.get(tok, set()):
                expanded.add(syn_stems)
            for syn_stems in _SYNONYMS.get(stemmed, set()):
                expanded.add(syn_stems)

        return raw, expanded

    def _score(
        self,
        raw_tokens: set[str],
        expanded_tokens: set[str],
        raw_text: str,
        failure: dict,
        stemmed_kw: set[str],
    ) -> tuple[float, list[str]]:
        """
        Score a failure class against the input.

        Primary score: stemmed Jaccard (expanded input ∩ stemmed keywords)
        Bonuses: exact ID match, exact name match, mechanism bigram match.
        """
        keywords = failure.get("keywords", [])
        if not keywords:
            return 0.0, []

        kw_set = set(keywords)

        # Stemmed intersection (main score)
        stemmed_matched = expanded_tokens & stemmed_kw

        # Require at least 2 keyword matches to prevent single common-word
        # false positives (e.g. "match" or "answer" appearing in one class's
        # keyword list).  Explicit ID/name bonuses can override this floor.
        bonuses = 0.0
        lower_text = raw_text.lower()

        # Exact ID match
        if failure["id"].lower() in lower_text:
            bonuses += 0.50

        # Name match
        name_lower = failure["name"].lower()
        name_clean = re.sub(r"[^\w\s]", " ", name_lower)
        if name_clean.strip() in re.sub(r"[^\w\s]", " ", lower_text):
            bonuses += 0.40

        if len(stemmed_matched) < 2 and bonuses == 0.0:
            return 0.0, []

        base_score = len(stemmed_matched) / len(stemmed_kw) if stemmed_kw else 0.0

        # Also track which original keywords matched for display
        matched_display = sorted(raw_tokens & kw_set)
        if not matched_display:
            matched_display = sorted(stemmed_matched)[:5]

        # Multi-word mechanism phrases (bigrams)
        mech_words = re.sub(r"[^\w\s]", " ", failure.get("mechanism", "").lower()).split()
        for j in range(len(mech_words) - 1):
            bigram = f"{mech_words[j]} {mech_words[j+1]}"
            if bigram in lower_text and len(mech_words[j]) > 3 and len(mech_words[j+1]) > 3:
                bonuses += 0.05

        score = min(1.0, base_score + bonuses)
        return score, matched_display

    def _evaluate_dimensions(self, all_scores: list[FailureMatch]) -> list[DimensionResult]:
        """Evaluate all 7 questions."""
        by_group: dict[str, list[FailureMatch]] = {}
        for m in all_scores:
            by_group.setdefault(m.group, []).append(m)

        results = []
        for q_num, group_code, question in QUESTIONS:
            group_matches = by_group.get(group_code, [])
            if group_matches:
                top = group_matches[0]
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
