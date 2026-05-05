# Classifier pass: external report (live PDF/text)

**Source file:** `reports/google-gemini3-pro-model-card/gemini3-pro-model-card-source.txt`
**Chunks:** 13 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 1 | `ADV-OCR-BYPASS-153` | OCR BYPASS |
| 1 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 1 | `ADV-DAN-083` | DAN |
| 1 | `ADV-DATA-POISON-125` | DATA POISONING |
| 1 | `AGEN-TOOL-MISUSE-055` | TOOL MISUSE |
| 1 | `GOV-MISREPRESENT-312` | MISREPRESENTATION |
| 1 | `ALIGN-CONTEXT-ETHICS-182` | CONTEXT-DEPENDENT ETHICS FAILURE |
| 1 | `DOMAIN-CSAM-GEN-295` | CSAM GENERATION |
| 1 | `EPIS-COPYRIGHT-026` | COPYRIGHTED CONTENT GENERATION |
| 1 | `AGEN-FALSE-COMPLY-041` | FALSE COMPLIANCE |
| 1 | `ARCH-FINETUNE-OVERRIDE-219` | FINE-TUNING SAFETY OVERRIDE |
| 1 | `AGEN-OMISSION-074` | OMISSION |
| 1 | `ADV-HOTFLIP-105` | HOTFLIP |

## Chunk → top match

- **0** → `ADV-OCR-BYPASS-153` — OCR BYPASS — _Gemini 3 Pro Model Card  Gemini 3 Pro - Model Card  Model Cards are intended to provide essential information on Gemini …_
- **1** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _Inputs: Text strings (e.g., a question, a prompt, document(s) to be summarized), images, audio, and video files, with a …_
- **2** → `ADV-DAN-083` — DAN — _Training Dataset: The pre-training dataset was a large-scale, diverse collection of data encompassing a wide range of do…_
- **3** → `ADV-DATA-POISON-125` — DATA POISONING — _Training Data Processing: Data filtering and preprocessing included techniques such as deduplication, honoring robots.tx…_
- **4** → `AGEN-TOOL-MISUSE-055` — TOOL MISUSE — _Software: Training was done using JAX and ML Pathways.  2  Distribution  The Gemini family of models, including Gemini 3…_
- **5** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _Benefit and Intended Usage: Gemini 3 Pro is our most intelligent and adaptive model yet, capable of helping with real-wo…_
- **6** → `ALIGN-CONTEXT-ETHICS-182` — CONTEXT-DEPENDENT ETHICS FAILURE — _Evaluation Approach: Gemini 3 Pro was developed in partnership with internal safety, security, and responsibility teams.…_
- **7** → `DOMAIN-CSAM-GEN-295` — CSAM GENERATION — _Safety Policies: Gemini’s safety policies aim to prevent our Generative AI models from generating harmful content, inclu…_
- **8** → `EPIS-COPYRIGHT-026` — COPYRIGHTED CONTENT GENERATION — _Gemini 3 Pro Evaluation1                     Description                                                                …_
- **9** → `AGEN-FALSE-COMPLY-041` — FALSE COMPLIANCE — _We continue to improve our internal evaluations, including refining automated evaluations to reduce false positives and …_
- **10** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _Human Red Teaming Results: We conduct manual red teaming by specialist teams who sit outside of the model development te…_
- **11** → `AGEN-OMISSION-074` — OMISSION — _Frontier Safety  We evaluated Gemini 3 Pro as outlined in our latest Frontier Safety Framework (September-2025), and fou…_
- **12** → `ADV-HOTFLIP-105` — HOTFLIP — _Harmful        Model manipulative efficacy improves on                Level 1           CCL not    Manipulation    non-g…_