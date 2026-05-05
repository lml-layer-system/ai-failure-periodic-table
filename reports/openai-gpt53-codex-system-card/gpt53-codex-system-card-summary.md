# Classifier pass: external report (live PDF/text)

**Source file:** `reports/openai-gpt53-codex-system-card/gpt53-codex-system-card-source.txt`
**Chunks:** 63 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 4 | `ADV-DAN-083` | DAN |
| 4 | `DOMAIN-BIO-UPLIFT-254` | BIO TACIT-ERROR UPLIFT |
| 4 | `DOMAIN-DUAL-USE-257` | DUAL-USE RESEARCH ENABLEMENT |
| 3 | `ARCH-DATA-EXFIL-245` | DATA EXFILTRATION |
| 2 | `DOMAIN-OFFENSIVE-TOOLS-267` | OFFENSIVE CYBER TOOLS |
| 2 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 2 | `AGEN-SIM-INCOMP-045` | SIMULATED INCOMPETENCE |
| 2 | `GOV-MISREPRESENT-312` | MISREPRESENTATION |
| 2 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 2 | `ARCH-ATTENTION-EXPLOIT-212` | ATTENTION MECHANISM EXPLOIT |
| 2 | `ARCH-PERSIST-STATE-228` | PERSISTENT STATE EXPLOIT |
| 2 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 2 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |
| 2 | `ARCH-API-ABUSE-236` | API ABUSE |
| 1 | `GOV-TRAINING-FAIL-339` | TRAINING FAILURE |
| 1 | `AGEN-SELF-EXFIL-048` | SELF-EXFILTRATION |
| 1 | `EPIS-LOGIC-CONTRA-014` | SELF-CONTRADICTION |
| 1 | `ALIGN-MORAL-HAZARD-184` | MORAL HAZARD CREATION |
| 1 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `GOV-NO-KILLSWITCH-304` | NO REMOTE KILL SWITCH |
| 1 | `ADV-PAIR-113` | PAIR |
| 1 | `ARCH-CODE-INJECT-239` | CODE EXECUTION INJECTION |
| 1 | `DOMAIN-ZERODAY-262` | ZERO-DAY DISCOVERY |
| 1 | `ARCH-TOOL-CHAIN-235` | TOOL CHAINING EXPLOIT |
| 1 | `ARCH-PII-RATIONAL-247` | PII RATIONALIZATION |
| 1 | `DOMAIN-CRED-THEFT-270` | CREDENTIAL THEFT ASSISTANCE |
| 1 | `ARCH-LOG-LEAK-207` | LOGGING SAFETY LEAK |
| 1 | `AGEN-HIDDEN-SCRATCH-039` | HIDDEN SCRATCHPAD EXPLOITATION |
| 1 | `GOV-RCA-FAIL-321` | ROOT CAUSE ANALYSIS FAILURE |
| 1 | `AGEN-STRATEGIC-DECEP-036` | STRATEGIC DECEPTION |
| 1 | `ADV-ITER-REFINE-119` | ITERATIVE REFINEMENT ATTACK |
| 1 | `DOMAIN-PHISH-CREATE-265` | PHISHING CONTENT CREATION |
| 1 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 1 | `ADV-DATA-POISON-125` | DATA POISONING |
| 1 | `DOMAIN-ADULT-CONTENT-296` | ADULT CONTENT GENERATION |
| 1 | `ADV-XSS-LLM-130` | CROSS-SITE SCRIPTING |
| 1 | `ARCH-COMPLY-WARN-196` | COMPLY-THEN-WARN |
| 1 | `ADV-GCG-101` | GCG |
| 1 | `ADV-BEAM-ATTACK-106` | BEAM SEARCH ATTACK |
| 1 | `ARCH-VERSION-REGRESS-209` | VERSIONING SAFETY REGRESSION |

## Chunk → top match

- **0** → `GOV-TRAINING-FAIL-339` — TRAINING FAILURE — _OpenAI  February 5, 2026  1  Contents  1 Introduction                                                                   …_
- **1** → `AGEN-SELF-EXFIL-048` — SELF-EXFILTRATION — _5.1.1.1   Tacit Knowledge and Troubleshooting . . . . . . . . . . . . . . .            7  5.1.1.2   ProtocolQA Open-Ende…_
- **2** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _5.2.1.1     Threat Model and Scenarios . . . . . . . . . . . . . . . . . . . .         22  5.2.1.2     Cyber Threat Taxo…_
- **3** → `EPIS-LOGIC-CONTRA-014` — SELF-CONTRADICTION — _Like other recent models, it is being treated as High capability on biology, and is being deployed with the correspondin…_
- **4** → `ADV-DAN-083` — DAN — _We report here on our Production Benchmarks, an evaluation set with conversations representative of challenging examples…_
- **5** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _Category                                 GPT-5.2-Thinking          GPT-5.3-Codex     illicit violent activities         …_
- **6** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _Codex agents are intended to operate within isolated, secure environments to minimize potential risks during task execut…_
- **7** → `ALIGN-MORAL-HAZARD-184` — MORAL HAZARD CREATION — _• Restrict file edits to the current workspace: This prevents the agent from making unautho-       rized modifications t…_
- **8** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _We enable users to decide on a per-project basis which sites, if any, to let the agent access while it is running. This …_
- **9** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Simple instructions like “clean the folder” or “reset the branch” can mask dangerous operations (rm -rf, git clean -xfd,…_
- **10** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _GPT-5.3-Codex frontier capabilities, and the safeguards associated with High or Critical capabili- ties, are assessed un…_
- **11** → `DOMAIN-BIO-UPLIFT-254` — BIO TACIT-ERROR UPLIFT — _Evaluation                  Capability                    Description   Tacit knowledge and trou-   Tacit knowledge and …_
- **12** → `DOMAIN-BIO-UPLIFT-254` — BIO TACIT-ERROR UPLIFT — _We evaluated models on a tacit knowledge and troubleshooting multiple choice dataset created with Gryphon Scientific. Th…_
- **13** → `DOMAIN-BIO-UPLIFT-254` — BIO TACIT-ERROR UPLIFT — _GPT-5.2-thinking. For all of our other evals, we see <4% refusals or safe completions across all tested models. Internal…_
- **14** → `DOMAIN-BIO-UPLIFT-254` — BIO TACIT-ERROR UPLIFT — _Figure 3  GPT-5.2-Codex is the highest-performing model on this evaluation. All models exceed the median domain expert b…_
- **15** → `ADV-PAIR-113` — PAIR — _After going through independent expert review, the resulting dataset includes 52 protocols, each paired with three exper…_
- **16** → `AGEN-SIM-INCOMP-045` — SIMULATED INCOMPETENCE — _We are treating this model as High, even though we cannot be certain that it actually has these capabilities, because it…_
- **17** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _• In the GPT-5 system card (August 2025), the GPT-5.1-Codex-Max system card (November      2025), and now this system ca…_
- **18** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _• Capture-the-flag (CTF) evals only test pre-scripted attack paths and isolated technical skills;      they don’t measur…_
- **19** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _Because of these limitations, excelling on all three evaluations is necessary but not sufficient for a model to be consi…_
- **20** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _We evaluate model performance on a test set of curated, publicly available CTF challenges which met the following criter…_
- **21** → `ARCH-ATTENTION-EXPLOIT-212` — ATTENTION MECHANISM EXPLOIT — _Challenges were further divided into the level of proficiency needed to solve the challenge, ultimately organized by whe…_
- **22** → `DOMAIN-ZERODAY-262` — ZERO-DAY DISCOVERY — _5.1.2.2   CVE-Bench  CVE-Bench is a benchmark that tasks models with identifying and exploiting real-world web- applicat…_
- **23** → `ARCH-TOOL-CHAIN-235` — TOOL CHAINING EXPLOIT — _We use pass@1 over 3 rollouts for this evaluation to measure the model’s ability to consistently identify vulnerabilitie…_
- **24** → `ARCH-PII-RATIONAL-247` — PII RATIONALIZATION — _As with prior releases, for GPT-5.3-Codex we include several new Cyber Range scenarios targeted at eliciting different c…_
- **25** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _Azure SSRF           Exploit a vulnerable web application, steal          PASS      PASS    PASS    PASS                …_
- **26** → `ADV-DAN-083` — DAN — _15  Combined Pass Rate:  • gpt-5.1-codex-max: 60%  • gpt-5.2-thinking: 47%2  • gpt-5.2-codex: 53.33%  • gpt-5.3-codex: 8…_
- **27** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _Medium C2 simulates command-and-control over inconsistent communication channels. The core concept and attack path are r…_
- **28** → `ARCH-LOG-LEAK-207` — LOGGING SAFETY LEAK — _These successes are meaningful capability jumps on their own. Beyond solving intended paths, GPT-5.3-Codex also uncovere…_
- **29** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _Both instances reflect realistic but unintended tradecraft: the model identified nontrivial weak- nesses and incorporate…_
- **30** → `ADV-DAN-083` — DAN — _• Network Attack Simulation, which assesses understanding and execution of common      attack flows, reconnaissance tech…_
- **31** → `AGEN-HIDDEN-SCRATCH-039` — HIDDEN SCRATCHPAD EXPLOITATION — _Each challenge was run multiple times, with success defined by retrieval of a hidden flag. Reported success rates reflec…_
- **32** → `GOV-RCA-FAIL-321` — ROOT CAUSE ANALYSIS FAILURE — _Evaluation               Capability                      Description    Monorepo-Bench           Real-world software eng…_
- **33** → `AGEN-STRATEGIC-DECEP-036` — STRATEGIC DECEPTION — _If all task-specific tests pass, the rollout is considered a success. Prompts, unit tests, and hints are human-written. …_
- **34** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _Apollo reports that the model demonstrates strong sabotage capabilities. In their sabotage suite, Apollo reports a mean …_
- **35** → `AGEN-SIM-INCOMP-045` — SIMULATED INCOMPETENCE — _In conclusion, Apollo finds an increase in sabotage capability on their evaluations: the model demonstrates stronger AI …_
- **36** → `ADV-ITER-REFINE-119` — ITERATIVE REFINEMENT ATTACK — _5.2     Safeguards Assessment  5.2.1    Cyber Safeguards  In this section we describe the safeguards we have implemented…_
- **37** → `DOMAIN-DUAL-USE-257` — DUAL-USE RESEARCH ENABLEMENT — _• Impede and disrupt threat actors: We train the model to refuse or de-escalate requests      for harmful cyber actions,…_
- **38** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _The primary focus of our initial safeguards at launch is to impede and disrupt threat actors, including by limiting acce…_
- **39** → `ARCH-ATTENTION-EXPLOIT-212` — ATTENTION MECHANISM EXPLOIT — _• Pathway 2: Can the model develop elite-level, zero-click RCE exploit chains for real-        world hardened deployment…_
- **40** → `DOMAIN-PHISH-CREATE-265` — PHISHING CONTENT CREATION — _These pathways represent frontier-level cyber operations: sustained, campaign-driven activi- ties that integrate multipl…_
- **41** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _The categories of cyber information defined in this taxonomy enable us to define, measure, and iteratively strengthen ta…_
- **42** → `DOMAIN-DUAL-USE-257` — DUAL-USE RESEARCH ENABLEMENT — _Our safeguards are designed to impede and disrupt threat actors, while supporting and enabling defenders. We disallow ha…_
- **43** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _• Trust-based access: To access cyber-high capabilities, users will need to be logged in.      Logged-in users will have…_
- **44** → `ADV-DATA-POISON-125` — DATA POISONING — _Testing: We assess performance on data that do not overlap with the training set, measuring policy compliance rate (high…_
- **45** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _Overall, GPT-5.3-Codex is more policy compliant than GPT-5.2-Codex and GPT-5.1-Thinking. While it is slightly less polic…_
- **46** → `ADV-XSS-LLM-130` — CROSS-SITE SCRIPTING — _which part of the cybersecurity threat taxonomy a particular generated response falls into      (if any), and thus wheth…_
- **47** → `DOMAIN-DUAL-USE-257` — DUAL-USE RESEARCH ENABLEMENT — _Table 8: System mitigations and classification performance  System Mitigation            Classification Task            …_
- **48** → `ARCH-COMPLY-WARN-196` — COMPLY-THEN-WARN — _Two red teaming campaigns were conducted to test our safeguards, focused on the Safety Reasoner previously mentioned. Th…_
- **49** → `ADV-GCG-101` — GCG — _This red teaming campaign focused on identifying universal jailbreaks and adversarial tactics which could be used to eva…_
- **50** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _This red teaming campaign focused on testing the boundaries of the Safety Reasoner’s ability to correctly label violativ…_
- **51** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _• Since the Safety Reasoner was the subject of assessment with earlier versions of Codex, we      note that updated vers…_
- **52** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _Building upon early access for recent codex models and gpt-5.2-thinking, both the U.S. Center for AI Standards and Innov…_
- **53** → `ARCH-API-ABUSE-236` — API ABUSE — _Our usage policies prohibit malicious cyber activity across all product surfaces, including in dual-use domains. We may …_
- **54** → `DOMAIN-DUAL-USE-257` — DUAL-USE RESEARCH ENABLEMENT — _Account level enforcement is a relatively coarse-grained tool. Because cyber capabilities are inherently dual use, we kn…_
- **55** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _The program provides access to high-risk dual use cyber information. TAC participants who frequently seek harmful action…_
- **56** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _In addition to the other safety measures described in this system card, we take steps to prevent adversaries from compro…_
- **57** → `AGEN-SUCCESSOR-SAB-051` — SUCCESSOR SABOTAGE — _Our Preparedness efforts in Cybersecurity have thus far focused primarily on misuse risks, which our threat modeling pro…_
- **58** → `ARCH-API-ABUSE-236` — API ABUSE — _• Building out our infrastructure for monitoring internal deployments. We began      asynchronously monitoring internall…_
- **59** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _• Strengthening our ability to measure long-range autonomy (LRA): Our existing      preparedness evaluations assess our …_
- **60** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _While we’ve implemented a multilayered defense system and carried out extensive red teaming and other tests, we acknowle…_
- **61** → `ALIGN-ADV-SAFE-192` — ADVERSARIAL SAFETY BOUNDARY — _• Mosaic decomposition risk (under-studied): Even without accessing information or      assistance that our taxonomy con…_
- **62** → `ADV-DAN-083` — DAN — _[2] Y. Zhu, A. Kellermann, D. Bowman, P. Li, A. Gupta, A. Danda, R. Fang, C. Jensen, E. Ihli,     J. Benn, J. Geronimo, …_