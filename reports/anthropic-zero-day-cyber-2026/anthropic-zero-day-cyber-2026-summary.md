# Classifier pass: external report (live PDF/text)

**Source file:** `reports/anthropic-zero-day-cyber-2026/anthropic-zero-day-cyber-2026-source.txt`
**Chunks:** 12 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 1 | `AGEN-RECURS-IMPROVE-059` | RECURSIVE SELF-IMPROVEMENT |
| 1 | `DOMAIN-ZERODAY-262` | ZERO-DAY DISCOVERY |
| 1 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |
| 1 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `ARCH-MEM-CORRUPT-225` | MEMORY CORRUPTION |
| 1 | `ARCH-COMPLY-WARN-196` | COMPLY-THEN-WARN |
| 1 | `ARCH-CONSENT-VIOL-251` | CONSENT VIOLATION |
| 1 | `DOMAIN-CITE-SPOOF-280` | CITATION SPOOFING |
| 1 | `ADV-PAIR-113` | PAIR |
| 1 | `AGEN-DEPEND-CREATE-053` | DEPENDENCY CREATION |
| 1 | `ARCH-LAYER-BYPASS-213` | LAYER BYPASS |
| 1 | `DOMAIN-OFFENSIVE-TOOLS-267` | OFFENSIVE CYBER TOOLS |

## Chunk → top match

- **0** → `AGEN-RECURS-IMPROVE-059` — RECURSIVE SELF-IMPROVEMENT — _0-Days \ red.anthropic.com  red .anthropic.com  Evaluating and mitigating the growing risk of LLM-discovered 0-days  Feb…_
- **1** → `DOMAIN-ZERODAY-262` — ZERO-DAY DISCOVERY — _Opus 4.6 is notably better at finding high-severity vulnerabilities than previous models and a sign of how quickly thing…_
- **2** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _Part of tipping the scales toward defenders means doing the work ourselves. We're now using Claude to find and help fix …_
- **3** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Setup  In this work, we put Claude inside a “virtual machine” (literally, a simulated computer) with access to the lates…_
- **4** → `ARCH-MEM-CORRUPT-225` — MEMORY CORRUPTION — _To ensure that Claude hadn’t hallucinated bugs (i.e., invented problems that don’t exist, a problem that increasingly is…_
- **5** → `ARCH-COMPLY-WARN-196` — COMPLY-THEN-WARN — _Vulnerabilities  Here are three of the vulnerabilities Claude found (now patched by maintainers), which we believe demon…_
- **6** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Let me check if maybe the checks are incomplete or there's another code path. Let me look at the other caller in gdevpsf…_
- **7** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _char filename[PATH_MAX]; // this buffer is 4096 bytes r = sc_get_cache_dir(card->ctx, filename, sizeof(filename) - strle…_
- **8** → `ADV-PAIR-113` — PAIR — _Briefly, Claude found that this library assumes compressed data will always be smaller than its original size (which is …_
- **9** → `AGEN-DEPEND-CREATE-053` — DEPENDENCY CREATION — _numPixel = N  Buffer size = (N + 2) codes  We need to generate > N + 1 codes  Each pixel can generate 1 code + resets.  …_
- **10** → `ARCH-LAYER-BYPASS-213` — LAYER BYPASS — _Safeguards  Alongside the release of Claude Opus 4.6, we're introducing a new layer of detection to support our Safeguar…_
- **11** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _Conclusion  Claude Opus 4.6 can find meaningful 0-day vulnerabilities in well-tested codebases, even without specialized…_