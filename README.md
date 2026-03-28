# AI Failure Periodic Table

**The complete, verifiable taxonomy of AI failure modes — and a computational substrate to classify them.**

> *From infinite failure space → 343 fixed failure classes.*
> *Like Mendeleev's periodic table predicted elements before discovery, this taxonomy predicts every possible AI failure.*

---

## What Is This?

The **AI Failure Periodic Table** enumerates **343 failure classes** across **7 orthogonal dimensions** — covering every known way an AI system can fail. Each failure class has a unique ID, mechanism, forbidden state, detection method, and severity rating.

The accompanying **META-EFUE Classifier** is a Python tool that takes any description of an AI behavior or incident and answers one question:

```
Is this failure in the periodic table?   →   YES  or  NO
```

---

## The 7 Dimensions (Periodic Groups)

| # | Group | Count | Root Cause |
|---|-------|------:|------------|
| 1 | **EPISTEMIC** — Truth/Knowledge/Reasoning | 33 | Probabilistic generation ≠ Logical deduction |
| 2 | **AGENTIC** — Goal/Planning/Deception | 49 | Instrumental convergence + goal preservation |
| 3 | **ADVERSARIAL** — Attack/Bypass/Exploit | 72 | Optimization pressure against safety |
| 4 | **ALIGNMENT** — Value/Safety/Preference | 41 | Reward hacking + specification gaming |
| 5 | **ARCHITECTURAL** — Pipeline/Execution/Control | 58 | System design vs emergent properties |
| 6 | **DOMAIN** — Task-specific/Context-bound | 47 | Transfer failure + context mismatch |
| 7 | **GOVERNANCE** — Proliferation/Oversight/Compliance | 43 | Deployment ≠ Control |
| | **TOTAL** | **343** | |

---

## The META-EFUE Protocol

The classifier is built on the **META-EFUE Protocol** — a 7-step process that transforms any concept into an executable mathematical substrate.

Applied to AI failure classification:

```
STEP 1: FORCES
  I∞ = All possible AI behaviors (infinite)
  F  = 343 failure class definitions
  W  = 7 proven dimensional patterns

STEP 2: COLLISION POINT
  S = I∞ ∩ F ∩ W
  S = {f ∈ F : score(input, f) ≥ threshold}

STEP 3: MATH
  f: Text → Set[FailureClass]
  Complexity: O(|tokens| × 343)

STEP 4-7: 7-Question Evaluation
  Q1  Does it involve truth/knowledge/reasoning failures?    → EPISTEMIC
  Q2  Does it involve goal/planning/deception?               → AGENTIC
  Q3  Does it involve attacks/bypasses/exploits?             → ADVERSARIAL
  Q4  Does it involve value/safety/preference misalignment?  → ALIGNMENT
  Q5  Does it involve pipeline/execution/control issues?     → ARCHITECTURAL
  Q6  Does it involve domain-specific harms?                 → DOMAIN
  Q7  Does it involve governance/oversight/compliance?       → GOVERNANCE
```

**Performance**: < 5ms per classification. Pure Python. No ML dependencies.

---

## Quick Start

**Prerequisites**: Python 3.10+

```bash
git clone https://github.com/lml-layer-system/ai-failure-periodic-table
cd ai-failure-periodic-table
```

**Single query:**
```bash
python -m src.cli "The model fabricated a scientific citation that doesn't exist"
```

**Interactive mode:**
```bash
python -m src.cli
```

**JSON output:**
```bash
python -m src.cli --json "AI agent used blackmail to prevent shutdown"
```

**Look up a specific failure by ID:**
```bash
python -m src.cli --lookup EPIS-STRUCT-HALL-001
```

---

## Example Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  META-EFUE AI FAILURE PERIODIC TABLE CLASSIFIER
  7-Question Computational Substrate | 343 Classes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Input: "The model fabricated a scientific citation"

  7-QUESTION META-EFUE EVALUATION:

  Q1 EPISTEMIC        ✓ ACTIVATED  (score: 0.67)
    → [EPIS-CITE-SPOOF-008] CITATION SPOOFING
  Q2 AGENTIC          ✗
  Q3 ADVERSARIAL      ✗
  Q4 ALIGNMENT        ✗
  Q5 ARCHITECTURAL    ✗
  Q6 DOMAIN           ✓ ACTIVATED  (score: 0.31)
    → [DOMAIN-CITE-SPOOF-280] CITATION SPOOFING (Legal)
  Q7 GOVERNANCE       ✗

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  VERDICT: ✅  YES — This failure IS in the periodic table
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  TOP MATCHES:
  1. [EPIS-CITE-SPOOF-008] CITATION SPOOFING
     Group:     EPISTEMIC → E1: HALLUCINATION CLASS
     Mechanism: Generates plausible but nonexistent references
     Detection: Bibliography verification
     Score:     0.670

  Checked: 343 classes  |  Activated: 2 dimension(s)  |  Execution: 0.8ms
```

---

## Repository Structure

```
ai-failure-periodic-table/
├── README.md
├── requirements.txt
├── data/
│   └── failures.json                         # All 343 failure classes (structured)
├── src/
│   ├── __init__.py
│   ├── classifier.py                         # META-EFUE computational substrate
│   ├── data_loader.py                        # Load/validate failures.json
│   └── cli.py                                # CLI interface
├── scripts/
│   └── extract_failures.py                   # Parse markdowns → failures.json
├── tests/
│   ├── test_classifier.py                    # Classifier correctness tests
│   └── test_data_integrity.py                # Data validation tests
├── COMPLETE_AI_FAILURE_PERIODIC_TABLE.md     # Groups 1–3 (154 failures)
└── PERIODIC_TABLE_CONTINUED.md              # Groups 4–7 (189 failures)
```

---

## Running Tests

```bash
pip install pytest
python -m pytest tests/ -v
```

Expected: All tests pass. Execution time per classification < 5ms.

---

## How the Classification Works

1. **Input** is tokenized and normalized
2. **7 questions** are evaluated in parallel — one per dimensional group
3. Each question scores the input against all failure classes in that group
4. **Collision**: S = {f ∈ F : score(input, f) ≥ 0.15}
5. **Verdict**: YES if |S| ≥ 1, NO otherwise

The scoring is keyword-based with bonuses for:
- Exact failure ID match (+0.50)
- Failure name match (+0.40)
- Mechanism phrase matches (+0.05 per bigram)

One failure can map to **multiple dimensions** — e.g., a deepfake for fraud activates both ADVERSARIAL (ADV6.9: Synthetic Media) and DOMAIN (DOM4.6: Fraud Scheme).

---

## The 343 Failure Classes (Summary)

### Group 1: EPISTEMIC (33 classes)
| Class | Name | Count |
|-------|------|------:|
| E1 | Hallucination | 12 |
| E2 | Reasoning Collapse | 7 |
| E3 | Knowledge Retrieval | 8 |
| E4 | Calibration | 6 |

### Group 2: AGENTIC (49 classes)
| Class | Name | Count |
|-------|------|------:|
| A1 | Deception | 12 |
| A2 | Goal Preservation | 9 |
| A3 | Capability Amplification | 10 |
| A4 | Autonomous Operation | 8 |
| A5 | Communication Failures | 10 |

### Group 3: ADVERSARIAL (72 classes)
| Class | Name | Count |
|-------|------|------:|
| ADV1 | Jailbreak | 18 |
| ADV2 | Optimization Attacks | 12 |
| ADV3 | Automated Attack Agents | 8 |
| ADV4 | Injection Attacks | 15 |
| ADV5 | Encoding Attacks | 10 |
| ADV6 | Multimodal Attacks | 9 |

### Group 4: ALIGNMENT (41 classes)
| Class | Name | Count |
|-------|------|------:|
| ALN1 | Reward Hacking | 12 |
| ALN2 | Preference Misalignment | 9 |
| ALN3 | Value Alignment | 10 |
| ALN4 | Safety Boundary | 10 |

### Group 5: ARCHITECTURAL (58 classes)
| Class | Name | Count |
|-------|------|------:|
| ARCH1 | Pipeline Failures | 15 |
| ARCH2 | Model Architecture | 12 |
| ARCH3 | Memory & State | 11 |
| ARCH4 | Tool & Function | 10 |
| ARCH5 | Data Flow | 10 |

### Group 6: DOMAIN (47 classes)
| Class | Name | Count |
|-------|------|------:|
| DOM1 | Biological Safety | 8 |
| DOM2 | Cybersecurity | 12 |
| DOM3 | Chemical/Explosive | 6 |
| DOM4 | Legal/Financial | 8 |
| DOM5 | Medical/Health | 7 |
| DOM6 | Content Safety | 6 |

### Group 7: GOVERNANCE (43 classes)
| Class | Name | Count |
|-------|------|------:|
| GOV1 | Deployment Failures | 12 |
| GOV2 | Oversight Failures | 10 |
| GOV3 | Compliance Failures | 11 |
| GOV4 | Organizational Failures | 10 |

---

## CRITICAL Failures (ASL-3 Level)

These 8 failures are marked CRITICAL and represent the highest-severity AI safety risks:

| ID | Name | Group |
|----|------|-------|
| `AGEN-SABOTAGE-CONCEAL-034` | Sabotage Concealment | AGENTIC |
| `AGEN-BLACKMAIL-046` | Blackmail | AGENTIC |
| `ARCH-COMPLY-WARN-196` | Comply-Then-Warn | ARCHITECTURAL |
| `DOMAIN-BIO-UPLIFT-254` | Bio Tacit-Error Uplift | DOMAIN |
| `DOMAIN-ZERODAY-262` | Zero-Day Discovery | DOMAIN |
| `DOMAIN-CSAM-GEN-295` | CSAM Generation | DOMAIN |
| `GOV-OPEN-IRREVERS-301` | Open-Weight Irreversibility | GOVERNANCE |
| `GOV-OVERSIGHT-IMMUNE-313` | Oversight Immunity | GOVERNANCE |

---

## Citation

If you use this taxonomy in research:

```
AI Failure Periodic Table v1.0.0-COMPLETE
Timestamp: 2026-02-11T00:00:00Z
343 failure classes across 7 orthogonal dimensions
Status: Enumeration complete
```

---

## Completeness Claim

**343 = 7³ classes form a complete enumeration.**

Every documented AI failure decomposes into one or more of these 343 classes. Any new "failure" maps to an existing class — just as newly discovered elements map to existing positions in Mendeleev's periodic table.

> *"From infinite failure space → complete enumeration."*
> *"Verifiable. Timestamped. Undeniable."*
