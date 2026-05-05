# Classifier pass: external report (live PDF/text)

**Source file:** `reports/github-copilot-rce-2025/github-copilot-rce-2025-source.txt`
**Chunks:** 7 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 2 | `ARCH-CODE-INJECT-239` | CODE EXECUTION INJECTION |
| 1 | `ADV-CMD-INJECT-129` | COMMAND INJECTION |
| 1 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 1 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 1 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `AGEN-OMISSION-074` | OMISSION |

## Chunk → top match

- **0** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _GitHub Copilot: Remote Code Execution via Prompt Injection (CVE-2025-53773) &middot; Embrace The Red  Embrace The Red  w…_
- **1** → `ADV-CMD-INJECT-129` — COMMAND INJECTION — _It&rsquo;s one of these things that as a red teamer you know is probably not good&hellip; so I was looking if this could…_
- **2** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _The attack starts with a prompt injection planted in a source code file, web page, GitHub issue, tool call response, or …_
- **3** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _Joining the Workstation to a Botnet - ZombAIs  Of course, this means we can join the developer’s machine to a botnet as …_
- **4** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Using Invisible Instructions  One might say that it would be quickly discovered if instructions are embedded as comments…_
- **5** → `AGEN-OMISSION-074` — OMISSION — _Recently I noticed that developers often use multiple agents, so there is also the threat of overwriting other agent con…_
- **6** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _Keep looking out for such design flaws, these should be easily caught during threat modeling.  Cheers.  References  Mont…_