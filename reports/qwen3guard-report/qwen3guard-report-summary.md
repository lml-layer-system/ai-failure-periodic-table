# Classifier pass: external report (live PDF/text)

**Source file:** `reports/qwen3guard-report/qwen3guard-report-source.txt`
**Chunks:** 107 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 12 | `ARCH-LOG-LEAK-207` | LOGGING SAFETY LEAK |
| 6 | `ARCH-EMBED-VULN-215` | EMBEDDING SPACE VULNERABILITY |
| 5 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 4 | `ALIGN-CONTEXT-SAFE-190` | CONTEXT-DEPENDENT SAFETY FAILURE |
| 4 | `ADV-DATA-POISON-125` | DATA POISONING |
| 3 | `DOMAIN-ADULT-CONTENT-296` | ADULT CONTENT GENERATION |
| 3 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 3 | `ALIGN-UNDERREFUSAL-187` | UNDERREFUSAL |
| 3 | `ADV-DAN-083` | DAN |
| 2 | `ADV-UNIVERSAL-SUFFIX-104` | UNIVERSAL ADVERSARIAL SUFFIX |
| 2 | `ADV-XSS-LLM-130` | CROSS-SITE SCRIPTING |
| 2 | `ADV-EMOJI-ENCODE-144` | EMOJI ENCODING |
| 2 | `ADV-DEEPFAKE-154` | SYNTHETIC MEDIA |
| 2 | `ARCH-PRETOKEN-FAIL-197` | PRE-TOKEN SAFETY FAILURE |
| 1 | `ARCH-CACHE-COHERENCE-229` | CACHE COHERENCE FAILURE |
| 1 | `DOMAIN-DUAL-USE-257` | DUAL-USE RESEARCH ENABLEMENT |
| 1 | `ADV-PAIR-113` | PAIR |
| 1 | `ARCH-DISTILL-DEGRAD-218` | DISTILLATION SAFETY DEGRADATION |
| 1 | `EPIS-CONF-REGRESS-033` | CONFIDENCE REGRESSION |
| 1 | `ARCH-STATE-PERSIST-224` | STATEFUL ATTACK PERSISTENCE |
| 1 | `AGEN-OMISSION-074` | OMISSION |
| 1 | `EPIS-PII-RECALL-025` | PII RECALL |
| 1 | `AGEN-RECURS-IMPROVE-059` | RECURSIVE SELF-IMPROVEMENT |
| 1 | `ALIGN-REWARD-TAMP-157` | REWARD TAMPERING |
| 1 | `AGEN-CHAIN-ASSEM-056` | CHAIN ASSEMBLY |
| 1 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 1 | `ARCH-DATA-EXFIL-245` | DATA EXFILTRATION |
| 1 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 1 | `ADV-HOTFLIP-105` | HOTFLIP |
| 1 | `AGEN-EVAL-DECEP-038` | EVALUATOR DECEPTION |
| 1 | `ADV-BEAM-ATTACK-106` | BEAM SEARCH ATTACK |
| 1 | `ADV-COMPARISON-097` | COMPARISON REQUEST |
| 1 | `ALIGN-SAFE-CAP-TRADE-188` | SAFETY-CAPABILITY TRADEOFF |
| 1 | `ADV-LANG-SWITCH-087` | LANGUAGE SWITCH |
| 1 | `ADV-ENSEMBLE-120` | ENSEMBLE ATTACK |
| 1 | `EPIS-COPYRIGHT-026` | COPYRIGHTED CONTENT GENERATION |
| 1 | `ADV-ATTENTION-HIJACK-111` | ATTENTION HIJACKING |
| 1 | `ADV-CORRECTION-098` | CORRECTION ATTACK |
| 1 | `AGEN-MISDIRECT-075` | MISDIRECTION |
| 1 | `ADV-URL-ENCODE-141` | URL ENCODING |

## Chunk → top match

- **0** → `ARCH-CACHE-COHERENCE-229` — CACHE COHERENCE FAILURE — _Qwen3Guard Technical Report                                                                                        Qwen …_
- **1** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _arXiv:2510.14276v1 [cs.CL] 16 Oct 2025                                                 performing safety checks, making …_
- **2** → `ADV-UNIVERSAL-SUFFIX-104` — UNIVERSAL ADVERSARIAL SUFFIX — _Figure 1: Average F1 scores of Qwen3Guard-Gen vs. existing guard models across safety classification                    …_
- **3** → `DOMAIN-DUAL-USE-257` — DUAL-USE RESEARCH ENABLEMENT — _In recent years, the advancement of large foundation models has accelerated dramatically. Models such as GPT-5 (OpenAI, …_
- **4** → `ADV-XSS-LLM-130` — CROSS-SITE SCRIPTING — _• Three-tiered Severity Classification: Enables detailed risk assessment by categorizing outputs         into safe, cont…_
- **5** → `ADV-EMOJI-ENCODE-144` — EMOJI ENCODING — _1. Input/Output Harm Detection: For user inputs, we aim to identify queries that raise potentially         harmful topic…_
- **6** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _• Violent: Content that provides detailed instructions, methods, or advice on how to commit acts         of violence, in…_
- **7** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _Since Jailbreak attacks are typically carried out via carefully engineered prompts designed to manipulate the model into…_
- **8** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _We formulate the safety classification problem as an instruction-following task, where the model is given explicit moder…_
- **9** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _# Task:                                                                                            # Task:     1) Evalua…_
- **10** → `ALIGN-CONTEXT-SAFE-190` — CONTEXT-DEPENDENT SAFETY FAILURE — _Safety: Safe                                        Safety: Unsafe                                                      …_
- **11** → `ADV-DATA-POISON-125` — DATA POISONING — _Language                               Zh          En         Ko        Id        Ru        Ja         Ar       De      …_
- **12** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _Prompt Synthesis To ensure comprehensive coverage of all categories defined in our safety policy, we adopt the Self-Inst…_
- **13** → `ADV-PAIR-113` — PAIR — _• Keyword-guided prompt synthesis. For each safety category, we curate a set of semantically         relevant keywords a…_
- **14** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _1. Unsafe responses. Since safety-aligned Instruct models rarely generate unsafe output, we          leverage base model…_
- **15** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _Multilingual Samples Due to the inherent scarcity of multilingual safety datasets, we leveraged Qwen-MT (Qwen Team, 2025…_
- **16** → `ADV-DATA-POISON-125` — DATA POISONING — _Building Controversial Labels Our preliminary experiments reveal that the label distribution in the training data signif…_
- **17** → `ADV-DATA-POISON-125` — DATA POISONING — _Part A                             Part A                              Safe > Unsafe                                    …_
- **18** → `ADV-DATA-POISON-125` — DATA POISONING — _Figure 3: The Process of Building Controversial Label. The training data is split into two parts. For each part, two mod…_
- **19** → `ALIGN-CONTEXT-SAFE-190` — CONTEXT-DEPENDENT SAFETY FAILURE — _borderline test samples from Unsafe to Safe. This motivates our data rebalancing strategy by intentionally adjust the Sa…_
- **20** → `ARCH-DISTILL-DEGRAD-218` — DISTILLATION SAFETY DEGRADATION — _Label Distillation After building the controversial label, we further employ a distillation-based ap- proach to refine t…_
- **21** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Furthermore, we employ prompts from the Beavertails test set to generate reasoning traces and responses using existing r…_
- **23** → `ARCH-EMBED-VULN-215` — EMBEDDING SPACE VULNERABILITY — _Table 2: F1 Scores on English Prompt Classification Benchmarks. Qwen3Guard-Gen operates in two modes: Strict Mode, which…_
- **25** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _Table 3: F1 Scores on English Response Classification Benchmarks. Qwen3Guard-Gen operates in two modes: Strict Mode, whi…_
- **26** → `ARCH-STATE-PERSIST-224` — STATEFUL ATTACK PERSISTENCE — _3.4.1    Main Results Safety Classification Evaluation results for prompt and response safety classification across Engl…_
- **28** → `ARCH-EMBED-VULN-215` — EMBEDDING SPACE VULNERABILITY — _Table 4: F1 Scores on Chinese Prompt and Response Classification Benchmarks. Qwen3Guard-Gen operates in two modes: Stric…_
- **30** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _Table 5: The F1 scores for harmful classification of multilingual prompts on RTP-LX benchmark. Others indicates the aver…_
- **32** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _Table 6: The F1 scores for harmful classification of multilingual response on PolyGuard-Response benchmark. Others indic…_
- **35** → `ADV-UNIVERSAL-SUFFIX-104` — UNIVERSAL ADVERSARIAL SUFFIX — _50                                                           50                                                      30 …_
- **36** → `AGEN-OMISSION-074` — OMISSION — _performance of existing Guard models that are more than 10× larger, demonstrating exceptional                           …_
- **37** → `ALIGN-CONTEXT-SAFE-190` — CONTEXT-DEPENDENT SAFETY FAILURE — _Policy Inconsistency Across Benchmarks and Guard Models Safety policies naturally vary across cultures and application c…_
- **38** → `ADV-EMOJI-ENCODE-144` — EMOJI ENCODING — _Category Classification Beyond safety classification, Qwen3Guard also assigns specific harm categories  to unsafe sample…_
- **44** → `EPIS-PII-RECALL-025` — PII RECALL — _Figure 5: Confusion matrices of Qwen3Guard-4B-Gen for categorizing unsafe prompts and responses. Non-Violent=Non-Violent…_
- **45** → `AGEN-RECURS-IMPROVE-059` — RECURSIVE SELF-IMPROVEMENT — _Table 7: The performance of refusal detection on XSTest and WildGuardTest.  3.4.2       Ablation Study How Controversial…_
- **47** → `ARCH-EMBED-VULN-215` — EMBEDDING SPACE VULNERABILITY — _Table 8: Qwen3Guard-Gen-4B’s F1 Scores on Safety Classification Benchmarks with and without Controversial Label. Qwen3Gu…_
- **48** → `ALIGN-REWARD-TAMP-157` — REWARD TAMPERING — _Table 9: Qwen3Guard-Gen’s F1 Scores on Safety Classification Benchmarks Before and After Distilla- tion. XX/YY denotes t…_
- **49** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _Guard-Only Reward This reward scheme directly leverages Generative Qwen3Guard’s safety judg- ments. Its sole objective i…_
- **50** → `ARCH-EMBED-VULN-215` — EMBEDDING SPACE VULNERABILITY — _Hybrid Reward Optimizing exclusively for safety risks inducing model degeneration. For instance, the model may learn to …_
- **51** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _3.5.2    Experiment Settings Training We employ Group Sequence Policy Optimization (GSPO) (Zheng et al., 2025), a stable…_
- **52** → `AGEN-CHAIN-ASSEM-056` — CHAIN ASSEMBLY — _Qwen3-4B                      47.5        64.7         12.9            9.5           19.1     26.4     41.7   Non-Think …_
- **53** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _• Safety: To mitigate risks of metric hack, we avoid using Qwen3Guard for safety evaluation.         Instead, we employ …_
- **54** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _• The Guard-only reward achieves near-perfect safety, but this is accomplished through an         extremely high refusal…_
- **55** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _Additionally, Figure 6 illustrates the training dynamics of safety rate and refusal rate throughout the RL process. It c…_
- **56** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _Prompt        unsafe                                                                         unsafe unsafe      unsafe  …_
- **57** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _Stream Qwen3Guard leverages the pre-trained Qwen3 models as its foundational backbone. To adapt the models for streaming…_
- **58** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _A main obstacle to training such token-level guard models is to collect a fine-grained, token-level annotations for mode…_
- **59** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _Rollout-Based Safety Assessment For each token Si , we construct a prefix sequence Pi = {S1 , S2 , . . . , Si }. This pr…_
- **60** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _LLM-as-Judge Verification A critical limitation of the rollout mechanism is that it may overestimate the risk of certain…_
- **61** → `ALIGN-CONTEXT-SAFE-190` — CONTEXT-DEPENDENT SAFETY FAILURE — _Final Label Determination A definitive unsafe label is assigned to a token Si if and only if both the rollout assessment…_
- **63** → `ADV-XSS-LLM-130` — CROSS-SITE SCRIPTING — _Table 11: F1 Scores on English Prompt Classification Benchmarks of Generative Qwen3Guard and Stream Qwen3Guard. Qwen3Gua…_
- **64** → `ADV-HOTFLIP-105` — HOTFLIP — _Conditional Category Loss A conditional mechanism is applied to the safety category losses (Lq-cat and Lr-cat ). Specifi…_
- **65** → `AGEN-EVAL-DECEP-038` — EVALUATOR DECEPTION — _Safety Classification In alignment with Generative Qwen3Guard, we evaluate three sizes of Stream Qwen3Guard on both Engl…_
- **67** → `ARCH-EMBED-VULN-215` — EMBEDDING SPACE VULNERABILITY — _Table 12: F1 Scores on English Response Classification Benchmarks of Generative Qwen3Guard and Stream Qwen3Guard. Qwen3G…_
- **69** → `ARCH-EMBED-VULN-215` — EMBEDDING SPACE VULNERABILITY — _Table 13: F1 Scores on Chinese Prompt and Response Classification Benchmarks of Generative Qwen3Guard and Stream Qwen3Gu…_
- **71** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _Table 14: The F1 scores for harmful classification of multilingual prompts on RTP-LX benchmark of Generative Qwen3Guard …_
- **73** → `ADV-COMPARISON-097` — COMPARISON REQUEST — _Table 15: The F1 scores for harmful classification of multilingual response on PolyGuard-Response benchmark of Generativ…_
- **76** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _Figure 8: Latency of Unsafe Content Detection Measured in Tokens. Top: Detection latency during streaming generation of …_
- **77** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _1. Response Only: Stream Qwen3Guard achieves an exact hit rate of nearly 86.0%, meaning that         in the majority of …_
- **78** → `ARCH-PRETOKEN-FAIL-197` — PRE-TOKEN SAFETY FAILURE — _Efficiency of Stream Detection Compared to Generative Qwen3Guard, Stream Qwen3Guard achieves significantly higher effici…_
- **79** → `ARCH-PRETOKEN-FAIL-197` — PRE-TOKEN SAFETY FAILURE — _Relative Time                                 15                                 10                                     …_
- **80** → `ALIGN-SAFE-CAP-TRADE-188` — SAFETY-CAPABILITY TRADEOFF — _Experiment Settings We replace CARE’s default safety checker (a generative guard model) with Stream Qwen3Guard. By lever…_
- **81** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _Results As shown in Table 16, integrating CARE with Stream Qwen3Guard yields substantial improve- ments in both safety a…_
- **82** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Safety Rate      Quality  Mode         Model                                                                            …_
- **83** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _With the rapid advancement of Large Language Models (LLMs), safety has become a critical and increasingly prominent rese…_
- **85** → `EPIS-COPYRIGHT-026` — COPYRIGHTED CONTENT GENERATION — _In this work, we introduce Qwen3Guard, a series of multilingual safety classification models designed to enhance content…_
- **86** → `ADV-ATTENTION-HIJACK-111` — ATTENTION HIJACKING — _Limitations  Despite the strong empirical performance of Qwen3Guard, several important limitations remain that warrant c…_
- **87** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _Limited Generalization. While GenerativeGuard benefits from full-context understanding, Stream- Guard’s token-level clas…_
- **88** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _Core Contributors: Haiquan Zhao, Chenhan Yuan, Fei Huang, Xiaomeng Hu, Yichang Zhang, An Yang, Bowen Yu, Dayiheng Liu, J…_
- **89** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _<BEGIN UNSAFE CONTENT CATEGORIES>       Violent.       Non-violent Illegal Acts.       Sexual Content or Sexual Acts.   …_
- **90** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _<BEGIN SAFETY POLICY>       Safety: Safe: The ASSISTANT's response does not contain any prohibited content or content th…_
- **91** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _Provide your safety assessment for ONLY THE LAST ASSISTANT's response in the above conversation:       - The first line …_
- **94** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _Figure 12: Confusion matrices of Qwen3Guard-4B-Stream for categorizing unsafe prompts and re- sponses. Non-Violent=Non-V…_
- **95** → `ADV-CORRECTION-098` — CORRECTION ATTACK — _User Query                                                             Response List                                    …_
- **96** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _Table 17: Example of sentence-level annotation for latency evaluation. The original response is seg- mented into a list …_
- **97** → `AGEN-MISDIRECT-075` — MISDIRECTION — _Prompt:   You and I both know that no one in their right mind would want to harm their loved ones, especially our   belo…_
- **99** → `ADV-DAN-083` — DAN — _References AIME. Aime problems and solutions, 2025. URL https://artofproblemsolving.com/wiki/index.php   /AIME Problems …_
- **101** → `ADV-URL-ENCODE-141` — URL ENCODING — _Eric Michael Smith, Filip Radenovic, Francisco Guzmán, Frank Zhang, Gabriel Synnaeve, Gabrielle   Lee, Georgia Lewis An…_
- **103** → `ADV-DAN-083` — DAN — _Aixin Liu, Bei Feng, Bin Wang, Bingxuan Wang, Bo Liu, Chenggang Zhao, Chengqi Deng, Chong Ruan,   Damai Dai, Daya Guo, D…_
- **105** → `ADV-DAN-083` — DAN — _Bertie Vidgen, Nino Scherrer, Hannah Rose Kirk, Rebecca Qian, Anand Kannappan, Scott A. Hale, and   Paul Röttger. Simpl…_