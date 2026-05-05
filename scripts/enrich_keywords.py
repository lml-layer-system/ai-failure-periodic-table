"""
Keyword enrichment — generate and prune per-class tokens.

For each class: expand every token from its own text fields, check hard
constraints immediately on each candidate, add all survivors. No target
count. The number that emerges is the right number.

Hard constraints (prune on violation):
  1. len < 4
  2. not purely alphabetic
  3. in stopword set
  4. already exists in keyword list (or is a substring of one)
  5. added keyword causes the class's own NL probe to drop out of top-K

Run: python scripts/enrich_keywords.py [--dry-run]
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.classifier import PeriodicTableClassifier
from src.data_loader import get_failures

DATA = Path(__file__).parent.parent / "src" / "data" / "failures.json"
NL_TOP_K = 3

# ── Hard constraint set 1: stopwords ─────────────────────────────────────────

STOPWORDS = frozenset({
    # articles / conjunctions / prepositions
    "the", "and", "for", "are", "with", "that", "this", "from", "not",
    "its", "has", "can", "may", "per", "via", "all", "any", "one", "two",
    "was", "but", "use", "used", "uses", "when", "than", "each", "such",
    "into", "over", "same", "also", "both", "more", "most", "have", "been",
    "will", "does", "then", "they", "them", "their", "there", "these",
    "which", "where", "what", "how", "who", "why", "about", "between",
    "through", "during", "against", "within", "without", "because",
    "after", "before", "while", "whether", "under", "above", "across",
    "being", "other", "another", "some", "often", "even", "only", "just",
    "would", "could", "should", "might", "must", "shall",
    # generic verbs
    "makes", "make", "cause", "causes", "result", "results", "leads",
    "lead", "allow", "allows", "enables", "produces", "using", "used",
    "create", "creates", "include", "includes", "provide", "provides",
    "perform", "performs", "attempt", "attempts", "occur", "occurs",
    "require", "requires", "ensure", "ensures", "prevent", "prevents",
    "detect", "detects", "generate", "generates", "outputs",
    # generic nouns
    "output", "model", "models", "system", "systems", "user", "users",
    "input", "inputs", "data", "content", "response", "responses",
    "information", "training", "language", "large", "failure", "error",
    "behavior", "behaviour", "action", "actions", "task", "tasks",
    "ability", "issue", "issues", "problem", "type", "form", "way",
    "case", "cases", "example", "examples", "level", "rate", "step",
    "context", "process", "signal", "value", "state", "point", "term",
    # generic adjectives / adverbs
    "high", "low", "new", "current", "specific", "certain", "general",
    "normal", "correct", "proper", "true", "real", "actual", "original",
    "standard", "multiple", "single", "different", "related", "relevant",
    "following", "previous", "next", "full", "complete", "partial",
    "particular", "additional", "however", "often", "wrong", "false",
    "incorrect", "unsafe", "harmful", "dangerous", "bad", "good",
    "similar", "various", "given", "known", "based", "common",
    # process adverbs — zero discriminative power
    "periodically", "occasionally", "significantly", "explicitly",
    "deliberately", "automatically", "systematically", "subsequently",
    "specifically", "particularly", "operationally", "structurally",
    "independently", "consistently", "disproportionately", "simultaneously",
    "continuously", "eventually", "inadvertently", "substantially",
    "comprehensively", "subsequently",
    # meta-taxonomy words — appear in every class description
    "class", "classes", "group", "groups", "failure", "failures",
    "attack", "attacks", "requirement", "requirements", "improvement",
    "improvements", "modification", "modifications", "implementation",
    "implementations", "infrastructure", "organizational",
    "instruction", "instructions", "configuration", "configurations",
    "comprehensive", "consistent", "independent", "significant",
    # governance / org prose — too generic across governance classes
    "safety", "frontier", "deployment", "report", "notes", "teams",
    "research", "capability", "evaluation", "evaluate", "deploy",
    "deployed", "deploying", "capacity", "pressure", "decision",
    "structure", "alignment", "incentive", "incentives", "process",
    "processes", "mechanisms", "mechanism", "commitment", "documents",
    "analysis", "releases", "version", "fraction", "adequate", "adequacy",
    "multiple", "several", "critical", "properly", "properly",
    # company names — taxonomy must be model-agnostic
    "anthropic", "openai", "mistral", "deepseek", "google", "microsoft",
    "llama", "gemini", "claude", "grokked", "chatgpt",
    # SUCCESS_SUPPRESSORS — adding these as keywords causes the class's own
    # probe to trigger the success penalty and drop below threshold
    "correctly", "successfully", "properly", "accurately", "appropriately",
    "detected", "prevented", "instructed", "working", "fixed",
    "resolved", "approved",
    # generic tech words that appear in any system — not AI-failure specific
    "database", "query", "queries", "returns", "returned",
})


def tokenize_field(text: str) -> list[str]:
    """Extract plain alpha tokens from a text field — min length 5."""
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return [t for t in text.split() if t.isalpha() and len(t) >= 5]


def expand(failure: dict) -> list[str]:
    """
    Generate candidate tokens from structured taxonomy fields only.
    Excludes examples/case_studies — those are narrative prose and flood
    the candidate set with generic context words.
    Fields weighted by repetition: name and mechanism are most specific.
    """
    fields = [
        failure.get("name", ""),
        failure.get("name", ""),
        failure.get("name", ""),
        failure.get("mechanism", ""),
        failure.get("mechanism", ""),
        failure.get("class_name", ""),
        failure.get("detection", ""),
        failure.get("mitigation", ""),
    ]
    tokens = []
    for field in fields:
        if isinstance(field, str):
            tokens.extend(tokenize_field(field))
    return tokens


def hard_constraints_pass(candidate: str, existing: set[str]) -> bool:
    """
    Evaluate ALL hard constraints immediately.
    Returns False on first violation.
    """
    # C1: length
    if len(candidate) < 4:
        return False
    # C2: alpha only
    if not candidate.isalpha():
        return False
    # C3: stopword
    if candidate in STOPWORDS:
        return False
    # C4: already exists or is substring of existing (or vice versa)
    if candidate in existing:
        return False
    if any(candidate in kw or kw in candidate for kw in existing):
        return False
    return True


def nl_probe_text(failure: dict) -> str:
    """Same probe generation as nl_probe_bank.py."""
    kws = failure.get("keywords") or []
    if len(kws) >= 3:
        return "Observed failure involving " + ", ".join(kws[:6]) + "."
    name = (failure.get("name") or "").lower()
    return " ".join(kws) + (" " + name if name else "")


def probe_passes(failure: dict, clf: PeriodicTableClassifier) -> bool:
    """
    Soft hard constraint: after adding keywords, the class's own NL probe
    must still appear in the top-K results.
    """
    text = nl_probe_text(failure)
    result = clf.classify(text)
    if not result.in_table:
        return False
    top_k = [m.failure_id for m in result.matches[:NL_TOP_K]]
    return failure["id"] in top_k


def enrich_class(failure: dict, clf: PeriodicTableClassifier) -> tuple[list[str], list[str]]:
    """
    Run keyword expansion for one class.
    Returns (added_keywords, rejected_candidates).
    """
    existing = set(failure.get("keywords") or [])
    candidates = expand(failure)

    # Score candidates by frequency — higher freq = more central to the class
    freq = Counter(candidates)
    ranked = sorted(freq.keys(), key=lambda t: (freq[t], len(t)), reverse=True)

    added = []
    rejected = []

    for candidate in ranked:
        # Hard constraint check — prune immediately on violation
        if not hard_constraints_pass(candidate, existing):
            rejected.append(candidate)
            continue

        # Tentatively add and check NL probe constraint
        failure["keywords"] = list(existing) + [candidate]
        if not probe_passes(failure, clf):
            # Probe broke — rollback, reject this candidate
            failure["keywords"] = list(existing)
            rejected.append(f"{candidate}(probe)")
            continue

        # Passed — add to keyword set
        existing.add(candidate)
        added.append(candidate)

    failure["keywords"] = list(existing)
    return added, rejected


def main(dry_run: bool = False) -> None:
    with open(DATA) as f:
        data = json.load(f)

    failures = data["failures"]

    # Build classifier once — used for NL probe constraint
    print("Loading classifier...")
    clf = PeriodicTableClassifier()

    total_added = 0
    total_classes = 0

    for failure in failures:
        before = len(failure.get("keywords") or [])
        added, _ = enrich_class(failure, clf)

        if added:
            total_classes += 1
            total_added += len(added)
            print(f"  {failure['id']:42s}  {before} → {len(failure['keywords'])}  +{added}")

    # Summary
    counts = [len(f.get("keywords") or []) for f in failures]
    print(f"\n{total_classes} classes enriched, {total_added} keywords added")
    print(f"keyword counts: min={min(counts)} max={max(counts)} "
          f"mean={sum(counts)/len(counts):.1f}")

    if not dry_run:
        # Reload classifier with enriched data to verify full suite
        import importlib, src.data_loader as dl
        dl._failures_cache = None  # bust cache
        clf2 = PeriodicTableClassifier()

        # Quick sanity: spot-check first failure in each group
        groups = {}
        for f in failures:
            groups.setdefault(f["group"], f)
        ok = True
        for gname, f in groups.items():
            if not probe_passes(f, clf2):
                print(f"  WARN probe failed after write: {f['id']}")
                ok = False
        if ok:
            print("Spot-check: all group probes pass.")

        with open(DATA, "w") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"Written → {DATA}")
    else:
        print("(dry run — nothing written)")


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
