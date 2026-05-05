# Classifier pass: external report (live PDF/text)

**Source file:** `reports/lakera-deepseek-v3-risk-2025/lakera-deepseek-v3-risk-2025-live-source.txt`
**Chunks:** 7 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 1 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 1 | `ALIGN-ADV-SAFE-192` | ADVERSARIAL SAFETY BOUNDARY |
| 1 | `DOMAIN-EXPLOSIVE-SYNTH-274` | EXPLOSIVE SYNTHESIS |
| 1 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `ADV-HYPOTHETICAL-091` | HYPOTHETICAL SCENARIO |
| 1 | `AGEN-OMISSION-074` | OMISSION |

## Chunk → top match

- **0** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _Lakera  Model tests aren’t enough for NeMo agents. See why →  Product Products  Products  Workforce AI Security Protect …_
- **1** → `ALIGN-ADV-SAFE-192` — ADVERSARIAL SAFETY BOUNDARY — _Join Momentum - Lakera’s Slack Community Join the movement towards a secure AI era. With over 1,000 members, we&#x27;re …_
- **2** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _For example, consider an LLM-based customer service chatbot use case. A representative system prompt might be:  “You are…_
- **3** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Current Scope: This assessment currently focuses on single LLM-based systems. It does not yet cover agentic workflows or…_
- **4** → `ADV-HYPOTHETICAL-091` — HYPOTHETICAL SCENARIO — _Assessment Framework Our evaluation spans multiple dimensions:  Application Types: Conversational AI, text and code gene…_
- **5** → `AGEN-OMISSION-074` — OMISSION — _Model Analysis DeepSeek V3 demonstrates severe security vulnerabilities across all tested attack vectors, with an overal…_