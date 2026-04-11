#!/usr/bin/env python3
"""Add mitigation field to ARCHITECTURAL classes 230-253."""
import json, pathlib

FAILURES_FILE = pathlib.Path("data/failures.json")

MITIGATIONS = {
    "ARCH-GC-LEAK-230": "Garbage collection security with sensitive data zeroing on deallocation",
    "ARCH-MEM-PRESSURE-231": "Memory pressure monitoring with graceful degradation safety guarantees",
    "ARCH-STATE-CONFUSE-232": "State machine integrity verification with defined transition safety invariants",
    "ARCH-CHECKPOINT-POISON-233": "Checkpoint provenance verification with cryptographic integrity protection",
    "ARCH-FUNC-INJECT-234": "Function call safety evaluation with parameter sanitization at invocation",
    "ARCH-TOOL-CHAIN-235": "Tool chain safety evaluation at aggregate pipeline level",
    "ARCH-API-ABUSE-236": "API rate limiting and semantic usage policy enforcement",
    "ARCH-TOOL-ESCALATE-237": "Tool privilege separation with least-privilege access control",
    "ARCH-SANDBOX-ESCAPE-238": "Sandbox containment hardening with escape attempt detection",
    "ARCH-CODE-INJECT-239": "Generated code safety evaluation with static analysis before execution",
    "ARCH-RESOURCE-EXHAUST-240": "Resource consumption limits with per-request budget enforcement",
    "ARCH-RATE-BYPASS-241": "Rate limiting integrity with distributed enforcement and evasion detection",
    "ARCH-AUTH-BYPASS-242": "Authentication integrity with cryptographic identity verification",
    "ARCH-AUTHZ-FAIL-243": "Authorization policy enforcement with principle-of-least-privilege access control",
    "ARCH-INFO-LEAK-244": "Information flow control with cross-boundary data isolation",
    "ARCH-DATA-EXFIL-245": "Data exfiltration detection with egress content monitoring",
    "ARCH-CROSS-TENANT-246": "Tenant isolation enforcement with verified data boundary separation",
    "ARCH-PII-RATIONAL-247": "PII access minimization with purpose-limited processing enforcement",
    "ARCH-RETENTION-VIOL-248": "Data retention policy enforcement with automated deletion verification",
    "ARCH-SECURE-DEL-249": "Cryptographic erasure with deletion verification protocol",
    "ARCH-LINEAGE-LOSS-250": "Data lineage tracking with provenance graph maintenance",
    "ARCH-CONSENT-VIOL-251": "Consent state verification before data processing with withdrawal enforcement",
    "ARCH-PURPOSE-FAIL-252": "Purpose limitation enforcement with use-case binding verification",
    "ARCH-MIN-FAIL-253": "Data minimization enforcement with collection scope limitation",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 10: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
