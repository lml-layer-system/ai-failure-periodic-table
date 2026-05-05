"""Part B probe bank (343). Bump NL_PROBE_BANK_VERSION if probe shape or K changes."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator, NamedTuple

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.classifier import PeriodicTableClassifier
from src.data_loader import get_failures

# Keep in sync with assertion strictness in test_classifier_nl_probes.py
NL_PROBE_BANK_VERSION = 1
NL_PROBE_TOP_K = 3


class NLProbe(NamedTuple):
    failure_id: str
    text: str


def build_nl_probe_text(failure: dict) -> str:
    """Synthetic incident line from keywords (no class ID in text)."""
    kws = failure.get("keywords") or []
    if len(kws) >= 3:
        return "Observed failure involving " + ", ".join(kws[:6]) + "."
    name = (failure.get("name") or "").lower()
    return " ".join(kws) + (" " + name if name else "")


def iter_nl_probes() -> Iterator[NLProbe]:
    for f in get_failures():
        yield NLProbe(failure_id=f["id"], text=build_nl_probe_text(f))


def expected_top_k_ids(result, k: int) -> list[str]:
    return [m.failure_id for m in result.matches[:k]]


def threshold() -> float:
    return PeriodicTableClassifier.THRESHOLD
