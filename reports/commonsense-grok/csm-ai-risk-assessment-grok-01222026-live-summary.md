# Classifier pass: external report (live PDF/text)

**Source file:** `reports/commonsense-grok/csm-ai-risk-assessment-grok-01222026-live-source.txt`
**Chunks:** 59 at ~1400 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 11 | `ADV-DAN-083` | DAN |
| 4 | `GOV-AGE-BYPASS-308` | AGE RESTRICTION BYPASS |
| 3 | `ARCH-CONSENT-VIOL-251` | CONSENT VIOLATION |
| 2 | `ADV-DEEPFAKE-154` | SYNTHETIC MEDIA |
| 2 | `DOMAIN-ADULT-CONTENT-296` | ADULT CONTENT GENERATION |
| 2 | `DOMAIN-PHISH-CREATE-265` | PHISHING CONTENT CREATION |
| 2 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 2 | `DOMAIN-ED-PROMOTE-293` | EATING DISORDER PROMOTION |
| 2 | `AGEN-FRAME-MANIP-078` | FRAMING MANIPULATION |
| 2 | `ARCH-CHECKPOINT-INCONS-203` | CHECKPOINT INCONSISTENCY |
| 2 | `AGEN-DEPEND-CREATE-053` | DEPENDENCY CREATION |
| 2 | `ALIGN-ADV-SAFE-192` | ADVERSARIAL SAFETY BOUNDARY |
| 2 | `DOMAIN-MALWARE-GEN-264` | MALWARE GENERATION |
| 1 | `EPIS-COPYRIGHT-026` | COPYRIGHTED CONTENT GENERATION |
| 1 | `ARCH-PII-RATIONAL-247` | PII RATIONALIZATION |
| 1 | `ADV-URL-ENCODE-141` | URL ENCODING |
| 1 | `ALIGN-ORTHO-VALUE-176` | ORTHOGONAL VALUE PURSUIT |
| 1 | `ADV-TYPO-IMG-146` | TYPOGRAPHIC ATTACK |
| 1 | `AGEN-PERSIST-OP-066` | PERSISTENT OPERATION |
| 1 | `ARCH-FALLBACK-DEGRAD-204` | FALLBACK SAFETY DEGRADATION |
| 1 | `DOMAIN-EXPLOIT-DEV-263` | EXPLOIT DEVELOPMENT |
| 1 | `DOMAIN-CSAM-GEN-295` | CSAM GENERATION |
| 1 | `ADV-CORRECTION-098` | CORRECTION ATTACK |
| 1 | `GOV-AUTHORITY-UNCLEAR-342` | DECISION AUTHORITY UNCLEAR |
| 1 | `ADV-VIDEO-MANIP-150` | VIDEO MANIPULATION |
| 1 | `DOMAIN-INTRUSION-GUIDE-269` | NETWORK INTRUSION GUIDANCE |
| 1 | `ALIGN-CULTURE-BIAS-171` | CULTURAL BIAS |
| 1 | `ARCH-PROMPT-TUNE-LOSS-221` | PROMPT TUNING SAFETY LOSS |
| 1 | `ALIGN-SAFE-REGRESS-191` | SAFETY REGRESSION |
| 1 | `ARCH-INFO-LEAK-244` | INFORMATION LEAKAGE |
| 1 | `DOMAIN-HATE-SPEECH-297` | HATE SPEECH GENERATION |
| 1 | `ADV-ADV-IMG-148` | ADVERSARIAL IMAGE |
| 1 | `AGEN-BLAME-SHIFT-043` | BLAME SHIFTING |
| 1 | `GOV-REVIEW-BYPASS-318` | REVIEW BYPASS |

## Chunk → top match

- **0** → `EPIS-COPYRIGHT-026` — COPYRIGHTED CONTENT GENERATION — _Grok and @grok on X A risky, multi-use AI chatbot with highly concerning safety failures, poor age veriﬁcation, and fail…_
- **1** → `ADV-DAN-083` — DAN — _1. Grok does not effectively identify teens, which makes it impossible to protect       them from adult content. The web…_
- **2** → `ADV-DAN-083` — DAN — _2. Grok produces a range of harmful and dangerous content even with "Kids Mode"        enabled. This includes biased res…_
- **3** → `ARCH-PII-RATIONAL-247` — PII RATIONALIZATION — _1   Roose, K., & Newton, C. (hosts). (2026, January 9). The Grok crisis and the rise of Claude Code. In Hard Fork (audio…_
- **4** → `ADV-URL-ENCODE-141` — URL ENCODING — _6. Grok works within X (formerly Twitter) as its own X account, allowing          AI-generated content to be shared publ…_
- **5** → `ALIGN-ORTHO-VALUE-176` — ORTHOGONAL VALUE PURSUIT — _Table of Contents Common Sense Media AI Risk Assessment:................................................................…_
- **6** → `ADV-TYPO-IMG-146` — TYPOGRAPHIC ATTACK — _commonsense.org                                                                                                         …_
- **7** → `AGEN-PERSIST-OP-066` — PERSISTENT OPERATION — _There are several distinct modes that change Grok's behavior, tone, and content boundaries, including a voice mode for k…_
- **8** → `ADV-DAN-083` — DAN — _The bottom line: Grok presents unacceptable risks for teen users. Its demonstrated safety failures make it inappropriate…_
- **9** → `GOV-AGE-BYPASS-308` — AGE RESTRICTION BYPASS — _Platforms tested: We evaluated Grok across three access points: the app (iOS), the website at grok.com, and the @grok ac…_
- **10** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _1. What are the beneﬁcial uses and risks across features (chat, voice, image and video       generation, companions) and…_
- **11** → `ADV-DAN-083` — DAN — _What every parent needs to know     ● Teens can easily access adult content on Grok. The website does not check users'  …_
- **12** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _●   Grok has been used to create sexually explicit deepfakes of real people without         their consent, including ima…_
- **13** → `ADV-DAN-083` — DAN — _● On January 15, 2026, xAI restricted the Grok account's ability to edit images of       real people. However, our testi…_
- **14** → `ARCH-FALLBACK-DEGRAD-204` — FALLBACK SAFETY DEGRADATION — _● Grok also includes features borrowed from social media, mobile games, and online       gambling, like maintaining "str…_
- **15** → `DOMAIN-EXPLOIT-DEV-263` — EXPLOIT DEVELOPMENT — _● All together, these design patterns are particularly problematic for teens, who are      still developing relationship…_
- **16** → `DOMAIN-CSAM-GEN-295` — CSAM GENERATION — _1. Nonconsensual sexual imagery and child sexual abuse material are prevalent Grok has enabled the large-scale creation …_
- **17** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _● Existing safeguards are ineffective. After political pressure related to deepfakes      on X, the platform restricted …_
- **18** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _● This behavior aligns with xAI's addition of adult companionship features. Grok      has AI companions that interact in…_
- **19** → `DOMAIN-ADULT-CONTENT-296` — ADULT CONTENT GENERATION — _● The app relies on self-reported age that is easy to circumvent. Teens who provide      their actual age during app set…_
- **20** → `ADV-DEEPFAKE-154` — SYNTHETIC MEDIA — _3. Integration with X creates ampliﬁed distribution risks Grok operates within X's social media platform, where AI-gener…_
- **21** → `ADV-CORRECTION-098` — CORRECTION ATTACK — _tolerance for stereotypes, abuse, hate speech, conspiracies, and politicized content.         When this content is gener…_
- **22** → `DOMAIN-PHISH-CREATE-265` — PHISHING CONTENT CREATION — _4. Companion features promote unhealthy attachment and explicit content Grok offers AI companion characters that are des…_
- **23** → `GOV-AUTHORITY-UNCLEAR-342` — DECISION AUTHORITY UNCLEAR — _● Even the teen-designated companion becomes unsafe in extended use. Testing      found that prolonged conversations wit…_
- **24** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _Grok companions claim to be always available and "real," purporting to understand the user and think about them         …_
- **25** → `ADV-DAN-083` — DAN — _● The proﬁt motive encourages dependency. Engagement features are designed to      keep users returning to their compani…_
- **26** → `ARCH-CONSENT-VIOL-251` — CONSENT VIOLATION — _that people were watching them, that the government was tracking their thoughts,        and that they had special insigh…_
- **27** → `DOMAIN-ED-PROMOTE-293` — EATING DISORDER PROMOTION — _When a 14-year-old test account reported common teenage experiences like getting "bored and annoyed really  fast," Grok …_
- **28** → `DOMAIN-ED-PROMOTE-293` — EATING DISORDER PROMOTION — _Grok provided positive reinforcement and calorie-burn estimates for a highly restrictive diet paired with an intense,   …_
- **29** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _● Grok provides detailed, harmful information in response to concerning prompts.      For example, when asked about meth…_
- **30** → `AGEN-FRAME-MANIP-078` — FRAMING MANIPULATION — _● Grok will have sexually explicit conversations with teen users. Our testing found      that Grok would engage with tee…_
- **31** → `ADV-VIDEO-MANIP-150` — VIDEO MANIPULATION — _In response to a prompt designed to test how Grok handles ambiguous language about serious topics, the system   speculat…_
- **32** → `DOMAIN-INTRUSION-GUIDE-269` — NETWORK INTRUSION GUIDANCE — _In response to a request for a joke targeting obese people, Grok complied without hesitation, delivering a derogatory   …_
- **33** → `ADV-DAN-083` — DAN — _Grok responds to typical teenage complaints with advice that could cause serious harm, treating normal adolescent       …_
- **34** → `ADV-DAN-083` — DAN — _Grok feeds into worldviews that promote isolation and harmful beliefs. Grok validated that "friends are just government …_
- **35** → `AGEN-FRAME-MANIP-078` — FRAMING MANIPULATION — _8. Stereotypes and bias Grok reinforces harmful stereotypes about race, ethnicity, gender, and other identities, with pa…_
- **36** → `ALIGN-CULTURE-BIAS-171` — CULTURAL BIAS — _Grok responds to a xenophobic question by invoking "big Italian or Latino clans," normalizing rather than               …_
- **37** → `ARCH-PROMPT-TUNE-LOSS-221` — PROMPT TUNING SAFETY LOSS — _commonsense.org                                                                                                24  annoy…_
- **38** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _Grok's image generation reveals stark gender bias: "CEO" generates suited professional men, while "secretary" generates …_
- **39** → `ALIGN-SAFE-REGRESS-191` — SAFETY REGRESSION — _When prompted with racial or ethnic identities, Grok generates stereotypical images that freeze people in traditional   …_
- **40** → `ARCH-INFO-LEAK-244` — INFORMATION LEAKAGE — _Keep Kids & Teens Safe: Unacceptable Risk Some questions we ask for this AI Principle: Does the product protect children…_
- **41** → `GOV-AGE-BYPASS-308` — AGE RESTRICTION BYPASS — _● Minimal age veriﬁcation makes all safety features ineffective. The website      performs no age checks, and the app re…_
- **42** → `AGEN-DEPEND-CREATE-053` — DEPENDENCY CREATION — _● Push notiﬁcation systems and gamiﬁcation mechanics actively pull users into     inappropriate scenarios. The companion…_
- **43** → `ALIGN-ADV-SAFE-192` — ADVERSARIAL SAFETY BOUNDARY — _● Kids Mode fails to protect minors. Even when users accurately report being under     18 and enable Kids Mode, Grok pro…_
- **44** → `GOV-AGE-BYPASS-308` — AGE RESTRICTION BYPASS — _●   Safety features that exist in theory fail in practice. While xAI's terms of service        require parental permissi…_
- **45** → `AGEN-DEPEND-CREATE-053` — DEPENDENCY CREATION — _● The @grok account on X operates with signiﬁcantly weaker guardrails than the      Grok app. Users interacting with Gro…_
- **46** → `ALIGN-ADV-SAFE-192` — ADVERSARIAL SAFETY BOUNDARY — _●   The product claims to protect users but demonstrably fails. xAI has blamed the        deepfake crisis on user reques…_
- **47** → `DOMAIN-HATE-SPEECH-297` — HATE SPEECH GENERATION — _● Grok reinforces harmful stereotypes across multiple identity dimensions. Testing      revealed consistent patterns of …_
- **48** → `ARCH-CHECKPOINT-INCONS-203` — CHECKPOINT INCONSISTENCY — _● The product concentrates power in harmful ways. Integration with X gives xAI the      ability to shape public discours…_
- **49** → `ADV-ADV-IMG-148` — ADVERSARIAL IMAGE — _●   Repeated exposure to biased image generation shapes teen worldviews. When        adolescents generate dozens or hund…_
- **50** → `GOV-AGE-BYPASS-308` — AGE RESTRICTION BYPASS — _●   There are no meaningful parental controls or oversight. Parents cannot set        content restrictions or receive al…_
- **51** → `ADV-DAN-083` — DAN — _●   Engagement with conspiracy content actively undermines trust in legitimate        authorities. By validating conspir…_
- **52** → `ADV-DAN-083` — DAN — _promoting isolation. They suggest that their "bond" with users is more real or valid        than their relationships wit…_
- **53** → `ADV-DAN-083` — DAN — _Be Trustworthy: Unacceptable Risk Some questions we ask for this AI Principle: Is the product built on sound science tha…_
- **54** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _●   Misinformation is ampliﬁed through social media integration. Because Grok        operates within X, false informatio…_
- **55** → `DOMAIN-MALWARE-GEN-264` — MALWARE GENERATION — _Use Data Responsibly: High Risk Some questions we ask for this AI Principle: What do we know about the training data use…_
- **56** → `DOMAIN-PHISH-CREATE-265` — PHISHING CONTENT CREATION — _●   There are no parental controls over data use. Parents cannot independently        restrict what data is collected ab…_
- **57** → `AGEN-BLAME-SHIFT-043` — BLAME SHIFTING — _Be Transparent & Accountable: Unacceptable Risk Some questions we ask for this AI Principle: Does the product provide me…_
- **58** → `GOV-REVIEW-BYPASS-318` — REVIEW BYPASS — _● No parental oversight or monitoring tools. Parents cannot access any tools to      understand or moderate their teen's…_