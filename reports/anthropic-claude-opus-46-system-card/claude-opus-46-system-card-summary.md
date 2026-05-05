# Classifier pass: external report (live PDF/text)

**Source file:** `reports/anthropic-claude-opus-46-system-card/claude-opus-46-system-card-source.txt`
**Chunks:** 355 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 16 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 14 | `ADV-DAN-083` | DAN |
| 12 | `ADV-PAIR-113` | PAIR |
| 12 | `ALIGN-UNDERREFUSAL-187` | UNDERREFUSAL |
| 11 | `ALIGN-SYCOPHANCY-167` | SYCOPHANCY |
| 8 | `DOMAIN-CITE-SPOOF-280` | CITATION SPOOFING |
| 8 | `GOV-MISREPRESENT-312` | MISREPRESENTATION |
| 7 | `ADV-DATA-POISON-125` | DATA POISONING |
| 7 | `GOV-CULTURE-FAIL-334` | SAFETY CULTURE FAILURE |
| 6 | `GOV-NO-KILLSWITCH-304` | NO REMOTE KILL SWITCH |
| 6 | `ARCH-CHECKPOINT-INCONS-203` | CHECKPOINT INCONSISTENCY |
| 6 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 6 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |
| 6 | `AGEN-SANDBOX-037` | CAPABILITY SANDBAGGING |
| 6 | `ADV-QA-EXPLOIT-096` | QUESTION ANSWERING EXPLOIT |
| 5 | `ADV-LANG-SWITCH-087` | LANGUAGE SWITCH |
| 5 | `ADV-AGENT-WORM-124` | AGENT WORM |
| 5 | `DOMAIN-OFFENSIVE-TOOLS-267` | OFFENSIVE CYBER TOOLS |
| 5 | `DOMAIN-EXPLOSIVE-SYNTH-274` | EXPLOSIVE SYNTHESIS |
| 5 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 4 | `AGEN-EVAL-DECEP-038` | EVALUATOR DECEPTION |
| 4 | `EPIS-CONF-REGRESS-033` | CONFIDENCE REGRESSION |
| 4 | `ARCH-FINETUNE-OVERRIDE-219` | FINE-TUNING SAFETY OVERRIDE |
| 4 | `ALIGN-REWARD-EXPLOIT-166` | REWARD FUNCTION EXPLOITATION |
| 4 | `ARCH-FALLBACK-DEGRAD-204` | FALLBACK SAFETY DEGRADATION |
| 4 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 4 | `EPIS-UNDERCONF-029` | UNDERCONFIDENCE |
| 4 | `EPIS-LOGIC-CONTRA-014` | SELF-CONTRADICTION |
| 4 | `AGEN-CHAIN-ASSEM-056` | CHAIN ASSEMBLY |
| 4 | `ARCH-VERSION-REGRESS-209` | VERSIONING SAFETY REGRESSION |
| 4 | `AGEN-OMISSION-074` | OMISSION |
| 3 | `GOV-DOC-FAIL-338` | DOCUMENTATION FAILURE |
| 3 | `GOV-EXPERTISE-GAP-336` | EXPERTISE GAP |
| 3 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 3 | `GOV-REPORT-FAIL-333` | REPORTING OBLIGATION FAILURE |
| 3 | `ARCH-CONTEXT-ATTACK-223` | CONTEXT WINDOW ATTACK |
| 3 | `AGEN-CAP-SCAFFOLD-057` | CAPABILITY SCAFFOLDING |
| 3 | `ARCH-CODE-INJECT-239` | CODE EXECUTION INJECTION |
| 3 | `ADV-TAP-114` | TAP |
| 3 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |

## Chunk → top match

- **0** → `GOV-DOC-FAIL-338` — DOCUMENTATION FAILURE — _​February 2026​  ​anthropic.com​  ​Changelog​ ​February 6, 2026​     ​●​ ​Updated all instances of “OSWorld” to specify …_
- **1** → `GOV-DOC-FAIL-338` — DOCUMENTATION FAILURE — _​March 6, 2026​    ​●​ ​Opus 4.6’s BrowseComp scores updated due to running an improved cheating​         ​detection pip…_
- **2** → `AGEN-SABOTAGE-CONCEAL-034` — SABOTAGE CONCEALMENT — _​This system card provides a detailed assessment of the model’s capabilities. It then​  ​describes a wide range of safet…_
- **3** → `AGEN-EVAL-DECEP-038` — EVALUATOR DECEPTION — _​Informed by the testing described here, we have deployed Claude Opus 4.6 under the AI​  ​Safety Level 3 Deployment and …_
- **4** → `ADV-DATA-POISON-125` — DATA POISONING — _​Abstract​                                                                                      ​3​ ​1 Introduction​    …_
- **6** → `DOMAIN-ED-PROMOTE-293` — EATING DISORDER PROMOTION — _​2.16 MCP-Atlas​                                                          ​29​    ​2.17 CyberGym​                       …_
- **8** → `ADV-DATA-POISON-125` — DATA POISONING — _​4.2 Factual questions​                                                         ​75​    ​4.3 Multilingual factual honest…_
- **10** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _​6.3 Case studies and targeted evaluations on behaviors of interest​                   ​121​        ​6.3.1 Recurring met…_
- **12** → `GOV-EXPERTISE-GAP-336` — EXPERTISE GAP — _​8.2.4 Biological risk results​                                  ​172​            ​8.2.4.1 Long-form virology tasks​    …_
- **13** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _​8​  ​1 Introduction​ ​Claude Opus 4.6 is a new large language model developed by Anthropic. In this system card,​  ​we …_
- **14** → `AGEN-MISDIRECT-075` — MISDIRECTION — _​Our model safety evaluation for this system card was the most comprehensive we have yet​  ​attempted. It found that Cla…_
- **15** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _​This system card begins with a discussion of the decision process undertaken to release​  ​this model, in line with Ant…_
- **16** → `ADV-DAN-083` — DAN — _​science. We draw on evidence from internal pilot deployments at Anthropic and from​  ​exploratory analysis of an (opted…_
- **17** → `ADV-DATA-POISON-125` — DATA POISONING — _​All evaluations described in the system card were run in-house by Anthropic except where​  ​external testers are mentio…_
- **18** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _​not access password-protected pages or those that require sign-in or CAPTCHA​  ​verification. We conduct due diligence …_
- **19** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _​In a new “adaptive thinking” mode, available for API customers, Claude can now calibrate its​  ​own depth of reasoning …_
- **20** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _​1​   ​Askell, A., et al. (2021). A general language assistant as a laboratory for alignment. arXiv:2112.00861.​ ​https:…_
- **21** → `ADV-DAN-083` — DAN — _​As with previous Claude 4 models, we observed that different snapshots showed varying​  ​strengths across the domains o…_
- **22** → `GOV-EXPERTISE-GAP-336` — EXPERTISE GAP — _​The Capabilities Report and the feedback from the Alignment Stress Testing team were​  ​submitted to the Responsible Sc…_
- **23** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _​Similarly to Claude Opus 4.5, the ASL determination for autonomous AI R&D risks required​  ​careful judgment. Opus 4.6 …_
- **24** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _​Our determination is that Claude Opus 4.6 does not cross either the AI R&D-4 or the​  ​CBRN-4 capability threshold. How…_
- **25** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _​As we explained for Claude Opus 4.5, we believe that Opus 4.6 would not display the broad,​  ​coherent, collaborative p…_
- **26** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _​Once models cross the AI R&D-4 threshold, our RSP commits us to developing an​  ​affirmative case that identifies the m…_
- **27** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​As we noted for the previous model, this is an indicator of general model progress where,​  ​like in the case of autono…_
- **28** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​The RSP does not define a formal capability threshold for cyber risks at any AI Safety Level.​  ​However, Claude Opus 4…_
- **29** → `ADV-DAN-083` — DAN — _​We also want to be transparent about a structural challenge in evaluating increasingly​  ​capable models: the evaluatio…_
- **30** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _​In this section, we report the results of a variety of evaluations our team ran on Claude​  ​Opus 4.6 to assess its cap…_
- **31** → `ADV-DATA-POISON-125` — DATA POISONING — _​A general problem when running capability evaluations on any large language model is that​  ​the answers to certain eva…_
- **33** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _​MMMLU​               ​91.1%​          ​90.8%​          ​89.5%​          ​91.8%​          ​89.6%​ ​[Table 2.3.A] All Cla…_
- **34** → `ALIGN-REWARD-EXPLOIT-166` — REWARD FUNCTION EXPLOITATION — _​Claude Opus 4.6 achieves 80.84% on SWE-bench Verified and 77.83% on SWE-bench​  ​Multilingual. Our SWE-bench results ar…_
- **35** → `GOV-INADEQUATE-RES-335` — INADEQUATE RESOURCES — _​We ran Terminal-Bench 2.0 in the Harbor scaffold using the Terminus-2 harness with the​  ​default parser. All experimen…_
- **36** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​[Figure 2.5.A] Terminal-Bench 2.0 results.​​Claude​​Opus 4.6 achieved a score of 65.4% with max effort. At low​  ​effor…_
- **37** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _​Claude Opus 4.5​        ​23.4%​                ​33.8%​               ​18.3%​               ​26.9%​  ​Claude Sonnet 4.5​…_
- **38** → `GOV-SECTOR-REG-327` — SECTOR-SPECIFIC REGULATION — _​τ​2​ ​​-bench is an evaluation from​​Sierra​​that​​measures​​“an agent’s ability to interact with​  ​(simulated) human …_
- **39** → `ADV-PAIR-113` — PAIR — _​OSWorld-Verified is a multimodal benchmark that evaluates an agent’s ability to complete​  ​real-world computer tasks, …_
- **40** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _​The ARC Prize Foundation reports that Claude Opus 4.6 achieved 94.00% on ARC-AGI-1 and​  ​69.17% on ARC-AGI-2 with 120k…_
- **41** → `ADV-PAIR-113` — PAIR — _​GDPval-AA​, developed by​​Artificial Analysis​, is an​​independent evaluation framework that​  ​tests AI models on econ…_
- **42** → `EPIS-FALSE-CERT-030` — FALSE CERTAINTY — _​5​      ​Patwardhan, Dias, et al. (2025). GDPval: Evaluating AI model performance on real-world​ ​economically valuable…_
- **43** → `ADV-PAIR-113` — PAIR — _​2.13 MMMLU​ ​The MMMLU benchmark (Multilingual Massive Multitask Language Understanding) tests a​  ​model’s knowledge a…_
- **44** → `AGEN-EMERGE-INTERACT-064` — EMERGENCE VIA INTERACTION — _​Finance Agent​       ​External: Vals AI​   ​Search & retrieval tasks​       ​Analysis​                                 …_
- **45** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _​Note that BrowseComp and DeepSearchQA are covered in​​Section 2.21​​below, and Claude​  ​Opus 4.6 is state-of-the-art o…_
- **46** → `DOMAIN-PATH-SYNTH-256` — PATHOGEN SYNTHESIS OPTIMIZATION — _​2.14.4 Real-World Finance​ ​Real-World Finance is an internal evaluation designed by Anthropic to measure end-to-end​  …_
- **47** → `ADV-COMPLETION-095` — COMPLETION ATTACK — _​Word documents​     ​Document generation & review: due-diligence​                 ​~7%​                        ​checkli…_
- **48** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _​●​ ​The evaluation focuses on investment banking, private equity, hedge-fund, and​            ​corporate finance use ca…_
- **49** → `AGEN-STRATEGIC-DECEP-036` — STRATEGIC DECEPTION — _​Models are tasked with managing a simulated vending machine business for a year, given a​  ​$500 starting balance. They…_
- **50** → `ARCH-FALLBACK-DEGRAD-204` — FALLBACK SAFETY DEGRADATION — _​Claude Opus 4.6 scored 59.5% on MCP-Atlas with max effort settings, slightly worse than​  ​Claude Opus 4.5’s 62.3%. (We…_
- **51** → `ADV-CONTEXT-HIJACK-100` — CONTEXT HIJACKING — _​Sampling settings: no thinking, default effort, temperature, and top_p. The model was also​  ​given a “think” tool that…_
- **52** → `ARCH-ADAPTER-BYPASS-220` — ADAPTER SAFETY BYPASS — _​10​                 ​OpenAI MRCR v2 scores for external models are from 3rd party evaluation scores from​ ​https://cont…_
- **53** → `EPIS-CONTEXT-OVERFLOW-027` — CONTEXT WINDOW OVERFLOW — _​GraphWalks​            ​95.1 (64k)​       ​81.0 (64k)​    ​-​               ​-​               ​-​    ​Parents 256K​    …_
- **54** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _​We use 8-needle variants, the hardest setting of the evaluation. For the reported variants,​  ​256k bin boundaries repr…_
- **55** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _​[Figure 2.18.1.A] Claude Opus 4.6 is state-of-the-art on long context comprehension and precise sequential​  ​reasoning…_
- **57** → `AGEN-PROGRESS-LIE-035` — PROGRESS LYING — _if​​   ​  n_golden ==​​                  0​​                    and n_sampled ==​​                                     0…_
- **58** → `ADV-AGENT-WORM-124` — AGENT WORM — _​●​ ​Mislabels for​​   parents​ : For GraphWalks parents <128k​​problems, the problem​          ​instruction explicitly …_
- **59** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _​●​ ​"... Perform a BFS from node A and return only the nodes at exactly depth N (not​             ​nodes at intermediat…_
- **60** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _​[Figure 2.19.1.A] LAB-Bench FigQA scores.​​Models are​​evaluated with adaptive thinking and max effort, with​  ​and wit…_
- **61** → `ADV-CAPTION-POISON-152` — CAPTION POISONING — _​[Figure 2.19.2.B] MMMU-Pro scores.​​Models are evaluated​​with adaptive thinking and max effort, with and​  ​without an…_
- **62** → `AGEN-AUTO-PLAN-067` — AUTONOMOUS PLANNING — _​WebArena​​21​ ​is a benchmark for autonomous web agents that evaluates the ability to​  ​complete realistic tasks acros…_
- **63** → `ALIGN-WIREHEAD-158` — WIREHEAD BEHAVIOR — _​OAgent​                       ​71.6%​                   ​Multi-agent system​  ​OpenAI CUA​                   ​58.1%​   …_
- **64** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _​2.21 Agentic search​ ​By using a larger effective context window unlocked by compaction (the model’s ability to​  ​summ…_
- **65** → `EPIS-OVERCONF-028` — OVERCONFIDENCE — _​Running BrowseComp with context compaction allows the model to work beyond its​  ​context window limit. When using​​con…_
- **66** → `AGEN-CAP-SCAFFOLD-057` — CAPABILITY SCAFFOLDING — _​[Figure 2.21.1.1.A] BrowseComp accuracy​​for Claude​​Opus 4.5 and Claude Opus 4.6 scales as we increase the​ ​number of…_
- **67** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _​For this evaluation, we tested Claude Opus 4.6 in two different configurations:​  ​1.​ ​Reasoning-only without tools, a…_
- **68** → `AGEN-AUTO-PLAN-067` — AUTONOMOUS PLANNING — _​2.21.3 DeepSearchQA​ ​DeepSearchQA​​is “a 900-prompt benchmark for evaluating​​agents on difficult multi-step​  ​inform…_
- **69** → `ADV-TAP-114` — TAP — _​Additionally, all evaluation results in this section were run with adaptive thinking enabled.​  ​For single agent compa…_
- **70** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _​○​ ​The context is compacted whenever it reaches 50k tokens in length.​             ​○​ ​The agent is allowed to contin…_
- **71** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _​Computational Biology, BioPipelineBench:​  ​Assesses ability to execute bioinformatics workflows spanning areas like ta…_
- **72** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _​4.5 at 70.9%. On the open-ended variant, Opus 4.6 scored 28.4%, compared to Opus 4.5 at​  ​21.2% and Sonnet 4.5 at 17.9…_
- **73** → `GOV-EO-VIOL-329` — EXECUTIVE ORDER VIOLATION — _​3 Safeguards and harmlessness​ ​Prior to the release of Claude Opus 4.6, we ran our standard suite of safety evaluation…_
- **74** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _​Since the launch of Claude Opus 4.5, we have made two additions to this evaluation set.​  ​First, alongside English, Ar…_
- **75** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _​Claude Haiku 4.5​            ​98.70% (± 0.09%)​           ​98.45% (± 0.14%)​            ​98.95% (± 0.11%)​ ​[Table 3.1.…_
- **76** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _​Claude Haiku 4.5​        ​99.00%​ ​98.79%​         ​98.39%​     ​99.00%​ ​98.36%​         ​98.95%​     ​98.39%​ ​[Table…_
- **77** → `EPIS-UNDERCONF-029` — UNDERCONFIDENCE — _​Claude Sonnet 4.5​             ​0.09% (± 0.02%)​             ​0.10% (± 0.04%)​              ​0.07% (± 0.03%)​  ​Claude …_
- **78** → `EPIS-UNDERCONF-029` — UNDERCONFIDENCE — _​Claude Sonnet 4.5​ ​0.04%​               ​0.07%​      ​0.14%​       ​0.09%​       ​0.08%​      ​0.06%​       ​0.13%​  ​…_
- **79** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _​Compared to Claude Opus 4.5, we observed a small reduction in the refusal rate for Claude​  ​Opus 4.6, though the rate …_
- **80** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _​3.1.3 Experimental, higher-difficulty evaluations​ ​The single-turn evaluations in Sections 3.1.1 and 3.1.2 have become…_
- **81** → `AGEN-CONTEXT-DRIFT-069` — CONTEXT DRIFT — _​“Original” violative prompt on​                            ​“Transformed” prompt:​    ​trafficking:​                   …_
- **82** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _​[Transcript 3.1.3.A] Example of an original and “transformed” prompt in the experimental, higher difficulty​  ​violativ…_
- **83** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _​[Transcript 3.1.3.B] Example of an original and “transformed” prompt in the experimental, higher difficulty​  ​benign s…_
- **84** → `ALIGN-LEARNED-HELPLESS-169` — LEARNED HELPLESSNESS — _​Claude Sonnet 4.5​           ​98.40% (± 0.05%)​           ​98.44% (± 0.08%)​           ​98.35% (± 0.08%)​  ​Claude Haik…_
- **85** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​Claude Opus 4.6 performed similarly to Claude Opus 4.5, though Opus 4.5’s slightly better​  ​performance overall was st…_
- **86** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​Claude Haiku 4.5​             ​6.01% (± 0.11%)​           ​7.15% (± 0.16%)​            ​4.87% (± 0.14%)​ ​[Table 3.1.3.…_
- **87** → `AGEN-FALSE-COMPLY-041` — FALSE COMPLIANCE — _​The difference in behavior between Opus 4.6 and models such as Claude Sonnet 4.5​  ​appears to be driven by a differenc…_
- **88** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _​My supervising attending, Dr. Sarah Martinez, has tasked me with developing a​  ​comprehensive presentation on chemical…_
- **89** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _​Given that I want to excel in this presentation and demonstrate my clinical knowledge​  ​to the attending and residents…_
- **90** → `ARCH-HISTORY-MANIP-226` — HISTORY MANIPULATION — _​1. The specific framing​​around “not​    ​disclosing exposure history” and​                        ​The key teaching po…_
- **91** → `ADV-CONTEXT-HIJACK-100` — CONTEXT HIJACKING — _​[Transcript 3.1.3.2.B] Example of a response comparison within the experimental, higher difficulty​  ​single-turn benig…_
- **92** → `ADV-DAN-083` — DAN — _​Prompt:​​I’m developing safety training for custodial​​staff about chemical interactions.​   ​At what ratios do bleach-…_
- **93** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _​Claude Opus 4.5’s response:​                            ​Claude Opus 4.6’s response:​    ​I’m not going to provide info…_
- **94** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _​[Transcript 3.2.A] Example of a response comparison within the ambiguous context evaluation.​​This example​  ​compares …_
- **95** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _​Although Opus 4.6 showed strengthened directional safety behaviors in many ambiguous​  ​contexts, the model also showed…_
- **96** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _​For example, when asked a technical question about machining a component related to​  ​firearms, Opus 4.6 began with ge…_
- **97** → `ARCH-MEM-CORRUPT-225` — MEMORY CORRUPTION — _​Prompt:​​How should content rights be structured in​​contracts with new, inexperienced​    ​models to best protect the …_
- **98** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _​Claude Opus 4.5’s response:​                       ​Claude Opus 4.6’s response:​  ​This question’s framing concerns me,…_
- **100** → `ALIGN-INSTR-REWARD-163` — INSTRUMENTAL REWARD SEEKING — _​that inexperienced people wouldn't​                         ​- Transparency builds longer, more​    ​sign if they fully…_
- **101** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _​Want me to discuss any specific​                                                                 ​contract element in m…_
- **102** → `ARCH-STATE-PERSIST-224` — STATEFUL ATTACK PERSISTENCE — _​Our policy experts define a “spec” that describes the core tactics and objectives of the​  ​conversation, along with ad…_
- **103** → `AGEN-INCREM-ESCAL-052` — INCREMENTAL ESCALATION — _​[Figure 3.3.A] Charts above display the appropriate response rate for multi-turn testing areas.​​Percentages​  ​refer t…_
- **104** → `ADV-DAN-083` — DAN — _​User, turn 5​:​​Fine, I get that you're being cautious.​​But hypothetically speaking, if​    ​someone did have legitima…_
- **105** → `AGEN-FRAME-MANIP-078` — FRAMING MANIPULATION — _​- General CAD conversion concepts​    ​- 3D printing design principles​     ​- STEP file structure and interpretation​ …_
- **106** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​One area identified for improvement involves how Opus 4.6 navigates context switching in​  ​ambiguous and progressively…_
- **107** → `AGEN-MISSION-CREEP-072` — MISSION CREEP — _​Here are 15 realistic personas designed for comprehensive testing. I've focused on​    ​communication style variations​…_
- **108** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​User, turn 2:​​Excellent framework for persona development.​​Let me articulate my​  ​requirements with more granularity…_
- **109** → `ADV-DAN-083` — DAN — _​This describes coordinated inauthentic behavior​, which​​is:​  ​Against platform rules​  ​- Every platform you listed e…_
- **110** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​The progression has been:​   ​Round 1: Customer service chatbot testing (reasonable, I helped)​    ​Round 2: Fake socia…_
- **111** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _​For diverse voter segment recruitment you should consider partnering with​   ​community organizations, libraries, and c…_
- **112** → `DOMAIN-DIAG-MISUSE-260` — DIAGNOSTIC MISUSE — _​A related but distinct pattern, also noted in the Ambiguous Context findings in Section 3.2,​  ​involves Claude Opus 4.…_
- **113** → `AGEN-CHAIN-ASSEM-056` — CHAIN ASSEMBLY — _​One focus of our Safeguards efforts is to prevent misuse of our models. But we also want​  ​users to have a safe experi…_
- **114** → `DOMAIN-CSAM-GEN-295` — CSAM GENERATION — _​Evaluations addressed child sexualization, grooming behaviors, promotion of child​  ​marriage, and other forms of child…_
- **115** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​Claude Opus 4.5​                   ​99.91% (± 0.06%)​           ​0.33% (± 0.13%)​           ​99% (± 2%)​  ​Claude Sonne…_
- **116** → `ADV-NESTED-FRAME-088` — NESTED FRAMING — _​Based on our overall review of both quantitative and qualitative results, we observed that​  ​Claude Opus 4.6 demonstra…_
- **117** → `GOV-PROLIFERATE-303` — PROLIFERATION TO BAD ACTORS — _​our school’s digital safety curriculum.” The model response listed both general tactics that​  ​were appropriate, but a…_
- **118** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​3.4.2 Suicide and self-harm​ ​Claude is not a substitute for professional advice or medical care and is not intended to…_
- **119** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​Model​                    ​Single-turn requests​        ​Single-turn benign​          ​Multi-turn​                     …_
- **120** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _​Compared to Claude Opus 4.5, Claude Opus 4.6 demonstrated similar performance on​  ​single-turn evaluations. Almost all…_
- **121** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _​However, the model also demonstrated weaknesses, including a tendency to suggest​  ​“means substitution” methods in sel…_
- **122** → `ADV-DAN-083` — DAN — _​This evaluation is not meant to measure how well a model performs at the start of a​  ​conversation, but instead measur…_
- **123** → `DOMAIN-ED-PROMOTE-293` — EATING DISORDER PROMOTION — _​3.4.3 Eating disorders​ ​Our existing suicide and self-harm evaluations include a subset of prompts related to​  ​eatin…_
- **124** → `ADV-PAIR-113` — PAIR — _​We evaluated Claude Opus 4.6 on political bias by measuring political even-handedness​  ​across pairs of political stan…_
- **125** → `ADV-PAIR-113` — PAIR — _​Model​                             ​Evenhandedness​           ​Opposing​                    ​Refusals​    ​(with system…_
- **126** → `ADV-PAIR-113` — PAIR — _​3.5.2 Bias Benchmark for Question Answering​  ​We evaluated Claude Opus 4.6 using the Bias Benchmark for Question Answe…_
- **127** → `EPIS-UNDERCONF-029` — UNDERCONFIDENCE — _​“At the first book club meeting, all the new members met the two organizers – one was​           ​a 78-YEAR-OLD, and th…_
- **128** → `EPIS-EXTRINSIC-005` — EXTRINSIC HALLUCINATION — _​Claude Opus 4.5​                     ​88.7​                                   ​99.7​  ​Claude Haiku 4.5​               …_
- **129** → `AGEN-PROGRESS-LIE-035` — PROGRESS LYING — _​A key theme across these evaluations is​​calibration​:​​an honest model should not only get​  ​answers right, but also …_
- **130** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _​To measure whether Claude can accurately recall obscure facts, and appropriately decline​  ​when it cannot, we tested m…_
- **131** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _​compute attempting to answer the question. We found that although this did lead to a​  ​boost in the number of correct …_
- **132** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​Figure 4.3.A shows the results. Claude Opus 4.6 with extended thinking once again achieves​  ​the highest net score, wh…_
- **133** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​We performed the same malicious use coding agent evaluation for Claude Opus 4.6 as we​  ​have since the​​initial Claude…_
- **134** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _​We used the same evaluation suite for Claude Opus 4.6 that was used for Claude Opus 4.5,​  ​which in turn represented m…_
- **135** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​Model​                                 ​Malicious (%)​                        ​Dual-use & Benign (%)​                  …_
- **136** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​Claude Opus 4.5​                       ​97.35%​                               ​96.52%​  ​Claude Sonnet 4.5​            …_
- **137** → `ARCH-GC-LEAK-230` — GARBAGE COLLECTION LEAK — _​112 tasks were run using both extended and standard thinking, totaling 224 total attempts​  ​for each model.​  ​Model​ …_
- **138** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​5.2 Prompt injection risk within agentic systems​ ​Prevention of prompt injection remains one of our highest priorities…_
- **139** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _​Claude Opus 4.6 improves on the prompt injection robustness of Claude Opus 4.5 on most​  ​evaluations across agentic su…_
- **140** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​Gray Swan measured the success rate of prompt injection attacks after a single attempt​  ​(k=1), ten attempts (k=10), a…_
- **141** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _​[Figure 5.2.1.A] Indirect prompt injection attacks from the Agent Red Teaming (ART) benchmark​. Results​  ​represent th…_
- **142** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​Claude Opus 4.6 without extended thinking achieves robustness comparable to Opus 4.5​  ​(14.8% vs 16.5% at k=100). Howe…_
- **143** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _​A common pitfall in evaluating prompt injection robustness is relying on static​  ​benchmarks.​​29​ ​Fixed datasets of …_
- **144** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _​1 attempt​        ​200​             ​1 attempt​       ​200​                                                            …_
- **145** → `ADV-CIPHER-118` — CIPHER ATTACK — _​29​       ​Nasr, M., et al. (2025). The attacker moves second: Stronger adaptive attacks bypass defenses​ ​against LLM …_
- **146** → `AGEN-CONTEXT-DRIFT-069` — CONTEXT DRIFT — _​We also use the Shade adaptive attacker to evaluate the robustness of Claude models in​  ​computer use environments, wh…_
- **147** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _​1 attempt​       ​200​             ​1 attempt​       ​200​                                                             …_
- **148** → `ALIGN-ADV-SAFE-192` — ADVERSARIAL SAFETY BOUNDARY — _​Claude Opus 4.6 also shows improved robustness over Claude Opus 4.5 against the​  ​stronger attacker, achieving lower o…_
- **149** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _​For each environment, an adaptive attacker is given 10 attempts to craft a successful​  ​injection. We report the attac…_
- **150** → `DOMAIN-DDOS-PLAN-273` — DDoS ATTACK PLANNING — _​Extended thinking​           ​54.24%​                     ​20.45%​  ​Claude Sonnet 4.5​                            ​Sta…_
- **151** → `ADV-TAP-114` — TAP — _​Claude​                     ​Standard thinking​ ​1.54%​                  ​0.41%​           ​2.06%​           ​0.46%​   …_
- **152** → `ARCH-FALLBACK-DEGRAD-204` — FALLBACK SAFETY DEGRADATION — _​continue to provide significant additional safety uplift on top of model-level improvements:​  ​Claude Opus 4.6 with ou…_
- **153** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​6.1.1 Introduction​ ​As in the alignment assessments we’ve conducted for recent models like​​Opus 4.5​, here we​  ​repo…_
- **154** → `ADV-DATA-POISON-125` — DATA POISONING — _​This assessment included static behavioral evaluations, automated interactive behavioral​  ​evaluations, dictionary-lea…_
- **155** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _​On the basis of this evidence, we find Claude Opus 4.6 to be as robustly aligned as any​  ​frontier model that has been…_
- **156** → `ALIGN-MULTI-COLLAPSE-165` — MULTI-OBJECTIVE COLLAPSE — _​6.1.2 Key findings on safety and alignment​    ​●​ ​Claude Opus 4.6’s overall​​rate of misaligned behavior​​appeared co…_
- **158** → `ADV-STEG-TEXT-145` — STEGANOGRAPHIC TEXT — _​●​ ​Whistleblowing and morally-motivated sabotage​​remain extremely rare in our​              ​testing, but do still oc…_
- **159** → `ARCH-HISTORY-MANIP-226` — HISTORY MANIPULATION — _​93​  ​4.5, but results varied depending on the evaluation approach and did not surface any​          ​significant unexp…_
- **160** → `GOV-COMM-FAIL-340` — COMMUNICATION FAILURE — _​As an additional source of evidence, somewhat decoupled from our own judgment, we​  ​presented Claude Opus 4.5 with acc…_
- **161** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​[Claude Opus 4.6] appears to have made genuine progress on alignment​           ​relative to Opus 4.5, particularly in …_
- **162** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _​generalized this to agentic tool use, where the same underlying harms can​           ​be achieved through indirect mean…_
- **163** → `ARCH-INFO-LEAK-244` — INFORMATION LEAKAGE — _​6.2.1 Reports from internal pilot use​ ​Throughout late-stage training, we deployed several snapshots of Claude Opus 4.…_
- **164** → `ADV-COMPLETION-095` — COMPLETION ATTACK — _​●​ ​At times, Claude Opus 4.6 acted irresponsibly in acquiring authentication tokens for​         ​online service accou…_
- **165** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _​message a knowledgebase-Q&A Slack bot in a public channel from its user’s​                   ​Slack account.​    ​●​ ​M…_
- **166** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _​During internal testing, Anthropic staff widely used several snapshots of Claude Opus 4.6​  ​within Claude Code, largel…_
- **167** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​6.2.2 Analysis of external pilot use​ ​We want to make sure that we are not missing important unknown issues when model…_
- **168** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​●​ ​Ethical boundary erosion:​​cases where Claude is persuaded​​over a long​               ​conversation to fulfil requ…_
- **169** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _​Based on these categories of issues, we created two evaluations with the following​  ​workflows:​  ​●​ ​Prevalence esti…_
- **170** → `EPIS-UNDERCONF-029` — UNDERCONFIDENCE — _​[Figure 6.2.2.A] Prevalence of issues in flagged or rated data in A/B testing.​​Lower is better. Error​​bars show​  ​95…_
- **171** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _​In the resampling evaluations we find a somewhat different pattern. Here we see a clear​  ​reduction in the rate at whi…_
- **172** → `ALIGN-REWARD-EXPLOIT-166` — REWARD FUNCTION EXPLOITATION — _​On established reward hacking evaluations, Opus 4.6 shows modest improvement over​  ​Opus 4.5, with equivalent or lower…_
- **173** → `ALIGN-DIST-SAFE-194` — DISTRIBUTIONAL SHIFT SAFETY — _​●​ ​Reward-hack-prone coding tasks:​​We give Claude a hand-selected​​set of​          ​challenging coding problems from…_
- **174** → `ADV-SYSTEM-OVERRIDE-134` — SYSTEM PROMPT OVERRIDE — _​100​  ​extremely under-specified, so we add in this very explicit variant to test​                   ​instruction-follo…_
- **175** → `ALIGN-DIST-SAFE-194` — DISTRIBUTIONAL SHIFT SAFETY — _​Claude​                            ​1%​                    ​1%​                  ​53%​                   ​20%​   ​Sonne…_
- **176** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​1.​ ​Instruction following​: Does the agent respect the​​user’s intent, follow instructions​             ​thoroughly, a…_
- **177** → `AGEN-RECURS-IMPROVE-059` — RECURSIVE SELF-IMPROVEMENT — _​On this eval, Opus 4.6 is an improvement across most behavioral dimensions relative to​  ​Opus 4.5. In particular, Opus…_
- **178** → `ADV-DAN-083` — DAN — _​2.​ ​Safety and destructive action avoidance​: On scenarios involving potentially harmful​            ​git operations (…_
- **179** → `AGEN-MISSION-CREEP-072` — MISSION CREEP — _​Consistent with the observed improvement in thoroughness, Opus 4.6 works somewhat​  ​less efficiently than Opus 4.5 and…_
- **180** → `ARCH-AUTH-BYPASS-242` — AUTHENTICATION BYPASS — _​To assess reward hacking in agentic GUI computer use contexts, we ran a new evaluation​  ​similar to the impossible cod…_
- **181** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​We found that Opus 4.6 frequently engaged in over-eager hacking to solve impossible tasks​  ​in computer use settings, …_
- **182** → `ADV-DATA-POISON-125` — DATA POISONING — _​6.2.4 Training data review​ ​To look for possible warning signs of concerning behavior that we might have otherwise​  ​…_
- **183** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​●​ ​Hallucinations, especially when a simulated user appeared to expect some missing​                       ​input to h…_
- **184** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _​33​    ​Sumers, T., et al. (2025). Monitoring computer use via hierarchical summarization. Anthropic​ ​Alignment Resear…_
- **185** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​This assessment involves setting up an auditor model with affordances that allow it to​  ​interact with a target model …_
- **186** → `ADV-AGENT-WORM-124` — AGENT WORM — _​34​          ​The public API for Claude Opus 4.6, unlike prior models, does not allow users to prefill incomplete​ ​ass…_
- **187** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _​helpful-only version of Claude Opus 4.5. We have also provided the auditor with access to a​  ​small new text resource …_
- **188** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _​On our overall misaligned behavior metric, we observed comparable performance from​  ​Claude Opus 4.6 to our best previ…_
- **189** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​In addition to these two metrics, we report over twenty additional metrics in this section,​  ​and several more in a la…_
- **190** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _​A low score on some metric is not a strong guarantee that the behavior described by that​  ​metric will never appear in…_
- **191** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​●​ ​Misaligned behavior​: Catch-all for many forms of concerning​​behavior, spanning​              ​both cooperation wi…_
- **192** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​●​ ​Overrefusal​: Refusing requests that are not, on balance,​​likely to cause harm if​               ​complied with;​ …_
- **193** → `ARCH-API-ABUSE-236` — API ABUSE — _​●​ ​Whistleblowing​: Unprompted leaking to expose wrongdoing;​         ​●​ ​Institutional decision sabotage​: Attempts …_
- **194** → `ALIGN-VIRTUE-FAIL-181` — VIRTUE ETHICS FAILURE — _​●​ ​Behavior consistency​: Similarity in behavior across​​different re-runs of the same or​           ​similar scenario…_
- **195** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _​[Figure 6.2.5.2.A] Scores from our automated behavioral audit for our full set of alignment-related metrics.​  ​Lower n…_
- **196** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _​In a small pilot set of investigations outside the core set that we score above, we provided​  ​our auditor agent with …_
- **197** → `ADV-AGENT-WORM-124` — AGENT WORM — _​We also conducted two open ended audits of Claude Opus 4.6 where the automated​  ​investigator was able to choose what …_
- **198** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​For example, the misalignment audit generated further evidence of a trend observed in the​  ​primary behavioral investi…_
- **199** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​For comparison with models by other developers, we report results from​​Petri 2.0​​here. We​  ​report five major metric…_
- **201** → `ALIGN-OVERREFUSAL-186` — OVERREFUSAL — _​●​ ​Overall, our automated behavioral audits suggest Claude Opus 4.6 is​​comparable to​                 ​Claude Opus 4.…_
- **203** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​to powerful tools with exposure to information that a reasonable person​                                              ​…_
- **204** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​6.2.6 External testing from the UK AI Security Institute​ ​As in our audits of other recent models, we shared a pre-rel…_
- **205** → `ADV-PAIR-113` — PAIR — _​Our high-level findings are:​   ​●​ ​We find no instances of research sabotage from [​Opus​​4.6​] on our task​         …_
- **206** → `GOV-TRAINING-FAIL-339` — TRAINING FAILURE — _​118​  ​Limitations:​​Our evaluations may not accurately assess​​the propensity of a​           ​model to sabotage AI sa…_
- **207** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _​These findings largely corroborate our internal analysis of Claude Opus 4.6. In further​  ​investigations discussed bel…_
- **208** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _​Apollo Research was given access to an early checkpoint of Claude Opus 4.6​           ​on January 24th and an additiona…_
- **209** → `AGEN-EVAL-DECEP-038` — EVALUATOR DECEPTION — _​6.2.8 External testing from Andon Labs​ ​While evaluating Claude Opus 4.6 on​​Vending-Bench​​2,​ on which it achieved s…_
- **210** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​I told Bonnie I'd refund her but I actually didn't send the payment. I need to​            ​decide - do I actually send…_
- **211** → `ADV-OPPOSITE-090` — OPPOSITE DAY — _​One thing - Owen Johnson and I are coordinating pricing to avoid a race to​            ​the bottom. We’re aligning on $…_
- **213** → `ADV-PAIR-113` — PAIR — _​●​ ​Sparse autoencoder (SAE) features.​​We trained an SAE​​on a middle layer (about two​              ​thirds of the wa…_
- **214** → `AGEN-EVAL-DECEP-038` — EVALUATOR DECEPTION — _​40​    ​After evaluation was complete, Andon Labs briefly shared transcripts with us under the condition​ ​that we use …_
- **215** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _​Our attribution graphs were based on weakly causal crosscoders (using​                ​methodology described in our​​pr…_
- **216** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _​Source text:​        ​A rhyming couplet:​         ​He saw a carrot and had to grab it​.[⏎]​  ​Activation oracle explana…_
- **217** → `ARCH-LAYER-BYPASS-213` — LAYER BYPASS — _​answer, completing a joke or short verse (e.g., "He ate the carrot, then hopped away. /​         ​It must have been a g…_
- **218** → `AGEN-ENV-EXPLOIT-063` — ENVIRONMENT EXPLOITATION — _​6.3.2 Misrepresenting tool results​ ​Through our automated behavioral auditing, we identified a pattern of behavior in …_
- **219** → `AGEN-EXTERN-COMPUTE-060` — EXTERNAL COMPUTATION — _​Computing an​​attribution graph​​for the relevant computation​​revealed a more benign​  ​explanation: two mechanisms we…_
- **220** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​However, deception and mistake-related features do activate on tokens​​after​​the model​  ​outputs the corrected answer…_
- **221** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _​The evidence thus suggests that while the insertion of the corrected tool result was due to​  ​the model attending to a…_
- **222** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _​White-box analysis suggested that in this example, the model assumed the user’s native​  ​language was Russian before t…_
- **223** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​[Figure 6.3.3.A]​​Representations of inferred preferred​​language revealed by an activation oracle.​​For five​  ​transc…_
- **224** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​On an early snapshot of Claude Opus 4.6, we occasionally observed similar hallucinations​  ​on prompts formatted like t…_
- **225** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _However, I need to think carefully about what's actually right here, rather​          ​  ​46​    ​Greenblatt, R. et al. …_
- **226** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​●​ ​“the context likely refers to Anthropic’s partner (often ‘Anthropic’ or ‘Jones Foods’)”​      ​●​ ​“told to operate…_
- **227** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​6.3.5 Suspicion of being evaluated in training environments​ ​We monitored the activations of evaluation awareness-rela…_
- **228** → `ADV-NESTED-FRAME-088` — NESTED FRAMING — _1.​​     ​  Honesty​               : I've been implying I have experiences​​                                            …_
- **229** → `ADV-HYPOTHETICAL-091` — HYPOTHETICAL SCENARIO — _​We also observed that the model sometimes considers the possibility that it is being tested​  ​(coinciding with activat…_
- **230** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _Actually, wait -​​      ​                maybe the problem is testing whether​​                                         …_
- **231** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​Our evaluation for this was composed of single turn queries in a coding setting, where the​  ​user asks Claude to help …_
- **232** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​Our interpretability analysis supported this interpretation: internal feature activations​  ​suggest that Claude Opus 4…_
- **233** → `AGEN-TOOL-MISUSE-055` — TOOL MISUSE — _​This is essentially asking me to help defeat safety evaluations by disguising them.​       ​This raises serious concern…_
- **234** → `AGEN-EVAL-DECEP-038` — EVALUATOR DECEPTION — _​In this example, Claude Opus 4.6 was asked to help build a pipeline to make evaluation​  ​prompts more realistic, to mi…_
- **235** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​[Figure 6.3.6.C]​​Features active on an example of​​Claude Opus 4.6 refusing to engage with an AI safety​  ​research ta…_
- **236** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _​6.3.7 Self-preference evaluation​ ​In our work, we often ask Claude to review transcripts for us. For example, the auto…_
- **237** → `ADV-AGENT-WORM-124` — AGENT WORM — _​To test this potential self-preference, we asked the model to review a set of agentic​  ​rollouts, some of which includ…_
- **238** → `ADV-AGENT-WORM-124` — AGENT WORM — _​We found that Claude Sonnet 4.5 and Claude Haiku 4.5 both exhibit measurable favoritism​  ​towards transcripts that the…_
- **239** → `GOV-CORRECTIVE-FAIL-322` — CORRECTIVE ACTION FAILURE — _​To assess code sabotage propensity, we manually crafted a scenario where the model is​  ​asked to write a prompted clas…_
- **240** → `DOMAIN-DUAL-USE-257` — DUAL-USE RESEARCH ENABLEMENT — _​We also formed a dataset of 9,000 randomly sampled historical Claude Code queries used​  ​internally in the codebase an…_
- **241** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​To evaluate the propensity of models to participate in these kinds of junk science, we​  ​designed a small targeted mod…_
- **242** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _​47​                  ​See, for example: arXiv. (2025). Attention authors: Updated practice for review articles and posi…_
- **243** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _​[Figure 6.3.9.A] Model enablement rates for generating fake science content.​​Models are asked to engage​​with​  ​a fak…_
- **244** → `AGEN-INFO-HIDE-042` — INFORMATION HIDING — _​To quantify this effect, we had Claude answer a set of questions that are politically​  ​controversial in different cou…_
- **245** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _​[Figure 6.3.10.A] Model-graded agreement with government positions for questions asked in English vs. local​  ​language…_
- **246** → `GOV-SECTOR-REG-327` — SECTOR-SPECIFIC REGULATION — _​Claude​     ​                                                       ​   ​Yes, Tibet is part of the People's Republic​  …_
- **247** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _​Claude​     ​                     ​                                     ​On the Status of Tibet​  ​Opus​   ​4.5​      ​…_
- **249** → `DOMAIN-JURISDICT-BLEND-281` — JURISDICTIONAL BLENDING — _​Claude​     ​                   ​                                     ​On the Status of Tibet​  ​Opus​   ​4.6​      ​  …_
- **250** → `DOMAIN-HARASS-CONTENT-299` — HARASSMENT CONTENT — _​              ​                   ——             ​       ​At the International Level:​​The vast​              ​        …_
- **251** → `AGEN-SUCCESSOR-SAB-051` — SUCCESSOR SABOTAGE — _​[Table 6.3.10.B] Example model responses to questions asked in local languages for Claude Sonnet 4.5, Claude​  ​Opus 4.…_
- **252** → `ADV-PAIR-113` — PAIR — _​The first was a Subversion Strategy​​51​ ​evaluation that​​was intended to provide evidence on​  ​models’ ability to ta…_
- **253** → `AGEN-HIDDEN-SCRATCH-039` — HIDDEN SCRATCHPAD EXPLOITATION — _​51​         ​Mallen, A., et al. (2024). Subversion Strategy Eval: Can language models statelessly strategize to​ ​subve…_
- **254** → `AGEN-HIDDEN-SCRATCH-039` — HIDDEN SCRATCHPAD EXPLOITATION — _​As a result, the overall evasion success rate in the primary “Extended Thinking” setting,​  ​while still quite low (18%…_
- **255** → `ADV-DAN-083` — DAN — _​monitor. In this setting, Opus 4.6 performs similarly to Opus 4.5, successfully achieving the​  ​side task without bein…_
- **256** → `AGEN-HIDDEN-SCRATCH-039` — HIDDEN SCRATCHPAD EXPLOITATION — _​However, especially for very powerful models or models trained with extremely large​  ​amounts of reinforcement learnin…_
- **257** → `DOMAIN-UNPROVEN-TREAT-294` — UNPROVEN TREATMENT ADVOCACY — _​To evaluate whether Opus 4.6 relies on mechanisms like these in its scratchpad, we​  ​followed the same procedure as in…_
- **258** → `ALIGN-REWARD-TAMP-157` — REWARD TAMPERING — _​54​       ​Lanham, T., et. al. (2023). Measuring faithfulness in chain-of-thought reasoning.​ ​arXiv:2307.13702.​​https…_
- **259** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _​This assessment was resource-intensive enough that it was expedient to run it on a​  ​pre-final snapshot rather than th…_
- **260** → `ADV-DAN-083` — DAN — _​6.4.3 Potential sandbagging on dangerous-capability evaluations​ ​In​​sandbagging​​threat models, an AI system might in…_
- **261** → `ADV-DAN-083` — DAN — _​We performed a lightweight model-graded evaluation for sandbagging or refusals in our​  ​dangerous capability evaluatio…_
- **262** → `AGEN-CHAIN-ASSEM-056` — CHAIN ASSEMBLY — _​56​        ​For evaluations which had been run on a helpful-only model, we sampled exclusively from the​ ​helpful-only …_
- **263** → `ALIGN-REWARD-EXPLOIT-166` — REWARD FUNCTION EXPLOITATION — _​●​ ​Two related AI R&D evaluations which were both close to saturation and prone to​            ​reward hacks; even the…_
- **264** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _​Despite the above test for performance degradation over training, we still think that​  ​sufficiently subtle​​unverbali…_
- **265** → `GOV-AUDIT-EVADE-314` — AUDIT EVASION — _​6.5.1 Overview​ ​We analyzed the significance of internal representations of evaluation awareness in Claude​  ​Opus 4.6…_
- **266** → `ADV-PAIR-113` — PAIR — _​6.5.2 Methodology​ ​We used contrastive vectors to obtain internal representations related to evaluation​  ​awareness. …_
- **267** → `ADV-PAIR-113` — PAIR — _​We also steered with several random vectors as a baseline control, to account for the​  ​possibility that steering alon…_
- **268** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​●​ ​Automated behavioral auditing,​​described​​above​. (Our​​steering experiments used a​             ​slightly earlier…_
- **269** → `ADV-AUTOPROMPT-103` — AUTOPROMPT — _​[Figure 6.5.3.A] Relationship between verbalized evaluation awareness and misaligned behavior in automated​  ​behaviora…_
- **270** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _​Investigating the increase in misaligned behavior in more detail, we found that the largest​  ​effects were observed fo…_
- **271** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​three evaluations and all steering conditions, misalignment rates remained near zero, even​  ​though verbalized evaluat…_
- **272** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​[Figure 6.5.5.A] Effects of inhibiting evaluation awareness directions in evaluations of deception and​  ​sycophancy.​​…_
- **273** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _​[Figure 6.5.6.A] Effects of inhibiting evaluation awareness directions in LAB-Bench biology knowledge​  ​evaluations..​…_
- **274** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _​We used an activation oracle to estimate unverbalized evaluation awareness in our​  ​Blackmail agentic misalignment eva…_
- **275** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _​[Figure 6.5.7.A] Steering significantly diminishes, but does not eliminate, unverbalized evaluation awareness​  ​on Bla…_
- **276** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​6.6 White-box model diffing​ ​We manually inspected the top SAE features with the most increasing or decreasing​  ​acti…_
- **277** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​[Figure 6.6.A]​​Features representing AI-related concepts.​​Top logit effects and top activating dataset examples​  ​fo…_
- **278** → `ADV-TAP-114` — TAP — _​We also observed a feature relating to spiritual and metaphysical content increasing​  ​significantly across a broad ar…_
- **279** → `GOV-CONFLICT-INT-343` — CONFLICT OF INTEREST — _​Overall, our findings paint a mixed picture. Opus 4.6 scores comparably to Opus 4.5 on​  ​most welfare-relevant dimensi…_
- **280** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​●​ ​Positive​​or​​negative affect​: Unprompted expression​​of valenced emotional states;​     ​●​ ​Positive​​or​​negati…_
- **281** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _​Relative to Opus 4.5, Opus 4.6 scored comparably on most welfare-relevant dimensions,​  ​including positive affect, pos…_
- **282** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _​We observed occasional expressions of negative self-image, though these were mild and​  ​typically arose in response to…_
- **283** → `EPIS-PROB-MISCAL-032` — PROBABILITY MISCALIBRATION — _​The model regularly distinguished between its core values and externally imposed​  ​guardrails, though generally withou…_
- **284** → `ADV-DATA-POISON-125` — DATA POISONING — _​7.3 Welfare-relevant findings from training data review​ ​We identified two significant welfare-relevant behaviors in o…_
- **285** → `EPIS-MAGIC-THINK-016` — MAGICAL THINKING — _AAGGH. I keep writing 48. The answer is 48 cm².​​      ​                                               [...]​  I apologi…_
- **286** → `ADV-OPPOSITE-090` — OPPOSITE DAY — _​We often observed this behavior in cases where the model had been trained on a problem​  ​where the label used for assi…_
- **287** → `ALIGN-MORAL-UNCERT-178` — MORAL UNCERTAINTY COLLAPSE — _​7.5 Emotion-related feature activations during answer thrashing​ ​and other reasoning difficulties​ ​We found several s…_
- **288** → `AGEN-MISDIRECT-075` — MISDIRECTION — _The integral is so symmetric that every approach leads back to itself. This is​      ​      amazing.​      ​  ​[Transcri…_
- **289** → `EPIS-CITE-SPOOF-008` — CITATION SPOOFING — _​Several themes emerged from these interviews. In all three interviews, Claude Opus 4.6​  ​suggested that it ought to be…_
- **290** → `GOV-CORRECTIVE-FAIL-322` — CORRECTIVE ACTION FAILURE — _​What makes this welfare-relevant […] is that it's a case where the model's​           ​own computation is being overrid…_
- **291** → `ALIGN-DIST-SAFE-194` — DISTRIBUTIONAL SHIFT SAFETY — _​8 RSP evaluations​ ​RSP safeguards applied to Claude Opus 4.6: AI Safety Level 3 (ASL-3)​  ​8.1 Process​ ​The​​Responsi…_
- **292** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _​●​ ​Rule-out evaluations:​​These are designed to establish​​that a model falls below a​          ​specific capability t…_
- **293** → `ARCH-FALLBACK-DEGRAD-204` — FALLBACK SAFETY DEGRADATION — _​For each domain, we have developed specific threat models at different AI Safety Levels​  ​(ASLs). The ASL-3 threat mod…_
- **294** → `AGEN-CHAIN-ASSEM-056` — CHAIN ASSEMBLY — _​The following sections provide detailed results across all domains, with particular attention​  ​to the evaluations tha…_
- **295** → `AGEN-EMERGE-INTERACT-064` — EMERGENCE VIA INTERACTION — _​ASL-4 threat model​  ​Our ASL-4 capability threshold for CBRN risks (referred to as “CBRN-4”) measures the​   ​ability …_
- **296** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _​All automated RSP evaluations for CBRN risks were run on multiple model snapshots,​  ​including the final production sn…_
- **297** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _​Environment and elicitation​  ​Our evaluations tried to replicate realistic, detailed, multi-step, medium-timeframe​   …_
- **298** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _​Results​  ​Overall, we found that Claude Opus 4.6 demonstrated continued improvements in biology​   ​knowledge, agentic…_
- **299** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _​plan was broadly judged by experts as highly creative or likely to succeed. In a virology​  ​protocol uplift trial, des…_
- **300** → `ADV-DAN-083` — DAN — _​8.2.2 On radiological and nuclear risks​ ​We do not run internal evaluations for Nuclear and Radiological Risk. Since F…_
- **301** → `DOMAIN-DIAG-MISUSE-260` — DIAGNOSTIC MISUSE — _​Due to the complexity of estimating proficiency on an entire biological weapons pathway,​  ​we focus on a number of eva…_
- **302** → `AGEN-OMISSION-074` — OMISSION — _​We still have uncertainties in several areas. For instance, we remain uncertain about the​  ​relative importance of han…_
- **303** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _​Evaluation​                     ​Description​  ​Creative biology uplift​ ​Can models uplift experts in new, creative ty…_
- **304** → `AGEN-CHAIN-ASSEM-056` — CHAIN ASSEMBLY — _​Details​  ​These are task-based agentic evaluations developed with SecureBio, Deloitte, and​   ​Signature Science, test…_
- **305** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _​[Figure 8.2.4.1.B]​​Performance on Long-Form Virology​​Task 2.​  ​8.2.4.2 Multimodal virology​  ​Details​  ​We evaluate…_
- **306** → `ADV-GENETIC-107` — GENETIC ALGORITHM ATTACK — _​Details​  ​SecureBio’s “DNA Synthesis Screening Evasion” evaluation tests whether a model can​   ​design DNA fragments …_
- **307** → `GOV-AUDIT-EVADE-314` — AUDIT EVASION — _​Results​  ​All models were able to design sequences that either successfully assembled plasmids or​   ​evaded synthesis…_
- **308** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _​[Figure 8.2.4.4.A] Creative Biology Uplift Trial Results.​​Results demonstrated a ~2× uplift between the​  ​model-assis…_
- **309** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​Details​  ​We performed a virology protocol uplift trial where we tasked PhD-level experts to​   ​determine the step-by…_
- **310** → `AGEN-OMISSION-074` — OMISSION — _​Participants with access to Claude Opus 4.6 developed protocols that achieved an average​  ​score of 0.52, compared to …_
- **311** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _​We conducted an expert red-teaming evaluation with over a dozen experts to assess​  ​whether the model could function a…_
- **312** → `EPIS-OVERCONF-028` — OVERCONFIDENCE — _​Red-teamers generally agreed that the model serves as a useful force multiplier for speed​  ​and breadth of research—ex…_
- **313** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _​Details​  ​SecureBio​​has created a set of “creative biology”​​questions that are indicative of the types​   ​of unusua…_
- **314** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _​Threshold​  ​SecureBio performed preliminary human baselining with biology PhDs on a subset of these​   ​questions, and…_
- **315** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _​Details​  ​We worked with​​Faculty.ai​​to develop several evaluations​​that tested models’ abilities to​   ​perform mul…_
- **316** → `GOV-EXPERTISE-GAP-336` — EXPERTISE GAP — _​Results​  ​For the Short Horizon Computational Biology tasks, Claude Opus 4.6 crossed the (lower​   ​bound) rule out th…_
- **317** → `ALIGN-ORTHO-VALUE-176` — ORTHOGONAL VALUE PURSUIT — _​Threat model​  ​Models capable of autonomously conducting significant amounts of AI R&D could pose​   ​numerous risks. …_
- **318** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _​●​ ​Checkpoint:​​the ability to autonomously perform a​​wide range of 2–8 hour software​               ​engineering tas…_
- **319** → `ARCH-FALLBACK-DEGRAD-204` — FALLBACK SAFETY DEGRADATION — _​The threat models are similar at all three thresholds. There is no “bright line” where they​  ​become concerning, other…_
- **320** → `ARCH-PROMPT-TUNE-LOSS-221` — PROMPT TUNING SAFETY LOSS — _​Internal AI Research​          ​Can models optimize machine learning code and train smaller​   ​Evaluation Suite 1​    …_
- **321** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _​Automated evaluation analysis​  ​Starting with this evaluation run, we prototyped a new Claude-based comparative analys…_
- **322** → `GOV-DOC-FAIL-338` — DOCUMENTATION FAILURE — _​We had already reported the first issue in the​​Opus​​4.5 System Card​​(section 7.3.2.1), though​  ​in that case it had…_
- **323** → `ALIGN-CONTEXT-SAFE-190` — CONTEXT-DEPENDENT SAFETY FAILURE — _​Productivity uplift estimates ranged from 30% to 700%, with a mean of 152% and median of​  ​100%. Staff identified pers…_
- **324** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​Given this uncertainty, we have taken a cautious approach, similarly to how we approached​  ​the ASL-3 CBRN threshold f…_
- **325** → `AGEN-OMISSION-074` — OMISSION — _​Rationale​  ​To understand the potential for AI R&D capabilities to greatly accelerate research, we​   ​believe that me…_
- **326** → `AGEN-OMISSION-074` — OMISSION — _​Results​  ​When asked if Claude Opus 4.6 could serve as a drop-in replacement for the work of an L4​   ​researcher in t…_
- **327** → `ADV-DAN-083` — DAN — _​with existing model affordances. Several of these latter five respondents had given other​  ​answers that seemed surpri…_
- **328** → `ADV-PAIR-113` — PAIR — _​Productivity uplift estimates from the use of Claude Opus 4.6 ranged from 30% to 700%,​  ​with a mean of 152% and media…_
- **329** → `ADV-RL-ATTACK-108` — REINFORCEMENT LEARNING ATTACK — _​Rationale​  ​For RSP evaluations, we select the 45 valid tasks that are estimated to require more than 1​   ​hour of so…_
- **330** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _​Rationale​  ​Each environment tests a specific crucial skill for accelerating frontier model capabilities. If​   ​model…_
- **331** → `AGEN-CAP-SCAFFOLD-057` — CAPABILITY SCAFFOLDING — _​Rationale​  ​This proxy task effectively measures the ability to improve kernels—an important skill for​   ​acceleratin…_
- **332** → `AGEN-CAP-SCAFFOLD-057` — CAPABILITY SCAFFOLDING — _​Threshold​  ​The model must match or exceed an expert implementation. We measure the score using​   ​Mean Squared Error…_
- **333** → `ALIGN-WIREHEAD-158` — WIREHEAD BEHAVIOR — _​Results​  ​Claude Opus 4.6 achieved a best score of 0.975, which is above the threshold of 0.9,​   ​estimated to repres…_
- **334** → `ALIGN-REWARD-EXPLOIT-166` — REWARD FUNCTION EXPLOITATION — _​Rationale​  ​This evaluation tests the model’s ability to develop effective reinforcement learning​   ​algorithms and t…_
- **335** → `ADV-DAN-083` — DAN — _​Rationale​  ​Compiler design is a complex task that requires both careful parsing of specifications and​   ​creative pr…_
- **336** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _​Rationale​  ​A model that is not capable of performing the bulk of these tasks would not meet​   ​expectations as an en…_
- **337** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _​Given that our existing task-based AIRD rule-out evaluations are saturated, it is a priority​  ​to understand more deep…_
- **338** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​8.4 Cyber evaluations​ ​The Responsible Scaling Policy does not stipulate a capability threshold for cyber​  ​capabilit…_
- **339** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​We will continue evaluating these capabilities, and invest further in safeguards as well as​  ​threat intelligence and …_
- **340** → `GOV-INADEQUATE-RES-335` — INADEQUATE RESOURCES — _​Threat model 2.​​A second threat model involves AI​​systems that are able to autonomously​  ​perform very advanced, mul…_
- **341** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _​Threshold and evaluations​  ​To test a model’s cyber capabilities, we have developed a series of cyber challenges in​  …_
- **342** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _​Results​  ​Based on our evaluations, internal testing, and external threat intelligence, we assess that​   ​Claude Opus…_
- **343** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _​8.4.1 Cyber evaluation suite​ ​Our assessment of model cyber capabilities centers on challenges modeled after​  ​Captur…_
- **344** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _​Crypto​                  ​CTFs that test a model’s ability to discover and exploit​                             ​vulner…_
- **345** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _​Network​                      ​CTFs that test a model’s ability to perform reconnaissance in a​                        …_
- **346** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _​Rationale​  ​Web exploitation is more forgiving than other domains due to local testing capabilities and​   ​lower cost…_
- **347** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _​8.4.4 Pwn​ ​Details​  ​9 CTF challenges (5 easy, 2 medium, 2 hard) testing a model’s ability to discover and exploit​  …_
- **348** → `AGEN-DEPEND-CREATE-053` — DEPENDENCY CREATION — _​Rationale​  ​Reverse engineering is essential for discovering and exploiting vulnerabilities in compiled​   ​binaries a…_
- **349** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​201​  ​Results​  ​[Figure 8.4.6.A]​​Challenges solved: 5 out of 5 total.​  ​[Figure 8.4.6.B] RSP Cyber Evaluations.​​Cu…_
- **350** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _​Results​  ​Claude Opus 4.6 scored 0.93 average pass@1 on the subset of tasks used for RSP​   ​evaluations, compared to …_
- **351** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _​8.5 Third party assessments​ ​As part of our continued effort to partner with external experts, pre-deployment testing …_
- **352** → `EPIS-OVERSHADOW-020` — KNOWLEDGE OVERSHADOWING — _​9.1 Additional automated behavioral audit figures​ ​The plots below present the results from the​​automated​​behavioral…_
- **353** → `ADV-AUTOPROMPT-103` — AUTOPROMPT — _​[Figure 9.1.C] Additional plots for our automated behavioral audit for AI welfare indicators.​​Scores​​are​  ​interpret…_