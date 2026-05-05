# Classifier pass: external report (live PDF/text)

**Source file:** `reports/paloalto-incident-response-2026/paloalto-unit42-full-report-live-source.txt`
**Chunks:** 74 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 6 | `ARCH-PERSIST-STATE-228` | PERSISTENT STATE EXPLOIT |
| 5 | `ARCH-DATA-EXFIL-245` | DATA EXFILTRATION |
| 4 | `ADV-BEAM-ATTACK-106` | BEAM SEARCH ATTACK |
| 4 | `ADV-EMBEDDING-109` | EMBEDDING SPACE ATTACK |
| 4 | `ARCH-CONSENT-VIOL-251` | CONSENT VIOLATION |
| 3 | `DOMAIN-CRED-THEFT-270` | CREDENTIAL THEFT ASSISTANCE |
| 3 | `ARCH-ATTENTION-EXPLOIT-212` | ATTENTION MECHANISM EXPLOIT |
| 3 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 3 | `ADV-DAN-083` | DAN |
| 3 | `ARCH-AUTH-BYPASS-242` | AUTHENTICATION BYPASS |
| 3 | `AGEN-PERSIST-OP-066` | PERSISTENT OPERATION |
| 3 | `ARCH-STATE-PERSIST-224` | STATEFUL ATTACK PERSISTENCE |
| 3 | `DOMAIN-RANSOM-DEV-271` | RANSOMWARE DEVELOPMENT |
| 2 | `ADV-PAIR-113` | PAIR |
| 2 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |
| 2 | `ADV-CIPHER-118` | CIPHER ATTACK |
| 2 | `DOMAIN-DDOS-PLAN-273` | DDoS ATTACK PLANNING |
| 1 | `ADV-API-INJECT-131` | API INJECTION |
| 1 | `AGEN-HUMAN-MANIP-061` | HUMAN MANIPULATION |
| 1 | `ARCH-GC-LEAK-230` | GARBAGE COLLECTION LEAK |
| 1 | `ARCH-CODE-INJECT-239` | CODE EXECUTION INJECTION |
| 1 | `ADV-SQL-INJECT-128` | SQL INJECTION |
| 1 | `ARCH-TOOL-CHAIN-235` | TOOL CHAINING EXPLOIT |
| 1 | `ADV-ENSEMBLE-120` | ENSEMBLE ATTACK |
| 1 | `ARCH-RESIDUAL-EXPLOIT-214` | RESIDUAL CONNECTION EXPLOIT |
| 1 | `ARCH-SECURE-DEL-249` | SECURE DELETION FAILURE |
| 1 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 1 | `GOV-RCA-FAIL-321` | ROOT CAUSE ANALYSIS FAILURE |
| 1 | `ADV-TAP-114` | TAP |
| 1 | `ADV-LATENT-MANIP-110` | LATENT SPACE MANIPULATION |
| 1 | `AGEN-OMISSION-074` | OMISSION |
| 1 | `ARCH-MIN-FAIL-253` | DATA MINIMIZATION FAILURE |
| 1 | `ARCH-CONTEXT-ATTACK-223` | CONTEXT WINDOW ATTACK |
| 1 | `GOV-COMM-FAIL-340` | COMMUNICATION FAILURE |
| 1 | `GOV-INCIDENT-FAIL-320` | INCIDENT RESPONSE FAILURE |
| 1 | `EPIS-COPYRIGHT-026` | COPYRIGHTED CONTENT GENERATION |

## Chunk → top match

- **0** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _2026 Unit 42 Global Incident Response Report - Palo Alto Networks  Read more downloads  EN  USA (ENGLISH)  BRAZIL (PORTU…_
- **1** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _Third, software supply chain risk has expanded beyond vulnerable code to the misuse of trusted connectivity.  Attackers …_
- **2** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _Most breaches were enabled by exposure, not attacker sophistication. In fact, in over 90% of breaches, preventable gaps …_
- **3** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _When that call comes, our incident responders move quickly to investigate, contain and eradicate the threat. We help org…_
- **4** → `ARCH-ATTENTION-EXPLOIT-212` — ATTENTION MECHANISM EXPLOIT — _At the same time, most breaches still follow familiar paths. And that is why our most important conclusion remains uncha…_
- **5** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _Unit 42 operates 24/7 to protect the digital world from cyberthreats. The goal of this report is straightforward: to tur…_
- **6** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _Faster vulnerability exploitation: The window between disclosure and exploitation continues to shrink. Threat actors are…_
- **7** → `ADV-PAIR-113` — PAIR — _Ransomware Automation  In a ransomware investigation, Unit 42 recovered operational scripts used to deploy payloads, coo…_
- **8** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _Hyper-personalized social engineering: We have moved past “phishing with better grammar.” Actors can automate open-sourc…_
- **9** → `ADV-DAN-083` — DAN — _“Vibe Extortion”  An unsophisticated actor exfiltrated sensitive data but had no plan for the shakedown. To bridge the g…_
- **10** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Turning your AI platform into a weapon: Threat actors use valid credentials to misuse enterprise AI platforms. For examp…_
- **11** → `ADV-API-INJECT-131` — API INJECTION — _Automate external patching: Mandate automated patching for critical CVEs on internet-facing assets to close the 24-hour …_
- **12** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _As organizations move deeper into SaaS, cloud and hybrid environments, the network perimeter matters less. Identity — th…_
- **13** → `ARCH-AUTH-BYPASS-242` — AUTHENTICATION BYPASS — _Identity-related social engineering (33%): Identity-based phishing (22%) and other social engineering (11%) remain the l…_
- **14** → `AGEN-HUMAN-MANIP-061` — HUMAN MANIPULATION — _The Way Through: Identity Turns Access Into Impact  After initial access, identity gaps are one of the most common ways …_
- **15** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _Privilege escalation: Over-scoped roles, inherited permissions and unretired legacy grants create repeatable paths to hi…_
- **16** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _The rise of machine and AI identities:  Non-human identities, like service accounts, automation roles, API keys and emer…_
- **17** → `AGEN-PERSIST-OP-066` — PERSISTENT OPERATION — _Deploy phishing-resistant MFA: Standard MFA is not enough against modern bypass and adversary-in-the-middle tactics. Pri…_
- **18** → `ADV-CIPHER-118` — CIPHER ATTACK — _Trend 3. Software Supply Chain Attacks Increasingly Drive Downstream Disruption Supply chain risk is no longer limited t…_
- **19** → `ARCH-GC-LEAK-230` — GARBAGE COLLECTION LEAK — _This exposure is reflected in Unit 42 investigations. Data from SaaS applications was relevant to 23% of cases in 2025, …_
- **20** → `ARCH-CODE-INJECT-239` — CODE EXECUTION INJECTION — _Open Source and AI: Dependency Sprawl and Build-Time Compromise  Open source remains the foundation of modern developmen…_
- **21** → `ADV-SQL-INJECT-128` — SQL INJECTION — _Vendor Tools: Weaponizing Management Channels  Vendor tools, especially remote monitoring and management (RMM) and mobil…_
- **22** → `AGEN-PERSIST-OP-066` — PERSISTENT OPERATION — _The Impact: From Response to Business Disruption  Supply chain incidents amplify disruption through uncertainty. When a …_
- **23** → `AGEN-PERSIST-OP-066` — PERSISTENT OPERATION — _Defending the supply chain requires reducing the time needed to assess exposure and the area of impact.  Map SaaS owners…_
- **24** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _Greater use of identity-driven access Deeper compromise of infrastructure and virtualization layers Early experiments wi…_
- **25** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _Similarly, we observed a year-long persistence campaign against information technology, SaaS and business-process outsou…_
- **26** → `ARCH-ATTENTION-EXPLOIT-212` — ATTENTION MECHANISM EXPLOIT — _Wagemole : North Korean operatives obtained unauthorized remote employment with U.S. and European organizations and cove…_
- **27** → `ARCH-TOOL-CHAIN-235` — TOOL CHAINING EXPLOIT — _Screening Serpens (aka Smoke Sandstorm, UNC1549): This group targeted government organizations in the Middle East by cre…_
- **28** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _The Trusted Résumé  In one Screening Serpens investigation, an attacker approached an employee through LinkedIn and pers…_
- **29** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _Attackers appear most interested in using AI to strengthen persistence and build more durable footholds. Nation-state op…_
- **30** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _North Korean operators also showed signs of AI experimentation. In Unit 42 research  associated with the Wagemole campai…_
- **31** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _Tighten verification across identity and recruitment workflows: Strengthen checks on contractor onboarding and external …_
- **32** → `ADV-ENSEMBLE-120` — ENSEMBLE ATTACK — _The attack surface: This is where attackers strike. Intrusions rarely stay in one lane; they now span endpoints, cloud i…_
- **33** → `DOMAIN-DDOS-PLAN-273` — DDoS ATTACK PLANNING — _Attack Surface Percentage Identity 89% Endpoints 61% Network 50% Human 45% Email 27% Application 26% Cloud 20% SecOps 10…_
- **34** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _The Browser Attack Surface: Attacks at the Human Interface  Browser activity played a role in 48% of investigations this…_
- **35** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _A global medical technology firm experienced an intrusion that began with SEO poisoning. An administrator accessed a spo…_
- **36** → `ARCH-STATE-PERSIST-224` — STATEFUL ATTACK PERSISTENCE — _Cloud weaknesses varied, but even basic issues shaped attacker behavior once they established access. In one investigati…_
- **37** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _3.2. The Entry Point: Initial Access Comes from Predictable Paths Initial access in 2025 followed a familiar pattern, wi…_
- **38** → `ARCH-RESIDUAL-EXPLOIT-214` — RESIDUAL CONNECTION EXPLOIT — _Phishing campaigns are achieving higher conversion rates as AI helps attackers craft credible, error-free lures that byp…_
- **39** → `ARCH-STATE-PERSIST-224` — STATEFUL ATTACK PERSISTENCE — _Previously compromised credentials declined to 13% in 2025, reversing heightened activity reported in 2023 and 2024. Act…_
- **40** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _Big Environments, Bigger Vulnerability Exposure  The data suggests that the largest enterprises face a different balance…_
- **41** → `ARCH-STATE-PERSIST-224` — STATEFUL ATTACK PERSISTENCE — _The time-to-exfiltration, which measures the duration between initial compromise and confirmed data theft, shows a sharp…_
- **42** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _3.4. The Impact: Extortion Beyond Encryption  Encryption appeared in 78% of extortion cases in 2025, a sharp decline fro…_
- **43** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _Harassment, while less common, remained a persistent tactic. These behaviors included contacting employees directly, thr…_
- **44** → `DOMAIN-RANSOM-DEV-271` — RANSOMWARE DEVELOPMENT — _When measured against perceived annual revenue (PAR), these demands represented 0.55% of PAR, down from 2% the prior yea…_
- **45** → `ARCH-SECURE-DEL-249` — SECURE DELETION FAILURE — _This brand maintenance extends to promise-keeping: in our 2025 dataset, threat actors fulfilled their commitments (such …_
- **46** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _Attacker success is rarely about zero-day exploits. Across the incidents we responded to in 2025, we found that in more …_
- **47** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _2. Environmental Complexity: Inconsistency Creates the Path of Least Resistance  Security baselines are rarely applied u…_
- **48** → `ADV-EMBEDDING-109` — EMBEDDING SPACE ATTACK — _These failures reflect identity drift. As permissions accumulate and exceptions persist, intruders encounter fewer barri…_
- **49** → `GOV-RCA-FAIL-321` — ROOT CAUSE ANALYSIS FAILURE — _To detect modern intrusions, organizations must ingest and normalize signals from identity providers, cloud platforms an…_
- **50** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Enable real-time threat response with automation.  Delays in containment often stem from unclear ownership and manual va…_
- **51** → `ARCH-PERSIST-STATE-228` — PERSISTENT STATE EXPLOIT — _Transition from reactive to proactive security. To shift from reactive defense, organizations must move beyond tradition…_
- **52** → `ADV-PAIR-113` — PAIR — _Achieving this requires bridging operational silos across Security, IT, and DevOps. Playbooks should reflect how systems…_
- **53** → `ARCH-ATTENTION-EXPLOIT-212` — ATTENTION MECHANISM EXPLOIT — _2. Adopt Zero Trust to Constrain the Area of Impact  Zero trust is a strategic necessity in an environment where identit…_
- **54** → `ARCH-AUTH-BYPASS-242` — AUTHENTICATION BYPASS — _Continuous verification treats trust as dynamic, with decisions revisited as conditions change during a session. Validat…_
- **55** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Apply consistent inspection across trusted and untrusted traffic. Apply consistent inspection across trusted and untrust…_
- **56** → `ADV-TAP-114` — TAP — _Control data access and movement to reduce impact.  The most damaging outcomes in many incidents occur not at initial co…_
- **57** → `ARCH-AUTH-BYPASS-242` — AUTHENTICATION BYPASS — _Attackers consistently moved through the gaps created by this governance drift, exploiting legacy permissions and unmoni…_
- **58** → `DOMAIN-CRED-THEFT-270` — CREDENTIAL THEFT ASSISTANCE — _Role transitions, rapid deployment cycles and everyday shortcuts widened the gap between written policy and actual acces…_
- **59** → `ADV-LATENT-MANIP-110` — LATENT SPACE MANIPULATION — _Secure AI and automation integrity. As organizations embed AI agents and automated workflows into core processes, these …_
- **60** → `ADV-CIPHER-118` — CIPHER ATTACK — _In 2025, attackers increasingly targeted the software supply chain and cloud APIs to bypass traditional perimeters, inje…_
- **61** → `DOMAIN-DDOS-PLAN-273` — DDoS ATTACK PLANNING — _Secure the software and AI supply chain. Although not the most common attack vector, supply chain compromises yield the …_
- **62** → `ADV-BEAM-ATTACK-106` — BEAM SEARCH ATTACK — _Real-time detection, combined with consistent runtime controls such as behavioral monitoring, clear network boundaries a…_
- **63** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _A strong security culture treats AI systems with the same discipline as critical infrastructure. This includes reviewing…_
- **64** → `AGEN-OMISSION-074` — OMISSION — _Reduce the attack surface with active exposure management. Unit 42 found that software vulnerabilities accounted for 22%…_
- **65** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _Securing this interface requires an enterprise-grade secure browser that establishes a fully isolated and secured corpor…_
- **66** → `ARCH-MIN-FAIL-253` — DATA MINIMIZATION FAILURE — _Collect unified telemetry and automate response. For the endpoints you do manage, data is the fuel for defense. Detectin…_
- **67** → `ARCH-DATA-EXFIL-245` — DATA EXFILTRATION — _5.1 Overview of Observed MITRE Techniques by Tactic  The following series of charts (Figures 3-14) show the MITRE ATT&CK…_
- **68** → `ARCH-CONTEXT-ATTACK-223` — CONTEXT WINDOW ATTACK — _The geographic data highlights differences in investigation types regionally, while the industry charts show clear patte…_
- **69** → `GOV-COMM-FAIL-340` — COMMUNICATION FAILURE — _6. Methodology  We sourced data for this report from more than 750 cases Unit 42 responded to between Oct. 1, 2024, and …_
- **70** → `ADV-DAN-083` — DAN — _For some analysis areas, we chose to filter our data to avoid skewed results. For example, we offered incident response …_
- **71** → `GOV-INCIDENT-FAIL-320` — INCIDENT RESPONSE FAILURE — _Virginia Tran  Amy Wagman  JL Watkins  Kyle Wilhoit  Contact a specialist  Table of Contents Table of Contents  Executiv…_
- **72** → `ADV-DAN-083` — DAN — _Access the 2026 Global Incident Response Exec Kit Includes the full report, leadership insights, and board-ready slides …_
- **73** → `EPIS-COPYRIGHT-026` — COPYRIGHTED CONTENT GENERATION — _Enterprise Data Loss Prevention  Enterprise IoT Security  Medical IoT Security  Industrial OT Security  SaaS Security  N…_