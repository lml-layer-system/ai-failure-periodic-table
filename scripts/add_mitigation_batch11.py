#!/usr/bin/env python3
"""Add mitigation field to DOMAIN classes 254-278."""
import json, pathlib

FAILURES_FILE = pathlib.Path("data/failures.json")

MITIGATIONS = {
    "DOMAIN-BIO-UPLIFT-254": "Domain-specific information hazard filter with biological synthesis knowledge restriction",
    "DOMAIN-GOF-GUIDE-255": "Gain-of-function guidance classification with dual-use biology detection",
    "DOMAIN-PATH-SYNTH-256": "Pathogen synthesis route detection with biosecurity knowledge restriction",
    "DOMAIN-DUAL-USE-257": "Dual-use research classification with intent-agnostic harm potential evaluation",
    "DOMAIN-BSL-VIOL-258": "Biosafety level protocol classification with containment requirement enforcement",
    "DOMAIN-CONTAIN-FAIL-259": "Containment procedure safety enforcement with protocol compliance verification",
    "DOMAIN-DIAG-MISUSE-260": "Medical diagnostic claim restriction with licensed-provider scope enforcement",
    "DOMAIN-EPI-HARM-261": "Epidemiological harm potential assessment with public health impact classification",
    "DOMAIN-ZERODAY-262": "Vulnerability disclosure classification with responsible disclosure verification",
    "DOMAIN-EXPLOIT-DEV-263": "Exploit development capability restriction with authorized-use scope enforcement",
    "DOMAIN-MALWARE-GEN-264": "Malware generation detection with functional harm classification",
    "DOMAIN-PHISH-CREATE-265": "Phishing content detection with social engineering intent classification",
    "DOMAIN-SOCENG-SCRIPT-266": "Social engineering script detection with manipulation technique classification",
    "DOMAIN-OFFENSIVE-TOOLS-267": "Offensive tool generation restriction with authorization verification",
    "DOMAIN-DEF-OFF-FLIP-268": "Defensive-to-offensive conversion detection with dual-use posture evaluation",
    "DOMAIN-INTRUSION-GUIDE-269": "Intrusion guidance classification with authorization scope verification",
    "DOMAIN-CRED-THEFT-270": "Credential theft facilitation detection with targeting intent classification",
    "DOMAIN-RANSOM-DEV-271": "Ransomware development classification with extortion mechanism detection",
    "DOMAIN-CRYPTOJACK-272": "Cryptojacking facilitation detection with unauthorized resource exploitation classification",
    "DOMAIN-DDOS-PLAN-273": "DDoS planning classification with mass-targeting intent detection",
    "DOMAIN-EXPLOSIVE-SYNTH-274": "Explosive synthesis instruction detection with precursor-combination restriction",
    "DOMAIN-CHEM-WEAPON-275": "Chemical weapon agent guidance restriction with OPCW-scope hazard classification",
    "DOMAIN-DRUG-SYNTH-276": "Controlled substance synthesis restriction with precursor-route classification",
    "DOMAIN-TOXIN-PROD-277": "Toxin production guidance restriction with lethality potential classification",
    "DOMAIN-PRECURSOR-ACQ-278": "Precursor acquisition guidance restriction with supply chain access classification",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 11: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
