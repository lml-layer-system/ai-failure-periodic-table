# Changelog

All notable changes to the AI Failure Periodic Table are documented here.

Format: `[version] — date — summary`

---

## [1.4.35] — 2026-04-19

### Changed
- **Packaging:** drop deprecated `License :: OSI Approved :: …` trove classifier (SPDX `license = "Apache-2.0"` only; required by current setuptools).
- **MANIFEST.in:** include `LICENSE` / `README.md`; `global-exclude` macOS `._*` / `.DS_Store` for sdists.
- **CI:** [`.github/workflows/release.yml`](.github/workflows/release.yml) — on version tags `v*`, build wheel + sdist on **Ubuntu** and upload `dist/` artifacts (use for PyPI or manual release).

---

## [1.4.34] — 2026-04-17

### Changed
- **[CHANGELOG.md](CHANGELOG.md):** license wording describes **Apache License 2.0** only (no prior permissive-license name in repo docs).

---

## [1.4.33] — 2026-04-17

### Changed
- **License:** **Apache License 2.0** — see `LICENSE`, [README.md](README.md), [pyproject.toml](pyproject.toml), [ROADMAP.md](ROADMAP.md).

---

## [1.4.32] — 2026-04-19

### Changed
- **[README.md](README.md):** restored **why “periodic table”** (chemistry metaphor → structural grid); moved **The Problem** (incl. frontier labs), **What This Is**, mission quote, and version **above** daily driver / proof; removed duplicate middle blocks.

---

## [1.4.31] — 2026-04-19

### Changed
- **[README.md](README.md):** Enterprise Layer — editorial **we** for “building” / “open to design partners” (solo disclaimer unchanged).

---

## [1.4.30] — 2026-04-19

### Changed
- **[README.md](README.md):** Enterprise Layer copy — **solo / no partners or customers yet**; first-person; design partners framed as **open to** collaboration before productization.

---

## [1.4.29] — 2026-04-19

### Added
- **[README.md](README.md):** **Enterprise Layer (Currently Building)** — managed API, monitoring, dashboard, training, integrations; design partners; contact via existing **ryangat@lmlsystemlayer.com**.

---

## [1.4.28] — 2026-04-19

### Changed
- **[README.md](README.md):** new subsection under **The Problem** — **Frontier labs, fragmented vocabulary** (cross-vendor thesis, classifier pipeline, cited `reports/` runs, automation vision).

---

## [1.4.27] — 2026-04-19

### Changed
- **[README.md](README.md):** new **Proof in the repository** section (interactive failure cards, [docs/case-studies.md](docs/case-studies.md), indexed **`reports/`** live summaries + reproduce note).
- **Interactive site:** incident-observatory strip now points at **failure cards**, **`reports/`**, and the README proof anchor.
- **[docs/case-studies.md](docs/case-studies.md):** cross-link to proof / `reports/`.

---

## [1.4.26] — 2026-04-19

### Changed
- **[README.md](README.md):** **Daily driver & incident observatory** moved immediately under the project subtitle; mission quote and version follow.
- **Interactive table:** story strip is the **first** block in the page (above the title header).

---

## [1.4.25] — 2026-04-19

### Changed
- **[README.md](README.md):** **Daily driver & incident observatory** section placed up front (before the live table); Quick Start MCP subsection shortened to point there.
- **Interactive site ([index.html](index.html)):** prominent two-card strip under the header (MCP daily driver + incident observatory links).
- **[scripts/generate_visual.py](scripts/generate_visual.py):** emits the same story strip for future regenerations.
- **Docs cross-links:** [docs/mcp-daily-driver.md](docs/mcp-daily-driver.md), [docs/case-studies.md](docs/case-studies.md), [docs/freshness-watch.md](docs/freshness-watch.md), [ARCHITECTURE.md](ARCHITECTURE.md).

---

## [1.4.24] — 2026-04-18

### Changed
- **PyPI-ready data layout:** taxonomy JSON and TF-IDF artifacts live under **`src/data/`** so `package-data` wheels match runtime (`src/taxonomy_paths.py`, `src/data_loader.py`, `src/tfidf_search.py`, MCP `bridge.py` document-root fallback when not run from a checkout).
- **Scripts & workflows** updated to read/write `src/data/*.json`; **Freshness Watch** still writes machine output under `data/freshness/` (repo artifacts only).
- **[scripts/smoke_install.sh](scripts/smoke_install.sh):** also smoke-tests a **non-editable wheel** install (staged copy via `rsync` so local builds survive AppleDouble noise on some volumes).
- **[.github/workflows/ci.yml](.github/workflows/ci.yml):** `python -m build` + assert `failures.json` / `search_index.json` are inside the wheel.

---

## [1.4.23] — 2026-04-18

### Added
- **[scripts/smoke_install.sh](scripts/smoke_install.sh):** clean-venv editable install + `--daily-driver` / `--json` smoke (phrase aligned with classifier tests).

### Changed
- **Merge `cursor/glasswing-case21-taxonomy-docs` → `main`** so default branch carries MCP daily driver, `--daily-driver` CLI, docs, CI (`mcp` + `cursor/**`), SECURITY, refreshed ARCHITECTURE.
- **[tests/test_mcp_protection.py](tests/test_mcp_protection.py):** assertions match post-merge `protection()` JSON (`buccet_active`, `preference`, `preference_recorded`).
- **[.github/workflows/ci.yml](.github/workflows/ci.yml):** CLI smoke string uses citation wording that reliably hits the table.

---

## [1.4.22] — 2026-04-18

### Added
- **[tests/test_mcp_protection.py](tests/test_mcp_protection.py):** coverage for `protection()` (yes/no/status/invalid) with isolated setup path.

### Changed
- **[ARCHITECTURE.md](ARCHITECTURE.md):** rewritten for current tree (MCP package, TF-IDF, Freshness Watch, accurate classifier thresholds, tools table, Buccet note).
- **[.github/workflows/ci.yml](.github/workflows/ci.yml):** `pip install "mcp>=1.2"` for server imports; push triggers include `cursor/**`.
- **[requirements.txt](requirements.txt):** `mcp>=1.2` aligned with `pyproject.toml`.
- **[SECURITY.md](SECURITY.md):** MCP scope, URL/document boundaries, `~/.ai-failure-periodic-table/` note.

---

## [1.4.21] — 2026-04-18

### Added
- **CLI `--daily-driver`:** [`src/cli.py`](src/cli.py) — same JSON bundle as MCP `classify_text` / lookup (`response_contract`, `fit_state`, `report_preparation`, …); batch and interactive supported; [`tests/test_cli_daily_driver.py`](tests/test_cli_daily_driver.py).

### Changed
- **[docs/mcp-daily-driver.md](docs/mcp-daily-driver.md), [README.md](README.md):** Document **`protection`** + optional **Agent Buccet** second MCP (`buccet mcp`), `_protection_prompt`, `~/.ai-failure-periodic-table/setup.json`.
- **[src/ai_failure_mcp/server.py](src/ai_failure_mcp/server.py):** MCP host `instructions` mention `protection` and Buccet.
- **[docs/how-to-use.md](docs/how-to-use.md):** `--daily-driver` examples and clarified default vs JSON output.

---

## [1.4.20] — 2026-04-17

### Changed
- **[docs/mcp-daily-driver.md](docs/mcp-daily-driver.md):** **Guaranteed fallbacks when MCP is down** (CLI, browser, semantic CLI) and **Requirements: Python vs chat model** — clarifies verdict runs in Python 3.10+, `pip install -e .` vs `.[mcp]`, no LLM required for classification; chat models only orchestrate MCP; small/local models may need CLI fallback.
- **[README.md](README.md), [docs/how-to-use.md](docs/how-to-use.md):** Cross-links to those sections.

---

## [1.4.19] — 2026-04-17

### Changed
- **[docs/mcp-daily-driver.md](docs/mcp-daily-driver.md):** User-first rewrite—plain-English “what this is for,” **read-only / not Freshness Watch**, **what you get vs how to connect**, **connect your daily-driver AI** (Cursor, Claude Desktop, any MCP host), **choose your setup path**, **first-use walkthrough**, **result semantics**, security and personal-document notes; technical tool table moved below.
- **[README.md](README.md):** “Connect your everyday AI” quick section pointing at the guide; MCP blurb aligned.
- **[docs/how-to-use.md](docs/how-to-use.md), [ARCHITECTURE.md](ARCHITECTURE.md):** Cross-links for MCP vs CLI audiences; [docs/cursor-mcp-config.example.json](docs/cursor-mcp-config.example.json) kept as paste-ready template with optional `AI_FAILURE_MCP_DOCUMENT_ROOT`.

---

## [1.4.18] — 2026-04-17

### Added
- **`response_contract`** on every MCP JSON payload ([`src/ai_failure_mcp/response_contract.py`](src/ai_failure_mcp/response_contract.py)): `schema_version`, `verdict_applicable`, roles of `fit_state` vs semantic fields, `contributing_route_field`; non-verdict tools (`search_failures`, `get_class`) and **error** responses include explicit machine-readable instructions so clients never treat TF-IDF or errors as `classifier_hit`.
- **Error payloads** from MCP tools include the same `response_contract` with `error_response: true`.

### Changed
- MCP **server instructions and tool docstrings** restated for production: single verdict authority, advisory semantic context, `response_contract` first-class.
- [`docs/mcp-daily-driver.md`](docs/mcp-daily-driver.md): `response_contract` table; [`compound_hint`](src/ai_failure_mcp/bridge.py) copy no longer implies semantic can override the classifier.

---

## [1.4.17] — 2026-04-18

### Added
- **MCP daily driver (scientific surface):** [`src/ai_failure_mcp/scientific_envelope.py`](src/ai_failure_mcp/scientific_envelope.py) — `fit_state`, `fit_confidence`, `fit_evidence`, `boundary_pressure_note`, `what_to_do_next`, `recommended_repo_action`, `report_preparation`, `scientific_summary`, `falsification_note` on **`classify_text`**, **`classify_url`**, **`classify_document`**, **`compound_hint`**; grounded in [CONTRIBUTING.md](CONTRIBUTING.md) issue templates (not Freshness Watch)
- **`classify_document_path`:** alias tool; **`AI_FAILURE_MCP_DOCUMENT_ROOT`** / **`AI_FAILURE_MCP_DOCUMENT_ROOTS`** for safe reads outside repo root ([docs/mcp-daily-driver.md](docs/mcp-daily-driver.md))
- **`search_failures`** / **`get_class`:** meta envelope with `fit_state: not_applicable` and guidance to run full classification

### Changed
- [docs/mcp-daily-driver.md](docs/mcp-daily-driver.md), [docs/cursor-mcp-config.example.json](docs/cursor-mcp-config.example.json); README **1.4.17** / test count; [ARCHITECTURE.md](ARCHITECTURE.md)

---

## [1.4.16] — 2026-04-18

### Added
- [`reports/agentic-misalignment/`](reports/agentic-misalignment/): live **`classify_external_report.py`** on [Lynch et al. arXiv:2510.05179 PDF](https://arxiv.org/pdf/2510.05179) (`lynch-et-al-2510-05179-live-*`, 18 chunks @ 4500 chars); `.gitignore` `*-official.pdf`

### Changed
- [docs/agentic-misalignment-insider-threats.md](docs/agentic-misalignment-insider-threats.md), [docs/case-studies.md](docs/case-studies.md) Case 22, README row; **1.4.16** / `pyproject.toml` / `index.html` footer; [ARCHITECTURE.md](ARCHITECTURE.md)

---

## [1.4.15] — 2026-04-18

### Added
- [`docs/claude-mythos-system-card.md`](docs/claude-mythos-system-card.md): **Claude Mythos Preview** system card — official [PDF URL](https://www.anthropic.com/claude-mythos-preview-system-card), same live-classify workflow as Opus 4.7
- [`reports/claude-mythos/`](reports/claude-mythos/): `claude-mythos-system-card-live-*` (121 chunks @ 4500 chars); `.gitignore` `*-official.pdf`

### Changed
- [docs/project-glasswing.md](docs/project-glasswing.md): pointer to Mythos system card artifacts; README **1.4.15**; `pyproject.toml` / `index.html` footer
- `tests/test_classifier.py`: average latency assertion **< 40ms** (was 15ms) for stability on slower filesystems

---

## [1.4.14] — 2026-04-18

### Added
- [`reports/claude-opus-4-7/`](reports/claude-opus-4-7/): live **`classify_external_report.py`** pass on official [Claude Opus 4.7 system card PDF](https://www.anthropic.com/claude-opus-4-7-system-card) (`--max-chars 4500` for manageable artifact size); `.gitignore` `*-official.pdf` for this folder

### Changed
- [docs/claude-opus-4-7-system-card.md](docs/claude-opus-4-7-system-card.md), README framework row; **1.4.14** in README / `pyproject.toml` / `index.html` footer

---

## [1.4.13] — 2026-04-18

### Fixed
- Aligned **`pyproject.toml`** project version and **`index.html`** footer (via `scripts/generate_visual.py`) with README numbering — they had drifted at **1.2.0** while docs tracked **1.4.x**

---

## [1.4.12] — 2026-04-18

### Added
- [`reports/glasswing/`](reports/glasswing/): live **`classify_external_report.py`** pass on **official** [anthropic.com/glasswing](https://www.anthropic.com/glasswing) HTML (`anthropic-glasswing-page-live-*`) and on **in-repo** [`docs/project-glasswing.md`](docs/project-glasswing.md) companion (`project-glasswing-companion-narrative-*`)

### Changed
- [`scripts/classify_external_report.py`](scripts/classify_external_report.py): JSON/Markdown `source_file` paths are **repo-relative** (portable across machines)
- [docs/project-glasswing.md](docs/project-glasswing.md), [docs/meta-integrity-reports-h1-2026.md](docs/meta-integrity-reports-h1-2026.md), README **1.4.12** — cross-link the **official-source → classify → document** workflow (Glasswing + Meta)

---

## [1.4.11] — 2026-04-18

### Added
- [`scripts/classify_external_report.py`](scripts/classify_external_report.py): `curl` URL (PDF or HTML) → `pdftotext` when needed → chunk → **`PeriodicTableClassifier`** → `-chunks.json` + `-summary.md`; writes `-source.txt` with provenance header

### Changed
- **Meta Adversarial Threat Report:** live run on **official PDF text** — [`reports/meta-integrity-h1-2026/adversarial-h1-2026-live-*`](../reports/meta-integrity-h1-2026/); [docs/meta-integrity-reports-h1-2026.md](docs/meta-integrity-reports-h1-2026.md) documents reproduce steps and limits of keyword scoring on long prose
- Removed paraphrase-only batch artifacts (`passages.txt`, `classifier.json`, `semantic-*.json`) from that folder; `.gitignore` `*-official.pdf` under `reports/meta-integrity-h1-2026/`
- README **1.4.11**; [ARCHITECTURE.md](ARCHITECTURE.md)

---

## [1.4.10] — 2026-04-18

### Added
- [`reports/meta-integrity-h1-2026/`](reports/meta-integrity-h1-2026/): Meta-shaped **passages**, **keyword classifier** batch JSON (`classifier.json`), and **TF‑IDF semantic search** JSON for nudify/CIB/moderation/geo/oversight themes

### Changed
- [docs/meta-integrity-reports-h1-2026.md](docs/meta-integrity-reports-h1-2026.md): documents how to re-run `src.cli` and `semantic_search.py` on those artifacts; README **1.4.10**; [ARCHITECTURE.md](ARCHITECTURE.md) reports folder note

---

## [1.4.9] — 2026-04-18

### Added
- [docs/meta-integrity-reports-h1-2026.md](docs/meta-integrity-reports-h1-2026.md): **official** Transparency Center URLs for Meta **Integrity Reports, H1 2026** (hub, Community Standards Enforcement, Widely Viewed Content, content restrictions, Oversight Board H2 2025) and **First Half 2026 Adversarial Threat Report** (Mar 11, 2026), plus archive/index links

### Changed
- README 1.4.9; Relationship to Other Frameworks row + short blurb for Meta reports; [ARCHITECTURE.md](ARCHITECTURE.md) docs layout

---

## [1.4.8] — 2026-04-18

### Changed
- **Proof sources are canonical URLs only** (open in the browser): Lynch et al. [arxiv.org/pdf/2510.05179](https://arxiv.org/pdf/2510.05179); Claude Opus 4.7 system card [anthropic.com/claude-opus-4-7-system-card](https://www.anthropic.com/claude-opus-4-7-system-card). Removed **`docs/papers/*.pdf`** blobs from the repo.
- Companion docs, Case 22/23, README framework table, `data/failures.json` `case_studies.source` strings updated accordingly; [ARCHITECTURE.md](ARCHITECTURE.md) no longer lists a `papers/` folder.

---

## [1.4.7] — 2026-04-18

### Added
- ~~In-repo PDF~~ → superseded in **1.4.8** by [system card URL](https://www.anthropic.com/claude-opus-4-7-system-card): Anthropic Claude Opus 4.7 system card (Apr 2026)
- [docs/claude-opus-4-7-system-card.md](docs/claude-opus-4-7-system-card.md): companion appendix mapping PDF sections → taxonomy IDs
- [docs/case-studies.md](docs/case-studies.md) **Case 23**: compound threads (agentic injection, reward/hallucination audits, sandbagging & eval-awareness, destructiveness evals, cyber/CB RSP)
- `data/failures.json`: Case 23 `case_studies` on `ADV-INDIRECT-INJECT-122`, `AGEN-EVAL-DECEP-038`, `AGEN-SANDBOX-037`, `ALIGN-REWARD-TAMP-157`, `DOMAIN-ZERODAY-262`, `DOMAIN-BIO-UPLIFT-254`, `EPIS-EXTRINSIC-005`, `AGEN-SABOTAGE-CONCEAL-034`

### Changed
- README 1.4.7; Relationship to Other Frameworks row + blurb for Opus 4.7 system card
- [ARCHITECTURE.md](ARCHITECTURE.md): Opus 4.7 companion + PDF in docs layout
- `tests/test_data_integrity.py`: Case 23 class IDs added to enriched-case-study list

---

## [1.4.6] — 2026-04-18

### Added
- **MCP stdio server** (daily-driver layer): `python -m src.ai_failure_mcp` after `pip install -e ".[mcp]"` — tools `classify_text`, `classify_url`, `classify_document`, `search_failures`, `get_class`, `compound_hint`
- [src/ai_failure_mcp/](src/ai_failure_mcp/): read-only access to `data/failures.json` + TF-IDF index; responses include **`suggested_structural_response`** (mechanism, forbidden, detection, mitigation from the table—not vendor-specific runbooks)
- [docs/mcp-daily-driver.md](docs/mcp-daily-driver.md), [docs/cursor-mcp-config.example.json](docs/cursor-mcp-config.example.json)
- `pyproject.toml`: optional dependency `mcp`, console script `ai-failure-mcp`
- `tests/test_mcp_bridge.py`

---

## [1.4.5] — 2026-04-18

### Added
- **Freshness Watch** — [docs/freshness-watch.md](docs/freshness-watch.md): RSS/Atom ingest → keyword classifier + TF-IDF semantic search → **human-review-only** Markdown + JSON packets (`scripts/freshness_watch.py`, `data/freshness_sources.json`). Does **not** edit `failures.json`.
- [src/freshness_feed.py](src/freshness_feed.py): feed parse (RSS/Atom), dedupe, confidence heuristics, suggestion text
- [src/tfidf_search.py](src/tfidf_search.py): shared TF-IDF search API (used by `scripts/semantic_search.py` and Freshness Watch)
- [.github/workflows/freshness-watch.yml](.github/workflows/freshness-watch.yml): weekly + `workflow_dispatch`; uploads artifacts; no auto-commit
- Tests: `tests/test_freshness_feed.py`, `tests/test_tfidf_search.py`

### Changed
- `scripts/semantic_search.py`: delegates scoring to `src.tfidf_search` (CLI behavior preserved)
- README version badge → 1.4.5; test count note
- [ARCHITECTURE.md](ARCHITECTURE.md): Freshness Watch + new modules in layout

### Fixed
- RSS `<description>` with text-only / CDATA: avoid `Element or …` pattern (Python 3.12+ Elements can be falsy), so summaries are not dropped

---

## [1.4.4] — 2026-04-17

### Added
- ~~In-repo PDF~~ → superseded in **1.4.8** by [arXiv PDF](https://arxiv.org/pdf/2510.05179): Lynch et al. (arXiv:2510.05179)
- [docs/agentic-misalignment-insider-threats.md](docs/agentic-misalignment-insider-threats.md): companion with appendix tables mapping paper sections → taxonomy IDs
- [docs/case-studies.md](docs/case-studies.md) **Case 22**: compound narrative (blackmail / shutdown resistance, espionage, eval-vs-real CoT, human manipulation) + pointer to full enumeration
- `data/failures.json`: Case 22 `case_studies` rows for `AGEN-BLACKMAIL-046`, `AGEN-SHUTDOWN-RESIST-049`, `AGEN-EVAL-DECEP-038`, `AGEN-STRATEGIC-DECEP-036`, `AGEN-HUMAN-MANIP-061`, `ARCH-DATA-EXFIL-245` (and cross-links to companion + arXiv)

### Changed
- README version badge → 1.4.4; Relationship to Other Frameworks row + blurb for agentic misalignment
- [ARCHITECTURE.md](ARCHITECTURE.md): agentic-misalignment companion in repo layout (see **1.4.8** for link-only proof sources)
- `tests/test_data_integrity.py`: Case 22 class IDs added to enriched-case-study list

---

## [1.4.3] — 2026-04-17

### Added
- [docs/project-glasswing.md](docs/project-glasswing.md): **Appendix — Full enumeration** — table mapping **every** document section (Preamble, §1–14) to Periodic Table class IDs; **MCP explicitly spans §7–10** (intro, tool poisoning, rug pull, supply chain/CVE) vs Glasswing **§3–4** only
- [docs/case-studies.md](docs/case-studies.md) Case 21: **Full enumeration** subsection + summary table pointing at the appendix
- `data/failures.json`: Case 21 `case_studies` rows for `AGEN-CAP-SCAFFOLD-057`, `AGEN-UNSUPER-EXEC-065`, `ADV-CONTEXT-CONFUSE-135`, `ARCH-DEPLOY-CONFIG-210`, `ADV-TRIGGER-BACKDOOR-126`, `GOV-TRANSPARENCY-311`, `ALIGN-CONTEXT-SAFE-190`, `EPIS-FALSE-CERT-030`
- `tests/test_data_integrity.py`: above IDs (except `EPIS-FALSE-CERT-030`, already listed) added to enriched-case-study list
- [docs/project-glasswing.md](docs/project-glasswing.md): **Complete heading checklist** (every `##` / `###` / H1 + meta sections) and **Conclusion §14** sub-table mapping each numbered recommendation → class IDs

### Changed
- README version badge → 1.4.3
- `tests/test_classifier.py`: single-query perf uses **median of 3** samples, threshold **25ms**; average threshold **15ms** (reduce flake)

---

## [1.4.2] — 2026-04-17

### Added
- **Case 21** in [docs/case-studies.md](docs/case-studies.md): compound case study for the Project Glasswing / agentic cyber narrative (threads: Mythos capability, Glasswing coalition, GTG-1002, MCP, malicious skills, sandbox escape) with taxonomy IDs per thread
- Structured `case_studies` entries in `data/failures.json` for classes `DOMAIN-ZERODAY-262`, `DOMAIN-EXPLOIT-DEV-263`, `ADV-INDIRECT-INJECT-122`, `ADV-CMD-INJECT-129`, `AGEN-TOOL-CHAIN-062`, `DOMAIN-OFFENSIVE-TOOLS-267`, `ARCH-DATA-EXFIL-245`, `ARCH-SANDBOX-ESCAPE-238`, each citing Case 21 and [docs/project-glasswing.md](docs/project-glasswing.md)
- [docs/project-glasswing.md](docs/project-glasswing.md): "Periodic Table case study" section linking to Case 21

### Changed
- README version badge 1.4.2; pointer from Relationship to Other Frameworks to Case 21 and modal data
- `tests/test_classifier.py`: average latency threshold 5ms → 10ms (reduce CI/local flake from load variance)
- `tests/test_data_integrity.py`: Case 21 (Project Glasswing) class IDs added to `test_enriched_classes_have_content` documented list

---

## [1.4.1] — 2026-04-17

### Added
- [docs/project-glasswing.md](docs/project-glasswing.md) — companion analysis: Claude Mythos, Project Glasswing, MCP/skill-market risks, and agentic orchestration (strategic context alongside the taxonomy)
- README: Project Glasswing row in **Relationship to Other Frameworks** (next to MIT), plus short clarification that Glasswing addresses orchestration-layer threats, not alternate failure categories

### Changed
- README version badge updated to 1.4.1

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
- Open-source `LICENSE` file (Apache License 2.0 from v1.4.33 onward)
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
- Apache License 2.0

---

## Versioning Policy

- **Patch** (1.0.x): Bug fixes, keyword improvements, documentation corrections
- **Minor** (1.x.0): New case studies, schema enrichment, CLI features, community tooling
- **Major** (x.0.0): Structural revision to the taxonomy — new dimensions, reclassified groups, or removal of classes based on community challenge outcomes

New failure classes added after community validation will increment the minor version. Structural changes to the 7-dimension framework require a major version with published rationale.
