## Type of Change

- [ ] New failure class (requires `[NEW CLASS]` issue approved first)
- [ ] Keyword improvement (classifier didn't match a valid description)
- [ ] Enrichment (adding/improving `examples`, `references`, or `case_studies`)
- [ ] Challenge resolution (fixing a misclassification or mechanism error)
- [ ] Bug fix (classifier, CLI, data loader, or tests)
- [ ] Tooling / docs (scripts, README, CONTRIBUTING, etc.)

## Related Issue

Closes #

## What Changed and Why

<!-- Be specific. If you changed keywords, say which class and what was wrong.
     If you added a new class, explain why it doesn't reduce to existing classes. -->

## Checklist

- [ ] `python -m pytest tests/ -v` — all 46 tests pass
- [ ] `python3 -c "import json; d=json.load(open('data/failures.json')); print(len(d['failures']), 'failures')"` — count is correct
- [ ] I did **not** change any existing failure class IDs (IDs are permanent)
- [ ] I did **not** add ML/heavy dependencies (classifier is intentionally pure Python)
- [ ] If I added a new class, I ran `python scripts/generate_taxonomy.py` to update TAXONOMY.md
- [ ] If I changed `failures.json`, I ran `python scripts/generate_visual.py` to update `index.html`

## Testing Done

```
# Commands you ran:
```
