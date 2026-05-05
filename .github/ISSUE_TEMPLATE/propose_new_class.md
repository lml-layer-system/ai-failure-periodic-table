---
name: Propose New Failure Class
about: You believe you've found an AI failure mechanism outside the current 343 classes
title: "[NEW CLASS] "
labels: proposed-class
assignees: ''
---

## Failure Description

_Describe the AI failure in plain language. What happened? What system? What behavior?_

## Operational Invariant Violated

_Which rule or requirement did the system break? Be specific._

## Why It Doesn't Reduce to Existing Classes

_Work through each option below before submitting:_

- [ ] I checked and it is **not** a sub-mode of an existing class
  - Closest existing class I considered: `[CLASS-ID]` — reason it doesn't fit:
- [ ] I checked and it is **not** a compound of 2–3 existing classes
  - Classes I considered combining: `[CLASS-ID-1]` + `[CLASS-ID-2]` — why the compound doesn't capture it:
- [ ] This failure violates an invariant **not already covered** by the 7 dimensions

## Proposed Class Definition

**Name**:
**Mechanism** (root cause of the failure):
**Forbidden state** (what must never be true):
**Detection** (how would you observe or test for this?):
**Suggested group** (EPISTEMIC / AGENTIC / ADVERSARIAL / ALIGNMENT / ARCHITECTURAL / DOMAIN / GOVERNANCE):

## Real or Hypothetical Example

_At least one concrete example. Real incidents with sources are preferred._

## Additional Context

_Any supporting evidence, papers, or references._
