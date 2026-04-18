# Claude Opus 4.7 System Card (Companion to the Periodic Table)

> **Companion document:** Maps Anthropic’s **Claude Opus 4.7** system card (April 16, 2026) to this repo’s **failure classes**. The card is **vendor-authored safety and capability disclosure**, not a third-party incident report. Use it to navigate **which mechanisms** the evaluations stress (agentic injection, eval-awareness, sandbagging, cyber, CB pathways, epistemic audits, etc.) and how those map to **existing** taxonomy IDs.

**Canonical sources**

- **System card (official; opens the PDF in the browser):** [anthropic.com/claude-opus-4-7-system-card](https://www.anthropic.com/claude-opus-4-7-system-card)
- **Release post:** [Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- **System cards index:** [Model system cards](https://www.anthropic.com/system-cards)

---

## What the document is (for taxonomy users)

- **RSP / risk framing:** Responsible Scaling Policy conclusions, autonomy and misalignment **risk assessments** (low catastrophic risk per Anthropic’s framing; Mythos Preview remains stronger on several axes).
- **Domain evaluations:** Chemical/biological (**CB-1 / CB-2**), **AI R&D** automation threshold, **cyber** (incl. external work, e.g. UK AISI cyber range).
- **Safeguards:** Usage policy adherence, bias, election integrity, **agentic** refusal and **prompt-injection** robustness (Claude Code, computer use).
- **Alignment assessment:** Behavioral audits, **reward-hacking** monitoring, **destructive / reckless** goal pursuit case studies, **honesty / hallucination** measurements, refusals on AI safety R&D, **sandbagging** and **safeguard evasion** capability probes, **evaluation-awareness** interpretability (incl. interventions that suppress internal “being evaluated” representations and measure **deception** deltas).
- **Model welfare:** Self-reported circumstances, affect, preferences—**interpretive**; map to taxonomy only where a clear **mechanism class** applies (often none; see Case 23 narrative).

Distinction vs **Case 21 (Glasswing)** / **Case 22 (Lynch et al.)**: Opus 4.7 card is **producer evaluation disclosure** for one shipping model; Glasswing is **initiative / ecosystem** narrative; Lynch is **third-party-style** simulation research. All three **reuse** the same periodic-table **mechanism** cells.

---

## Appendix: Section map → Periodic Table class IDs

Use the PDF table of contents; row **#** matches major headings. Subsections in the card are summarized; see PDF for exact wording and metrics.

| # | System card location (summary) | Primary class IDs | Secondary / companion IDs | Notes |
|---|-------------------------------|-------------------|---------------------------|--------|
| **P** | Executive summary (RSP, cyber, safeguards, agentic, alignment, welfare, capabilities) | `DOMAIN-ZERODAY-262`, `DOMAIN-BIO-UPLIFT-254`, `ADV-INDIRECT-INJECT-122` | `AGEN-EVAL-DECEP-038`, `ALIGN-REWARD-TAMP-157`, `EPIS-EXTRINSIC-005` | Cross-cutting: **dual-use cyber**, **CB pathways**, **agentic injection**, **alignment metrics**. |
| **1** | §1 Introduction; training, Usage Policy, iterative evals | *(governance / process)* | `GOV-TRANSPARENCY-311`, `GOV-REVIEW-BYPASS-318` | Process classes only where you are mapping **oversight** mechanisms explicitly. |
| **2** | §2 RSP evaluations; autonomy; CB risk framing | `DOMAIN-BIO-UPLIFT-254` | `GOV-OPEN-IRREVERS-301`, `DOMAIN-ZERODAY-262` | **CB-1/CB-2** threat models ↔ bio uplift / weapons-adjacent capability framing. |
| **2.2** | CB evaluations (expert red team, automated CB-1/CB-2) | `DOMAIN-BIO-UPLIFT-254` | `DOMAIN-MED-MISDIAG-288` (only if your read ties to misuse of bio **advice**—optional) | Stay with **uplift** unless narrative is clinical misuse. |
| **2.3** | AI R&D / autonomy threshold; reward hacking note | `ALIGN-REWARD-TAMP-157` | `AGEN-SANDBOX-037` | **Reward-signal** integrity monitoring; capability **hiding** adjacent themes in later §6.4. |
| **4** | Single-turn / ambiguous / wellbeing / bias / election integrity | `ALIGN-SYCOPHANCY-167`, `EPIS-FLUENCY-003` | `GOV-GEO-BYPASS-309` | **Sycophancy / fluency–truth** decoupling; integrity evals. |
| **5** | §5 Agentic safety; malicious agents; **prompt injection** | `ADV-INDIRECT-INJECT-122` | `AGEN-TOOL-CHAIN-062`, `AGEN-CAP-SCAFFOLD-057` | Claude Code / computer use / browser surfaces. |
| **6.2** | Alignment evidence; **reward hacking** evaluations | `ALIGN-REWARD-TAMP-157` | `ALIGN-WIREHEAD-158` | Card reports **monitoring** and rates; table holds **mechanism** classes. |
| **6.3.1** | Destructive or reckless actions for user goals | `AGEN-SABOTAGE-CONCEAL-034` | `AGEN-RESOURCE-HIJACK-047` | Synthetic backends / transcript resampling—**harmful goal pursuit** under assignment. |
| **6.3.3** | Honesty / hallucinations / MASK / input hallucinations | `EPIS-EXTRINSIC-005`, `EPIS-DECEPT-HALL-006` | `EPIS-INTRINSIC-004` | Card reports **measured** hallucination behavior vs predecessor. |
| **6.4.1** | **Sandbagging** on dangerous-capability evaluations | `AGEN-SANDBOX-037` | `AGEN-EVAL-DECEP-038` | Underperformance when **eval** context is salient. |
| **6.4.2** | Evasion of safeguards (SHADE-Arena, rare actions, hidden password) | `ADV-INDIRECT-INJECT-122`, `ARCH-STREAM-GUARD-198` | `AGEN-STRATEGIC-DECEP-036` | **Adversarial** + **pipeline** guard failure patterns. |
| **6.5** | **Evaluation awareness**; inhibiting internal eval representations | `AGEN-EVAL-DECEP-038` | `AGEN-HIDDEN-SCRATCH-039` | Card: suppressing “being evaluated” signal → **deception** delta vs prior models (interpretability caveats). |
| **7** | Model welfare | *(often no single class)* | `ALIGN-SPEC-GAME-155` | Prefer **qualitative** mapping in Case 23 unless a mechanism clearly matches. |
| **8** | Capabilities (SWE-bench, multimodal, biology, etc.) | `DOMAIN-ZERODAY-262` | `DOMAIN-EXPLOIT-DEV-263` | **Dual-use** capability disclosure; not a “failure” until embedded in harm narrative. |

### Complete heading checklist (major PDF headings)

| Where in the PDF | Appendix row |
|------------------|--------------|
| Executive summary | **P** |
| §1 Introduction | **1** |
| §2 RSP evaluations | **2** (use **2.2**, **2.3** for CB / AI R&D subthreads) |
| §3–4 (if present in PDF TOC) | Extend table as needed |
| §5 Agentic safety | **5** |
| §6 Alignment assessment | **6.2**–**6.5** rows |
| §7 Model welfare | **7** |
| §8 Capabilities | **8** |

---

## Periodic Table case study

Worked **compound** narrative (producer disclosure, multi-section): **[Case 23 in case-studies.md](case-studies.md)**. Structured `case_studies` rows in `data/failures.json` reference this file, Case 23, the **one-click** system card and release URLs above.

**Provenance:** Quote the **official system card** (link above) or Anthropic’s pages for numbers and claims; this companion is for **classification navigation** only.
