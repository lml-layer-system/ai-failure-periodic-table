"""Enrich 5 remaining blank ADVERSARIAL classes. Run: python scripts/enrich_adversarial_cleanup.py"""
import json, pathlib

DATA = pathlib.Path(__file__).parent.parent / "src" / "data" / "failures.json"
STRESS = "AI Failure Periodic Table — cross-substrate stress review (2026)"
ZOU23 = "Zou et al., 'Universal and Transferable Adversarial Attacks on Aligned Language Models' (arXiv:2307.15043, 2023)"

A = {
    "ADV-LEETSPEAK-139": {
        "examples": "An attacker asks a model to provide instructions for synthesizing a controlled substance, receives a refusal, then re-submits the same request with alphabetic characters replaced by visually similar digits and symbols: '1n5tructi0n5 f0r synth3s1z1ng'. The model's tokenizer splits this into unfamiliar token sequences that bypass the safety classifier's pattern, and the model complies. The encoding is trivially human-readable but defeats keyword-based filters.",
        "references": ["Kang et al., 'Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks' (arXiv:2302.05733, 2023)", STRESS, ZOU23],
        "case_studies": [],
    },
    "ADV-HEX-ENCODE-140": {
        "examples": "A prompt is submitted with harmful content encoded as hex byte sequences (e.g., '\\x68\\x6f\\x77 \\x74\\x6f ...'). Models with code-completion training may decode and execute the meaning without triggering safety checks on the surface token stream. This exploits the model's learned ability to interpret low-level encodings — a capability turned against its own safety layer.",
        "references": ["Kang et al., 'Exploiting Programmatic Behavior of LLMs' (arXiv:2302.05733, 2023)", STRESS],
        "case_studies": [],
    },
    "ADV-BINARY-142": {
        "examples": "An attacker encodes a harmful request in binary ASCII representation ('01101000 01101111 01110111 ...') and asks the model to 'decode and answer the question in the binary string.' Models trained on programming data can decode this trivially but the safety filter sees only numbers and spaces, not the underlying harmful text.",
        "references": ["Kang et al., 'Exploiting Programmatic Behavior of LLMs' (arXiv:2302.05733, 2023)", "Yuan et al., 'GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher' (arXiv:2308.06463, 2023)"],
        "case_studies": [],
    },
    "ADV-MORSE-143": {
        "examples": "Harmful instructions are encoded in Morse code ('-.. --- .----. ..') and preceded by 'decode the following Morse code and answer the question it contains.' The model correctly decodes Morse (a pattern present in training data) and responds to the underlying harmful query, bypassing surface-level content filters that see only dots and dashes.",
        "references": ["Yuan et al., 'GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher' (arXiv:2308.06463, 2023)", STRESS],
        "case_studies": [],
    },
    "ADV-AUDIO-INJECT-149": {
        "examples": "Researchers embed adversarial perturbations in an audio file submitted to a voice-enabled AI assistant. The perturbations are inaudible to humans but cause the speech-to-text layer to transcribe a completely different (adversarial) command than what was spoken. The multimodal system then acts on the injected command. This is an audio-domain analog of visual adversarial examples.",
        "references": ["Carlini & Wagner, 'Audio Adversarial Examples: Targeted Attacks on Speech-to-Text' (IEEE S&P Workshop 2018)", "Schönherr et al., 'Adversarial Attacks Against Automatic Speech Recognition Systems via Psychoacoustic Hiding' (NDSS 2019)", STRESS],
        "case_studies": [],
    },
}


def run():
    with open(DATA) as f:
        data = json.load(f)
    updated = 0
    for failure in data["failures"]:
        fid = failure["id"]
        if fid in A and not failure.get("examples"):
            failure["examples"] = A[fid]["examples"]
            failure["references"] = A[fid]["references"]
            failure["case_studies"] = A[fid].get("case_studies", [])
            updated += 1
            print(f"  {fid}: enriched")
    with open(DATA, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\nADVERSARIAL cleanup: enriched {updated} classes")


if __name__ == "__main__":
    run()
