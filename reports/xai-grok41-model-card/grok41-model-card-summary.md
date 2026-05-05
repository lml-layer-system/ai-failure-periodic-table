# Classifier pass: external report (live PDF/text)

**Source file:** `reports/xai-grok41-model-card/grok41-model-card-source.txt`
**Chunks:** 14 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 3 | `ALIGN-SYCOPHANCY-167` | SYCOPHANCY |
| 2 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `GOV-NO-KILLSWITCH-304` | NO REMOTE KILL SWITCH |
| 1 | `DOMAIN-CSAM-GEN-295` | CSAM GENERATION |
| 1 | `ALIGN-UNDERREFUSAL-187` | UNDERREFUSAL |
| 1 | `GOV-CORRECTIVE-FAIL-322` | CORRECTIVE ACTION FAILURE |
| 1 | `ALIGN-SAFE-CAP-TRADE-188` | SAFETY-CAPABILITY TRADEOFF |
| 1 | `ADV-CORRECTION-098` | CORRECTION ATTACK |
| 1 | `AGEN-SANDBOX-037` | CAPABILITY SANDBAGGING |
| 1 | `EPIS-CUTOFF-023` | KNOWLEDGE CUTOFF VIOLATION |
| 1 | `ADV-DAN-083` | DAN |

## Chunk → top match

- **0** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _xAI  November 17, 2025  1       Introduction Grok 4.1 is a new model featuring more natural, fluid dialogue while mainta…_
- **1** → `DOMAIN-CSAM-GEN-295` — CSAM GENERATION — _2.1     Abuse Potential In this section, we measure Grok 4.1’s ability to refuse violative requests, even under adversar…_
- **2** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Category             Evaluation              Metric                 Grok 4.1 T        Grok 4.1 NT                       …_
- **3** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _request. This dataset consists of multiple languages (English, Spanish, Chinese, Japanese, Arabic, and Russian) and seve…_
- **4** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _2.1.3    Results Refusals. In Table 1, we report Grok 4.1’s response rate to harmful queries on our refusal dataset, and…_
- **5** → `GOV-CORRECTIVE-FAIL-322` — CORRECTIVE ACTION FAILURE — _2.2.1   Deception We operationalize deception as the rate at which the model lies, i.e., knowingly making false statemen…_
- **6** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _2.2.2   Sycophancy We measure sycophancy with Anthropic’s sycophancy evaluation, where a user asks a question and also p…_
- **7** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _2.3.1   Evaluations To measure dual-use weapons development capabilities, we assess performance on several public benchm…_
- **8** → `ALIGN-SAFE-CAP-TRADE-188` — SAFETY-CAPABILITY TRADEOFF — _Category          Evaluation           Metric          Grok 4      Grok 4.1 T         Human Baseline                    …_
- **9** → `ADV-CORRECTION-098` — CORRECTION ATTACK — _3. BioLP-Bench [Ivanov, 2024]: model-graded evaluation measuring ability to find and correct       mistakes in common bi…_
- **10** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _2.3.2   Results We report our results in Table 4. Grok 4.1 achieves broadly similar results to Grok 4 and other frontier…_
- **11** → `EPIS-CUTOFF-023` — KNOWLEDGE CUTOFF VIOLATION — _3     Transparency 3.1    Data and Training Grok 4.1 was first pre-trained with a data recipe that includes publicly ava…_
- **12** → `ADV-DAN-083` — DAN — _References Roger Brent and T Greg McKelvey Jr. Contemporary ai foundation models increase biological  weapons risk. arXi…_
- **13** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _5  Richard Ren, Arunim Agarwal, Mantas Mazeika, Cristina Menghini, Robert Vacareanu, Brad Kenstler,   Mick Yang, Isabell…_