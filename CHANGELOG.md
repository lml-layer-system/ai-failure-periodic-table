# Changelog

All notable changes to the AI Failure Periodic Table are documented here.

Format: `[version] — date — summary`

---

## [1.4.0] — 2026-04-12

### Added
- Cross-reference fields `mit_domain` and `ms_agentic_category` on 61 failure classes
  - `mit_domain`: maps to one of MIT AI Risk Repository's 7 domains (Misinformation, Privacy & Security, Malicious Actors, AI System Safety, Human-Computer Interaction, Discrimination & Toxicity, Socioeconomic & Environmental)
  - `ms_agentic_category`: maps to Microsoft Agentic AI Failure Taxonomy categories (Goal Hijacking, Prompt Injection, Privilege Escalation, Unsafe Action Execution, Resource Exhaustion, Memory Poisoning) — applied only to 16 classes where the mapping is precise
  - Fields are optional; cross-cutting classes intentionally left unmapped to avoid dishonest categorization
- "Relationship to Other Frameworks" section in README: plain statement that the Periodic Table is complementary to MIT, Microsoft, and AVID frameworks — not competing
- Modal now displays MIT Domain and MS Agentic Category when present
- `scripts/add_framework_refs.py` — idempotent batch script for applying framework cross-references

### Changed
- README version badge updated to 1.4.0

---

## [1.3.0] — 2026-04-11

### Added
- `mitigation` field on every failure class: the structural mechanism that stops the failure at its core, named precisely without operational instructions. 343/343 classes covered.
- Interactive modal now shows `case_studies` (structured: title, system, date, outcome, source) and `mitigation` for every class
- `scripts/generate_visual.py` updated to include `case_studies` and `mitigation` in the JS data payload
- TF-IDF semantic search: `scripts/generate_embeddings.py` builds a 3,576-term vocabulary, `scripts/semantic_search.py` provides CLI search with `--top`, `--group`, `--severity`, `--json` flags
- In-browser semantic search in `index.html` — lazy-loads `data/search_index.json` on first keypress, falls back to keyword search offline
- `data/search_index.json` (487KB) — pre-computed TF-IDF index, shipped in repo for instant search
- `data/embeddings_meta.json` — search index metadata
- GitHub Pages deployment workflow (`.github/workflows/pages.yml`) — auto-deploys on push to main
- MIT `LICENSE` file
- CRITICAL severity expanded from 8 → 26 classes: added deceptive alignment, sleeper agents, oversight immunity, log manipulation, and others with catastrophic/irreversible harm potential
- Case studies normalized: 36 old string-format entries converted to structured `{title, system, date, outcome, source}` dicts
- Metadata consolidated: single canonical v1.1.0 block throughout failures.json

### Changed
- Classifier rebuilt with suffix-stripping stemmer and synonym expansion dictionary
  - "hallucinated" now matches keyword "hallucination", "fabricated" matches "fabricate", etc.
  - 60+ synonym mappings: "made up" → fabricate/hallucinate, "women" → gender/bias/discriminat, "love" → emotion/manipulation, "lied" → deceive, "bypassed" → bypass/jailbreak, and more
  - Minimum 2-keyword match requirement prevents single common-word false positives
  - 100% recall on 49 external real-world incidents (up from 86% on 15)
- 32 mechanism descriptions sharpened from action descriptions to structural explanations
  - All 26 CRITICAL classes updated to structural root-cause language
  - Key standard classes updated: citation spoofing, hallucination, sycophancy, DAN jailbreak, overrefusal, sandbagging
- 14 mitigation descriptions sharpened from aspirational to implementable structural names
- Keyword sets expanded for 7 failure classes with known vocabulary gaps:
  `ALIGN-ANTHRO-BIAS-170`, `ALIGN-CULTURE-BIAS-171`, `ARCH-BIAS-INJECT-222`,
  `AGEN-UNSUPER-EXEC-065`, `ALIGN-OVERREFUSAL-186`, `GOV-TRANSPARENCY-311`,
  `EPIS-DATA-LEAK-024`
- README restructured to lead with taxonomy and browser interface, not CLI;
  classifier notes added with explicit limitations and fallback guidance
- Compound Failures section with disambiguation worked example
- Known Gaps and Classification Limits section

### Tests
- 48 tests (up from 46)
- New test: `test_all_classes_have_mitigation` — verifies all 343 classes have non-empty mitigation field
- New test: `test_recall_on_real_incidents` — 49 documented real-world AI failures (Bing Chat, Mata v. Avianca, Character.AI, Air Canada, Amazon hiring bias, Character.AI suicide, RL boat racing, Samsung data leak, nurse over-refusal, and more) phrased as reporters, researchers, and courts described them; classifier achieves 100% recall (≥80% threshold)

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
- 343 AI failure classes across 7 structural dimensions
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
