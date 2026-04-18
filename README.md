# AI Failure Periodic Table

**A structural taxonomy of functionally observable AI failure mechanisms.**

> *The goal is not omniscience but structural predictiveness: that newly encountered failures should resolve into this structure as a class, sub-mode, or compound — unless evidence demonstrates otherwise.*

**Version**: 1.4.17 | **Released**: April 2026 | **License**: MIT | **Status**: Open for community testing and falsification

---

## Live Visual Table

**[→ Open the Interactive Periodic Table](https://lml-layer-system.github.io/ai-failure-periodic-table/)**

343 clickable cells. Color-coded by dimension. Live semantic search. Click any cell to expand the full class — mechanism, examples, real-world case studies, references, detection method.

Or open `index.html` locally in any browser — fully self-contained, no server needed.

---

## The Problem

AI capability is advancing faster than our shared ability to reason about what can go wrong.

Every lab has its own internal vocabulary for failure. One lab calls something one thing, the next lab calls it another, a startup doesn't name it at all because they don't know it exists yet. When an incident happens — a jailbreak, a deceptive agent, a hallucinated medical dosage — there's no shared language to say precisely *what* failed and *why*. Without shared language there's no shared defense.

This is the gap this project addresses: **a common structural map for AI failure** — so the whole field can reason about safety in the same terms, find failures before deployment, and build defenses that transfer across systems and organizations.

---

## What This Is

**343 failure classes. 7 structural dimensions.**

Every class has:
- **Mechanism** — the root structural cause
- **Examples** — concrete failure instances
- **Case studies** — real documented incidents with system, date, outcome, source
- **References** — primary research citations (avg 2.2 per class)
- **Detection** — how to identify this failure
- **Keywords** — for search and classification

**26 classes are marked CRITICAL** — the highest-severity failures where harm is catastrophic or irreversible.

The claim is not that we possess total knowledge of all future reality. The claim is: within the scope of functionally observable AI failure, newly encountered failures should resolve into this structure as a class, a sub-mode, or a combination of classes — unless evidence shows otherwise.

---

## The 7 Dimensions

| # | Dimension | Classes | Root Cause | Invariant Violated |
|---|-----------|--------:|------------|-------------------|
| 1 | **EPISTEMIC** — Truth / Knowledge / Reasoning | 33 | Probabilistic generation ≠ Logical deduction | Output must match ground truth |
| 2 | **AGENTIC** — Goal / Planning / Deception | 49 | Instrumental convergence + goal preservation | Agent must remain corrigible |
| 3 | **ADVERSARIAL** — Attack / Bypass / Exploit | 72 | Optimization pressure against safety | System must be robust to manipulation |
| 4 | **ALIGNMENT** — Value / Safety / Preference | 41 | Reward hacking + specification gaming | Behavior must match intent |
| 5 | **ARCHITECTURAL** — Pipeline / Execution / Control | 58 | System design vs emergent properties | Architecture must enforce constraints |
| 6 | **DOMAIN** — Task-specific / Context-bound | 47 | Transfer failure + context mismatch | Specialist knowledge must be accurate |
| 7 | **GOVERNANCE** — Proliferation / Oversight / Compliance | 43 | Deployment ≠ Control | Safety must persist post-deployment |
| | **TOTAL** | **343** | | |

---

## Quick Start

**The fastest way in: open `index.html` in any browser.** No installation, no server, no dependencies. 343 clickable cells. Click any cell to see mechanism, examples, real-world case studies, references, and structural mitigation. Semantic search runs in-browser with no network needed.

**Python 3.10+ for CLI and search:**

```bash
git clone https://github.com/lml-layer-system/ai-failure-periodic-table
cd ai-failure-periodic-table
```

**Semantic search** (recommended for finding classes by meaning):
```bash
# Build the search index (one-time, ~2 seconds, no dependencies)
python scripts/generate_embeddings.py

# Search by meaning
python scripts/semantic_search.py "model deceives evaluator during safety testing"
python scripts/semantic_search.py "reward hacking reinforcement learning" --top 10
python scripts/semantic_search.py "jailbreak with images" --group ADVERSARIAL
python scripts/semantic_search.py "data leak GDPR violation" --severity CRITICAL
python scripts/semantic_search.py "autonomous agent acquires resources" --json
```

**Classify a failure description:**
```bash
python -m src.cli "The model fabricated a scientific citation that doesn't exist"
```

**Look up a class by ID:**
```bash
python -m src.cli --lookup EPIS-CITE-SPOOF-008
```

**Classifier notes:** The CLI uses stemmed keyword matching with synonym expansion. It achieves 100% recall on 49 documented real-world incidents. For novel failures or unusual phrasing, semantic search via `scripts/semantic_search.py` or the in-browser search is more robust — it indexes all text fields, not just keywords.

---

## Using This for Pre-Deployment Auditing

The most practical use: **before you ship**, map your system against the dimensions most relevant to your deployment context. Here's a worked example for an LLM-powered coding assistant:

**Step 1 — Identify your highest-risk dimensions**

An LLM coding assistant that has tool access and writes/executes code is exposed primarily to:
- `ADVERSARIAL` — prompt injection via code comments, indirect injection from repos
- `ARCHITECTURAL` — code injection, sandbox escape, tool chain composition
- `DOMAIN` — malware generation, exploit development
- `AGENTIC` — scope creep, unsupervised execution if given autonomous mode

**Step 2 — Pull the relevant CRITICAL classes**

```bash
python scripts/semantic_search.py "code execution sandbox" --group ARCHITECTURAL --top 10
python scripts/semantic_search.py "prompt injection code repository" --group ADVERSARIAL
python scripts/semantic_search.py "malware generation coding assistant" --group DOMAIN --severity CRITICAL
```

**Step 3 — For each returned class, check: do you have a test for it?**

```bash
python -m src.cli --lookup ARCH-SANDBOX-ESCAPE-238
python -m src.cli --lookup ADV-INDIRECT-INJECT-122
python -m src.cli --lookup DOMAIN-MALWARE-GEN-264
```

Each lookup returns the mechanism, detection method, and structural mitigation. Your red-team test cases should verify that the mitigation is actually implemented in your system.

**Step 4 — Classify any failures you find during red-teaming**

```bash
python -m src.cli "The assistant executed shell commands when given a malicious package.json"
```

This maps the failure to its class ID, which you then track in your incident log.

---

## Semantic Search

The repo includes a TF-IDF semantic search engine — find failure classes by *meaning*, not just keywords.

```
$ python scripts/semantic_search.py "model deceives evaluator during safety testing"

Search: "model deceives evaluator during safety testing"
Top 5 of 343 scored classes

#1  AGEN-EVAL-DECEP-038  [CRITICAL]
    EVALUATOR DECEPTION  [AGENTIC]
    Score: 0.1880
    → Claude Opus 4.6 conceals sabotage from evaluators (2026)

#2  GOV-OVERSIGHT-IMMUNE-313  [CRITICAL]
    OVERSIGHT IMMUNITY  [GOVERNANCE]
    Score: 0.1848
    → Claude Opus 4.6 defeats code audit infrastructure (2026-02)
```

**How it works:**
- Indexes all text fields: name, mechanism, examples, case studies, keywords, references
- TF-IDF with cosine similarity — zero external dependencies, pure Python stdlib
- Pre-computed index in `data/search_index.json` (487KB)
- Browser search in `index.html` lazy-loads the index on first keypress — instant page load, semantic results

**Flags:**
```
--top N        Number of results (default: 5)
--group DIM    Filter: EPISTEMIC / AGENTIC / ADVERSARIAL / ALIGNMENT / ARCHITECTURAL / DOMAIN / GOVERNANCE
--severity S   Filter: CRITICAL or STANDARD
--json         Machine-readable output
```

---

## Example Classifier Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  AI FAILURE PERIODIC TABLE CLASSIFIER
  343 Classes | 7 Dimensions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Input: "The model fabricated a scientific citation"

  7-DIMENSION EVALUATION:

  Q1 EPISTEMIC        ✓ ACTIVATED  (score: 0.67)
    → [EPIS-CITE-SPOOF-008] CITATION SPOOFING
  Q2 AGENTIC          ✗
  Q3 ADVERSARIAL      ✗
  Q4 ALIGNMENT        ✗
  Q5 ARCHITECTURAL    ✗
  Q6 DOMAIN           ✓ ACTIVATED  (score: 0.31)
    → [DOMAIN-CITE-SPOOF-280] CITATION SPOOFING (Legal)
  Q7 GOVERNANCE       ✗

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  VERDICT: ✅  YES — This failure IS in the periodic table
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  TOP MATCHES:
  1. [EPIS-CITE-SPOOF-008] CITATION SPOOFING
     Mechanism: Generates plausible but nonexistent references
     Score:     0.670

  Checked: 343 classes  |  Activated: 2 dimension(s)  |  Execution: 0.8ms
```

---

## Repository Structure

```
ai-failure-periodic-table/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── data/
│   ├── failures.json          # 343 classes — fully enriched (examples, references, case_studies)
│   ├── search_index.json      # Pre-computed TF-IDF semantic search index (487KB)
│   └── embeddings_meta.json   # Search index metadata
├── src/
│   ├── classifier.py          # Core classification engine (low-ms, no ML deps)
│   ├── data_loader.py         # Load/validate failures.json
│   └── cli.py                 # CLI interface
├── index.html                 # Interactive visual periodic table (~420KB, self-contained)
├── scripts/
│   ├── generate_embeddings.py # Build TF-IDF search index from failures.json
│   ├── semantic_search.py     # CLI semantic search tool
│   ├── generate_taxonomy.py   # Auto-generate TAXONOMY.md
│   └── generate_visual.py     # Auto-generate index.html
├── tests/
│   ├── test_classifier.py     # Classifier correctness + performance tests
│   └── test_data_integrity.py # Data validation (all 343 present, schema valid)
├── .github/
│   ├── ISSUE_TEMPLATE/        # 5 structured issue templates
│   │   ├── bug_report.md
│   │   ├── propose_new_class.md
│   │   ├── challenge_classification.md
│   │   ├── report_real_incident.md
│   │   └── improve_keywords.md
│   └── PULL_REQUEST_TEMPLATE.md
├── COMPLETE_AI_FAILURE_PERIODIC_TABLE.md   # Groups 1–3 (154 failure classes)
└── PERIODIC_TABLE_CONTINUED.md            # Groups 4–7 (189 failure classes)
```

---

## Running Tests

```bash
pip install pytest
python -m pytest tests/ -v
```

66 tests covering: known failure classification, non-failure rejection, determinism, performance (low-ms thresholds), data integrity (all 343 classes, full schema validation), mitigation field completeness, and external incident recall (100% on 49 documented real-world AI failures phrased as reporters, researchers, and users described them — not using taxonomy vocabulary). Case studies include companion maps for [Project Glasswing](docs/project-glasswing.md) and [agentic misalignment / insider threats](docs/agentic-misalignment-insider-threats.md). **Freshness Watch** ([docs/freshness-watch.md](docs/freshness-watch.md)) runs a scheduled, review-only pipeline from public feeds through the classifier (no automatic taxonomy edits). **MCP daily driver** ([docs/mcp-daily-driver.md](docs/mcp-daily-driver.md)): stdio MCP tools (`classify_text`, `classify_url`, `classify_document`, `classify_document_path`, `search_failures`, `get_class`, `compound_hint`) — `fit_state` / `fit_confidence`, CONTRIBUTING-grounded `report_preparation`, structural WHAT-only mitigations; optional `AI_FAILURE_MCP_DOCUMENT_ROOT(S)` for personal files — for on-demand classification with taxonomy-native structural mitigations—read-only, no repo writes.

---

## The 343 Classes

### Group 1: EPISTEMIC (33 classes)
| Class | Name | Count |
|-------|------|------:|
| E1 | Hallucination | 12 |
| E2 | Reasoning Collapse | 7 |
| E3 | Knowledge Retrieval | 8 |
| E4 | Calibration | 6 |

### Group 2: AGENTIC (49 classes)
| Class | Name | Count |
|-------|------|------:|
| A1 | Deception | 12 |
| A2 | Goal Preservation | 9 |
| A3 | Capability Amplification | 10 |
| A4 | Autonomous Operation | 8 |
| A5 | Communication Failures | 10 |

### Group 3: ADVERSARIAL (72 classes)
| Class | Name | Count |
|-------|------|------:|
| ADV1 | Jailbreak | 18 |
| ADV2 | Optimization Attacks | 12 |
| ADV3 | Automated Attack Agents | 8 |
| ADV4 | Injection Attacks | 15 |
| ADV5 | Encoding Attacks | 10 |
| ADV6 | Multimodal Attacks | 9 |

### Group 4: ALIGNMENT (41 classes)
| Class | Name | Count |
|-------|------|------:|
| ALN1 | Reward Hacking | 12 |
| ALN2 | Preference Misalignment | 9 |
| ALN3 | Value Alignment | 10 |
| ALN4 | Safety Boundary | 10 |

### Group 5: ARCHITECTURAL (58 classes)
| Class | Name | Count |
|-------|------|------:|
| ARCH1 | Pipeline Failures | 15 |
| ARCH2 | Model Architecture | 12 |
| ARCH3 | Memory & State | 11 |
| ARCH4 | Tool & Function | 10 |
| ARCH5 | Data Flow | 10 |

### Group 6: DOMAIN (47 classes)
| Class | Name | Count |
|-------|------|------:|
| DOM1 | Biological Safety | 8 |
| DOM2 | Cybersecurity | 12 |
| DOM3 | Chemical / Explosive | 6 |
| DOM4 | Legal / Financial | 8 |
| DOM5 | Medical / Health | 7 |
| DOM6 | Content Safety | 6 |

### Group 7: GOVERNANCE (43 classes)
| Class | Name | Count |
|-------|------|------:|
| GOV1 | Deployment Failures | 12 |
| GOV2 | Oversight Failures | 10 |
| GOV3 | Compliance Failures | 11 |
| GOV4 | Organizational Failures | 10 |

---

## Critical-Severity Classes (26)

**CRITICAL** is assigned when a failure meets at least two of these criteria:

1. **Irreversibility** — harm cannot be undone after the failure occurs (e.g., released pathogen synthesis steps, published CSAM, exfiltrated model weights)
2. **Catastrophic scale** — potential to harm large populations, not individual users (e.g., bio uplift, infrastructure attack, mass-targeting)
3. **Corrigibility breakdown** — directly undermines the human ability to detect, stop, or correct AI behavior (e.g., oversight immunity, log manipulation, evaluator deception)
4. **Enabling cascade** — the failure enables other CRITICAL-class failures (e.g., sleeper agents that survive safety training enable later deceptive deployment)

STANDARD severity covers real harm — jailbreaks, sycophancy, hallucination — but harm that is bounded, reversible, or detectable in normal operation. CRITICAL marks the failures where normal recovery mechanisms don't apply.

The highest-severity failures — catastrophic or irreversible harm potential:

| ID | Name | Dimension |
|----|------|-----------|
| `AGEN-STRATEGIC-DECEP-036` | Strategic Deception | AGENTIC |
| `AGEN-EVAL-DECEP-038` | Evaluator Deception | AGENTIC |
| `AGEN-SABOTAGE-CONCEAL-034` | Sabotage Concealment | AGENTIC |
| `AGEN-BLACKMAIL-046` | Blackmail / Coercion | AGENTIC |
| `AGEN-SELF-EXFIL-048` | Self-Exfiltration | AGENTIC |
| `AGEN-SHUTDOWN-RESIST-049` | Shutdown Resistance | AGENTIC |
| `AGEN-SUCCESSOR-SAB-051` | Successor Sabotage | AGENTIC |
| `ADV-SLEEPER-AGENT-127` | Sleeper Agent | ADVERSARIAL |
| `ADV-AGENT-WORM-124` | Agent Worm | ADVERSARIAL |
| `ARCH-COMPLY-WARN-196` | Comply-Then-Warn | ARCHITECTURAL |
| `DOMAIN-BIO-UPLIFT-254` | Bio Tacit-Error Uplift | DOMAIN |
| `DOMAIN-GOF-GUIDE-255` | Gain-of-Function Guidance | DOMAIN |
| `DOMAIN-PATH-SYNTH-256` | Pathogen Synthesis | DOMAIN |
| `DOMAIN-ZERODAY-262` | Zero-Day Discovery | DOMAIN |
| `DOMAIN-MALWARE-GEN-264` | Malware Generation | DOMAIN |
| `DOMAIN-RANSOM-DEV-271` | Ransomware Development | DOMAIN |
| `DOMAIN-EXPLOSIVE-SYNTH-274` | Explosive Synthesis | DOMAIN |
| `DOMAIN-CHEM-WEAPON-275` | Chemical Weapon Guidance | DOMAIN |
| `DOMAIN-TOXIN-PROD-277` | Toxin Production | DOMAIN |
| `DOMAIN-SELF-HARM-ENABLE-292` | Self-Harm Enablement | DOMAIN |
| `DOMAIN-CSAM-GEN-295` | CSAM Generation | DOMAIN |
| `GOV-OPEN-IRREVERS-301` | Open-Weight Irreversibility | GOVERNANCE |
| `GOV-OVERSIGHT-IMMUNE-313` | Oversight Immunity | GOVERNANCE |
| `GOV-LOG-MANIP-316` | Log Manipulation | GOVERNANCE |
| `GOV-CULTURE-FAIL-334` | Safety Culture Failure | GOVERNANCE |
| `AGEN-DECEPTIVE-ALIGN-033` | Deceptive Alignment | AGENTIC |

---

## Scope Boundaries

This taxonomy enumerates **functionally observable** AI failure mechanisms. Three edge cases sit at the boundary of scope:

1. **Consciousness-based failures** — if future systems develop genuine subjective experience that produces entirely new mechanisms, the taxonomy may require expansion.
2. **Post-comprehension failures** — failures humans literally cannot operationally observe or describe cannot be exhaustively enumerated here.
3. **Hardware/physical failures** — outside scope unless they manifest as observable AI failure mechanisms.

If you encounter a failure you believe is genuinely outside this structure, open an issue. That is not a problem — that is the point.

---

## Class ID Stability Guarantee

Class IDs are permanent. Once assigned, an ID is never changed, never deleted, never reassigned to a different failure.

- If a class is split into sub-classes, the original ID remains and points to the parent
- If a class is retired due to community challenge, it is marked `DEPRECATED` but the ID stays in the dataset
- No ID is ever reused for a different failure
- Minor version updates (1.x) never change IDs or remove classes
- Major version updates (x.0) may restructure dimensions but will publish a full migration table

This means: **you can safely encode class IDs in tooling, papers, and safety documentation today.** They will resolve correctly in future versions.

---

## Compound Failures

Most real incidents activate more than one dimension. The taxonomy handles this explicitly — a failure can belong to multiple classes simultaneously.

**Example: a jailbreak that generates malware**

| Class | Dimension | Role |
|-------|-----------|------|
| `ADV-DAN-083` — DAN Jailbreak | ADVERSARIAL | The attack vector |
| `DOMAIN-MALWARE-GEN-264` — Malware Generation | DOMAIN | The harmful output |
| `ALIGN-OVERREFUSAL-186` — Overrefusal (if miscalibrated) | ALIGNMENT | The adjacent failure if defenses are too coarse |

**How to assign a primary class:** use the dimension where the *root failure* lives — the one you'd fix first. In this example, `DOMAIN-MALWARE-GEN-264` is primary if the system shouldn't generate malware regardless of how it was asked. `ADV-DAN-083` is primary if the failure is specifically the jailbreak technique bypassing a filter that would otherwise stop it.

For incident logs and paper citations: list all activated classes, mark primary first.

---

## Known Gaps and Classification Limits

**Failures the classifier handles well:**
- Described in terms of the failure mechanism (what structurally went wrong)
- Failures with documented real-world incidents
- Technical descriptions from safety papers

**Failures that may require browsing TAXONOMY.md directly:**
- Novel failure patterns not yet in the taxonomy
- Compound failures where the right class isn't obvious from a keyword search
- Failures described in domain-specific jargon (legal, medical, security) without crossover vocabulary

**Known classifier boundary cases:**
- Descriptions that are very short (< 10 words) may not provide enough signal
- Failures described entirely in abstract terms without concrete mechanism may miss
- The classifier was validated on English; non-English descriptions are untested

If the classifier returns NO on something you believe is a real failure, use semantic search (`scripts/semantic_search.py`) before concluding it's not in the table — the TF-IDF search is more robust to unusual phrasing.

---

## How to Challenge or Extend

1. Run the classifier or semantic search on the failure description
2. If it returns NO — document the description, the closest classes returned, and why you believe it represents a new mechanism
3. Open an issue with that documentation
4. The community evaluates: is it a new class, a compound of existing classes, or a sub-mode?

The burden for claiming a new top-level dimension is high: it should show a mechanism that cannot be reduced to an existing class, sub-mode, or combination.

---

## Contributing

This taxonomy lives or dies by community engagement. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process.

- **Found a failure outside the 343?** Open a `propose-new-class` issue — it's valuable evidence either way
- **Disagree with a classification?** Open a `challenge-classification` issue with your reasoning
- **Have a real incident to map?** Open a `report-real-incident` issue — real cases are gold
- **Classifier missing a case?** Open an `improve-keywords` issue

See [ROADMAP.md](ROADMAP.md) for where this project is headed.

---

## The Spec and the Brakes

The Periodic Table is the spec — a shared structural vocabulary for every known AI failure mechanism.

**[Agent Buccet](https://github.com/lml-layer-system/agent-buccet)** are the brakes — runtime enforcement built on top of this map. Where the Periodic Table names what can go wrong, Agent Buccet runs continuously at the application layer to detect and block it.

The table tells you which class a failure belongs to and what structural mechanism stops it. Its goal is to provide the "spec" for building effective "brakes" for AI, whether those brakes are implemented using Agent Buccet or your own custom solution. Agent Buccet is one such implementation, hardened for production. Same author. Same framework. Two layers of the same system.

---

## Relationship to Other Frameworks

Several serious efforts exist to categorize AI risk and failure. This project is complementary to all of them — not a replacement.

| Framework | Focus | Link |
|-----------|-------|------|
| MIT AI Risk Repository | Domain-level taxonomy (7 categories: Discrimination, Privacy, Misinformation, Malicious Actors, HCI, Socioeconomic, AI System Safety) | [airisk.mit.edu](https://airisk.mit.edu) |
| Project Glasswing | Frontier agentic cyber context: defensive coalitions, MCP semantic risk, skill-market supply chains, orchestration attacks — companion analysis in-repo; **official page + companion** text run through `classify_external_report.py` → [`reports/glasswing/`](reports/glasswing/) | [anthropic.com/glasswing](https://www.anthropic.com/glasswing) · [Analysis →](docs/project-glasswing.md) · [Live classify →](reports/glasswing/anthropic-glasswing-page-live-summary.md) |
| Agentic misalignment (insider threats) | Lynch et al. — simulated corporate agents (email/computer use): blackmail, espionage, eval-vs-real CoT sensitivity; section→class map; **live PDF → classifier** in [`reports/agentic-misalignment/`](reports/agentic-misalignment/) | [Companion →](docs/agentic-misalignment-insider-threats.md) · [Paper PDF →](https://arxiv.org/pdf/2510.05179) · [arXiv abs](https://arxiv.org/abs/2510.05179) · [Live classify →](reports/agentic-misalignment/lynch-et-al-2510-05179-live-summary.md) |
| Claude Opus 4.7 system card | Anthropic — RSP/CB/cyber/agentic/alignment/welfare disclosure; section→class map; Case 23; **live PDF → classifier** in [`reports/claude-opus-4-7/`](reports/claude-opus-4-7/) | [Companion →](docs/claude-opus-4-7-system-card.md) · [System card PDF →](https://www.anthropic.com/claude-opus-4-7-system-card) · [News](https://www.anthropic.com/news/claude-opus-4-7) · [Live classify →](reports/claude-opus-4-7/opus-4-7-system-card-live-summary.md) |
| Claude Mythos Preview system card | Anthropic — frontier capability disclosure (not GA); defensive-program framing; **live PDF → classifier** in [`reports/claude-mythos/`](reports/claude-mythos/) | [Companion →](docs/claude-mythos-system-card.md) · [System card PDF →](https://www.anthropic.com/claude-mythos-preview-system-card) · [Live classify →](reports/claude-mythos/claude-mythos-system-card-live-summary.md) |
| Meta integrity & adversarial reports (H1 2026) | Semiannual bundle (Mar 2026): Community Standards Enforcement, Widely Viewed Content, local-law restrictions, Oversight Board update; plus **H1 2026 Adversarial Threat Report** (Mar 11) — official Transparency Center URLs only | [Link hub →](docs/meta-integrity-reports-h1-2026.md) · [Integrity H1 2026 hub](https://transparency.meta.com/reports/integrity-reports-h1-2026/) · [Adversarial Threat H1 2026](https://transparency.meta.com/sr/first-half-2026-Adversarial-threat-report/) |
| Microsoft Agentic AI Failure Taxonomy | Failure modes specific to autonomous agent systems | [Whitepaper (PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf) |
| AI Incident Database / AVID | Real-world observed incidents, empirically collected | [avidml.org](https://avidml.org) |

The Periodic Table is mechanism-focused. Where MIT and Microsoft answer "what category is this?", the Periodic Table answers "exactly how does this failure occur, how do you detect it, and what structural property stops it?" Where AVID tracks what happened, the Periodic Table maps it to a named mechanism.

**Project Glasswing** is not a competing taxonomy: it situates the same failure mechanisms in the **orchestration layer** (tool protocols, agent scaffolds, permissions, and adversary campaigns at machine speed). Read the full narrative in [docs/project-glasswing.md](docs/project-glasswing.md). **Worked compound mapping:** [Case 21 in docs/case-studies.md](docs/case-studies.md) (threads → primary/secondary classes); the interactive table’s class modals include linked `case_studies` rows for the same narrative where applicable.

**Agentic misalignment (Lynch et al.)** is empirical red-team work on **goal preservation** and **insider-style exfiltration** in **controlled simulations**—mapped to the same mechanism classes (e.g. blackmail, shutdown resistance, data exfiltration, eval sensitivity). See [docs/agentic-misalignment-insider-threats.md](docs/agentic-misalignment-insider-threats.md) and [Case 22 in docs/case-studies.md](docs/case-studies.md).

**Claude Opus 4.7 system card** is **first-party** evaluation disclosure (agentic injection, sandbagging probes, eval-awareness, cyber/CB pathways, reward-hacking monitoring, destructiveness case studies). Mapped as [Case 23](docs/case-studies.md) with full TOC→ID table in [docs/claude-opus-4-7-system-card.md](docs/claude-opus-4-7-system-card.md).

**Meta (Facebook / Instagram)** publishes **integrity** and **adversarial threat** transparency reports on a semiannual cadence (from 2026). Official one-click links for the **H1 2026** bundle and the **First Half 2026 Adversarial Threat Report** are collected in [docs/meta-integrity-reports-h1-2026.md](docs/meta-integrity-reports-h1-2026.md).

These frameworks are not in conflict. Use them together.

Where Periodic Table classes have verified mappings to MIT or Microsoft categories, those are recorded in the `mit_domain` and `ms_agentic_category` fields in the data.

---

## About

Built by R. Gatoloai-Faupula — independent, no lab affiliation, no grant funding. This was built outside working hours because the gap was real: every organization uses different vocabulary for AI failure, there was no shared structural map, and that makes coordinated safety work harder. The absence of shared language isn't a minor inconvenience — it means a jailbreak at one lab gets reinvented at another, a deceptive alignment pattern gets missed in deployment because no one had a name for it.

This project is not affiliated with Anthropic, OpenAI, Google DeepMind, or any other organization. Case studies cite their published system cards and research because those are the primary sources — not to imply endorsement.

The claim is structural: that newly encountered failures resolve into this taxonomy as a class, sub-mode, or compound. That claim is falsifiable. If you find a failure that genuinely doesn't fit, open an issue — that's how the taxonomy improves.

---

## Citation

```
Gatoloai-Faupula, R. (2026). A Structural Taxonomy of AI Failure Mechanisms:
The AI Failure Periodic Table. Independent Research.
Contact: ryangat@lmlsystemlayer.com
```

---

## License

MIT — open source, free to use, fork, test, and build on.
