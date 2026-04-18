# MCP daily driver (Cursor / stdio)

Personal **scientific / falsification surface** against the **343-class** table: point at text, a public URL, or a file path, and see **how strongly** the current ontology resolves the input—not a blind “yes/no” wrapper.

This layer is **read-only**: it loads `data/failures.json` and `data/search_index.json` and **never** edits the repo. It is **not** [Freshness Watch](freshness-watch.md) (the official weekly review pipeline).

## Install

From the repository root:

```bash
pip install -e ".[mcp]"
```

Ensure the TF-IDF index exists (for `search_failures` and semantic evidence inside classify tools):

```bash
python scripts/generate_embeddings.py
```

## Run

```bash
python -m src.ai_failure_mcp
```

Or the console script (after install):

```bash
ai-failure-mcp
```

The process speaks **MCP over stdio**; do not pipe extra data into stdin.

## Tools

| Tool | Purpose |
|------|---------|
| `classify_text` | Full pass: keyword classifier, 7-dimension view, TF-IDF hits, **`suggested_structural_response`** (WHAT only), plus **`fit_state`**, **`fit_confidence`**, **`scientific_summary`**, CONTRIBUTING-grounded **`report_preparation`** |
| `classify_url` | Fetch **http(s)** public URL → extract text → same bundle (blocks localhost/private IPs) |
| `classify_document` | Read **UTF-8** file under **repo root** and/or **`AI_FAILURE_MCP_DOCUMENT_ROOT(S)`** → same bundle |
| `classify_document_path` | **Alias** of `classify_document` for clients that want an explicit path-oriented tool name |
| `search_failures` | TF-IDF retrieval; each hit includes **`suggested_structural_response`**; meta envelope explains this is **not** a classifier verdict (`fit_state`: `not_applicable`) |
| `get_class` | Lookup by class ID; record + structural fields + envelope (`fit_state`: `not_applicable` — classify narrative text separately) |
| `compound_hint` | Same envelope as `classify_text`; encourages **compound** reading when multiple dimensions activate; consolidated structural mitigations |

### Fit state & confidence (classify_* and `compound_hint`)

- **`fit_state`**: `strong_fit` · `compound_fit` · `weak_fit` · `possible_gap_candidate` (derived from keyword scores, activated dimensions, and keyword vs semantic agreement).
- **`fit_confidence`**: `high` · `medium` · `low`.
- **`fit_evidence`**: numeric/debug hints (scores, agreement flags)—for transparency, not for end-user spin.

### Boundary pressure & repo-native next steps

When fit is weak or ambiguous, responses include:

- **`boundary_pressure_note`** — what is uncertain about the mapping.
- **`what_to_do_next`** — plain-language path grounded in **[CONTRIBUTING.md](../CONTRIBUTING.md)** (sub-mode → compound → invariant → mechanism vs cause; §2–§4 issue templates).
- **`recommended_repo_action`** — structured: `issue_type`, template path, rationale.
- **`report_preparation`** — **`recommended_issue_type`**, **`why_this_issue_type`**, **`closest_existing_classes`**, **`questions_to_answer_before_reporting`**, **`suggested_report_inputs`** so **another AI** can draft the right GitHub issue (`Propose New Class`, `Report Real Incident`, `Improve Keywords`, `Challenge Classification`).

Issue template paths mirror CONTRIBUTING:

- `.github/ISSUE_TEMPLATE/propose_new_class.md`
- `.github/ISSUE_TEMPLATE/report_real_incident.md`
- `.github/ISSUE_TEMPLATE/improve_keywords.md`
- `.github/ISSUE_TEMPLATE/challenge_classification.md`

### `scientific_summary` block

Concise, host-friendly recap: mechanism observation, primary/secondary reading, possible gap flag, structural response summary (WHAT), uncertainty notes, and recommended action string.

### Suggested structural response (WHAT, not HOW)

For every class hit, the server returns taxonomy fields only:

- **what** — `mechanism`
- **control_principle_forbidden** — `forbidden`
- **detection_pattern** — `detection`
- **structural_mitigation** — `mitigation`
- **mitigation_domain** — `mit_domain` when present

No vendor runbooks, no stack-specific implementation steps.

## Personal documents outside the repo

By default, `classify_document` accepts paths under the **repository root**. To allow a **personal workspace** (e.g. iCloud notes) **without** copying files into the repo, set **one or both**:

- **`AI_FAILURE_MCP_DOCUMENT_ROOT`** — single absolute directory.
- **`AI_FAILURE_MCP_DOCUMENT_ROOTS`** — multiple absolute directories, separated by **`:`** (or **`;`** if any entry contains `:`).

The resolved file path must still lie **under** one of those roots (plus the repo). This does **not** weaken `classify_url` rules (still no localhost/private fetches).

In **Cursor MCP** server config you can pass env vars if your client supports them, e.g.:

```json
{
  "mcpServers": {
    "ai-failure-periodic-table": {
      "command": "python3",
      "args": ["-m", "src.ai_failure_mcp"],
      "cwd": "/absolute/path/to/ai-failure-periodic-table",
      "env": {
        "AI_FAILURE_MCP_DOCUMENT_ROOT": "/Users/you/Documents/ai-failure-notes"
      }
    }
  }
}
```

## Cursor configuration (minimal)

```json
{
  "mcpServers": {
    "ai-failure-periodic-table": {
      "command": "python3",
      "args": ["-m", "src.ai_failure_mcp"],
      "cwd": "/absolute/path/to/ai-failure-periodic-table"
    }
  }
}
```

A copy-paste template lives at [docs/cursor-mcp-config.example.json](cursor-mcp-config.example.json).

## Security notes

- **`classify_url`**: Only `http`/`https`; resolves host and blocks loopback, private, and link-local targets.
- **`classify_document` / `classify_document_path`**: File must resolve under **repo root** and/or **`AI_FAILURE_MCP_DOCUMENT_ROOT(S)`**; arbitrary system paths are rejected.

## Doctrine

- **Test the ontology**, don’t fabricate confidence: strong fits remain defeasible; `possible_gap_candidate` is an honest invitation to use CONTRIBUTING checklists and issues.
- **Freshness Watch** stays the scheduled, maintainer-facing pipeline; the daily driver never writes taxonomy data.
