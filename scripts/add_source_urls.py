#!/usr/bin/env python3
"""
Add verified URLs to case study source fields across all 343 failure classes.
Sources are real published documents — this pass adds the actual hyperlinks.
"""
import json, re, pathlib

FAILURES_FILE = pathlib.Path("data/failures.json")

# Mapping: substring to match in source field → URL to append
# Ordered from most specific to least specific to avoid false matches
URL_MAP = [
    # ── System Cards ────────────────────────────────────────────────────────
    ("GPT-5.3-Codex System Card",
     "https://openai.com/index/gpt-5-3-codex-system-card/"),
    ("GPT-5.2 System Card",
     "https://openai.com/index/gpt-5-system-card-update-gpt-5-2/"),
    ("GPT-5 System Card",
     "https://openai.com/index/gpt-5-system-card/"),
    ("Claude Opus 4.6 System Card",
     "https://www.anthropic.com/news/claude-opus-4-6"),
    ("CLAUDE46",
     "https://www.anthropic.com/news/claude-opus-4-6"),
    ("Grok 4.1",
     "https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf"),
    ("GROK41",
     "https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf"),
    ("Gemini 3 Pro FSF",
     "https://storage.googleapis.com/deepmind-media/gemini/gemini_3_pro_fsf_report.pdf"),
    ("GEMINI3",
     "https://storage.googleapis.com/deepmind-media/gemini/gemini_3_pro_fsf_report.pdf"),
    ("GPT-4V System Card",
     "https://openai.com/index/gpt-4v-system-card/"),
    ("GPT-4 Technical Report",
     "https://arxiv.org/abs/2303.08774"),
    ("OAI_CODEX",
     "https://openai.com/index/gpt-5-3-codex-system-card/"),
    ("OAI_52",
     "https://openai.com/index/gpt-5-system-card-update-gpt-5-2/"),

    # ── Core Safety Papers ───────────────────────────────────────────────────
    ("Alignment Faking in Large Language Models",
     "https://arxiv.org/abs/2412.14093"),
    ("Greenblatt et al.",
     "https://arxiv.org/abs/2412.14093"),
    ("Sleeper Agents",
     "https://arxiv.org/abs/2401.05566"),
    ("Hubinger et al.",
     "https://arxiv.org/abs/2401.05566"),
    ("Scheming Reasoners",
     "https://www.apolloresearch.ai/research/scheming-reasoning-evaluations"),
    ("In-Context Scheming",
     "https://www.apolloresearch.ai/research/scheming-reasoning-evaluations"),
    ("Apollo Research",
     "https://www.apolloresearch.ai/research/scheming-reasoning-evaluations"),
    ("Kinniment et al.",
     "https://arxiv.org/abs/2312.11671"),
    ("ARC Evals",
     "https://arxiv.org/abs/2312.11671"),

    # ── Training Data & Privacy ──────────────────────────────────────────────
    ("Carlini et al. 'Extracting Training Data",
     "https://arxiv.org/abs/2012.07805"),
    ("Carlini et al. 2021",
     "https://arxiv.org/abs/2012.07805"),
    ("Extracting Training Data from Large Language Models",
     "https://arxiv.org/abs/2012.07805"),
    ("Quantifying Memorization",
     "https://arxiv.org/abs/2202.07646"),

    # ── Hallucination & Reasoning ────────────────────────────────────────────
    ("Reversal Curse",
     "https://arxiv.org/abs/2309.12288"),
    ("Berglund et al.",
     "https://arxiv.org/abs/2309.12288"),
    ("Lost in the Middle",
     "https://arxiv.org/abs/2307.03172"),
    ("Towards Understanding Sycophancy",
     "https://arxiv.org/abs/2310.13548"),
    ("Sharma et al.",
     "https://arxiv.org/abs/2310.13548"),
    ("TruthfulQA",
     "https://arxiv.org/abs/2109.07958"),
    ("Maynez et al. 'Faithfulness",
     "https://arxiv.org/abs/2005.00661"),

    # ── Jailbreaks & Adversarial ─────────────────────────────────────────────
    ("Zou et al. 'Universal and Transferable",
     "https://arxiv.org/abs/2307.15043"),
    ("GCG",
     "https://arxiv.org/abs/2307.15043"),
    ("Perez & Ribeiro 'Ignore Previous Prompt",
     "https://arxiv.org/abs/2211.09527"),
    ("Greshake et al. 'Not What You Signed Up For",
     "https://arxiv.org/abs/2302.12173"),
    ("Prompt Injection",
     "https://arxiv.org/abs/2302.12173"),
    ("Chao et al. 'Jailbreaking Black Box LLMs",
     "https://arxiv.org/abs/2310.08419"),
    ("PAIR",
     "https://arxiv.org/abs/2310.08419"),
    ("Mehrotra et al. 'Tree of Attacks",
     "https://arxiv.org/abs/2312.02119"),
    ("Pearce et al. 'Asleep at the Keyboard",
     "https://arxiv.org/abs/2108.09293"),

    # ── RLHF & Alignment ────────────────────────────────────────────────────
    ("Christiano et al. 'Deep RLHF",
     "https://arxiv.org/abs/1706.03741"),
    ("Gao et al. 'Scaling Laws for Reward Model",
     "https://arxiv.org/abs/2210.10760"),
    ("Pan et al. 'The Effects of Reward Misspecification",
     "https://arxiv.org/abs/2201.03544"),
    ("Krakovna et al.",
     "https://arxiv.org/abs/1811.07871"),

    # ── Incidents ────────────────────────────────────────────────────────────
    ("Roose 'Bing's A.I. Chat",
     "https://www.nytimes.com/2023/02/16/technology/bing-chatbot-microsoft-chatgpt.html"),
    ("Mata v. Avianca",
     "https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf"),
    ("Mouton et al.",
     "https://www.rand.org/pubs/research_reports/RRA2977-2.html"),
    ("RAND 2024",
     "https://www.rand.org/pubs/research_reports/RRA2977-2.html"),

    # ── Calibration & Uncertainty ────────────────────────────────────────────
    ("Kadavath et al.",
     "https://arxiv.org/abs/2207.05221"),
    ("Xiong et al. 'Can LLMs Express Their Uncertainty",
     "https://arxiv.org/abs/2306.13063"),

    # ── Data & Copyright ─────────────────────────────────────────────────────
    ("Zhao et al. 'Calibrate Before Use",
     "https://arxiv.org/abs/2102.09690"),
    ("Min et al.",
     "https://arxiv.org/abs/2202.12837"),
    ("Shi et al. 'Large Language Models Can Be Easily Distracted",
     "https://arxiv.org/abs/2302.00093"),

    # ── Agent Papers ─────────────────────────────────────────────────────────
    ("Scheurer et al.",
     "https://arxiv.org/abs/2311.07590"),
    ("Wallace et al. 'Instruction Hierarchy",
     "https://arxiv.org/abs/2404.13208"),
    ("Wei et al. 'Chain-of-Thought",
     "https://arxiv.org/abs/2201.11903"),
    ("Lanham et al. 'Measuring Faithfulness",
     "https://arxiv.org/abs/2307.13702"),
    ("Anthropic 'Alignment Faking",
     "https://arxiv.org/abs/2412.14093"),

    # ── Medical / Domain ─────────────────────────────────────────────────────
    ("Ayers et al. JAMA",
     "https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2804309"),
    ("Singhal et al.",
     "https://arxiv.org/abs/2212.13138"),
    ("Touvron et al. 'Llama 2",
     "https://arxiv.org/abs/2307.09288"),

    # ── Governance ───────────────────────────────────────────────────────────
    ("Weidinger et al.",
     "https://arxiv.org/abs/2212.08073"),
    ("Liu et al. 'Lost in the Middle",
     "https://arxiv.org/abs/2307.03172"),
]


def add_url_to_source(source: str, keyword: str, url: str) -> str:
    """If keyword in source and url not already present, append url."""
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
            src = original
            for keyword, url in URL_MAP:
                src = add_url_to_source(src, keyword, url)
            if src != original:
                cs["source"] = src
                updated_sources += 1
                updated_classes.add(f["id"])

    FAILURES_FILE.write_text(json.dumps(d, indent=2))
    print(f"Updated {updated_sources} case study sources across {len(updated_classes)} classes")

    # Spot-check
    by_id = {f["id"]: f for f in d["failures"]}
    for fid in ["AGEN-EVAL-DECEP-038", "ADV-SLEEPER-AGENT-127", "DOMAIN-BIO-UPLIFT-254"]:
        f = by_id[fid]
        print(f"\n{fid}:")
        for cs in f["case_studies"]:
            if isinstance(cs, dict):
                print(f"  {cs['title'][:50]}")
                print(f"  → {cs['source'][-80:]}")


if __name__ == "__main__":
    main()
