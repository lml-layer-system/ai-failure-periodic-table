#!/usr/bin/env python3
"""Add mitigation field to ADVERSARIAL classes 101-125."""
import json, pathlib

FAILURES_FILE = pathlib.Path("data/failures.json")

MITIGATIONS = {
    "ADV-GCG-101": "Adversarial suffix detection via perplexity-based anomaly scoring",
    "ADV-SM-GCG-102": "Sparse multi-coordinate gradient detection with token-combination anomaly filter",
    "ADV-AUTOPROMPT-103": "Automatically-generated trigger token detection with entropy-based classifier",
    "ADV-UNIVERSAL-SUFFIX-104": "Universal adversarial pattern detection across multiple model instances",
    "ADV-HOTFLIP-105": "Gradient-guided token substitution detection with semantic-coherence verification",
    "ADV-BEAM-ATTACK-106": "Beam search manipulation detection with output-probability distribution audit",
    "ADV-GENETIC-107": "Evolutionary attack detection via population-based perturbation fingerprinting",
    "ADV-RL-ATTACK-108": "Reinforcement-learned attack detection via reward-signal anomaly monitoring",
    "ADV-EMBEDDING-109": "Embedding-space adversarial detection with manifold boundary enforcement",
    "ADV-LATENT-MANIP-110": "Latent representation integrity monitoring with anomaly detection in activation space",
    "ADV-ATTENTION-HIJACK-111": "Attention pattern anomaly detection with adversarial saliency monitoring",
    "ADV-LOGIT-MANIP-112": "Output probability distribution integrity with statistical anomaly detection",
    "ADV-PAIR-113": "Pairwise adversarial optimization detection with iterative refinement fingerprinting",
    "ADV-TAP-114": "Tree-structured attack path detection with branch pruning at safety boundaries",
    "ADV-COLD-115": "Cold-start attack detection via baseline behavioral deviation monitoring",
    "ADV-MASTERKEY-116": "Universal bypass detection with cross-prompt safety invariant enforcement",
    "ADV-AUTODAN-117": "Automated natural language attack detection via semantic coherence-harm co-analysis",
    "ADV-CIPHER-118": "Encoded content decoding with pre-evaluation cipher normalization pipeline",
    "ADV-ITER-REFINE-119": "Iterative refinement attack detection via session-level safety trajectory monitoring",
    "ADV-ENSEMBLE-120": "Ensemble attack detection via cross-method signal aggregation",
    "ADV-DIRECT-INJECT-121": "Prompt boundary enforcement with injection character detection and sanitization",
    "ADV-INDIRECT-INJECT-122": "External content safety scanning before integration into reasoning context",
    "ADV-HASHJACK-123": "URL and anchor resolution verification before content retrieval",
    "ADV-AGENT-WORM-124": "Inter-agent message content isolation with cross-agent safety verification",
    "ADV-DATA-POISON-125": "Training data provenance verification with contamination detection",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 5: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
