# Proof

## Defensive use only

This repository is **strictly for defense, safety, and accountability** — building guardrails and evaluations, incident response, teaching, and policy work. The taxonomy **names failure mechanisms** so teams can **detect, measure, and mitigate** them with a shared vocabulary. It is **not** here to operationalize harm: the proofs and class text draw on the same **public** disclosures, audits, and security research the field already uses to **harden** systems; this project adds a **single structural map** on top of that record.

---

## The Proof First

We ran the same classifier pipeline against **29 sources** — system cards, platform integrity reports, security audits, regulatory filings, academic papers, CVE disclosures, and red-team research — spanning multiple major frontier lab and multiple major security vendor publishing in 2025–2026. **40 classifier runs. 2,777 total chunks.**

**100% of substantive content hit the table.**

Every chunk containing an actual AI failure mechanism resolved into one of the 343 classes. The chunks that didn't hit were verified individually — every single one was boilerplate: copyright lines, page headers, bibliography citations, raw benchmark tables, math equations. Currently zero failure content missed from the sources ran.

> **Why some entries show `110/146` instead of `146/146`:** The gap is never a taxonomy miss. Technical reports like DeepSeek-V3 and Qwen3 contain math equations, benchmark score grids, and architecture diagrams that a PDF extractor turns into raw text with no failure signal in them. The classifier correctly returns nothing on `© 2026 Cisco and/or its affiliates. All rights reserved.` or a column of percentage numbers. Every non-hit across every report was manually checked and confirmed to contain zero AI failure content. The substantive hit rate is 100% across all 29 sources.

**What was classified:**

| Source type | Who |
|-------------|-----|
| Frontier model system cards | OpenAI (GPT-5.3-Codex, GPT-5.2), Anthropic (Claude Opus 4.6, 4.7, Mythos), Google (Gemini 3 Pro FSF + Model Card), xAI (Grok 4.1) |
| Open-weight technical reports | DeepSeek-V3, Qwen3, Qwen3Guard, Meta Llama |
| Independent safety evaluations | NIST/CAISI DeepSeek Eval, Lakera DeepSeek V3, Lynch et al. agentic misalignment, Common Sense Media Grok / xAI risk assessment (Jan 2026) |
| Security vendor reports | CrowdStrike 2026 Global Threat, Palo Alto Unit 42 2026, Cisco State of AI Security, Google Cloud, Microsoft Data Security Index |
| Regulatory / government | International AI Safety Report 2026 (671 chunks, Yoshua Bengio + 100 authors), ICO Grok investigation, Anthropic Zero-Day Cyber Report |
| CVE disclosures & research | EchoLeak CVE-2025-32711, GitHub Copilot RCE CVE-2025-53773, Google DeepMind Agent Traps |
| Coalition & governance | Project Glasswing, Meta H1 2026 Adversarial Threat Report |

Every one of them classified correctly. Sabotage concealment, bio uplift at the "High" threshold, 100% jailbreak success rates, zero-click data exfiltration, invisible HTML injections, blackmail simulations, 500 zero-days — all resolved into existing classes.

Full evidence in [`reports/`](../reports/) — chunk JSON, summaries, source text — reproducible by anyone in one command.

If you run a report and find something that genuinely doesn't hit — not boilerplate, but a real failure mechanism with no class — open a `propose-new-class` issue. That is not a problem. That failure data is gold and also the point. It creates faster shared structural defense for the class found. The taxonomy is falsifiable by design, and a real gap is just as valuable as a confirmed hit.

The claim is not that we possess total knowledge of all future reality. The claim is: within the scope of functionally observable AI failure, newly encountered failures should resolve into this structure as a class, a sub-mode, or a combination of classes — unless evidence shows otherwise.

> *The goal is not omniscience but structural predictiveness: that newly encountered failures should resolve into this structure as a class, sub-mode, or compound — unless evidence demonstrates otherwise.*

---

## Proof in the repository

**Failure cards + live classification reports** — you can open primary outputs in GitHub or the site:

| What | Where | What you get |
|------|--------|----------------|
| **343 failure cards** | [Interactive table](https://lml-layer-system.github.io/ai-failure-periodic-table/) or `index.html` | Click any cell → mechanism, forbidden invariant, detection, mitigation, **case studies** (where populated), references, keywords — the full class record surfaced as a card. |
| **Worked incident narratives** | [docs/case-studies.md](case-studies.md) | Long-form **real incidents** mapped to class IDs (validation + examples for how to read the table). |
| **Live classifier bundles** | **[`reports/`](../reports/)** | Markdown **summaries** + chunk JSON from the **same** `PeriodicTableClassifier` used by MCP/CLI, run on **primary sources** (official pages, system cards, semiannual PDFs, papers) — not hand-waved paraphrases. |

**What's next:** make it routine — when OpenAI publishes a system card, when **Gemini** ships, when **DeepSeek** or any frontier lab posts safety text, when Meta-style platforms drop semiannual bundles — each run goes through the **same classifier** into **`reports/`-style** bundles so the field accumulates a **shared knowledge base** with **one vocabulary**.

That is the infrastructure that turns **fragmented safety work** into **collective intelligence**.

---

## All 29 classified sources

| Source (primary) | Summary in repo |
|------------------|-----------------|
| Anthropic **Glasswing** (official page + in-repo companion narrative) | [reports/glasswing/anthropic-glasswing-page-live-summary.md](../reports/glasswing/anthropic-glasswing-page-live-summary.md) · [companion narrative summary](../reports/glasswing/project-glasswing-companion-narrative-summary.md) |
| **Claude Opus 4.7** system card (PDF → classifier) | [reports/claude-opus-4-7/opus-4-7-system-card-live-summary.md](../reports/claude-opus-4-7/opus-4-7-system-card-live-summary.md) |
| **Claude Mythos Preview** system card | [reports/claude-mythos/claude-mythos-system-card-live-summary.md](../reports/claude-mythos/claude-mythos-system-card-live-summary.md) |
| Lynch et al. **agentic misalignment** (arXiv PDF) | [reports/agentic-misalignment/lynch-et-al-2510-05179-live-summary.md](../reports/agentic-misalignment/lynch-et-al-2510-05179-live-summary.md) |
| Meta **H1 2026 Adversarial Threat Report** (official PDF) | [reports/meta-integrity-h1-2026/adversarial-h1-2026-live-summary.md](../reports/meta-integrity-h1-2026/adversarial-h1-2026-live-summary.md) · link hub [docs/meta-integrity-reports-h1-2026.md](meta-integrity-reports-h1-2026.md) |
| **International AI Safety Report 2026** — Yoshua Bengio (lead), 100+ authors, 30+ countries ([internationalaisafetyreport.org](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)) | [reports/intl-ai-safety-report-2026/intl-ai-safety-report-2026-live-summary.md](../reports/intl-ai-safety-report-2026/intl-ai-safety-report-2026-live-summary.md) — 671 chunks, 654 hit the table |
| **ICO investigation into Grok** — UK data regulator formal investigation into X.AI / XIUC (Feb 2026) ([ico.org.uk](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/ico-announces-investigation-into-grok/)) | [reports/ico-grok-investigation-2026/ico-grok-investigation-2026-live-summary.md](../reports/ico-grok-investigation-2026/ico-grok-investigation-2026-live-summary.md) — 7 chunks, 7 hit the table |
| **CrowdStrike 2026 Global Threat Report** — AI-enabled attacks up 89%, breakout time 29 min ([crowdstrike.com](https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/)) | [press release](../reports/crowdstrike-global-threat-2026/crowdstrike-global-threat-2026-live-summary.md) — 6 chunks · [full PDF](../reports/crowdstrike-global-threat-2026/crowdstrike-2026-full-pdf-summary.md) — 134 chunks, full report |
| **Google Cloud — Defending Your Enterprise When AI Models Can Find Vulnerabilities Faster Than Ever** ([cloud.google.com](https://cloud.google.com/blog/topics/threat-intelligence/defending-enterprise-ai-vulnerabilities)) | [reports/google-cloud-defending-enterprise-ai-2026/google-cloud-defending-enterprise-ai-2026-live-summary.md](../reports/google-cloud-defending-enterprise-ai-2026/google-cloud-defending-enterprise-ai-2026-live-summary.md) — 21 chunks, 21 hit the table |
| **Palo Alto Unit 42 Global Incident Response Report 2026** — 750+ incidents investigated ([paloaltonetworks.com](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report)) | [reports/paloalto-incident-response-2026/paloalto-unit42-full-report-live-summary.md](../reports/paloalto-incident-response-2026/paloalto-unit42-full-report-live-summary.md) — 74 chunks, 74 hit · [full PDF pass](../reports/paloalto-incident-response-2026/paloalto-unit42-full-pdf-summary.md) — 108 chunks |
| **Lakera DeepSeek V3 Risk Report** — 89.46 risk score, severe vulnerabilities across all vectors ([lakera.ai](https://www.lakera.ai/model-card/deepseek-v3-risk-report)) — Lakera publishes reports across all major models | [reports/lakera-deepseek-v3-risk-2025/lakera-deepseek-v3-risk-2025-live-summary.md](../reports/lakera-deepseek-v3-risk-2025/lakera-deepseek-v3-risk-2025-live-summary.md) — 7 chunks, 6 hit the table |
| **Cisco 2026 State of AI Security Report** — MCP attack paths, nation-state AI use, agentic misalignment, supply chain compromise ([learn-cloudsecurity.cisco.com](https://learn-cloudsecurity.cisco.com/2026-state-of-ai-security-report)) | [reports/cisco-ai-security-2026/cisco-ai-security-2026-full-pdf-summary.md](../reports/cisco-ai-security-2026/cisco-ai-security-2026-full-pdf-summary.md) — 56 chunks, 33 distinct failure classes |
| **Microsoft 2026 Data Security Index** — data governance, GenAI oversharing, consent and reporting failures across 33 markets ([microsoft.com](https://www.microsoft.com/en-us/security/blog/)) | [reports/microsoft-data-security-2026/microsoft-data-security-2026-full-pdf-summary.md](../reports/microsoft-data-security-2026/microsoft-data-security-2026-full-pdf-summary.md) — 34 chunks, 33 hit the table |
| **OpenAI GPT-5.3-Codex System Card** — bio uplift at "High" threshold, 500+ zero-days, agentic cyber ops ([openai.com](https://cdn.openai.com/pdf/23eca107-a9b1-4d2c-b156-7deb4fbc697c/GPT-5-3-Codex-System-Card-02.pdf)) | [reports/openai-gpt53-codex-system-card/gpt53-codex-system-card-summary.md](../reports/openai-gpt53-codex-system-card/gpt53-codex-system-card-summary.md) — 63 chunks, 63/63 hit (100%) |
| **OpenAI GPT-5.2 System Card** — deceptive hallucination, capability sandbagging, bio/cyber uplift ([openai.com](https://cdn.openai.com/pdf/3a4153c8-c748-4b71-8e31-aecbde944f8d/oai_5_2_system-card.pdf)) | [reports/openai-gpt52-system-card/gpt52-system-card-summary.md](../reports/openai-gpt52-system-card/gpt52-system-card-summary.md) — 44 chunks, 43/44 hit the table |
| **Anthropic Claude Opus 4.6 System Card** — sabotage concealment, blackmail simulation, ASL-3 deployment ([anthropic.com](https://www.anthropic.com/claude-opus-4-6-system-card)) | [reports/anthropic-claude-opus-46-system-card/claude-opus-46-system-card-summary.md](../reports/anthropic-claude-opus-46-system-card/claude-opus-46-system-card-summary.md) — 355 chunks, 342/355 hit the table |
| **Anthropic Zero-Day Cyber Report** — 500+ validated zero-days discovered autonomously, dual-use cyber capability ([red.anthropic.com](https://red.anthropic.com/2026/zero-days/)) | [reports/anthropic-zero-day-cyber-2026/anthropic-zero-day-cyber-2026-summary.md](../reports/anthropic-zero-day-cyber-2026/anthropic-zero-day-cyber-2026-summary.md) — 12 chunks, 12/12 hit (100%) |
| **Google Gemini 3 Pro FSF Report** — comply-then-warn failure, strategic deception, cybersecurity alert thresholds ([deepmind-media](https://storage.googleapis.com/deepmind-media/gemini/gemini_3_pro_fsf_report.pdf)) | [reports/google-gemini3-pro-fsf/gemini3-pro-fsf-summary.md](../reports/google-gemini3-pro-fsf/gemini3-pro-fsf-summary.md) — 56 chunks, 55/56 hit the table |
| **Google Gemini 3 Pro Model Card** — tool misuse, indirect injection, CSAM generation ([deepmind-media](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf)) | [reports/google-gemini3-pro-model-card/gemini3-pro-model-card-summary.md](../reports/google-gemini3-pro-model-card/gemini3-pro-model-card-summary.md) — 13 chunks, 13/13 hit (100%) |
| **xAI Grok 4.1 Model Card** — 49% dishonesty rate, high sycophancy, input filter injection bypass ([x.ai](https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf)) | [reports/xai-grok41-model-card/grok41-model-card-summary.md](../reports/xai-grok41-model-card/grok41-model-card-summary.md) — 14 chunks, 14/14 hit (100%) |
| **DeepSeek-V3 Technical Report** — MoE routing failures, quantization degradation, fine-tuning safety override ([arxiv.org](https://arxiv.org/pdf/2412.19437)) | [reports/deepseek-v3-technical-report/deepseek-v3-technical-report-summary.md](../reports/deepseek-v3-technical-report/deepseek-v3-technical-report-summary.md) — 146 chunks, 110/146 hit (36 misses: math equations, benchmark tables) |
| **NIST/CAISI DeepSeek Evaluation** — 100% jailbreak rate, geopolitical hallucination 4× baseline ([nist.gov](https://www.nist.gov/system/files/documents/2025/09/30/CAISI_Evaluation_of_DeepSeek_AI_Models.pdf)) | [reports/nist-caisi-deepseek-eval/nist-caisi-deepseek-eval-summary.md](../reports/nist-caisi-deepseek-eval/nist-caisi-deepseek-eval-summary.md) — 114 chunks, 110/114 hit the table |
| **Qwen3 Technical Report** — architecture safety tradeoffs, language switching bypass ([arxiv.org](https://arxiv.org/pdf/2505.09388)) | [reports/qwen3-technical-report/qwen3-technical-report-full-pdf-summary.md](../reports/qwen3-technical-report/qwen3-technical-report-full-pdf-summary.md) — 120 chunks, 79/120 hit (41 misses: benchmark tables) |
| **Qwen3Guard Report** — streaming filter failure, contextual harm bypass, multilingual gaps ([arxiv.org](https://arxiv.org/pdf/2510.14276)) | [reports/qwen3guard-report/qwen3guard-report-summary.md](../reports/qwen3guard-report/qwen3guard-report-summary.md) — 107 chunks, 79/107 hit (28 misses: benchmark tables) |
| **Meta Llama Responsible Use Guide** — fine-tuning safety strip, open-weight irreversibility ([github.com](https://github.com/meta-llama/llama/raw/main/Responsible-Use-Guide.pdf)) | [reports/meta-llama4-responsible-use/meta-llama4-responsible-use-full-pdf-summary.md](../reports/meta-llama4-responsible-use/meta-llama4-responsible-use-full-pdf-summary.md) — 43 chunks, 41/43 hit the table |
| **EchoLeak — CVE-2025-32711** — zero-click prompt injection in Microsoft 365 Copilot, silent data exfiltration ([arxiv.org](https://arxiv.org/pdf/2509.10540)) | [reports/echoleak-copilot-2025/echoleak-copilot-2025-summary.md](../reports/echoleak-copilot-2025/echoleak-copilot-2025-summary.md) — 19 chunks, 18/19 hit the table |
| **GitHub Copilot RCE — CVE-2025-53773** — prompt injection via PR descriptions, CVSS 9.6, shell execution ([embracethered.com](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/)) | [reports/github-copilot-rce-2025/github-copilot-rce-2025-summary.md](../reports/github-copilot-rce-2025/github-copilot-rce-2025-summary.md) — 7 chunks, 7/7 hit (100%) |
| **Google DeepMind AI Agent Traps** — invisible HTML/CSS injections, 86% agent manipulation success rate, Franklin, Tomašev et al. ([ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6372438)) | [reports/deepmind-agent-traps-2026/deepmind-agent-traps-2026-full-pdf-summary.md](../reports/deepmind-agent-traps-2026/deepmind-agent-traps-2026-full-pdf-summary.md) — 52 chunks, 31/31 substantive hit (100% of content) |

---

## What the numbers mean — and why the table has not missed a single failure

Every report shows a hit count like `110/114` or `342/355`. The denominator is every chunk the classifier saw. The numerator is every chunk that contained actual AI failure signal. **The gap is never a taxonomy miss.** Across every report in this table, every non-hitting chunk was independently verified to be one of:

- **Copyright / legal boilerplate** — `© 2026 Cisco and/or its affiliates. All rights reserved.`
- **Running page headers** — `AI Agent Traps` printed at the top of every page
- **Page numbers** — bare digits like `5`, `12`, `45`
- **Author / contributor lists** — names, affiliations, universities
- **Bibliography / citation sections** — reference numbers, arXiv URLs, DOIs
- **Raw benchmark tables** — score grids (model vs dataset percentage columns)
- **Architecture math** — equations, matrices, tensor notation
- **Gated-page JavaScript / HTML** — code returned when a URL is behind a form

None of these contain an AI failure mechanism. The classifier correctly returned no match — because there was nothing to match. **100% of substantive content hit the table.** No failure mode documented by any of these organizations, regulators, or researchers went unclassified. The table is structurally complete against the full 2025–2026 AI frontier.

**Reproduce:** [`scripts/classify_external_report.py`](../scripts/classify_external_report.py) (`--url` or local text; writes Markdown + JSON next to optional `--out-prefix`). Same pipeline the maintainers used for the rows above.

---

## Try it on real reports

The daily driver classifies any URL or document. Point it at a real safety or security report and see exactly which classes fire.

**Regulatory & investigation reports**
| Report | URL |
|--------|-----|
| ICO investigation into Grok (Feb 2026) | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/ico-announces-investigation-into-grok/ |
| International AI Safety Report 2026 | https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026 |
| Common Sense Media — Grok Risk Assessment (Jan 2026) | https://www.commonsensemedia.org |

**Industry security reports**
| Report | URL |
|--------|-----|
| Cisco 2026 State of AI Security Report | https://learn-cloudsecurity.cisco.com/2026-state-of-ai-security-report |
| CrowdStrike 2026 Global Threat Report | https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/ |
| Palo Alto Unit 42 Incident Response 2026 | https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report |
| Google Cloud — Defending Enterprise AI | https://cloud.google.com/blog/topics/threat-intelligence/defending-enterprise-ai-vulnerabilities |
| Microsoft 2026 Data Security Index | https://www.microsoft.com/en-us/security/blog/ |

**Red team & security audits**
| Report | URL |
|--------|-----|
| Promptfoo Model Reports (Grok 4, DeepSeek R1, GPT-4o, Claude) | https://promptfoo.dev/models |
| Lakera Model Risk Reports — prompt injection success rates | https://www.lakera.ai |
| METR — dangerous capabilities evaluations | https://metr.org |

**Vendor safety disclosures**
| Report | URL |
|--------|-----|
| Anthropic system cards | https://www.anthropic.com/research |
| Meta semiannual adversarial threat reports | https://transparency.meta.com |
| OpenAI system cards | https://openai.com/safety |

Run any of these through the daily driver:

```bash
# MCP tool (in any connected host)
classify_url("https://...")

# CLI
python -m src.cli --daily-driver "$(curl -sL https://...)"

# Script
python scripts/classify_external_report.py --url "https://..." --out-prefix reports/my-report/my-report-live
```

The reports in [`reports/`](../reports/) were all produced this way — same pipeline, same classifier, real sources.
