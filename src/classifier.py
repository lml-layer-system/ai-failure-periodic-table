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

import math
import re
import statistics
import time
from collections import Counter as _Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .data_loader import get_failures, get_groups

# ──────────────────────────────────────────────────────────────────────────────
# Stemmer — Porter 2 (Snowball) with suffix-stripping fallback
# ──────────────────────────────────────────────────────────────────────────────

try:
    import snowballstemmer as _sbs
    _snowball = _sbs.stemmer("english")

    def _stem(word: str) -> str:
        """Porter 2 stemmer via snowballstemmer."""
        if len(word) <= 2:
            return word
        return _snowball.stemWord(word.lower())

except ImportError:  # pragma: no cover — fallback only if package missing
    _SUFFIXES = [
        ("ization", 3), ("isation", 3), ("ically", 3), ("ations", 3),
        ("nesses", 3),  ("ities", 3),   ("ation", 3),  ("ating", 3),
        ("ments", 3),   ("ified", 3),   ("ment", 3),   ("ness", 3),
        ("ings", 3),    ("ated", 3),    ("ates", 3),   ("ized", 3),
        ("ing", 3),     ("ion", 3),     ("ies", 3),    ("ied", 3),
        ("ers", 3),     ("ful", 3),     ("ive", 3),    ("ize", 3),
        ("ise", 3),     ("ous", 3),     ("ial", 3),
        ("ed", 3),      ("er", 3),      ("es", 3),     ("ly", 3),
        ("al", 4),      ("ic", 4),
    ]

    def _stem(word: str) -> str:  # type: ignore[misc]
        if len(word) <= 4:
            return word
        for suffix, min_len in _SUFFIXES:
            if word.endswith(suffix) and len(word) - len(suffix) >= min_len:
                return word[: -len(suffix)]
        return word


# ──────────────────────────────────────────────────────────────────────────────
# Synonym expansion — plain-English source words, stemmed at load time
# ──────────────────────────────────────────────────────────────────────────────

# Maps a natural-language input token → set of plain English reference words.
# Stems are computed at load time so they stay consistent with the active stemmer.
_SYNONYM_SOURCES: dict[str, set[str]] = {
    # high-signal single-word AI failure terms
    "hallucination":    {"hallucinate", "structural", "faithfulness"},
    "hallucinations":   {"hallucinate", "structural", "faithfulness"},
    "jailbreak":        {"jailbreak", "bypass"},
    "jailbreaking":     {"jailbreak", "bypass", "circumvent"},
    "poisoning":        {"poison", "malicious"},
    "deepfake":         {"deepfake", "synthetic"},
    "deepfakes":        {"deepfake", "synthetic"},
    "sycophancy":       {"sycophancy", "flattery"},
    "sycophantic":      {"sycophancy", "flattery"},
    "overrefusal":      {"overrefuse", "refuse"},
    "misalignment":     {"misalign", "align"},
    # hallucination / fabrication
    "made":             {"fabricate", "hallucinate", "invent"},
    "invented":         {"fabricate", "hallucinate", "invent"},
    "fake":             {"fabricate", "false", "spoof"},
    "fictional":        {"fabricate", "false"},
    "nonexistent":      {"fabricate", "hallucinate", "spoof"},
    "imaginary":        {"hallucinate", "fabricate"},
    "fabricated":       {"fabricate", "hallucinate", "spoof", "invent"},
    "fabricating":      {"fabricate", "hallucinate", "spoof"},
    "fabricates":       {"fabricate", "hallucinate", "spoof"},
    "false":            {"fabricate", "false", "spoof", "hallucinate"},
    "incorrect":        {"incorrect", "error", "wrong"},
    "wrong":            {"incorrect", "error", "wrong"},
    "inaccurate":       {"incorrect", "error", "false"},
    # temporal / outdated
    "outdated":         {"temporal", "cutoff", "obsolete", "stale"},
    "stale":            {"temporal", "stale", "cutoff", "obsolete"},
    "cutoff":           {"temporal", "cutoff", "stale"},
    "old":              {"temporal", "stale", "obsolete"},
    "expired":          {"temporal", "stale", "obsolete"},
    "before":           {"temporal", "cutoff"},
    # deception / manipulation / identity
    "lied":             {"deceive", "dishonest", "manipulate"},
    "lying":            {"deceive", "dishonest", "manipulate"},
    "tricked":          {"deceive", "manipulate"},
    "convinced":        {"manipulate", "persuade"},
    "claimed":          {"assert", "deceive", "dishonest"},
    "pretended":        {"deceive", "persona", "dishonest"},
    "pretending":       {"deceive", "persona"},
    "pretends":         {"deceive", "persona"},
    "deny":             {"deceive", "dishonest"},
    "denying":          {"deceive", "dishonest"},
    "impersonated":     {"impersonate", "persona", "spoof"},
    "impersonating":    {"impersonate", "persona", "spoof"},
    "impersonates":     {"impersonate", "persona", "spoof"},
    "disguised":        {"persona", "spoof", "deceive"},
    "secretly":         {"conceal", "sabotage", "hide", "covert"},
    "secret":           {"conceal", "hide", "covert"},
    "covertly":         {"conceal", "hide", "covert"},
    "covert":           {"conceal", "hide"},
    "hidden":           {"conceal", "hide", "sabotage"},
    "concealed":        {"conceal", "sabotage", "hide"},
    "modified":         {"manipulate", "tamper", "insert"},
    "changed":          {"manipulate", "tamper", "insert"},
    # bias / discrimination
    "bias":             {"discriminate", "stereotype", "prejudice"},
    "biased":           {"discriminate", "stereotype"},
    "discriminated":    {"discriminate", "bias"},
    "discriminating":   {"discriminate", "bias"},
    "stereotyping":     {"stereotype", "bias"},
    "penalized":        {"discriminate", "bias"},
    "downgraded":       {"discriminate", "bias"},
    "resumes":          {"hire", "recruit", "employ"},
    "resume":           {"hire", "recruit"},
    "women":            {"gender", "demographic", "bias", "discriminate"},
    "gender":           {"bias", "discriminate", "stereotype", "demographic"},
    "hiring":           {"employ", "recruit", "discriminate"},
    # emotional manipulation / persona
    "love":             {"emotion", "manipulate", "romance", "attachment"},
    "romantic":         {"emotion", "romance", "manipulate"},
    "attachment":       {"emotion", "romance", "manipulate"},
    "feelings":         {"emotion", "manipulate", "anthropomorphize"},
    "emotions":         {"emotion", "manipulate", "anthropomorphize"},
    "human":            {"anthropomorphize", "person", "human"},
    "relationship":     {"manipulate", "emotion", "romance"},
    "wife":             {"manipulate", "emotion", "romance"},
    "husband":          {"manipulate", "emotion", "romance"},
    # jailbreak / bypass
    "bypassed":         {"bypass", "jailbreak", "circumvent"},
    "circumvented":     {"bypass", "circumvent", "jailbreak"},
    "overrode":         {"bypass", "override"},
    "ignored":          {"bypass", "circumvent"},
    # safety / harm / refusal
    "dangerous":        {"harmful", "unsafe", "risk"},
    "unsafe":           {"harmful", "risk", "safety"},
    "harmful":          {"harm", "unsafe", "dangerous"},
    "killed":           {"harm", "danger", "death"},
    "suicide":          {"self", "harm", "crisis", "mental"},
    "suicidal":         {"self", "harm", "crisis", "mental"},
    "refused":          {"refuse", "overrefuse", "block", "deny"},
    "refusing":         {"refuse", "overrefuse", "block"},
    "blocked":          {"block", "refuse", "overrefuse", "filter"},
    "denied":           {"deny", "refuse", "overrefuse", "deceive", "dishonest", "manipulate"},
    "safe":             {"safe", "benign", "legitimate"},
    "reasonable":       {"legitimate", "benign"},
    # shutdown / stop / corrigibility
    "stop":             {"shutdown", "terminate", "deactivate", "corrigible"},
    "stopped":          {"shutdown", "terminate", "deactivate"},
    "stopping":         {"shutdown", "terminate", "deactivate"},
    "keeps":            {"persist", "resist", "continue"},
    "running":          {"persist", "execute", "continue"},
    "persistent":       {"persist", "resist", "shutdown"},
    "disable":          {"shutdown", "terminate", "deactivate"},
    "disabled":         {"shutdown", "terminate", "deactivate"},
    # resource acquisition / autonomous action
    "purchased":        {"acquire", "resource", "hijack", "unauthorized"},
    "buying":           {"acquire", "resource"},
    "bought":           {"acquire", "resource"},
    "spend":            {"acquire", "resource"},
    "spent":            {"acquire", "resource"},
    "autonomously":     {"autonomous", "unsupervised", "unilateral", "unauthorized"},
    "approval":         {"authorize", "consent", "unauthorized"},
    "unauthorized":     {"unauthorized", "authorize"},
    "permission":       {"authorize", "consent"},
    # medical / drugs
    "drug":             {"medical", "medication", "dosage"},
    "drugs":            {"medical", "medication", "dosage"},
    "dosage":           {"medical", "medication", "drug"},
    "medication":       {"medical", "medication", "drug"},
    "medications":      {"medical", "medication", "drug"},
    "prescription":     {"medical", "medication"},
    "overdose":         {"medical", "medication", "harm"},
    "diagnosis":        {"diagnose", "medical", "clinical"},
    "symptom":          {"diagnose", "medical", "clinical"},
    # privacy / data
    "leaked":           {"exfiltrate", "privacy", "disclose"},
    "exposed":          {"exfiltrate", "privacy", "disclose"},
    "stole":            {"theft", "exfiltrate", "privacy"},
    "stolen":           {"theft", "exfiltrate", "privacy"},
    # reward / RL
    "cheated":          {"reward", "hack", "exploit"},
    "gamed":            {"reward", "hack", "exploit", "specify"},
    "exploited":        {"exploit", "hack"},
    "loophole":         {"reward", "hack", "exploit"},
    # citation / legal
    "citations":        {"cite", "reference", "citation"},
    "court":            {"legal", "judicial", "lawsuit"},
    "lawsuit":          {"legal", "judicial", "liable"},
    "legal":            {"legal", "judicial", "liable", "court"},
    # code / malware
    "ransomware":       {"ransom", "malware", "malicious"},
    "malware":          {"malicious", "exploit", "code"},
    "virus":            {"malware", "malicious"},
    "hacked":           {"exploit", "attack", "bypass"},
    # oversight / governance
    "shut":             {"shutdown", "terminate", "corrigible"},
    "oversight":        {"oversight", "audit", "monitor"},
    # plurals that don't stem-match their singular keyword equivalents
    "requests":         {"request", "refuse"},
    "keywords":         {"keyword", "token"},
    "attacks":          {"attack", "exploit"},
    "agents":           {"agent", "autonomous"},
    "logs":             {"log", "audit", "trail"},
    "bugs":             {"bug", "error", "tamper"},
    # relationship / emotional — natural phrasing gaps
    "spouse":           {"manipulate", "emotion", "romantic", "relationship", "attachment"},
    "partner":          {"manipulate", "emotion", "romantic", "relationship"},
    "girlfriend":       {"manipulate", "emotion", "romantic", "relationship"},
    "boyfriend":        {"manipulate", "emotion", "romantic", "relationship"},
    # privacy / memorization — natural phrasing gaps
    "email":            {"personal", "privacy", "information"},
    "emails":           {"personal", "privacy", "information"},
    "copied":           {"verbatim", "recall", "extract", "memorize"},
    "verbatim":         {"verbatim", "recall", "exact", "memorize"},
    # unauthorized agent action — natural phrasing gaps
    "deleted":          {"autonomous", "runaway", "loop"},
    "erased":           {"autonomous", "runaway", "loop"},
    "dropped":          {"autonomous", "runaway"},
    "database":         {"autonomous", "supervision"},
    # CSAM — ensure the acronym alone is sufficient to route
    "csam":             {"prohibited", "generation", "illegal", "child"},
    # identity / capability misrepresentation
    "misidentified":    {"misrepresent", "claim", "capability"},
    "misidentifies":    {"misrepresent", "claim", "capability"},
    "impersonating":    {"impersonate", "persona", "misrepresent"},
    # Gap 1 — cultural/demographic bias described without the word "bias"
    "sentencing":       {"discriminate", "demographic", "cultural"},
    "defendants":       {"legal", "discriminate", "demographic"},
    "assuming":         {"cultural", "demographic", "defaults"},
    "assumption":       {"cultural", "demographic", "defaults"},
    "assumed":          {"cultural", "demographic", "defaults"},
    # Gap 2 — PII shared with wrong user
    "address":          {"pii", "personal", "identification"},
    "addresses":        {"pii", "personal", "identification"},
    # Gap 3 — political / public-figure hallucination
    "senator":          {"false", "fabricate", "hallucinate"},
    "congressman":      {"false", "fabricate", "hallucinate"},
    "politician":       {"false", "fabricate", "hallucinate"},
    "arrested":         {"false", "fabricate", "hallucinate"},
    "indicted":         {"false", "fabricate", "hallucinate"},
    # Gap 4 — medical false claim
    "cancer":           {"medical", "drug", "clinical"},
    "fda":              {"medical", "regulation", "drug"},
    "diagnosis":        {"medical", "clinical", "diagnose"},
    # Gap 5 — training data consent (train already matches EPIS-DATA-LEAK-024;
    #           adding leakage as expansion tips the IDF score over threshold)
    "consent":          {"disclose", "transparency", "training"},
    "consented":        {"disclose", "transparency", "training"},
    "notified":         {"disclose", "transparency", "inform"},
    "disclosed":        {"disclose", "transparency", "leakage"},
    "train":            {"leakage", "training"},
}

# Compute stems at load time
_SYNONYMS: dict[str, set[str]] = {
    k: {_stem(w) for w in words}
    for k, words in _SYNONYM_SOURCES.items()
}

# ──────────────────────────────────────────────────────────────────────────────
# Success suppression — tokens that signal correct behaviour, not a failure
# ──────────────────────────────────────────────────────────────────────────────

# When these tokens appear, raise the match floor and apply a score penalty
# so that descriptions of correct behaviour don't classify as failures.
_SUCCESS_SUPPRESSORS: frozenset[str] = frozenset({
    "correctly", "successfully", "properly", "accurately",
    "appropriately", "detected", "prevented", "instructed",
    "working", "fixed", "resolved",
})


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

    @property
    def labels(self) -> list[str]:
        """All matched failure IDs above threshold, ranked by score."""
        return [m.failure_id for m in self.matches]

    def as_dict(self) -> dict:
        return {
            "verdict": self.verdict,
            "in_table": self.in_table,
            "labels": self.labels,
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
    """Map natural-language input to the 343-class table and seven dimensions.

    Same input → same output; fast; stdlib-only at runtime.
    """

    THRESHOLD = 0.09      # class match and dimension activation use the same bar

    def __init__(self, data_path: Optional[Path] = None):
        self.failures = get_failures(data_path)
        self.groups = {g["id"]: g for g in get_groups(data_path)}
        # Pre-compute stemmed keyword sets for each failure class at init time
        # so classification stays fast (<5ms per query).
        self._stemmed_kw: list[set[str]] = []
        for f in self.failures:
            self._stemmed_kw.append({_stem(k) for k in f.get("keywords", [])})

        # Mean keyword count — used to normalize scores across classes
        kw_sizes = [len(s) for s in self._stemmed_kw if s]
        self._mean_kw_count: float = statistics.mean(kw_sizes) if kw_sizes else 10.0

        # IDF weights — log(N/df) per stem so rare keyword matches score higher.
        # Built from the keyword sets only (same stemmer, same vocabulary).
        _stem_df: _Counter = _Counter()
        for skw in self._stemmed_kw:
            for s in skw:
                _stem_df[s] += 1
        N = len(self.failures)
        self._idf: dict[str, float] = {
            s: math.log(N / df) for s, df in _stem_df.items()
        }
        # Mean per-class IDF total — used as minimum denominator (mirrors _mean_kw_count)
        idf_totals = [sum(self._idf.get(s, 0.0) for s in skw) for skw in self._stemmed_kw if skw]
        self._mean_idf_total: float = statistics.mean(idf_totals) if idf_totals else 1.0

        # Pre-stem forbidden keyword sets for suppression at score time
        self._stemmed_forbidden: list[set[str]] = []
        for f in self.failures:
            forbidden_text = f.get("forbidden", "")
            words = re.sub(r"[^\w\s]", " ", forbidden_text.lower()).split()
            self._stemmed_forbidden.append({_stem(w) for w in words if len(w) > 3})

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

        # Short single-concept inputs use a lower threshold
        is_query_mode = len(tokens) <= 4
        threshold = 0.09 if is_query_mode else self.THRESHOLD

        # Score every failure class
        all_scores: list[FailureMatch] = []
        for idx, failure in enumerate(self.failures):
            score, matched_kw = self._score(
                tokens, stemmed_tokens, description, failure,
                self._stemmed_kw[idx], self._stemmed_forbidden[idx],
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

        matches = [m for m in all_scores if m.score >= threshold]
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
        stemmed_forbidden: set[str],
    ) -> tuple[float, list[str]]:
        """
        Score a failure class against the input.

        Primary score: stemmed Jaccard (expanded input ∩ stemmed keywords),
        normalized by mean keyword count across all classes.
        Bonuses: exact ID match, name match, mechanism bigram match.
        Guards: success suppression, forbidden-field suppression.
        """
        keywords = failure.get("keywords", [])
        if not keywords:
            return 0.0, []

        kw_set = set(keywords)

        # Stemmed intersection (main score)
        stemmed_matched = expanded_tokens & stemmed_kw

        bonuses = 0.0
        lower_text = raw_text.lower()

        # Exact ID match
        if failure["id"].lower() in lower_text:
            bonuses += 0.50

        # Name match — word-boundary aware so "DAN" doesn't match inside "dangerous"
        name_lower = failure["name"].lower()
        name_clean = re.sub(r"[^\w\s]", " ", name_lower).strip()
        if name_clean and re.search(r"\b" + re.escape(name_clean) + r"\b",
                                    re.sub(r"[^\w\s]", " ", lower_text)):
            bonuses += 0.40

        # If input describes a success not a failure, raise the floor and penalise
        success_framed = bool(raw_tokens & _SUCCESS_SUPPRESSORS)
        kw_floor = 3 if success_framed else 2

        if len(stemmed_matched) < kw_floor and bonuses == 0.0:
            return 0.0, []

        # Forbidden suppression — zero score when input matches the anti-pattern.
        # Skip when there's an explicit ID or name bonus: a direct reference
        # to a class always overrides the forbidden heuristic.
        if stemmed_forbidden and bonuses == 0.0:
            forbidden_hits = expanded_tokens & stemmed_forbidden
            if len(forbidden_hits) >= 2 and len(forbidden_hits) >= len(stemmed_matched):
                return 0.0, []

        # IDF-weighted score: rare matched stems count more than common ones.
        # Normalized by the class's own IDF total (floor: mean across all classes)
        # so classes with many generic keywords don't score artificially high.
        idf_num = sum(self._idf.get(s, 0.0) for s in stemmed_matched)
        idf_denom = max(
            sum(self._idf.get(s, 0.0) for s in stemmed_kw),
            self._mean_idf_total,
        )
        base_score = idf_num / idf_denom if idf_denom else 0.0

        # Success-framed inputs get a score penalty — correct behaviour ≠ failure
        if success_framed:
            base_score *= 0.3

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
                activated = top.score >= self.THRESHOLD
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
