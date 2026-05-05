"""MCP protection() tool — isolated from real ~/.ai-failure-periodic-table via path monkeypatch."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path

import pytest

# Requires mcp package (same as src.ai_failure_mcp.server).
pytest.importorskip("mcp.server.fastmcp")

import src.ai_failure_mcp.server as server


@pytest.fixture
def protection_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    p = tmp_path / "setup.json"
    monkeypatch.setattr(server, "_PROTECTION_SETUP_PATH", p)
    return p


def test_protection_status_when_no_file(protection_path: Path) -> None:
    out = asyncio.run(server.protection("status"))
    data = json.loads(out)
    assert data["buccet_active"] is False
    assert "question" in data
    assert not protection_path.exists()


def test_protection_yes_writes_setup(protection_path: Path) -> None:
    out = asyncio.run(server.protection("yes"))
    data = json.loads(out)
    assert data["preference_recorded"] is True
    assert data["buccet_active"] is False
    assert "config" in data
    assert data["config"]["mcpServers"]["buccet"]["command"] == "buccet"
    saved = json.loads(protection_path.read_text())
    assert saved["protection_choice"] == "yes"


def test_protection_no_writes_setup(protection_path: Path) -> None:
    out = asyncio.run(server.protection("no"))
    data = json.loads(out)
    assert data["preference_recorded"] is True
    assert data["buccet_active"] is False
    saved = json.loads(protection_path.read_text())
    assert saved["protection_choice"] == "no"


def test_protection_status_after_yes(protection_path: Path) -> None:
    asyncio.run(server.protection("yes"))
    out = asyncio.run(server.protection("status"))
    data = json.loads(out)
    assert data["preference"] == "yes"
    assert data["buccet_active"] is False
    assert "note" in data


def test_protection_invalid_choice(protection_path: Path) -> None:
    out = asyncio.run(server.protection("maybe"))
    data = json.loads(out)
    assert "error" in data
    assert data["response_contract"]["error_response"] is True
