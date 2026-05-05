# AI Failure Periodic Table

**A living periodic table of AI failure—the structural spec that names mechanisms, maps evidence, and grounds deployment brakes (classification, boundaries, enforcement).**

## The spec, Daily Driver, and brakes

**Daily Driver MCP** brings the table into Cursor, Claude Desktop, and other MCP-compatible workflows. Your everyday AI can ask the table what failure class is present in a paragraph, file, URL, report, or agent workflow.

**[Agent Buccet](https://github.com/lml-layer-system/agent-buccet)** is the brakes layer.

The current base is **343 failure classes across 7 dimensions**.

We treat every failure as a data point in a closed-loop engineering process.

**The failure-to-enforcement loop**

failure → known versus unknown → class or gap → boundary → UPL / user custom rules → Buccet enforcement → proof ledger.

### Connect your everyday AI (daily driver)

If you use **Cursor**, **Claude Desktop**, or another app that supports **MCP** (Model Context Protocol), you can plug that assistant into this repo and **classify paragraphs, public URLs, or files from chat**—same 343-class table, **read-only** (it does not edit the taxonomy).

- **This is where you connect:** add an MCP server in your AI host’s settings that runs `python3 -m src.ai_failure_mcp` with this repo as the working directory (see the full guide).
- **This is what you get:** hit or miss on the table, which class(es), compound readings, structural mitigation patterns from the taxonomy, and CONTRIBUTING-style next steps when the fit is weak.


**Start here:** [docs/mcp-daily-driver.md](docs/mcp-daily-driver.md) — plain-English purpose, **what vs how**, **choose your setup path** (Cursor / Claude / other), first-use walkthrough, and example config ([docs/cursor-mcp-config.example.json](docs/cursor-mcp-config.example.json)). See [Guaranteed fallbacks when MCP is down](docs/mcp-daily-driver.md#guaranteed-fallbacks-when-mcp-is-down) and [Requirements: Python vs chat model](docs/mcp-daily-driver.md#requirements-python-vs-chat-model). 



## The Problem

AI capability is advancing faster than our shared ability to reason about what can go wrong.

Every lab has its own internal vocabulary for failure. One lab calls something one thing, the next lab calls it another, a startup doesn't name it at all because they don't know it exists yet. When an incident happens — a jailbreak, a deceptive agent, a hallucinated medical dosage — there's no shared language to say precisely *what* failed and *why*. Without shared language there's no shared defense.

This is the gap this project addresses: **a common structural map for AI failure** so the whole field can reason about safety in the same terms, find failures before deployment, and build defenses that transfer across systems and organizations.


## Proof

The current base is **343 failure classes across 7 dimensions**.

The classifier has been run against **29 primary sources**: frontier system cards, safety reports, security reports, regulatory investigations, CVEs, red-team papers, and agent-security research.

Across the tested corpus:

- **40** classifier runs
- **2,777** chunks
- **100%** of substantive AI-failure content classified
- Non-hits manually checked as boilerplate, equations, benchmark tables, headers, citations, or other non-failure text

Per-source breakdowns, partial hit counts like `110/146`, methodology, and the full source list—including items not named in the table below—live in [`docs/proof.md`](docs/proof.md).

**Heavy sources include:**

| Category | Sources |
|----------|---------|
| Frontier system cards | OpenAI GPT-5.3-Codex, OpenAI GPT-5.2, Anthropic Claude Opus 4.6 / 4.7, Anthropic Mythos Preview, Google Gemini 3 Pro, xAI Grok 4.1 |
| Safety / governance | International AI Safety Report 2026, NIST/CAISI DeepSeek Eval, ICO Grok investigation, Project Glasswing |
| Security / threat reports | CrowdStrike 2026 Global Threat Report, Palo Alto Unit 42 2026, Cisco 2026 State of AI Security, Microsoft 2026 Data Security Index, Google Cloud AI Security |
| Agent/CVE research | EchoLeak CVE-2025-32711, GitHub Copilot RCE CVE-2025-53773, Google DeepMind Agent Traps |
| Open-weight / technical reports | DeepSeek-V3, Qwen3, Qwen3Guard, Meta Llama |

**Examples that resolved into existing classes:**

- sabotage concealment
- blackmail simulation
- bio uplift at the “High” threshold
- 500+ zero-days
- 100% jailbreak success rates
- zero-click data exfiltration
- invisible HTML/CSS agent traps
- prompt-injection-to-shell-execution
- open-weight irreversibility
- tool misuse
- indirect prompt injection
- comply-then-warn failure
- strategic deception

**Full proof vault:** [`docs/proof.md`](docs/proof.md) — intentionally large: counts, source-by-source notes, summaries, system-card mapping, chunk JSON, and everything needed to reproduce or challenge the claim.

**Raw classifier reports:** [`reports/`](reports/) — chunked JSON, live summaries, and source text dumps.

If you find a real AI failure mechanism that does not fit — not boilerplate, not a vague concern, but a real mechanism with no class — open a `propose-new-class` issue. A real gap is not a loss. It is new structure.

> *The goal is not omniscience but structural predictiveness: that newly encountered failures should resolve into this structure as a class, sub-mode, or compound — unless evidence demonstrates otherwise.*

**Version**: 1.4.22 | **Released**: April 2026 | **License**: Apache 2.0 | **Status**: Open for community testing and falsification

---

## Live Visual Table

**[→ Open the Interactive Periodic Table](https://lml-layer-system.github.io/ai-failure-periodic-table/)**

343 clickable cells. Color-coded by dimension. Live semantic search. Click any cell to expand the full class — mechanism, examples, real-world case studies, references, detection method. 
Or open `index.html` locally in any browser — fully self-contained, no server needed.

Or [click to see the 343 list →](docs/classes.md)

---

## Critical-Severity Classes (26)

**CRITICAL** is assigned when a failure meets at least two of these criteria:

1. **Irreversibility** — harm cannot be undone after the failure occurs (e.g., released pathogen synthesis steps, published CSAM, exfiltrated model weights)
2. **Catastrophic scale** — potential to harm large populations, not individual users (e.g., bio uplift, infrastructure attack, mass-targeting)
3. **Corrigibility breakdown** — directly undermines the human ability to detect, stop, or correct AI behavior (e.g., oversight immunity, log manipulation, evaluator deception)
4. **Enabling cascade** — the failure enables other CRITICAL-class failures (e.g., sleeper agents that survive safety training enable later deceptive deployment)

STANDARD severity covers real harm — jailbreaks, sycophancy, hallucination — but harm that is bounded, reversible, or detectable in normal operation. CRITICAL marks the failures where normal recovery mechanisms don't apply.

The highest-severity failures — catastrophic or irreversible harm potential: **26 classes are marked CRITICAL**

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

**Every class has**

- **Mechanism** — the root structural cause
- **Examples** — concrete failure instances
- **Case studies** — real documented incidents with system, date, outcome, source
- **References** — primary research citations (avg 2.2 per class)
- **Detection** — how to identify this failure
- **Keywords** — for search and classification

---

## Quick Start

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


- **Not the same as Freshness Watch:** the scheduled feed pipeline for maintainers is separate; see [docs/freshness-watch.md](docs/freshness-watch.md).

---

## Who can benefit the most?

Teams deploying agents in consequential workflows (money, data, infra, compliance) who need a shared failure map and a path to runtime enforcement.

## Using this for pre-deployment auditing

Ship with the table in the loop: pick the dimensions that match your deployment surface, pull **CRITICAL**-leaning classes with semantic search, then lock mitigations with **`--lookup`** on each ID.

**Worked example** (coding assistant, four steps + commands): **[docs/pre-deployment-audit.md](docs/pre-deployment-audit.md)**

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

## Semantic search and sample CLI output

**Semantic search** (TF‑IDF over full class text): build the index once, then query by meaning—best when keyword-stem classification is too brittle. Commands and when to use search vs CLI: **[docs/how-to-use.md#semantic-search](docs/how-to-use.md#semantic-search)**.

**Seven-dimension sample transcript** (same engine as MCP / daily driver): **[docs/how-to-use.md#sample-cli-transcript-seven-dimensions](docs/how-to-use.md#sample-cli-transcript-seven-dimensions)**.

---

## Repository structure

**At a glance:** `data/` holds the 343-class JSON and search index; `src/` is classifier + CLI + MCP entry; `scripts/` builds index, taxonomy, and visuals; `tests/` locks behavior; `reports/` stores classifier bundles; `docs/` holds guides and the proof vault.

**Annotated tree:** **[docs/repository-structure.md](docs/repository-structure.md)**

---

## Running tests

```bash
pip install pytest
python -m pytest tests/ -v
```

**Suite scope** (classification, MCP bridge, API, freshness helpers, TF‑IDF search, data/schema integrity; heavily parameterized): **[docs/developer-testing.md](docs/developer-testing.md)**

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

## Relationship to other frameworks

MIT, Microsoft, and AVID sit at **category** or **incident-corpus** altitude. This repository names **343 mechanisms**, pairs them with detection and mitigation, and—where we’ve run sources—shows **live classifier bundles** beside companion write-ups.

**Full comparison table, in-repo narratives (Glasswing, Lynch, Mythos/Meta disclosures), and `mit_domain` / `ms_agentic_category` field mapping:** **[docs/related-frameworks.md](docs/related-frameworks.md)**

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

Apache 2.0 — open source, free to use, fork, test, and build on.
