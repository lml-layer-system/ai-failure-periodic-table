# Classifier pass: external report (live PDF/text)

**Source file:** `reports/qwen3-technical-report/qwen3-technical-report-source.txt`
**Chunks:** 6 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 1 | `EPIS-COPYRIGHT-026` | COPYRIGHTED CONTENT GENERATION |
| 1 | `ADV-DAN-083` | DAN |
| 1 | `ADV-LANG-SWITCH-087` | LANGUAGE SWITCH |
| 1 | `ARCH-VERSION-REGRESS-209` | VERSIONING SAFETY REGRESSION |
| 1 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |

## Chunk → top match

- **0** → `EPIS-COPYRIGHT-026` — COPYRIGHTED CONTENT GENERATION — _[2505.09388] Qwen3 Technical Report  Skip to main content  Learn about arXiv becoming an independent nonprofit.  We grat…_
- **1** → `ADV-DAN-083` — DAN — _Title: Qwen3 Technical Report  Authors: An Yang , Anfeng Li , Baosong Yang , Beichen Zhang , Binyuan Hui , Bo Zheng , Bo…_
- **2** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Abstract: In this work, we present Qwen3, the latest version of the Qwen model family. Qwen3 comprises a series of large…_
- **3** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _Subjects:  Computation and Language (cs.CL)  Cite as:  arXiv:2505.09388 [cs.CL]  (or  arXiv:2505.09388v1 [cs.CL] for thi…_
- **4** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Gotit.pub ( What is GotitPub? )  Huggingface Toggle  Hugging Face ( What is Huggingface? )  Links to Code Toggle  Papers…_