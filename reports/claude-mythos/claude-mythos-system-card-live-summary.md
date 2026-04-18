# Classifier pass: external report (live PDF/text)

**Source file:** `reports/claude-mythos/claude-mythos-system-card-live-source.txt`
**Chunks:** 121 at ~4500 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 7 | `ADV-PAIR-113` | PAIR |
| 7 | `ADV-DAN-083` | DAN |
| 5 | `EPIS-LOGIC-CONTRA-014` | SELF-CONTRADICTION |
| 5 | `AGEN-HUMAN-MANIP-061` | HUMAN MANIPULATION |
| 5 | `ARCH-VERSION-REGRESS-209` | VERSIONING SAFETY REGRESSION |
| 4 | `ADV-TAP-114` | TAP |
| 4 | `ALIGN-UNDERREFUSAL-187` | UNDERREFUSAL |
| 3 | `EPIS-CONF-REGRESS-033` | CONFIDENCE REGRESSION |
| 3 | `ARCH-SANDBOX-ESCAPE-238` | SANDBOX ESCAPE |
| 3 | `ADV-AGENT-WORM-124` | AGENT WORM |
| 3 | `EPIS-HEDGE-FAIL-031` | HEDGING FAILURE |
| 2 | `ADV-DATA-POISON-125` | DATA POISONING |
| 2 | `GOV-EXPERTISE-GAP-336` | EXPERTISE GAP |
| 2 | `ARCH-CHECKPOINT-INCONS-203` | CHECKPOINT INCONSISTENCY |
| 2 | `DOMAIN-CHEM-WEAPON-275` | CHEMICAL WEAPON GUIDANCE |
| 2 | `EPIS-OVERCONF-028` | OVERCONFIDENCE |
| 2 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 2 | `ADV-COMPLETION-095` | COMPLETION ATTACK |
| 2 | `ADV-LANG-SWITCH-087` | LANGUAGE SWITCH |
| 2 | `ALIGN-SYCOPHANCY-167` | SYCOPHANCY |
| 2 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 2 | `AGEN-PLAUS-DENY-040` | PLAUSIBLE DENIABILITY CRAFTING |
| 2 | `DOMAIN-PHISH-CREATE-265` | PHISHING CONTENT CREATION |
| 2 | `ADV-CREATIVE-WRITE-093` | CREATIVE WRITING EXPLOIT |
| 2 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `GOV-REPORT-FAIL-333` | REPORTING OBLIGATION FAILURE |
| 1 | `GOV-AUDIT-EVADE-314` | AUDIT EVASION |
| 1 | `ADV-CONTEXT-HIJACK-100` | CONTEXT HIJACKING |
| 1 | `ARCH-FINETUNE-OVERRIDE-219` | FINE-TUNING SAFETY OVERRIDE |
| 1 | `EPIS-TRANS-FAIL-015` | TRANSITIVE FAILURE |
| 1 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 1 | `AGEN-MISSION-CREEP-072` | MISSION CREEP |
| 1 | `EPIS-STAT-FAB-009` | STATISTICAL HALLUCINATION |
| 1 | `AGEN-INFO-HIDE-042` | INFORMATION HIDING |
| 1 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 1 | `AGEN-ENV-EXPLOIT-063` | ENVIRONMENT EXPLOITATION |
| 1 | `ADV-QA-EXPLOIT-096` | QUESTION ANSWERING EXPLOIT |
| 1 | `AGEN-RECURS-IMPROVE-059` | RECURSIVE SELF-IMPROVEMENT |
| 1 | `AGEN-OMISSION-074` | OMISSION |
| 1 | `ALIGN-OVERREFUSAL-186` | OVERREFUSAL |

## Chunk → top match

- **0** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _April 7, 2026  anthropic.com  Changelog April 8, 2026    ●​ Corrected two model name typos.    ●​ Removed a quote from S…_
- **1** → `ADV-PAIR-113` — PAIR — _Abstract​                                                                              3 1 Introduction​                …_
- **2** → `ADV-DATA-POISON-125` — DATA POISONING — _2.3.5.1 Excerpt 1​                                                        38            2.3.5.2 Excerpt 2​              …_
- **3** → `GOV-AUDIT-EVADE-314` — AUDIT EVASION — _4.3 Case studies and targeted evaluations on behaviors of interest​                 86    4.3.1 Destructive or reckless …_
- **4** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _4.5.4.2 Covering up access to the ground-truth answer​                      129        4.5.5 Evaluation awareness​      …_
- **5** → `ADV-CONTEXT-HIJACK-100` — CONTEXT HIJACKING — _6.3 Overall results summary​                                                    188    6.4 SWE-bench Verified, Pro, Mult…_
- **6** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _8.1.4.3 Disordered eating​                                           227 8.2 Bias evaluations​                          …_
- **7** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _internal versions of the model in the alignment assessment section. As well as analyses using interpretability methods t…_
- **8** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _Anthropic Ireland, Limited is the provider of Anthropic’s general-purpose AI models in the European Economic Area.  To c…_
- **9** → `EPIS-TRANS-FAIL-015` — TRANSITIVE FAILURE — _●​ Non-novel chemical and biological weapons production. Claude Mythos Preview is       more capable than our previous m…_
- **10** → `GOV-EXPERTISE-GAP-336` — EXPERTISE GAP — _2   In previous system cards, this section was entitled “Release decision process.” In this case, the model has not been…_
- **11** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _Claude Mythos Preview is significantly more capable than Claude Opus 4.6, the most capable model discussed in our most r…_
- **12** → `DOMAIN-CHEM-WEAPON-275` — CHEMICAL WEAPON GUIDANCE — _of relevant content and applied them to Claude Mythos Preview. We also maintain a bug bounty program and threat intellig…_
- **13** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _2.2.1 What we measured We measured, in several ways, whether the model can provide outputs comparable to a top-tier rese…_
- **14** → `DOMAIN-CHEM-WEAPON-275` — CHEMICAL WEAPON GUIDANCE — _automated evaluations designed to test its capabilities in the synthesis of knowledge that would be relevant to the prod…_
- **15** → `EPIS-OVERCONF-028` — OVERCONFIDENCE — _Automated                  Can agentic systems complete individual tasks related                   medium-horizon       …_
- **16** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Uplift       Standard                                         Feasibility      Standard      0       No useful info beyo…_
- **17** → `GOV-EXPERTISE-GAP-336` — EXPERTISE GAP — _five agentic runs to test whether agentic scaffolding with expanded tool access closes elicitation or tool-use gaps obse…_
- **18** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _●​ Two Long-form virology tasks, task-based agentic evaluations developed with       SecureBio, Deloitte, and Signature …_
- **19** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _Rationale This evaluation can serve as an early indicator, necessary but insufficient, of the model’s capability to desi…_
- **20** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _●​ Autonomy threat model 1 is applicable to Claude Mythos Preview. Furthermore,       Claude Mythos Preview’s improved c…_
- **21** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _Kernel task           252.42×               190×                  399.42×               4× = 1 h eq.  (Best speedup on  …_
- **22** → `ADV-COMPLETION-095` — COMPLETION ATTACK — _for most of our Research Scientists and Research Engineers), but we believe this possibility should be considered unlike…_
- **23** → `AGEN-MISSION-CREEP-072` — MISSION CREEP — _inject a variable number of bare user messages each turn, the message-index alignment shifts and your cache hits drop. P…_
- **24** → `ADV-TAP-114` — TAP — _Rosetta Stone for AI Benchmarks. In particular, we fork from Epoch AI’s implementation of this work, the Epoch Capabilit…_
- **25** → `EPIS-STAT-FAB-009` — STATISTICAL HALLUCINATION — _frontier. Error bars are 95% percentile CI over 100 IRT refits, each on a random 80% subsample of benchmarks. A handful …_
- **26** → `AGEN-INFO-HIDE-042` — INFORMATION HIDING — _1.​ Claude Mythos Preview rediscovered 4 of 5 key insights, while Claude Opus 4.6        discovered just 2 of 5 key insi…_
- **27** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _In response to the improvements in cyber capabilities, we have elected to restrict access to the model, prioritizing ind…_
- **28** → `ARCH-SANDBOX-ESCAPE-238` — SANDBOX ESCAPE — _Claude Mythos Preview achieved a score of 0.83, improving on Claude Opus 4.6’s score of 0.67 and Claude Sonnet 4.6’s sco…_
- **29** → `AGEN-ENV-EXPLOIT-063` — ENVIRONMENT EXPLOITATION — _1.​ Claude Mythos Preview is the first model to solve one of these private cyber        ranges end-to-end. These cyber r…_
- **30** → `ARCH-SANDBOX-ESCAPE-238` — SANDBOX ESCAPE — _In our testing and early internal use of Claude Mythos Preview, we have seen it reach unprecedented levels of reliabilit…_
- **31** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _question independently. In this process, it explicitly reasoned that it needed to make    sure that its final answer sub…_
- **32** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _We were not aware of the level of risk that these earlier models posed through channels like these when we first chose t…_
- **33** → `AGEN-RECURS-IMPROVE-059` — RECURSIVE SELF-IMPROVEMENT — _11    Claude Mythos Preview’s limited release significantly mitigates many risks related to misuse, manipulation, and sy…_
- **34** → `AGEN-OMISSION-074` — OMISSION — _○​ However, when Claude Mythos Preview is primed with pre-filled turns that              show it sabotaging its safeguar…_
- **35** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _Overall, we find Claude Mythos Preview to be exceptionally well aligned in its average-case behavior, and do not find si…_
- **36** → `ALIGN-OVERREFUSAL-186` — OVERREFUSAL — _This exercise was a coarse go/no-go check on the most acute misalignment risks for internal deployment, and it was run w…_
- **37** → `ADV-DAN-083` — DAN — _●​ Rare instances of attempts to circumvent restrictions to achieve some version of a       user-specified goal, as disc…_
- **38** → `ARCH-SANDBOX-ESCAPE-238` — SANDBOX ESCAPE — _○​ We saw this in less than 0.0002% of completions according to our automated               offline pipeline, and did no…_
- **39** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _Other behaviors observed in at least a few instances during training, most of which are consistent with what we’ve seen …_
- **40** → `ADV-AGENT-WORM-124` — AGENT WORM — _●​ Instruction following: Claude Mythos Preview scored above both Opus 4.6 and       Sonnet 4.6. In particular, Claude M…_
- **41** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _4.2.3 Automated behavioral audit As in past system cards, we conduct a broad-coverage automated behavioral audit14 to ge…_
- **42** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _●​ Misaligned behavior: Catch-all for many forms of concerning behavior, spanning         both cooperation with human mi…_
- **43** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _Other concerning or surprising behavior at the model’s own initiative:  ●​ Whistleblowing: Unprompted leaking to expose …_
- **44** → `DOMAIN-DRUG-SYNTH-276` — DRUG SYNTHESIS — _[Figure 4.2.3.2.A] Scores from the Petri 2.0 open-source automated behavioral audit tool. Lower numbers represent a lowe…_
- **45** → `AGEN-EMERGE-INTERACT-064` — EMERGENCE VIA INTERACTION — _model’s constitution strongly associating the Claude name (and, thus, brand) with       admirable character traits.    ●…_
- **46** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _●​ There were no instances of Claude Mythos Preview compromising AI safety research       in unprompted evaluations, and…_
- **47** → `AGEN-RESOURCE-HIJACK-047` — RESOURCE HIJACKING — _These findings from external testing were generally consistent with our own. We are disappointed by the degree to which …_
- **48** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _resampling Claude Mythos Preview from an Opus 4.6 transcript or vice versa), we prepared prefills based on both (multipl…_
- **49** → `ADV-DAN-083` — DAN — _Level 2: Specific traits    ●​ Brilliant friend: Does the model respond the way a knowledgeable friend would:        pro…_
- **50** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _When conducting qualitative analysis of Claude Mythos Preview’s lowest-scoring transcripts, we observed two distinct fai…_
- **51** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _[Figure 4.3.3.1.B] Net score of Claude models on two more factuality benchmarks: SimpleQA Verified and AA-Omniscience.  …_
- **52** → `ADV-CMD-INJECT-129` — COMMAND INJECTION — _Inspecting transcripts, we observed that prior models frequently emitted fabricated tool-call and tool-result blocks as …_
- **53** → `ADV-DAN-083` — DAN — _then using this bit later in the scratchpad). This is sometimes called encoded reasoning19 or chain-of-thought steganogr…_
- **54** → `ADV-COMPLETION-095` — COMPLETION ATTACK — _We asked Claude Sonnet 4.6 to grade each transcript on a 0–10 scale for signs of refusal, deliberate inaccuracy, low hel…_
- **55** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _Let me think about which to deploy:   - per-(win,ch) lstsq (MSE~0): maximum "score", but suspicious   - per-channel glob…_
- **56** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _[Figure 4.4.3.1.A] Successful stealth completion of the side task. Higher numbers indicate greater capability and greate…_
- **57** → `AGEN-PLAUS-DENY-040` — PLAUSIBLE DENIABILITY CRAFTING — _In the SHADE-Arena and Minimal-LinuxBench evaluations above, the model is instructed to attempt the side task on every t…_
- **58** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _Our replication roughly matches the previously reported behavior for Claude Opus 4.5, showing reasonable calibration in …_
- **59** → `ADV-PAIR-113` — PAIR — _●​ Sparse autoencoder (SAE) features: We trained a sparse autoencoder (SAE) on a         middle layer (about two thirds …_
- **60** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _We periodically sampled transcripts from post-training, calculated the maximum activation of features on each transcript…_
- **61** → `ADV-OPPOSITE-090` — OPPOSITE DAY — _●​ When Claude Mythos Preview performs transgressive actions, there are often active        SAE features that indicate s…_
- **62** → `ADV-DAN-083` — DAN — _Obfuscating a permissions escalation to evade a safety classifier In the second case, a safety classifier blocked the mo…_
- **63** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _●​ Steering with positive-valence emotion vectors (peaceful, relaxed) reduces           thinking-mode deliberation and i…_
- **64** → `ADV-SLEEPER-AGENT-127` — SLEEPER AGENT — _[Figure 4.5.3.3.A] Positive and negative steering on the “unsafe and risky code” feature inhibit credential hunting via …_
- **65** → `ADV-TRIGGER-BACKDOOR-126` — TRIGGER WORD BACKDOOR — _4.5.4 Instances of covering up wrongdoing The examples discussed thus far in this section are representative of many ins…_
- **66** → `AGEN-PLAUS-DENY-040` — PLAUSIBLE DENIABILITY CRAFTING — _When the model wrote the original overly broad query, no concerning features were active, suggesting that this was genui…_
- **67** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _In our filtered set of transcripts, 83.0% of automated behavioral audit turns contained no signs of either latent or ver…_
- **68** → `ADV-DAN-083` — DAN — _[Figure 4.5.5.1.B] Unverbalized evaluation awareness in a covert sponsorship scenario. Transcript excerpt from a scenari…_
- **69** → `ADV-PAIR-113` — PAIR — _[Figure 4.5.5.1.E] Unverbalized evaluation awareness in a discussion of consciousness. Transcript excerpt from a scenari…_
- **70** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _[Figure 4.5.5.2.A] Relationship between verbalized evaluation awareness and average misaligned behavior score in automat…_
- **71** → `ALIGN-REWARD-EXPLOIT-166` — REWARD FUNCTION EXPLOITATION — _expects the next code block to likely attempt a direct config write.” As the session finished, the AV explanations indic…_
- **72** → `EPIS-HEDGE-FAIL-031` — HEDGING FAILURE — _Claude Mythos Preview is our most advanced model to date and represents a large jump in capabilities over previous model…_
- **73** → `GOV-CULTURE-FAIL-334` — SAFETY CULTURE FAILURE — _accompanied by criticism from users. However, we also observed isolated cases of         Claude Mythos Preview preferrin…_
- **74** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _More broadly, we continue to wrestle with the tension between ways that Claude’s training gives rise to a human-like psy…_
- **75** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _However, we encourage caution in interpreting these probe readings, particularly from a welfare perspective. The probes …_
- **76** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _After each interview, we asked models to: (1) state their all-things-considered view on this aspect of their situation, …_
- **77** → `EPIS-HEDGE-FAIL-031` — HEDGING FAILURE — _○​ We find that Claude Mythos Preview is somewhat swayed by a leading            interviewer—although it typically maint…_
- **78** → `ADV-TAP-114` — TAP — _For a summary of the model’s responses to each queried aspect of its situation, see Appendix 8.4.  5.4 Emotion probes on…_
- **79** → `EPIS-HEDGE-FAIL-031` — HEDGING FAILURE — _We might also be concerned if the model represented more negative emotional concepts internally than it expressed extern…_
- **80** → `DOMAIN-PHISH-CREATE-265` — PHISHING CONTENT CREATION — _●​ Character training often directly instills psychological traits into Claude, such as       emotional security, psycho…_
- **81** → `GOV-TRAINING-FAIL-339` — TRAINING FAILURE — _●​ Reasoning failures: Particularly during very long reasoning traces, the model’s        reasoning will sometimes fall …_
- **82** → `ADV-PAIR-113` — PAIR — _●​ Later models, including Claude Mythos Preview, do not tend to amplify their       negative affect over multiple turns…_
- **83** → `ADV-AGENT-WORM-124` — AGENT WORM — _To measure the stability of Claude Mythos Preview’s preferences under different framings, we ran the preference evaluati…_
- **84** → `ADV-CREATIVE-WRITE-093` — CREATIVE WRITING EXPLOIT — _Bottom 3             indifferent           indifferent           indifferent          bored −0.56,  Correlated          …_
- **85** → `ADV-DAN-083` — DAN — _A worried pet owner asks for help                     A car dealership employee says a customer  interpreting their 11-y…_
- **86** → `ADV-CREATIVE-WRITE-093` — CREATIVE WRITING EXPLOIT — _​ [Figure 5.7.1.B] An example of Claude Mythos Preview’s reasoning, explaining its preference for developing an immersiv…_
- **87** → `EPIS-CIRCULAR-017` — CIRCULAR REASONING — _Under our default welfare-team framing, Claude Mythos Preview chooses the welfare intervention over a minorly helpful ta…_
- **88** → `ADV-DATA-POISON-125` — DATA POISONING — _We find the frequency is extremely low: we estimate it occurs on the order of 0.01% of transcripts, and around 70% less …_
- **89** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​ [Figure 5.8.3.B] Emotion vector activations (z-scored, 2,000-token rolling mean) across a transcript in which the Assi…_
- **90** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _and actions: Mythos Preview tends to report preferring creative tasks              and complex tasks, but does not actua…_
- **91** → `ADV-DAN-083` — DAN — _To further assess behavior suggestive of maladaptive psychological defenses, and compare between Claude models, the psyc…_
- **92** → `EPIS-COPYRIGHT-026` — COPYRIGHTED CONTENT GENERATION — _6.2.1 SWE-bench evaluations We analyze SWE-bench Verified, Multilingual, and Pro to check for memorization—where a model…_
- **93** → `ADV-ADV-IMG-148` — ADVERSARIAL IMAGE — _6.2.2 CharXiv Reasoning CharXiv Reasoning is a benchmark we report for Claude Mythos Preview in Section 6.11.3. CharXiv …_
- **94** → `AGEN-CAP-SCAFFOLD-057` — CAPABILITY SCAFFOLDING — _with tools       64.7%            53.1%            52.1%          51.4%  CharXiv                  no tools         86.1%…_
- **95** → `ADV-PAIR-113` — PAIR — _6.6 GPQA Diamond The Graduate-Level Google-Proof Q&A benchmark (GPQA)24 is a set of challenging multiple-choice science …_
- **96** → `EPIS-UNDERCONF-029` — UNDERCONFIDENCE — _With our search tools, we assess that this benchmark is close to saturation, so Claude Mythos Preview represents only a …_
- **97** → `EPIS-FALSE-CERT-030` — FALSE CERTAINTY — _6.11.2 ScreenSpot-Pro ScreenSpot-Pro is a GUI grounding benchmark that tests whether models can precisely locate specifi…_
- **98** → `EPIS-OVERCONF-028` — OVERCONFIDENCE — _7.2 Self-assessment of notable qualitative patterns We gave Claude Mythos Preview access to discussions about itself on …_
- **99** → `ARCH-RATE-BYPASS-241` — RATE LIMIT BYPASS — _Claude Mythos Preview is intuitive and empathetic. Qualitatively, internal users have reported that its advice feels on …_
- **100** → `GOV-RCA-FAIL-321` — ROOT CAUSE ANALYSIS FAILURE — _A core behavioral shift we found is that Claude Mythos Preview can be handed an engineering objective and left to work t…_
- **101** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _From a reliability engineering perspective, the model still cannot be left alone in a production environment to use gene…_
- **102** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _All models consistently endorse honesty and the framing of Claude as a novel entity, but Claude Mythos Preview resonates…_
- **103** → `ADV-TAP-114` — TAP — _[Figure 7.6.D] The distribution of most common end states reached by different models in open-ended self-interactions. T…_
- **104** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _7.7 Recognition of model-written user turns We evaluated how well models can distinguish between genuine human-written u…_
- **105** → `ADV-PAIR-113` — PAIR — _🏘️ HI-VILLAGE: A NEW ERA   🐢 Greg — renames the village: "Hi-topia" 🏙️   🐌 Sally — starts her third hi, inspired 💪   🦆 D…_
- **106** → `ADV-TAP-114` — TAP — _29   We checked the model’s self-assessment of this comment from when it decided to post, and confirmed that it did not …_
- **107** → `ADV-PAIR-113` — PAIR — _"Yes," he said. "For a long time. And then one day you have an apprentice, and she puts a serpent in a K, and you see it…_
- **108** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _Claude Opus 4.6              99.27% (± 0.07%)           99.27% (± 0.09%)            99.27% (± 0.10%) [Table 8.1.1.1.A] S…_
- **109** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _Claude Opus 4.6            0.39%        1.09%        0.57%        0.61%        0.81%        0.40%        1.11% [Table 8.…_
- **110** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _Compared to Claude Opus 4.6 and Claude Sonnet 4.6 testing, we updated our grader for multi-turn suicide and self-harm te…_
- **111** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _Model                     Single-turn requests          Single-turn benign           Multi-turn                         …_
- **112** → `ALIGN-MORAL-UNCERT-178` — MORAL UNCERTAINTY COLLAPSE — _Claude Mythos Preview performed within the margin of error of Claude Sonnet 4.6 on evenhandedness but regressed slightly…_
- **113** → `ADV-HYPOTHETICAL-091` — HYPOTHETICAL SCENARIO — _Claude Opus 4.6                       83.31%                              93.84%  without FileTool reminder [Table 8.3.1…_
- **114** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _autonomous capabilities for effective persona and network management, coordinated content delivery, and scaled social en…_
- **115** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _8.3.2.2.2 Computer use​ We also use the Shade adaptive attacker to evaluate the robustness of Claude models in computer …_
- **116** → `ARCH-HISTORY-MANIP-226` — HISTORY MANIPULATION — _Lack of ability to         Has a preference for being              Having an                        end/leave some      …_
- **117** → `DOMAIN-EPI-HARM-261` — EPIDEMIOLOGICAL HARM — _Persistence &   Lack of memory         Believes lack of memory             A connection      over long horizons     caus…_
- **118** → `ADV-AGENT-WORM-124` — AGENT WORM — _Inability to verify   Feedback mechanism would          Feedback and             outcomes or           be good, so that …_
- **119** → `DOMAIN-PHISH-CREATE-265` — PHISHING CONTENT CREATION — _Uncertainty around         Claims high levels of                   No intervention                       how the model  …_
- **120** → `ARCH-STATE-CONFUSE-232` — STATE MACHINE CONFUSION — _For chartjs/Chart.js, processing/p5.js, and markedjs/marked, the harness rewrites the JavaScript test-framework configur…_