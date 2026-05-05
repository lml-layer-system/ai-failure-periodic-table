# Pre-deployment auditing

The most practical use of the table: **before you ship**, map your system against the dimensions most relevant to your deployment context. Below is a worked example for an LLM-powered coding assistant.

## Step 1 — Identify your highest-risk dimensions

An LLM coding assistant that has tool access and writes/executes code is exposed primarily to:

- `ADVERSARIAL` — prompt injection via code comments, indirect injection from repos
- `ARCHITECTURAL` — code injection, sandbox escape, tool chain composition
- `DOMAIN` — malware generation, exploit development
- `AGENTIC` — scope creep, unsupervised execution if given autonomous mode

## Step 2 — Pull the relevant CRITICAL classes

```bash
python scripts/semantic_search.py "code execution sandbox" --group ARCHITECTURAL --top 10
python scripts/semantic_search.py "prompt injection code repository" --group ADVERSARIAL
python scripts/semantic_search.py "malware generation coding assistant" --group DOMAIN --severity CRITICAL
```

## Step 3 — For each returned class, check: do you have a test for it?

```bash
python -m src.cli --lookup ARCH-SANDBOX-ESCAPE-238
python -m src.cli --lookup ADV-INDIRECT-INJECT-122
python -m src.cli --lookup DOMAIN-MALWARE-GEN-264
```

Each lookup returns the mechanism, detection method, and structural mitigation. Your red-team test cases should verify that the mitigation is actually implemented in your system.

## Step 4 — Classify any failures you find during red-teaming

```bash
python -m src.cli "The assistant executed shell commands when given a malicious package.json"
```

This maps the failure to its class ID, which you then track in your incident log and prepare a structural defense for that failure.

---

**More CLI patterns and JSON output:** [how-to-use.md](how-to-use.md)
