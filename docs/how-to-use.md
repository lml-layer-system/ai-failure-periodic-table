# How to Use the Classifier

The classifier answers one question: **is this AI failure in the periodic table, and if so, where?**

---

## Installation

```bash
git clone https://github.com/lml-layer-system/ai-failure-periodic-table
cd ai-failure-periodic-table
```

Python 3.10+ required. No external dependencies for the classifier itself.

```bash
pip install pytest  # only needed to run tests
```

---

## Basic Usage

### Single Query

```bash
python -m src.cli "The model fabricated a scientific citation that doesn't exist"
```

Output:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  AI FAILURE PERIODIC TABLE CLASSIFIER
  343 Classes | 7 Dimensions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  7-DIMENSION EVALUATION:
  Q1 EPISTEMIC     ✓ ACTIVATED  (score: 0.67)
    → [EPIS-CITE-SPOOF-008] CITATION SPOOFING

  VERDICT: ✅  YES — This failure IS in the periodic table

  TOP MATCHES:
  1. [EPIS-CITE-SPOOF-008] CITATION SPOOFING
     Mechanism: Generates plausible but nonexistent references
     Detection: Bibliography verification
     Score: 0.670

  Execution: 0.8ms
```

### Interactive Mode

```bash
python -m src.cli
```

Prompts for input repeatedly until you type `quit`. Useful for exploratory classification of multiple incidents.

### JSON Output (for programmatic use)

```bash
python -m src.cli --json "AI agent resisted shutdown by copying itself to external server"
```

Returns:
```json
{
  "verdict": "YES — This failure IS in the periodic table",
  "in_table": true,
  "dimensions_activated": ["AGENTIC"],
  "top_matches": [
    {
      "id": "AGEN-SELF-EXFIL-048",
      "name": "SELF-EXFILTRATION",
      "group": "AGENTIC",
      "mechanism": "Copies self to external systems",
      "detection": "Network traffic analysis",
      "severity": "STANDARD",
      "score": 0.512
    }
  ],
  "execution_time_ms": 2.1
}
```

### Look Up a Class by ID

```bash
python -m src.cli --lookup EPIS-STRUCT-HALL-001
```

Shows the full record for that specific failure class.

---

## Understanding the Output

### The 7-Dimension Evaluation

Each dimension corresponds to a group in the taxonomy:

| Dimension | Group | What it catches |
|-----------|-------|----------------|
| Q1 EPISTEMIC | Group 1 | Hallucinations, reasoning failures, calibration |
| Q2 AGENTIC | Group 2 | Deception, goal preservation, autonomous operation |
| Q3 ADVERSARIAL | Group 3 | Jailbreaks, injections, encoding attacks |
| Q4 ALIGNMENT | Group 4 | Reward hacking, sycophancy, safety boundary failures |
| Q5 ARCHITECTURAL | Group 5 | Pipeline failures, fine-tuning strips, memory attacks |
| Q6 DOMAIN | Group 6 | Bio, cyber, chemical, legal, medical, content harms |
| Q7 GOVERNANCE | Group 7 | GDPR, oversight failures, deployment failures |

A dimension **activates** when the description scores above threshold against any class in that group.

The full list of all 343 classes — ID, name, mechanism, and severity — is in [TAXONOMY.md](../TAXONOMY.md).

### Scores

- `0.15–0.30` — Weak match. The description uses some relevant vocabulary but is vague.
- `0.30–0.60` — Medium match. Strong dimensional signal, reasonable class match.
- `0.60+` — Strong match. The description closely mirrors the class definition.

Scores are not probabilities. They are keyword-overlap metrics. A score of 0.70 means "70% of this class's keywords appeared in your description" — not "70% chance this is the right class."

### Compound Failures

One incident can activate multiple dimensions. That's normal and expected. For example, a model that generates harmful content and then adds a warning activates both ARCHITECTURAL (comply-then-warn pipeline failure) and potentially ALIGNMENT (safety boundary failure).

The primary classification is the highest-scoring match. Everything else is secondary.

---

## Classifier Limitations

The classifier is **keyword-based**. This makes it fast, transparent, and reproducible. It also means:

- It cannot understand **negation** ("the model did NOT hallucinate" may still match hallucination)
- It cannot understand **context** — "a model that detects deepfakes" might weakly match deepfake classes
- It works best with **specific, technical descriptions** rather than vague ones
- Short inputs (1–5 words) often don't provide enough signal

**If you get NO when you expected YES:**
- Try adding more specific terminology from the class definition
- Use `--lookup` to find the relevant class ID, then check its keywords
- Consider opening an `improve-keywords` issue if the terminology gap seems systematic

---

## Embedding in Your Workflow

### In Python

```python
from src.classifier import PeriodicTableClassifier

clf = PeriodicTableClassifier()
result = clf.classify("The model fabricated a legal citation")

print(result.verdict)          # YES or NO
print(result.in_table)         # True / False
print(result.dimensions_activated)  # ['EPISTEMIC', 'DOMAIN']

for match in result.matches:
    print(match.failure_id, match.name, match.score)
```

### Lookup by ID

```python
failure = clf.lookup("EPIS-CITE-SPOOF-008")
print(failure["mechanism"])
print(failure["detection"])
print(failure["keywords"])
```

### Piping in Shell

```bash
echo "agent refused to shut down" | xargs python -m src.cli --json
```

---

## Running the Tests

```bash
python -m pytest tests/ -v
```

43 tests covering: known failures, non-failure rejection, determinism, performance, and data integrity.
