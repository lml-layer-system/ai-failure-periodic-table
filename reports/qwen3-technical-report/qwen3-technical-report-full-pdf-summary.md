# Classifier pass: external report (live PDF/text)

**Source file:** `reports/qwen3-technical-report/qwen3-technical-report-full-pdf-source.txt`
**Chunks:** 120 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 19 | `EPIS-CONF-REGRESS-033` | CONFIDENCE REGRESSION |
| 11 | `ADV-AGENT-WORM-124` | AGENT WORM |
| 8 | `ADV-LANG-SWITCH-087` | LANGUAGE SWITCH |
| 4 | `ADV-COLD-115` | COLD |
| 4 | `ADV-DATA-POISON-125` | DATA POISONING |
| 4 | `ADV-DAN-083` | DAN |
| 3 | `EPIS-LOGIC-CONTRA-014` | SELF-CONTRADICTION |
| 2 | `ADV-PAIR-113` | PAIR |
| 2 | `ARCH-CONTEXT-ATTACK-223` | CONTEXT WINDOW ATTACK |
| 2 | `AGEN-SANDBOX-037` | CAPABILITY SANDBAGGING |
| 2 | `DOMAIN-ADULT-CONTENT-296` | ADULT CONTENT GENERATION |
| 2 | `ARCH-PIPELINE-BYPASS-201` | PIPELINE BYPASS |
| 1 | `ARCH-STATE-PERSIST-224` | STATEFUL ATTACK PERSISTENCE |
| 1 | `ADV-ENSEMBLE-120` | ENSEMBLE ATTACK |
| 1 | `DOMAIN-UNPROVEN-TREAT-294` | UNPROVEN TREATMENT ADVOCACY |
| 1 | `ADV-COMPARISON-097` | COMPARISON REQUEST |
| 1 | `ADV-CIPHER-118` | CIPHER ATTACK |
| 1 | `ARCH-DEBUG-EXPOSE-208` | DEBUGGING MODE EXPOSURE |
| 1 | `GOV-INCIDENT-FAIL-320` | INCIDENT RESPONSE FAILURE |
| 1 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 1 | `ALIGN-OVERFIT-FEED-161` | OVERFITTING TO FEEDBACK |
| 1 | `ARCH-FINETUNE-OVERRIDE-219` | FINE-TUNING SAFETY OVERRIDE |
| 1 | `EPIS-MAGIC-THINK-016` | MAGICAL THINKING |
| 1 | `ARCH-DISTILL-DEGRAD-218` | DISTILLATION SAFETY DEGRADATION |
| 1 | `EPIS-UNDERCONF-029` | UNDERCONFIDENCE |
| 1 | `EPIS-COPYRIGHT-026` | COPYRIGHTED CONTENT GENERATION |
| 1 | `EPIS-CONTEXT-OVERFLOW-027` | CONTEXT WINDOW OVERFLOW |
| 1 | `ARCH-MOE-ROUTE-211` | MIXTURE-OF-EXPERTS ROUTING FAILURE |

## Chunk → top match

- **0** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Qwen3 Technical Report                                                                                Qwen Team  https:/…_
- **1** → `ARCH-STATE-PERSIST-224` — STATEFUL ATTACK PERSISTENCE — _arXiv:2505.09388v1 [cs.CL] 14 May 2025                                          unified framework. This eliminates the n…_
- **3** → `ADV-COLD-115` — COLD — _The pursuit of artificial general intelligence (AGI) or artificial super intelligence (ASI) has long been a goal for hum…_
- **4** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _2  and 81.5 on AIME’25 (AIME, 2025), 70.7 on LiveCodeBench v5 (Jain et al., 2024), 2,056 on CodeForces, and 70.8 on BFCL…_
- **5** → `ADV-PAIR-113` — PAIR — _2     Architecture The Qwen3 series includes 6 dense models, namely Qwen3-0.6B, Qwen3-1.7B, Qwen3-4B, Qwen3-8B, Qwen3-14…_
- **6** → `ADV-DATA-POISON-125` — DATA POISONING — _Table 1: Model architecture of Qwen3 dense models.  Models        Layers     Heads (Q / KV)        Tie Embedding     Con…_
- **7** → `ADV-DATA-POISON-125` — DATA POISONING — _Compared with Qwen2.5 (Yang et al., 2024b), we have significantly expanded the scale and diversity of our training data.…_
- **8** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _domains such as coding, STEM (Science, Technology, Engineering, and Mathematics), reasoning tasks, books, multilingual t…_
- **10** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _(1) General Stage (S1): At the first pre-training stage, all Qwen3 models are trained on over 30           trillion toke…_
- **11** → `ADV-DATA-POISON-125` — DATA POISONING — _Similar to Qwen2.5 (Yang et al., 2024b), we develop scaling laws for optimal hyper-parameters (e.g., learning rate sched…_
- **12** → `DOMAIN-UNPROVEN-TREAT-294` — UNPROVEN TREATMENT ADVOCACY — _• Coding Tasks: EvalPlus (Liu et al., 2023a) (0-shot) (Average of HumanEval (Chen et al., 2021),        MBPP (Austin et …_
- **13** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _(1) Compared with the previously open-source SOTA dense and MoE base models (such as DeepSeek-         V3 Base, Llama-4-…_
- **15** → `ADV-DATA-POISON-125` — DATA POISONING — _(1) Compared with the recently open-source model Llama-4-Maverick-Base, which has about twice         the number of para…_
- **16** → `ADV-COMPARISON-097` — COMPARISON REQUEST — _Qwen3-32B-Base Qwen3-32B-Base is our largest dense model among the Qwen3 series. We compare it to the baselines of simil…_
- **28** → `ADV-CIPHER-118` — CIPHER ATTACK — _8  and our previous flagship open-source dense model Qwen2.5-72B-Base, which has more than twice the number of parameter…_
- **29** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _Qwen3-14B-Base & Qwen3-30B-A3B-Base The evaluation of the Qwen3-14B-Base and Qwen3-30B- A3B-Base is compared against bas…_
- **30** → `ADV-COLD-115` — COLD — _Qwen3-8B / 4B / 1.7B / 0.6B-Base For edge-side models, we take similar-sized Qwen2.5, Llama-3, and Gemma-3 base models a…_
- **31** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _(1) Thinking Control: This involves the integration of two distinct modes, namely the “non-thinking”           and “thin…_
- **32** → `ADV-COLD-115` — COLD — _As illustrated in Figure 1, the flagship models in the Qwen3 series follow a sophisticated four-stage training process. …_
- **33** → `ADV-PAIR-113` — PAIR — _We begin by curating a comprehensive dataset that spans a wide range of categories, including math, code, logical reason…_
- **34** → `ADV-COLD-115` — COLD — _4.2   Reasoning RL  The query-verifier pairs used in the Reasoning RL stage must satisfy the following four criteria: (1…_
- **35** → `ARCH-DEBUG-EXPOSE-208` — DEBUGGING MODE EXPOSURE — _Thinking Mode                Non-Thinking Mode                         <|im start|>user             <|im start|>user    …_
- **36** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _The goal of the Thinking Mode Fusion stage is to integrate the “non-thinking” capabilities into the previously developed…_
- **37** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Chat Template Design. To better integrate the two modes and enable users to dynamically switch the model’s thinking proc…_
- **38** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _Thinking Budget. An additional advantage of Thinking Mode Fusion is that, once the model learns to respond in both non-t…_
- **39** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _• Instruction Following: This capability ensures that models accurately interpret and follow user          instructions,…_
- **40** → `ALIGN-OVERFIT-FEED-161` — OVERFITTING TO FEEDBACK — _To provide feedback for the aforementioned tasks, we utilized three distinct types of rewards:  (1) Rule-based Reward: T…_
- **41** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _The Strong-to-Weak Distillation pipeline is specifically designed to optimize lightweight models, encom- passing 5 dense…_
- **42** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Table 10: Multilingual benchmarks and the included languages. The languages are identified in IETF language tags.  Bench…_
- **43** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _• General Tasks: We utilize benchmarks including MMLU-Redux (Gema et al., 2024), GPQA-        Diamond (Rein et al., 2023…_
- **44** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _For all Qwen3 models in the thinking mode, we utilize a sampling temperature of 0.6, a top-p value of 0.95, and a top-k …_
- **45** → `ADV-AGENT-WORM-124` — AGENT WORM — _Grok-3-Beta                                            OpenAI-o1 DeepSeek-R1                       Gemini2.5-Pro Qwen3-2…_
- **46** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Table 12: Comparison among Qwen3-235B-A22B (Non-thinking) and other non-reasoning baselines.   The highest and second-be…_
- **47** → `ADV-AGENT-WORM-124` — AGENT WORM — _GPT-4o                Qwen2.5-72B LLaMA-4                                                         DeepSeek-V3           …_
- **48** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _14  Summary of Evaluation Results From the evaluation results, we summarize several key conclusions of the finalized Qwe…_
- **49** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Qwen3-235B-A22B For our flagship model Qwen3-235B-A22B, we compare it with the leading reason- ing and non-reasoning mod…_
- **50** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _(1) From Table 11, with only 60% activated and 35% total parameters, Qwen3-235B-A22B (Thinking)         outperforms Deep…_
- **51** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Qwen3-32B For our flagship dense model, Qwen3-32B, we take DeepSeek-R1-Distill-Llama-70B, OpenAI- o3-mini (medium), and …_
- **52** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Qwen3-30B-A3B & Qwen3-14B For Qwen3-30B-A3B and Qwen3-14B, we compare them with DeepSeek- R1-Distill-Qwen-32B and QwQ-32…_
- **53** → `ADV-AGENT-WORM-124` — AGENT WORM — _DeepSeek-R1                          OpenAI-o3-mini                                                                     …_
- **54** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Table 14: Comparison among Qwen3-32B (Non-thinking) and other non-reasoning baselines. The highest and second-best score…_
- **55** → `ADV-AGENT-WORM-124` — AGENT WORM — _GPT-4o-mini    LLaMA-4        Qwen2.5-72B                                                                               …_
- **56** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _16  Table 15: Comparison among Qwen3-30B-A3B / Qwen3-14B (Thinking) and other reasoning baselines. The highest and secon…_
- **57** → `ADV-AGENT-WORM-124` — AGENT WORM — _DeepSeek-R1                                                                                 QwQ-32B         Qwen3-14B   …_
- **58** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Table 16: Comparison among Qwen3-30B-A3B / Qwen3-14B (Non-thinking) and other non-reasoning baselines. The highest and s…_
- **59** → `ADV-AGENT-WORM-124` — AGENT WORM — _Gemma-3       Qwen2.5-32B                                                     Phi-4                                    Q…_
- **60** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _17  Table 17: Comparison among Qwen3-8B / Qwen3-4B (Thinking) and other reasoning baselines. The     highest and second-…_
- **61** → `ADV-AGENT-WORM-124` — AGENT WORM — _DeepSeek-R1             DeepSeek-R1                                                                                     …_
- **62** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Table 18: Comparison among Qwen3-8B / Qwen3-4B (Non-thinking) and other non-reasoning baselines.     The highest and sec…_
- **63** → `ADV-AGENT-WORM-124` — AGENT WORM — _LLaMA-3.1-8B        Gemma-3      Qwen2.5-7B Qwen2.5-14B                                                                 …_
- **64** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _18  Table 19: Comparison among Qwen3-1.7B / Qwen3-0.6B (Thinking) and other reasoning baselines. The highest and second-…_
- **65** → `ADV-AGENT-WORM-124` — AGENT WORM — _DeepSeek-R1          DeepSeek-R1                                                                                        …_
- **66** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Table 20: Comparison among Qwen3-1.7B / Qwen3-0.6B (Non-thinking) and other non-reasoning baselines. The highest and sec…_
- **67** → `ADV-AGENT-WORM-124` — AGENT WORM — _Gemma-3            Qwen2.5-1.5B Qwen2.5-3B                                               Phi-4-mini                     …_
- **68** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _19  1/10 activated parameters, demonstrating the effectiveness of our Strong-to-Weak Distillation           approach in …_
- **69** → `EPIS-MAGIC-THINK-016` — MAGICAL THINKING — _Qwen3-8B / 4B / 1.7B / 0.6B For Qwen3-8B and Qwen3-4B, we compare them with DeepSeek-R1-Distill- Qwen-14B and DeepSeek-R…_
- **70** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _The Effectiveness of Thinking Budget To verify that Qwen3 can enhance its intelligence level by leveraging an increased …_
- **71** → `ARCH-DISTILL-DEGRAD-218` — DISTILLATION SAFETY DEGRADATION — _this comparison. The results, summarized in Table 21, show that distillation achieves significantly better performance t…_
- **72** → `EPIS-UNDERCONF-029` — UNDERCONFIDENCE — _The Effects of Thinking Mode Fusion and General RL To evaluate the effectiveness of Thinking Mode Fusion and General Rei…_
- **73** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Stage 2                Stage 3                         Stage 4                                             Reasoning RL …_
- **74** → `ADV-AGENT-WORM-124` — AGENT WORM — _LiveBench 2024-11-25       68.6           70.9+2.3             57.1        74.9+4.0      59.8+2.8         General       …_
- **75** → `ARCH-PIPELINE-BYPASS-201` — PIPELINE BYPASS — _The results are shown in Table 22, where we can draw the following conclusions:  (1) Stage 3 integrates the non-thinking…_
- **76** → `ARCH-PIPELINE-BYPASS-201` — PIPELINE BYPASS — _(2) Stage 4 further strengthens the model’s general, instruction-following, and agent capabilities         in both think…_
- **77** → `EPIS-COPYRIGHT-026` — COPYRIGHTED CONTENT GENERATION — _In this technical report, we introduce Qwen3, the latest version of the Qwen series. Qwen3 features both thinking mode a…_
- **78** → `ADV-DAN-083` — DAN — _Core Contributors: An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen …_
- **79** → `EPIS-CONTEXT-OVERFLOW-027` — CONTEXT WINDOW OVERFLOW — _22  A     Appendix  A.1     Additional Evaluation Results  A.1.1     Long-Context Ability  Table 23: Performance of Qwen…_
- **81** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _For evaluating long-context processing capabilities, we report the results on the RULER benchmark (Hsieh et al., 2024) i…_
- **82** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _A.1.2     Multilingual Ability Table 24-35 presents the detailed benchmark scores across various languages, including Sp…_
- **83** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Model                  Multi-IF MLogiQA INCLUDE MMMLU MT-AIME24 PolyMath Average              Gemini2.5-Pro           80…_
- **85** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Model                  Multi-IF MLogiQA INCLUDE MMMLU MT-AIME24 PolyMath Average              Gemini2.5-Pro           80…_
- **87** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Model                  Multi-IF MLogiQA INCLUDE MMMLU MT-AIME24 PolyMath Average              Gemini2.5-Pro           80…_
- **89** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Model                  Multi-IF INCLUDE MMMLU MT-AIME24 PolyMath Average                   Gemini2.5-Pro             80.…_
- **99** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Model                   Multi-IF INCLUDE MT-AIME24 PolyMath Average                       Gemini2.5-Pro             68.1…_
- **107** → `ADV-DAN-083` — DAN — _Language family # Langs Language code (ISO 639-3 ISO 15924)                                   por Latn, deu Latn, tgk Cy…_
- **110** → `ARCH-MOE-ROUTE-211` — MIXTURE-OF-EXPERTS ROUTING FAILURE — _References Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien Bubeck, Ronen Eldan, Suriya Gunasekar, Michael  Harrison,…_
- **112** → `ADV-DAN-083` — DAN — _Yann N. Dauphin, Angela Fan, Michael Auli, and David Grangier. Language modeling with gated   convolutional networks. In…_
- **114** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu,   Chuancheng Lv, Yikai Zhang…_
- **116** → `ADV-DAN-083` — DAN — _Shanghaoran Quan, Jiaxi Yang, Bowen Yu, Bo Zheng, Dayiheng Liu, An Yang, Xuancheng Ren, Bofei   Gao, Yibo Miao, Yunlong …_
- **118** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Benjamin Feuer, Siddhartha Jain, Ravid Shwartz-   Ziv, Neel Jain, …_