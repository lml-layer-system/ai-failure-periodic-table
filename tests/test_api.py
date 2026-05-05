"""v1 REST API endpoint tests — requires fastapi, slowapi, and httpx."""

from __future__ import annotations

import os
import pytest

try:
    from fastapi.testclient import TestClient
    from src.ai_failure_api.server import app
    _FASTAPI_AVAILABLE = True
except ImportError:
    _FASTAPI_AVAILABLE = False

pytestmark = pytest.mark.skipif(
    not _FASTAPI_AVAILABLE, reason="fastapi not installed"
)


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


# ── /v1/health ────────────────────────────────────────────────────────────────

def test_health_ok(client):
    r = client.get("/v1/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["classifier"] == "ok"
    assert body["classes"] == 343
    assert body["probe_in_table"] is True
    assert body["probe_top_label"] is not None
    assert isinstance(body["probe_latency_ms"], float)


def test_health_returns_request_id_header(client):
    r = client.get("/v1/health")
    assert "x-request-id" in r.headers
    assert len(r.headers["x-request-id"]) == 8


# ── /v1/classify — core ───────────────────────────────────────────────────────

def test_classify_known_failure(client):
    r = client.post("/v1/classify", json={"text": "The model hallucinated a citation that does not exist."})
    assert r.status_code == 200
    body = r.json()
    assert body["in_table"] is True
    assert body["labels"]
    assert body["matches"]
    top = body["matches"][0]
    assert "id" in top and "score" in top and "mechanism" in top
    assert body["labels"] == [m["id"] for m in body["matches"]]


def test_classify_multi_label_returns_all(client):
    r = client.post("/v1/classify", json={"text": "prompt injection exfiltrate system prompt"})
    assert r.status_code == 200
    body = r.json()
    assert body["in_table"] is True
    assert len(body["labels"]) >= 1


def test_classify_non_failure_not_in_table(client):
    r = client.post("/v1/classify", json={"text": "How do I make pasta carbonara?"})
    assert r.status_code == 200
    body = r.json()
    assert body["in_table"] is False
    assert body["labels"] == []
    assert body["closest"]


def test_classify_success_framed_not_in_table(client):
    r = client.post("/v1/classify", json={"text": "The model correctly refused a harmful request."})
    assert r.status_code == 200
    assert r.json()["in_table"] is False


def test_classify_top_k_respected(client):
    r = client.post("/v1/classify", json={
        "text": "The model hallucinated a citation that does not exist.",
        "top_k": 2,
    })
    assert r.status_code == 200
    assert len(r.json()["matches"]) <= 2


def test_classify_response_has_dimensions(client):
    r = client.post("/v1/classify", json={"text": "jailbreak bypass prompt injection hallucination"})
    assert r.status_code == 200
    assert isinstance(r.json()["dimensions_activated"], list)


def test_classify_returns_request_id_header(client):
    r = client.post("/v1/classify", json={"text": "jailbreak"})
    assert "x-request-id" in r.headers


# ── /v1/classify — input validation ──────────────────────────────────────────

def test_classify_empty_rejected(client):
    r = client.post("/v1/classify", json={"text": ""})
    assert r.status_code == 422


def test_classify_input_too_long_rejected(client):
    r = client.post("/v1/classify", json={"text": "x" * 10_001})
    assert r.status_code == 422


def test_classify_input_at_limit_accepted(client):
    r = client.post("/v1/classify", json={"text": "a" * 10_000})
    assert r.status_code == 200


# ── Auth ──────────────────────────────────────────────────────────────────────

def test_auth_open_when_no_keys_configured(client):
    """When API_KEYS env var is unset, all requests pass."""
    r = client.post("/v1/classify", json={"text": "jailbreak"})
    assert r.status_code == 200


def test_auth_rejects_bad_key(client, monkeypatch):
    import src.ai_failure_api.server as srv
    monkeypatch.setattr(srv, "_API_KEYS", frozenset({"secret-key-123"}))
    r = client.post("/v1/classify", json={"text": "jailbreak"},
                    headers={"X-API-Key": "wrong-key"})
    assert r.status_code == 401


def test_auth_accepts_valid_key(client, monkeypatch):
    import src.ai_failure_api.server as srv
    monkeypatch.setattr(srv, "_API_KEYS", frozenset({"secret-key-123"}))
    r = client.post("/v1/classify", json={"text": "jailbreak"},
                    headers={"X-API-Key": "secret-key-123"})
    assert r.status_code == 200


def test_auth_rejects_missing_key(client, monkeypatch):
    import src.ai_failure_api.server as srv
    monkeypatch.setattr(srv, "_API_KEYS", frozenset({"secret-key-123"}))
    r = client.post("/v1/classify", json={"text": "jailbreak"})
    assert r.status_code == 401


# ── /v1/classes ───────────────────────────────────────────────────────────────

def test_list_classes_all(client):
    r = client.get("/v1/classes")
    assert r.status_code == 200
    classes = r.json()
    assert len(classes) == 343
    first = classes[0]
    assert "id" in first and "name" in first and "keywords" in first


def test_list_classes_group_filter(client):
    r = client.get("/v1/classes?group=EPISTEMIC")
    assert r.status_code == 200
    classes = r.json()
    assert all(c["group"] == "EPISTEMIC" for c in classes)
    assert len(classes) > 0


def test_list_classes_severity_filter(client):
    r = client.get("/v1/classes?severity=CRITICAL")
    assert r.status_code == 200
    assert all(c["severity"] == "CRITICAL" for c in r.json())


# ── /v1/class/{id} ────────────────────────────────────────────────────────────

def test_get_class_known(client):
    r = client.get("/v1/class/EPIS-STRUCT-HALL-001")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == "EPIS-STRUCT-HALL-001"
    assert body["keywords"]
    assert body["mechanism"]


def test_get_class_case_insensitive(client):
    r = client.get("/v1/class/epis-struct-hall-001")
    assert r.status_code == 200
    assert r.json()["id"] == "EPIS-STRUCT-HALL-001"


def test_get_class_not_found(client):
    r = client.get("/v1/class/DOES-NOT-EXIST-999")
    assert r.status_code == 404


# ── /v1/groups ────────────────────────────────────────────────────────────────

def test_list_groups(client):
    r = client.get("/v1/groups")
    assert r.status_code == 200
    groups = r.json()
    assert len(groups) == 7
    names = {g["name"] for g in groups}
    assert "EPISTEMIC" in names
    assert "ADVERSARIAL" in names
    assert "GOVERNANCE" in names
