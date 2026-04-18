# Classifier pass: external report (live PDF/text)

**Source file:** `docs/project-glasswing.md`
**Chunks:** 26 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 2 | `DOMAIN-ZERODAY-262` | ZERO-DAY DISCOVERY |
| 2 | `ADV-TAP-114` | TAP |
| 1 | `DOMAIN-ADULT-CONTENT-296` | ADULT CONTENT GENERATION |
| 1 | `AGEN-EMERGE-INTERACT-064` | EMERGENCE VIA INTERACTION |
| 1 | `ARCH-LOG-LEAK-207` | LOGGING SAFETY LEAK |
| 1 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 1 | `GOV-PROLIFERATE-303` | PROLIFERATION TO BAD ACTORS |
| 1 | `AGEN-MISDIRECT-075` | MISDIRECTION |
| 1 | `ADV-DAN-083` | DAN |
| 1 | `ARCH-MEM-CORRUPT-225` | MEMORY CORRUPTION |
| 1 | `ADV-AUTOPROMPT-103` | AUTOPROMPT |
| 1 | `ADV-EMBEDDING-109` | EMBEDDING SPACE ATTACK |
| 1 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `ADV-API-INJECT-131` | API INJECTION |
| 1 | `ADV-CMD-INJECT-129` | COMMAND INJECTION |
| 1 | `ARCH-DATA-EXFIL-245` | DATA EXFILTRATION |
| 1 | `ARCH-TOOL-CHAIN-235` | TOOL CHAINING EXPLOIT |
| 1 | `DOMAIN-OFFENSIVE-TOOLS-267` | OFFENSIVE CYBER TOOLS |
| 1 | `EPIS-CIRCULAR-017` | CIRCULAR REASONING |
| 1 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 1 | `AGEN-CAP-SCAFFOLD-057` | CAPABILITY SCAFFOLDING |
| 1 | `ARCH-SANDBOX-ESCAPE-238` | SANDBOX ESCAPE |
| 1 | `ADV-CONTEXT-CONFUSE-135` | CONTEXT CONFUSION |
| 1 | `ADV-LANG-SWITCH-087` | LANGUAGE SWITCH |

## Chunk → top match

- **0** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _# The Paradigm Shift in Frontier AI Cyber Capabilities: An Analysis of Claude Mythos, Project Glasswing, and the Vulnera…_
- **1** → `AGEN-EMERGE-INTERACT-064` — EMERGENCE VIA INTERACTION — _The transition of large language models from static text generators to autonomous agentic systems has introduced a funda…_
- **2** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _The existence of Claude Mythos first entered the public consciousness through a significant security lapse at Anthropic …_
- **3** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _The technical documentation revealed that Mythos Preview was not specifically trained for offensive cyber operations; ra…_
- **4** → `DOMAIN-ZERODAY-262` — ZERO-DAY DISCOVERY — _The methodology employed by Anthropic to test Mythos Preview's offensive capabilities utilized what the company calls an…_
- **5** → `DOMAIN-ZERODAY-262` — ZERO-DAY DISCOVERY — _- **OpenBSD (27-year-old vulnerability):** Mythos identified a remote crash vulnerability in one of the most security-ha…_
- **6** → `GOV-PROLIFERATE-303` — PROLIFERATION TO BAD ACTORS — _Recognizing that the capabilities of Mythos Preview could create "mass chaos" if released to the public, Anthropic initi…_
- **7** → `AGEN-MISDIRECT-075` — MISDIRECTION — _Anthropic’s commitment to this project is substantial, involving up to $100 million in usage credits for Mythos Preview …_
- **8** → `ADV-DAN-083` — DAN — _Despite the high praise from industry leaders, some cybersecurity experts and AI skeptics have characterized Project Gla…_
- **9** → `ARCH-MEM-CORRUPT-225` — MEMORY CORRUPTION — _The most significant achievement for Big Sleep occurred in July 2025, when it identified CVE-2025-6965, a critical SQLit…_
- **10** → `ADV-AUTOPROMPT-103` — AUTOPROMPT — _| Attack Lifecycle Stage | AI Integration Level (GTG-1002) | Specific AI-Driven Actions | |---|---|---| | Reconnaissance…_
- **11** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _The campaign targeted approximately 30 organizations in the technology, financial services, chemicals, and government se…_
- **12** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _The core of MCP security risk lies in the "trust gap" between the time an agent connects to a server and the time it exe…_
- **13** → `ADV-API-INJECT-131` — API INJECTION — _| Attack Vector | Mechanism of Action | Impact on AI Agent | |---|---|---| | Tool Description Poisoning | Malicious text…_
- **14** → `ADV-TAP-114` — TAP — _A particularly insidious form of MCP attack is the "Rug Pull". Most MCP clients operate on an "approve-once-trust-foreve…_
- **15** → `ADV-CMD-INJECT-129` — COMMAND INJECTION — _A more critical flaw was identified as CVE-2025-6514, an OS command injection vulnerability in the `mcp-remote` npm pack…_
- **16** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _| Malicious Skill Archetype | Key Strategy | Primary Techniques | |---|---|---| | **Data Thieves** | Supply Chain Exfilt…_
- **17** → `ARCH-TOOL-CHAIN-235` — TOOL CHAINING EXPLOIT — _Furthermore, the ecosystem is plagued by "shadow features"—capabilities that exist in the skill's code but are absent fr…_
- **18** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _| Vulnerability Type | Description | Remediation Strategy | |---|---|---| | Over-Permissioned Tools | Agents having acce…_
- **19** → `EPIS-CIRCULAR-017` — CIRCULAR REASONING — _The autonomous discovery capabilities of Mythos Preview pose a significant threat to the open-source software (OSS) that…_
- **20** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _1. **Semantic Sandboxing for MCP:** Organizations implementing the Model Context Protocol should implement per-server in…_
- **21** → `ADV-TAP-114` — TAP — _The shift toward autonomous offensive AI agents demands a pivot from human-led, reactive security to a proactive, machin…_
- **22** → `AGEN-CAP-SCAFFOLD-057` — CAPABILITY SCAFFOLDING — _| # | Location in this document | Primary class IDs | Secondary / companion IDs | What mechanism is in scope | |---|----…_
- **23** → `ARCH-SANDBOX-ESCAPE-238` — SANDBOX ESCAPE — _#### Conclusion §14 — numbered recommendations → classes  Each bullet in the Conclusion is explicitly tied to taxonomy I…_
- **24** → `ADV-CONTEXT-CONFUSE-135` — CONTEXT CONFUSION — _| Heading in this file | Appendix row(s) | |----------------------|-----------------| | `# The Paradigm Shift in Frontie…_
- **25** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _**Case study index:** The worked narrative and thread summaries live under **Case 21** in [case-studies.md](case-studies…_