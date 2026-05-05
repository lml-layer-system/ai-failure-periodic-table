# Classifier pass: external report (live PDF/text)

**Source file:** `reports/paloalto-incident-response-2026/paloalto-unit42-full-pdf-source.txt`
**Chunks:** 108 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 19 | `GOV-INCIDENT-FAIL-320` | INCIDENT RESPONSE FAILURE |
| 9 | `DOMAIN-RANSOM-DEV-271` | RANSOMWARE DEVELOPMENT |
| 7 | `ADV-BEAM-ATTACK-106` | BEAM SEARCH ATTACK |
| 5 | `ADV-EMBEDDING-109` | EMBEDDING SPACE ATTACK |
| 5 | `DOMAIN-CRED-THEFT-270` | CREDENTIAL THEFT ASSISTANCE |
| 4 | `ARCH-PERSIST-STATE-228` | PERSISTENT STATE EXPLOIT |
| 4 | `ARCH-DATA-EXFIL-245` | DATA EXFILTRATION |
| 3 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 3 | `ARCH-CONSENT-VIOL-251` | CONSENT VIOLATION |
| 2 | `GOV-REPORT-FAIL-333` | REPORTING OBLIGATION FAILURE |
| 2 | `ADV-PAIR-113` | PAIR |
| 2 | `ARCH-AUTH-BYPASS-242` | AUTHENTICATION BYPASS |
| 2 | `ARCH-RETENTION-VIOL-248` | DATA RETENTION VIOLATION |
| 2 | `AGEN-HUMAN-MANIP-061` | HUMAN MANIPULATION |
| 2 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |
| 2 | `AGEN-PERSIST-OP-066` | PERSISTENT OPERATION |
| 2 | `ARCH-GC-LEAK-230` | GARBAGE COLLECTION LEAK |
| 2 | `ARCH-CODE-INJECT-239` | CODE EXECUTION INJECTION |
| 2 | `DOMAIN-DDOS-PLAN-273` | DDoS ATTACK PLANNING |
| 2 | `DOMAIN-SOCENG-SCRIPT-266` | SOCIAL ENGINEERING SCRIPTS |
| 2 | `ARCH-STATE-PERSIST-224` | STATEFUL ATTACK PERSISTENCE |
| 1 | `ARCH-CONTEXT-ATTACK-223` | CONTEXT WINDOW ATTACK |
| 1 | `ARCH-DEBUG-EXPOSE-208` | DEBUGGING MODE EXPOSURE |
| 1 | `ADV-SQL-INJECT-128` | SQL INJECTION |
| 1 | `ADV-DEEPFAKE-154` | SYNTHETIC MEDIA |
| 1 | `ADV-ENSEMBLE-120` | ENSEMBLE ATTACK |
| 1 | `ARCH-RESIDUAL-EXPLOIT-214` | RESIDUAL CONNECTION EXPLOIT |
| 1 | `ARCH-SECURE-DEL-249` | SECURE DELETION FAILURE |
| 1 | `AGEN-MISSION-CREEP-072` | MISSION CREEP |
| 1 | `ARCH-ATTENTION-EXPLOIT-212` | ATTENTION MECHANISM EXPLOIT |
| 1 | `ARCH-INFO-LEAK-244` | INFORMATION LEAKAGE |
| 1 | `ADV-LATENT-MANIP-110` | LATENT SPACE MANIPULATION |
| 1 | `ADV-CIPHER-118` | CIPHER ATTACK |
| 1 | `AGEN-OMISSION-074` | OMISSION |
| 1 | `ARCH-MIN-FAIL-253` | DATA MINIMIZATION FAILURE |
| 1 | `ARCH-DEPLOY-CONFIG-210` | DEPLOYMENT CONFIGURATION ERROR |
| 1 | `AGEN-SELECT-DISCLOS-077` | SELECTIVE DISCLOSURE |
| 1 | `AGEN-RESOURCE-HIJACK-047` | RESOURCE HIJACKING |
| 1 | `DOMAIN-INTRUSION-GUIDE-269` | NETWORK INTRUSION GUIDANCE |
| 1 | `ADV-DAN-083` | DAN |

## Chunk → top match

- **0** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _CASE ID: CL-STA-0043  SYSTEM.               REFLECTION.METHODINFO  METHODINFO  =               ASSEMBLY.GETTYPES()      …_
- **1** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _Fourth,nation-state actors are adapting stealth and persistence tactics to modern enterprise operating environments. The…_
- **2** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _While these four trends each present a challenge, attacker success is rarely determined by a single attack vector. In mo…_
- **3** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _Security leaders must close the gaps attackers rely on. First, reduce exposure by securing the application ecosystem, in…_
- **4** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _In 2025, Unit 42 responded to more than 750 major cyber incidents. Our teams worked with large organizations facing exto…_
- **5** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _Over the past year, attack speeds continued to accelerate. Attackers are still early in their adoption of AI-enabled tra…_
- **6** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _Inside the Intrusion:         An aggregate view of observed tactics, techniques and procedures across Unit 42         in…_
- **7** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _While much of this activity occurs on adversary infrastructure—beyond our ability to directly observe—Unit 42 investigat…_
- **8** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _Ransomware at scale: We see actors using AI to reduce manual work during deployment (script generation, templating) and …_
- **9** → `ADV-PAIR-113` — PAIR — _In a ransomware investigation, Unit 42 recovered                     In an extortion case, Unit 42 negotiators         o…_
- **10** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _AI IMPROVES ATTACKER OUTCOMES                                                                              Vibe Extortio…_
- **11** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _Bottom line: AI improves the attackers’ rates of success at each stage. It improves     the quality of lures, shortens t…_
- **12** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _The AI-Assisted Insider AI CREATES NEW ATTACK VECTORS                                                                   …_
- **13** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _The risk is clear: If a tool can help employees get work done, it can also     help intruders understand your environmen…_
- **14** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _The Global Incident Response Report 2026   9  Section 02  TREND 2:  Identity Is the Most Reliable Path to Attacker Succe…_
- **15** → `ARCH-AUTH-BYPASS-242` — AUTHENTICATION BYPASS — _THE WAY IN: IDENTITY-DRIVEN INITIAL ACCESS Unit 42 case data shows that 65% of initial access is driven by identity-base…_
- **16** → `ARCH-RETENTION-VIOL-248` — DATA RETENTION VIOLATION — _65%                                                                                                                     …_
- **18** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _Iden                                                                                               -b                   …_
- **19** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _Credential misuse and brute force (21%): Previously compromised credentials (13%) and brute force activity (8%) allow at…_
- **20** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _THE WAY THROUGH: IDENTITY TURNS ACCESS INTO IMPACT                                                                      …_
- **21** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _Credential reuse and lateral movement: Actors commonly test compromised credentials across other systems. This is especi…_
- **22** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _The rise of machine and AI identities: Non-human identities, like service accounts, automation roles, API keys and emerg…_
- **23** → `AGEN-PERSIST-OP-066` — PERSISTENT OPERATION — _Deploy phishing-resistant MFA: Standard MFA is not enough against modern bypass and adversary-in-the-middle tactics.    …_
- **24** → `ARCH-DEBUG-EXPOSE-208` — DEBUGGING MODE EXPOSURE — _Software Supply Chain Attacks Increasingly Drive Downstream Disruption Supply chain risk is no longer limited to vulnera…_
- **25** → `ARCH-GC-LEAK-230` — GARBAGE COLLECTION LEAK — _SAAS INTEGRATIONS: INHERITED PERMISSIONS AT SCALE                                                                       …_
- **26** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _The Global Incident Response Report 2026     13  Section 02…_
- **27** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _OPEN SOURCE AND AI: DEPENDENCY SPRAWL AND BUILD-TIME COMPROMISE Open source remains the foundation of modern development…_
- **28** → `ADV-SQL-INJECT-128` — SQL INJECTION — _VENDOR TOOLS: WEAPONIZING MANAGEMENT CHANNELS Vendor tools, especially remote monitoring and management (RMM) and mobile…_
- **29** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _The Global Incident Response Report 2026     14  Section 02  THE IMPACT: FROM RESPONSE TO BUSINESS DISRUPTION Supply cha…_
- **30** → `AGEN-PERSIST-OP-066` — PERSISTENT OPERATION — _Defending the supply chain requires reducing the time needed to assess exposure and the area of impact.  Map SaaS owners…_
- **31** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _•    Greater use of identity-driven access      •    Deeper compromise of infrastructure and virtualization layers      …_
- **32** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _Curious Serpens                                   (aka APT33, Peach                                   Sandstorm)        …_
- **33** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _Chinese-nexus threat activity continued to prioritize long-term access and data collection. Notable shifts in 2025 moved…_
- **34** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _NORTH KOREA: WEAPONIZED HR PART I North Korean threat activity remained a persistent challenge for enterprises in 2025. …_
- **35** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _IRAN: WEAPONIZED HR PART II                                                                                             …_
- **36** → `ARCH-GC-LEAK-230` — GARBAGE COLLECTION LEAK — _Curious Serpens (aka APT33, Peach Sandstorm): Curious Serpens targeted a         communications provider through job-rec…_
- **37** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _Evidence of large-scale AI adoption by nation-state actors remains limited, but 2025 offered early signs that some group…_
- **38** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _North Korean operators also showed signs of AI experimentation. In Unit 42 research associated with the Wagemole        …_
- **39** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _Expand monitoring across virtualized and application infrastructure: Baseline and log activity on virtualization platfor…_
- **40** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _The Entry Point: This is how they get in. Phishing and vulnerabilities have tied as the leading initial access vectors, …_
- **41** → `DOMAIN-DDOS-PLAN-273` — DDoS ATTACK PLANNING — _Across all incidents, 87% involved activity                           61%                45% across two or more attack s…_
- **42** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _Identity featured prominently in many incidents—at nearly 90%— representing one of the most commonly involved attack sur…_
- **43** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _A global medical technology firm experienced an intrusion that began with SEO poisoning. An administrator accessed a spo…_
- **44** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _Cloud weaknesses varied, but even basic issues shaped attacker behavior once they  established access. In one investigat…_
- **45** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _The Entry Point:  Initial Access Comes  from Predictable Paths  Initial access in 2025 followed a familiar pattern, with…_
- **46** → `DOMAIN-SOCENG-SCRIPT-266` — SOCIAL ENGINEERING SCRIPTS — _40%                                                       25%                                               12% 35%     …_
- **48** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _5%                                                    4.0%                                                   12%        …_
- **50** → `DOMAIN-SOCENG-SCRIPT-266` — SOCIAL ENGINEERING SCRIPTS — _5%                                              4.0%                                                    12%             …_
- **51** → `ARCH-RESIDUAL-EXPLOIT-214` — RESIDUAL CONNECTION EXPLOIT — _PHISHING AND VULNERABILITIES TIE FOR DOMINANCE  Phishing and vulnerability exploitation are the most common initial acce…_
- **52** → `ARCH-STATE-PERSIST-224` — STATEFUL ATTACK PERSISTENCE — _Beyond phishing and vulnerability exploitation, we see important trends for the other key initial access vectors across …_
- **53** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _This pattern reflects attacker pragmatism. Operators tend to exploit whatever is most accessible and cost-effective at a…_
- **54** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _Velocity: The Fastest Attacks Are Getting Faster The time-to-exfiltration, which measures the duration between initial c…_
- **55** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _In 2025 it took                    72 minutes                           to exfiltrate                                   …_
- **56** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _Data theft remained a consistent feature of extortion activity, appearing in more than half of cases year over year. Thr…_
- **57** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _Harassment                        53%                     59%                                                60%    Data…_
- **58** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _Median Initial Ransom Demands     2025                                                                                  …_
- **59** → `ARCH-SECURE-DEL-249` — SECURE DELETION FAILURE — _The choice to pay remains highly situational, influenced by operational impact, regulatory considerations, legal require…_
- **60** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _Recovery practices also shape extortion outcomes. About 41% of victims were capable of restoring systems from backup wit…_
- **61** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _Common Contributing Factors: Why Attacks Succeed Attacker success is rarely about zero-day exploits. Across the incident…_
- **62** → `AGEN-MISSION-CREEP-072` — MISSION CREEP — _1. VISIBILITY GAPS: MISSING CONTEXT DELAYS DETECTION Many organizations fail to leverage the telemetry needed to observe…_
- **63** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _In multiple investigations, critical controls like endpoint protection were fully deployed in one business unit yet miss…_
- **64** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _1. EMPOWER SECURITY OPERATIONS TO DETECT AND RESPOND FASTER  With the fastest attacks now exfiltrating data in roughly a…_
- **65** → `GOV-REPORT-FAIL-333` — REPORTING OBLIGATION FAILURE — _Prevent, detect and prioritize threats with AI-driven capabilities. High alert volumes and fragmented         tools allo…_
- **66** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _Section 04  By replacing ad hoc judgment with standardized, validated playbooks, organizations ensure that response foll…_
- **67** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _Proactivity extends to recovery. Resilient organizations verify that systems are free of residual access, such as compro…_
- **68** → `ADV-PAIR-113` — PAIR — _Deepen your bench with an IR retainer. The right retainer extends your capabilities beyond emergency response. To stay a…_
- **69** → `ARCH-ATTENTION-EXPLOIT-212` — ATTENTION MECHANISM EXPLOIT — _In reality, achieving zero trust is complex. However, even small gains will reduce the attack surface, constrain lateral…_
- **70** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Enforce least privilege to constrain attacker movement. Excessive permissions act as a force multiplier for attackers. I…_
- **71** → `ARCH-RETENTION-VIOL-248` — DATA RETENTION VIOLATION — _To achieve consistent, pervasive threat analysis, organizations must consolidate all network, cloud and secure access   …_
- **72** → `ARCH-INFO-LEAK-244` — INFORMATION LEAKAGE — _Stronger governance over how data is accessed, shared and transferred reduces these opportunities by limiting where     …_
- **73** → `ARCH-STATE-PERSIST-224` — STATEFUL ATTACK PERSISTENCE — _Centralize identity management for humans and machines. You cannot govern what you cannot see. When         identity dat…_
- **74** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _Role transitions, rapid deployment cycles and everyday shortcuts widened the gap between written policy and actual      …_
- **75** → `ADV-LATENT-MANIP-110` — LATENT SPACE MANIPULATION — _Secure AI and automation integrity. As organizations embed AI agents and automated workflows into core         processes…_
- **76** → `ADV-CIPHER-118` — CIPHER ATTACK — _In 2025, attackers increasingly targeted the software supply chain and cloud APIs to bypass traditional perimeters, inje…_
- **77** → `DOMAIN-DDOS-PLAN-273` — DDoS ATTACK PLANNING — _Secure the software and AI supply chain. Although not the most common attack vector, supply chain compromises yield the …_
- **78** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _Real-time detection, combined with consistent runtime controls such as behavioral monitoring, clear network boundaries a…_
- **79** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _A strong security culture treats AI systems with the same discipline as critical infrastructure. This includes reviewing…_
- **80** → `AGEN-OMISSION-074` — OMISSION — _As defenders, we face a dual challenge. We must rigorously manage the external exposures that attackers constantly scan …_
- **81** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Protect the human interface. The browser is the new endpoint and the new corporate desktop. This is where employees     …_
- **82** → `ARCH-MIN-FAIL-253` — DATA MINIMIZATION FAILURE — _By securing the workspace through the browser, companies can grant contractors and BYOD users secure access to        co…_
- **83** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _By securing the browser as the primary workspace and rigorously managing the external attack                            …_
- **84** → `ARCH-DEPLOY-CONFIG-210` — DEPLOYMENT CONFIGURATION ERROR — _T1078 - Valid Accounts                                   39%                                   T1087 - Account Discovery…_
- **85** → `ARCH-AUTH-BYPASS-242` — AUTHENTICATION BYPASS — _T1047 - Windows                                                     Figure 8. Relative prevalence of techniques         …_
- **86** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _Figure 10. Relative prevalence of techniques                                                                            …_
- **87** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _T1070 - Indicator Removal                     31%                           T1078 - Valid Accounts                      …_
- **88** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _T1556 - Modify Authentication Process            4%    T1212 - Exploitation for Credential Access          3%           …_
- **89** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _T1534 - Internal Spearphishing    <1%  Figure 13. Relative prevalence of techniques observed  in association with the cr…_
- **90** → `AGEN-SELECT-DISCLOS-077` — SELECTIVE DISCLOSURE — _T1074 - Data Staged                             33%           T1219 - Remote Access Tools                               …_
- **91** → `AGEN-RESOURCE-HIJACK-047` — RESOURCE HIJACKING — _T1486 - Data Encrypted for Impact                                   60% Figure 15. Relative prevalence of techniques obs…_
- **92** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _T1529 - System Shutdown/Reboot          2%                 T1052 - Exfiltration                                         …_
- **93** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _5.2. INVESTIGATION TYPE BY REGION Figures 19 - 21 provide a regional and industry-level view of the investigations handl…_
- **94** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _Network Intrusion                                34%                       Network Intrusion                            …_
- **95** → `DOMAIN-INTRUSION-GUIDE-269` — NETWORK INTRUSION GUIDANCE — _Figure 19. Investigation type by region: North America.                       Figure 20. Investigation type by region: E…_
- **96** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _5.3.                                                                                                Network Intrusion   …_
- **98** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _Network Intrusion                                  38%                                                                  …_
- **100** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _29%                               Network Intrusion                                        40%             Network Intru…_
- **102** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _Network Intrusion                                     49%                         Network Intrusion                     …_
- **103** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _Figure 27. Investigation type by industry: State and Local Government.           Figure 28. Investigation type by indust…_
- **104** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _We combined this case data with insights from our threat research, which is informed by product telemetry, observations …_
- **105** → `ADV-DAN-083` — DAN — _Contributors     Amelia Albanese               Alexis Godwin                Vraj Mehta                    Doel Santos   …_
- **106** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _The Global Incident Response Report 2026      42  About Palo Alto Networks Palo Alto Networks® is the world’s cybersecur…_
- **107** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _About Unit 42 Palo Alto Networks® Unit 42® brings together world-renowned threat researchers, elite incident responders …_