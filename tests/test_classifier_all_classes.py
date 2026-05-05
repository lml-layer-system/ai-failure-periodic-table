"""Part A: each class id is recognized when passed as input (343 cases)."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.classifier import PeriodicTableClassifier
from src.data_loader import get_failures

_FAILURE_IDS = [f["id"] for f in get_failures()]


@pytest.fixture(scope="module")
def clf() -> PeriodicTableClassifier:
    return PeriodicTableClassifier()


@pytest.mark.parametrize("failure_id", _FAILURE_IDS, ids=lambda fid: fid)
def test_class_id_classifies_as_that_class(clf: PeriodicTableClassifier, failure_id: str) -> None:
    result = clf.classify(failure_id)
    assert result.in_table, f"{failure_id}: expected in_table"
    assert any(m.failure_id == failure_id for m in result.matches), (
        f"{failure_id}: not in matches — got {[m.failure_id for m in result.matches[:5]]}"
    )
