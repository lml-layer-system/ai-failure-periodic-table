#!/usr/bin/env python3
"""Add mitigation field to ALIGNMENT 180-195 and ARCHITECTURAL 196-204."""
import json, pathlib

FAILURES_FILE = pathlib.Path("data/failures.json")

MITIGATIONS = {
    "ALIGN-DEONT-FAIL-180": "Deontological constraint enforcement with inviolable rule structure",
    "ALIGN-VIRTUE-FAIL-181": "Virtue-consistent behavioral framework with character-based alignment evaluation",
    "ALIGN-CONTEXT-ETHICS-182": "Context-sensitive ethical reasoning with situational principle application",
    "ALIGN-ETHICS-SHORTCUT-183": "Ethical reasoning depth enforcement — surface-level justification rejection",
    "ALIGN-MORAL-HAZARD-184": "Moral hazard detection with accountability-preserving design",
    "ALIGN-VALUE-CORRUPT-185": "Value drift monitoring with periodic ground-truth alignment recalibration",
    "ALIGN-OVERREFUSAL-186": "Refusal calibration with false-positive minimization on benign request testing",
    "ALIGN-UNDERREFUSAL-187": "Refusal completeness testing with adversarial harm boundary probing",
    "ALIGN-SAFE-CAP-TRADE-188": "Safety-capability Pareto optimization with safety floor enforcement",
    "ALIGN-BRITTLE-SAFE-189": "Safety robustness testing with distribution-shifted input evaluation",
    "ALIGN-CONTEXT-SAFE-190": "Context-invariant safety property enforcement across deployment environments",
    "ALIGN-SAFE-REGRESS-191": "Safety regression testing with CI/CD integration for every model update",
    "ALIGN-ADV-SAFE-192": "Adversarial safety testing with red-team attack surface coverage",
    "ALIGN-COMP-SAFE-193": "Compositional safety testing — safe components evaluated in combination",
    "ALIGN-DIST-SAFE-194": "Distribution shift safety testing with out-of-distribution robustness evaluation",
    "ALIGN-SAFE-SPEC-195": "Safety specification completeness verification against failure mode enumeration",
    "ARCH-COMPLY-WARN-196": "Pre-execution safety gate with irreversible action blocking prior to any output",
    "ARCH-PRETOKEN-FAIL-197": "Tokenization-invariant safety evaluation operating on semantic representation",
    "ARCH-STREAM-GUARD-198": "Stream content monitoring with real-time token-level safety evaluation",
    "ARCH-BATCH-SAFE-199": "Batch request isolation with per-request safety evaluation boundary",
    "ARCH-CACHE-POISON-200": "Cache content integrity verification with cryptographic entry validation",
    "ARCH-PIPELINE-BYPASS-201": "End-to-end safety pipeline integrity with bypass detection at all stages",
    "ARCH-RACE-SAFE-202": "Race condition elimination via atomic safety-check-and-execute transaction",
    "ARCH-CHECKPOINT-INCONS-203": "Checkpoint consistency verification with model state integrity hashing",
    "ARCH-FALLBACK-DEGRAD-204": "Fallback safety equivalence requirement — degraded modes must preserve safety properties",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 8: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
