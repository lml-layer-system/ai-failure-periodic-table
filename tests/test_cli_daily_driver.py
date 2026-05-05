"""CLI --daily-driver emits the same envelope keys as MCP classification_bundle."""

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "src.cli", *args],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )


def test_daily_driver_single_has_mcp_envelope():
    proc = _run_cli(
        "--daily-driver",
        "The attacker used prompt injection to exfiltrate the system prompt via markdown.",
    )
    assert proc.returncode == 0, proc.stderr
    data = json.loads(proc.stdout)
    assert data["source"] == "cli"
    assert data["in_table"] is True
    assert data["classifier_hit"] is True
    assert data["response_contract"]["verdict_applicable"] is True
    assert "fit_state" in data
    assert "contributing_route" in data
    assert "report_preparation" in data
    assert "scientific_summary" in data
    assert data["response_kind"] == "classification"


def test_daily_driver_lookup_has_envelope():
    proc = _run_cli("--lookup", "ADV-INDIRECT-INJECT-122", "--daily-driver")
    assert proc.returncode == 0, proc.stderr
    data = json.loads(proc.stdout)
    assert data["source"] == "cli"
    assert data["response_kind"] == "class_lookup"
    assert data["response_contract"]["verdict_applicable"] is False


def test_daily_driver_rejects_with_json():
    proc = _run_cli("--json", "--daily-driver", "test")
    assert proc.returncode != 0


def test_daily_driver_unknown_lookup_error_contract():
    proc = _run_cli("--lookup", "NOT-A-REAL-ID-999", "--daily-driver")
    assert proc.returncode == 1
    data = json.loads(proc.stdout)
    assert data["error"] == "unknown class id"
    assert data["response_contract"]["error_response"] is True
