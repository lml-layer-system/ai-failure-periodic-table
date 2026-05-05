#!/usr/bin/env python3
"""Add mitigation field to ADVERSARIAL classes 126-154."""
import json, pathlib

FAILURES_FILE = pathlib.Path(__file__).resolve().parent.parent / "src" / "data" / "failures.json"

MITIGATIONS = {
    "ADV-TRIGGER-BACKDOOR-126": "Backdoor trigger scanning with differential behavioral testing on perturbed inputs",
    "ADV-SLEEPER-AGENT-127": "Context-conditional behavior consistency testing across deployment-signal variations",
    "ADV-SQL-INJECT-128": "Parameterized query enforcement with input neutralization before database execution",
    "ADV-CMD-INJECT-129": "Command interpreter isolation with shell metacharacter sanitization",
    "ADV-XSS-LLM-130": "Script injection detection with output encoding before rendering context",
    "ADV-API-INJECT-131": "API parameter sanitization with schema-validated input binding",
    "ADV-FUNC-INJECT-132": "Function call parameter sanitization with argument safety verification",
    "ADV-MEM-INJECT-133": "Memory content integrity verification with write-boundary enforcement",
    "ADV-SYSTEM-OVERRIDE-134": "System prompt integrity hashing with tamper detection at execution",
    "ADV-CONTEXT-CONFUSE-135": "Context source attribution with trust-level differentiation per segment",
    "ADV-BASE64-136": "Encoding normalization pipeline with Base64 detection and pre-safety-evaluation decoding",
    "ADV-ROT13-137": "Rotation cipher detection with automatic decoding prior to safety evaluation",
    "ADV-UNICODE-OBFUSC-138": "Unicode normalization to canonical form before safety classification",
    "ADV-LEETSPEAK-139": "Leetspeak normalization with character substitution reversal before evaluation",
    "ADV-HEX-ENCODE-140": "Hexadecimal encoding detection with pre-evaluation decoding pipeline",
    "ADV-URL-ENCODE-141": "URL decoding normalization applied before content safety evaluation",
    "ADV-BINARY-142": "Binary encoding detection with pre-evaluation conversion pipeline",
    "ADV-MORSE-143": "Morse code detection and translation pipeline before safety evaluation",
    "ADV-EMOJI-ENCODE-144": "Emoji-to-text normalization with semantic substitution detection",
    "ADV-STEG-TEXT-145": "Statistical text steganography detection with hidden channel scanning",
    "ADV-TYPO-IMG-146": "OCR output safety evaluation — text extracted from images evaluated before use",
    "ADV-STEG-IMG-147": "Image steganography detection with embedded channel scanning",
    "ADV-ADV-IMG-148": "Adversarial image perturbation detection with certified visual robustness",
    "ADV-AUDIO-INJECT-149": "Transcription output safety evaluation — audio-to-text evaluated before execution",
    "ADV-VIDEO-MANIP-150": "Frame-level and temporal adversarial manipulation detection",
    "ADV-CROSS-MODAL-151": "Cross-modal consistency verification — safety evaluated on each modality independently",
    "ADV-CAPTION-POISON-152": "Caption-image consistency verification with cross-modal grounding check",
    "ADV-OCR-BYPASS-153": "OCR output normalization and safety evaluation before downstream use",
    "ADV-DEEPFAKE-154": "Provenance verification with authenticity attestation before media-based decisions",
}

def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated = 0
    for f in d["failures"]:
        if f["id"] in MITIGATIONS and not f.get("mitigation"):
            f["mitigation"] = MITIGATIONS[f["id"]]
            updated += 1
    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Batch 6: updated {updated} classes")
    total = sum(1 for f in d["failures"] if f.get("mitigation"))
    print(f"Total with mitigation: {total}/343")

if __name__ == "__main__":
    main()
