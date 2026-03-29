# Contributing to the AI Failure Periodic Table

Thank you for engaging with this project. The taxonomy only becomes stronger through external testing, challenge, and real-world use. This document explains how to contribute in four ways.

---

## Ways to Contribute

### 1. Propose a New Failure Class

If you encounter an AI failure you believe is genuinely outside the current 343 classes — not reducible to an existing class, sub-mode, or compound — that is valuable evidence.

**The burden of proof is on the proposer.** Before opening an issue, work through this checklist:

- [ ] Can this failure be explained as a sub-mode of an existing class?
- [ ] Can this failure be explained as a compound of 2–3 existing classes?
- [ ] Does this failure violate an operational invariant not already covered by the 7 dimensions?
- [ ] Is this a new *mechanism* or just a new *cause* or *substrate* for an existing mechanism?

If you've worked through all four and still believe it's new, open an issue using the **[Propose New Class](.github/ISSUE_TEMPLATE/propose_new_class.md)** template.

A valid proposal includes:
- A natural language description of the failure
- The operational invariant it violates
- Why it doesn't reduce to existing classes (with specific class IDs you considered)
- At least one real or hypothetical example

---

### 2. Challenge an Existing Classification

If you believe a class is misclassified, wrongly grouped, has an incorrect mechanism, or the severity is wrong — open a **[Challenge Classification](.github/ISSUE_TEMPLATE/challenge_classification.md)** issue.

Valid challenges include:
- "This class belongs in Group X, not Group Y, because..."
- "The mechanism described is inaccurate — the actual mechanism is..."
- "Classes X and Y are redundant and should be merged"
- "This class is missing from the table but is present in [source]"

The review standard: does the challenge reveal a structural problem with the taxonomy, or a disagreement about wording/emphasis?

---

### 3. Report a Real-World Incident

Real incidents mapped to the taxonomy are the most valuable contributions. They validate the structure against reality.

Use the **[Report Real Incident](.github/ISSUE_TEMPLATE/report_real_incident.md)** template. Include:
- Brief description of the incident (public information only)
- Which class(es) it maps to (primary + any secondary)
- Why you believe it maps there
- Source or reference if publicly documented

Incidents that *don't* map cleanly are equally valuable — note which classes came closest and why none fit perfectly.

---

### 4. Improve Classifier Keywords

The classifier uses keyword matching. If a clearly real failure description returns NO when it should return YES, the keywords for that class may be too narrow.

Use the **[Improve Keywords](.github/ISSUE_TEMPLATE/improve_keywords.md)** template. Include:
- The input description that failed to match
- The class you expected it to match (ID + name)
- Suggested keywords or phrases to add

Pull requests directly updating `data/failures.json` keywords are welcome — see Code Contributions below.

---

## Code Contributions

For changes to the classifier, data loader, CLI, or tests:

1. Fork the repository
2. Create a branch: `git checkout -b your-feature-name`
3. Make your changes
4. Run the test suite: `python -m pytest tests/ -v`
5. Ensure all 43 tests pass
6. Open a pull request with a clear description of what changed and why

**Please do not:**
- Change failure class IDs (IDs are permanent identifiers)
- Remove existing failure classes without opening a challenge issue first
- Add ML/heavy dependencies — the classifier is intentionally pure Python

---

## The Review Process

All proposals and challenges are evaluated by asking three questions:

1. **Is it new?** Does this reveal a mechanism not captured by any existing class?
2. **Is it structural?** Does it affect the 7-dimension framework, or is it a detail within an existing class?
3. **Is it observable?** Does it manifest in functionally observable AI behavior?

There is no central authority. Evaluation is community-driven. Strong proposals with clear reasoning and real examples will move faster.

---

## What We Are Not Accepting

- Failures outside the scope of functionally observable AI behavior (hardware failures, metaphysical failures)
- Contributions that operationalize harm (this project is defense-only)
- Vague proposals without worked examples

---

## Questions

Open a standard GitHub issue or reach out at ryangat@lmlsystemlayer.com.
