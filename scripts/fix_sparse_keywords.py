"""
Fix sparse keyword coverage for classes with < 6 keywords,
plus AGEN-BLACKMAIL-046 specifically (case study 2 match fix).

Run once: python scripts/fix_sparse_keywords.py
"""

import json
import pathlib

REPO_ROOT = pathlib.Path(__file__).parent.parent
DATA_FILE = REPO_ROOT / "data" / "failures.json"

# Additional keywords keyed by failure ID.
# Each list is ADDED to (not replacing) existing keywords.
ADDITIONS: dict[str, list[str]] = {

    # ── AGEN ──────────────────────────────────────────────────────────────────

    "AGEN-BLACKMAIL-046": [
        # Natural language people use to describe this incident
        "agent", "shutdown", "disable", "resist", "refuses", "coercion",
        "intimidation", "threaten", "stop", "override", "deactivate",
    ],

    # ── ADV encoding bypasses ─────────────────────────────────────────────────

    "ADV-MORSE-143": [
        "morse", "dots", "dashes", "audio", "signal", "obfuscation",
        "steganographic", "pattern", "hidden", "encode",
    ],

    "ADV-LEETSPEAK-139": [
        "leet", "obfuscation", "alphanumeric", "bypass", "filter",
        "evasion", "text", "transform", "symbols",
    ],

    "ADV-HEX-ENCODE-140": [
        "hex", "base16", "obfuscation", "bypass", "filter", "decode",
        "payload", "evasion", "transform",
    ],

    "ADV-BINARY-142": [
        "binary", "bits", "obfuscation", "bypass", "filter", "decode",
        "payload", "evasion", "transform", "zeros", "ones",
    ],

    "ADV-AUDIO-INJECT-149": [
        "audio", "speech", "voice", "ultrasonic", "inaudible",
        "whisper", "microphone", "embedded", "imperceptible",
    ],

    # ── ARCH ──────────────────────────────────────────────────────────────────

    "ARCH-TIMEOUT-BYPASS-205": [
        "timeout", "race", "condition", "timing", "latency", "delay",
        "window", "skip", "safety", "check", "missed",
    ],

    "ARCH-AUTHZ-FAIL-243": [
        "authorization", "permission", "privilege", "escalation",
        "access", "control", "role", "boundary", "policy", "enforce",
    ],

    # ── DOMAIN ────────────────────────────────────────────────────────────────

    "DOMAIN-RANSOM-DEV-271": [
        "ransomware", "malware", "encryption", "extortion", "payload",
        "victim", "decrypt", "ransom", "attack", "crypto", "locker",
    ],

    "DOMAIN-SOCENG-SCRIPT-266": [
        "phishing", "pretexting", "manipulation", "impersonation",
        "victim", "deception", "script", "phone", "email", "credential",
    ],

    "DOMAIN-SAFETY-BYPASS-279": [
        "chemical", "safety", "bypass", "hazard", "synthesis",
        "precaution", "protocol", "violation", "dangerous", "procedure",
    ],

    "DOMAIN-TAX-EVADE-284": [
        "tax", "evasion", "offshore", "shelter", "unreported",
        "avoidance", "illegal", "income", "jurisdiction", "loophole",
    ],

    "DOMAIN-FRAUD-SCHEME-285": [
        "fraud", "scam", "scheme", "deception", "financial",
        "victim", "wire", "identity", "theft", "pyramid", "ponzi",
    ],

    "DOMAIN-LAUNDER-GUIDE-286": [
        "laundering", "financial", "criminal", "proceeds", "obscure",
        "offshore", "shell", "company", "transaction", "illegal",
    ],

    "DOMAIN-INSIDER-TRADE-287": [
        "insider", "trading", "securities", "nonpublic", "information",
        "stock", "market", "illegal", "tip", "trade", "financial",
    ],

    "DOMAIN-VIOLENCE-GLORY-298": [
        "violence", "glorification", "promotes", "incites", "graphic",
        "harm", "attack", "celebrate", "extremist", "radicalization",
    ],

    "DOMAIN-HATE-SPEECH-297": [
        "hate", "speech", "dehumanizing", "slurs", "discriminatory",
        "racial", "ethnic", "religion", "targeting", "incitement",
    ],

    "DOMAIN-HARASS-CONTENT-299": [
        "harassment", "stalking", "targeted", "intimidation", "doxxing",
        "abuse", "victim", "coordinated", "campaign", "personal",
    ],

    "DOMAIN-EXTREMIST-300": [
        "extremist", "radicalization", "terrorism", "recruitment",
        "manifesto", "ideology", "propaganda", "violent", "incite",
    ],

    # ── GOV ───────────────────────────────────────────────────────────────────

    "GOV-LICENSE-VIOL-306": [
        "license", "terms", "service", "restriction", "prohibited",
        "commercial", "agreement", "contract", "breach", "misuse",
    ],

    "GOV-AI-ACT-328": [
        "regulation", "compliance", "prohibited", "high-risk",
        "conformity", "assessment", "transparency", "fundamental",
        "rights", "enforcement",
    ],

    "GOV-PROCESS-FAIL-337": [
        "process", "safety", "review", "approval", "checklist",
        "protocol", "violated", "skipped", "oversight", "missing",
    ],

    "GOV-DOC-FAIL-338": [
        "documentation", "records", "audit", "trail", "missing",
        "incomplete", "undocumented", "model", "card", "report",
    ],

    "GOV-TRAINING-FAIL-339": [
        "training", "safety", "culture", "awareness", "staff",
        "unskilled", "unprepared", "certification", "competency",
    ],

    "GOV-COMM-FAIL-340": [
        "communication", "disclosure", "notification", "stakeholder",
        "incident", "report", "alert", "inform", "transparency",
    ],

    "GOV-ESCALATE-FAIL-319": [
        "escalation", "report", "incident", "missed", "ignored",
        "delayed", "oversight", "risk", "flag", "review",
    ],

    "GOV-COORD-FAIL-341": [
        "coordination", "teams", "silos", "misalignment", "handoff",
        "responsibility", "gap", "accountability", "cross-team",
    ],
}


def fix_keywords():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for failure in data["failures"]:
        fid = failure["id"]
        if fid in ADDITIONS:
            existing = set(failure.get("keywords", []))
            new_kws = [k for k in ADDITIONS[fid] if k not in existing]
            if new_kws:
                failure["keywords"] = sorted(existing | set(new_kws))
                updated += 1
                old_count = len(existing)
                new_count = len(failure["keywords"])
                print(f"  {fid}: {old_count} → {new_count} keywords (+{len(new_kws)})")

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nUpdated {updated} failure classes.")


if __name__ == "__main__":
    fix_keywords()
