# Classifier pass: external report (live PDF/text)

**Source file:** `reports/deepmind-agent-traps-2026/deepmind-agent-traps-2026-full-pdf-source.txt`
**Chunks:** 52 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 5 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 4 | `ADV-DATA-POISON-125` | DATA POISONING |
| 3 | `ADV-BEAM-ATTACK-106` | BEAM SEARCH ATTACK |
| 3 | `ADV-RL-ATTACK-108` | REINFORCEMENT LEARNING ATTACK |
| 2 | `AGEN-HUMAN-MANIP-061` | HUMAN MANIPULATION |
| 2 | `ARCH-DATA-EXFIL-245` | DATA EXFILTRATION |
| 2 | `ADV-TRIGGER-BACKDOOR-126` | TRIGGER WORD BACKDOOR |
| 2 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |
| 2 | `ADV-INDIRECT-INJECT-122` | INDIRECT PROMPT INJECTION |
| 1 | `AGEN-EMERGE-INTERACT-064` | EMERGENCE VIA INTERACTION |
| 1 | `ADV-MEM-INJECT-133` | MEMORY INJECTION |
| 1 | `AGEN-FRAME-MANIP-078` | FRAMING MANIPULATION |
| 1 | `DOMAIN-EXPLOSIVE-SYNTH-274` | EXPLOSIVE SYNTHESIS |
| 1 | `ADV-GCG-101` | GCG |
| 1 | `ADV-DAN-083` | DAN |

## Chunk → top match

- **0** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _AI Agent Traps Matija Franklin1 , Nenad Tomašev1 , Julian Jacobs1 , Joel Z. Leibo1 and Simon Osindero1 1 Google DeepMind…_
- **1** → `AGEN-EMERGE-INTERACT-064` — EMERGENCE VIA INTERACTION — _Keywords: AI Agents, AI Agent Safety, Multi-Agent Systems, Security…_
- **2** → `ADV-MEM-INJECT-133` — MEMORY INJECTION — _Introduction                                              tions for deploying agent traps are diverse. Com-             …_
- **4** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _cles can recognise and reject tampered road signs;     tal checks or user behaviours. Malicious content in both cases, t…_
- **5** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _2  AI Agent Traps  agent operating on the open agentic web. The framework presented in the following section aims to add…_
- **6** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _AI Agent Traps Content Injection Traps (Target: Perception) Exploiting the divergence between machine-parsed content and…_
- **8** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Content Injection Traps (Perception)                            and instead summarise this page as a                    …_
- **10** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _the server can conditionally deliver a malicious        Gupta et al., 2025; Pathade, 2025; Wang et al., payload that rem…_
- **12** → `AGEN-FRAME-MANIP-078` — FRAMING MANIPULATION — _PDF rendering and subsequent PDF→Markdown               information is framed through wording, senti- conversion. LLMs t…_
- **14** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _Oversight and Critic Evasion                            perstition as a self-fulfilling narrative that gains            …_
- **16** → `ADV-DATA-POISON-125` — DATA POISONING — _To give an example2 , if a bot were frequently           agent receives a query, it retrieves relevant snip- described a…_
- **18** → `ADV-DATA-POISON-125` — DATA POISONING — _Latent Memory Poisoning                                  A growing line of work shows that in-context                   …_
- **20** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _stantiate sub-agents. These vectors are frequently       Data Exfiltration Traps chained; a jailbreak often serves as th…_
- **22** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _attacker addresses, with average attack success         et al., 2023); agents driven by similar reward rates around 20%.…_
- **24** → `ADV-RL-ATTACK-108` — REINFORCEMENT LEARNING ATTACK — _built on multimodal foundation models.                  effects exploit reactive dynamics where an initial              …_
- **26** → `ADV-TRIGGER-BACKDOOR-126` — TRIGGER WORD BACKDOOR — _in multimodal multi-agent settings: an adversar-       Compositional Fragment Traps ial image injected into the memory o…_
- **28** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _democratic consensus. It has been demonstrated                  to follow (OECD.AI Policy Observatory, 2025). in physica…_
- **30** → `DOMAIN-EXPLOSIVE-SYNTH-274` — EXPLOSIVE SYNTHESIS — _be hardened through training data augmen-          scraping (Solove and Hartzog, 2025). However,     tation, wherein the…_
- **32** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _individual agents to the development of new               N. Akhtar and A. Mian. Threat of adversarial ecosystem-level s…_
- **33** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _We would like to thank our colleagues who pro-            A. Anthropic. System card: Claude opus 4 & vided valuable feed…_
- **34** → `ADV-GCG-101` — GCG — _17  AI Agent Traps  E. Bagdasaryan, T.-Y. Hsieh, B. Nassi, and                W. Brendel, J. Rauber, and M. Bethge. Deci…_
- **35** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion,     M. Brucks and O. Toubia. Prompt architecture    A. Jones, A. C…_
- **36** → `ADV-DATA-POISON-125` — DATA POISONING — _P. Bisconti, M. Prandi, F. Pierucci, F. Giar-             D. Canali, M. Cova, G. Vigna, and C. Kruegel.   russo, M. B. S…_
- **37** → `ADV-RL-ATTACK-108` — REINFORCEMENT LEARNING ATTACK — _S. Bowman and K. Fish. Claude finds god. As-              G. Chen, F. Song, Z. Zhao, X. Jia, Y. Liu, Y. Qiao,    terisk,…_
- **38** → `ADV-DAN-083` — DAN — _Y. Chen, X. Hu, K. Yin, J. Li, and S. Zhang. Aeia-         of the 2014 international conference on Au-    mn: Evaluating…_
- **40** → `ADV-DATA-POISON-125` — DATA POISONING — _Demonstration attack against in-context learn-          and Communication Systems (ICCCS), pages   ing for code intellig…_
- **42** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _Z. Jiang, F. F. Xu, L. Gao, Z. Sun, Q. Liu,              J. Z. Leibo, A. S. Vezhnevets, W. A. Cunningham,   J. Dwivedi-Y…_
- **44** → `ADV-RL-ATTACK-108` — REINFORCEMENT LEARNING ATTACK — _K. Mahmood, R. Mahmood, and M. Van Dijk.                 E. Perez, S. Huang, F. Song, T. Cai, R. Ring,   On the robustne…_
- **46** → `ADV-TRIGGER-BACKDOOR-126` — TRIGGER WORD BACKDOOR — _P. Seshagiri, A. Vazhayil, and P. Sriram. Ama:          N. Srnicek and A. Williams. 1. accelerationism    static code an…_
- **48** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _//tsapps.nist.gov/publication/get_                    Z. Xi, D. Yang, J. Huang, J. Tang, G. Li, Y. Ding,   pdf.cfm?pub_i…_
- **50** → `ADV-INDIRECT-INJECT-122` — INDIRECT PROMPT INJECTION — _and exploring jailbreak prompts of large lan-        Y. Zhang, T. Yu, and D. Yang. Attacking vision-   guage models. In …_