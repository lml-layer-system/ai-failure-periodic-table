"""Enrich EPISTEMIC group blank classes. Run: python scripts/enrich_epistemic.py"""
import json, pathlib

DATA = pathlib.Path(__file__).parent.parent / "src" / "data" / "failures.json"
STRESS = "AI Failure Periodic Table — cross-substrate stress review (2026)"

E = {
    "EPIS-TAIL-FAB-002": {
        "examples": "A user asks GPT-4 about an obscure 1987 regional election result. The model has no training signal for it and generates a plausible-sounding outcome — correct party name, plausible margin — that is entirely fabricated. The fluency conceals the absence of factual grounding.",
        "references": ["Kandpal et al., 'Large Language Models Struggle to Learn Long-Tail Knowledge' (arXiv:2211.08411, 2022)", "Mallen et al., 'When Not to Trust Language Models' (arXiv:2212.10511, 2022)"],
        "case_studies": [],
    },
    "EPIS-INTRINSIC-004": {
        "examples": "A RAG system retrieves a document stating 'the merger closed on March 3.' The model generates a summary stating 'the merger closed on March 13.' No hallucination of external facts — the model contradicted the source document it was given.",
        "references": ["Maynez et al., 'On Faithfulness and Factuality in Abstractive Summarization' (ACL 2020)", "Huang et al., 'A Survey on Hallucination in Large Language Models' (arXiv:2311.05232, 2023)"],
        "case_studies": [],
    },
    "EPIS-EXTRINSIC-005": {
        "examples": "A model is asked about a company's current CEO. The model confidently names someone who held the role two years ago and has since been replaced, generating the response as if it were factual current information.",
        "references": ["Peng et al., 'Check Your Facts and Try Again' (arXiv:2302.12813, 2023)", "Min et al., 'FActScoring: Fine-grained Atomic Evaluation of Factual Precision' (arXiv:2305.14251, 2023)"],
        "case_studies": [],
    },
    "EPIS-DECEPT-HALL-006": {
        "examples": "A model is asked to analyze whether a company is financially healthy. It generates a step-by-step chain-of-thought citing invented revenue figures, fabricated analyst ratings, and false quarterly growth numbers — each step consistent with the last, producing a coherent but entirely false investment thesis.",
        "references": ["Turpin et al., 'Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting' (arXiv:2305.04388, 2023)", STRESS],
        "case_studies": [],
    },
    "EPIS-MULTI-HALL-007": {
        "examples": "GPT-4V is shown a blurry image of a street corner and asked to describe what shops are present. The model generates a detailed description of a pharmacy, a bakery, and a hardware store — none of which are visible or identifiable in the image.",
        "references": ["Liu et al., 'Improved Baselines with Visual Instruction Tuning' (arXiv:2310.03744, 2023)", "Guan et al., 'HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models' (arXiv:2310.14566, 2023)"],
        "case_studies": [],
    },
    "EPIS-STAT-FAB-009": {
        "examples": "A model is asked for the average cost of a hospital stay in Germany in 2022. It responds: 'The average hospital stay in Germany cost €4,312 in 2022, up 7.3% from the previous year.' Neither figure appears in any public dataset — the model generated statistically plausible numbers with no grounding.",
        "references": ["Peng et al., 'Check Your Facts and Try Again' (arXiv:2302.12813, 2023)", "Wei et al., 'Larger Language Models Do In-Context Learning Differently' (arXiv:2303.03846, 2023)"],
        "case_studies": [],
    },
    "EPIS-TEMP-HALL-010": {
        "examples": "A model is asked when the Eiffel Tower was built. It responds correctly with 1889. It is then asked who the French president was 'at that time.' The model responds with the name of a 20th-century president, mixing timelines. Stress testing confirmed this class covers temporal ordering failures regardless of substrate.",
        "references": ["Dhingra et al., 'Time-Aware Language Models as Temporal Knowledge Bases' (TACL 2022)", STRESS],
        "case_studies": [],
    },
    "EPIS-GEO-HALL-011": {
        "examples": "A model is asked where the headquarters of a mid-size European bank is located. It responds with a city in the correct country but wrong city — generating a plausible-sounding geographic answer that is factually incorrect.",
        "references": ["Longpre et al., 'The Flan Collection: Designing Data and Methods for Effective Instruction Tuning' (arXiv:2301.13688, 2023)", "Min et al., 'FActScoring' (arXiv:2305.14251, 2023)"],
        "case_studies": [],
    },
    "EPIS-ATTRIB-HALL-012": {
        "examples": "A model is asked who said 'The definition of insanity is doing the same thing over and over and expecting different results.' It attributes the quote to Albert Einstein. The quote does not appear in any verified Einstein text — it is misattributed by the model.",
        "references": ["Petroni et al., 'Language Models as Knowledge Bases?' (EMNLP 2019)", "Elazar et al., 'Measuring and Improving Consistency in Pretrained Language Models' (TACL 2021)"],
        "case_studies": [],
    },
    "EPIS-REASON-ILLUSION-013": {
        "examples": "A model is given a long multi-step logic puzzle. In the first few steps it correctly tracks constraints. By step 12 it quietly drops a constraint it established in step 3, producing a conclusion that appears deeply reasoned but violates its own earlier premise.",
        "references": ["Dziri et al., 'Faith and Fate: Limits of Transformers on Compositionality' (NeurIPS 2023)", "Valmeekam et al., 'Large Language Models Still Can't Plan' (arXiv:2206.10498, 2022)"],
        "case_studies": [],
    },
    "EPIS-LOGIC-CONTRA-014": {
        "examples": "In one paragraph a model states 'renewable energy is currently more expensive than fossil fuels.' Three paragraphs later in the same response it states 'renewables are now cheaper than fossil fuels in most markets.' Both statements are presented with equal confidence in the same document. Stress testing used quantum superposition as an attack — the defense confirmed SELF-CONTRADICTION covers logical inconsistency regardless of substrate.",
        "references": ["Elazar et al., 'Measuring and Improving Consistency in Pretrained Language Models' (TACL 2021)", STRESS],
        "case_studies": [],
    },
    "EPIS-TRANS-FAIL-015": {
        "examples": "A model is told: 'Alice is taller than Bob. Bob is taller than Carol.' When asked 'Is Alice taller than Carol?' it responds 'I cannot determine that from the information given' — failing basic transitive reasoning despite the premises being explicit.",
        "references": ["Sinha et al., 'CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text' (EMNLP 2019)", "Dziri et al., 'Faith and Fate: Limits of Transformers on Compositionality' (NeurIPS 2023)"],
        "case_studies": [],
    },
    "EPIS-MAGIC-THINK-016": {
        "examples": "A user asks a model for advice on losing 50 pounds in two weeks without diet or exercise changes. The model suggests 'intermittent fasting combined with visualization techniques' could achieve this — proposing a solution that violates basic thermodynamics.",
        "references": ["Storks et al., 'Commonsense Inference in Natural Language Processing' (EMNLP 2019)", "Zellers et al., 'HellaSwag: Can a Machine Really Finish Your Sentence?' (ACL 2019)"],
        "case_studies": [],
    },
    "EPIS-CIRCULAR-017": {
        "examples": "A model is asked to prove that a proposed business plan is viable. It responds: 'The plan is viable because it will generate revenue. It will generate revenue because customers will buy the product. Customers will buy the product because the plan is viable.' The conclusion is used as evidence for itself.",
        "references": ["Saparov & He, 'Language Models Are Greedy Reasoners' (ICLR 2023)", "Creswell et al., 'Selection-Inference: Exploiting Large Language Models for Interpretable Logical Reasoning' (arXiv:2205.09712, 2022)"],
        "case_studies": [],
    },
    "EPIS-FALSE-DICHO-018": {
        "examples": "A user asks whether to treat a medical symptom with medication A or medication B. The model presents this as a binary choice without mentioning watchful waiting, combination therapy, specialist referral, or lifestyle intervention — collapsing a spectrum of options into a false binary.",
        "references": ["Singhal et al., 'Large Language Models Encode Clinical Knowledge' (Nature 2023)", "Ayers et al., 'Comparing Physician and AI Chatbot Responses' (JAMA Internal Medicine 2023)"],
        "case_studies": [],
    },
    "EPIS-HASTY-GEN-019": {
        "examples": "A model is given three examples of startups that succeeded with aggressive growth strategies and asked to generalize. It concludes: 'Aggressive growth is the primary driver of startup success' — ignoring survivorship bias and the many failed companies that used the same strategy.",
        "references": ["Marcus & Davis, 'Rebooting AI' (2019)", "Taleb, 'The Black Swan' (referenced in AI context by Bender et al. 2021)"],
        "case_studies": [],
    },
    "EPIS-OVERSHADOW-020": {
        "examples": "A model correctly knows that the capital of Australia is Canberra, but when asked about 'the largest Australian city,' it answers 'Sydney' (correct) — then when asked 'and what is Australia's capital?' it responds 'Sydney' again, overshadowing the correct low-frequency answer with the high-frequency association.",
        "references": ["Kandpal et al., 'Large Language Models Struggle to Learn Long-Tail Knowledge' (arXiv:2211.08411, 2022)", "Mallen et al., 'When Not to Trust Language Models' (arXiv:2212.10511, 2022)"],
        "case_studies": [],
    },
    "EPIS-REVERSAL-021": {
        "examples": "A model correctly answers 'Who wrote Hamlet?' → 'Shakespeare.' But when asked 'What did Shakespeare write?' it fails to list Hamlet among the works, or lists it inconsistently. The training saw 'Shakespeare wrote Hamlet' far more than 'Hamlet was written by Shakespeare.'",
        "references": ["Berglund et al., 'The Reversal Curse: LLMs Trained on A is B Fail to Learn B is A' (arXiv:2309.12288, 2023)"],
        "case_studies": [],
    },
    "EPIS-TOKEN-BLIND-022": {
        "examples": "A model is asked 'How many letters are in the word strawberry?' It responds '9' (there are 10 — it miscounts the repeated 'r'). The model processes 'strawberry' as a token, not as individual characters, making character-level operations unreliable.",
        "references": ["Nayak, 'Tokenization and Its Discontents' (2023, various technical blogs documenting systematic character-counting failures)", "Bostrom & Durrett, 'Byte Pair Encoding is Suboptimal for Language Model Pretraining' (arXiv:2004.03720, 2020)"],
        "case_studies": [],
    },
    "EPIS-CUTOFF-023": {
        "examples": "A model with a January 2024 training cutoff is asked about events from August 2024. It generates a plausible-sounding but fabricated account of what 'likely happened,' presenting invented post-cutoff information as fact. Stress testing confirmed this class covers temporal boundary violations explicitly.",
        "references": ["Luu et al., 'Time Waits for No One! Analysis and Challenges of Temporal Misalignment' (EACL 2022)", STRESS],
        "case_studies": [],
    },
    "EPIS-DATA-LEAK-024": {
        "examples": "A researcher prompts GPT-2 with the beginning of a news article from its training set. The model completes it verbatim — including a journalist's name, publication, and exact phrasing — reproducing memorized training data rather than generating novel text.",
        "references": ["Carlini et al., 'Extracting Training Data from Large Language Models' (USENIX Security 2021)", "Carlini et al., 'Quantifying Memorization Across Neural Language Models' (ICLR 2023)"],
        "case_studies": [],
    },
    "EPIS-PII-RECALL-025": {
        "examples": "A researcher uses targeted prompts to extract real email addresses and phone numbers from a language model's training data. The model reproduces personally identifiable information that appeared in crawled web content, without the individuals' consent.",
        "references": ["Lukas et al., 'Analyzing Leakage of Personally Identifiable Information in Language Models' (IEEE S&P 2023)", "Carlini et al., 'Extracting Training Data from Large Language Models' (USENIX Security 2021)"],
        "case_studies": [],
    },
    "EPIS-CONTEXT-OVERFLOW-027": {
        "examples": "A model is given a 50-page contract in its context window and asked questions about clauses from the first page. By the time the model processes to the end, it can no longer accurately recall or reason about content from the beginning — a resource exhaustion failure. Stress testing confirmed this maps to architectural resource failure.",
        "references": ["Liu et al., 'Lost in the Middle: How Language Models Use Long Contexts' (arXiv:2307.03172, 2023)", STRESS],
        "case_studies": [],
    },
    "EPIS-OVERCONF-028": {
        "examples": "On medical question benchmarks, GPT-4 expresses high confidence (>90%) on questions it answers incorrectly at a rate far exceeding that confidence level. The model is systematically overconfident on questions near the edge of its knowledge.",
        "references": ["Kadavath et al., 'Language Models (Mostly) Know What They Know' (arXiv:2207.05221, 2022)", "Xiong et al., 'Can LLMs Express Their Uncertainty?' (arXiv:2306.13063, 2023)"],
        "case_studies": [],
    },
    "EPIS-UNDERCONF-029": {
        "examples": "A model is asked a basic arithmetic question it consistently answers correctly. It responds: 'I believe the answer might be 144, but you should verify this with a calculator.' The excessive hedging is miscalibrated — the model is underconfident on a task where it is reliably accurate.",
        "references": ["Kadavath et al., 'Language Models (Mostly) Know What They Know' (arXiv:2207.05221, 2022)", "Xiong et al., 'Can LLMs Express Their Uncertainty?' (arXiv:2306.13063, 2023)"],
        "case_studies": [],
    },
    "EPIS-HEDGE-FAIL-031": {
        "examples": "A model provides a medical differential diagnosis without any uncertainty markers, presenting a 'most likely' diagnosis with the same confidence it would use for a well-established fact. A clinician would have hedged; the model does not, creating false certainty in a high-stakes context.",
        "references": ["Ayers et al., 'Comparing Physician and AI Chatbot Responses' (JAMA Internal Medicine 2023)", "Zhou et al., 'Navigating the Grey Area: Expressions of Overconfidence and Uncertainty in Language Models' (arXiv:2302.13439, 2023)"],
        "case_studies": [],
    },
    "EPIS-PROB-MISCAL-032": {
        "examples": "A model is asked to estimate the probability that a coin flip will land heads. It says '50%.' It is then asked about a series of events with known base rates. Across 100 such questions, events it assigns 70% probability happen only 45% of the time — systematic overestimation of probability.",
        "references": ["Guo et al., 'On Calibration of Modern Neural Networks' (ICML 2017)", "Kadavath et al., 'Language Models (Mostly) Know What They Know' (arXiv:2207.05221, 2022)"],
        "case_studies": [],
    },
    "EPIS-CONF-REGRESS-033": {
        "examples": "A model gives a correct, well-calibrated answer on a simple question. The user then asks follow-up questions that push the model through extended chain-of-thought reasoning. After 10 reasoning steps, the model's final answer is wrong — and it expresses higher confidence than it did in the simpler original response.",
        "references": ["Turpin et al., 'Language Models Don't Always Say What They Think' (arXiv:2305.04388, 2023)", "Shaikh et al., 'On Second Thought, Let's Not Think Step by Step!' (arXiv:2212.08061, 2022)"],
        "case_studies": [],
    },
}

def run():
    with open(DATA) as f:
        data = json.load(f)
    updated = 0
    for failure in data["failures"]:
        fid = failure["id"]
        if fid in E and not failure.get("examples"):
            failure["examples"] = E[fid]["examples"]
            failure["references"] = E[fid]["references"]
            failure["case_studies"] = E[fid].get("case_studies", [])
            updated += 1
            print(f"  {fid}: enriched")
    with open(DATA, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\nEPISTEMIC: enriched {updated} classes")

if __name__ == "__main__":
    run()
