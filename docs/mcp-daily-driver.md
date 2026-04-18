# MCP daily driver (Cursor / stdio)

Personal, **on-demand** classification against the **343-class** table. This layer is **read-only**: it loads `data/failures.json` and `data/search_index.json` and **never** edits the repo (contrast with [Freshness Watch](freshness-watch.md)).

## Install

From the repository root:

```bash
pip install -e ".[mcp]"
```

Ensure the TF-IDF index exists (for `search_failures` and semantic columns in classify tools):

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
| `classify_text` | Full pass: keyword classifier, 7-dimension view, TF-IDF top hits, each with **`suggested_structural_response`** |
| `classify_url` | Fetch **http(s)** public URL → extract text → same bundle (blocks localhost/private IPs) |
| `classify_document` | Read **UTF-8 file under repo root** → same bundle |
| `search_failures` | TF-IDF search only; each hit includes **`suggested_structural_response`** |
| `get_class` | Lookup by class ID; returns record + **`suggested_structural_response`** |
| `compound_hint` | Like `classify_text` plus explicit **compound** reading and consolidated structural mitigations |

### Suggested structural response

For every class, the server returns taxonomy fields only:

- **what** — `mechanism`
- **control_principle_forbidden** — `forbidden`
- **detection_pattern** — `detection`
- **structural_mitigation** — `mitigation`
- **mitigation_domain** — `mit_domain` when present

These are **structural** patterns from the periodic table, not stack-specific runbooks or vendor steps.

## Cursor configuration

In **Cursor Settings → MCP**, add a server (adjust paths and Python):

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

Use the same `python3` where you ran `pip install -e ".[mcp]"`.

A copy-paste template lives at [docs/cursor-mcp-config.example.json](cursor-mcp-config.example.json).

## Security notes

- **`classify_url`**: Only `http`/`https`; resolves host and blocks loopback, private, and link-local targets.
- **`classify_document`**: Only files that resolve **inside** the repository root.
