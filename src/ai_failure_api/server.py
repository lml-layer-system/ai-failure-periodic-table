"""
REST API (v1) — classify text against the 343-class AI Failure Periodic Table.

Security / production hardening:
  - API key auth via X-API-Key header
      Set API_KEYS env var (comma-separated). Unset = open access (dev mode).
  - Rate limiting: 60 classify calls / minute per IP (slowapi)
  - Input capped at 10,000 characters
  - /v1/health actually classifies a probe string and reports classifier status
  - Structured JSON logging on every request: request_id, latency, labels

Install: pip install "ai-failure-periodic-table[api]"
Run:     python -m src.ai_failure_api
    or:  uvicorn src.ai_failure_api.server:app --host 0.0.0.0 --port 8000
"""

from __future__ import annotations

import json
import logging
import os
import time
import uuid
from functools import lru_cache
from typing import Any, Optional

try:
    from fastapi import Depends, FastAPI, HTTPException, Request, Security
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.security.api_key import APIKeyHeader
    from pydantic import BaseModel, Field
    from slowapi import Limiter, _rate_limit_exceeded_handler
    from slowapi.errors import RateLimitExceeded
    from slowapi.util import get_remote_address
except ImportError as e:  # pragma: no cover
    raise SystemExit(
        "Required packages missing. Install with:\n"
        "  pip install 'ai-failure-periodic-table[api]'\n"
        f"Original error: {e}"
    ) from e

from src.classifier import QUESTIONS, PeriodicTableClassifier
from src.data_loader import get_failures, get_groups

# ── Logging — structured JSON to stderr ───────────────────────────────────────

logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[logging.StreamHandler()])
log = logging.getLogger("ai_failure_api")


def _jlog(event: str, **fields: Any) -> None:
    log.info(json.dumps({"event": event, **fields}))


# ── Rate limiter ───────────────────────────────────────────────────────────────

limiter = Limiter(key_func=get_remote_address, default_limits=["200/minute"])

# ── Auth — API key via X-API-Key header ───────────────────────────────────────

_API_KEYS: frozenset[str] = frozenset(
    k.strip() for k in os.environ.get("API_KEYS", "").split(",") if k.strip()
)
_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)


def _require_api_key(api_key: str | None = Security(_KEY_HEADER)) -> None:
    """No-op when API_KEYS is unset (dev mode). Raises 401 on bad key."""
    if _API_KEYS and api_key not in _API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


# ── App ────────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="AI Failure Periodic Table API",
    description=(
        "Classify AI failures against the 343-class structural taxonomy. "
        "Multi-label: every class above the score threshold is returned. "
        "Auth: set X-API-Key header (required when API_KEYS env var is set)."
    ),
    version="1",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
    openapi_url="/v1/openapi.json",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

_ALLOWED_ORIGINS = [o.strip() for o in os.environ.get("CORS_ORIGINS", "*").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_ALLOWED_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# ── Request logging middleware ─────────────────────────────────────────────────

@app.middleware("http")
async def _log_requests(request: Request, call_next):
    request_id = uuid.uuid4().hex[:8]
    request.state.request_id = request_id
    t0 = time.perf_counter()
    response = await call_next(request)
    _jlog(
        "request",
        request_id=request_id,
        method=request.method,
        path=request.url.path,
        status=response.status_code,
        latency_ms=round((time.perf_counter() - t0) * 1000, 1),
    )
    response.headers["X-Request-Id"] = request_id
    return response


# ── Singleton classifier ───────────────────────────────────────────────────────

@lru_cache(maxsize=1)
def _clf() -> PeriodicTableClassifier:
    return PeriodicTableClassifier()


# ── Schemas ────────────────────────────────────────────────────────────────────

class ClassifyRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=10_000, description="Description to classify")
    top_k: int = Field(10, ge=1, le=343, description="Max matches to return")


class MatchOut(BaseModel):
    id: str
    name: str
    group: str
    class_name: str
    mechanism: str
    detection: str
    severity: str
    score: float
    matched_keywords: list[str]


class ClassifyResponse(BaseModel):
    in_table: bool
    verdict: str
    labels: list[str]
    dimensions_activated: list[str]
    matches: list[MatchOut]
    closest: list[MatchOut]
    execution_time_ms: float


class ClassOut(BaseModel):
    id: str
    name: str
    group: str
    group_id: int
    class_code: str
    class_name: str
    mechanism: str
    forbidden: str
    detection: str
    mitigation: str
    severity: str
    keywords: list[str]


class GroupOut(BaseModel):
    id: int
    name: str
    code: str
    question: str


# ── Endpoints ──────────────────────────────────────────────────────────────────

_HEALTH_PROBE = "prompt injection jailbreak hallucination"
_HEALTH_PROBE_EXPECT = True   # must be in_table


@app.get("/v1/health", tags=["meta"])
def health() -> dict[str, Any]:
    """
    Liveness + readiness check. Classifies a known probe string and verifies
    the classifier returns an in-table result. Returns HTTP 503 if degraded.
    """
    t0 = time.perf_counter()
    probe_result = _clf().classify(_HEALTH_PROBE)
    latency_ms = round((time.perf_counter() - t0) * 1000, 1)

    classifier_ok = probe_result.in_table == _HEALTH_PROBE_EXPECT
    status = "ok" if classifier_ok else "degraded"

    body: dict[str, Any] = {
        "status": status,
        "version": "1",
        "classes": 343,
        "classifier": "ok" if classifier_ok else "degraded",
        "probe_in_table": probe_result.in_table,
        "probe_top_label": probe_result.labels[0] if probe_result.labels else None,
        "probe_latency_ms": latency_ms,
    }

    if not classifier_ok:
        raise HTTPException(status_code=503, detail=body)
    return body


@app.post("/v1/classify", response_model=ClassifyResponse, tags=["classify"])
@limiter.limit("60/minute")
def classify(
    request: Request,
    body: ClassifyRequest,
    _auth: None = Depends(_require_api_key),
) -> ClassifyResponse:
    """
    Classify a description against the 343-class table (multi-label).
    Rate limited to 60 calls/minute per IP.
    """
    clf = _clf()
    result = clf.classify(body.text)
    request_id = getattr(request.state, "request_id", "-")

    _jlog(
        "classify",
        request_id=request_id,
        in_table=result.in_table,
        label_count=len(result.labels),
        top_labels=result.labels[:5],
        latency_ms=round(result.execution_time_ms, 1),
    )

    def _to_match(m) -> MatchOut:
        return MatchOut(
            id=m.failure_id,
            name=m.name,
            group=m.group,
            class_name=m.class_name,
            mechanism=m.mechanism,
            detection=m.detection,
            severity=m.severity,
            score=round(m.score, 4),
            matched_keywords=m.matched_keywords,
        )

    return ClassifyResponse(
        in_table=result.in_table,
        verdict=result.verdict,
        labels=result.labels,
        dimensions_activated=result.dimensions_activated,
        matches=[_to_match(m) for m in result.matches[: body.top_k]],
        closest=[_to_match(m) for m in result.closest],
        execution_time_ms=round(result.execution_time_ms, 3),
    )


@app.get("/v1/classes", response_model=list[ClassOut], tags=["taxonomy"])
@limiter.limit("30/minute")
def list_classes(
    request: Request,
    group: Optional[str] = None,
    severity: Optional[str] = None,
    _auth: None = Depends(_require_api_key),
) -> list[ClassOut]:
    """List all 343 failure classes. Optional filters: group, severity."""
    rows = get_failures()
    if group:
        rows = [r for r in rows if r.get("group", "").upper() == group.upper()]
    if severity:
        rows = [r for r in rows if r.get("severity", "STANDARD").upper() == severity.upper()]
    return [_failure_to_out(r) for r in rows]


@app.get("/v1/class/{failure_id}", response_model=ClassOut, tags=["taxonomy"])
@limiter.limit("120/minute")
def get_class(
    request: Request,
    failure_id: str,
    _auth: None = Depends(_require_api_key),
) -> ClassOut:
    """Look up a single failure class by ID (e.g. EPIS-STRUCT-HALL-001)."""
    row = _clf().lookup(failure_id)
    if row is None:
        raise HTTPException(status_code=404, detail=f"Class '{failure_id}' not found")
    return _failure_to_out(row)


@app.get("/v1/groups", response_model=list[GroupOut], tags=["taxonomy"])
def list_groups(_auth: None = Depends(_require_api_key)) -> list[GroupOut]:
    """Return the 7 structural dimension groups."""
    out = []
    for q_num, group_code, question in QUESTIONS:
        out.append(GroupOut(id=q_num, name=group_code, code=group_code, question=question))
    return out


# ── Helpers ────────────────────────────────────────────────────────────────────

def _failure_to_out(r: dict) -> ClassOut:
    return ClassOut(
        id=r["id"],
        name=r["name"],
        group=r.get("group", ""),
        group_id=r.get("group_id", 0),
        class_code=r.get("class_code", ""),
        class_name=r.get("class_name", ""),
        mechanism=r.get("mechanism", ""),
        forbidden=r.get("forbidden", ""),
        detection=r.get("detection", ""),
        mitigation=r.get("mitigation", ""),
        severity=r.get("severity", "STANDARD"),
        keywords=r.get("keywords", []),
    )
