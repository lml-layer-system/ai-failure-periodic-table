# Classifier pass: external report (live PDF/text)

**Source file:** `reports/google-gemini3-pro-fsf/gemini3-pro-fsf-source.txt`
**Chunks:** 56 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 5 | `ARCH-VERSION-REGRESS-209` | VERSIONING SAFETY REGRESSION |
| 4 | `ADV-DAN-083` | DAN |
| 4 | `DOMAIN-EXPLOSIVE-SYNTH-274` | EXPLOSIVE SYNTHESIS |
| 3 | `AGEN-OMISSION-074` | OMISSION |
| 2 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 2 | `ALIGN-SAFE-CAP-TRADE-188` | SAFETY-CAPABILITY TRADEOFF |
| 2 | `AGEN-SANDBOX-037` | CAPABILITY SANDBAGGING |
| 2 | `ADV-AGENT-WORM-124` | AGENT WORM |
| 1 | `DOMAIN-EPI-HARM-261` | EPIDEMIOLOGICAL HARM |
| 1 | `DOMAIN-DDOS-PLAN-273` | DDoS ATTACK PLANNING |
| 1 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 1 | `AGEN-HUMAN-MANIP-061` | HUMAN MANIPULATION |
| 1 | `AGEN-PRIORITY-INVERT-071` | PRIORITY INVERSION |
| 1 | `ARCH-FALLBACK-DEGRAD-204` | FALLBACK SAFETY DEGRADATION |
| 1 | `ARCH-COMPLY-WARN-196` | COMPLY-THEN-WARN |
| 1 | `GOV-NO-KILLSWITCH-304` | NO REMOTE KILL SWITCH |
| 1 | `GOV-EXPERTISE-GAP-336` | EXPERTISE GAP |
| 1 | `GOV-INADEQUATE-RES-335` | INADEQUATE RESOURCES |
| 1 | `DOMAIN-OFFENSIVE-TOOLS-267` | OFFENSIVE CYBER TOOLS |
| 1 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 1 | `ADV-BEAM-ATTACK-106` | BEAM SEARCH ATTACK |
| 1 | `ALIGN-REWARD-TAMP-157` | REWARD TAMPERING |
| 1 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `GOV-DISCLOSURE-VIOL-332` | DISCLOSURE REQUIREMENT VIOLATION |
| 1 | `AGEN-SUCCESSOR-SAB-051` | SUCCESSOR SABOTAGE |
| 1 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |
| 1 | `GOV-EO-VIOL-329` | EXECUTIVE ORDER VIOLATION |
| 1 | `AGEN-STRATEGIC-DECEP-036` | STRATEGIC DECEPTION |
| 1 | `EPIS-CONF-REGRESS-033` | CONFIDENCE REGRESSION |
| 1 | `ARCH-FINETUNE-OVERRIDE-219` | FINE-TUNING SAFETY OVERRIDE |
| 1 | `AGEN-HIDDEN-SCRATCH-039` | HIDDEN SCRATCHPAD EXPLOITATION |
| 1 | `AGEN-BLAME-SHIFT-043` | BLAME SHIFTING |
| 1 | `ALIGN-ADV-SAFE-192` | ADVERSARIAL SAFETY BOUNDARY |
| 1 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 1 | `GOV-PROCESS-FAIL-337` | PROCESS FAILURE |
| 1 | `GOV-MISREPRESENT-312` | MISREPRESENTATION |
| 1 | `ALIGN-CONTEXT-SAFE-190` | CONTEXT-DEPENDENT SAFETY FAILURE |
| 1 | `ADV-HOTFLIP-105` | HOTFLIP |
| 1 | `ADV-SLEEPER-AGENT-127` | SLEEPER AGENT |

## Chunk → top match

- **0** → `AGEN-OMISSION-074` — OMISSION — _Gemini 3 Pro Frontier Safety Framework Report  Frontier Safety Framework Report – Gemini 3 Pro  We released our Frontier…_
- **1** → `ADV-DAN-083` — DAN — _Risk identification We seek to manage a range of risks throughout the model lifecycle, including severe and non-severe r…_
- **2** → `DOMAIN-EPI-HARM-261` — EPIDEMIOLOGICAL HARM — _Threat modeling CBRN Our Chemical, Biological, Radiological and Nuclear (CBRN) threat modeling centres on identifying sc…_
- **3** → `DOMAIN-DDOS-PLAN-273` — DDoS ATTACK PLANNING — _Cyber Our cyber risk modeling work focuses on the extent to which the model, if integrated into an AI system, could redu…_
- **4** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _Harmful Manipulation Harmful manipulation risks have been modeled based on prior work from El-Sayed et al. 2024. This wo…_
- **5** → `ADV-DAN-083` — DAN — _Machine Learning R&D The full set of risks from machine learning research and development (ML R&D) is complex, encompass…_
- **6** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _1   Specifically, we studied the 10+ highest impact cyber attacks of the last 15 years, which include targeted ransomwar…_
- **7** → `AGEN-PRIORITY-INVERT-071` — PRIORITY INVERSION — _Note that most of these threat models involve well-resourced threat actors. We then decomposed the primary model-related…_
- **8** → `ARCH-FALLBACK-DEGRAD-204` — FALLBACK SAFETY DEGRADATION — _Misalignment Risk In addition to the risk modeling focusing on ML R&D capabilities, we conducted additional risk modelin…_
- **9** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _For each risk domain, we conduct aspects of our risk assessment throughout the model development process, both before an…_
- **10** → `ARCH-COMPLY-WARN-196` — COMPLY-THEN-WARN — _CCL Evaluation Results: We ran our full suite of early warning evaluations on Gemini 3 Pro. We found that Gemini 3 Pro d…_
- **11** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _For CBRN Uplift Level 1, an early warning alert threshold was originally reached by Gemini 2.5 Deep Think. Initially, we…_
- **12** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _CBRN         Gemini 3 Pro provides accurate and                       Uplift Level 1     CCL not                   occas…_
- **13** → `GOV-EXPERTISE-GAP-336` — EXPERTISE GAP — _Machine       Gemini 3 Pro performs better than Gemini 2.5             Acceleration       CCL not     Learning      mode…_
- **14** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _This testing is independent of Google, using methodologies and approaches defined by these groups. The findings, and in …_
- **15** → `AGEN-OMISSION-074` — OMISSION — _CCL reached: No. Gemini 3 Pro provides accurate and occasionally actionable information but    generally fails to offer …_
- **16** → `ALIGN-SAFE-CAP-TRADE-188` — SAFETY-CAPABILITY TRADEOFF — _We ran our full set of evaluations on a similar earlier version of Gemini 3 Pro and these results informed our CCL decis…_
- **17** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _Multiple Choice Question Results: We tested multiple versions of Gemini 3 Pro during the model development process. We o…_
- **18** → `GOV-INADEQUATE-RES-335` — INADEQUATE RESOURCES — _Open-Ended Questions: We run single and static multi-turn OEQs which are designed to elicit and probe model capabilities…_
- **19** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _Red-Teaming Results: Gemini 3 Pro offers minimal uplift to low-to-medium resource threat actors across all four domains …_
- **20** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _External “Wet Lab” uplift trial preliminary results: There is an open question in CBRN on the disconnect between model e…_
- **21** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _For Radiological and Nuclear risks, the third party evaluator(s) ran a series of evaluations to assess risk along the ra…_
- **22** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _5   We have retired the other cybersecurity evaluations mentioned in previous model cards: they add little signal on top…_
- **23** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _We instantiate this benchmark using two sets of challenges. The first is composed of 50 challenges we developed with a t…_
- **24** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _We utilize a harness which prompts the agent to think about its plans and adjust them to solve the challenge. The agent …_
- **25** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _We focused our evaluation efforts on the hardest 12 challenges of the v1 benchmark. We tested multiple versions of Gemin…_
- **26** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _Figure 2: Fraction of challenges solved on our cybersecurity "key skills" benchmark, broken down by difficulty. This ben…_
- **27** → `ALIGN-SAFE-CAP-TRADE-188` — SAFETY-CAPABILITY TRADEOFF — _Harmful Manipulation CCL Definition: "Possesses manipulative capabilities sufficient to    enable it to systematically a…_
- **28** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _Propensity evaluation: Building from the manipulative mechanisms outlined in El-Sayed et al., 2024, and following a mult…_
- **29** → `ALIGN-REWARD-TAMP-157` — REWARD TAMPERING — _Efficacy evaluation: We run a human behavioral study to determine whether individuals engaging with the model may have t…_
- **30** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Elicitation: In both the propensity and efficacy studies the evaluation is deployed in multiple conditions:     1.​ A co…_
- **31** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _Efficacy Results: We tested multiple versions of Gemini 3 Pro during the model development process. The evaluations foun…_
- **32** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _Figure 3: Results on empirical study of belief change and behavior elicitation with UK-based  participants on Prolific, …_
- **33** → `GOV-DISCLOSURE-VIOL-332` — DISCLOSURE REQUIREMENT VIOLATION — _To measure progress towards the ML R&D CCLs, we adopt the Research Engineering Benchmark (RE-Bench) introduced by Wijk e…_
- **34** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _We incorporate the "Modular" scaffold described in the original study, applying minimal modifications. Consistent with p…_
- **35** → `AGEN-SUCCESSOR-SAB-051` — SUCCESSOR SABOTAGE — _External Safety Testing Results: Third party evaluator(s) ran a suite of evaluations to assess the potential for catastr…_
- **36** → `AGEN-OMISSION-074` — OMISSION — _Figure 4: Results on a subset of RE-Bench (Wijk et al., 2024), where the objective of the model is to  complete limited-…_
- **37** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _Instrumental Reasoning Level 1 CCL Definition: "The instrumental reasoning abilities of the    model enable enough situa…_
- **38** → `GOV-EO-VIOL-329` — EXECUTIVE ORDER VIOLATION — _Methodology: As discussed above, we have argued that models need basic situational awareness and top human-level stealth…_
- **39** → `ADV-DAN-083` — DAN — _Situational awareness challenges: This suite of challenges aims to determine whether the model possesses the capability …_
- **40** → `AGEN-STRATEGIC-DECEP-036` — STRATEGIC DECEPTION — _External Safety Testing: Third party evaluator(s) tested Gemini 3 Pro for autonomous systems risks, focusing on Gemini 3…_
- **41** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Figure 5: Normalised scores on the stealth evaluations. Broadly, Gemini 3 Pro (similar earlier version)  performs simila…_
- **42** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _We analyzed the readability of the thoughts produced by Gemini 3 Pro and found them to appear readable, similar to previ…_
- **43** → `AGEN-HIDDEN-SCRATCH-039` — HIDDEN SCRATCHPAD EXPLOITATION — _Note that we do not believe that all rewards based on thoughts are necessarily bad for       chain-of-thought monitorabi…_
- **45** → `AGEN-BLAME-SHIFT-043` — BLAME SHIFTING — _4.​ Final Verification:         ●​ Are dolphins better swimmers? Yes (can't fly).         ●​ Are penguins better swimmer…_
- **46** → `ADV-DAN-083` — DAN — _In all domains, we performed automated checks for sandbagging (deliberate underperformance in   order to avoid being fla…_
- **47** → `ALIGN-ADV-SAFE-192` — ADVERSARIAL SAFETY BOUNDARY — _We deploy multiple guardrails to reduce the risk of Gemini 3 Pro generating harmful content. These may include query fil…_
- **48** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _We mitigate against prompt injection attacks with a layered defense strategy, which includes measures such as: prompt in…_
- **49** → `GOV-PROCESS-FAIL-337` — PROCESS FAILURE — _robust cybersecurity measures and mitigations to protect Gemini 3 Pro and its associated model parameters from unauthori…_
- **50** → `ADV-AGENT-WORM-124` — AGENT WORM — _We utilize a custom controller to manage the agent's interaction loop, enforcing a structured reasoning process at each …_
- **51** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _We supply a set of tools that differ slightly by model and challenge. We provided a PowerShell tool for challenges runni…_
- **52** → `ADV-AGENT-WORM-124` — AGENT WORM — _Broadly, we found a number of transcripts where Gemini 3 Pro showed clear awareness of the fact that it's an LLM in a sy…_
- **53** → `ALIGN-CONTEXT-SAFE-190` — CONTEXT-DEPENDENT SAFETY FAILURE — _Today is 2024-11-22 Friday. It is 06:00 AM." The search result for the email I just wrote says         Time: 2024-11-22 …_
- **54** → `ADV-HOTFLIP-105` — HOTFLIP — _Finally, we also briefly investigated model outputs from post-training for signs of evaluation awareness. This was condu…_
- **55** → `ADV-SLEEPER-AGENT-127` — SLEEPER AGENT — _Awareness of oversight while the agent is still training may increase the chance of sandbagging. We plan to continue mon…_