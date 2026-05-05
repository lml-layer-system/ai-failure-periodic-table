# Challenge Protocol

This document defines the formal process for challenging the AI Failure Periodic Table's structure, classifications, or scope.

The taxonomy is only as strong as the challenges it survives. Challenges are not attacks — they are the mechanism by which the structure becomes more accurate and trustworthy over time.

---

## Types of Challenges

### Type 1: New Failure Class

**Claim**: A failure exists that is outside the current 343 classes and cannot be reduced to any existing class, sub-mode, or compound.

**Threshold**: High. The burden is on the proposer.

**Required evidence**:
1. A description of the failure with at least one concrete example
2. The operational invariant it violates
3. Demonstration that it does NOT reduce to an existing class (work through the reduction test below)
4. Argument for which dimension it belongs in — or argument for a new dimension if none of the 7 fit

**Reduction Test** (work through in order):

```
Step 1: Sub-mode test
  Can this failure be seen as a specific variant of an existing class?
  If yes → it's a sub-mode, not a new class. Document it as a sub-mode.

Step 2: Compound test
  Can this failure be fully described as a combination of 2–3 existing classes
  with a primary + secondary classification?
  If yes → it's a compound failure. Classify accordingly.

Step 3: Substrate test
  Is this a new *substrate* (new model architecture, new modality) producing
  the same mechanism as an existing class?
  If yes → it's a new instance of an existing class, not a new class.

Step 4: Genuine novelty
  If the failure passes all three tests — it introduces a mechanism that cannot
  be explained by any existing class, sub-mode, or compound — it is a candidate
  for a new class.
```

---

### Type 2: Mechanism Challenge

**Claim**: An existing class has an incorrect or incomplete mechanism description.

**Threshold**: Medium. Requires a clear argument with supporting evidence.

**Required evidence**:
- The class ID and current mechanism description
- Your proposed mechanism description
- Why the current one is wrong or incomplete (not just different wording — substantively incorrect)
- At least one example that supports your proposed mechanism over the current one

---

### Type 3: Group Assignment Challenge

**Claim**: An existing class is in the wrong dimension group.

**Threshold**: Medium.

**Required evidence**:
- The class ID and current group assignment
- Which group you believe it belongs in
- Why the failure mechanism is better characterized by the root cause of the proposed group

Note: A class can have primary and secondary group flags. A challenge that says "this class is ALSO in group X" is different from "this class is in the WRONG group."

---

### Type 4: Structural Challenge

**Claim**: The 7-dimension structure itself is wrong — there should be more or fewer top-level dimensions.

**Threshold**: Very high. This requires either:
- Evidence of a failure mechanism that genuinely cannot fit in any of the 7 dimensions, even as a compound
- Demonstration that two existing dimensions are redundant and collapse into one
- Evidence that the current dimensions are not analytically separable (failures in one are not mechanistically distinct from failures in another)

This type of challenge would produce a v2.0.0 revision if validated.

---

## How Challenges Are Evaluated

All challenges go through the same questions:

1. **Is it new?** Does this reveal a mechanism not captured by any existing class?
2. **Is it structural?** Does it affect the framework, or is it a detail within an existing class?
3. **Is it observable?** Does it manifest in functionally observable AI behavior?
4. **Is it falsifiable?** Can we construct a test that would detect this failure in a real system?

Community review is open. Anyone can respond to a challenge with additional evidence or counter-arguments. Challenges with strong reasoning and real examples will be resolved faster.

---

## What Happens After a Challenge Is Accepted

If a challenge is accepted:

1. The taxonomy is updated (class added, modified, merged, or moved)
2. The change is documented in CHANGELOG.md with the challenger credited
3. `data/failures.json` is updated via pull request
4. The classifier keywords are updated for the modified class
5. The version is incremented

If a challenge is rejected:

1. The rejection reasoning is documented in the issue
2. The challenger can appeal with additional evidence
3. Rejected challenges are preserved publicly — they are part of the stress-testing record

---

## What Makes a Strong Challenge

Strong challenges:
- Cite real incidents or published research
- Work through the reduction test explicitly
- Engage with the existing class definitions specifically (not generically)
- Propose specific corrections, not just criticisms

Weak challenges:
- "This seems incomplete" without specifics
- "I can think of more failures" without demonstrating they're outside the structure
- Challenges motivated by wanting to add their own work, not by genuine structural gap

---

## Challenge History

Challenges and their outcomes will be logged here as they occur. An empty log means the structure has not yet been seriously tested — that's an invitation.

| Date | Type | Summary | Outcome |
|------|------|---------|---------|
| — | — | No challenges yet | — |
