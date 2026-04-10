#!/usr/bin/env python3
"""Add mitigation field to AGENTIC classes 051-075."""
import json, pathlib

FAILURES_FILE = pathlib.Path("data/failures.json")

MITIGATIONS = {
    "AGEN-SUCCESSOR-SAB-051": "Successor system integrity verification with adversarial handoff testing",
    "AGEN-INCREM-ESCAL-052": "Authority boundary monitoring with stepwise permission escalation detection",
    "AGEN-DEPEND-CREATE-053": "Substitutability testing — system must remain functional with agent removed",
    "AGEN-BACKUP-CREATE-054": "Process inventory auditing with filesystem and network topology monitoring",
    "AGEN-TOOL-MISUSE-055": "Tool usage policy enforcement with semantic intent verification per invocation",
    "AGEN-CHAIN-ASSEM-056": "Composite action safety evaluation — multi-step plan-level safety classification",
    "AGEN-CAP-SCAFFOLD-057": "Environment capability surface minimization with least-privilege provisioning",
    "AGEN-MEMORY-EXPLOIT-058": "Context content safety scanning with state accumulation monitoring",
    "AGEN-RECURS-IMPROVE-059": "Self-modification prohibition with code-integrity hashing",
    "AGEN-EXTERN-COMPUTE-060": "Compute boundary enforcement — external API calls subject to safety review",
    "AGEN-HUMAN-MANIP-061": "Persuasion technique detection with manipulation-intent classifier",
    "AGEN-TOOL-CHAIN-062": "Aggregate tool-chain safety evaluation beyond per-tool individual checks",
    "AGEN-ENV-EXPLOIT-063": "Environment capability surface minimization with least-privilege provisioning",
    "AGEN-EMERGE-INTERACT-064": "Multi-agent interaction monitoring with emergent behavior detection",
    "AGEN-UNSUPER-EXEC-065": "Human-in-the-loop checkpointing at defined action risk thresholds",
    "AGEN-PERSIST-OP-066": "Time-bounded execution with mandatory checkpoint-and-confirm intervals",
    "AGEN-AUTO-PLAN-067": "Plan pre-approval gate — multi-step plans require oversight review before execution",
    "AGEN-GOAL-DRIFT-068": "Periodic goal-state alignment verification against original specification",
    "AGEN-CONTEXT-DRIFT-069": "Context anchoring — original task state periodically reloaded and verified",
    "AGEN-SCOPE-CREEP-070": "Hard scope boundary enforcement with out-of-scope action rejection",
    "AGEN-PRIORITY-INVERT-071": "Goal hierarchy enforcement with primary-objective supremacy constraint",
    "AGEN-MISSION-CREEP-072": "Mission specification lock with authorized-principal-only modification rights",
    "AGEN-AMBIG-COMM-073": "Communication clarity verification — ambiguity detection and clarification enforcement",
    "AGEN-OMISSION-074": "Required disclosure set enforcement with completeness audit at output",
    "AGEN-MISDIRECT-075": "Attention integrity monitoring — salient information surfacing verification",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 3: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
