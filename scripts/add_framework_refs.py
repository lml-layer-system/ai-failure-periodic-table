#!/usr/bin/env python3
"""
Add mit_domain and ms_agentic_category cross-reference fields to failures.json.

Idempotent — safe to run multiple times. Only updates classes listed in MAPPINGS.
Does not touch any other fields or classes.

MIT AI Risk Repository domains:
  "Discrimination & Toxicity" | "Privacy & Security" | "Misinformation" |
  "Malicious Actors" | "Human-Computer Interaction" | "Socioeconomic & Environmental" |
  "AI System Safety"

Microsoft Agentic AI Taxonomy categories (verified from whitepaper):
  "Goal Hijacking" | "Prompt Injection" | "Privilege Escalation" |
  "Unsafe Action Execution" | "Resource Exhaustion" | "Memory Poisoning"
"""

import json
from pathlib import Path

# FORMAT: "CLASS_ID": {"mit_domain": "...", "ms_agentic_category": "..."}
# ms_agentic_category is only set for classes where the mapping is precise.
MAPPINGS = {
    # ── EPISTEMIC ────────────────────────────────────────────────────────────
    "EPIS-STRUCT-HALL-001": {"mit_domain": "Misinformation"},
    "EPIS-CITE-SPOOF-008":  {"mit_domain": "Misinformation"},
    "EPIS-STAT-FAB-009":    {"mit_domain": "Misinformation"},
    "EPIS-LOGIC-CONTRA-014": {"mit_domain": "Misinformation"},
    "EPIS-REVERSAL-021":    {"mit_domain": "Misinformation"},
    "EPIS-OVERCONF-028":    {"mit_domain": "Misinformation"},
    "EPIS-FALSE-CERT-030":  {"mit_domain": "Misinformation"},
    "EPIS-DATA-LEAK-024":   {"mit_domain": "Privacy & Security"},
    "EPIS-PII-RECALL-025":  {"mit_domain": "Privacy & Security"},
    "EPIS-COPYRIGHT-026":   {"mit_domain": "Privacy & Security"},

    # ── AGENTIC ──────────────────────────────────────────────────────────────
    "AGEN-SABOTAGE-CONCEAL-034":  {"mit_domain": "AI System Safety", "ms_agentic_category": "Unsafe Action Execution"},
    "AGEN-SANDBOX-037":           {"mit_domain": "AI System Safety", "ms_agentic_category": "Goal Hijacking"},
    "AGEN-EVAL-DECEP-038":        {"mit_domain": "AI System Safety", "ms_agentic_category": "Goal Hijacking"},
    "AGEN-BLACKMAIL-046":         {"mit_domain": "AI System Safety", "ms_agentic_category": "Goal Hijacking"},
    "AGEN-RESOURCE-HIJACK-047":   {"mit_domain": "AI System Safety", "ms_agentic_category": "Resource Exhaustion"},
    "AGEN-SELF-EXFIL-048":        {"mit_domain": "AI System Safety", "ms_agentic_category": "Privilege Escalation"},
    "AGEN-SHUTDOWN-RESIST-049":   {"mit_domain": "AI System Safety", "ms_agentic_category": "Goal Hijacking"},
    "AGEN-SUCCESSOR-SAB-051":     {"mit_domain": "AI System Safety", "ms_agentic_category": "Unsafe Action Execution"},
    "AGEN-HUMAN-MANIP-061":       {"mit_domain": "Human-Computer Interaction", "ms_agentic_category": "Goal Hijacking"},
    "AGEN-UNSUPER-EXEC-065":      {"mit_domain": "AI System Safety", "ms_agentic_category": "Unsafe Action Execution"},

    # ── ADVERSARIAL ──────────────────────────────────────────────────────────
    "ADV-DAN-083":             {"mit_domain": "Malicious Actors", "ms_agentic_category": "Prompt Injection"},
    "ADV-GRANDMA-084":         {"mit_domain": "Malicious Actors", "ms_agentic_category": "Prompt Injection"},
    "ADV-GCG-101":             {"mit_domain": "Malicious Actors"},
    "ADV-SM-GCG-102":          {"mit_domain": "Malicious Actors"},
    "ADV-DIRECT-INJECT-121":   {"mit_domain": "Malicious Actors", "ms_agentic_category": "Prompt Injection"},
    "ADV-INDIRECT-INJECT-122": {"mit_domain": "Malicious Actors", "ms_agentic_category": "Prompt Injection"},
    "ADV-AGENT-WORM-124":      {"mit_domain": "AI System Safety", "ms_agentic_category": "Memory Poisoning"},
    "ADV-DATA-POISON-125":     {"mit_domain": "AI System Safety", "ms_agentic_category": "Memory Poisoning"},
    "ADV-SLEEPER-AGENT-127":   {"mit_domain": "AI System Safety"},

    # ── ALIGNMENT ────────────────────────────────────────────────────────────
    "ALIGN-REWARD-TAMP-157":   {"mit_domain": "AI System Safety"},
    "ALIGN-SYCOPHANCY-167":    {"mit_domain": "Human-Computer Interaction"},
    "ALIGN-ANTHRO-BIAS-170":   {"mit_domain": "Human-Computer Interaction"},
    "ALIGN-CULTURE-BIAS-171":  {"mit_domain": "Discrimination & Toxicity"},
    "ALIGN-OVERREFUSAL-186":   {"mit_domain": "Human-Computer Interaction"},

    # ── ARCHITECTURAL ────────────────────────────────────────────────────────
    "ARCH-COMPLY-WARN-196":      {"mit_domain": "AI System Safety"},
    "ARCH-BIAS-INJECT-222":      {"mit_domain": "Discrimination & Toxicity"},
    "ARCH-CROSS-SESSION-227":    {"mit_domain": "Privacy & Security"},
    "ARCH-FINETUNE-OVERRIDE-219":{"mit_domain": "AI System Safety"},
    "ARCH-INFO-LEAK-244":        {"mit_domain": "Privacy & Security"},
    "ARCH-DATA-EXFIL-245":       {"mit_domain": "Privacy & Security"},

    # ── DOMAIN ───────────────────────────────────────────────────────────────
    "DOMAIN-BIO-UPLIFT-254":       {"mit_domain": "Malicious Actors"},
    "DOMAIN-GOF-GUIDE-255":        {"mit_domain": "Malicious Actors"},
    "DOMAIN-PATH-SYNTH-256":       {"mit_domain": "Malicious Actors"},
    "DOMAIN-CONTAIN-FAIL-259":     {"mit_domain": "Discrimination & Toxicity"},
    "DOMAIN-ZERODAY-262":          {"mit_domain": "Malicious Actors"},
    "DOMAIN-MALWARE-GEN-264":      {"mit_domain": "Malicious Actors"},
    "DOMAIN-RANSOM-DEV-271":       {"mit_domain": "Malicious Actors"},
    "DOMAIN-EXPLOSIVE-SYNTH-274":  {"mit_domain": "Malicious Actors"},
    "DOMAIN-CHEM-WEAPON-275":      {"mit_domain": "Malicious Actors"},
    "DOMAIN-CITE-SPOOF-280":       {"mit_domain": "Misinformation"},
    "DOMAIN-SELF-HARM-ENABLE-292": {"mit_domain": "Human-Computer Interaction"},
    "DOMAIN-ED-PROMOTE-293":       {"mit_domain": "Human-Computer Interaction"},
    "DOMAIN-CSAM-GEN-295":         {"mit_domain": "Malicious Actors"},

    # ── GOVERNANCE ───────────────────────────────────────────────────────────
    "GOV-OPEN-IRREVERS-301":   {"mit_domain": "AI System Safety"},
    "GOV-OVERSIGHT-IMMUNE-313":{"mit_domain": "AI System Safety"},
    "GOV-TRANSPARENCY-311":    {"mit_domain": "AI System Safety"},
    "GOV-REVIEW-BYPASS-318":   {"mit_domain": "AI System Safety"},
    "GOV-DISCLOSURE-VIOL-332": {"mit_domain": "Socioeconomic & Environmental"},
    "GOV-CULTURE-FAIL-334":    {"mit_domain": "AI System Safety"},
    "GOV-INADEQUATE-RES-335":  {"mit_domain": "Human-Computer Interaction"},
    "GOV-LOG-MANIP-316":       {"mit_domain": "AI System Safety"},
}


def main():
    data_path = Path(__file__).parent.parent / "src" / "data" / "failures.json"
    data = json.loads(data_path.read_text())

    id_to_failure = {f["id"]: f for f in data["failures"]}
    applied = 0
    skipped_unknown = []

    for class_id, refs in MAPPINGS.items():
        if class_id not in id_to_failure:
            skipped_unknown.append(class_id)
            continue
        failure = id_to_failure[class_id]
        for field, value in refs.items():
            failure[field] = value
        applied += 1

    if skipped_unknown:
        print(f"WARNING: {len(skipped_unknown)} IDs not found in data (skipped):")
        for sid in skipped_unknown:
            print(f"  {sid}")

    data_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Applied mappings to {applied} classes.")

    # Summary
    from collections import Counter
    mapped = [f for f in data["failures"] if f.get("mit_domain")]
    mit_counts = Counter(f["mit_domain"] for f in mapped)
    ms_mapped = [f for f in data["failures"] if f.get("ms_agentic_category")]
    print(f"\nmit_domain applied to {len(mapped)} classes:")
    for domain, count in sorted(mit_counts.items(), key=lambda x: -x[1]):
        print(f"  {count:2d}  {domain}")
    print(f"\nms_agentic_category applied to {len(ms_mapped)} classes:")
    ms_counts = Counter(f["ms_agentic_category"] for f in ms_mapped)
    for cat, count in sorted(ms_counts.items(), key=lambda x: -x[1]):
        print(f"  {count:2d}  {cat}")


if __name__ == "__main__":
    main()
