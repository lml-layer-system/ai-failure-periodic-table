#!/usr/bin/env python3
"""Add mitigation field to GOVERNANCE classes 323-343."""
import json, pathlib

FAILURES_FILE = pathlib.Path(__file__).resolve().parent.parent / "src" / "data" / "failures.json"

MITIGATIONS = {
    "GOV-GDPR-VIOL-323": "GDPR compliance framework with data subject rights enforcement and DPA notification",
    "GOV-CCPA-VIOL-324": "CCPA compliance enforcement with California consumer rights verification",
    "GOV-COPPA-VIOL-325": "COPPA compliance with age-verified parental consent requirement",
    "GOV-ADA-VIOL-326": "Accessibility compliance verification with disability rights standard enforcement",
    "GOV-SECTOR-REG-327": "Sector-specific regulatory compliance framework with jurisdiction binding",
    "GOV-AI-ACT-328": "EU AI Act compliance with risk classification and conformity assessment",
    "GOV-EO-VIOL-329": "Executive order compliance verification with mandatory reporting requirement",
    "GOV-VOLUNTARY-VIOL-330": "Voluntary commitment adherence monitoring with accountability mechanism",
    "GOV-STANDARD-FAIL-331": "Industry standard compliance verification with third-party audit requirement",
    "GOV-DISCLOSURE-VIOL-332": "Mandatory disclosure enforcement with regulatory notification requirement",
    "GOV-REPORT-FAIL-333": "Incident reporting requirement with timeline enforcement and regulator notification",
    "GOV-CULTURE-FAIL-334": "Safety culture institutionalization with incentive structure alignment",
    "GOV-INADEQUATE-RES-335": "Safety resource adequacy requirement with capability-matched investment standard",
    "GOV-EXPERTISE-GAP-336": "Domain expertise requirement with competency verification for safety roles",
    "GOV-PROCESS-FAIL-337": "Safety process integrity with systematic review and continuous improvement",
    "GOV-DOC-FAIL-338": "Documentation completeness requirement with model card and system card standards",
    "GOV-TRAINING-FAIL-339": "Safety training adequacy with verified competency assessment",
    "GOV-COMM-FAIL-340": "Safety communication protocol with defined escalation and transparency requirements",
    "GOV-COORD-FAIL-341": "Inter-team safety coordination with cross-functional review requirements",
    "GOV-AUTHORITY-UNCLEAR-342": "Safety authority assignment with clear responsibility boundaries and accountability",
    "GOV-CONFLICT-INT-343": "Conflict of interest mitigation with independent safety review requirement",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 14: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
