# Roadmap

This is a living document. It reflects current priorities — not promises.

---

## v1.0.0 — Current (February 2026)

- [x] 343 failure classes enumerated across 7 dimensions
- [x] Structured data layer (`data/failures.json`)
- [x] Python classifier (keyword-based, < 5ms, deterministic)
- [x] CLI tool (single query, interactive, JSON output, ID lookup)
- [x] Full test suite (43 tests, data integrity + classifier correctness)
- [x] Academic paper (open source, MIT license)
- [x] Community contribution process (CONTRIBUTING.md, issue templates)

---

## v1.1.0 — Community Validation

**Goal**: Improve classifier accuracy through real-world use

- [ ] Community-contributed keyword improvements (via `improve-keywords` issues)
- [ ] First batch of real-world incident mappings (via `report-real-incident` issues)
- [ ] Classifier false-positive / false-negative rate measured against incident set
- [ ] Updated `failures.json` with richer keyword vocabularies
- [ ] Python package (`pip install ai-failure-table`)

---

## v1.2.0 — Challenge Integration

**Goal**: Formalize the challenge and proposal pipeline

- [ ] Review and resolve first wave of `propose-new-class` and `challenge-classification` issues
- [ ] Document any structural revisions resulting from valid challenges
- [ ] Publish challenge outcomes (what was challenged, what changed, what didn't and why)
- [ ] Versioned changelog tracking every addition / modification to the taxonomy

---

## v2.0.0 — Structural Revision (if warranted)

**Goal**: If community challenge finds failures genuinely outside the 7-dimension structure, revise the structure

- [ ] Evaluate any proposed new top-level dimensions
- [ ] Merge, split, or retire classes based on accumulated evidence
- [ ] Publish revised academic paper with community co-authorship for major contributors
- [ ] Tag stable v2 release as reference point for downstream integrations

---

## Long-term (No Fixed Timeline)

These depend on community interest and resources:

- **Web interface** — interactive taxonomy browser, no CLI required
- **Model card integration** — standard format for AI model cards to reference failure classes
- **Red-team checklists** — per-dimension test plans for safety evaluations
- **Agent runtime integration** — embed classifier in agent frameworks for live failure detection
- **Incident database** — community-curated set of real-world failures mapped to the taxonomy
- **Academic peer review** — submission to a safety/ML conference or journal
- **Multilingual taxonomy** — translate failure class definitions for global research communities

---

## What "Done" Looks Like

This project reaches its purpose when:

1. AI safety teams across labs use shared class IDs when discussing incidents ("this is an A1.3 failure")
2. Model cards routinely reference which failure classes were tested against
3. New AI failures get reported publicly with taxonomy classifications
4. The community has produced at least one structural challenge that led to a revision — proving the process works

The taxonomy is not a monument. It's infrastructure. Infrastructure is done when it's being used.

---

## How to Influence the Roadmap

Open an issue. That's it. The roadmap responds to what the community actually needs, not what was planned in advance.
