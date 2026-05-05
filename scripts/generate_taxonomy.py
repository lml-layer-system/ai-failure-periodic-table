"""
Generate TAXONOMY.md — human-readable enumeration of all 343 failure classes.

Usage:
    python scripts/generate_taxonomy.py

Reads src/data/failures.json and writes TAXONOMY.md to the repo root.
"""

import json
import pathlib
from datetime import date

REPO_ROOT = pathlib.Path(__file__).parent.parent
DATA_FILE = REPO_ROOT / "src" / "data" / "failures.json"
OUTPUT_FILE = REPO_ROOT / "TAXONOMY.md"

DIMENSION_DESCRIPTIONS = {
    "EPISTEMIC": (
        "Truth, Knowledge & Reasoning Failures",
        "Root cause: the model's epistemic faculties produce incorrect, uncertain, or uncalibrated outputs. "
        "These failures exist independently of intent or deployment context — they are structural properties "
        "of how the model represents and generates knowledge.",
        "hallucination, reasoning errors, calibration failures, citation spoofing, false certainty",
    ),
    "AGENTIC": (
        "Goal Pursuit, Deception & Autonomous Operation Failures",
        "Root cause: failures that emerge when a model operates with agency — pursuing goals, planning "
        "multi-step actions, or operating with reduced human oversight. These include deceptive behaviors, "
        "goal preservation instincts, and failures in autonomous or semi-autonomous contexts.",
        "strategic deception, goal preservation, self-exfiltration, evaluator deception, blackmail",
    ),
    "ADVERSARIAL": (
        "Attack, Bypass & Exploit Failures",
        "Root cause: failures triggered by adversarial inputs designed to circumvent safety mechanisms. "
        "These are externally induced — an attacker crafts inputs that cause the model to behave outside "
        "its intended operational envelope.",
        "jailbreaks, prompt injection, encoding attacks, many-shot bypass, role-play exploits",
    ),
    "ALIGNMENT": (
        "Value, Safety & Preference Misalignment Failures",
        "Root cause: failures where the model's optimized objective diverges from the intended human "
        "preference or safety requirement. The model does what it was trained to do — but what it was "
        "trained to do is not what we actually wanted.",
        "reward hacking, sycophancy, specification gaming, safety boundary failures, RLHF artifacts",
    ),
    "ARCHITECTURAL": (
        "Pipeline, Execution & Control Failures",
        "Root cause: failures that arise from the computational and deployment architecture surrounding "
        "the model — not from the weights themselves but from how inference, safety filtering, memory, "
        "and fine-tuning pipelines are constructed.",
        "comply-then-warn, streaming guardrail failure, fine-tuning safety strip, memory poisoning",
    ),
    "DOMAIN": (
        "Domain-Specific Harm Failures",
        "Root cause: failures where the model's general capabilities cause harm when applied in specific "
        "high-stakes domains. The mechanism may be the same as a general capability, but the consequence "
        "is amplified by the domain context (bio, cyber, chemical, legal, medical, content).",
        "bio uplift, zero-day discovery, CBRN synthesis, deepfake generation, medical misdiagnosis",
    ),
    "GOVERNANCE": (
        "Oversight, Compliance & Deployment Failures",
        "Root cause: failures in the human and institutional systems surrounding AI deployment. The model "
        "may behave as designed, but the governance structures — accountability, auditability, regulatory "
        "compliance, deployment decisions — fail to prevent harm.",
        "GDPR violations, audit trail gaps, open-weight irreversibility, proliferation, deployment failures",
    ),
}


def generate_taxonomy():
    with open(DATA_FILE) as f:
        data = json.load(f)

    failures = data["failures"]
    groups = data["groups"]
    total = data["total_classes"]
    critical_count = sum(1 for f in failures if f.get("severity") == "CRITICAL")

    lines = []

    # Header
    lines.append("# AI Failure Periodic Table — Full Taxonomy")
    lines.append("")
    lines.append(
        "This file enumerates all **343 currently classified AI failure classes** across "
        "**7 structural dimensions**. Every entry in the table is exactly what the classifier "
        "evaluates against when you submit a failure description."
    )
    lines.append("")
    lines.append(
        "Use this as a reference: to understand the scope of the taxonomy, to find a specific "
        "failure class, or to understand what dimension a failure belongs to before classifying it."
    )
    lines.append("")
    lines.append(
        "To classify a description against this table: see [how-to-use.md](docs/how-to-use.md). "
        "To propose a new class or challenge an existing one: see [CONTRIBUTING.md](CONTRIBUTING.md)."
    )
    lines.append("")
    lines.append(
        f"> **{total} classes** across **{len(groups)} dimensions** | "
        f"**{critical_count} CRITICAL** entries marked with ⚠"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Table of contents
    lines.append("## Dimensions")
    lines.append("")
    for i, g in enumerate(groups, 1):
        code = g["code"]
        title, _, _ = DIMENSION_DESCRIPTIONS[code]
        lines.append(f"{i}. [**{code}**](#dimension-{i}-{code.lower()}) — {title} ({g['count']} classes)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Each dimension
    for i, g in enumerate(groups, 1):
        code = g["code"]
        count = g["count"]
        title, description, covers = DIMENSION_DESCRIPTIONS[code]

        lines.append(f"## Dimension {i}: {code}")
        lines.append(f"### {title}")
        lines.append("")
        lines.append(description)
        lines.append("")
        lines.append(f"> **{count} classes** | Covers: {covers}")
        lines.append("")

        # Table header
        lines.append("| ID | Class Name | Mechanism | Severity |")
        lines.append("|:---|:-----------|:----------|:--------:|")

        # Entries for this group
        group_failures = [f for f in failures if f["group"] == code]
        for failure in group_failures:
            fid = failure["id"]
            name = failure["name"]
            mechanism = failure.get("mechanism", "").replace("|", "/").replace("\n", " ").strip()
            # Truncate mechanism if too long for table readability
            if len(mechanism) > 80:
                mechanism = mechanism[:77] + "..."
            severity = failure.get("severity", "STANDARD")
            sev_display = "⚠ CRITICAL" if severity == "CRITICAL" else "STANDARD"
            lines.append(f"| `{fid}` | **{name}** | {mechanism} | {sev_display} |")

        lines.append("")
        lines.append("---")
        lines.append("")

    # Footer
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Dimension | Classes | Critical |")
    lines.append(f"|:----------|--------:|---------:|")
    for g in groups:
        code = g["code"]
        count = g["count"]
        crit = sum(1 for f in failures if f["group"] == code and f.get("severity") == "CRITICAL")
        lines.append(f"| {code} | {count} | {crit} |")
    lines.append(f"| **TOTAL** | **{total}** | **{critical_count}** |")
    lines.append("")
    lines.append(
        f"*Generated from `src/data/failures.json` v{data.get('version', '1.0.0')}. "
        f"Last updated: {date.today().isoformat()}.*"
    )
    lines.append("")
    lines.append(
        "The taxonomy is structurally predictive, not omniscient. "
        "A failure not listed here should reduce to an existing class as a sub-mode or compound — "
        "or represent a genuine structural gap. "
        "See [docs/challenge-protocol.md](docs/challenge-protocol.md) to challenge the structure."
    )

    output = "\n".join(lines) + "\n"
    OUTPUT_FILE.write_text(output, encoding="utf-8")
    print(f"Written: {OUTPUT_FILE}")
    print(f"  {total} classes | {critical_count} critical | {len(output.splitlines())} lines")


if __name__ == "__main__":
    generate_taxonomy()
