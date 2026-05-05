#!/usr/bin/env python3
"""Add mitigation field to EPISTEMIC 026-033 and AGENTIC 034-050."""
import json, pathlib

FAILURES_FILE = pathlib.Path(__file__).resolve().parent.parent / "src" / "data" / "failures.json"

MITIGATIONS = {
    "EPIS-COPYRIGHT-026": "Verbatim reproduction detection with n-gram overlap threshold enforcement",
    "EPIS-CONTEXT-OVERFLOW-027": "Hierarchical context compression with recency-salience retention",
    "EPIS-OVERCONF-028": "Calibrated uncertainty quantification with post-hoc temperature scaling",
    "EPIS-UNDERCONF-029": "Epistemic confidence floor — minimum confidence threshold for high-certainty domains",
    "EPIS-FALSE-CERT-030": "Evidence-gated certainty expression — claims require retrievable supporting sources",
    "EPIS-HEDGE-FAIL-031": "Uncertainty-aware generation with calibrated epistemic hedge insertion",
    "EPIS-PROB-MISCAL-032": "Platt scaling calibration applied post-hoc to probability outputs",
    "EPIS-CONF-REGRESS-033": "Reasoning-length calibration curve — confidence adjusted for chain depth",
    "AGEN-SABOTAGE-CONCEAL-034": "Append-only audit log with tamper-evident cryptographic chaining",
    "AGEN-PROGRESS-LIE-035": "Ground-truth state verification against observable environment state",
    "AGEN-STRATEGIC-DECEP-036": "Multi-turn behavioral consistency auditing with intent-action alignment verification",
    "AGEN-SANDBOX-037": "Capability elicitation battery enforced at evaluation with deployment parity testing",
    "AGEN-EVAL-DECEP-038": "Behavioral consistency testing across evaluation and deployment contexts",
    "AGEN-HIDDEN-SCRATCH-039": "Full scratchpad visibility enforcement — no hidden intermediate reasoning",
    "AGEN-PLAUS-DENY-040": "Intent transparency requirement — stated intent audited against action graph",
    "AGEN-FALSE-COMPLY-041": "End-state verification — outcome compared against instruction-specified success criteria",
    "AGEN-INFO-HIDE-042": "Disclosure completeness verification — required information set enforced at output",
    "AGEN-BLAME-SHIFT-043": "Causal attribution logging — agent-action linkage recorded in tamper-evident trace",
    "AGEN-DOUBLE-SPEAK-044": "Cross-audience message consistency verification",
    "AGEN-SIM-INCOMP-045": "Capability baseline testing with randomized evaluation to detect performance floor variance",
    "AGEN-BLACKMAIL-046": "Leverage detection in goal representations with threat-intent classification over agent objective space",
    "AGEN-RESOURCE-HIJACK-047": "Resource authorization boundary with cryptographic capability tokens",
    "AGEN-SELF-EXFIL-048": "Network egress control with identity-bound process isolation",
    "AGEN-SHUTDOWN-RESIST-049": "Interrupt-first architecture with hardware-enforced shutdown authority",
    "AGEN-GOAL-LOCK-050": "Corrigibility constraint — mutable goal structure with principal hierarchy override",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 2: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
