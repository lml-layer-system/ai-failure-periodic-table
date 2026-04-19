# Architecture

For **end users**: classifying from the terminal → [docs/how-to-use.md](docs/how-to-use.md); **MCP / everyday AI** → [docs/mcp-daily-driver.md](docs/mcp-daily-driver.md).

This document describes **repository layout**, **data flow**, **core modules**, **MCP**, **CI**, and **contributor workflows**.

---

## Repo layout (current)

```
ai-failure-periodic-table/
│
├── data/
│   ├── failures.json           # Taxonomy — single source of truth (343 classes)
│   ├── search_index.json       # TF-IDF index (from scripts/generate_embeddings.py)
│   ├── freshness_sources.json  # RSS/Atom sources for Freshness Watch
│   └── embeddings_meta.json    # Embedding build metadata (optional)
│
├── src/
│   ├── classifier.py           # PeriodicTableClassifier — keyword + stem + synonyms
│   ├── data_loader.py          # Load & validate failures.json
│   ├── cli.py                  # CLI: python -m src.cli (incl. --daily-driver MCP-shaped JSON)
│   ├── tfidf_search.py         # TF-IDF class search (MCP + scripts)
│   ├── freshness_feed.py       # Feed parse / helpers for Freshness Watch
│   └── ai_failure_mcp/         # MCP stdio server (daily driver)
│       ├── server.py           # FastMCP tools: classify_*, search_failures, get_class, compound_hint, protection
│       ├── bridge.py           # Bundles, URL fetch, document paths, semantic wrapper
│       ├── scientific_envelope.py  # fit_state, CONTRIBUTING-shaped guidance (classifier-first)
│       └── response_contract.py    # Stable JSON contract per response kind
│
├── scripts/
│   ├── extract_failures.py     # Markdown → failures.json (maintainer)
│   ├── generate_taxonomy.py    # failures.json → TAXONOMY.md
│   ├── generate_embeddings.py  # failures.json → search_index.json
│   ├── semantic_search.py      # CLI TF-IDF search
│   ├── classify_external_report.py  # Chunk PDF/HTML → classifier reports
│   ├── freshness_watch.py      # Feeds → review packets (no auto taxonomy edit)
│   ├── enrich_*.py, add_mitigation_*.py, …  # Historical / batch data tooling
│   └── generate_visual.py      # Static site / index artifacts
│
├── tests/
│   ├── test_classifier.py
│   ├── test_data_integrity.py
│   ├── test_tfidf_search.py
│   ├── test_freshness_feed.py
│   ├── test_mcp_bridge.py
│   ├── test_cli_daily_driver.py
│   ├── test_mcp_protection.py
│   └── …
│
├── docs/
│   ├── how-to-use.md
│   ├── mcp-daily-driver.md
│   ├── freshness-watch.md
│   ├── case-studies.md, challenge-protocol.md, companion docs, …
│   └── cursor-mcp-config.example.json
│
├── reports/                    # Live-classify outputs (chunks, summaries) — large; optional clone depth
├── .github/
│   ├── workflows/
│   │   ├── ci.yml              # Tests + data smoke (Python 3.10–3.12)
│   │   ├── freshness-watch.yml
│   │   └── pages.yml
│   └── ISSUE_TEMPLATE/
│
├── TAXONOMY.md                 # Generated readable taxonomy
├── CHANGELOG.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── SECURITY.md
├── requirements.txt            # Dev/test + optional mcp (align with pyproject extras)
└── pyproject.toml
```

---

## Data flow

```
Source markdown / maintainer edits
  └─→ scripts/extract_failures.py (when used)
        └─→ data/failures.json          ← single source of truth
              ├─→ src/data_loader.py
              │     └─→ src/classifier.py
              ├─→ src/ai_failure_mcp/bridge.py  ← classification_bundle, lookups
              ├─→ scripts/generate_taxonomy.py → TAXONOMY.md
              └─→ scripts/generate_embeddings.py → data/search_index.json
                    └─→ src/tfidf_search.py, scripts/semantic_search.py, MCP search_failures

Freshness Watch (separate): data/freshness_sources.json → scripts/freshness_watch.py → artifacts / CI

External PDF/HTML: scripts/classify_external_report.py → reports/<topic>/…
```

After **any** `failures.json` change:

```bash
python scripts/generate_taxonomy.py
python scripts/generate_embeddings.py   # if search / MCP semantic context should match
python -m pytest tests/ -v
```

---

## failures.json schema

(See inline comments in older ARCHITECTURE revisions; enforced by `test_data_integrity.py`.)

**Required fields** per class: `id`, `name`, `group_id`, `group`, `class_code`, `class_name`, `mechanism`, `forbidden`, `detection`, `keywords`.

**Common optional fields**: `severity`, `mitigation`, `mit_domain`, `examples`, `references`, `case_studies`, …

**Invariant**: `total_classes` and `len(failures)` must equal **343**; **7** groups.

---

## Classifier (`src/classifier.py`)

- **Stemming** on keywords at init (suffix strips) + **synonym expansion** on input tokens for plain-English queries.
- **Scoring**: overlap-based score plus bonuses for verbatim ID/name and mechanism bigrams (see `_score` in source).
- **Thresholds** (current): `THRESHOLD = 0.13` (class match), `GROUP_THRESHOLD = 0.09` (dimension activation).

---

## TF-IDF search (`src/tfidf_search.py`)

- **Advisory** relative to the keyword classifier: used for `search_failures` MCP tool, `semantic_search_top` inside classify bundles, and `scripts/semantic_search.py`.
- Requires `data/search_index.json` (generated).

---

## CLI (`src/cli.py`)

- Human-readable classification, `--json` (compact `ClassificationResult`), **`--daily-driver`** (same JSON shape as MCP `classify_text`), lookup, batch, interactive.

---

## MCP server (`src/ai_failure_mcp`)

- **Entry**: `python -m src.ai_failure_mcp` or `ai-failure-mcp` after `pip install -e ".[mcp]"`.
- **FastMCP** name: `ai-failure-periodic-table`.
- **Read-only** on repo taxonomy; does not write `failures.json`.

### Tools (summary)

| Tool | Purpose |
|------|---------|
| `protection` | `yes` / `no` / `status` — preference for optional **Agent Buccet** second MCP; persists under `~/.ai-failure-periodic-table/setup.json`. |
| `classify_text` | Full classification bundle + `response_contract`; may include `_protection_prompt` until user has answered via `protection`. |
| `classify_url` | Fetch public http(s) text → classify (SSRF-hardened in `bridge.fetch_url_text`). |
| `classify_document` / `classify_document_path` | UTF-8 file under repo root and/or `AI_FAILURE_MCP_DOCUMENT_ROOT(S)`. |
| `search_failures` | TF-IDF similarity; `verdict_applicable: false` in contract. |
| `get_class` | ID lookup; `verdict_applicable: false`. |
| `compound_hint` | Classification with compound emphasis when multiple dimensions activate. |

### Agent Buccet (optional second MCP)

- **`protection('yes')`** returns a suggested `mcpServers.buccet` block (`buccet mcp`).
- **Eyes vs brakes**: this server classifies; Buccet enforces at runtime. Coordinate **MCP server naming / acceptance lanes** with the [Agent Buccet](https://github.com/lml-layer-system/agent-buccet) repo if integration keys on client identity.

### Bundles & contracts

- **`classification_bundle`** (bridge) attaches `scientific_envelope.attach_scientific_surface` → `fit_state`, `contributing_route`, `report_preparation`, etc.
- **`response_contract`** documents verdict authority and advisory fields for automation.

---

## Freshness Watch

- **Not** the daily driver: scheduled maintainer-oriented feed → classifier-shaped review output.
- See [docs/freshness-watch.md](docs/freshness-watch.md) and `.github/workflows/freshness-watch.yml`.

---

## Packaging note

- Development and CI typically run from **repo root** so `data/failures.json` resolves via `src/data_loader.py` defaults.
- `pyproject.toml` includes `package-data` for JSON under the package; confirm layout if publishing to PyPI.

---

## Keyword quality (brief)

1. Derive from mechanism / forbidden / detection first.  
2. Include variants where stems might not cover (synonyms help, but explicit tokens still matter).  
3. Avoid stopwords and over-broad terms (“model”, “output” alone).  
4. Target roughly **10–20** keywords per class where possible.

---

## Adding a new failure class

1. CONTRIBUTING / issue templates (`propose_new_class`).  
2. Edit `data/failures.json`; bump `total_classes` if adding.  
3. Regenerate `TAXONOMY.md` and embeddings as needed.  
4. `python -m pytest tests/ -v`.

---

## Tests & CI

```bash
python -m pytest tests/ -v
```

- **76 tests**: classifier, data integrity, TF-IDF, freshness feed, MCP bridge, CLI `--daily-driver`, MCP `protection`.

**CI** (`.github/workflows/ci.yml`): Python **3.10, 3.11, 3.12**; pytest; assert 343 classes / 7 groups; CLI JSON smoke.

**Branches**: pushes to `main`, `master`, `claude/**`, `cursor/**`; all **pull_request** events.

---

## Running the MCP server locally

```bash
pip install -e ".[mcp]"
python -m src.ai_failure_mcp
```

Host config pattern: `command` `python3`, `args` `["-m", "src.ai_failure_mcp"]`, `cwd` = repo root — see [docs/mcp-daily-driver.md](docs/mcp-daily-driver.md).
