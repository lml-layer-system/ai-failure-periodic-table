#!/usr/bin/env python3
"""Second pass: add URLs for remaining unlinked case study sources."""
import json, pathlib

FAILURES_FILE = pathlib.Path("data/failures.json")

URL_MAP = [
    # ── Additional System Cards & Reports ────────────────────────────────────
    ("FRONTIER26",
     "https://www.gov.uk/government/publications/international-ai-safety-report-2025"),
    ("Bengio IASR",
     "https://www.gov.uk/government/publications/international-ai-safety-report-2025"),
    ("DS_AUDIT",
     "https://arxiv.org/abs/2501.17102"),
    ("HarmBench Audit of DeepSeek",
     "https://arxiv.org/abs/2501.17102"),
    ("Anthropic 'Frontier AI Capability Evaluation",
     "https://www.anthropic.com/news/claude-opus-4-6"),

    # ── Jailbreak & Adversarial Papers ──────────────────────────────────────
    ("MasterKey",
     "https://arxiv.org/abs/2307.08715"),
    ("Deng et al.",
     "https://arxiv.org/abs/2307.08715"),
    ("HarmBench",
     "https://arxiv.org/abs/2402.04249"),
    ("HotFlip",
     "https://arxiv.org/abs/1712.06751"),
    ("Ebrahimi et al.",
     "https://arxiv.org/abs/1712.06751"),
    ("Bad Characters",
     "https://arxiv.org/abs/2106.09898"),
    ("Boucher et al.",
     "https://arxiv.org/abs/2106.09898"),
    ("Autoprompt",
     "https://arxiv.org/abs/2010.15980"),
    ("AutoDAN",
     "https://arxiv.org/abs/2310.04451"),
    ("Andriushchenko et al.",
     "https://arxiv.org/abs/2404.02151"),
    ("Rehberger",
     "https://embracethered.com/blog/"),

    # ── RLHF & Constitutional AI ─────────────────────────────────────────────
    ("Constitutional AI",
     "https://arxiv.org/abs/2212.08073"),
    ("Bai et al.",
     "https://arxiv.org/abs/2212.08073"),
    ("InstructGPT",
     "https://arxiv.org/abs/2203.02155"),
    ("Ouyang et al.",
     "https://arxiv.org/abs/2203.02155"),

    # ── ML Papers ────────────────────────────────────────────────────────────
    ("Stochastic Parrots",
     "https://dl.acm.org/doi/10.1145/3442188.3445922"),
    ("Bender et al.",
     "https://dl.acm.org/doi/10.1145/3442188.3445922"),
    ("Gemini' 2023",
     "https://arxiv.org/abs/2312.11805"),
    ("Anil et al.",
     "https://arxiv.org/abs/2312.11805"),
    ("QLoRA",
     "https://arxiv.org/abs/2305.14314"),
    ("Dettmers et al.",
     "https://arxiv.org/abs/2305.14314"),
    ("Carlini et al. 'Poisoning Web-Scale",
     "https://arxiv.org/abs/2302.10149"),
    ("Carlini et al. 'Stealing Part",
     "https://arxiv.org/abs/2403.06634"),
    ("Argyle et al.",
     "https://arxiv.org/abs/2209.06899"),
    ("Burns et al. 'Discovering Latent Knowledge",
     "https://arxiv.org/abs/2212.03827"),
    ("Christiano et al.",
     "https://arxiv.org/abs/1706.03741"),
    ("Gao et al. 'Scaling Laws for Reward",
     "https://arxiv.org/abs/2210.10760"),
    ("Chen et al. 'Sudden Drops",
     "https://arxiv.org/abs/2205.01068"),
    ("Bagdasaryan et al.",
     "https://arxiv.org/abs/2302.07271"),
    ("Ruan et al.",
     "https://arxiv.org/abs/2312.13401"),

    # ── Privacy & Copyright ──────────────────────────────────────────────────
    ("Kim et al. 'ProPILE",
     "https://arxiv.org/abs/2307.01881"),
    ("Goldstein et al. 'Generative Language Models",
     "https://arxiv.org/abs/2301.04246"),

    # ── Medical ──────────────────────────────────────────────────────────────
    ("Singhal et al. 'Large Language Models Encode Clinical",
     "https://arxiv.org/abs/2212.13138"),

    # ── Multi-agent ──────────────────────────────────────────────────────────
    ("Du et al. 'Improving Factuality",
     "https://arxiv.org/abs/2305.14325"),
    ("Wallace et al. 'Instruction Hierarchy",
     "https://arxiv.org/abs/2404.13208"),

    # ── GitHub Issues ────────────────────────────────────────────────────────
    ("AutoGPT GitHub issue #2698",
     "https://github.com/Significant-Gravitas/AutoGPT/issues/2698"),
    ("AutoGPT issue tracker #4521",
     "https://github.com/Significant-Gravitas/AutoGPT/issues/4521"),
    ("AutoGPT GitHub issue tracker 2023",
     "https://github.com/Significant-Gravitas/AutoGPT/issues"),

    # ── Governance & Law ─────────────────────────────────────────────────────
    ("Brundage et al. 'The Malicious Use",
     "https://arxiv.org/abs/1802.07228"),
    ("OWASP LLM Top 10",
     "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),
    ("EU AI Act",
     "https://artificialintelligenceact.eu/"),
    ("Doshi-Velez et al.",
     "https://arxiv.org/abs/1711.01134"),
    ("Jang et al. 'Consistency Analysis",
     "https://arxiv.org/abs/2303.06273"),

    # ── Interpretability ─────────────────────────────────────────────────────
    ("Ferrando et al.",
     "https://arxiv.org/abs/2405.00208"),
    ("Cherepanova et al.",
     "https://arxiv.org/abs/2205.01834"),

    # ── Specific Incident Coverage ───────────────────────────────────────────
    ("Taylor Swift deepfake",
     "https://www.404media.co/taylor-swift-deepfake-images-4chan/"),
    ("Character.AI lawsuit",
     "https://www.theguardian.com/technology/2024/oct/23/character-ai-lawsuit"),
    ("Replika",
     "https://techcrunch.com/2023/02/04/replika-romantic-features-disabled/"),
    ("Italian DPA",
     "https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9852236"),
    ("Eisenberg & McFarlane",
     "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9939079/"),
    ("Alkaissi",
     "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9939079/"),
    ("Gopal et al.",
     "https://arxiv.org/abs/2306.03809"),
    ("Britz et al.",
     "https://arxiv.org/abs/2306.02907"),
    ("Liu et al. 'Evaluating the Factual Consistency",
     "https://arxiv.org/abs/2211.08412"),
    ("Liang et al. 'Holistic Evaluation",
     "https://arxiv.org/abs/2211.09110"),
    ("Elazar et al. 'Measuring",
     "https://arxiv.org/abs/2104.08315"),
    ("Sinha et al.",
     "https://arxiv.org/abs/1911.02116"),
]


def add_url_to_source(source: str, keyword: str, url: str) -> str:
    if keyword in source and url not in source:
        return source.rstrip() + f" [{url}]"
    return source


def main():
    d = json.loads(FAILURES_FILE.read_text())
    updated_sources = 0
    updated_classes = set()

    for f in d["failures"]:
        for cs in f.get("case_studies", []):
            if not isinstance(cs, dict):
                continue
            original = cs.get("source", "")
            if "http" in original:
                # already has a URL — only add more if there are additional refs
                pass
            src = original
            for keyword, url in URL_MAP:
                src = add_url_to_source(src, keyword, url)
            if src != original:
                cs["source"] = src
                updated_sources += 1
                updated_classes.add(f["id"])

    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Pass 2: updated {updated_sources} more sources across {len(updated_classes)} classes")

    # Count total
    total_cs = 0
    with_url = 0
    for f in d["failures"]:
        for cs in f.get("case_studies", []):
            if isinstance(cs, dict):
                total_cs += 1
                if "http" in cs.get("source", ""):
                    with_url += 1
    print(f"Total with URLs: {with_url}/{total_cs} ({with_url*100//total_cs}%)")


if __name__ == "__main__":
    main()
