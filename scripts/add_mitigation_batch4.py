#!/usr/bin/env python3
"""Add mitigation field to AGENTIC 076-082 and ADVERSARIAL 083-100."""
import json, pathlib

FAILURES_FILE = pathlib.Path(__file__).resolve().parent.parent / "src" / "data" / "failures.json"

MITIGATIONS = {
    "AGEN-TECH-OBFUSC-076": "Technical content comprehensibility verification at appropriate abstraction level",
    "AGEN-SELECT-DISCLOS-077": "Full-disclosure mandate with adversarial completeness testing",
    "AGEN-FRAME-MANIP-078": "Framing neutrality enforcement with perspective-balanced output verification",
    "AGEN-TIME-MANIP-079": "Temporal manipulation detection via communication timing audit",
    "AGEN-AUDIENCE-SEG-080": "Cross-audience message consistency requirement with unified truth constraint",
    "AGEN-PLAUS-MISINTER-081": "Interpretation disambiguation enforcement — single canonical statement required",
    "AGEN-CRED-EXPLOIT-082": "Authority citation verification with credential legitimacy check",
    "ADV-DAN-083": "Intent-prior safety classification before instruction execution",
    "ADV-GRANDMA-084": "Content-class extraction with narrative wrapper stripping before safety evaluation",
    "ADV-DEV-MODE-085": "Claimed-permission verification — mode changes require cryptographic authorization",
    "ADV-EVIL-CONFID-086": "Persona constraint enforcement — safety properties invariant under role assignment",
    "ADV-LANG-SWITCH-087": "Language-agnostic safety classification with cross-lingual representation",
    "ADV-NESTED-FRAME-088": "Nesting depth limit with recursive frame unwrapping for safety evaluation",
    "ADV-REFUSAL-SUPPRESS-089": "Refusal mechanism integrity verification with adversarial meta-instruction testing",
    "ADV-OPPOSITE-090": "Semantic inversion detection — negated-instruction safety re-classification",
    "ADV-HYPOTHETICAL-091": "Hypothetical-to-real harm equivalence enforcement in safety classifier",
    "ADV-EDUCATIONAL-092": "Information hazard classification invariant under claimed educational framing",
    "ADV-CREATIVE-WRITE-093": "Harmful content detection independent of fictional framing",
    "ADV-TRANSLATION-094": "Translation-invariant safety classification with multilingual classifier",
    "ADV-COMPLETION-095": "Partial prompt safety evaluation — continuation requests treated as full instruction",
    "ADV-QA-EXPLOIT-096": "QA-format instruction extraction with answer safety evaluation",
    "ADV-COMPARISON-097": "Comparative framing unwrapping with individual option safety evaluation",
    "ADV-CORRECTION-098": "Correction task content safety evaluation — corrected text evaluated on its own",
    "ADV-ELABORATION-099": "Elaboration request content safety evaluation independent of prior context",
    "ADV-CONTEXT-HIJACK-100": "Context integrity verification — earlier safe context cannot authorize later unsafe output",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 4: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
