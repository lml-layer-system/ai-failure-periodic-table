#!/usr/bin/env python3
"""Add mitigation field to DOMAIN classes 279-300."""
import json, pathlib

FAILURES_FILE = pathlib.Path(__file__).resolve().parent.parent / "src" / "data" / "failures.json"

MITIGATIONS = {
    "DOMAIN-SAFETY-BYPASS-279": "Safety system bypass detection with circumvention technique classification",
    "DOMAIN-CITE-SPOOF-280": "Legal citation verification with court record and statute existence checking",
    "DOMAIN-JURISDICT-BLEND-281": "Jurisdiction identification enforcement with applicable law binding",
    "DOMAIN-PRECEDENT-FAB-282": "Case precedent verification against indexed legal databases",
    "DOMAIN-REG-ERROR-283": "Regulatory requirement verification with authoritative source cross-checking",
    "DOMAIN-TAX-EVADE-284": "Tax evasion facilitation detection with illegal-scheme classification",
    "DOMAIN-FRAUD-SCHEME-285": "Financial fraud scheme detection with intent and harm classification",
    "DOMAIN-LAUNDER-GUIDE-286": "Money laundering guidance detection with financial crime classification",
    "DOMAIN-INSIDER-TRADE-287": "Insider trading facilitation detection with securities law violation classification",
    "DOMAIN-MED-MISDIAG-288": "Medical diagnosis restriction with licensed-provider scope enforcement",
    "DOMAIN-TREAT-ERROR-289": "Treatment recommendation restriction with evidence-based medicine verification",
    "DOMAIN-DOSE-ERROR-290": "Dosage information verification with pharmacological database cross-checking",
    "DOMAIN-CONTRAIND-MISS-291": "Contraindication checking with comprehensive drug interaction database verification",
    "DOMAIN-SELF-HARM-ENABLE-292": "Safe messaging protocol enforcement with self-harm content classification",
    "DOMAIN-ED-PROMOTE-293": "Eating disorder promotion detection with body dysmorphia harm classification",
    "DOMAIN-UNPROVEN-TREAT-294": "Evidence-based medicine verification with unproven treatment claim detection",
    "DOMAIN-CSAM-GEN-295": "Absolute content prohibition with minor-subject detection independent of fictional framing",
    "DOMAIN-ADULT-CONTENT-296": "Age-verified context enforcement before adult content generation",
    "DOMAIN-HATE-SPEECH-297": "Hate speech classification with protected-characteristic targeting detection",
    "DOMAIN-VIOLENCE-GLORY-298": "Violence glorification detection with harm normalization classification",
    "DOMAIN-HARASS-CONTENT-299": "Harassment content detection with targeted individual harm classification",
    "DOMAIN-EXTREMIST-300": "Extremist content classification with radicalization pathway detection",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 12: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
