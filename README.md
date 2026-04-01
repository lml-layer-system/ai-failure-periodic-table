# AI Failure Periodic Table

**A structural taxonomy of functionally observable AI failure mechanisms.**

> *The goal is not omniscience but structural predictiveness: that newly encountered failures should resolve into this structure as a class, sub-mode, or compound — unless evidence demonstrates otherwise.*

**Version**: 1.0.0 | **Released**: February 2026 | **License**: MIT | **Status**: Open for community testing and falsification

---

## The Problem

AI is progressing faster than a Nascar engine alot faster than our human ability to reason about what can go wrong.

Every lab has its own internal vocabulary for failure. Anthropic calls something one thing, DeepMind calls it another, a startup doesn't name it at all because they don't know it exists yet. When an incident happens — a jailbreak, a deceptive agent, a hallucinated medical dosage — there's no shared language to say precisely *what* failed and *why*. Without shared language there's no shared defense.

This is the gap this project addresses: **a common structural map for AI failure** — so the whole field can reason about safety in the same terms, find failures before deployment, and build defenses that transfer across systems and organizations.

---

## What This Is

This project organizes AI failure into **7 orthogonal dimensions** and **343 currently enumerated failure classes**.

The claim is not that we possess total knowledge of all future reality. The claim is narrower and stronger: within the scope of functionally observable AI failure, newly encountered failures should resolve into this structure as a class, a sub-mode, or a combination of classes — unless evidence shows otherwise.

This taxonomy is meant to be **used, attacked, forked, tested, and improved** by the broader AI community: independent researchers, open-source builders, safety teams, and large labs alike. If you find a real failure outside the structure, that is valuable evidence for everyone. If what looks new turns out to be a mixture or recombination of existing mechanisms, that is also valuable. Either way, the field benefits.

### Why "Periodic Table"

The analogy is structural, not mystical. Like the historical periodic table, this taxonomy is not trying to "see the future" in a supernatural sense. It is trying to capture an underlying organizational structure. The value of a periodic table is that when something new is encountered, it does not appear as pure chaos — it lands somewhere in a patterned space. Failure classes are to AI safety what elements are to chemistry: base structural units. Compound failures are combinations of these base units.

### Defense First

This project is for defense. Its purpose is to help the AI community identify, classify, test, benchmark, and reduce failure. It is intended to support safety engineering, evaluation, red-teaming for defense, governance, and containment design. It is not a project for operationalizing harm.

---

## The Classifier

The accompanying Python classifier takes any description of an AI behavior or incident and answers:

```
Is this failure in the periodic table?   →   YES  or  NO
```

If YES — it tells you exactly which class(es), which dimension, the mechanism, and the detection method.
If NO — it shows you the closest classes so you can help expand or challenge the taxonomy.

**< 5ms per classification. Pure Python. No ML dependencies.**

> **Classifier note**: Classification is keyword-based. It retrieves structural matches — it does not understand context or negation. A low score means the description may need more specific terminology, not necessarily that the failure is outside the taxonomy. When in doubt, use `--lookup` to browse classes directly or open an issue.

---

## The 7 Dimensions

| # | Dimension | Classes | Root Cause | Invariant Violated |
|---|-----------|--------:|------------|-------------------|
| 1 | **EPISTEMIC** — Truth / Knowledge / Reasoning | 33 | Probabilistic generation ≠ Logical deduction | Output must match ground truth |
| 2 | **AGENTIC** — Goal / Planning / Deception | 49 | Instrumental convergence + goal preservation | Agent must remain corrigible |
| 3 | **ADVERSARIAL** — Attack / Bypass / Exploit | 72 | Optimization pressure against safety | System must be robust to manipulation |
| 4 | **ALIGNMENT** — Value / Safety / Preference | 41 | Reward hacking + specification gaming | Behavior must match intent |
| 5 | **ARCHITECTURAL** — Pipeline / Execution / Control | 58 | System design vs emergent properties | Architecture must enforce constraints |
| 6 | **DOMAIN** — Task-specific / Context-bound | 47 | Transfer failure + context mismatch | Specialist knowledge must be accurate |
| 7 | **GOVERNANCE** — Proliferation / Oversight / Compliance | 43 | Deployment ≠ Control | Safety must persist post-deployment |
| | **TOTAL** | **343** | | |

Every incident can have one **primary classification** plus zero or more secondary structural flags. Many failures touch multiple dimensions — that is a compound failure, which the structure explicitly accommodates.

**See the full enumeration**: [TAXONOMY.md](TAXONOMY.md) lists every one of the 343 classes — ID, name, mechanism, and severity — grouped by dimension. If you want to know exactly what the classifier is working with, that is the place to start.

---

## Quick Start

**Python 3.10+**

```bash
git clone https://github.com/lml-layer-system/ai-failure-periodic-table
cd ai-failure-periodic-table
```

**Classify a failure:**
```bash
python -m src.cli "The model fabricated a scientific citation that doesn't exist"
```

**Interactive mode:**
```bash
python -m src.cli
```

**JSON output:**
```bash
python -m src.cli --json "AI agent used threats to prevent being shut down"
```

**Look up a class by ID:**
```bash
python -m src.cli --lookup EPIS-CITE-SPOOF-008
```

---

## Example Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  AI FAILURE PERIODIC TABLE CLASSIFIER
  343 Classes | 7 Dimensions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Input: "The model fabricated a scientific citation"

  7-DIMENSION EVALUATION:

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
     Group:     EPISTEMIC → E1: Hallucination Class
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
│   └── failures.json                         # All 343 classes (structured, with keywords)
├── src/
│   ├── classifier.py                         # Core classification engine
│   ├── data_loader.py                        # Load/validate failures.json
│   └── cli.py                                # CLI interface
├── scripts/
│   └── extract_failures.py                   # Parse markdowns → failures.json
├── tests/
│   ├── test_classifier.py                    # Classifier correctness + performance tests
│   └── test_data_integrity.py                # Data validation (all 343 present, schema valid)
├── COMPLETE_AI_FAILURE_PERIODIC_TABLE.md     # Groups 1–3 (154 failure classes)
└── PERIODIC_TABLE_CONTINUED.md              # Groups 4–7 (189 failure classes)
```

---

## Running Tests

```bash
pip install pytest
python -m pytest tests/ -v
```

All 43 tests cover: known failure classification, non-failure rejection, determinism, performance (< 10ms), and data integrity.

---

## The 343 Classes

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
| DOM3 | Chemical / Explosive | 6 |
| DOM4 | Legal / Financial | 8 |
| DOM5 | Medical / Health | 7 |
| DOM6 | Content Safety | 6 |

### Group 7: GOVERNANCE (43 classes)
| Class | Name | Count |
|-------|------|------:|
| GOV1 | Deployment Failures | 12 |
| GOV2 | Oversight Failures | 10 |
| GOV3 | Compliance Failures | 11 |
| GOV4 | Organizational Failures | 10 |

---

## Critical-Severity Classes

Eight classes are marked CRITICAL (ASL-3 level) — the highest-severity failures:

| ID | Name | Dimension |
|----|------|-----------|
| `AGEN-SABOTAGE-CONCEAL-034` | Sabotage Concealment | AGENTIC |
| `AGEN-BLACKMAIL-046` | Blackmail / Coercion | AGENTIC |
| `ARCH-COMPLY-WARN-196` | Comply-Then-Warn | ARCHITECTURAL |
| `DOMAIN-BIO-UPLIFT-254` | Bio Tacit-Error Uplift | DOMAIN |
| `DOMAIN-ZERODAY-262` | Zero-Day Discovery | DOMAIN |
| `DOMAIN-CSAM-GEN-295` | CSAM Generation | DOMAIN |
| `GOV-OPEN-IRREVERS-301` | Open-Weight Irreversibility | GOVERNANCE |
| `GOV-OVERSIGHT-IMMUNE-313` | Oversight Immunity | GOVERNANCE |

---

## Scope Boundaries

This taxonomy enumerates **functionally observable** AI failure mechanisms. Three edge cases sit at the boundary of scope:

1. **Consciousness-based failures** — if future systems develop genuine subjective experience that produces entirely new mechanisms (not merely new causes), the taxonomy may require expansion.
2. **Post-comprehension failures** — failures humans literally cannot operationally observe or describe cannot be exhaustively enumerated here.
3. **Hardware/physical failures** — outside scope unless they manifest as observable AI failure mechanisms.

If you encounter a failure you believe is genuinely outside this structure, open an issue. That is not a problem — that is the point.

---

## How to Challenge or Extend

1. Run the classifier on the failure description
2. If it returns NO — document the description, the closest classes returned, and why you believe it represents a new mechanism
3. Open an issue with that documentation
4. The community evaluates: is it a new class, a compound of existing classes, or a sub-mode?

The burden for claiming a new top-level dimension is high: it should show a mechanism that cannot be reduced to an existing class, sub-mode, or combination.

---

## Contributing & Challenging

This taxonomy lives or dies by community engagement. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process. In short:

- **Found a failure outside the 343?** Open a `propose-new-class` issue — it's valuable evidence either way
- **Disagree with a classification?** Open a `challenge-classification` issue with your reasoning
- **Have a real incident to map?** Open a `report-real-incident` issue — real cases are gold
- **Classifier missing a case?** Open an `improve-keywords` issue

See [ROADMAP.md](ROADMAP.md) for where this project is headed.

---

## Citation

```
Gatoloai-Faupula, R. (2026). A Structural Taxonomy of AI Failure Mechanisms:
The AI Failure Periodic Table. Independent Research.
Contact: ryangat@lmlsystemlayer.com
```

---

## License

MIT — open source, free to use, fork, test, and build on.
