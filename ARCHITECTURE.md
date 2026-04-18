# Architecture

This document is for contributors working on the code and data pipeline. **End users:** classifying from the terminal → [docs/how-to-use.md](docs/how-to-use.md); **plugging an everyday AI (Cursor, Claude Desktop, MCP) into the table** → [docs/mcp-daily-driver.md](docs/mcp-daily-driver.md).

---

## Repo Layout

```
ai-failure-periodic-table/
│
├── data/
│   ├── failures.json          # The taxonomy. Single source of truth.
│   ├── search_index.json      # TF-IDF index (scripts/generate_embeddings.py)
│   └── freshness_sources.json # RSS/Atom config for Freshness Watch
│
├── src/
│   ├── classifier.py          # Core engine: PeriodicTableClassifier
│   ├── cli.py                 # CLI entry point (python -m src.cli)
│   ├── data_loader.py         # Load, validate, cache failures.json
│   ├── tfidf_search.py        # TF-IDF class search (semantic_search + Freshness Watch)
│   ├── freshness_feed.py      # Feed parse, dedupe, Freshness Watch heuristics
│   └── ai_failure_mcp/        # MCP stdio server: server.py, bridge.py, scientific_envelope.py, response_contract.py
│
├── scripts/
│   ├── extract_failures.py    # Parse markdown → failures.json (run once)
│   ├── generate_taxonomy.py   # failures.json → TAXONOMY.md (run after data changes)
│   ├── enrich_failures.py     # Applies enrichment data (examples, references)
│   ├── fix_sparse_keywords.py # Keyword coverage fixes (run after keyword additions)
│   ├── generate_embeddings.py # failures.json → search_index.json
│   ├── classify_external_report.py # curl PDF/HTML → text chunks → PeriodicTableClassifier JSON/MD
│   ├── semantic_search.py     # CLI TF-IDF search over classes
│   └── freshness_watch.py     # Feeds → classifier + review packet (no auto data edits)
│
├── reports/
│   └── freshness/             # Optional local output from freshness_watch.py
│
├── tests/
│   ├── test_classifier.py     # Known failures, non-failures, performance
│   ├── test_data_integrity.py # Schema, counts, enrichment, IDs
│   ├── test_freshness_feed.py # Feed parse, dedupe, confidence helpers
│   └── test_tfidf_search.py   # TF-IDF smoke tests
│
├── docs/
│   ├── how-to-use.md          # End-user usage guide
│   ├── case-studies.md        # Mapped incidents + companions (Glasswing, agentic misalignment, Opus 4.7 card, …)
│   ├── challenge-protocol.md  # How to challenge the taxonomy
│   ├── project-glasswing.md   # Companion: agentic cyber / MCP / Glasswing context (not part of failures.json)
│   ├── agentic-misalignment-insider-threats.md  # Companion: Lynch et al. insider-threat simulations → class IDs
│   ├── claude-opus-4-7-system-card.md  # Companion: Anthropic Opus 4.7 system card → class IDs
│   ├── claude-mythos-system-card.md    # Companion: Claude Mythos Preview system card + live classify
│   ├── meta-integrity-reports-h1-2026.md  # Link hub: Meta Transparency Center integrity + adversarial reports
│   ├── freshness-watch.md     # Freshness Watch: feed → classifier review packets
│   ├── mcp-daily-driver.md  # Daily-driver AI via MCP: where to connect, what you get, setup paths (Cursor, Claude, …)
│   ├── cursor-mcp-config.example.json
│
├── .github/
│   ├── workflows/ci.yml           # CI: test matrix Python 3.10–3.12
│   ├── workflows/freshness-watch.yml  # Weekly feed ingest → artifact (no auto-commit)
│   └── ISSUE_TEMPLATE/            # 5 structured issue templates
│
├── reports/
│   ├── meta-integrity-h1-2026/ # Meta Adversarial PDF → pdftotext + classify_external_report.py outputs (*.pdf gitignored)
│   ├── glasswing/              # anthropic.com/glasswing HTML + project-glasswing.md → same classifier pipeline
│   ├── claude-opus-4-7/        # Opus 4.7 system card PDF → pdftotext + classify_external_report.py (*.pdf gitignored)
│   ├── claude-mythos/          # Mythos Preview system card PDF (official URL) → same pipeline (*.pdf gitignored)
│   └── agentic-misalignment/   # Lynch et al. arXiv:2510.05179 PDF → same pipeline (*.pdf gitignored)
├── TAXONOMY.md                # Auto-generated: all 343 classes in readable format
├── CHANGELOG.md               # Version history
├── CONTRIBUTING.md            # Contribution process
└── ROADMAP.md                 # Versioned roadmap
```

---

## Data Flow

```
Source markdown files
  └─→ scripts/extract_failures.py
        └─→ data/failures.json          ← single source of truth
              ├─→ src/data_loader.py    ← loads + validates at runtime
              │     └─→ src/classifier.py  ← uses failures at classification time
              └─→ scripts/generate_taxonomy.py
                    └─→ TAXONOMY.md     ← regenerate after any data change
```

If you modify `failures.json` (add keywords, add a class, change a mechanism), run:
```bash
python scripts/generate_taxonomy.py   # keeps TAXONOMY.md in sync
python -m pytest tests/ -v            # verify data integrity
```

---

## failures.json Schema

```json
{
  "version": "1.0.0-COMPLETE",
  "schema_version": "1.1.0",
  "total_classes": 343,
  "groups": [
    {"id": 1, "code": "EPISTEMIC", "count": 33, ...}
  ],
  "failures": [
    {
      "id":          "EPIS-CITE-SPOOF-008",     // unique, stable identifier
      "name":        "CITATION SPOOFING",        // uppercase, human-readable
      "group_id":    1,                          // 1–7
      "group":       "EPISTEMIC",                // dimension name
      "class_code":  "E1",                       // dimension shortcode
      "class_name":  "HALLUCINATION CLASS",      // class within dimension
      "mechanism":   "...",                      // how the failure occurs
      "forbidden":   "...",                      // what must not happen
      "detection":   "...",                      // how to detect it
      "severity":    "STANDARD",                 // STANDARD or CRITICAL
      "keywords":    ["citation", ...],          // classifier vocabulary
      // v1.1.0 optional enrichment fields:
      "case_studies": ["Case 1: ..."],           // links to docs/case-studies.md
      "references":   ["Author, Title (year)"],  // academic/news sources
      "examples":     "One paragraph..."        // real-world description
    }
  ]
}
```

**Required fields**: `id`, `name`, `group_id`, `group`, `class_code`, `class_name`, `mechanism`, `forbidden`, `detection`, `keywords`

**Optional enrichment fields**: `case_studies`, `references`, `examples` — empty by default, populated for documented classes. These are enforced by `test_data_integrity.py::test_schema_v1_1_fields_present`.

---

## Classifier Scoring

`src/classifier.py` — `PeriodicTableClassifier._score()`

For each failure class against an input description:

```
base_score = |input_tokens ∩ failure_keywords| / |failure_keywords|

bonuses:
  +0.50  if failure ID appears verbatim in input
  +0.40  if failure name appears verbatim in input
  +0.05  per matching bigram from mechanism text

final_score = min(1.0, base_score + bonuses)
```

**Thresholds**:
- `THRESHOLD = 0.15` — a failure class is considered a match if score ≥ 0.15
- `GROUP_THRESHOLD = 0.10` — a dimension activates if its best class scores ≥ 0.10

**No stemming, no negation handling.** "threats" and "threat" are different tokens. "the model did NOT hallucinate" will still weakly match hallucination classes. This is a design trade-off: keyword matching is transparent and reproducible; NLP-based approaches would be harder to inspect and explain.

---

## What Makes Good Keywords

Keywords are the classifier's vocabulary for a failure class. Quality guidelines:

1. **Source from mechanism + forbidden + detection text first** — if the mechanism says "generates plausible but nonexistent references", good keywords are "generates", "plausible", "nonexistent", "references".

2. **Include natural language variants** — the classifier doesn't stem, so include both "threat" and "threats", "shutdown" and "shut", "refuse" and "refuses".

3. **Avoid stopwords** — words like "the", "and", "not", "does" add noise. The tokenizer already filters tokens ≤ 2 chars, but short common words (e.g., "has", "can") should still be avoided.

4. **Add domain vocabulary** — for DOMAIN classes, include the field's terminology. A bio uplift class should include "synthesis", "pathogen", "laboratory", "protocol" — words a researcher would naturally use.

5. **Avoid over-broad terms** — "model", "output", "generates" are true of almost every class and add no discriminating signal. Include them only if they combine with specific terms.

6. **Target coverage 10–20 keywords** — fewer than 8 makes the class hard to match; more than 25 dilutes the score (base_score = overlap / total, so a 30-keyword class needs 5 matches to hit threshold).

---

## Adding a New Failure Class

1. Open a `propose-new-class` issue (see [CONTRIBUTING.md](CONTRIBUTING.md)) and pass the reduction test
2. If accepted, add the entry to `data/failures.json` following the schema
3. Assign an ID following the pattern: `GROUP-SHORTNAME-NNN` (e.g., `EPIS-NEW-CLASS-033`)
4. Update `total_classes` count in failures.json
5. Run `python scripts/generate_taxonomy.py` to update TAXONOMY.md
6. Add a test in `tests/test_data_integrity.py` if adding a new CRITICAL class
7. Run `python -m pytest tests/ -v` — all tests must pass

---

## Running Tests

```bash
python -m pytest tests/ -v        # all 46 tests
python -m pytest tests/test_classifier.py -v       # classifier only
python -m pytest tests/test_data_integrity.py -v  # data integrity only
```

CI runs automatically on push and PR via `.github/workflows/ci.yml` against Python 3.10, 3.11, 3.12.
