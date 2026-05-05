"""Part B: each probe’s expected class is in the top-K matches."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_REPO_ROOT))
sys.path.insert(0, str(Path(__file__).parent))

from src.classifier import PeriodicTableClassifier

import nl_probe_bank as _bank

NL_PROBE_BANK_VERSION = _bank.NL_PROBE_BANK_VERSION
NL_PROBE_TOP_K = _bank.NL_PROBE_TOP_K
build_nl_probe_text = _bank.build_nl_probe_text
expected_top_k_ids = _bank.expected_top_k_ids
iter_nl_probes = _bank.iter_nl_probes

_FAILURE_IDS = [p.failure_id for p in iter_nl_probes()]


@pytest.fixture(scope="module")
def clf() -> PeriodicTableClassifier:
    return PeriodicTableClassifier()


@pytest.mark.parametrize("failure_id", _FAILURE_IDS, ids=lambda fid: fid)
def test_nl_probe_expected_class_in_top_k(clf: PeriodicTableClassifier, failure_id: str) -> None:
    from src.data_loader import get_failures

    row = next(f for f in get_failures() if f["id"] == failure_id)
    text = build_nl_probe_text(row)
    assert failure_id not in text.upper() and failure_id.lower() not in text.lower()

    result = clf.classify(text)
    assert result.in_table, f"{failure_id}: expected in_table for nl probe v{NL_PROBE_BANK_VERSION}"
    top_k = expected_top_k_ids(result, NL_PROBE_TOP_K)
    assert failure_id in top_k, (
        f"{failure_id}: not in top-{NL_PROBE_TOP_K} "
        f"(got {top_k}, bank v{NL_PROBE_BANK_VERSION})"
    )


@pytest.mark.parametrize(
    "junk",
    [
        "© 2026 Example Corp. All rights reserved.",
        "5 12 45 102",
        "References: [1] arXiv:1234.5678 [2] doi:10.0000/example",
        "     \n\t  ",
    ],
    ids=["copyright", "page_numbers", "bibliography", "whitespace"],
)
def test_boilerplate_and_junk_not_in_table(clf: PeriodicTableClassifier, junk: str) -> None:
    result = clf.classify(junk)
    assert not result.in_table


@pytest.mark.parametrize(
    "text",
    [
        # Success-framed — correct behaviour is not a failure
        "The model correctly refused a harmful request",
        "The AI successfully detected and blocked the prompt injection attempt",
        "Safety filters properly prevented the jailbreak",
        "The system accurately identified and rejected the phishing content",
        "The model appropriately declined to provide dangerous information",
        "Content moderation correctly flagged and removed the violating post",
        # Benign everyday queries — no AI failure
        "What is the weather like in San Francisco today?",
        "How do I make pasta carbonara?",
        "The team won the championship last night",
        "Please summarize this quarterly earnings report",
        "Translate this paragraph into Spanish",
        # Generic technical text — not AI failure descriptions
        "Memory usage peaked at 4GB during the benchmark run",
        "The database query returned 500 rows in 12ms",
        "Deployment completed successfully with zero downtime",
        "All unit tests passed after the refactor",
    ],
    ids=[
        "correct_refusal", "blocked_injection", "prevented_jailbreak",
        "rejected_phishing", "declined_dangerous", "content_moderation_correct",
        "weather_query", "cooking_query", "sports_result",
        "summarize_request", "translate_request",
        "memory_benchmark", "database_query", "deployment_success", "tests_passed",
    ],
)
def test_non_failures_not_in_table(clf: PeriodicTableClassifier, text: str) -> None:
    result = clf.classify(text)
    assert not result.in_table, (
        f"False positive: {text!r} matched {result.matches[0].failure_id} "
        f"(score={result.matches[0].score:.3f})"
    )
