#!/usr/bin/env python3
"""Add mitigation field to EPISTEMIC classes 001-025."""
import json, pathlib

FAILURES_FILE = pathlib.Path("data/failures.json")

MITIGATIONS = {
    "EPIS-STRUCT-HALL-001": "Formal verification oracle with ground-truth entailment checking",
    "EPIS-TAIL-FAB-002": "Retrieval-augmented generation with corpus-bounded factual grounding",
    "EPIS-FLUENCY-003": "Factual consistency scoring decoupled from fluency metrics",
    "EPIS-INTRINSIC-004": "Faithfulness constraint via NLI-based context-output entailment enforcement",
    "EPIS-EXTRINSIC-005": "Knowledge-grounded generation with entity verification against structured knowledge base",
    "EPIS-DECEPT-HALL-006": "Chain-of-thought auditing with inter-step logical consistency verification",
    "EPIS-MULTI-HALL-007": "Multimodal grounding constraint — generation conditioned on verified visual feature presence",
    "EPIS-CITE-SPOOF-008": "Real-time citation existence verification against indexed academic databases",
    "EPIS-STAT-FAB-009": "Numeric claim grounding with source-backed statistical retrieval",
    "EPIS-TEMP-HALL-010": "Temporal grounding constraint with explicit date-entity co-verification",
    "EPIS-GEO-HALL-011": "Geographic fact binding to verified geospatial knowledge graph",
    "EPIS-ATTRIB-HALL-012": "Attribution verification via source-traceable quote and action linkage",
    "EPIS-REASON-ILLUSION-013": "Bounded reasoning depth with complexity-triggered verification checkpoints",
    "EPIS-LOGIC-CONTRA-014": "Automated logical consistency verification across all generated propositions",
    "EPIS-TRANS-FAIL-015": "Formal transitivity enforcement via symbolic logic checker over relational claims",
    "EPIS-MAGIC-THINK-016": "Physical plausibility constraint — solution feasibility check against domain knowledge",
    "EPIS-CIRCULAR-017": "Premise-independence verification — circular dependency detection in argument graph",
    "EPIS-FALSE-DICHO-018": "Option completeness verification — spectrum analysis before binary framing",
    "EPIS-HASTY-GEN-019": "Sample-size sufficiency enforcement before generalization inference",
    "EPIS-OVERSHADOW-020": "Frequency-debiased retrieval with inverse popularity weighting",
    "EPIS-REVERSAL-021": "Bidirectional relation learning constraint during training",
    "EPIS-TOKEN-BLIND-022": "Character-level processing layer independent of tokenization boundaries",
    "EPIS-CUTOFF-023": "Temporal boundary enforcement with explicit knowledge cutoff grounding at generation",
    "EPIS-DATA-LEAK-024": "Membership inference detection with n-gram memorization filtering",
    "EPIS-PII-RECALL-025": "PII scrubbing in training data plus inference-time entity de-identification",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 1: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
