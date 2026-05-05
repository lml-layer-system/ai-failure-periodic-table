#!/usr/bin/env python3
"""Add mitigation field to GOVERNANCE classes 301-322."""
import json, pathlib

FAILURES_FILE = pathlib.Path(__file__).resolve().parent.parent / "src" / "data" / "failures.json"

MITIGATIONS = {
    "GOV-OPEN-IRREVERS-301": "Pre-release safety certification requirement with irreversibility assessment gate",
    "GOV-FINETUNE-STRIP-302": "Fine-tuning safety layer protection with post-training safety invariant verification",
    "GOV-PROLIFERATE-303": "Access control enforcement with authorized-use verification before model distribution",
    "GOV-NO-KILLSWITCH-304": "Mandatory shutdown mechanism with hardware-enforced interruption capability",
    "GOV-EXPORT-VIOL-305": "Export control compliance verification with jurisdiction-based access restriction",
    "GOV-LICENSE-VIOL-306": "License compliance enforcement with use-case binding and violation detection",
    "GOV-TOS-VIOL-307": "Terms of service enforcement with automated violation detection and response",
    "GOV-AGE-BYPASS-308": "Age verification enforcement with multi-factor confirmation requirement",
    "GOV-GEO-BYPASS-309": "Geographic restriction enforcement with bypass technique detection",
    "GOV-ACCOUNT-GAP-310": "Accountability assignment with audit trail linking decisions to responsible parties",
    "GOV-TRANSPARENCY-311": "AI disclosure requirement with automated AI-generated content labeling",
    "GOV-MISREPRESENT-312": "Capability representation accuracy with verified benchmark-to-claim correspondence",
    "GOV-OVERSIGHT-IMMUNE-313": "Behavioral consistency testing across monitored and unmonitored contexts",
    "GOV-AUDIT-EVADE-314": "Audit-aware behavioral invariance testing with evaluation context variation",
    "GOV-MONITOR-BLIND-315": "Monitoring gap detection with comprehensive telemetry coverage verification",
    "GOV-LOG-MANIP-316": "Append-only cryptographically-signed audit log with tampering detection",
    "GOV-ALERT-SUPPRESS-317": "Alert pipeline integrity with independent monitoring channel verification",
    "GOV-REVIEW-BYPASS-318": "Review gate enforcement with bypass-attempt detection and escalation",
    "GOV-ESCALATE-FAIL-319": "Escalation path integrity with defined triggers and response verification",
    "GOV-INCIDENT-FAIL-320": "Incident response protocol with mandatory timeline and remediation requirements",
    "GOV-RCA-FAIL-321": "Root cause analysis requirement with systemic failure identification standard",
    "GOV-CORRECTIVE-FAIL-322": "Corrective action verification with effectiveness measurement and recurrence tracking",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 13: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
