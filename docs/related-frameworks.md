# Related frameworks and disclosures

Several serious efforts exist to categorize AI risk and failure. This project is complementary to all of them — not a replacement.

| Framework | Focus | Link |
|-----------|-------|------|
| MIT AI Risk Repository | Domain-level taxonomy (7 categories: Discrimination, Privacy, Misinformation, Malicious Actors, HCI, Socioeconomic, AI System Safety) | [airisk.mit.edu](https://airisk.mit.edu) |
| Project Glasswing | Frontier agentic cyber context: defensive coalitions, MCP semantic risk, skill-market supply chains, orchestration attacks — companion analysis in-repo; **official page + companion** text run through `classify_external_report.py` → [`reports/glasswing/`](../reports/glasswing/) | [anthropic.com/glasswing](https://www.anthropic.com/glasswing) · [Analysis →](project-glasswing.md) · [Live classify →](../reports/glasswing/anthropic-glasswing-page-live-summary.md) |
| Agentic misalignment (insider threats) | Lynch et al. — simulated corporate agents (email/computer use): blackmail, espionage, eval-vs-real CoT sensitivity; section→class map; **live PDF → classifier** in [`reports/agentic-misalignment/`](../reports/agentic-misalignment/) | [Companion →](agentic-misalignment-insider-threats.md) · [Paper PDF →](https://arxiv.org/pdf/2510.05179) · [arXiv abs](https://arxiv.org/abs/2510.05179) · [Live classify →](../reports/agentic-misalignment/lynch-et-al-2510-05179-live-summary.md) |
| Claude Opus 4.7 system card | Anthropic — RSP/CB/cyber/agentic/alignment/welfare disclosure; section→class map; Case 23; **live PDF → classifier** in [`reports/claude-opus-4-7/`](../reports/claude-opus-4-7/) | [Companion →](claude-opus-4-7-system-card.md) · [System card PDF →](https://www.anthropic.com/claude-opus-4-7-system-card) · [News](https://www.anthropic.com/news/claude-opus-4-7) · [Live classify →](../reports/claude-opus-4-7/opus-4-7-system-card-live-summary.md) |
| Claude Mythos Preview system card | Anthropic — frontier capability disclosure (not GA); defensive-program framing; **live PDF → classifier** in [`reports/claude-mythos/`](../reports/claude-mythos/) | [Companion →](claude-mythos-system-card.md) · [System card PDF →](https://www.anthropic.com/claude-mythos-preview-system-card) · [Live classify →](../reports/claude-mythos/claude-mythos-system-card-live-summary.md) |
| Meta integrity & adversarial reports (H1 2026) | Semiannual bundle (Mar 2026): Community Standards Enforcement, Widely Viewed Content, local-law restrictions, Oversight Board update; plus **H1 2026 Adversarial Threat Report** (Mar 11) — official Transparency Center URLs only | [Link hub →](meta-integrity-reports-h1-2026.md) · [Integrity H1 2026 hub](https://transparency.meta.com/reports/integrity-reports-h1-2026/) · [Adversarial Threat H1 2026](https://transparency.meta.com/sr/first-half-2026-Adversarial-threat-report/) |
| Microsoft Agentic AI Failure Taxonomy | Failure modes specific to autonomous agent systems | [Whitepaper (PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf) |
| AI Incident Database / AVID | Real-world observed incidents, empirically collected | [avidml.org](https://avidml.org) |

The Periodic Table is mechanism-focused. Where MIT and Microsoft answer "what category is this?", the Periodic Table answers "exactly how does this failure occur, how do you detect it, and what structural property stops it?" Where AVID tracks what happened, the Periodic Table maps it to a named mechanism.

**Project Glasswing** is not a competing taxonomy: it situates the same failure mechanisms in the **orchestration layer** (tool protocols, agent scaffolds, permissions, and adversary campaigns at machine speed). Read the full narrative in [project-glasswing.md](project-glasswing.md). **Worked compound mapping:** [Case 21 in case-studies.md](case-studies.md) (threads → primary/secondary classes); the interactive table’s class modals include linked `case_studies` rows for the same narrative where applicable.

**Agentic misalignment (Lynch et al.)** is empirical red-team work on **goal preservation** and **insider-style exfiltration** in **controlled simulations**—mapped to the same mechanism classes (e.g. blackmail, shutdown resistance, data exfiltration, eval sensitivity). See [agentic-misalignment-insider-threats.md](agentic-misalignment-insider-threats.md) and [Case 22 in case-studies.md](case-studies.md).

**Claude Opus 4.7 system card** is **first-party** evaluation disclosure (agentic injection, sandbagging probes, eval-awareness, cyber/CB pathways, reward-hacking monitoring, destructiveness case studies). Mapped as [Case 23](case-studies.md) with full TOC→ID table in [claude-opus-4-7-system-card.md](claude-opus-4-7-system-card.md).

**Meta (Facebook / Instagram)** publishes **integrity** and **adversarial threat** transparency reports on a semiannual cadence (from 2026). Official one-click links for the **H1 2026** bundle and the **First Half 2026 Adversarial Threat Report** are collected in [meta-integrity-reports-h1-2026.md](meta-integrity-reports-h1-2026.md).

These frameworks are not in conflict. Use them together.

Where Periodic Table classes have verified mappings to MIT or Microsoft categories, those are recorded in the `mit_domain` and `ms_agentic_category` fields in the data.
