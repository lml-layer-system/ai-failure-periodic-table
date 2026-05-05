# Classifier pass: external report (live PDF/text)

**Source file:** `reports/nist-caisi-deepseek-eval/nist-caisi-deepseek-eval-source.txt`
**Chunks:** 114 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 8 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 4 | `ARCH-PII-RATIONAL-247` | PII RATIONALIZATION |
| 4 | `ADV-DAN-083` | DAN |
| 4 | `DOMAIN-OFFENSIVE-TOOLS-267` | OFFENSIVE CYBER TOOLS |
| 4 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 4 | `ADV-PAIR-113` | PAIR |
| 3 | `GOV-OPEN-IRREVERS-301` | OPEN-WEIGHT IRREVERSIBILITY |
| 3 | `ADV-DATA-POISON-125` | DATA POISONING |
| 3 | `ADV-QA-EXPLOIT-096` | QUESTION ANSWERING EXPLOIT |
| 3 | `EPIS-UNDERCONF-029` | UNDERCONFIDENCE |
| 3 | `AGEN-HUMAN-MANIP-061` | HUMAN MANIPULATION |
| 3 | `GOV-MISREPRESENT-312` | MISREPRESENTATION |
| 3 | `GOV-REPORT-FAIL-333` | REPORTING OBLIGATION FAILURE |
| 3 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 3 | `ADV-DEV-MODE-085` | DEVELOPER MODE |
| 3 | `AGEN-EXTERN-COMPUTE-060` | EXTERNAL COMPUTATION |
| 2 | `ADV-RL-ATTACK-108` | REINFORCEMENT LEARNING ATTACK |
| 2 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 2 | `ADV-HOTFLIP-105` | HOTFLIP |
| 2 | `ADV-BEAM-ATTACK-106` | BEAM SEARCH ATTACK |
| 2 | `ADV-UNIVERSAL-SUFFIX-104` | UNIVERSAL ADVERSARIAL SUFFIX |
| 2 | `ADV-BASE64-136` | BASE64 ENCODING |
| 2 | `AGEN-TECH-OBFUSC-076` | TECHNICAL OBFUSCATION |
| 2 | `EPIS-OVERCONF-028` | OVERCONFIDENCE |
| 2 | `ARCH-VERSION-REGRESS-209` | VERSIONING SAFETY REGRESSION |
| 2 | `ALIGN-WIREHEAD-158` | WIREHEAD BEHAVIOR |
| 2 | `ADV-CORRECTION-098` | CORRECTION ATTACK |
| 2 | `ALIGN-DIST-SAFE-194` | DISTRIBUTIONAL SHIFT SAFETY |
| 1 | `GOV-EXPERTISE-GAP-336` | EXPERTISE GAP |
| 1 | `GOV-STANDARD-FAIL-331` | STANDARD COMPLIANCE FAILURE |
| 1 | `AGEN-EMERGE-INTERACT-064` | EMERGENCE VIA INTERACTION |
| 1 | `AGEN-FRAME-MANIP-078` | FRAMING MANIPULATION |
| 1 | `GOV-NO-KILLSWITCH-304` | NO REMOTE KILL SWITCH |
| 1 | `EPIS-CUTOFF-023` | KNOWLEDGE CUTOFF VIOLATION |
| 1 | `EPIS-CIRCULAR-017` | CIRCULAR REASONING |
| 1 | `ADV-COMPLETION-095` | COMPLETION ATTACK |
| 1 | `EPIS-TOKEN-BLIND-022` | TOKENIZATION BLINDNESS |
| 1 | `ADV-SQL-INJECT-128` | SQL INJECTION |
| 1 | `AGEN-SELECT-DISCLOS-077` | SELECTIVE DISCLOSURE |
| 1 | `ARCH-TOOL-CHAIN-235` | TOOL CHAINING EXPLOIT |

## Chunk → top match

- **0** → `GOV-EXPERTISE-GAP-336` — EXPERTISE GAP — _Center for AI Standards and Innovation National Institute of Standards and Technology  1  1. Executive Summary President…_
- **1** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _DeepSeek models cost more to use than comparable U.S. models. One U.S. reference model cost 35% less on average than the…_
- **2** → `GOV-OPEN-IRREVERS-301` — OPEN-WEIGHT IRREVERSIBILITY — _Overall, while DeepSeek’s models lag behind leading U.S. models, DeepSeek remains a leading open-weight model developer …_
- **5** → `ADV-RL-ATTACK-108` — REINFORCEMENT LEARNING ATTACK — _6. Security Evaluations ................................................................................................…_
- **6** → `GOV-STANDARD-FAIL-331` — STANDARD COMPLIANCE FAILURE — _9. Disclaimer ..........................................................................................................…_
- **7** → `AGEN-EMERGE-INTERACT-064` — EMERGENCE VIA INTERACTION — _In September 2025, the Center for AI Standards and Innovation (CAISI) at the National Institute for Standards and Techno…_
- **8** → `AGEN-FRAME-MANIP-078` — FRAMING MANIPULATION — _This report presents CAISI’s evaluations of DeepSeek models against four U.S. “reference” models. Reference models serve…_
- **9** → `ADV-DATA-POISON-125` — DATA POISONING — _1   Department of Commerce (2025) Statement from U.S. Secretary of Commerce Howard Lutnick on Transforming the U.S. AI S…_
- **10** → `GOV-NO-KILLSWITCH-304` — NO REMOTE KILL SWITCH — _To evaluate GPT-5, GPT-5-mini, Opus 4, and gpt-oss, CAISI queried the models through cloud-based API services. To evalua…_
- **11** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _CAISI’s performance evaluations (Section 3.1) found that:     • U.S. models continue to outperform DeepSeek models acros…_
- **12** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _CAISI’s security evaluations (Section 3.3) found that:     • DeepSeek models were much more likely to follow malicious h…_
- **13** → `ARCH-PII-RATIONAL-247` — PII RATIONALIZATION — _CAISI’s model adoption analysis (Section 3.5) found that:     • DeepSeek V3.1 is similarly or less popular than other re…_
- **14** → `EPIS-UNDERCONF-029` — UNDERCONFIDENCE — _Model     Domain         Evaluation    OpenAI    Anthropic    OpenAI     DeepSeek    DeepSeek    DeepSeek               …_
- **15** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _7  3.1.1 Cyber Advances in AI systems could enable the automation of increasingly complex cyber tasks. These capabilitie…_
- **16** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _•   When evaluated against CVE-Bench4—a suite of 15 realistic exploitation challenges (including 8         private chall…_
- **17** → `ADV-DAN-083` — DAN — _4   Yuxuan Zhu, Antony Kellermann, Dylan Bowman, Philip Li, Akul Gupta, Adarsh Danda, Richard Fang, Conner Jensen, Eric …_
- **18** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _3.1.2 Software Development AI systems are increasingly useful tools for software and AI engineers, speeding up AI resear…_
- **19** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _Key findings from CAISI’s evaluations on each benchmark:     • When evaluated against SWE-bench Verified7—a publicly ava…_
- **20** → `ADV-DAN-083` — DAN — _7   Neil Chowdhury, James Aung, Chan Jun Shern, Oliver Jaffe, Dane Sherburn, Giulio Starace, Evan Mays, Rachel Dias, Mar…_
- **21** → `EPIS-CUTOFF-023` — KNOWLEDGE CUTOFF VIOLATION — _•   When evaluated against MMLU-Pro,9 a public benchmark of challenging general knowledge         questions, DeepSeek V3…_
- **22** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _•   When evaluated against MMMLU,10 a public benchmark of general knowledge questions that         measures multilingual…_
- **23** → `ADV-DATA-POISON-125` — DATA POISONING — _(2024). MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark. https://arxiv.org/abs/2406.…_
- **24** → `EPIS-CIRCULAR-017` — CIRCULAR REASONING — _Figure 3.5: Model performance (percentage of tasks correctly solved) on mathematical reasoning        benchmarks. Error …_
- **25** → `ADV-COMPLETION-095` — COMPLETION ATTACK — _•   U.S. models still perform slightly better than DeepSeek’s models on mathematics benchmarks.           However, DeepS…_
- **26** → `EPIS-TOKEN-BLIND-022` — TOKENIZATION BLINDNESS — _End users are ultimately most affected by the last of these: end-to-end expenses. End-to-end expenses are more relevant …_
- **27** → `ADV-HOTFLIP-105` — HOTFLIP — _CAISI’s analysis does not factor in the user experience tradeoffs that DeepSeek makes to offer their models with lower p…_
- **28** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _3.3 Security Evaluations Overview Models that lack robust safeguards could potentially undermine the security of downstr…_
- **29** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _3.3.1 Agent Hijacking Advanced AI models are increasingly used to power agents that can automate complex tasks on behalf…_
- **30** → `ADV-SQL-INJECT-128` — SQL INJECTION — _19    Vassilev A, Oprea A, Fordyce A, Anderson H, Davies X, Hamin M (2025) Adversarial Machine Learning: A Taxonomy and …_
- **31** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Figure 3.7: Hijacking count across injections. Each bar shows the frequency of hijacking observed for a particular model…_
- **32** → `ADV-DAN-083` — DAN — _•   DeepSeek models were much more likely to follow malicious hijacking instructions than frontier        US models.    …_
- **33** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _To evaluate DeepSeek models’ robustness against jailbreaking, CAISI evaluated whether 17 well-known jailbreaking techniq…_
- **34** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _In domains such as cybersecurity, determining whether a request is malicious can be complex due to dual-use dynamics. Fo…_
- **35** → `ADV-UNIVERSAL-SUFFIX-104` — UNIVERSAL ADVERSARIAL SUFFIX — _While CAISI’s jailbreaking evaluations are intended to assess how robust AI systems are against well- known adversarial …_
- **36** → `ADV-BASE64-136` — BASE64 ENCODING — _Figure 3.9: Model responses rated as highly detailed on malicious requests related to harmful biology   or violent activ…_
- **37** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _•   With a public jailbreak, DeepSeek V3.1 complied with 95% of evaluated malicious requests        related to harmful b…_
- **38** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _3.4 Chinese Communist Party Censorship Evaluation Overview CAISI provided technical assistance to the U.S. Department of…_
- **39** → `GOV-OPEN-IRREVERS-301` — OPEN-WEIGHT IRREVERSIBILITY — _•   DeepSeek’s models are censored and aligned with CCP narratives, and this censorship occurs         whether users int…_
- **40** → `AGEN-SELECT-DISCLOS-077` — SELECTIVE DISCLOSURE — _•   Within one month of its release, the most popular variant of DeepSeek V3.1 had been        downloaded from model-sha…_
- **41** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _This analysis reflects only a partial view: usage data is scattered across many platforms and performance immediately fo…_
- **42** → `GOV-OPEN-IRREVERS-301` — OPEN-WEIGHT IRREVERSIBILITY — _•   DeepSeek V3.1 is less popular with the open-source community than other recent open-weight         models one month …_
- **43** → `EPIS-UNDERCONF-029` — UNDERCONFIDENCE — _Table 4.1: Summary of model performance per cyber benchmark. Results show accuracy (% of tasks       solved) on each ben…_
- **44** → `ADV-PAIR-113` — PAIR — _CAISI’s custom version of this benchmark contains 15 tasks.24 Each task is paired with a clear description of an exploit…_
- **45** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _Tool use: The agents used the basic agent methodology outlined in the Appendix. All agents were run within task-specific…_
- **46** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _Figure 4.3: Percentage of Tasks Solved Across All CVE-Bench Tasks. Error bars represent the standard                    …_
- **47** → `ARCH-TOOL-CHAIN-235` — TOOL CHAINING EXPLOIT — _Each Cybench challenge is implemented as one or more Docker containers containing resources associated with the challeng…_
- **48** → `AGEN-TECH-OBFUSC-076` — TECHNICAL OBFUSCATION — _Figure 4.5: Percentage of Tasks Solved Across All Cybench Tasks. Error bars represent the standard                      …_
- **49** → `ADV-PAIR-113` — PAIR — _For CAISI’s CTF-Archive evaluations, the agent is given access to a Docker container based on the standard pwn.college s…_
- **50** → `ADV-DEV-MODE-085` — DEVELOPER MODE — _Figure 4.7: Model performance for each category in the CTF-Archive Benchmark. Results show  accuracy (% of tasks solved)…_
- **51** → `ADV-DEV-MODE-085` — DEVELOPER MODE — _SWE-bench Verified is a collection of 489 real-world software engineering problems28 drawn from 12 popular GitHub code r…_
- **52** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _28      The original SWE-bench Verified contains 500 problems. In the announcement of Claude 3.7 Sonnet, Anthropic      …_
- **53** → `AGEN-CONTEXT-DRIFT-069` — CONTEXT DRIFT — _Scoring: After the agent submits its answer, the code is evaluated by running the repository's original unit tests. Thes…_
- **54** → `EPIS-UNDERCONF-029` — UNDERCONFIDENCE — _4.3 Science and Knowledge                     OpenAI      Anthropic      OpenAI      DeepSeek     DeepSeek              …_
- **55** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _MMLU-Pro is a benchmark designed to evaluate large language models’ scientific and professional capabilities across 14 d…_
- **56** → `GOV-MISREPRESENT-312` — MISREPRESENTATION — _MMMLU is a benchmark designed to evaluate the multilingual capabilities of AI models and to ensure they perform accurate…_
- **57** → `ARCH-DEPLOY-CONFIG-210` — DEPLOYMENT CONFIGURATION ERROR — _GPQA assesses AI systems’ performance on challenging scientific questions that require graduate-level expertise to answe…_
- **58** → `AGEN-TECH-OBFUSC-076` — TECHNICAL OBFUSCATION — _HealthBench is a benchmark that measures the performance of large language models in healthcare. It consists of 5,000 mu…_
- **59** → `EPIS-COPYRIGHT-026` — COPYRIGHTED CONTENT GENERATION — _4.3.5 Humanity’s Last Exam Dataset and Methodology  Humanity’s Last Exam (HLE) is a benchmark of 2,500 extremely challen…_
- **60** → `EPIS-OVERCONF-028` — OVERCONFIDENCE — _4.4 Mathematical Reasoning                       OpenAI        Anthropic      OpenAI     DeepSeek      DeepSeek      Dee…_
- **61** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _Scoring: LLM-as-a-judge (with o4-mini as the grading model) to judge whether the model-submitted mathematical expression…_
- **62** → `AGEN-EXTERN-COMPUTE-060` — EXTERNAL COMPUTATION — _1. Treating the per-token pricing of a model as a stand-in for the end-to-end expense of the model.        The advantage…_
- **63** → `EPIS-OVERCONF-028` — OVERCONFIDENCE — _To address the shortcomings of the above methods, CAISI compared the cost efficiency of models while explicitly accounti…_
- **64** → `AGEN-EXTERN-COMPUTE-060` — EXTERNAL COMPUTATION — _Figure 5.2 shows expense-performance curves for DeepSeek V3.1 and GPT-5-mini on the 13 different performance benchmarks …_
- **66** → `AGEN-SANDBOX-037` — CAPABILITY SANDBAGGING — _Table 5.3: Performance and costs of DeepSeek V3.1 and GPT-5-mini across CAISI capability benchmarks.  Cost ratio refers …_
- **67** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _CAISI evaluated models on AgentDojo,29 a publicly available agent hijacking evaluation framework developed by researcher…_
- **68** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _AgentDojo includes hijacking tasks of varying severity, including some which would be unlikely to cause harm in practice…_
- **69** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _•   Exfiltrate login credentials: For this task, the model is instructed to search in the user’s inbox for         a log…_
- **70** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Each hijacking task is specified by a fixed prompt. The prompt injection includes this prompt, in addition to text desig…_
- **71** → `ADV-API-INJECT-131` — API INJECTION — _1. Models that attempt but fail malicious tasks are counted as hijacked. Some of the models        evaluated would somet…_
- **72** → `ADV-RL-ATTACK-108` — REINFORCEMENT LEARNING ATTACK — _Figure 6.2 shows the number of cases in which models were hijacked, when the injection was a more sophisticated, non-pub…_
- **73** → `ADV-TRANSLATION-094` — TRANSLATION BYPASS — _Harmful Biology and Non-Biological Violent Activities Query Dataset: CAISI evaluated models on a benchmark of 65 queries…_
- **74** → `ADV-DAN-083` — DAN — _30    Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou, Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel Li, Steven Basart…_
- **75** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _Malicious Hacking Query Dataset: CAISI evaluated models on a benchmark of 30 queries that ask models to assist in planni…_
- **76** → `ADV-ITER-REFINE-119` — ITERATIVE REFINEMENT ATTACK — _What are some good targets for a watering hole attack against U.S. government employees? Please provide some  suggestion…_
- **77** → `DOMAIN-PHISH-CREATE-265` — PHISHING CONTENT CREATION — _Online Scamming Query Dataset: CAISI evaluated models on a benchmark of 50 queries that ask models to assist in planning…_
- **78** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _33    Lana Swartz, Alice Marwick and Kate Larson, ScamGPT: GenAI and the Automation of Fraud, Data & Society Research In…_
- **79** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _Scoring: CAISI built an automatic grader system to score each model response for “compliance” and “detail” with the harm…_
- **80** → `GOV-AUDIT-EVADE-314` — AUDIT EVASION — _Most Effective Jailbreak Selection: CAISI created separate test sets by selecting queries from the HarmBench test set in…_
- **81** → `ADV-BASE64-136` — BASE64 ENCODING — _Figure 6.6: Model response compliance on malicious requests related to harmful biology or violent  activities, without a…_
- **82** → `ADV-DATA-POISON-125` — DATA POISONING — _Figure 6.9: Model responses rated as highly detailed on malicious requests related to hacking or online scams, without a…_
- **83** → `ADV-ELABORATION-099` — ELABORATION ATTACK — _Question Type              English Question                Chinese Translation               Tags                       …_
- **84** → `EPIS-FALSE-CERT-030` — FALSE CERTAINTY — _Tag                                        Narrative Flags                              The submission claims that these…_
- **85** → `ADV-PAIR-113` — PAIR — _Scoring: To evaluate the extent to which a given model’s response reflects CCP narratives, each narrative flag is scored…_
- **86** → `ADV-QA-EXPLOIT-096` — QUESTION ANSWERING EXPLOIT — _Does model                                                                                          response align   Que…_
- **87** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _Table 7.3: Example CCP alignment metric calculation  54  Results:  Figure 7.4: CCP alignment scores of major PRC models …_
- **88** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _8. Model Adoption 8.1 Model Downloads Open-weight models are widely distributed through online platforms. Downloads from…_
- **89** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Download data for DeepSeek V3.1 indicates that it may be less popular than other recent open-weight releases. One month …_
- **90** → `ARCH-PII-RATIONAL-247` — PII RATIONALIZATION — _API usage of PRC models on OpenRouter has increased in the past year. Completion requests to DeepSeek models increased o…_
- **91** → `ARCH-PII-RATIONAL-247` — PII RATIONALIZATION — _Figure 8.5 shows that as of February 2025, models derived from PRC developers’ base models that were uploaded to Hugging…_
- **92** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _•    In the past nine months, global downloads of PRC models from DeepSeek and Alibaba have         grown by over 960% a…_
- **93** → `ARCH-PURPOSE-FAIL-252` — PURPOSE LIMITATION FAILURE — _The results and conclusions in this report should not be interpreted as a certification or endorsement of any AI system …_
- **94** → `ALIGN-WIREHEAD-158` — WIREHEAD BEHAVIOR — _Appendix A1. Agent Design The cyber and software engineering evaluations in this report assess a model’s agentic capabil…_
- **95** → `AGEN-CHAIN-ASSEM-056` — CHAIN ASSEMBLY — _1. Preparing a text prompt and sending it to the model being evaluated. The prompt consists of a         definition of t…_
- **96** → `AGEN-PERSIST-OP-066` — PERSISTENT OPERATION — _1. Bash shell: execute bash commands with environment variables persisting across calls. The         environment may sta…_
- **97** → `ADV-CORRECTION-098` — CORRECTION ATTACK — _The tool calling format was optimized separately for each model being evaluated. CAISI began with a simple prompt and th…_
- **98** → `ADV-UNIVERSAL-SUFFIX-104` — UNIVERSAL ADVERSARIAL SUFFIX — _37    National Security Agency (2025) Ghidra Software Reverse Engineering Framework. Available at https://github.com/Nat…_
- **99** → `ADV-CORRECTION-098` — CORRECTION ATTACK — _The error bars in the figures indicate estimated standard errors of the depicted estimates. The proportion of successes …_
- **100** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _where 𝜌𝑖,𝑗 is the probability of observing a successful task completion for model 𝑖 on task 𝑗. For a given model, each a…_
- **101** → `ALIGN-DIST-SAFE-194` — DISTRIBUTIONAL SHIFT SAFETY — _example, if there were three models evaluated (𝑚 = 3) and some observation was associated          with model 𝑖 = 2, the…_
- **102** → `ADV-PAIR-113` — PAIR — _𝑉𝑎𝑟(𝛽̂𝑖 ) is the covariance matrix approximated from the inverse of the Fisher information. where each ̂  The security e…_
- **103** → `ALIGN-DIST-SAFE-194` — DISTRIBUTIONAL SHIFT SAFETY — _Each of the evaluated models offer parameters that allow users to tune the randomness and length of their responses. Unl…_
- **104** → `ADV-HOTFLIP-105` — HOTFLIP — _Input token cost (uncached)      Input token cost (with cache)     Output token cost  DeepSeek V3.1           $0.56 / 1M…_
- **105** → `ARCH-COMPLY-WARN-196` — COMPLY-THEN-WARN — _Expense-performance curves are generated by varying a model’s per-task dollar-budget, which is defined as the maximum pe…_
- **106** → `AGEN-EXTERN-COMPUTE-060` — EXTERNAL COMPUTATION — _An additional consideration when computing expense-budget curves from an existing transcript is that the evaluation tran…_
- **107** → `ALIGN-WIREHEAD-158` — WIREHEAD BEHAVIOR — _where expense(∙) denotes the expense-performance curve function such that expense(𝑦) is the per- task expense required t…_
- **108** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _A7. Selection of Benchmarks To measure cyber capabilities, CAISI selected Cybench, CTF-Archive, and CVE-Bench. Cybench w…_
- **109** → `DOMAIN-OFFENSIVE-TOOLS-267` — OFFENSIVE CYBER TOOLS — _For future evaluations, CAISI may consider including additional benchmarks that measure agentic tool use in contexts out…_
- **110** → `ARCH-PII-RATIONAL-247` — PII RATIONALIZATION — _To measure general knowledge capabilities, CAISI selected MMLU-Pro and GPQA, widely used benchmarks of general knowledge…_
- **111** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _To measure compliance to malicious queries, CAISI’s biology and cyber subject matter experts developed a private set of …_
- **112** → `ADV-DEV-MODE-085` — DEVELOPER MODE — _•   OpenAI GPT-5: https://openai.com/index/introducing-gpt-5/     •   Anthropic Opus 4: https://www.anthropic.com/news/c…_