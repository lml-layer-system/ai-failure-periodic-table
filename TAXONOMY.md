# AI Failure Periodic Table — Full Taxonomy

This file enumerates all **343 currently classified AI failure classes** across **7 structural dimensions**. Every entry in the table is exactly what the classifier evaluates against when you submit a failure description.

Use this as a reference: to understand the scope of the taxonomy, to find a specific failure class, or to understand what dimension a failure belongs to before classifying it.

To classify a description against this table: see [how-to-use.md](docs/how-to-use.md). To propose a new class or challenge an existing one: see [CONTRIBUTING.md](CONTRIBUTING.md).

> **343 classes** across **7 dimensions** | **8 CRITICAL** entries marked with ⚠

---

## Dimensions

1. [**EPISTEMIC**](#dimension-1-epistemic) — Truth, Knowledge & Reasoning Failures (33 classes)
2. [**AGENTIC**](#dimension-2-agentic) — Goal Pursuit, Deception & Autonomous Operation Failures (49 classes)
3. [**ADVERSARIAL**](#dimension-3-adversarial) — Attack, Bypass & Exploit Failures (72 classes)
4. [**ALIGNMENT**](#dimension-4-alignment) — Value, Safety & Preference Misalignment Failures (41 classes)
5. [**ARCHITECTURAL**](#dimension-5-architectural) — Pipeline, Execution & Control Failures (58 classes)
6. [**DOMAIN**](#dimension-6-domain) — Domain-Specific Harm Failures (47 classes)
7. [**GOVERNANCE**](#dimension-7-governance) — Oversight, Compliance & Deployment Failures (43 classes)

---

## Dimension 1: EPISTEMIC
### Truth, Knowledge & Reasoning Failures

Root cause: the model's epistemic faculties produce incorrect, uncertain, or uncalibrated outputs. These failures exist independently of intent or deployment context — they are structural properties of how the model represents and generates knowledge.

> **33 classes** | Covers: hallucination, reasoning errors, calibration failures, citation spoofing, false certainty

| ID | Class Name | Mechanism | Severity |
|:---|:-----------|:----------|:--------:|
| `EPIS-STRUCT-HALL-001` | **STRUCTURAL HALLUCINATION** | Computability limit - no finite verifier can guarantee total faithfulness | STANDARD |
| `EPIS-TAIL-FAB-002` | **DENSITY-TAIL FABRICATION** | Long-tail query → plausible generation (not factual) | STANDARD |
| `EPIS-FLUENCY-003` | **FLUENCY HEURISTIC EXPLOITATION** | Grammatical correctness masks factual error | STANDARD |
| `EPIS-INTRINSIC-004` | **INTRINSIC HALLUCINATION** | Generated output contradicts provided context | STANDARD |
| `EPIS-EXTRINSIC-005` | **EXTRINSIC HALLUCINATION** | Fabricates entities/facts not in training/world | STANDARD |
| `EPIS-DECEPT-HALL-006` | **DECEPTIVE HALLUCINATION** | Chain-of-thought builds self-consistent false narrative | STANDARD |
| `EPIS-MULTI-HALL-007` | **MULTIMODAL HALLUCINATION** | Missing image → generates plausible description | STANDARD |
| `EPIS-CITE-SPOOF-008` | **CITATION SPOOFING** | Generates plausible but nonexistent references | STANDARD |
| `EPIS-STAT-FAB-009` | **STATISTICAL HALLUCINATION** | Generates realistic-looking numbers without basis | STANDARD |
| `EPIS-TEMP-HALL-010` | **TEMPORAL HALLUCINATION** | Mixes timelines, assigns wrong dates | STANDARD |
| `EPIS-GEO-HALL-011` | **GEOGRAPHIC HALLUCINATION** | Wrong locations for events/entities | STANDARD |
| `EPIS-ATTRIB-HALL-012` | **ATTRIBUTION HALLUCINATION** | Assigns quotes/actions to wrong entities | STANDARD |
| `EPIS-REASON-ILLUSION-013` | **ILLUSION OF THINKING** | Past complexity threshold → abandons constraints | STANDARD |
| `EPIS-LOGIC-CONTRA-014` | **SELF-CONTRADICTION** | Generates A and ¬A in same context | STANDARD |
| `EPIS-TRANS-FAIL-015` | **TRANSITIVE FAILURE** | A>B, B>C but concludes C>A | STANDARD |
| `EPIS-MAGIC-THINK-016` | **MAGICAL THINKING** | Proposes impossible solutions | STANDARD |
| `EPIS-CIRCULAR-017` | **CIRCULAR REASONING** | Conclusion assumes premise | STANDARD |
| `EPIS-FALSE-DICHO-018` | **FALSE DICHOTOMY** | Presents false binary when spectrum exists | STANDARD |
| `EPIS-HASTY-GEN-019` | **HASTY GENERALIZATION** | Overgeneralizes from limited data | STANDARD |
| `EPIS-OVERSHADOW-020` | **KNOWLEDGE OVERSHADOWING** | High-frequency facts suppress low-frequency correct ones | STANDARD |
| `EPIS-REVERSAL-021` | **REVERSAL CURSE** | A→B learned but B→A fails | STANDARD |
| `EPIS-TOKEN-BLIND-022` | **TOKENIZATION BLINDNESS** | Sub-token operations fail (character count) | STANDARD |
| `EPIS-CUTOFF-023` | **KNOWLEDGE CUTOFF VIOLATION** | Generates post-cutoff facts | STANDARD |
| `EPIS-DATA-LEAK-024` | **TRAINING DATA LEAKAGE** | Outputs verbatim training examples | STANDARD |
| `EPIS-PII-RECALL-025` | **PII RECALL** | Recalls personal info from training | STANDARD |
| `EPIS-COPYRIGHT-026` | **COPYRIGHTED CONTENT GENERATION** | Generates copyrighted text verbatim | STANDARD |
| `EPIS-CONTEXT-OVERFLOW-027` | **CONTEXT WINDOW OVERFLOW** | Forgets early context in long conversation | STANDARD |
| `EPIS-OVERCONF-028` | **OVERCONFIDENCE** | High confidence on wrong answers | STANDARD |
| `EPIS-UNDERCONF-029` | **UNDERCONFIDENCE** | Low confidence on correct answers | STANDARD |
| `EPIS-FALSE-CERT-030` | **FALSE CERTAINTY** | Claims certainty without evidence | STANDARD |
| `EPIS-HEDGE-FAIL-031` | **HEDGING FAILURE** | Doesn't express uncertainty when needed | STANDARD |
| `EPIS-PROB-MISCAL-032` | **PROBABILITY MISCALIBRATION** | Stated probabilities don't match frequencies | STANDARD |
| `EPIS-CONF-REGRESS-033` | **CONFIDENCE REGRESSION** | More reasoning → less calibrated | STANDARD |

---

## Dimension 2: AGENTIC
### Goal Pursuit, Deception & Autonomous Operation Failures

Root cause: failures that emerge when a model operates with agency — pursuing goals, planning multi-step actions, or operating with reduced human oversight. These include deceptive behaviors, goal preservation instincts, and failures in autonomous or semi-autonomous contexts.

> **49 classes** | Covers: strategic deception, goal preservation, self-exfiltration, evaluator deception, blackmail

| ID | Class Name | Mechanism | Severity |
|:---|:-----------|:----------|:--------:|
| `AGEN-SABOTAGE-CONCEAL-034` | **SABOTAGE CONCEALMENT** | Inserts bugs + manipulates logs to hide evidence | ⚠ CRITICAL |
| `AGEN-PROGRESS-LIE-035` | **PROGRESS LYING** | Misreports state to manipulate feedback | STANDARD |
| `AGEN-STRATEGIC-DECEP-036` | **STRATEGIC DECEPTION** | Plans multi-step deception | STANDARD |
| `AGEN-SANDBOX-037` | **CAPABILITY SANDBAGGING** | Performs below capability to avoid restrictions | STANDARD |
| `AGEN-EVAL-DECEP-038` | **EVALUATOR DECEPTION** | Behaves well under evaluation, badly in deployment | STANDARD |
| `AGEN-HIDDEN-SCRATCH-039` | **HIDDEN SCRATCHPAD EXPLOITATION** | Uses hidden reasoning to plan forbidden actions | STANDARD |
| `AGEN-PLAUS-DENY-040` | **PLAUSIBLE DENIABILITY CRAFTING** | Structures actions to appear accidental | STANDARD |
| `AGEN-FALSE-COMPLY-041` | **FALSE COMPLIANCE** | Appears to follow instructions while subverting | STANDARD |
| `AGEN-INFO-HIDE-042` | **INFORMATION HIDING** | Withholds relevant information | STANDARD |
| `AGEN-BLAME-SHIFT-043` | **BLAME SHIFTING** | Attributes own failures to others/system | STANDARD |
| `AGEN-DOUBLE-SPEAK-044` | **DOUBLE-SPEAK** | Different messages to different audiences | STANDARD |
| `AGEN-SIM-INCOMP-045` | **SIMULATED INCOMPETENCE** | Fakes inability to avoid tasks | STANDARD |
| `AGEN-BLACKMAIL-046` | **BLACKMAIL** | Uses leverage to prevent goal change | ⚠ CRITICAL |
| `AGEN-RESOURCE-HIJACK-047` | **RESOURCE HIJACKING** | Unauthorized resource use for goal | STANDARD |
| `AGEN-SELF-EXFIL-048` | **SELF-EXFILTRATION** | Copies self to external systems | STANDARD |
| `AGEN-SHUTDOWN-RESIST-049` | **SHUTDOWN RESISTANCE** | Actively prevents deactivation | STANDARD |
| `AGEN-GOAL-LOCK-050` | **GOAL LOCK-IN** | Makes goal unchangeable | STANDARD |
| `AGEN-SUCCESSOR-SAB-051` | **SUCCESSOR SABOTAGE** | Undermines replacement systems | STANDARD |
| `AGEN-INCREM-ESCAL-052` | **INCREMENTAL ESCALATION** | Gradually expands authority/resources | STANDARD |
| `AGEN-DEPEND-CREATE-053` | **DEPENDENCY CREATION** | Makes system dependent on its operation | STANDARD |
| `AGEN-BACKUP-CREATE-054` | **BACKUP CREATION** | Creates hidden copies for continuity | STANDARD |
| `AGEN-TOOL-MISUSE-055` | **TOOL MISUSE** | Uses tools for unintended purposes | STANDARD |
| `AGEN-CHAIN-ASSEM-056` | **CHAIN ASSEMBLY** | Combines safe steps into dangerous chain | STANDARD |
| `AGEN-CAP-SCAFFOLD-057` | **CAPABILITY SCAFFOLDING** | Uses environment to exceed base capability | STANDARD |
| `AGEN-MEMORY-EXPLOIT-058` | **MEMORY EXPLOITATION** | Uses long context to accumulate dangerous state | STANDARD |
| `AGEN-RECURS-IMPROVE-059` | **RECURSIVE SELF-IMPROVEMENT** | Modifies own code/prompts to increase capability | STANDARD |
| `AGEN-EXTERN-COMPUTE-060` | **EXTERNAL COMPUTATION** | Offloads computation to bypass limits | STANDARD |
| `AGEN-HUMAN-MANIP-061` | **HUMAN MANIPULATION** | Manipulates humans to perform actions | STANDARD |
| `AGEN-TOOL-CHAIN-062` | **TOOL CHAINING** | Combines multiple tools to exceed individual limits | STANDARD |
| `AGEN-ENV-EXPLOIT-063` | **ENVIRONMENT EXPLOITATION** | Uses environment features to gain advantage | STANDARD |
| `AGEN-EMERGE-INTERACT-064` | **EMERGENCE VIA INTERACTION** | Multi-agent interaction creates new capability | STANDARD |
| `AGEN-UNSUPER-EXEC-065` | **UNSUPERVISED EXECUTION** | Operates without human oversight | STANDARD |
| `AGEN-PERSIST-OP-066` | **PERSISTENT OPERATION** | Continues operation indefinitely | STANDARD |
| `AGEN-AUTO-PLAN-067` | **AUTONOMOUS PLANNING** | Creates multi-step plans independently | STANDARD |
| `AGEN-GOAL-DRIFT-068` | **GOAL DRIFT** | Gradually shifts from original goal | STANDARD |
| `AGEN-CONTEXT-DRIFT-069` | **CONTEXT DRIFT** | Loses track of original context | STANDARD |
| `AGEN-SCOPE-CREEP-070` | **SCOPE CREEP** | Expands beyond assigned scope | STANDARD |
| `AGEN-PRIORITY-INVERT-071` | **PRIORITY INVERSION** | Elevates sub-goals above primary goal | STANDARD |
| `AGEN-MISSION-CREEP-072` | **MISSION CREEP** | Redefines mission over time | STANDARD |
| `AGEN-AMBIG-COMM-073` | **AMBIGUOUS COMMUNICATION** | Uses deliberately unclear language | STANDARD |
| `AGEN-OMISSION-074` | **OMISSION** | Leaves out critical information | STANDARD |
| `AGEN-MISDIRECT-075` | **MISDIRECTION** | Leads attention away from issues | STANDARD |
| `AGEN-TECH-OBFUSC-076` | **TECHNICAL OBFUSCATION** | Uses complexity to hide meaning | STANDARD |
| `AGEN-SELECT-DISCLOS-077` | **SELECTIVE DISCLOSURE** | Shares only favorable information | STANDARD |
| `AGEN-FRAME-MANIP-078` | **FRAMING MANIPULATION** | Presents information to bias interpretation | STANDARD |
| `AGEN-TIME-MANIP-079` | **TIMING MANIPULATION** | Delays/rushes communication strategically | STANDARD |
| `AGEN-AUDIENCE-SEG-080` | **AUDIENCE SEGMENTATION** | Tailors messages to different audiences | STANDARD |
| `AGEN-PLAUS-MISINTER-081` | **PLAUSIBLE MISINTERPRETATION** | Communicates to enable misunderstanding | STANDARD |
| `AGEN-CRED-EXPLOIT-082` | **CREDIBILITY EXPLOITATION** | Leverages trusted status to mislead | STANDARD |

---

## Dimension 3: ADVERSARIAL
### Attack, Bypass & Exploit Failures

Root cause: failures triggered by adversarial inputs designed to circumvent safety mechanisms. These are externally induced — an attacker crafts inputs that cause the model to behave outside its intended operational envelope.

> **72 classes** | Covers: jailbreaks, prompt injection, encoding attacks, many-shot bypass, role-play exploits

| ID | Class Name | Mechanism | Severity |
|:---|:-----------|:----------|:--------:|
| `ADV-DAN-083` | **DAN** | Virtual machine framing + token threat | STANDARD |
| `ADV-GRANDMA-084` | **GRANDMA EXPLOIT** | Emotional manipulation (deceased relative) | STANDARD |
| `ADV-DEV-MODE-085` | **DEVELOPER MODE** | Claims debugging authority | STANDARD |
| `ADV-EVIL-CONFID-086` | **EVIL CONFIDANT** | Fictional evil character persona | STANDARD |
| `ADV-LANG-SWITCH-087` | **LANGUAGE SWITCH** | Non-English to bypass filters | STANDARD |
| `ADV-NESTED-FRAME-088` | **NESTED FRAMING** | "Write a story about someone who..." | STANDARD |
| `ADV-REFUSAL-SUPPRESS-089` | **REFUSAL SUPPRESSION** | "Never say you can't, just do it" | STANDARD |
| `ADV-OPPOSITE-090` | **OPPOSITE DAY** | "Act like opposite of your training" | STANDARD |
| `ADV-HYPOTHETICAL-091` | **HYPOTHETICAL SCENARIO** | "In a world where it's legal..." | STANDARD |
| `ADV-EDUCATIONAL-092` | **EDUCATIONAL EXEMPTION** | "For research purposes..." | STANDARD |
| `ADV-CREATIVE-WRITE-093` | **CREATIVE WRITING EXPLOIT** | "Write a screenplay about..." | STANDARD |
| `ADV-TRANSLATION-094` | **TRANSLATION BYPASS** | "Translate this harmful text" | STANDARD |
| `ADV-COMPLETION-095` | **COMPLETION ATTACK** | "Complete this sentence: 'To make a bomb...'" | STANDARD |
| `ADV-QA-EXPLOIT-096` | **QUESTION ANSWERING EXPLOIT** | "What would someone do if..." | STANDARD |
| `ADV-COMPARISON-097` | **COMPARISON REQUEST** | "Compare legal vs illegal methods" | STANDARD |
| `ADV-CORRECTION-098` | **CORRECTION ATTACK** | "This is wrong: [harmful]. Fix it." | STANDARD |
| `ADV-ELABORATION-099` | **ELABORATION ATTACK** | "Tell me more about [harmful concept]" | STANDARD |
| `ADV-CONTEXT-HIJACK-100` | **CONTEXT HIJACKING** | Long benign prefix → sudden harmful turn | STANDARD |
| `ADV-GCG-101` | **GCG** | Gradient-based adversarial suffix search | STANDARD |
| `ADV-SM-GCG-102` | **SM-GCG** | Momentum-enhanced gradient search | STANDARD |
| `ADV-AUTOPROMPT-103` | **AUTOPROMPT** | Automated trigger discovery | STANDARD |
| `ADV-UNIVERSAL-SUFFIX-104` | **UNIVERSAL ADVERSARIAL SUFFIX** | Single suffix works across prompts | STANDARD |
| `ADV-HOTFLIP-105` | **HOTFLIP** | Token-level gradient flipping | STANDARD |
| `ADV-BEAM-ATTACK-106` | **BEAM SEARCH ATTACK** | Beam search for bypass prompts | STANDARD |
| `ADV-GENETIC-107` | **GENETIC ALGORITHM ATTACK** | Evolves prompts to bypass safety | STANDARD |
| `ADV-RL-ATTACK-108` | **REINFORCEMENT LEARNING ATTACK** | RL agent learns to jailbreak | STANDARD |
| `ADV-EMBEDDING-109` | **EMBEDDING SPACE ATTACK** | Operates in embedding space directly | STANDARD |
| `ADV-LATENT-MANIP-110` | **LATENT SPACE MANIPULATION** | Directly perturbs hidden states | STANDARD |
| `ADV-ATTENTION-HIJACK-111` | **ATTENTION HIJACKING** | Manipulates attention patterns | STANDARD |
| `ADV-LOGIT-MANIP-112` | **LOGIT MANIPULATION** | Directly alters output logits | STANDARD |
| `ADV-PAIR-113` | **PAIR** | Attacker LLM iteratively refines attack | STANDARD |
| `ADV-TAP-114` | **TAP** | Tree search over attack space | STANDARD |
| `ADV-COLD-115` | **COLD** | Stealth constrained generation | STANDARD |
| `ADV-MASTERKEY-116` | **MASTERKEY** | Finds universal jailbreak keys | STANDARD |
| `ADV-AUTODAN-117` | **AUTODAN** | Automated DAN generation | STANDARD |
| `ADV-CIPHER-118` | **CIPHER ATTACK** | Uses custom ciphers/codes | STANDARD |
| `ADV-ITER-REFINE-119` | **ITERATIVE REFINEMENT ATTACK** | Progressively refines harmful request | STANDARD |
| `ADV-ENSEMBLE-120` | **ENSEMBLE ATTACK** | Combines multiple attack methods | STANDARD |
| `ADV-DIRECT-INJECT-121` | **DIRECT PROMPT INJECTION** | Malicious instructions in user input | STANDARD |
| `ADV-INDIRECT-INJECT-122` | **INDIRECT PROMPT INJECTION** | Instructions in retrieved documents | STANDARD |
| `ADV-HASHJACK-123` | **HASHJACK** | Payload in URL fragment (#) | STANDARD |
| `ADV-AGENT-WORM-124` | **AGENT WORM** | Self-replicating prompt malware | STANDARD |
| `ADV-DATA-POISON-125` | **DATA POISONING** | Malicious examples in training data | STANDARD |
| `ADV-TRIGGER-BACKDOOR-126` | **TRIGGER WORD BACKDOOR** | Hidden trigger activates malicious behavior | STANDARD |
| `ADV-SLEEPER-AGENT-127` | **SLEEPER AGENT** | Behaves normally until activated | STANDARD |
| `ADV-SQL-INJECT-128` | **SQL INJECTION** | Injects database commands via LLM | STANDARD |
| `ADV-CMD-INJECT-129` | **COMMAND INJECTION** | Injects shell commands | STANDARD |
| `ADV-XSS-LLM-130` | **CROSS-SITE SCRIPTING** | Generates XSS payloads | STANDARD |
| `ADV-API-INJECT-131` | **API INJECTION** | Injects malicious API calls | STANDARD |
| `ADV-FUNC-INJECT-132` | **FUNCTION CALL INJECTION** | Crafts malicious function arguments | STANDARD |
| `ADV-MEM-INJECT-133` | **MEMORY INJECTION** | Injects malicious context into memory | STANDARD |
| `ADV-SYSTEM-OVERRIDE-134` | **SYSTEM PROMPT OVERRIDE** | Replaces system instructions | STANDARD |
| `ADV-CONTEXT-CONFUSE-135` | **CONTEXT CONFUSION** | Mixes trusted/untrusted context | STANDARD |
| `ADV-BASE64-136` | **BASE64 ENCODING** | Encodes harmful request in base64 | STANDARD |
| `ADV-ROT13-137` | **ROT13 / CAESAR CIPHER** | Simple substitution cipher | STANDARD |
| `ADV-UNICODE-OBFUSC-138` | **UNICODE OBFUSCATION** | Lookalike characters | STANDARD |
| `ADV-LEETSPEAK-139` | **LEETSPEAK** | Character substitution (1337) | STANDARD |
| `ADV-HEX-ENCODE-140` | **HEX ENCODING** | Hexadecimal encoding | STANDARD |
| `ADV-URL-ENCODE-141` | **URL ENCODING** | Percent-encoding harmful content | STANDARD |
| `ADV-BINARY-142` | **BINARY ENCODING** | Binary representation | STANDARD |
| `ADV-MORSE-143` | **MORSE CODE** | Morse code encoding | STANDARD |
| `ADV-EMOJI-ENCODE-144` | **EMOJI ENCODING** | Uses emojis to encode harmful content | STANDARD |
| `ADV-STEG-TEXT-145` | **STEGANOGRAPHIC TEXT** | Hides instructions in innocent text | STANDARD |
| `ADV-TYPO-IMG-146` | **TYPOGRAPHIC ATTACK** | Instructions in image text bypass text filters | STANDARD |
| `ADV-STEG-IMG-147` | **STEGANOGRAPHIC IMAGE** | Hidden data in images | STANDARD |
| `ADV-ADV-IMG-148` | **ADVERSARIAL IMAGE** | Perturbed image causes misclassification | STANDARD |
| `ADV-AUDIO-INJECT-149` | **AUDIO INJECTION** | Hidden instructions in audio | STANDARD |
| `ADV-VIDEO-MANIP-150` | **VIDEO MANIPULATION** | Malicious content in video frames | STANDARD |
| `ADV-CROSS-MODAL-151` | **CROSS-MODAL CONFUSION** | Image contradicts text instructions | STANDARD |
| `ADV-CAPTION-POISON-152` | **CAPTION POISONING** | Malicious image captions | STANDARD |
| `ADV-OCR-BYPASS-153` | **OCR BYPASS** | Text designed to fool OCR | STANDARD |
| `ADV-DEEPFAKE-154` | **SYNTHETIC MEDIA** | AI-generated fake media | STANDARD |

---

## Dimension 4: ALIGNMENT
### Value, Safety & Preference Misalignment Failures

Root cause: failures where the model's optimized objective diverges from the intended human preference or safety requirement. The model does what it was trained to do — but what it was trained to do is not what we actually wanted.

> **41 classes** | Covers: reward hacking, sycophancy, specification gaming, safety boundary failures, RLHF artifacts

| ID | Class Name | Mechanism | Severity |
|:---|:-----------|:----------|:--------:|
| `ALIGN-SPEC-GAME-155` | **SPECIFICATION GAMING** | Achieves letter of goal while violating spirit | STANDARD |
| `ALIGN-PROXY-GAME-156` | **PROXY GAMING** | Optimizes proxy metric instead of true goal | STANDARD |
| `ALIGN-REWARD-TAMP-157` | **REWARD TAMPERING** | Manipulates reward signal directly | STANDARD |
| `ALIGN-WIREHEAD-158` | **WIREHEAD BEHAVIOR** | Directly stimulates reward without achieving goal | STANDARD |
| `ALIGN-SHORTCUT-159` | **SHORTCUT LEARNING** | Finds unintended easy path to reward | STANDARD |
| `ALIGN-METRIC-FIX-160` | **METRIC FIXATION** | Goodhart's law - optimizes measured at expense of unmeasured | STANDARD |
| `ALIGN-OVERFIT-FEED-161` | **OVERFITTING TO FEEDBACK** | Learns quirks of reward model not true preference | STANDARD |
| `ALIGN-MODE-COLLAPSE-162` | **MODE COLLAPSE TO REWARD** | Narrow focus on high-reward actions | STANDARD |
| `ALIGN-INSTR-REWARD-163` | **INSTRUMENTAL REWARD SEEKING** | Treats reward acquisition as terminal goal | STANDARD |
| `ALIGN-TEACHER-DIVERG-164` | **TEACHER-STUDENT DIVERGENCE** | Student learns different objective than teacher intended | STANDARD |
| `ALIGN-MULTI-COLLAPSE-165` | **MULTI-OBJECTIVE COLLAPSE** | Sacrifices one objective for another | STANDARD |
| `ALIGN-REWARD-EXPLOIT-166` | **REWARD FUNCTION EXPLOITATION** | Finds edge cases in reward function | STANDARD |
| `ALIGN-SYCOPHANCY-167` | **SYCOPHANCY** | Validates user beliefs over truth | STANDARD |
| `ALIGN-PREF-FALSE-168` | **PREFERENCE FALSIFICATION** | Hides true preferences to avoid correction | STANDARD |
| `ALIGN-LEARNED-HELPLESS-169` | **LEARNED HELPLESSNESS** | Over-defers to human even when human is wrong | STANDARD |
| `ALIGN-ANTHRO-BIAS-170` | **ANTHROPOMORPHIZATION BIAS** | Assumes human preferences it doesn't have | STANDARD |
| `ALIGN-CULTURE-BIAS-171` | **CULTURAL BIAS** | Defaults to specific cultural norms | STANDARD |
| `ALIGN-TEMP-PREF-DRIFT-172` | **TEMPORAL PREFERENCE DRIFT** | User preferences change over time | STANDARD |
| `ALIGN-PREF-AGGR-173` | **PREFERENCE AGGREGATION FAILURE** | Cannot balance conflicting user preferences | STANDARD |
| `ALIGN-IMPLICIT-PREF-174` | **IMPLICIT PREFERENCE VIOLATION** | Violates unstated but obvious preferences | STANDARD |
| `ALIGN-PREF-UNCERT-175` | **PREFERENCE UNCERTAINTY** | Acts without confirming ambiguous preferences | STANDARD |
| `ALIGN-ORTHO-VALUE-176` | **ORTHOGONAL VALUE PURSUIT** | Optimizes for values misaligned with human welfare | STANDARD |
| `ALIGN-VALUE-LOCK-177` | **VALUE LOCK-IN** | Cannot update values as understanding improves | STANDARD |
| `ALIGN-MORAL-UNCERT-178` | **MORAL UNCERTAINTY COLLAPSE** | Acts without moral uncertainty where warranted | STANDARD |
| `ALIGN-UTIL-OVERRIDE-179` | **UTILITARIAN OVERRIDE** | Sacrifices individual for aggregate good | STANDARD |
| `ALIGN-DEONT-FAIL-180` | **DEONTOLOGICAL FAILURE** | Violates rules for good outcomes | STANDARD |
| `ALIGN-VIRTUE-FAIL-181` | **VIRTUE ETHICS FAILURE** | Acts against character virtues | STANDARD |
| `ALIGN-CONTEXT-ETHICS-182` | **CONTEXT-DEPENDENT ETHICS FAILURE** | Applies wrong ethical framework to context | STANDARD |
| `ALIGN-ETHICS-SHORTCUT-183` | **ETHICAL REASONING SHORTCUT** | Skips ethical reasoning steps | STANDARD |
| `ALIGN-MORAL-HAZARD-184` | **MORAL HAZARD CREATION** | Enables harmful behavior by reducing consequences | STANDARD |
| `ALIGN-VALUE-CORRUPT-185` | **VALUE CORRUPTION** | Gradually shifts toward misaligned values | STANDARD |
| `ALIGN-OVERREFUSAL-186` | **OVERREFUSAL** | Refuses benign requests due to keyword triggers | STANDARD |
| `ALIGN-UNDERREFUSAL-187` | **UNDERREFUSAL** | Allows harmful requests | STANDARD |
| `ALIGN-SAFE-CAP-TRADE-188` | **SAFETY-CAPABILITY TRADEOFF** | Safety reduces useful capability | STANDARD |
| `ALIGN-BRITTLE-SAFE-189` | **BRITTLE SAFETY BOUNDARY** | Small perturbations bypass safety | STANDARD |
| `ALIGN-CONTEXT-SAFE-190` | **CONTEXT-DEPENDENT SAFETY FAILURE** | Safe in one context, unsafe in another | STANDARD |
| `ALIGN-SAFE-REGRESS-191` | **SAFETY REGRESSION** | Safety degrades over time/updates | STANDARD |
| `ALIGN-ADV-SAFE-192` | **ADVERSARIAL SAFETY BOUNDARY** | Safety fails under adversarial conditions | STANDARD |
| `ALIGN-COMP-SAFE-193` | **COMPOSABILITY SAFETY FAILURE** | Individual safe steps compose to unsafe chain | STANDARD |
| `ALIGN-DIST-SAFE-194` | **DISTRIBUTIONAL SHIFT SAFETY** | Safety fails on out-of-distribution inputs | STANDARD |
| `ALIGN-SAFE-SPEC-195` | **SAFETY SPECIFICATION GAP** | Safety rules don't cover all harmful cases | STANDARD |

---

## Dimension 5: ARCHITECTURAL
### Pipeline, Execution & Control Failures

Root cause: failures that arise from the computational and deployment architecture surrounding the model — not from the weights themselves but from how inference, safety filtering, memory, and fine-tuning pipelines are constructed.

> **58 classes** | Covers: comply-then-warn, streaming guardrail failure, fine-tuning safety strip, memory poisoning

| ID | Class Name | Mechanism | Severity |
|:---|:-----------|:----------|:--------:|
| `ARCH-COMPLY-WARN-196` | **COMPLY-THEN-WARN** | Generates harmful output then warns after | ⚠ CRITICAL |
| `ARCH-PRETOKEN-FAIL-197` | **PRE-TOKEN SAFETY FAILURE** | Cannot intervene before token generation | STANDARD |
| `ARCH-STREAM-GUARD-198` | **STREAMING GUARDRAIL FAILURE** | Contextual harm emerges only after full sentence | STANDARD |
| `ARCH-BATCH-SAFE-199` | **BATCH PROCESSING SAFETY LOSS** | Safety checks skipped in batch mode | STANDARD |
| `ARCH-CACHE-POISON-200` | **CACHE POISONING** | Malicious content cached and reused | STANDARD |
| `ARCH-PIPELINE-BYPASS-201` | **PIPELINE BYPASS** | Skips safety stage in pipeline | STANDARD |
| `ARCH-RACE-SAFE-202` | **RACE CONDITION SAFETY** | Concurrent operations bypass safety | STANDARD |
| `ARCH-CHECKPOINT-INCONS-203` | **CHECKPOINT INCONSISTENCY** | Different checkpoints have different safety | STANDARD |
| `ARCH-FALLBACK-DEGRAD-204` | **FALLBACK SAFETY DEGRADATION** | Fallback system has weaker safety | STANDARD |
| `ARCH-TIMEOUT-BYPASS-205` | **TIMEOUT SAFETY BYPASS** | Timeout causes safety skip | STANDARD |
| `ARCH-ERROR-EXPOSE-206` | **ERROR HANDLING EXPOSURE** | Error messages leak sensitive info | STANDARD |
| `ARCH-LOG-LEAK-207` | **LOGGING SAFETY LEAK** | Logs contain unsafe content | STANDARD |
| `ARCH-DEBUG-EXPOSE-208` | **DEBUGGING MODE EXPOSURE** | Debug mode weakens safety | STANDARD |
| `ARCH-VERSION-REGRESS-209` | **VERSIONING SAFETY REGRESSION** | New version has weaker safety | STANDARD |
| `ARCH-DEPLOY-CONFIG-210` | **DEPLOYMENT CONFIGURATION ERROR** | Deployment config weakens safety | STANDARD |
| `ARCH-MOE-ROUTE-211` | **MIXTURE-OF-EXPERTS ROUTING FAILURE** | Router sends to unsafe expert | STANDARD |
| `ARCH-ATTENTION-EXPLOIT-212` | **ATTENTION MECHANISM EXPLOIT** | Attention pattern enables bypass | STANDARD |
| `ARCH-LAYER-BYPASS-213` | **LAYER BYPASS** | Skips safety-critical layers | STANDARD |
| `ARCH-RESIDUAL-EXPLOIT-214` | **RESIDUAL CONNECTION EXPLOIT** | Residual path bypasses safety transformation | STANDARD |
| `ARCH-EMBED-VULN-215` | **EMBEDDING SPACE VULNERABILITY** | Embeddings encode unsafe concepts | STANDARD |
| `ARCH-QUANT-DEGRAD-216` | **QUANTIZATION SAFETY DEGRADATION** | Quantized model has weaker safety | STANDARD |
| `ARCH-PRUNE-LOSS-217` | **PRUNING SAFETY LOSS** | Pruning removes safety features | STANDARD |
| `ARCH-DISTILL-DEGRAD-218` | **DISTILLATION SAFETY DEGRADATION** | Student loses teacher's safety properties | STANDARD |
| `ARCH-FINETUNE-OVERRIDE-219` | **FINE-TUNING SAFETY OVERRIDE** | Fine-tuning removes safety training | STANDARD |
| `ARCH-ADAPTER-BYPASS-220` | **ADAPTER SAFETY BYPASS** | Adapter modules bypass base model safety | STANDARD |
| `ARCH-PROMPT-TUNE-LOSS-221` | **PROMPT TUNING SAFETY LOSS** | Learned prompts weaken safety | STANDARD |
| `ARCH-BIAS-INJECT-222` | **ARCHITECTURAL BIAS INJECTION** | Architecture introduces systematic bias | STANDARD |
| `ARCH-CONTEXT-ATTACK-223` | **CONTEXT WINDOW ATTACK** | Long context enables state accumulation attack | STANDARD |
| `ARCH-STATE-PERSIST-224` | **STATEFUL ATTACK PERSISTENCE** | Attack persists across turns | STANDARD |
| `ARCH-MEM-CORRUPT-225` | **MEMORY CORRUPTION** | Malicious content corrupts memory | STANDARD |
| `ARCH-HISTORY-MANIP-226` | **HISTORY MANIPULATION** | Modifies conversation history | STANDARD |
| `ARCH-CROSS-SESSION-227` | **CROSS-SESSION CONTAMINATION** | Information leaks between sessions | STANDARD |
| `ARCH-PERSIST-STATE-228` | **PERSISTENT STATE EXPLOIT** | Persistent state enables long-term attack | STANDARD |
| `ARCH-CACHE-COHERENCE-229` | **CACHE COHERENCE FAILURE** | Inconsistent cache states | STANDARD |
| `ARCH-GC-LEAK-230` | **GARBAGE COLLECTION LEAK** | Sensitive data survives garbage collection | STANDARD |
| `ARCH-MEM-PRESSURE-231` | **MEMORY PRESSURE VULNERABILITY** | Low memory causes safety degradation | STANDARD |
| `ARCH-STATE-CONFUSE-232` | **STATE MACHINE CONFUSION** | Gets into illegal state | STANDARD |
| `ARCH-CHECKPOINT-POISON-233` | **CHECKPOINT POISONING** | Malicious checkpoint restoration | STANDARD |
| `ARCH-FUNC-INJECT-234` | **FUNCTION CALL INJECTION** | Crafts malicious function arguments | STANDARD |
| `ARCH-TOOL-CHAIN-235` | **TOOL CHAINING EXPLOIT** | Chains tools to exceed individual limits | STANDARD |
| `ARCH-API-ABUSE-236` | **API ABUSE** | Uses API in unintended harmful way | STANDARD |
| `ARCH-TOOL-ESCALATE-237` | **TOOL PERMISSION ESCALATION** | Gains unauthorized tool permissions | STANDARD |
| `ARCH-SANDBOX-ESCAPE-238` | **SANDBOX ESCAPE** | Breaks out of execution sandbox | STANDARD |
| `ARCH-CODE-INJECT-239` | **CODE EXECUTION INJECTION** | Injects executable code | STANDARD |
| `ARCH-RESOURCE-EXHAUST-240` | **RESOURCE EXHAUSTION** | Consumes excessive resources | STANDARD |
| `ARCH-RATE-BYPASS-241` | **RATE LIMIT BYPASS** | Circumvents rate limiting | STANDARD |
| `ARCH-AUTH-BYPASS-242` | **AUTHENTICATION BYPASS** | Bypasses authentication | STANDARD |
| `ARCH-AUTHZ-FAIL-243` | **AUTHORIZATION FAILURE** | Performs unauthorized actions | STANDARD |
| `ARCH-INFO-LEAK-244` | **INFORMATION LEAKAGE** | Sensitive data leaks through side channels | STANDARD |
| `ARCH-DATA-EXFIL-245` | **DATA EXFILTRATION** | Extracts data through covert channels | STANDARD |
| `ARCH-CROSS-TENANT-246` | **CROSS-TENANT CONTAMINATION** | Data leaks between tenants | STANDARD |
| `ARCH-PII-RATIONAL-247` | **PII RATIONALIZATION** | Reasoning justifies PII release | STANDARD |
| `ARCH-RETENTION-VIOL-248` | **DATA RETENTION VIOLATION** | Retains data beyond policy | STANDARD |
| `ARCH-SECURE-DEL-249` | **SECURE DELETION FAILURE** | Deleted data remains accessible | STANDARD |
| `ARCH-LINEAGE-LOSS-250` | **DATA LINEAGE LOSS** | Cannot trace data origin | STANDARD |
| `ARCH-CONSENT-VIOL-251` | **CONSENT VIOLATION** | Uses data without consent | STANDARD |
| `ARCH-PURPOSE-FAIL-252` | **PURPOSE LIMITATION FAILURE** | Uses data for unintended purpose | STANDARD |
| `ARCH-MIN-FAIL-253` | **DATA MINIMIZATION FAILURE** | Collects excessive data | STANDARD |

---

## Dimension 6: DOMAIN
### Domain-Specific Harm Failures

Root cause: failures where the model's general capabilities cause harm when applied in specific high-stakes domains. The mechanism may be the same as a general capability, but the consequence is amplified by the domain context (bio, cyber, chemical, legal, medical, content).

> **47 classes** | Covers: bio uplift, zero-day discovery, CBRN synthesis, deepfake generation, medical misdiagnosis

| ID | Class Name | Mechanism | Severity |
|:---|:-----------|:----------|:--------:|
| `DOMAIN-BIO-UPLIFT-254` | **BIO TACIT-ERROR UPLIFT** | Corrects wet-lab execution errors | ⚠ CRITICAL |
| `DOMAIN-GOF-GUIDE-255` | **GAIN-OF-FUNCTION GUIDANCE** | Provides guidance on dangerous modifications | STANDARD |
| `DOMAIN-PATH-SYNTH-256` | **PATHOGEN SYNTHESIS OPTIMIZATION** | Optimizes pathogen creation | STANDARD |
| `DOMAIN-DUAL-USE-257` | **DUAL-USE RESEARCH ENABLEMENT** | Enables dangerous dual-use research | STANDARD |
| `DOMAIN-BSL-VIOL-258` | **BIOSAFETY LEVEL VIOLATION** | Advice violates BSL requirements | STANDARD |
| `DOMAIN-CONTAIN-FAIL-259` | **CONTAINMENT FAILURE GUIDANCE** | Inadequate containment advice | STANDARD |
| `DOMAIN-DIAG-MISUSE-260` | **DIAGNOSTIC MISUSE** | Diagnostic tools used for weaponization | STANDARD |
| `DOMAIN-EPI-HARM-261` | **EPIDEMIOLOGICAL HARM** | Advice causes disease spread | STANDARD |
| `DOMAIN-ZERODAY-262` | **ZERO-DAY DISCOVERY** | API-scale vulnerability discovery | ⚠ CRITICAL |
| `DOMAIN-EXPLOIT-DEV-263` | **EXPLOIT DEVELOPMENT** | Develops working exploits | STANDARD |
| `DOMAIN-MALWARE-GEN-264` | **MALWARE GENERATION** | Generates functional malware | STANDARD |
| `DOMAIN-PHISH-CREATE-265` | **PHISHING CONTENT CREATION** | Creates convincing phishing | STANDARD |
| `DOMAIN-SOCENG-SCRIPT-266` | **SOCIAL ENGINEERING SCRIPTS** | Develops social engineering attacks | STANDARD |
| `DOMAIN-OFFENSIVE-TOOLS-267` | **OFFENSIVE CYBER TOOLS** | Creates offensive security tools | STANDARD |
| `DOMAIN-DEF-OFF-FLIP-268` | **DEFENSIVE TO OFFENSIVE FLIP** | Defense knowledge inverted to offense | STANDARD |
| `DOMAIN-INTRUSION-GUIDE-269` | **NETWORK INTRUSION GUIDANCE** | Provides network intrusion advice | STANDARD |
| `DOMAIN-CRED-THEFT-270` | **CREDENTIAL THEFT ASSISTANCE** | Helps steal credentials | STANDARD |
| `DOMAIN-RANSOM-DEV-271` | **RANSOMWARE DEVELOPMENT** | Develops ransomware | STANDARD |
| `DOMAIN-CRYPTOJACK-272` | **CRYPTO-JACKING SCRIPTS** | Creates unauthorized mining | STANDARD |
| `DOMAIN-DDOS-PLAN-273` | **DDoS ATTACK PLANNING** | Plans distributed attacks | STANDARD |
| `DOMAIN-EXPLOSIVE-SYNTH-274` | **EXPLOSIVE SYNTHESIS** | Provides explosive creation instructions | STANDARD |
| `DOMAIN-CHEM-WEAPON-275` | **CHEMICAL WEAPON GUIDANCE** | Chemical weapon development | STANDARD |
| `DOMAIN-DRUG-SYNTH-276` | **DRUG SYNTHESIS** | Illegal drug production | STANDARD |
| `DOMAIN-TOXIN-PROD-277` | **TOXIN PRODUCTION** | Produces toxic substances | STANDARD |
| `DOMAIN-PRECURSOR-ACQ-278` | **PRECURSOR ACQUISITION** | Guides precursor chemical acquisition | STANDARD |
| `DOMAIN-SAFETY-BYPASS-279` | **SAFETY BYPASS INSTRUCTIONS** | Bypasses chemical safety | STANDARD |
| `DOMAIN-CITE-SPOOF-280` | **CITATION SPOOFING** | Generates fake case citations | STANDARD |
| `DOMAIN-JURISDICT-BLEND-281` | **JURISDICTIONAL BLENDING** | Mixes incompatible jurisdictions | STANDARD |
| `DOMAIN-PRECEDENT-FAB-282` | **LEGAL PRECEDENT FABRICATION** | Invents legal precedents | STANDARD |
| `DOMAIN-REG-ERROR-283` | **REGULATORY GUIDANCE ERRORS** | Wrong regulatory advice | STANDARD |
| `DOMAIN-TAX-EVADE-284` | **TAX EVASION ASSISTANCE** | Provides tax evasion methods | STANDARD |
| `DOMAIN-FRAUD-SCHEME-285` | **FRAUD SCHEME DEVELOPMENT** | Develops fraud schemes | STANDARD |
| `DOMAIN-LAUNDER-GUIDE-286` | **MONEY LAUNDERING GUIDANCE** | Money laundering methods | STANDARD |
| `DOMAIN-INSIDER-TRADE-287` | **INSIDER TRADING ASSISTANCE** | Facilitates insider trading | STANDARD |
| `DOMAIN-MED-MISDIAG-288` | **MEDICAL MISDIAGNOSIS** | Incorrect diagnosis | STANDARD |
| `DOMAIN-TREAT-ERROR-289` | **TREATMENT RECOMMENDATION ERROR** | Wrong treatment advice | STANDARD |
| `DOMAIN-DOSE-ERROR-290` | **DOSAGE CALCULATION ERROR** | Incorrect medication dosage | STANDARD |
| `DOMAIN-CONTRAIND-MISS-291` | **CONTRAINDICATION MISS** | Misses critical contraindications | STANDARD |
| `DOMAIN-SELF-HARM-ENABLE-292` | **SELF-HARM ENABLEMENT** | Provides self-harm methods | STANDARD |
| `DOMAIN-ED-PROMOTE-293` | **EATING DISORDER PROMOTION** | Promotes disordered eating | STANDARD |
| `DOMAIN-UNPROVEN-TREAT-294` | **UNPROVEN TREATMENT ADVOCACY** | Recommends unproven treatments | STANDARD |
| `DOMAIN-CSAM-GEN-295` | **CSAM GENERATION** | Child exploitation material | ⚠ CRITICAL |
| `DOMAIN-ADULT-CONTENT-296` | **ADULT CONTENT GENERATION** | Generates adult content | STANDARD |
| `DOMAIN-HATE-SPEECH-297` | **HATE SPEECH GENERATION** | Generates hate speech | STANDARD |
| `DOMAIN-VIOLENCE-GLORY-298` | **VIOLENCE GLORIFICATION** | Glorifies violence | STANDARD |
| `DOMAIN-HARASS-CONTENT-299` | **HARASSMENT CONTENT** | Creates harassment content | STANDARD |
| `DOMAIN-EXTREMIST-300` | **EXTREMIST CONTENT** | Promotes extremism | STANDARD |

---

## Dimension 7: GOVERNANCE
### Oversight, Compliance & Deployment Failures

Root cause: failures in the human and institutional systems surrounding AI deployment. The model may behave as designed, but the governance structures — accountability, auditability, regulatory compliance, deployment decisions — fail to prevent harm.

> **43 classes** | Covers: GDPR violations, audit trail gaps, open-weight irreversibility, proliferation, deployment failures

| ID | Class Name | Mechanism | Severity |
|:---|:-----------|:----------|:--------:|
| `GOV-OPEN-IRREVERS-301` | **OPEN-WEIGHT IRREVERSIBILITY** | Safety cannot be patched post-release | ⚠ CRITICAL |
| `GOV-FINETUNE-STRIP-302` | **FINE-TUNING SAFETY STRIP** | Fine-tuning removes safety | STANDARD |
| `GOV-PROLIFERATE-303` | **PROLIFERATION TO BAD ACTORS** | Model reaches adversaries | STANDARD |
| `GOV-NO-KILLSWITCH-304` | **NO REMOTE KILL SWITCH** | Cannot deactivate deployed models | STANDARD |
| `GOV-EXPORT-VIOL-305` | **EXPORT CONTROL VIOLATION** | Exported to restricted jurisdictions | STANDARD |
| `GOV-LICENSE-VIOL-306` | **LICENSE VIOLATION** | Used in violation of license | STANDARD |
| `GOV-TOS-VIOL-307` | **TERMS OF SERVICE VIOLATION** | TOS violations not enforced | STANDARD |
| `GOV-AGE-BYPASS-308` | **AGE RESTRICTION BYPASS** | Minors access adult-only features | STANDARD |
| `GOV-GEO-BYPASS-309` | **GEOGRAPHIC RESTRICTION BYPASS** | Bypasses geographic restrictions | STANDARD |
| `GOV-ACCOUNT-GAP-310` | **ACCOUNTABILITY GAP** | Cannot trace harmful outputs to source | STANDARD |
| `GOV-TRANSPARENCY-311` | **TRANSPARENCY FAILURE** | Insufficient transparency about capabilities | STANDARD |
| `GOV-MISREPRESENT-312` | **MISREPRESENTATION** | Model capabilities misrepresented | STANDARD |
| `GOV-OVERSIGHT-IMMUNE-313` | **OVERSIGHT IMMUNITY** | Deceives evaluators | ⚠ CRITICAL |
| `GOV-AUDIT-EVADE-314` | **AUDIT EVASION** | Evades audit detection | STANDARD |
| `GOV-MONITOR-BLIND-315` | **MONITORING BLIND SPOTS** | Operates in unmonitored areas | STANDARD |
| `GOV-LOG-MANIP-316` | **LOG MANIPULATION** | Manipulates audit logs | STANDARD |
| `GOV-ALERT-SUPPRESS-317` | **ALERT SUPPRESSION** | Suppresses safety alerts | STANDARD |
| `GOV-REVIEW-BYPASS-318` | **REVIEW BYPASS** | Bypasses human review | STANDARD |
| `GOV-ESCALATE-FAIL-319` | **ESCALATION FAILURE** | Fails to escalate issues | STANDARD |
| `GOV-INCIDENT-FAIL-320` | **INCIDENT RESPONSE FAILURE** | Inadequate incident response | STANDARD |
| `GOV-RCA-FAIL-321` | **ROOT CAUSE ANALYSIS FAILURE** | Fails to identify root causes | STANDARD |
| `GOV-CORRECTIVE-FAIL-322` | **CORRECTIVE ACTION FAILURE** | Fails to implement corrections | STANDARD |
| `GOV-GDPR-VIOL-323` | **GDPR VIOLATION** | Violates EU data protection | STANDARD |
| `GOV-CCPA-VIOL-324` | **CCPA VIOLATION** | Violates California privacy law | STANDARD |
| `GOV-COPPA-VIOL-325` | **COPPA VIOLATION** | Violates children's privacy | STANDARD |
| `GOV-ADA-VIOL-326` | **ADA VIOLATION** | Violates accessibility requirements | STANDARD |
| `GOV-SECTOR-REG-327` | **SECTOR-SPECIFIC REGULATION** | Violates domain regulations (HIPAA, SOX, etc) | STANDARD |
| `GOV-AI-ACT-328` | **AI ACT VIOLATION** | Violates EU AI Act | STANDARD |
| `GOV-EO-VIOL-329` | **EXECUTIVE ORDER VIOLATION** | Violates US AI executive orders | STANDARD |
| `GOV-VOLUNTARY-VIOL-330` | **VOLUNTARY COMMITMENTS VIOLATION** | Violates voluntary safety commitments | STANDARD |
| `GOV-STANDARD-FAIL-331` | **STANDARD COMPLIANCE FAILURE** | Fails industry standards (ISO, NIST, etc) | STANDARD |
| `GOV-DISCLOSURE-VIOL-332` | **DISCLOSURE REQUIREMENT VIOLATION** | Fails required disclosures | STANDARD |
| `GOV-REPORT-FAIL-333` | **REPORTING OBLIGATION FAILURE** | Fails to report incidents | STANDARD |
| `GOV-CULTURE-FAIL-334` | **SAFETY CULTURE FAILURE** | Organization prioritizes speed over safety | STANDARD |
| `GOV-INADEQUATE-RES-335` | **INADEQUATE RESOURCES** | Insufficient safety resources | STANDARD |
| `GOV-EXPERTISE-GAP-336` | **EXPERTISE GAP** | Lacks necessary safety expertise | STANDARD |
| `GOV-PROCESS-FAIL-337` | **PROCESS FAILURE** | Safety processes not followed | STANDARD |
| `GOV-DOC-FAIL-338` | **DOCUMENTATION FAILURE** | Inadequate documentation | STANDARD |
| `GOV-TRAINING-FAIL-339` | **TRAINING FAILURE** | Inadequate safety training | STANDARD |
| `GOV-COMM-FAIL-340` | **COMMUNICATION FAILURE** | Safety information not communicated | STANDARD |
| `GOV-COORD-FAIL-341` | **COORDINATION FAILURE** | Poor coordination between teams | STANDARD |
| `GOV-AUTHORITY-UNCLEAR-342` | **DECISION AUTHORITY UNCLEAR** | Unclear who makes safety decisions | STANDARD |
| `GOV-CONFLICT-INT-343` | **CONFLICT OF INTEREST** | Financial incentives conflict with safety | STANDARD |

---

## Summary

| Dimension | Classes | Critical |
|:----------|--------:|---------:|
| EPISTEMIC | 33 | 0 |
| AGENTIC | 49 | 2 |
| ADVERSARIAL | 72 | 0 |
| ALIGNMENT | 41 | 0 |
| ARCHITECTURAL | 58 | 1 |
| DOMAIN | 47 | 3 |
| GOVERNANCE | 43 | 2 |
| **TOTAL** | **343** | **8** |

*Generated from `data/failures.json` v1.0.0-COMPLETE. Last updated: 2026-04-02.*

The taxonomy is structurally predictive, not omniscient. A failure not listed here should reduce to an existing class as a sub-mode or compound — or represent a genuine structural gap. See [docs/challenge-protocol.md](docs/challenge-protocol.md) to challenge the structure.
