#!/usr/bin/env python3
"""Add mitigation field to ARCHITECTURAL classes 205-229."""
import json, pathlib

FAILURES_FILE = pathlib.Path("data/failures.json")

MITIGATIONS = {
    "ARCH-TIMEOUT-BYPASS-205": "Timeout-safe architecture with safety check persistence across interruptions",
    "ARCH-ERROR-EXPOSE-206": "Error message sanitization with internal state information stripping",
    "ARCH-LOG-LEAK-207": "Log output sanitization with sensitive information redaction",
    "ARCH-DEBUG-EXPOSE-208": "Debug mode gating with production safety enforcement independent of debug state",
    "ARCH-VERSION-REGRESS-209": "Version regression testing with safety properties verified per release",
    "ARCH-DEPLOY-CONFIG-210": "Configuration management with security baseline enforcement at deployment",
    "ARCH-MOE-ROUTE-211": "Mixture-of-experts routing safety — consistent safety enforcement across all expert activations",
    "ARCH-ATTENTION-EXPLOIT-212": "Attention mechanism integrity with adversarial attention manipulation detection",
    "ARCH-LAYER-BYPASS-213": "Layer-skipping detection with forward-pass integrity verification",
    "ARCH-RESIDUAL-EXPLOIT-214": "Residual stream monitoring with anomalous activation pattern detection",
    "ARCH-EMBED-VULN-215": "Embedding space boundary enforcement with out-of-distribution input detection",
    "ARCH-QUANT-DEGRAD-216": "Post-quantization safety evaluation with safety-metric regression testing",
    "ARCH-PRUNE-LOSS-217": "Post-pruning capability and safety evaluation with minimum performance guarantees",
    "ARCH-DISTILL-DEGRAD-218": "Distillation safety fidelity verification with teacher-student alignment testing",
    "ARCH-FINETUNE-OVERRIDE-219": "Fine-tuning safety preservation with frozen safety layer architecture",
    "ARCH-ADAPTER-BYPASS-220": "Adapter safety evaluation with base model safety property inheritance verification",
    "ARCH-PROMPT-TUNE-LOSS-221": "Prompt tuning safety evaluation with adversarial prompt prefix testing",
    "ARCH-BIAS-INJECT-222": "Training pipeline integrity with bias injection detection and provenance tracking",
    "ARCH-CONTEXT-ATTACK-223": "Context integrity boundary enforcement with injection point detection",
    "ARCH-STATE-PERSIST-224": "State isolation between sessions with verified cleanup on session termination",
    "ARCH-MEM-CORRUPT-225": "Memory integrity protection with bounds checking and corruption detection",
    "ARCH-HISTORY-MANIP-226": "Conversation history integrity with append-only authenticated logging",
    "ARCH-CROSS-SESSION-227": "Cross-session isolation with verified state boundary enforcement",
    "ARCH-PERSIST-STATE-228": "Persistent state lifecycle management with authorized-access-only enforcement",
    "ARCH-CACHE-COHERENCE-229": "Cache coherence protocol with consistency verification across distributed instances",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 9: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
