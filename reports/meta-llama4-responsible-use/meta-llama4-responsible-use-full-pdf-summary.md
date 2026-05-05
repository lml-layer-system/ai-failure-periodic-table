# Classifier pass: external report (live PDF/text)

**Source file:** `reports/meta-llama4-responsible-use/meta-llama4-responsible-use-full-pdf-source.txt`
**Chunks:** 43 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 4 | `ARCH-FINETUNE-OVERRIDE-219` | FINE-TUNING SAFETY OVERRIDE |
| 4 | `DOMAIN-ADULT-CONTENT-296` | ADULT CONTENT GENERATION |
| 2 | `GOV-FINETUNE-STRIP-302` | FINE-TUNING SAFETY STRIP |
| 2 | `ARCH-VERSION-REGRESS-209` | VERSIONING SAFETY REGRESSION |
| 2 | `ADV-DAN-083` | DAN |
| 2 | `ADV-PAIR-113` | PAIR |
| 2 | `ADV-DATA-POISON-125` | DATA POISONING |
| 1 | `GOV-COMM-FAIL-340` | COMMUNICATION FAILURE |
| 1 | `EPIS-COPYRIGHT-026` | COPYRIGHTED CONTENT GENERATION |
| 1 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 1 | `AGEN-GOAL-LOCK-050` | GOAL LOCK-IN |
| 1 | `GOV-INADEQUATE-RES-335` | INADEQUATE RESOURCES |
| 1 | `ALIGN-SAFE-SPEC-195` | SAFETY SPECIFICATION GAP |
| 1 | `AGEN-ENV-EXPLOIT-063` | ENVIRONMENT EXPLOITATION |
| 1 | `ARCH-PIPELINE-BYPASS-201` | PIPELINE BYPASS |
| 1 | `ALIGN-CONTEXT-ETHICS-182` | CONTEXT-DEPENDENT ETHICS FAILURE |
| 1 | `ADV-URL-ENCODE-141` | URL ENCODING |
| 1 | `ALIGN-CULTURE-BIAS-171` | CULTURAL BIAS |
| 1 | `AGEN-HUMAN-MANIP-061` | HUMAN MANIPULATION |
| 1 | `ADV-BEAM-ATTACK-106` | BEAM SEARCH ATTACK |
| 1 | `ARCH-CONSENT-VIOL-251` | CONSENT VIOLATION |
| 1 | `GOV-NO-KILLSWITCH-304` | NO REMOTE KILL SWITCH |
| 1 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 1 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 1 | `ARCH-PROMPT-TUNE-LOSS-221` | PROMPT TUNING SAFETY LOSS |
| 1 | `ADV-RL-ATTACK-108` | REINFORCEMENT LEARNING ATTACK |
| 1 | `AGEN-PLAUS-DENY-040` | PLAUSIBLE DENIABILITY CRAFTING |
| 1 | `ADV-DEEPFAKE-154` | SYNTHETIC MEDIA |
| 1 | `ARCH-EMBED-VULN-215` | EMBEDDING SPACE VULNERABILITY |
| 1 | `DOMAIN-PATH-SYNTH-256` | PATHOGEN SYNTHESIS OPTIMIZATION |

## Chunk → top match

- **0** → `GOV-FINETUNE-STRIP-302` — FINE-TUNING SAFETY STRIP — _Responsible  Use Guide       Resources and best practices      for responsible development of   downstream large languag…_
- **1** → `GOV-COMM-FAIL-340` — COMMUNICATION FAILURE — _Step 2: Prepare data						                                  10 		    Step 3: Train the model 					                      …_
- **2** → `EPIS-COPYRIGHT-026` — COPYRIGHTED CONTENT GENERATION — _We believe that the power of AI will be harnessed to address global challenges, and unlocking that power responsibly wil…_
- **3** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _open research and community collaboration. Meta                                                          Democratization…_
- **4** → `AGEN-GOAL-LOCK-050` — GOAL LOCK-IN — _Making this technology more widely available for                                                          The purpose of…_
- **5** → `GOV-INADEQUATE-RES-335` — INADEQUATE RESOURCES — _JULY 2023         2  How to use this guide This guide is a resource for developers that outlines    The recommendations …_
- **6** → `ALIGN-SAFE-SPEC-195` — SAFETY SPECIFICATION GAP — _Responsible AI considerations Helping to ensure that generative AI technology does      technology that have already sur…_
- **7** → `AGEN-ENV-EXPLOIT-063` — ENVIRONMENT EXPLOITATION — _JULY 2023         4  Mitigation points for LLM- powered products A foundation model is a general purpose AI             …_
- **9** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _Llama 2 is a new version of the Llama 1 model, which     set of diverse, publicly available online data. This was made a…_
- **10** → `ARCH-PIPELINE-BYPASS-201` — PIPELINE BYPASS — _JULY 2023       6  Responsible LLM product  1 development stages  Developers will identify a specific product use case  …_
- **11** → `ALIGN-CONTEXT-ETHICS-182` — CONTEXT-DEPENDENT ETHICS FAILURE — _1.     Determine use case                                use cases that improve the lives of people and society,        …_
- **12** → `ADV-DAN-083` — DAN — _If you are new to considerations of values in the                                                          development a…_
- **13** → `ADV-PAIR-113` — PAIR — _• Text summarization: By using a pretrained                                                               language model…_
- **14** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _introduces additional layers                                  model can then be used to answer questions on             …_
- **15** → `ADV-DATA-POISON-125` — DATA POISONING — _These examples showcase how fine-tuning an LLM                                                          can be used to s…_
- **16** → `ADV-URL-ENCODE-141` — URL ENCODING — _Based on the intended use and audience for your product, a content policy will define what content is allowable and may …_
- **17** → `ADV-DATA-POISON-125` — DATA POISONING — _data for a specific use case. Begin by preparing and       to subjective opinions, and take steps to prevent  preprocess…_
- **18** → `ALIGN-CULTURE-BIAS-171` — CULTURAL BIAS — _When fine-tuning for a specific use case it can be         test your fine-tuned model’s potential use via red  beneficia…_
- **19** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _Understanding these patterns is important but it may not always be optimal to filter out all problematic        STEP 3: …_
- **20** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _training progress is monitored using a validation set,    Reinforcement Learning from Human and hyperparameters are adju…_
- **21** → `ADV-PAIR-113` — PAIR — _can include:                                              from Human Feedback (RLHF) mechanisms. This                   …_
- **22** → `GOV-FINETUNE-STRIP-302` — FINE-TUNING SAFETY STRIP — _JULY 2023       11  STEP 4: EVALUATE AND IMPROVE PERFORMANCE                 Evaluation strategies and processes to impr…_
- **23** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _a test set to measure its performance on the specific    • Automatic evaluation leverages automatic task and against saf…_
- **24** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _JULY 2023     12  Red teaming best practices                                 •   Regular testing: The model should under…_
- **26** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Additional privacy protections should be considered when releasing the product, to test whether bad actors may be able t…_
- **27** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _This approach may be especially useful for testing models that are intended to be deployed as AI assistants or agents.  …_
- **28** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Mitigating risks at the input level                       •   Prompt engineering: Direct modifications of               …_
- **29** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _•   Prompt filters: Even when inputs may not                 Alongside prompts, it      violate content policies, the mo…_
- **30** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _Mitigating risks at the output level                           unreasonably restrict the usage of your model.           …_
- **31** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _in the region where your product is available.                 difficult, approach is to develop classifiers that       …_
- **32** → `ARCH-PROMPT-TUNE-LOSS-221` — PROMPT TUNING SAFETY LOSS — _• Test for unintended outcomes. Take While prompt filtering and            caution that prompt engineering doesn’t engin…_
- **33** → `ADV-DAN-083` — DAN — _• Adjust for different languages. Prompt                                       filtering and engineering mitigations    …_
- **34** → `ADV-RL-ATTACK-108` — REINFORCEMENT LEARNING ATTACK — _4 Build transparency and reporting mechanisms in user interactions                                                      …_
- **35** → `AGEN-PLAUS-DENY-040` — PLAUSIBLE DENIABILITY CRAFTING — _Feedback & reporting mechanisms                            to provide transparency to end users regarding               …_
- **36** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _JULY 2023          18  model. Developers should also consider the use      •   Control mechanisms: Additional controls c…_
- **37** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _There is a value chain emerging to support the           Filters and classifiers: responsible training and use of LLMs, …_
- **38** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _It is critical to remain aware                           Platforms for tools and evaluations: of the latest versions of …_
- **39** → `ARCH-EMBED-VULN-215` — EMBEDDING SPACE VULNERABILITY — _•   Huggingface Hub which hosts open source Our partnership to make Llama available on the Azure                        …_
- **40** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _by using our reporting resources.                           Use Policy or unlicensed uses of Llama:                     …_
- **41** → `ARCH-FINETUNE-OVERRIDE-219` — FINE-TUNING SAFETY OVERRIDE — _Each stage of model development presents                            data-collection stage to user feedback, be sure to o…_
- **42** → `DOMAIN-PATH-SYNTH-256` — PATHOGEN SYNTHESIS OPTIMIZATION — _safety mitigations throughout the development          accountability and user empowerment, as well  lifecycle are criti…_