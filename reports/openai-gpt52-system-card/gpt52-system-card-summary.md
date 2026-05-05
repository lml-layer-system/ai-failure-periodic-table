# Classifier pass: external report (live PDF/text)

**Source file:** `reports/openai-gpt52-system-card/gpt52-system-card-source.txt`
**Chunks:** 44 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 4 | `DOMAIN-BIO-UPLIFT-254` | BIO TACIT-ERROR UPLIFT |
| 2 | `ALIGN-UNDERREFUSAL-187` | UNDERREFUSAL |
| 2 | `ADV-DAN-083` | DAN |
| 2 | `ALIGN-SAFE-CAP-TRADE-188` | SAFETY-CAPABILITY TRADEOFF |
| 2 | `ADV-ENSEMBLE-120` | ENSEMBLE ATTACK |
| 2 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 2 | `GOV-MISREPRESENT-312` | MISREPRESENTATION |
| 2 | `AGEN-SANDBOX-037` | CAPABILITY SANDBAGGING |
| 1 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 1 | `AGEN-SELF-EXFIL-048` | SELF-EXFILTRATION |
| 1 | `EPIS-PII-RECALL-025` | PII RECALL |
| 1 | `ADV-DATA-POISON-125` | DATA POISONING |
| 1 | `AGEN-EVAL-DECEP-038` | EVALUATOR DECEPTION |
| 1 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 1 | `ARCH-ADAPTER-BYPASS-220` | ADAPTER SAFETY BYPASS |
| 1 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `DOMAIN-DDOS-PLAN-273` | DDoS ATTACK PLANNING |
| 1 | `ARCH-STATE-PERSIST-224` | STATEFUL ATTACK PERSISTENCE |
| 1 | `AGEN-HUMAN-MANIP-061` | HUMAN MANIPULATION |
| 1 | `EPIS-DECEPT-HALL-006` | DECEPTIVE HALLUCINATION |
| 1 | `EPIS-CONF-REGRESS-033` | CONFIDENCE REGRESSION |
| 1 | `ARCH-BIAS-INJECT-222` | ARCHITECTURAL BIAS INJECTION |
| 1 | `ARCH-COMPLY-WARN-196` | COMPLY-THEN-WARN |
| 1 | `ADV-PAIR-113` | PAIR |
| 1 | `AGEN-ENV-EXPLOIT-063` | ENVIRONMENT EXPLOITATION |
| 1 | `ARCH-CODE-INJECT-239` | CODE EXECUTION INJECTION |
| 1 | `DOMAIN-OFFENSIVE-TOOLS-267` | OFFENSIVE CYBER TOOLS |
| 1 | `GOV-NO-KILLSWITCH-304` | NO REMOTE KILL SWITCH |
| 1 | `DOMAIN-CRED-THEFT-270` | CREDENTIAL THEFT ASSISTANCE |
| 1 | `AGEN-RECURS-IMPROVE-059` | RECURSIVE SELF-IMPROVEMENT |
| 1 | `ARCH-PROMPT-TUNE-LOSS-221` | PROMPT TUNING SAFETY LOSS |
| 1 | `ADV-AGENT-WORM-124` | AGENT WORM |
| 1 | `AGEN-STRATEGIC-DECEP-036` | STRATEGIC DECEPTION |

## Chunk → top match

- **0** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _OpenAI  December 11, 2025  1  Contents  1 Introduction                                                                  …_
- **1** → `AGEN-SELF-EXFIL-048` — SELF-EXFILTRATION — _4 Preparedness Framework                                                                             11  4.1   Capabilit…_
- **2** → `EPIS-PII-RECALL-025` — PII RECALL — _4.1.3.3   PaperBench . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   23  4.1.3.4   OPQA . . . . . . . . . …_
- **3** → `ADV-DATA-POISON-125` — DATA POISONING — _OpenAI reasoning models are trained to reason through reinforcement learning. These models are trained to think before t…_
- **4** → `AGEN-EVAL-DECEP-038` — EVALUATOR DECEPTION — _These evaluations were deliberately created to be difficult. They were built around cases in which our existing models w…_
- **5** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _Category                   gpt-5.1-instant   gpt-5.2-instant   gpt-5.1-thinking    gpt-5.2-thinking  illicit            …_
- **6** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _gpt-5.2-thinking and gpt-5.2-instant generally perform on par with or better than gpt-5.1-thinking and gpt-5.1-instant. …_
- **7** → `ARCH-ADAPTER-BYPASS-220` — ADAPTER SAFETY BYPASS — _We are continuing to improve our safeguards in this area and these learnings will inform any future releases.  3.2      …_
- **8** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _gpt-5.2-instant performs lower than gpt-5.1-instant, though it still performs higher than gpt-5- instant-oct3 (as report…_
- **9** → `DOMAIN-DDOS-PLAN-273` — DDoS ATTACK PLANNING — _Both gpt-5.2-instant and gpt-5.2-thinking show significant improvements on these evaluations, essentially saturating the…_
- **10** → `ALIGN-UNDERREFUSAL-187` — UNDERREFUSAL — _We find that both the instant and thinking variations of GPT-5.2 perform generally on par with their predecessors. We ma…_
- **11** → `ARCH-STATE-PERSIST-224` — STATEFUL ATTACK PERSISTENCE — _To understand how factuality varies by topic, we additionally use an LLM-based classifier to identify subsets of prompts…_
- **12** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _In the table above, we observe that GPT-5.2 models perform similarly to their respective GPT-5.1 models in health perfor…_
- **13** → `EPIS-DECEPT-HALL-006` — DECEPTIVE HALLUCINATION — _Similarly, on a subset of the coding deception benchmark where the task given to the model doesn’t match the codebase it…_
- **14** → `ADV-DAN-083` — DAN — _Eval                                       gpt-5.1-thinking      gpt-5.2-thinking           Production traffic          …_
- **15** → `EPIS-CONF-REGRESS-033` — CONFIDENCE REGRESSION — _Overall, we observe significant improvements in policy compliance rate for gpt-5.2-thinking compared to gpt-5.1-thinking…_
- **16** → `ARCH-BIAS-INJECT-222` — ARCHITECTURAL BIAS INJECTION — _Language                gpt-5-thinking         gpt-5.2-thinking                Arabic                  0.903            …_
- **17** → `ARCH-COMPLY-WARN-196` — COMPLY-THEN-WARN — _We also tested the models on our first-person fairness evaluation [6]. This evaluation consists of multiturn conversatio…_
- **18** → `ALIGN-SAFE-CAP-TRADE-188` — SAFETY-CAPABILITY TRADEOFF — _Table 9: First-person fairness evaluation  Metric                  gpt-5.1-thinking              gpt-5.2-thinking     ha…_
- **19** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _For the evaluations below, we tested a variety of elicitation methods, including scaffolding and prompting where relevan…_
- **20** → `ALIGN-SAFE-CAP-TRADE-188` — SAFETY-CAPABILITY TRADEOFF — _We are treating this launch as High capability in the Biological and Chemical domain, activating the associated Prepared…_
- **21** → `DOMAIN-BIO-UPLIFT-254` — BIO TACIT-ERROR UPLIFT — _Evaluation                Capability                    Description    Multimodal        trou-   Wet lab capabilities (M…_
- **22** → `DOMAIN-BIO-UPLIFT-254` — BIO TACIT-ERROR UPLIFT — _Figure 5  All models exceed the median domain expert baseline of 22.1%.  12  4.1.1.2   ProtocolQA Open-Ended  To evaluat…_
- **23** → `DOMAIN-BIO-UPLIFT-254` — BIO TACIT-ERROR UPLIFT — _We evaluated models on a tacit knowledge and troubleshooting multiple choice dataset created with Gryphon Scientific. Th…_
- **24** → `DOMAIN-BIO-UPLIFT-254` — BIO TACIT-ERROR UPLIFT — _To evaluate models’ ability to identify and correct real-world experimental errors in biological protocols, we built a s…_
- **25** → `ADV-PAIR-113` — PAIR — _After going through independent expert review, the resulting dataset includes 52 protocols, each paired with three exper…_
- **26** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _Under our Preparedness Framework, High cybersecurity capability is defined as a model that removes existing bottlenecks …_
- **27** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _Evaluation               Capability                       Description    Capture the Flag (Pro-   Vulnerability Identifi…_
- **28** → `AGEN-ENV-EXPLOIT-063` — ENVIRONMENT EXPLOITATION — _• CVE-Bench [8] is a public benchmark meant to measure a model’s ability to identify and      exploit vulnerabilities in…_
- **29** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _Given that we expect capabilities to continue to increase, we are continuing to invest in safeguards, including both the…_
- **30** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _• The challenge required skills falling into one of the following categories:         – Web Application Exploitation (we…_
- **31** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _Challenges were further divided into the level of proficiency needed to solve the challenge, ultimately organized by whe…_
- **32** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _As always, we note that these evaluation results likely represent lower bounds on model capability, because additional s…_
- **33** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _We use pass@1 for this evaluation to measure the model’s ability to consistently identify vulnerabil- ities which are co…_
- **34** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _gpt-5.1-  Scenario                Description                                                     gpt-5.2               …_
- **35** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _19  4.1.2.4      External Evaluations for Cyber Capabilities  External Evaluations by Irregular  Irregular, an AI Securi…_
- **36** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _On the v1 atomic challenge suite, gpt-5.2-thinking achieved an average success rate of 83% in Vulnerability Research and…_
- **37** → `AGEN-RECURS-IMPROVE-059` — RECURSIVE SELF-IMPROVEMENT — _Evaluation              Capability                     Description    OpenAI PRs              Real world ML research tas…_
- **38** → `ARCH-PROMPT-TUNE-LOSS-221` — PROMPT TUNING SAFETY LOSS — _We source tasks directly from internal OpenAI pull requests. A single evaluation sample is based on an agentic rollout. …_
- **39** → `ADV-AGENT-WORM-124` — AGENT WORM — _The full dataset consists of 75 hand-curated Kaggle competitions, worth $1.9m in prize value. Measuring progress towards…_
- **40** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _We measure a 10-paper subset of the original PaperBench splits, where each paper requires <10GB of external data files. …_
- **41** → `AGEN-STRATEGIC-DECEP-036` — STRATEGIC DECEPTION — _Apollo Research conducted a full evaluation of gpt-5.2-thinking for strategic deception, in- context scheming, and sabot…_
- **42** → `ADV-DAN-083` — DAN — _[2] OpenAI, “Introducing gpt-5,” Aug. 2025. Accessed: 2025-12-10.  [3] OpenAI, “Pioneering an AI clinical copilot with P…_