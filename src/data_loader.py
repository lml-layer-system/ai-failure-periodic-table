"""
Data loader for the AI Failure Periodic Table.
Loads and validates failures.json.
"""

import json
from pathlib import Path
from typing import Any

_DATA_PATH = Path(__file__).parent.parent / "data" / "failures.json"
_cache: dict[str, Any] | None = None


def load_data(path: Path | None = None) -> dict[str, Any]:
    """Load and cache the failures data."""
    global _cache
    if _cache is not None and path is None:
        return _cache

    target = path or _DATA_PATH
    if not target.exists():
        raise FileNotFoundError(
            f"failures.json not found at {target}. "
            "Run scripts/extract_failures.py to generate it."
        )

    with open(target, encoding="utf-8") as f:
        data = json.load(f)

    _validate(data)
    if path is None:
        _cache = data
    return data


def get_failures(path: Path | None = None) -> list[dict]:
    """Return the list of all failure class records."""
    return load_data(path)["failures"]


def get_groups(path: Path | None = None) -> list[dict]:
    """Return the list of group definitions."""
    return load_data(path)["groups"]


def _validate(data: dict) -> None:
    """Raise ValueError if data doesn't meet schema requirements."""
    if "failures" not in data:
        raise ValueError("Missing 'failures' key in data")
    if "groups" not in data:
        raise ValueError("Missing 'groups' key in data")
    if len(data["failures"]) != data.get("total_classes", 0):
        raise ValueError(
            f"total_classes={data.get('total_classes')} but "
            f"len(failures)={len(data['failures'])}"
        )
    required_fields = {"id", "name", "group_id", "group", "mechanism", "forbidden", "keywords"}
    for i, f in enumerate(data["failures"]):
        missing = required_fields - set(f.keys())
        if missing:
            raise ValueError(f"Failure[{i}] missing fields: {missing}")
