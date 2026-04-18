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
| `classify_text` | Full pass: keyword classifier (the **only** accept/reject gate), 7-dimension view, TF-IDF hits (advisory), **`response_contract`**, **`classifier_hit`**, **`contributing_route`**, **`fit_state`**, **`fit_confidence`**, **`scientific_summary`**, CONTRIBUTING **`report_preparation`**, **`suggested_structural_response`** (WHAT only) |
| `classify_url` | Fetch **http(s)** public URL → extract text → same bundle (blocks localhost/private IPs) |
| `classify_document` | Read **UTF-8** file under **repo root** and/or **`AI_FAILURE_MCP_DOCUMENT_ROOT(S)`** → same bundle |
| `classify_document_path` | **Alias** of `classify_document` for clients that want an explicit path-oriented tool name |
| `search_failures` | TF-IDF retrieval; **`response_contract.verdict_applicable: false`**; each hit includes **`suggested_structural_response`**; `fit_state`: `not_applicable` |
| `get_class` | Lookup by ID; **`response_contract.verdict_applicable: false`**; `fit_state`: `not_applicable` — run **`classify_*`** on narrative text for a verdict |
| `compound_hint` | Same envelope as `classify_text`; encourages **compound** reading when multiple dimensions activate; consolidated structural mitigations |

### Classifier verdict, fit summary, and confidence (classify_* and `compound_hint`)

**What it’s for:** the periodic-table **keyword classifier** decides **hit vs miss** (`in_table`, also exposed as **`classifier_hit`**). There is no second “acceptance engine”: TF-IDF / semantic hits are **extra context** in `fit_evidence` (e.g. whether the semantic top differs from the keyword primary). **`contributing_route`** is the recommended CONTRIBUTING issue path derived from that verdict and the same classifier signals (matches, dimensions, neighbour scores)—not from overriding the table with semantic scores.

- **`classifier_hit`**: same as **`in_table`** — at least one class met the classifier’s keyword threshold.
- **`contributing_route`**: suggested next step type (`none`, `improve_keywords`, `report_real_incident`, `propose_new_class`, …) aligned with [CONTRIBUTING.md](../CONTRIBUTING.md).
- **`fit_state`**: short **summary of the classifier outcome**, not a parallel taxonomy:
  - **`possible_gap_candidate`** — classifier **miss** (nothing accepted).
  - **`compound_fit`** — hit with **multiple structural dimensions** activated (compound reading).
  - **`strong_fit`** — hit with a **clear** primary score (well above the same threshold the classifier uses).
  - **`weak_fit`** — hit but **marginal** primary score (still accepted by the table’s rules).
- **`fit_confidence`**: `high` · `medium` · `low` — coarse certainty **on top of** the classifier verdict (e.g. miss → low).
- **`fit_evidence`**: scores, thresholds, dimension counts, optional **cross-modal hints** (keyword vs semantic)—for transparency; semantic disagreement does **not** replace `classifier_hit`.

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

### `response_contract` (every tool)

Stable JSON for **clients and downstream agents** — check this before interpreting scores:

| Field | `classify_*` / `compound_hint` | `search_failures` / `get_class` | Error payloads |
|--------|----------------------------------|----------------------------------|----------------|
| `schema_version` | `"1"` | `"1"` | `"1"` |
| `verdict_applicable` | `true` | `false` | `false` |
| `verdict_authority` | `periodic_table_keyword_classifier` | *(absent)* | *(absent)* |
| `error_response` | — | — | `true` |

- **Classification tools:** lists `verdict_boolean_fields` (`classifier_hit`, `in_table`), `fit_state_role`, `semantic_evidence_advisory_only`, `advisory_semantic_paths`, and `contributing_route_field`.
- **Non-verdict tools:** `instruction` tells you to run `classify_*` for a real verdict.
- **Errors:** `error_response: true` — fix the `error` field; do not treat the payload as classification output.

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

- **One gate:** the table’s classifier accepts or rejects; everything else (including TF-IDF) informs narrative and **CONTRIBUTING** routing, it does not invent a second “did it fit?” authority.
- **Test the ontology**, don’t fabricate confidence: strong fits remain defeasible; on a miss, `possible_gap_candidate` plus CONTRIBUTING paths are an honest map—not a hidden alternate classifier.
- **Freshness Watch** stays the scheduled, maintainer-facing pipeline; the daily driver never writes taxonomy data.
