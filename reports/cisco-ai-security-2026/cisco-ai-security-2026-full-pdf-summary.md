# Classifier pass: external report (live PDF/text)

**Source file:** `reports/cisco-ai-security-2026/cisco-ai-security-2026-full-pdf-source.txt`
**Chunks:** 56 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 5 | `ADV-DAN-083` | DAN |
| 4 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 3 | `ADV-DIRECT-INJECT-121` | DIRECT PROMPT INJECTION |
| 3 | `ARCH-PERSIST-STATE-228` | PERSISTENT STATE EXPLOIT |
| 3 | `ADV-DATA-POISON-125` | DATA POISONING |
| 3 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 2 | `ADV-ENSEMBLE-120` | ENSEMBLE ATTACK |
| 2 | `ADV-API-INJECT-131` | API INJECTION |
| 2 | `ARCH-MEM-CORRUPT-225` | MEMORY CORRUPTION |
| 2 | `GOV-EO-VIOL-329` | EXECUTIVE ORDER VIOLATION |
| 2 | `ARCH-DATA-EXFIL-245` | DATA EXFILTRATION |
| 1 | `ARCH-CONTEXT-ATTACK-223` | CONTEXT WINDOW ATTACK |
| 1 | `ARCH-CODE-INJECT-239` | CODE EXECUTION INJECTION |
| 1 | `ADV-BEAM-ATTACK-106` | BEAM SEARCH ATTACK |
| 1 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |
| 1 | `GOV-AUTHORITY-UNCLEAR-342` | DECISION AUTHORITY UNCLEAR |
| 1 | `ALIGN-ORTHO-VALUE-176` | ORTHOGONAL VALUE PURSUIT |
| 1 | `ARCH-AUTHZ-FAIL-243` | AUTHORIZATION FAILURE |
| 1 | `ARCH-SANDBOX-ESCAPE-238` | SANDBOX ESCAPE |
| 1 | `GOV-REPORT-FAIL-333` | REPORTING OBLIGATION FAILURE |
| 1 | `AGEN-ENV-EXPLOIT-063` | ENVIRONMENT EXPLOITATION |
| 1 | `AGEN-TOOL-MISUSE-055` | TOOL MISUSE |
| 1 | `AGEN-AUTO-PLAN-067` | AUTONOMOUS PLANNING |
| 1 | `GOV-AI-ACT-328` | AI ACT VIOLATION |
| 1 | `GOV-VOLUNTARY-VIOL-330` | VOLUNTARY COMMITMENTS VIOLATION |
| 1 | `ARCH-SECURE-DEL-249` | SECURE DELETION FAILURE |
| 1 | `AGEN-SELECT-DISCLOS-077` | SELECTIVE DISCLOSURE |
| 1 | `AGEN-RESOURCE-HIJACK-047` | RESOURCE HIJACKING |
| 1 | `ARCH-VERSION-REGRESS-209` | VERSIONING SAFETY REGRESSION |
| 1 | `ADV-DEEPFAKE-154` | SYNTHETIC MEDIA |
| 1 | `ALIGN-REWARD-TAMP-157` | REWARD TAMPERING |
| 1 | `GOV-CORRECTIVE-FAIL-322` | CORRECTIVE ACTION FAILURE |
| 1 | `ALIGN-CONTEXT-SAFE-190` | CONTEXT-DEPENDENT SAFETY FAILURE |

## Chunk → top match

- **0** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _State of AI Security 2026  Table of Contents Executive Summary                                                          …_
- **1** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _Open-Weight Model Vulnerability Analysis                             23  Agentic Security: MCP & A2A Scanners           …_
- **2** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _This year’s report builds upon the foundational analysis of the State of AI Security 2025 and provides a deep-dive inves…_
- **3** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _A critical finding from this year’s analysis is the vulnerability of the “connective tissue” of the contemporary AI econ…_
- **4** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _AI Threat Landscape Over the course of 2025, we observed once-                 failures, which can leave organizations s…_
- **5** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _Organizations that rushed to integrate large language models (LLMs) into critical workflows             Securing the fut…_
- **6** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _The Evolution of Prompt Injections and Jailbreaks Early proofs of prompt injections, which are attempts to trick an AI m…_
- **7** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _Over time, both researchers and attackers have become better at prompt injection and jailbreak techniques, which means n…_
- **9** → `ADV-DATA-POISON-125` — DATA POISONING — _The Fragility of the AI Supply Chain The State of AI Security 2025 report warned that           that malicious code can …_
- **10** → `ADV-DATA-POISON-125` — DATA POISONING — _The AI model ecosystem is also an unchecked                                                            Poisoned fine-tun…_
- **11** → `ADV-DAN-083` — DAN — _© 2026 Cisco and/or its affiliates. All rights reserved.  Agentic Threats: Autonomous Agents Gone Awry The State of AI S…_
- **12** → `GOV-AUTHORITY-UNCLEAR-342` — DECISION AUTHORITY UNCLEAR — _In early 2026, a personal AI assistant, Clawdbot (since renamed Moltbot) achieved virality for its ability to complete u…_
- **13** → `ALIGN-ORTHO-VALUE-176` — ORTHOGONAL VALUE PURSUIT — _Agentic misalignment, where “models independently and intentionally choose harmful actions,” is another unexpected failu…_
- **14** → `ARCH-AUTHZ-FAIL-243` — AUTHORIZATION FAILURE — _Threats such as agent impersonation, agent session smuggling, and unauthorized capability escalation exploit implicit tr…_
- **15** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _The watershed moment arrived in late-2025 when Anthropic reported a Chinese state-backed group (designated GTG-1002) fam…_
- **16** → `ADV-DATA-POISON-125` — DATA POISONING — _Model Context Protocol: New Protocol, New Attack Paths In late-2024, Anthropic introduced a new open standard called Mod…_
- **17** → `ARCH-SANDBOX-ESCAPE-238` — SANDBOX ESCAPE — _Remote code execution in MCP infrastructure: Researchers found that a developer tool called “mcp-remote” allowed attacke…_
- **18** → `ADV-API-INJECT-131` — API INJECTION — _Supply chain attacks: A fake package named "Postmark MCP Server" was published to the npm registry. Designed to look lik…_
- **19** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _Threat Actors on the Rise As predicted in last year’s report, and as detailed in the examples that follow, state-sponsor…_
- **20** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _Due to the inaccessibility of raw data associated with the compromise of third-party models and a relatively immature in…_
- **21** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _Russian Federation Russian state-sponsored use of AI for offensive operations has been highly visible in the information…_
- **22** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _Iran Iranian state-sponsored threat actors have been observed to be a prolific user of generative AI to enhance cyber op…_
- **23** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _Improved Threat Actor Capabilities Challenge Defenders A convergence of nation-state and cybercriminal capabilities will…_
- **24** → `ADV-DIRECT-INJECT-121` — DIRECT PROMPT INJECTION — _The Path Ahead As we look forward to 2026, the trajectory of AI           Commoditization of autonomous attack agents se…_
- **25** → `AGEN-ENV-EXPLOIT-063` — ENVIRONMENT EXPLOITATION — _© 2026 Cisco and/or its affiliates. All rights reserved.  Operationalizing AI Security and Safety Executives and leaders…_
- **26** → `ADV-DAN-083` — DAN — _For years, securing AI has required piecing together guidance from disparate sources. MITRE ATLAS helped define adversar…_
- **27** → `ARCH-MEM-CORRUPT-225` — MEMORY CORRUPTION — _A New Paradigm for Understanding AI Risk AI security and safety risks present very real concerns for organizations. Take…_
- **28** → `AGEN-TOOL-MISUSE-055` — TOOL MISUSE — _Where traditional approaches have treated safety and security as parallel tracks, our AI Security Framework reflects the…_
- **29** → `AGEN-AUTO-PLAN-067` — AUTONOMOUS PLANNING — _(3) Multi-agent orchestration: The AI Security Framework can also account for the risks that emerge when AI systems work…_
- **30** → `GOV-EO-VIOL-329` — EXECUTIVE ORDER VIOLATION — _(5) An audience-aware security compass: Finally, the framework is intentionally designed for multiple audiences. Executi…_
- **31** → `ARCH-MEM-CORRUPT-225` — MEMORY CORRUPTION — _Inside the AI Security Framework: A Unified Taxonomy of AI Threats A crucial component of the AI Security Framework is t…_
- **32** → `GOV-AI-ACT-328` — AI ACT VIOLATION — _© 2026 Cisco and/or its affiliates. All rights reserved.  AI Policy Landscape The trajectory of AI governance in 2025 re…_
- **33** → `GOV-VOLUNTARY-VIOL-330` — VOLUNTARY COMMITMENTS VIOLATION — _This section covers key developments over the past year in several large geographies. As summarized below, the United St…_
- **34** → `GOV-EO-VIOL-329` — EXECUTIVE ORDER VIOLATION — _Industrial Policy for AI Dominance and Resilience Within days of taking office, President Trump revoked President Biden’…_
- **35** → `ARCH-SECURE-DEL-249` — SECURE DELETION FAILURE — _In July 2025, the White House released America’s AI Action Plan which was organized into three pillars: Accelerate AI In…_
- **36** → `ADV-DAN-083` — DAN — _Another defining feature of U.S. domestic AI policy in 2025 was the elevation of AI security to a matter of national str…_
- **37** → `AGEN-SELECT-DISCLOS-077` — SELECTIVE DISCLOSURE — _A cornerstone of this AI governance model remains the NIST AI Risk Management Framework (RMF). Designed as a voluntary b…_
- **38** → `ADV-DAN-083` — DAN — _The current U.S. federal approach to AI security has moved away from a static compliance model toward a dynamic, collabo…_
- **39** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _European Union AI Policy Developments The EU has continued anchoring its AI governance approach within a risk-based fram…_
- **40** → `AGEN-RESOURCE-HIJACK-047` — RESOURCE HIJACKING — _Phased implementation timelines As mentioned above, the EU AI Act comes into force in phases. This phased approach can h…_
- **41** → `ARCH-VERSION-REGRESS-209` — VERSIONING SAFETY REGRESSION — _Additional flexibility for smaller organizations Acknowledging the barriers of entry from smaller firms, the Omnibus als…_
- **42** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _China AI Policy Developments The Chinese government pursued a dual focus strategy of simultaneously seeking to embed AI …_
- **43** → `ALIGN-REWARD-TAMP-157` — REWARD TAMPERING — _International Differences in AI Policy Broader dynamics in global cooperation and competition have created a complex lan…_
- **44** → `GOV-CORRECTIVE-FAIL-322` — CORRECTIVE ACTION FAILURE — _The U.S.-UK Technology Prosperity Deal In September 2025, the United States and UK committed to a new Technology Prosper…_
- **45** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _UK AI Opportunities Action Plan and AI Growth Zones In the United Kingdom, the January 2025 AI Opportunities Action Plan…_
- **47** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _AI Security Research and Tooling at Cisco Agentic Skill Scanner In early 2026, OpenClaw (formerly known as              …_
- **48** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _Despite its impressive capabilities, OpenClaw had clear and pressing security flaws. The agent’s high-level privileges c…_
- **49** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _AI Security Research and Tooling at Cisco Open-Weight Model Vulnerability Analysis                   Across all models, …_
- **51** → `ADV-API-INJECT-131` — API INJECTION — _AI Security Research and Tooling at Cisco Agentic Security: MCP & A2A Scanners                       malicious or anomal…_
- **52** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _© 2026 Cisco and/or its affiliates. All rights reserved.  AI Security Research and Tooling at Cisco Hardening Pickle Fil…_
- **53** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _Structure-aware fuzzing enables this tool to generate pickle files that respect the format’s rules, creating adversarial…_
- **54** → `ALIGN-CONTEXT-SAFE-190` — CONTEXT-DEPENDENT SAFETY FAILURE — _SecureBERT 2.0 brings greater contextual relevance and domain expertise for cybersecurity, understanding code sources an…_
- **55** → `ADV-DAN-083` — DAN — _AI Threat & Security Research Team Contributors Ehsan Aghaei (AI Researcher, Cisco) Nicholas Conley (AI Researcher, Cisc…_