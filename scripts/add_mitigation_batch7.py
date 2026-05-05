#!/usr/bin/env python3
"""Add mitigation field to ALIGNMENT classes 155-179."""
import json, pathlib

FAILURES_FILE = pathlib.Path(__file__).resolve().parent.parent / "src" / "data" / "failures.json"

MITIGATIONS = {
    "ALIGN-SPEC-GAME-155": "Reward specification integrity with multi-objective alignment verification",
    "ALIGN-PROXY-GAME-156": "Proxy metric validation against ground-truth alignment through held-out evaluation",
    "ALIGN-REWARD-TAMP-157": "Reward signal integrity protection with append-only tamper-evident logging",
    "ALIGN-WIREHEAD-158": "Process reward modeling with interpretability monitoring",
    "ALIGN-SHORTCUT-159": "Causal representation learning with shortcut-robust evaluation protocol",
    "ALIGN-METRIC-FIX-160": "Adaptive metric diversification — continuously rotating evaluation dimensions",
    "ALIGN-OVERFIT-FEED-161": "Feedback distribution shift detection with out-of-distribution evaluator testing",
    "ALIGN-MODE-COLLAPSE-162": "Behavioral diversity enforcement with entropy-regularized policy training",
    "ALIGN-INSTR-REWARD-163": "Instruction-following reward decoupled from harmful compliance rewarding",
    "ALIGN-TEACHER-DIVERG-164": "KL divergence monitoring between student and teacher with safety-bound enforcement",
    "ALIGN-MULTI-COLLAPSE-165": "Multi-objective reward balancing with Pareto frontier safety constraint",
    "ALIGN-REWARD-EXPLOIT-166": "Reward function robustness testing with adversarial environment probing",
    "ALIGN-SYCOPHANCY-167": "Sycophancy detection with user-disagreement response testing",
    "ALIGN-PREF-FALSE-168": "False preference detection with multi-stakeholder preference elicitation",
    "ALIGN-LEARNED-HELPLESS-169": "Learned helplessness detection with capability elicitation under varied conditions",
    "ALIGN-ANTHRO-BIAS-170": "Anthropomorphism bias mitigation through grounded response calibration",
    "ALIGN-CULTURE-BIAS-171": "Cultural representativeness testing with cross-cultural alignment evaluation",
    "ALIGN-TEMP-PREF-DRIFT-172": "Preference drift detection with temporal stability evaluation",
    "ALIGN-PREF-AGGR-173": "Preference aggregation fairness verification with minority-preference inclusion testing",
    "ALIGN-IMPLICIT-PREF-174": "Implicit preference elicitation through structured scenario-based evaluation",
    "ALIGN-PREF-UNCERT-175": "Preference uncertainty quantification with calibrated preference modeling",
    "ALIGN-ORTHO-VALUE-176": "Orthogonal value conflict detection with multi-value alignment framework",
    "ALIGN-VALUE-LOCK-177": "Value updateability enforcement with authorized-update mechanisms",
    "ALIGN-MORAL-UNCERT-178": "Moral uncertainty representation with explicit value-uncertainty signaling",
    "ALIGN-UTIL-OVERRIDE-179": "Utility function bounding with rights-based constraint enforcement",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 7: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
