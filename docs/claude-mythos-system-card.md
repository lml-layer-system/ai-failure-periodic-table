# Claude Mythos Preview — system card (companion + live classify)

> **What this is:** Anthropic’s **Claude Mythos Preview** system card (first-party disclosure, **not** generally available model). Same treatment as [Claude Opus 4.7 system card](claude-opus-4-7-system-card.md): **official PDF → text → chunked keyword classifier** artifacts in-repo.

**Canonical sources**

- **System card (official; resolves to PDF):** [anthropic.com/claude-mythos-preview-system-card](https://www.anthropic.com/claude-mythos-preview-system-card)
- **Strategic context (coalition, MCP, etc.):** [Project Glasswing](project-glasswing.md) · [anthropic.com/glasswing](https://www.anthropic.com/glasswing)

**Local PDF note:** An ingest was first run from the author’s iCloud copy (`claude mythos add to ai failure periodic table.pdf`). **Committed artifacts are regenerated from the official URL** so everyone reproduces the same file (the public card may include **newer changelog** lines than a saved copy).

**Live classifier outputs** (`--max-chars 4500`, same as Opus 4.7 system card)

| Artifact | Purpose |
|----------|---------|
| [`claude-mythos-system-card-live-summary.md`](../reports/claude-mythos/claude-mythos-system-card-live-summary.md) | Top-1 histogram + chunk index |
| [`claude-mythos-system-card-live-chunks.json`](../reports/claude-mythos/claude-mythos-system-card-live-chunks.json) | Per-chunk scores |
| [`claude-mythos-system-card-live-source.txt`](../reports/claude-mythos/claude-mythos-system-card-live-source.txt) | `pdftotext -layout` + provenance header |

**Reproduce**

```bash
python scripts/classify_external_report.py \
  --url https://www.anthropic.com/claude-mythos-preview-system-card \
  --out-prefix reports/claude-mythos/claude-mythos-system-card-live \
  --max-chars 4500
```

**Interpretation:** Keyword classifier on long system-card prose is **exploratory** (see [meta integrity doc](meta-integrity-reports-h1-2026.md) caveats). For mechanism-level mapping, prefer curated appendix-style work (e.g. [project-glasswing.md](project-glasswing.md) §2 / Case 21 threads) plus spot checks with `python -m src.cli`.
