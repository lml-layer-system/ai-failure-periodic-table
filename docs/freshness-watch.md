# Freshness Watch

One leg of the **[incident observatory](../README.md#daily-driver--incident-observatory)**: scheduled scanning of public feeds into maintainer review packets (not the same as the MCP **daily driver**).

**Freshness Watch** is a **human-review-only** pipeline: it pulls public RSS/Atom sources, filters for AI / security / agent-relevant keywords, runs each item through the **keyword classifier** and **TF-IDF semantic search**, and writes a **review packet** (Markdown + JSON). It does **not** edit `failures.json` or add classes automatically.

## Doctrine

- The feed **observes**; the classifier **suggests**; the **maintainer decides**.
- Prefer **enrichment** (references, case studies, keywords) over **new taxonomy IDs**.
- If nothing matches strongly, items are labeled **`possible_gap_candidate`** for manual triage—not instant new classes.

## Commands

From the repository root (after `python scripts/generate_embeddings.py` if `src/data/search_index.json` is missing):

```bash
python scripts/freshness_watch.py --days 14 --out reports/freshness/latest.md
```

Options:

- `--config path` — default `src/data/freshness_sources.json`
- `--json-out path` — default `data/freshness/latest.json`
- `--no-keyword-filter` — include all items in the time window (no keyword gate)
- `--max-items N` — cap volume (default 80)

## Configuration

Edit **`src/data/freshness_sources.json`**: feed URLs, `filter_keywords`, timeouts, and per-feed `enabled` flags.

## CI

**`.github/workflows/freshness-watch.yml`** runs weekly (and on demand), uploads the generated reports as workflow **artifacts**. It does **not** auto-commit to the repo.

On some local machines, HTTPS feeds may fail with `CERTIFICATE_VERIFY_FAILED` (Python SSL store). Ubuntu runners in GitHub Actions typically succeed; fix local certs or run the workflow remotely if you hit this.

## Daily-driver vs repo upkeep

- **Freshness Watch** = official, slower, source-grounded **review** for what might enrich the public table.
- **On-demand classification** (e.g. `python -m src.cli`, `python scripts/semantic_search.py`) = **instant** analysis of any text you paste; separate from this pipeline.
