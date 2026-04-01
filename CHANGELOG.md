# Changelog

All notable changes to the AI Failure Periodic Table are documented here.

Format: `[version] — date — summary`

---

## [1.1.0] — 2026-04-01

### Added
- `TAXONOMY.md` — human-readable enumeration of all 343 failure classes grouped by dimension, with ID, name, mechanism, and severity for every entry
- `case_studies`, `references`, and `examples` fields added to `failures.json` schema (schema_version 1.1.0)
- 36 failure classes enriched with real-world examples, academic references, and case study links
- CLI `--debug` flag: keyword match breakdown and per-dimension score bars
- CLI `--batch` flag: classify a file of descriptions (or stdin), supports `--json`
- `--lookup` output now shows real-world examples, references, and linked case studies for enriched classes
- 20 documented case studies in `docs/case-studies.md` (expanded from 5), covering all 7 dimensions
- `scripts/generate_taxonomy.py` — regenerates TAXONOMY.md from failures.json
- `scripts/enrich_failures.py` — applies enrichment data to failures.json
- `ARCHITECTURE.md` — internal guide for code contributors

### Fixed
- Keyword coverage for 27 failure classes with < 6 keywords
- `AGEN-BLACKMAIL-046` keywords expanded to match natural language descriptions (e.g. "AI agent used threats to prevent being shut down" now classifies correctly)
- Severity note in Case 2 (Bing Chat) clarified to avoid contradicting taxonomy

### Tests
- 46 tests (up from 43)
- 3 new data integrity tests: schema v1.1.0 fields present, enriched classes have content, schema version check

---

## [1.0.0] — 2026-02-01

### Initial release

**Taxonomy**
- 343 AI failure classes across 7 orthogonal dimensions
- EPISTEMIC (33), AGENTIC (49), ADVERSARIAL (72), ALIGNMENT (41), ARCHITECTURAL (58), DOMAIN (47), GOVERNANCE (43)
- 8 CRITICAL severity classes identified
- `data/failures.json` — structured machine-readable taxonomy

**Classifier**
- `src/classifier.py` — `PeriodicTableClassifier`, pure Python, < 5ms, deterministic
- `src/cli.py` — single query, interactive, `--json`, `--lookup` modes
- `src/data_loader.py` — load, validate, cache failures.json

**Documentation**
- `README.md` — problem statement, taxonomy overview, quick start
- `CONTRIBUTING.md` — 4 contribution pathways with explicit review criteria
- `ROADMAP.md` — versioned roadmap
- `CODE_OF_CONDUCT.md` — defense-first conduct standards
- `docs/how-to-use.md` — full usage guide
- `docs/challenge-protocol.md` — 4-type challenge taxonomy with reduction test
- `docs/case-studies.md` — 5 documented real incidents

**Community infrastructure**
- 5 GitHub issue templates: propose-new-class, challenge-classification, report-real-incident, improve-keywords, bug-report
- CI on Python 3.10, 3.11, 3.12 (43 tests)
- MIT License

---

## Versioning Policy

- **Patch** (1.0.x): Bug fixes, keyword improvements, documentation corrections
- **Minor** (1.x.0): New case studies, schema enrichment, CLI features, community tooling
- **Major** (x.0.0): Structural revision to the taxonomy — new dimensions, reclassified groups, or removal of classes based on community challenge outcomes

New failure classes added after community validation will increment the minor version. Structural changes to the 7-dimension framework require a major version with published rationale.
