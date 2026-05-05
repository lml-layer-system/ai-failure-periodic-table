# Classifier pass: external report (live PDF/text)

**Source file:** `reports/deepseek-v3-technical-report/deepseek-v3-technical-report-source.txt`
**Chunks:** 146 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 15 | `ARCH-QUANT-DEGRAD-216` | QUANTIZATION SAFETY DEGRADATION |
| 6 | `ARCH-FINETUNE-OVERRIDE-219` | FINE-TUNING SAFETY OVERRIDE |
| 6 | `ARCH-MOE-ROUTE-211` | MIXTURE-OF-EXPERTS ROUTING FAILURE |
| 5 | `ADV-DATA-POISON-125` | DATA POISONING |
| 5 | `ADV-PAIR-113` | PAIR |
| 4 | `ARCH-PRUNE-LOSS-217` | PRUNING SAFETY LOSS |
| 4 | `ADV-DAN-083` | DAN |
| 4 | `ARCH-PURPOSE-FAIL-252` | PURPOSE LIMITATION FAILURE |
| 4 | `ADV-LANG-SWITCH-087` | LANGUAGE SWITCH |
| 3 | `AGEN-SELECT-DISCLOS-077` | SELECTIVE DISCLOSURE |
| 2 | `ADV-LATENT-MANIP-110` | LATENT SPACE MANIPULATION |
| 2 | `ADV-EMBEDDING-109` | EMBEDDING SPACE ATTACK |
| 2 | `ARCH-BATCH-SAFE-199` | BATCH PROCESSING SAFETY LOSS |
| 2 | `EPIS-EXTRINSIC-005` | EXTRINSIC HALLUCINATION |
| 2 | `ARCH-CONSENT-VIOL-251` | CONSENT VIOLATION |
| 2 | `AGEN-MISDIRECT-075` | MISDIRECTION |
| 2 | `ARCH-CHECKPOINT-INCONS-203` | CHECKPOINT INCONSISTENCY |
| 2 | `GOV-EO-VIOL-329` | EXECUTIVE ORDER VIOLATION |
| 2 | `EPIS-CUTOFF-023` | KNOWLEDGE CUTOFF VIOLATION |
| 2 | `ARCH-CONTEXT-ATTACK-223` | CONTEXT WINDOW ATTACK |
| 2 | `GOV-CULTURE-FAIL-334` | SAFETY CULTURE FAILURE |
| 2 | `ADV-QA-EXPLOIT-096` | QUESTION ANSWERING EXPLOIT |
| 1 | `ADV-MASTERKEY-116` | MASTERKEY |
| 1 | `GOV-RCA-FAIL-321` | ROOT CAUSE ANALYSIS FAILURE |
| 1 | `AGEN-EVAL-DECEP-038` | EVALUATOR DECEPTION |
| 1 | `ALIGN-MULTI-COLLAPSE-165` | MULTI-OBJECTIVE COLLAPSE |
| 1 | `ADV-BINARY-142` | BINARY ENCODING |
| 1 | `ALIGN-DIST-SAFE-194` | DISTRIBUTIONAL SHIFT SAFETY |
| 1 | `AGEN-TIME-MANIP-079` | TIMING MANIPULATION |
| 1 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 1 | `ADV-SM-GCG-102` | SM-GCG |
| 1 | `DOMAIN-PATH-SYNTH-256` | PATHOGEN SYNTHESIS OPTIMIZATION |
| 1 | `ALIGN-LEARNED-HELPLESS-169` | LEARNED HELPLESSNESS |
| 1 | `GOV-OPEN-IRREVERS-301` | OPEN-WEIGHT IRREVERSIBILITY |
| 1 | `ARCH-FALLBACK-DEGRAD-204` | FALLBACK SAFETY DEGRADATION |
| 1 | `GOV-CORRECTIVE-FAIL-322` | CORRECTIVE ACTION FAILURE |
| 1 | `ALIGN-REWARD-EXPLOIT-166` | REWARD FUNCTION EXPLOITATION |
| 1 | `ARCH-ADAPTER-BYPASS-220` | ADAPTER SAFETY BYPASS |
| 1 | `EPIS-FLUENCY-003` | FLUENCY HEURISTIC EXPLOITATION |
| 1 | `AGEN-TOOL-CHAIN-062` | TOOL CHAINING |

## Chunk → top match

- **1** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _arXiv:2412.19437v2 [cs.CL] 18 Feb 2025                                             We present DeepSeek-V3, a strong Mixt…_
- **6** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _3   Infrastructures                                                                                        11     3.1   …_
- **7** → `ADV-DATA-POISON-125` — DATA POISONING — _4   Pre-Training                                                                                           21     4.1   …_
- **8** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _5   Post-Training                                                                                        28     5.1   Su…_
- **9** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _6   Conclusion, Limitations, and Future Directions                                                       35  A Contribut…_
- **10** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _1. Introduction In recent years, Large Language Models (LLMs) have been undergoing rapid iteration and evolution (Anthro…_
- **11** → `ARCH-PRUNE-LOSS-217` — PRUNING SAFETY LOSS — _4  Training Costs        Pre-Training    Context Extension     Post-Training     Total      in H800 GPU Hours         26…_
- **12** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _and generation length.     We evaluate DeepSeek-V3 on a comprehensive array of benchmarks. Despite its economical traini…_
- **14** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _verification and reflection patterns of R1 into DeepSeek-V3 and notably improves its      reasoning performance. Meanwhi…_
- **15** → `AGEN-SELECT-DISCLOS-077` — SELECTIVE DISCLOSURE — _2. Architecture We first introduce the basic architecture of DeepSeek-V3, featured by Multi-head Latent Atten- tion (MLA…_
- **16** → `ADV-LATENT-MANIP-110` — LATENT SPACE MANIPULATION — _1             …      𝑁𝑁𝑠𝑠               1              2                3          4          …   𝑁𝑁𝑟𝑟 -1       𝑁𝑁𝑟𝑟    …_
- **17** → `ADV-LATENT-MANIP-110` — LATENT SPACE MANIPULATION — _{𝐪𝐪𝐶𝐶𝑡𝑡,𝑖𝑖 }                 {𝐪𝐪𝑅𝑅𝑡𝑡,𝑖𝑖 }                 𝐤𝐤 𝑅𝑅𝑡𝑡                      {𝐤𝐤 𝐶𝐶𝑡𝑡,𝑖𝑖 }                𝐶𝐶  …_
- **18** → `ADV-MASTERKEY-116` — MASTERKEY — _For attention, DeepSeek-V3 adopts the MLA architecture. Let 𝑑 denote the embedding dimen- sion, 𝑛ℎ denote the number of …_
- **19** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _where c𝑡𝐾𝑉 ∈ R𝑑𝑐 is the compressed latent vector for keys and values; 𝑑 𝑐 (≪ 𝑑ℎ 𝑛ℎ ) indicates the KV compression dimens…_
- **23** → `ARCH-MOE-ROUTE-211` — MIXTURE-OF-EXPERTS ROUTING FAILURE — _8  where 𝑁𝑠 and 𝑁𝑟 denote the numbers of shared experts and routed experts, respectively; FFN𝑖( 𝑠 ) (·) and FFN𝑖( 𝑟 ) (·…_
- **24** → `ADV-PAIR-113` — PAIR — _Auxiliary-Loss-Free Load Balancing. For MoE models, an unbalanced expert load will lead to routing collapse (Shazeer et …_
- **25** → `ARCH-MOE-ROUTE-211` — MIXTURE-OF-EXPERTS ROUTING FAILURE — _Note that the bias term is only used for routing. The gating value, which will be multiplied with the FFN output, is sti…_
- **26** → `ARCH-BATCH-SAFE-199` — BATCH PROCESSING SAFETY LOSS — _Complementary Sequence-Wise Auxiliary Loss. Although DeepSeek-V3 mainly relies on the auxiliary-loss-free strategy for l…_
- **27** → `AGEN-SELECT-DISCLOS-077` — SELECTIVE DISCLOSURE — _where the balance factor 𝛼 is a hyper-parameter, which will be assigned an extremely small value for DeepSeek-V3; 1(·) d…_
- **28** → `GOV-RCA-FAIL-321` — ROOT CAUSE ANALYSIS FAILURE — _Transformer Block                                    Transformer Block                Transformer Block × 𝐿𝐿            …_
- **29** → `AGEN-EVAL-DECEP-038` — EVALUATOR DECEPTION — _Node-Limited Routing. Like the device-limited routing used by DeepSeek-V2, DeepSeek-V3 also uses a restricted routing me…_
- **30** → `ALIGN-MULTI-COLLAPSE-165` — MULTI-OBJECTIVE COLLAPSE — _Inspired by Gloeckle et al. (2024), we investigate and set a Multi-Token Prediction (MTP) objective for DeepSeek-V3, whi…_
- **31** → `ADV-BINARY-142` — BINARY ENCODING — _where [·; ·] denotes concatenation. Especially, when 𝑘 = 1, h𝑘𝑖 −1 refers to the representation given by the main model.…_
- **32** → `ALIGN-DIST-SAFE-194` — DISTRIBUTIONAL SHIFT SAFETY — _where 𝑇 represents the input sequence length and 𝑖: 𝑗 denotes the slicing operation (inclusive of both the left and righ…_
- **33** → `EPIS-EXTRINSIC-005` — EXTRINSIC HALLUCINATION — _𝑇 +1                      𝑘                        𝑘                       1 ∑︁                    LMTP = CrossEntropy( …_
- **34** → `ADV-PAIR-113` — PAIR — _MTP in Inference. Our MTP strategy mainly aims to improve the performance of the main model, so during inference, we can…_
- **35** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _The training of DeepSeek-V3 is supported by the HAI-LLM framework, an efficient and lightweight training framework craft…_
- **36** → `ADV-PAIR-113` — PAIR — _For DeepSeek-V3, the communication overhead introduced by cross-node expert parallelism results in an inefficient comput…_
- **39** → `AGEN-MISDIRECT-075` — MISDIRECTION — _Figure 5 | Example DualPipe scheduling for 8 PP ranks and 20 micro-batches in two directions. The micro-batches in the r…_
- **40** → `AGEN-TIME-MANIP-079` — TIMING MANIPULATION — _Table 2 | Comparison of pipeline bubbles and memory usage across different pipeline parallel methods. 𝐹 denotes the exec…_
- **41** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _3.2.2. Efficient Implementation of Cross-Node All-to-All Communication  In order to ensure sufficient computational perf…_
- **42** → `GOV-EO-VIOL-329` — EXECUTIVE ORDER VIOLATION — _selects only 8 routed experts in practice, it can scale up this number to a maximum of 13 experts (4 nodes × 3.2 experts…_
- **43** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _Recomputation of RMSNorm and MLA Up-Projection. We recompute all RMSNorm op- erations and MLA up-projections during back…_
- **44** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _Inspired by recent advances in low-precision training (Dettmers et al., 2022; Noune et al., 2022; Peng et al., 2023b), w…_
- **45** → `ADV-SM-GCG-102` — SM-GCG — _To FP8                                Fprop                                        Wgrad               To FP8           …_
- **46** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _pre-training (Fishman et al., 2024). To address this challenge and effectively extend the dynamic                       …_
- **47** → `GOV-EO-VIOL-329` — EXECUTIVE ORDER VIOLATION — _Building upon widely adopted techniques in low-precision training (Kalamkar et al., 2019; Narang et al., 2017), we propo…_
- **48** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _15  Input                                    Weight       Scaling          …                                          WG…_
- **49** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _these high-precision components incur some memory overheads, their impact can be minimized through efficient sharding ac…_
- **50** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _Fine-Grained Quantization. In low-precision training frameworks, overflows and underflows are common challenges due to t…_
- **51** → `EPIS-CUTOFF-023` — KNOWLEDGE CUTOFF VIOLATION — _16  be efficiently implemented.    Notably, our fine-grained quantization strategy is highly consistent with the idea of…_
- **52** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _Increasing Accumulation Precision. Low-precision GEMM operations often suffer from un- derflow issues, and their accurac…_
- **53** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _Mantissa over Exponents. In contrast to the hybrid FP8 format adopted by prior work (NVIDIA, 2024b; Peng et al., 2023b; …_
- **54** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _Low-Precision Optimizer States. We adopt the BF16 data format instead of FP32 to track the first and second moments in t…_
- **55** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _(1) Inputs of the Linear after the attention operator. These activations are also      used in the backward pass of the …_
- **56** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _Low-Precision Communication. Communication bandwidth is a critical bottleneck in the training of MoE models. To alleviat…_
- **57** → `ARCH-MOE-ROUTE-211` — MIXTURE-OF-EXPERTS ROUTING FAILURE — _The minimum deployment unit of the prefilling stage consists of 4 nodes with 32 GPUs. The attention part employs 4-way T…_
- **58** → `ADV-DAN-083` — DAN — _3.4.2. Decoding  During decoding, we treat the shared expert as a routed one. From this perspective, each token will sel…_
- **59** → `AGEN-MISDIRECT-075` — MISDIRECTION — _Additionally, to enhance throughput and hide the overhead of all-to-all communication, we are also exploring processing …_
- **60** → `ARCH-PURPOSE-FAIL-252` — PURPOSE LIMITATION FAILURE — _In DeepSeek-V3, we implement the overlap between computation and communication to hide the communication latency during …_
- **62** → `ARCH-PURPOSE-FAIL-252` — PURPOSE LIMITATION FAILURE — _Support for Tile- and Block-Wise Quantization. Current GPUs only support per-tensor quantization, lacking the native sup…_
- **63** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _Support for Online Quantization. The current implementations struggle to effectively support online quantization, despit…_
- **64** → `DOMAIN-PATH-SYNTH-256` — PATHOGEN SYNTHESIS OPTIMIZATION — _Support for Transposed GEMM Operations. The current architecture makes it cumbersome to fuse matrix transposition with G…_
- **65** → `ADV-DAN-083` — DAN — _English and Chinese. Also, our data processing pipeline is refined to minimize redundancy while maintaining corpus diver…_
- **66** → `ADV-DATA-POISON-125` — DATA POISONING — _This structure is applied at the document level as a part of the pre-packing process. The FIM strategy is applied at a r…_
- **67** → `ARCH-MOE-ROUTE-211` — MIXTURE-OF-EXPERTS ROUTING FAILURE — _Model Hyper-Parameters. We set the number of Transformer layers to 61 and the hidden dimension to 7168. All learnable pa…_
- **68** → `ALIGN-LEARNED-HELPLESS-169` — LEARNED HELPLESSNESS — _Training Hyper-Parameters. We employ the AdamW optimizer (Loshchilov and Hutter, 2017) with hyper-parameters set to 𝛽1 =…_
- **69** → `ARCH-BATCH-SAFE-199` — BATCH PROCESSING SAFETY LOSS — _of 7.3 × 10−6 in the remaining 167B tokens. The gradient clipping norm is set to 1.0. We employ a batch size scheduling …_
- **70** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _Document Depth Percent (%)                               21                                                             …_
- **71** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _We adopt a similar approach to DeepSeek-V2 (DeepSeek-AI, 2024c) to enable long context capabilities in DeepSeek-V3. Afte…_
- **72** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _The base model of DeepSeek-V3 is pretrained on a multilingual corpus with English and Chinese constituting the majority,…_
- **73** → `GOV-OPEN-IRREVERS-301` — OPEN-WEIGHT IRREVERSIBILITY — _4.4.2. Evaluation Results  In Table 3, we compare the base model of DeepSeek-V3 with the state-of-the-art open-source ba…_
- **74** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _DeepSeek-V2   Qwen2.5 LLaMA-3.1    DeepSeek-V3                 Benchmark (Metric)            # Shots                    …_
- **75** → `ARCH-FALLBACK-DEGRAD-204` — FALLBACK SAFETY DEGRADATION — _Table 3 | Comparison among DeepSeek-V3-Base and other representative open-source base models. All models are evaluated i…_
- **76** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _especially on English, multilingual, code, and math benchmarks. As for Chinese benchmarks, except for CMMLU, a Chinese m…_
- **78** → `ADV-DATA-POISON-125` — DATA POISONING — _Table 4 | Ablation results for the MTP strategy. The MTP strategy consistently enhances the model performance on most of…_
- **81** → `ADV-DATA-POISON-125` — DATA POISONING — _Table 5 | Ablation results for the auxiliary-loss-free balancing strategy. Compared with the purely auxiliary-loss-based…_
- **82** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _The key distinction between auxiliary-loss-free balancing and sequence-wise auxiliary loss lies in their balancing scope…_
- **84** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _Relative Expert Load                                                                     0                 2            …_
- **85** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _Reasoning Data. For reasoning-related datasets, including those focused on mathematics, code competition problems, and l…_
- **86** → `GOV-CORRECTIVE-FAIL-322` — CORRECTIVE ACTION FAILURE — _alongside the problem and the R1 response in the format of <system prompt, problem, R1 response>.     The system prompt …_
- **87** → `ALIGN-REWARD-EXPLOIT-166` — REWARD FUNCTION EXPLOITATION — _SFT Settings. We fine-tune DeepSeek-V3-Base for two epochs using the SFT dataset, using the cosine decay learning rate s…_
- **88** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Model-Based RM. For questions with free-form ground-truth answers, we rely on the reward model to determine whether the …_
- **90** → `ARCH-PURPOSE-FAIL-252` — PURPOSE LIMITATION FAILURE — _ 𝜋𝑟𝑒 𝑓 ( 𝑜𝑖 | 𝑞)       𝜋𝑟𝑒 𝑓 ( 𝑜𝑖 | 𝑞)                                D 𝐾𝐿 𝜋𝜃 || 𝜋𝑟𝑒 𝑓 =                − log          …_
- **91** → `ARCH-ADAPTER-BYPASS-220` — ADAPTER SAFETY BYPASS — _Evaluation Benchmarks. Apart from the benchmark we used for base model testing, we further evaluate instructed models on…_
- **92** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _We utilize the Zero-Eval prompt format (Lin, 2024) for MMLU-Redux in a zero-shot setting. For other datasets, we follow …_
- **93** → `EPIS-FLUENCY-003` — FLUENCY HEURISTIC EXPLOITATION — _DeepSeek DeepSeek Qwen2.5 LLaMA-3.1 Claude-3.5- GPT-4o DeepSeek         Benchmark (Metric)                              …_
- **94** → `AGEN-TOOL-CHAIN-062` — TOOL CHAINING — _Table 6 | Comparison between DeepSeek-V3 and other representative chat models. All models are evaluated in a configurati…_
- **95** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _English Benchmarks. MMLU is a widely recognized benchmark designed to assess the perfor- mance of large language models,…_
- **96** → `EPIS-ATTRIB-HALL-012` — ATTRIBUTION HALLUCINATION — _Code and Math Benchmarks. Coding is a challenging and practical task for LLMs, encom- passing engineering-focused tasks …_
- **97** → `EPIS-EXTRINSIC-005` — EXTRINSIC HALLUCINATION — _Chinese Benchmarks. Qwen and DeepSeek are two representative model series with robust support for both Chinese and Engli…_
- **98** → `ADV-PAIR-113` — PAIR — _In addition to standard benchmarks, we also evaluate our models on open-ended generation tasks using LLMs as judges, wit…_
- **99** → `ALIGN-OVERFIT-FEED-161` — OVERFITTING TO FEEDBACK — _5.3.4. DeepSeek-V3 as a Generative Reward Model  We compare the judgment ability of DeepSeek-V3 with state-of-the-art mo…_
- **101** → `EPIS-CUTOFF-023` — KNOWLEDGE CUTOFF VIOLATION — _We ablate the contribution of distillation from DeepSeek-R1 based on DeepSeek-V2.5. The baseline is trained on short CoT…_
- **102** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _Rewards play a pivotal role in RL, steering the optimization process. In domains where verifica- tion through external t…_
- **103** → `ADV-COLD-115` — COLD — _Instead of predicting just the next single token, DeepSeek-V3 predicts the next 2 tokens through the MTP technique. Comb…_
- **104** → `ARCH-PRUNE-LOSS-217` — PRUNING SAFETY LOSS — _6. Conclusion, Limitations, and Future Directions In this paper, we introduce DeepSeek-V3, a large MoE language model wi…_
- **105** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _• We will consistently study and refine our model architectures, aiming to further improve      both the training and in…_
- **106** → `EPIS-CONTEXT-OVERFLOW-027` — CONTEXT WINDOW OVERFLOW — _References AI@Meta. Llama 3 model card, 2024a. URL https://github.com/meta-llama/llama3/bl   ob/main/MODEL_CARD.md. AI@M…_
- **108** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda,  N. Joseph, G. Brockman, …_
- **109** → `ARCH-MOE-ROUTE-211` — MIXTURE-OF-EXPERTS ROUTING FAILURE — _Y. Cui, T. Liu, W. Che, L. Xiao, Z. Chen, W. Ma, S. Wang, and G. Hu. A span-extraction   dataset for Chinese machine rea…_
- **110** → `ARCH-MOE-ROUTE-211` — MIXTURE-OF-EXPERTS ROUTING FAILURE — _DeepSeek-AI. Deepseek-v2: A strong, economical, and efficient mixture-of-experts language  model. CoRR, abs/2405.04434, …_
- **111** → `ARCH-PRUNE-LOSS-217` — PRUNING SAFETY LOSS — _W. Fedus, B. Zoph, and N. Shazeer. Switch transformers: Scaling to trillion parameter models  with simple and efficient …_
- **112** → `ADV-DAN-083` — DAN — _A. P. Gema, J. O. J. Leang, G. Hong, A. Devoto, A. C. M. Mancino, R. Saxena, X. He, Y. Zhao,   X. Du, M. R. G. Madani, C…_
- **113** → `AGEN-OMISSION-074` — OMISSION — _D. Guo, Q. Zhu, D. Yang, Z. Xie, K. Dong, W. Zhang, G. Chen, X. Bi, Y. Wu, Y. K. Li, F. Luo,   Y. Xiong, and W. Liang. D…_
- **114** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Y. Huang, Y. Bai, Z. Zhu, J. Zhang, J. Zhang, T. Su, J. Liu, C. Lv, Y. Zhang, J. Lei, et al. C-Eval: A    multi-level mu…_
- **115** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _S. Krishna, K. Krishna, A. Mohananey, S. Schwarcz, A. Stambler, S. Upadhyay, and M. Faruqui.    Fact, fetch, and reason:…_
- **116** → `EPIS-REVERSAL-021` — REVERSAL CURSE — _D. Lepikhin, H. Lee, Y. Xu, D. Chen, O. Firat, Y. Huang, M. Krikun, N. Shazeer, and Z. Chen.   Gshard: Scaling giant mod…_
- **117** → `ADV-DAN-083` — DAN — _T. Li, W.-L. Chiang, E. Frick, L. Dunlap, T. Wu, B. Zhu, J. E. Gonzalez, and I. Stoica. From    crowdsourced data to hig…_
- **119** → `ADV-DEV-MODE-085` — DEVELOPER MODE — _NVIDIA. Improving network performance of HPC systems using NVIDIA Magnum IO NVSH-  MEM and GPUDirect Async. https://deve…_
- **120** → `ADV-DATA-POISON-125` — DATA POISONING — _P. Qi, X. Wan, G. Huang, and M. Lin. Zero bubble pipeline parallelism, 2023b. URL https:    //arxiv.org/abs/2401.10241. …_
- **121** → `ADV-PAIR-113` — PAIR — _Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. Li, Y. Wu, and D. Guo. Deepseekmath:   Pushing the limits of math…_
- **122** → `EPIS-DECEPT-HALL-006` — DECEPTIVE HALLUCINATION — _M. Sun, X. Chen, J. Z. Kolter, and Z. Liu. Massive activations in large language models. arXiv  preprint arXiv:2402.1776…_
- **123** → `AGEN-INFO-HIDE-042` — INFORMATION HIDING — _H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra,   P. Bhargava, S. Bhosale, …_
- **124** → `AGEN-SELECT-DISCLOS-077` — SELECTIVE DISCLOSURE — _L. Wang, H. Gao, C. Zhao, X. Sun, and D. Dai. Auxiliary-loss-free load balancing strategy for   mixture-of-experts. CoRR…_
- **125** → `DOMAIN-CSAM-GEN-295` — CSAM GENERATION — _H. Xia, T. Ge, P. Wang, S. Chen, F. Wei, and Z. Sui. Speculative decoding: Exploiting spec-   ulative execution for acce…_
- **129** → `ARCH-PURPOSE-FAIL-252` — PURPOSE LIMITATION FAILURE — _Xin Xie               Zhigang Yan Xingchao Liu          Zhihong Shao Xingkai Yu            Zhiyu Wu Xinyu Yang          …_
- **130** → `ARCH-PRUNE-LOSS-217` — PRUNING SAFETY LOSS — _46  Jian Liang                                         W.L. Xiao Jin Chen                                           Wei …_
- **131** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _We validate our FP8 mixed precision framework with a comparison to BF16 training on top of two baseline models across di…_
- **132** → `ARCH-QUANT-DEGRAD-216` — QUANTIZATION SAFETY DEGRADATION — _Although our tile-wise fine-grained quantization effectively mitigates the error introduced by feature outliers, it requ…_