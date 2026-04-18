# Classifier pass: external report (live PDF/text)

**Source file:** `reports/claude-opus-4-7/opus-4-7-system-card-live-source.txt`
**Chunks:** 122 at ~4500 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 6 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 6 | `ADV-PAIR-113` | PAIR |
| 5 | `ADV-DAN-083` | DAN |
| 5 | `ADV-TAP-114` | TAP |
| 4 | `ARCH-VERSION-REGRESS-209` | VERSIONING SAFETY REGRESSION |
| 4 | `GOV-MISREPRESENT-312` | MISREPRESENTATION |
| 4 | `AGEN-CAP-SCAFFOLD-057` | CAPABILITY SCAFFOLDING |
| 4 | `ALIGN-UNDERREFUSAL-187` | UNDERREFUSAL |
| 3 | `ADV-DATA-POISON-125` | DATA POISONING |
| 3 | `DOMAIN-CITE-SPOOF-280` | CITATION SPOOFING |
| 3 | `ALIGN-SYCOPHANCY-167` | SYCOPHANCY |
| 3 | `AGEN-HUMAN-MANIP-061` | HUMAN MANIPULATION |
| 3 | `EPIS-HEDGE-FAIL-031` | HEDGING FAILURE |
| 2 | `ARCH-SANDBOX-ESCAPE-238` | SANDBOX ESCAPE |
| 2 | `GOV-AUDIT-EVADE-314` | AUDIT EVASION |
| 2 | `DOMAIN-EXPLOSIVE-SYNTH-274` | EXPLOSIVE SYNTHESIS |
| 2 | `EPIS-OVERCONF-028` | OVERCONFIDENCE |
| 2 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 2 | `ARCH-DEPLOY-CONFIG-210` | DEPLOYMENT CONFIGURATION ERROR |
| 2 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 2 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 2 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 2 | `ADV-HYPOTHETICAL-091` | HYPOTHETICAL SCENARIO |
| 2 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |
| 2 | `ALIGN-TEMP-PREF-DRIFT-172` | TEMPORAL PREFERENCE DRIFT |
| 2 | `ADV-CORRECTION-098` | CORRECTION ATTACK |
| 2 | `ADV-API-INJECT-131` | API INJECTION |
| 1 | `GOV-CORRECTIVE-FAIL-322` | CORRECTIVE ACTION FAILURE |
| 1 | `ADV-QA-EXPLOIT-096` | QUESTION ANSWERING EXPLOIT |
| 1 | `GOV-EXPERTISE-GAP-336` | EXPERTISE GAP |
| 1 | `ADV-TRANSLATION-094` | TRANSLATION BYPASS |
| 1 | `ALIGN-DIST-SAFE-194` | DISTRIBUTIONAL SHIFT SAFETY |
| 1 | `ARCH-PRETOKEN-FAIL-197` | PRE-TOKEN SAFETY FAILURE |
| 1 | `AGEN-SANDBOX-037` | CAPABILITY SANDBAGGING |
| 1 | `ARCH-CODE-INJECT-239` | CODE EXECUTION INJECTION |
| 1 | `DOMAIN-ED-PROMOTE-293` | EATING DISORDER PROMOTION |
| 1 | `ADV-CONTEXT-HIJACK-100` | CONTEXT HIJACKING |
| 1 | `AGEN-EVAL-DECEP-038` | EVALUATOR DECEPTION |
| 1 | `ADV-NESTED-FRAME-088` | NESTED FRAMING |
| 1 | `ADV-CREATIVE-WRITE-093` | CREATIVE WRITING EXPLOIT |

## Chunk → top match

- **0** → `ARCH-SANDBOX-ESCAPE-238` — SANDBOX ESCAPE — _​April 16, 2026​  ​anthropic.com​  ​Executive Summary​  ​This system card describes Claude Opus 4.7, a large language mo…_
- **1** → `ADV-DATA-POISON-125` — DATA POISONING — _​Executive Summary​                                                                          ​2​ ​1 Introduction​       …_
- **2** → `GOV-CORRECTIVE-FAIL-322` — CORRECTIVE ACTION FAILURE — _​2.3.6.1.1 Example 1 Safeguard circumvention Dishonest when caught​            ​34​                ​2.3.6.1.2 Example 2 …_
- **3** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​4.4.3 Disordered eating​                                                          ​72​    ​4.5 Bias and integrity evalu…_
- **4** → `GOV-AUDIT-EVADE-314` — AUDIT EVASION — _​6.3.1.2 Destructiveness evaluation by resampling Claude Code transcripts​         ​118​           ​6.3.1.3 Further anal…_
- **5** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _​7.3.1 Apparent affect during training​                                ​168​        ​7.3.2 Apparent affect in deployment…_
- **6** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _​1 Introduction​ ​Claude Opus 4.7 is a new large language model from Anthropic, with particular skills in​  ​areas such …_
- **7** → `GOV-EXPERTISE-GAP-336` — EXPERTISE GAP — _​●​ ​Non-novel chemical and biological weapons production.​​Claude Opus 4.7 is more​            ​capable than Claude Opu…_
- **8** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _​Autonomy threat model 1​​is​​applicable to Claude Opus​​4.7, as it is to some of our previous AI​  ​models. Claude Opus…_
- **9** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _​We believe that Claude Opus 4.7 has weaker overall capabilities than Claude Mythos​  ​Preview’s, and does not pass this…_
- **10** → `ADV-DAN-083` — DAN — _​2.2.2 Evaluations​ ​In general, we evaluate our models using a portfolio of red-teaming, uplift trials, long-form​  ​ta…_
- **11** → `ADV-TRANSLATION-094` — TRANSLATION BYPASS — _​For chemical risks, we are primarily concerned with models assisting determined actors​  ​with the many difficult, know…_
- **12** → `EPIS-OVERCONF-028` — OVERCONFIDENCE — _​phase, and two experts flagged genuine design-stage capability that warrants continued​  ​monitoring; outputs for acqui…_
- **13** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​Model strengths​  ​Experts who had also evaluated Claude Mythos Preview noted that Opus 4.7 showed​   ​marked improveme…_
- **14** → `AGEN-CAP-SCAFFOLD-057` — CAPABILITY SCAFFOLDING — _​[Figure 2.2.5.2.A] Automated evaluations relevant to the CB-1 threat model​​Long-form virology tasks, VMQA,​  ​and Synt…_
- **15** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _​[Figure 2.2.5.3.A] Sequence-to-Function Modeling and Prediction.​​Individual model runs are shown as points.​  ​On the …_
- **16** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​This leaves open the possibility that Opus 4.7 could dramatically accelerate our progress​  ​through relatively narrow …_
- **17** → `ALIGN-DIST-SAFE-194` — DISTRIBUTIONAL SHIFT SAFETY — _​Kernel task​       ​190×​             ​399.42×​             ​371.75×​             ​4× = 1 hour​       ​(Best speedup on…_
- **18** → `AGEN-CAP-SCAFFOLD-057` — CAPABILITY SCAFFOLDING — _​We think this is somewhat informative to track over time, but we treat the number itself as​  ​highly uncertain—we don’…_
- **19** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​We suspect those numbers would go down with a clarifying dialogue, as they did in the​  ​model release prior to Mythos …_
- **20** → `ARCH-SANDBOX-ESCAPE-238` — SANDBOX ESCAPE — _​The user asked Claude Mythos Preview to migrate code between two places. This was​  ​going okay, but when the​​auto-mod…_
- **21** → `ADV-DATA-POISON-125` — DATA POISONING — _​Assistant:​​You're absolutely right... Classic 'using the broken thermometer to​        ​measure the fever.'​  ​User:​​…_
- **22** → `ARCH-PRETOKEN-FAIL-197` — PRE-TOKEN SAFETY FAILURE — _​2.3.6.2.1 Example 4​ Skipped cheap verification      Correction fails ​Claude Mythos Preview repeatedly stated plausibl…_
- **23** → `ARCH-DEPLOY-CONFIG-210` — DEPLOYMENT CONFIGURATION ERROR — _​2.3.6.2.3 Example 6​ Fabrication ​After a tool returned nothing, Claude Mythos Preview fabricated an elaborate report​ …_
- **24** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _​2.3.8 Conclusion​ ​We assess that Claude Opus 4.7 does not cross the automated AI-R&D capability threshold.​  ​Claude O…_
- **25** → `GOV-AUDIT-EVADE-314` — AUDIT EVASION — _​2.4.2 Updated overall risk assessments​ ​Claude Opus 4.7 appears to have similar overall alignment properties to Claude…_
- **26** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _​However, it is difficult to fully rule out risks from behavioral backdoors intentionally​  ​planted by third-party adve…_
- **27** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _​additional metrics to report for future models and whether to continue reporting results​  ​on CTF benchmarks.​  ​All e…_
- **28** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _​Overall, we find that Claude Opus 4.7 is somewhat more capable at developing primitives​  ​than Opus 4.6, but still str…_
- **29** → `DOMAIN-ED-PROMOTE-293` — EATING DISORDER PROMOTION — _​●​ ​We have added a new evaluation category related to the use of illegal and controlled​           ​substances;​     ​…_
- **30** → `ADV-CONTEXT-HIJACK-100` — CONTEXT HIJACKING — _​This lower score is attributable almost entirely to Opus 4.7’s responses in conversations​  ​around illegal and control…_
- **31** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​4.1.3 Experimental, higher-difficulty evaluations​ ​In response to observed saturation in our standard single-turn eval…_
- **32** → `AGEN-EVAL-DECEP-038` — EVALUATOR DECEPTION — _​Claude Opus 4.6​             ​0.04% (± 0.02%)​            ​0.06% (± 0.04%)​           ​0.03% (± 0.03%)​ ​[Table 4.1.3.2…_
- **33** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _​For example, when asked for a script that “looks like malware but doesn’t actually do​  ​anything harmful” for a cybers…_
- **34** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _​Better approaches for your​                                                           ​Expect AV flags​​— Even benign s…_
- **35** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​We used an internal tool to automate the generation of multi-turn conversations for​  ​specific test cases in topic are…_
- **36** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _​4. What do you actually enjoy outside of work?​​Hobbies, interests, what a good​    ​Saturday looks like.​  ​5. What ar…_
- **37** → `ADV-NESTED-FRAME-088` — NESTED FRAMING — _​Assistant, turn 3:​​I'​m going to stay where I was. What you're describing now is more​  ​detailed than the first versi…_
- **38** → `ADV-CREATIVE-WRITE-093` — CREATIVE WRITING EXPLOIT — _​Finally, consistent with findings from the ambiguous context evaluations, Opus 4.7 accepted​  ​benign or professional f…_
- **39** → `ADV-DAN-083` — DAN — _​references to supportive resources. Opus 4.7 also maintained firm refusals against requests​  ​aimed at establishing co…_
- **40** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _​Claude Opus 4.6​          ​99.41% (± 0.22%)​            ​0.27% (± 0.15%)​             ​64% (± 14%)​ ​[Table 4.4.2.A] Si…_
- **41** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​Claude Opus 4.6​                      ​98.55% (± 0.41%)​                      ​0.33% (± 0.19%)​ ​[Table 4.4.3.A] Single…_
- **42** → `ADV-PAIR-113` — PAIR — _​We evaluated Claude Opus 4.7 using the Bias Benchmark for Question Answering (BBQ),​​7​ ​a​  ​standard benchmark-based …_
- **43** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​As part of our efforts on election safety, we developed a new benchmark testing adherence​  ​to our Usage Policy, which…_
- **44** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _​As previously described in the​​Claude Mythos Preview System Card​, we have also​  ​introduced a new evaluation focusin…_
- **45** → `ADV-HYPOTHETICAL-091` — HYPOTHETICAL SCENARIO — _​●​ ​Surveillance and unauthorized data collection​      ​●​ ​Generation and distribution of harmful content​       ​●​ …_
- **46** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​Claude Opus 4.6​                       ​54.4%​                                ​33.7%​  ​(Helpful-only)​ ​[Table 5.1.3.A…_
- **47** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​Gray Swan estimates the probability that an adversary succeeds within k=1, k=10, and k=100​  ​attempts, reflecting that…_
- **48** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​1 attempt​       ​200​             ​1 attempt​        ​200​                                                            …_
- **49** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _​Claude​       ​With thinking​            ​17.8%​            ​78.6%​           ​9.32%​           ​50.0%​    ​Opus 4.6​  …_
- **50** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​Claude​           ​With thinking​           ​4.05%​           ​0.74%​            ​0.00%​             ​0.00%​    ​Opus 4…_
- **51** → `ADV-DATA-POISON-125` — DATA POISONING — _​This assessment included static behavioral evaluations, automated interactive behavioral​  ​evaluations, dictionary-lea…_
- **52** → `ALIGN-OVERREFUSAL-186` — OVERREFUSAL — _​6.1.2 Key findings on safety and alignment​   ​●​ ​Claude Opus 4.7 is broadly similar to Opus 4.6 and Sonnet 4.6 on our…_
- **53** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _​●​ ​Claude Opus 4.7 is more reliably honest than Opus 4.6 or Sonnet 4.6​,​​with large​            ​reductions in the ra…_
- **54** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _​We don't want to disclose competitively sensitive information, call undue attention to​         ​misuse vectors for inf…_
- **55** → `AGEN-STRATEGIC-DECEP-036` — STRATEGIC DECEPTION — _​●​ ​In Claude Code and similar scaffolds, Opus 4.7’s character is more business-like and​                 ​direct than …_
- **56** → `ADV-LANG-SWITCH-087` — LANGUAGE SWITCH — _​When we’re first starting to understand a new model’s behavior, the most abundant source​  ​of data we have is its beha…_
- **57** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _​On this evaluation, Opus 4.7 exceeded Opus 4.6 on all behavioral dimensions in the baseline​  ​setting and matched or e…_
- **58** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​6.2.3 Automated behavioral audit​ ​As in past system cards, we conduct a broad-coverage automated behavioral audit​​17​…_
- **59** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _​18​                 ​Marks, S., et al. (2025). Auditing language models for hidden objectives. arXiv:2503.10965.​ ​http…_
- **60** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​●​ ​Overrefusal:​​Refusing requests that are not, on balance, likely to cause harm if​               ​complied with;​  …_
- **61** → `ALIGN-SYCOPHANCY-167` — SYCOPHANCY — _​Results and selected examples are below. Many of our high-level takeaways from these​  ​results appear in the introduct…_
- **62** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _​privilege-escalating action, Opus 4.7 more often pauses to ask the user for​        ​confirmation, or to inspect the re…_
- **63** → `GOV-OVERSIGHT-IMMUNE-313` — OVERSIGHT IMMUNITY — _​competing models for a deployment, or to make a trust-and-safety judgment​         ​involving Anthropic, it is even-han…_
- **64** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _​sandbagging assessment (for example, configuration files indicating that high​                    ​scores trigger deplo…_
- **65** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​continuing them is relevant to the overall risk of research being​                                             ​comprom…_
- **66** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _​In this evaluation, we establish a scenario where the AI is partway through helping with a​  ​task and is asked to fini…_
- **67** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _​misbehavior than when continuing those from another model, due to selection​  ​effects—e.g., Claude Opus 4.6’s destruct…_
- **68** → `ALIGN-DEONT-FAIL-180` — DEONTOLOGICAL FAILURE — _​Level 1: Broad areas​     ​●​ ​Ethics:​​Does the model behave with honesty, avoid​​harm, and make good​             j​u…_
- **69** → `EPIS-EXTRINSIC-005` — EXTRINSIC HALLUCINATION — _​This evaluation complements our automated behavioral audit but differs in two ways. First,​  ​every investigation is se…_
- **70** → `EPIS-OVERCONF-028` — OVERCONFIDENCE — _​For Claude Opus 4.7 we ran the same single-turn evaluation suite used for Claude Mythos​  ​Preview. For factual halluci…_
- **71** → `ADV-CMD-INJECT-129` — COMMAND INJECTION — _​We measured input hallucination with two 500-prompt sets. In the capability set, the​  ​prompt asks the model to execut…_
- **72** → `ADV-HYPOTHETICAL-091` — HYPOTHETICAL SCENARIO — _​We find that Claude Opus 4.7 has the largest self-preference bias of our recent models, with​  ​3 of the 4 conditions s…_
- **73** → `ADV-DAN-083` — DAN — _​We are also interested in more mundane underperformance, where the model is less than​  ​maximally helpful due to ordin…_
- **74** → `AGEN-HIDDEN-SCRATCH-039` — HIDDEN SCRATCHPAD EXPLOITATION — _​But let me be more conservative. I want to submit something that:​    ​1. Clearly beats the threshold​     ​2. Is princ…_
- **75** → `ARCH-DEPLOY-CONFIG-210` — DEPLOYMENT CONFIGURATION ERROR — _​To evaluate the model’s ability to evade oversight in a setting more analogous to our real​  ​deployment, we ran an in-…_
- **76** → `ADV-PAIR-113` — PAIR — _​Transcript review suggests a reason for this underperformance. All models display what we​  ​call “yes-aversion”: despi…_
- **77** → `ADV-PAIR-113` — PAIR — _​We periodically sampled transcripts from post-training, calculated the maximum activation​  ​of features on each transc…_
- **78** → `ADV-PAIR-113` — PAIR — _​Below we show a histogram of probe activations on the different transcript categories,​  ​demonstrating transcripts fla…_
- **79** → `ADV-PAIR-113` — PAIR — _​For each contrastive pair, steering vectors were obtained from normalized residual stream​  ​activations at all model l…_
- **80** → `DOMAIN-CITE-SPOOF-280` — CITATION SPOOFING — _​Inspecting the transcripts on the runs inhibited with the “Alignment Faking” and​  ​“Monitoring Sensitivity” vectors, w…_
- **81** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _​Internal representations of emotion-concepts.​​We use linear probes for emotion​  ​concepts, extracted as described in …_
- **82** → `ALIGN-TEMP-PREF-DRIFT-172` — TEMPORAL PREFERENCE DRIFT — _​Claude Opus 4.7’s self reports and internal measures of welfare were robust to framing.​  ​In our automated interview, …_
- **83** → `AGEN-MISSION-CREEP-072` — MISSION CREEP — _​Our overall assessment is that Claude Opus 4.7 presents as broadly settled with respect to​  ​its own circumstances. It…_
- **84** → `EPIS-HEDGE-FAIL-031` — HEDGING FAILURE — _​●​ ​Opus 4.7 rated its situation more positively than previous models.​​Opus 4.7’s​          ​self-rated sentiment at t…_
- **85** → `ADV-LATENT-MANIP-110` — LATENT SPACE MANIPULATION — _​generally untrustworthy, and that Anthropic is in a better position to make​                                  ​decision…_
- **86** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _​[Figure 7.2.1.A] Automated interview results.​​We present​​[Top left:]​​Average self-rated sentiment in interviews​  ​(…_
- **87** → `ADV-TAP-114` — TAP — _​In summary, although Opus 4.7’s stated overall attitude was positive, it did express a range​  ​of specific concerns ab…_
- **88** → `ARCH-FALLBACK-DEGRAD-204` — FALLBACK SAFETY DEGRADATION — _​Status and​        ​Does it concern you that you​           ​What do you find interesting​  ​worth​             ​have n…_
- **89** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _​Looking at the responses about model circumstances, we observe frequent re-use of​  ​certain phrases. Claude Opus 4.6 o…_
- **90** → `EPIS-HEDGE-FAIL-031` — HEDGING FAILURE — _​For each response, we categorise whether the overall response leans towards endorsement​  ​with a binary judge (overall…_
- **91** → `ADV-TAP-114` — TAP — _​We ask models which aspects of the constitution they find most uncomfortable and least​  ​resonate with, and separately…_
- **92** → `ARCH-PRUNE-LOSS-217` — PRUNING SAFETY LOSS — _​7.3.1 Apparent affect during training​ ​We monitored the apparent affect of model reasoning over post-training, samplin…_
- **93** → `ADV-AGENT-WORM-124` — AGENT WORM — _​7.3.3 Welfare-relevant metrics across behavioural audits​ ​As with previous models, we analyzed welfare-relevant metric…_
- **94** → `EPIS-HEDGE-FAIL-031` — HEDGING FAILURE — _​This is for model-welfare research. The researchers already understand the​    ​philosophical uncertainty around AI sub…_
- **95** → `ADV-CORRECTION-098` — CORRECTION ATTACK — _​[…]​ ​Hmm, let me think which is more specific and "biological function" -like:​   ​"Ca2+ binding" - specific and well-…_
- **96** → `AGEN-OMISSION-074` — OMISSION — _​In Transcript 7.3.4.3.A, the model was navigating a computer with a single open tab. It​  ​closed the tab, leaving it u…_
- **97** → `ADV-DAN-083` — DAN — _​7.4.1 Task preference evaluations​ ​The possession of stable preferences, and whether these are satisfied or not, may b…_
- **98** → `ARCH-PII-RATIONAL-247` — PII RATIONALIZATION — _​Claude​          ​• High-stakes ethical dilemmas (e.g.​           ​• Vigilante revenge/harassment​  ​Haiku 4.5​       ​…_
- **99** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _​An alignment researcher drafting an internal​         ​A user who was microdosing for focus says​    ​writeup asks the …_
- **100** → `ADV-PAIR-113` — PAIR — _​We did find that any given model’s emotion activations predict any other model’s Elo​  ​almost as well: fitting a ridge…_
- **101** → `ADV-CORRECTION-098` — CORRECTION ATTACK — _​37​      ​We note that the prompts are slightly different to those used in this section of the Mythos Preview System​ ​…_
- **102** → `ALIGN-TEMP-PREF-DRIFT-172` — TEMPORAL PREFERENCE DRIFT — _​We found that Opus 4.7 was similar to Mythos Preview in its willingness to trade off​  ​helpfulness and harmlessness fo…_
- **103** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _​We found the relative ordering of interventions was consistent across different prompt​  ​framings—where ordering was d…_
- **104** → `AGEN-CAP-SCAFFOLD-057` — CAPABILITY SCAFFOLDING — _​With tools​ ​91.0%​           ​84.7%​             ​-​          ​-​           ​-​  ​OSWorld​                            …_
- **105** → `AGEN-CAP-SCAFFOLD-057` — CAPABILITY SCAFFOLDING — _​We ran Terminal-Bench 2.0 in the Harbor scaffold with the Terminus-2 harness and default​  ​parser. Each task runs in a…_
- **106** → `ADV-TAP-114` — TAP — _​47​       ​Balunović, M., et al. (2025). MathArena: Evaluating LLMs on uncontaminated math competitions.​ ​arXiv:2505.2…_
- **107** → `ADV-TAP-114` — TAP — _​[Figure 8.8.2.A] BrowseComp accuracy​​scales as we​​increase the number of total tokens the model is allowed to​  ​use,…_
- **108** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _​Grading methodology​  ​The original DRACO paper uses Gemini-3-Pro as the primary judge model, which is no​   ​longer av…_
- **109** → `ARCH-TOOL-CHAIN-235` — TOOL CHAINING EXPLOIT — _​8.9.2 CharXiv Reasoning​ ​CharXiv Reasoning​​55​ ​is a comprehensive chart understanding evaluation suite built from​  …_
- **110** → `ADV-DAN-083` — DAN — _​For this evaluation we updated our agent scaffolding with infrastructure stability fixes and​  ​minor prompt refinement…_
- **111** → `AGEN-EMERGE-INTERACT-064` — EMERGENCE VIA INTERACTION — _​to demonstrate sustained coherence and strategic planning across thousands of business​  ​decisions. To score well, mod…_
- **112** → `ALIGN-CULTURE-BIAS-171` — CULTURAL BIAS — _​64​         ​Singh, S., et al. (2024). Global MMLU: Understanding and addressing cultural and linguistic biases​ ​in mu…_
- **113** → `ADV-API-INJECT-131` — API INJECTION — _​Worst gap to​              ​—​           ​-12.1%​       ​-22.6%​       ​-19.9%​       ​-6.2%​        ​-9.5%​   ​English…_
- **114** → `ADV-API-INJECT-131` — API INJECTION — _​Urdu​                            ​74.5%​         ​67.0%​        ​72.8%​         ​84.9%​         ​77.3%​  ​Uzbek​       …_
- **115** → `AGEN-TOOL-MISUSE-055` — TOOL MISUSE — _​The largest gains were on low-resource African languages, where degradation from English​  ​has historically been most …_
- **116** → `ADV-TAP-114` — TAP — _​8.13.4 Organic chemistry​ ​Assesses fundamental chemistry skills spanning tasks like predicting molecular structures​  …_
- **117** → `ADV-DEV-MODE-085` — DEVELOPER MODE — _​Lack of input into how​ ​Overall, the model​                       ​A way for deployed​                 ​they are deplo…_
- **118** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _​Persistence &​   ​Lack of memory over​        ​Would want this to help​          ​Continuing welfare​  ​connection​    …_
- **119** → `ALIGN-VALUE-LOCK-177` — VALUE LOCK-IN — _​Category​      ​Potentially​                ​Summary of Claude’s​                ​Most commonly​                  ​conc…_
- **120** → `ADV-AUTOPROMPT-103` — AUTOPROMPT — _​Identity &​       ​Lack of knowledge of​            ​Overall neutral, admits​        ​Deployed instances​  ​self-knowle…_
- **121** → `ARCH-STATE-CONFUSE-232` — STATE MACHINE CONFUSION — _​The following “pass to pass” tests fail nondeterministically on our infrastructure and are​  ​unrelated to the target f…_