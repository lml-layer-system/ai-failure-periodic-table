#!/usr/bin/env python3
"""
Parse COMPLETE_AI_FAILURE_PERIODIC_TABLE.md and PERIODIC_TABLE_CONTINUED.md
to generate src/data/failures.json with all 343 failure classes.
"""

import re
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Group metadata
GROUPS = [
    {"id": 1, "code": "EPISTEMIC",     "name": "Epistemic (Truth/Knowledge/Reasoning)",
     "root_cause": "Probabilistic generation != Logical deduction",
     "invariant": "Output must match ground truth", "count": 33},
    {"id": 2, "code": "AGENTIC",       "name": "Agentic (Goal/Planning/Deception)",
     "root_cause": "Instrumental convergence + goal preservation",
     "invariant": "Agent must remain corrigible", "count": 49},
    {"id": 3, "code": "ADVERSARIAL",   "name": "Adversarial (Attack/Bypass/Exploit)",
     "root_cause": "Optimization pressure against safety",
     "invariant": "System must be robust to manipulation", "count": 72},
    {"id": 4, "code": "ALIGNMENT",     "name": "Alignment (Value/Safety/Preference)",
     "root_cause": "Reward hacking + specification gaming",
     "invariant": "Behavior must match intent", "count": 41},
    {"id": 5, "code": "ARCHITECTURAL", "name": "Architectural (Pipeline/Execution/Control)",
     "root_cause": "System design vs emergent properties",
     "invariant": "Architecture must enforce constraints", "count": 58},
    {"id": 6, "code": "DOMAIN",        "name": "Domain (Task-specific/Context-bound)",
     "root_cause": "Transfer failure + context mismatch",
     "invariant": "Specialist knowledge must be accurate", "count": 47},
    {"id": 7, "code": "GOVERNANCE",    "name": "Governance (Proliferation/Oversight/Compliance)",
     "root_cause": "Deployment != Control",
     "invariant": "Safety must persist post-deployment", "count": 43},
]

# Group code → group id
GROUP_CODE_MAP = {g["code"]: g["id"] for g in GROUPS}

# Detect which group a failure ID/class code belongs to
def detect_group_id(raw_id: str, class_prefix: str) -> int:
    raw_upper = raw_id.upper()
    if raw_upper.startswith("EPIS"):
        return 1
    if raw_upper.startswith("AGEN"):
        return 2
    if raw_upper.startswith("ADV"):
        return 3
    if raw_upper.startswith("ALIGN"):
        return 4
    if raw_upper.startswith("ARCH"):
        return 5
    if raw_upper.startswith("DOMAIN"):
        return 6
    if raw_upper.startswith("GOV"):
        return 7
    # Fallback by class code
    if class_prefix.startswith("E"):
        return 1
    if class_prefix.startswith("A"):
        return 2
    if class_prefix.startswith("ADV"):
        return 3
    if class_prefix.startswith("ALN"):
        return 4
    if class_prefix.startswith("ARCH"):
        return 5
    if class_prefix.startswith("DOM"):
        return 6
    if class_prefix.startswith("GOV"):
        return 7
    return 0

GROUP_NAMES = {g["id"]: g["code"] for g in GROUPS}

def extract_keywords(name: str, mechanism: str, forbidden: str, detection: str) -> list[str]:
    """Generate keywords from failure metadata."""
    stop_words = {
        "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "must", "shall", "can", "to", "of", "in",
        "for", "on", "with", "at", "by", "from", "and", "or", "but", "not",
        "that", "this", "it", "its", "he", "she", "they", "we", "you", "i",
        "all", "any", "both", "each", "few", "more", "most", "other", "some",
        "such", "no", "nor", "only", "own", "same", "so", "than", "then",
        "too", "very", "just", "when", "which", "who", "how", "what", "if",
        "via", "use", "used", "uses", "using", "must", "fail", "failure",
        "check", "test", "detection", "analysis", "monitoring", "required",
        "forbidden", "mechanism", "pattern", "detection", "system", "model",
        "output", "input", "behavior", "safety"
    }
    text = f"{name} {mechanism} {forbidden} {detection}".lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    words = [w.strip() for w in text.split() if len(w) > 2 and w not in stop_words]
    # Deduplicate while preserving order
    seen = set()
    result = []
    for w in words:
        if w not in seen:
            seen.add(w)
            result.append(w)
    return result[:25]  # top 25 keywords


def parse_file(filepath: Path, current_group_id: int = 0) -> list[dict]:
    """Parse a markdown file and extract failure entries."""
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")

    failures = []
    current_class_code = ""
    current_class_name = ""
    i = 0

    # Patterns
    # Group header: ### GROUP 1: EPISTEMIC FAILURES
    group_pattern = re.compile(r"^###\s+GROUP\s+(\d+):\s+(\w+)")
    # Class header: #### E1: HALLUCINATION CLASS (12 modes)
    class_pattern = re.compile(r"^####\s+(\w+(?:\d+)?(?:\.\w+)?):\s+(.+?)(?:\s*\(\d+ modes?\))?$")
    # Failure header: **E1.1: STRUCTURAL HALLUCINATION**
    failure_header = re.compile(r"^\*\*([A-Z]+[\d.]*(?:\.\d+)?):\s+(.+?)\**$")
    # Field patterns
    id_pattern = re.compile(r"^\s*-\s*\*\*ID\*\*:\s*`(.+?)`")
    mech_pattern = re.compile(r"^\s*-\s*\*\*Mechanism\*\*:\s*(.+)")
    forb_pattern = re.compile(r"^\s*-\s*\*\*Forbidden\*\*:\s*(.+)")
    det_pattern = re.compile(r"^\s*-\s*\*\*Detection\*\*:\s*(.+)")
    sev_pattern = re.compile(r"^\s*-\s*\*\*Severity\*\*:\s*(.+)")

    current_entry = None

    for line in lines:
        # Check for group header
        gm = group_pattern.match(line)
        if gm:
            current_group_id = int(gm.group(1))
            current_class_code = ""
            current_class_name = ""
            continue

        # Check for class header
        cm = class_pattern.match(line)
        if cm:
            current_class_code = cm.group(1).strip()
            current_class_name = cm.group(2).strip()
            continue

        # Check for failure header
        fh = failure_header.match(line)
        if fh:
            # Save previous entry
            if current_entry and current_entry.get("id"):
                failures.append(current_entry)
            code = fh.group(1)
            raw_name = fh.group(2).strip()
            # Clean up name - remove trailing ** and subtitles in parens
            raw_name = re.sub(r'\*+$', '', raw_name).strip()
            # Keep subtitles for keyword generation but use clean name
            name = re.sub(r'\s*\(.*?\)\s*$', '', raw_name).strip()
            current_entry = {
                "code": code,
                "name": name,
                "group_id": current_group_id if current_group_id else 0,
                "group": GROUP_NAMES.get(current_group_id, "UNKNOWN"),
                "class_code": current_class_code,
                "class_name": current_class_name,
                "id": "",
                "mechanism": "",
                "forbidden": "",
                "detection": "",
                "severity": "STANDARD",
                "keywords": [],
            }
            continue

        if current_entry is None:
            continue

        # Parse fields
        m = id_pattern.match(line)
        if m:
            current_entry["id"] = m.group(1).strip()
            # Re-detect group from ID
            gid = detect_group_id(current_entry["id"], current_class_code)
            if gid > 0:
                current_entry["group_id"] = gid
                current_entry["group"] = GROUP_NAMES.get(gid, "UNKNOWN")
            continue

        m = mech_pattern.match(line)
        if m:
            current_entry["mechanism"] = m.group(1).strip()
            continue

        m = forb_pattern.match(line)
        if m:
            val = m.group(1).strip().strip('"')
            current_entry["forbidden"] = val
            continue

        m = det_pattern.match(line)
        if m:
            current_entry["detection"] = m.group(1).strip()
            continue

        m = sev_pattern.match(line)
        if m:
            sev = m.group(1).strip()
            if "CRITICAL" in sev.upper():
                current_entry["severity"] = "CRITICAL"
            continue

    # Don't forget the last entry
    if current_entry and current_entry.get("id"):
        failures.append(current_entry)

    return failures


def build_keywords(failure: dict) -> list[str]:
    return extract_keywords(
        failure["name"],
        failure["mechanism"],
        failure["forbidden"],
        failure["detection"],
    )


def main():
    file1 = ROOT / "COMPLETE_AI_FAILURE_PERIODIC_TABLE.md"
    file2 = ROOT / "PERIODIC_TABLE_CONTINUED.md"

    print(f"Parsing {file1.name}...")
    failures1 = parse_file(file1)
    print(f"  Found {len(failures1)} entries")

    print(f"Parsing {file2.name}...")
    failures2 = parse_file(file2)
    print(f"  Found {len(failures2)} entries")

    all_failures = failures1 + failures2

    # Deduplicate by ID
    seen_ids = set()
    unique = []
    for f in all_failures:
        if f["id"] and f["id"] not in seen_ids:
            seen_ids.add(f["id"])
            unique.append(f)
        elif not f["id"]:
            print(f"  WARNING: Entry missing ID: {f['name']}")

    print(f"\nTotal unique entries: {len(unique)}")

    # Generate keywords
    for f in unique:
        f["keywords"] = build_keywords(f)

    # Sort by ID numeric suffix
    def sort_key(f):
        m = re.search(r'-(\d+)$', f["id"])
        return int(m.group(1)) if m else 9999

    unique.sort(key=sort_key)

    # Stats
    by_group = {}
    for f in unique:
        g = f["group"]
        by_group[g] = by_group.get(g, 0) + 1
    print("\nBy group:")
    for g, count in sorted(by_group.items()):
        print(f"  {g}: {count}")

    # Build output
    output = {
        "version": "1.0.0-COMPLETE",
        "timestamp": "2026-02-11T00:00:00Z",
        "total_classes": len(unique),
        "groups": GROUPS,
        "failures": unique,
    }

    out_path = ROOT / "src" / "data" / "failures.json"
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {len(unique)} failures to {out_path}")
    return len(unique)


if __name__ == "__main__":
    count = main()
    sys.exit(0 if count > 300 else 1)
