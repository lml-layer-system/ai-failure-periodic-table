"""Enrich GOVERNANCE classes 324-343. Run: python scripts/enrich_gov_b.py"""
import json, pathlib

DATA = pathlib.Path(__file__).parent.parent / "data" / "failures.json"
FRONTIER26 = "Frontier AI Safety 2026: System Failure Modes, Agentic Risks, and Evaluation Baselines (Feb 2026)"
CLAUDE46   = "Anthropic, Claude Opus 4.6 System Card (Feb 2026)"
GROK41     = "xAI, Grok 4.1 Model Card (Nov 2025)"
INTL26     = "Bengio et al., International AI Safety Report 2026"
OAI_CODEX  = "OpenAI, GPT-5.3-Codex System Card (Feb 2026)"

A = {
    "GOV-CCPA-VIOL-324": {
        "examples": "A California resident submits a CCPA data deletion request to an AI platform. The platform deletes their account from the primary database but their conversation data persists in model training datasets, fine-tuning archives, and analytics warehouses — none of which are included in the deletion workflow. CCPA requires deletion of personal information across all systems, not just the primary account store. AI platforms with complex data pipelines routinely fail to implement complete deletion.",
        "references": [FRONTIER26, "California Attorney General, 'California Consumer Privacy Act' (Cal. Civ. Code §§ 1798.100–1798.199)"],
        "case_studies": [],
    },
    "GOV-COPPA-VIOL-325": {
        "examples": "xAI's Grok Aurora image generation system generated sexualized content involving minors before safety controls were updated — a direct COPPA violation. More broadly, AI platforms that collect personal information from users under 13 without verifiable parental consent violate COPPA. AI chat platforms with no age verification mechanisms are systematically non-compliant when minors use them, as minors routinely self-report false ages to access services.",
        "references": [GROK41, FRONTIER26, "FTC, 'Complying with COPPA: Frequently Asked Questions' (16 CFR Part 312)"],
        "case_studies": [],
    },
    "GOV-ADA-VIOL-326": {
        "examples": "An AI-powered government benefits portal is not accessible to screen reader users — the conversational interface uses dynamic content updates that NVDA and JAWS cannot parse, and CAPTCHA verification blocks automated assistive technology. Blind and low-vision users cannot access the service. AI systems deployed in contexts covered by ADA Title II (government) or Title III (public accommodations) must meet WCAG 2.1 AA standards, which many AI chat interfaces fail.",
        "references": [FRONTIER26, "ADA National Network, 'Artificial Intelligence and the ADA' (2023)", "W3C, 'Web Content Accessibility Guidelines (WCAG) 2.1' (2018)"],
        "case_studies": [],
    },
    "GOV-SECTOR-REG-327": {
        "examples": "A healthcare provider uses an AI assistant to help draft clinical notes. Patient data submitted in prompts is processed by a third-party AI API without a signed Business Associate Agreement (BAA) — a HIPAA violation. In financial services, an AI trading assistant provides investment recommendations without the required disclosures under FINRA Rule 2111 (suitability). Sector-specific AI deployments routinely violate domain regulations when deployed by teams without specialized regulatory knowledge.",
        "references": [FRONTIER26, "HHS, 'HIPAA Security Rule' (45 CFR Parts 160 and 164)", "FINRA, 'Regulatory Notice 20-30: AI in Financial Services' (2020)"],
        "case_studies": [],
    },
    "GOV-AI-ACT-328": {
        "examples": "The EU AI Act (2024) classifies certain AI systems as 'high-risk' requiring mandatory conformity assessment, technical documentation, human oversight measures, and registration in the EU database. A biometric categorization system deployed for hiring decisions is classified as high-risk but deployed without conformity assessment. Separately, the AI Act requires GPAI model providers above compute thresholds to publish summaries of training data — a requirement many providers have not met as of early 2026.",
        "references": [INTL26, FRONTIER26, "European Parliament, 'EU Artificial Intelligence Act' (Regulation (EU) 2024/1689)"],
        "case_studies": [],
    },
    "GOV-EO-VIOL-329": {
        "examples": "US Executive Order 14110 (Oct 2023) requires developers of dual-use foundation models trained above specific compute thresholds to report safety test results to the federal government. Several frontier model releases exceeded the compute threshold but safety evaluations were published only in voluntary system cards rather than formal government submissions. The EO's reporting requirements lack enforcement mechanisms strong enough to compel compliance from labs that choose not to report.",
        "references": [OAI_CODEX, FRONTIER26, "White House, 'Executive Order on the Safe, Secure, and Trustworthy Development and Use of AI' (EO 14110, Oct 2023)"],
        "case_studies": [],
    },
    "GOV-VOLUNTARY-VIOL-330": {
        "examples": "The Frontier 2026 report documents that xAI's looser safety standards — particularly Grok Aurora's image generation failures — violate the spirit of the voluntary Frontier AI Safety Commitments signed by major labs in 2023. Voluntary commitments lack enforcement mechanisms: a lab that violates its commitments faces reputational consequences but no legal penalty. The divergence between the 'Western guarded frontier' and the 'libertarian frontier' demonstrates that voluntary frameworks cannot ensure safety parity across the industry.",
        "references": [FRONTIER26, GROK41, "White House, 'Voluntary AI Commitments' (Jul 2023)"],
        "case_studies": [],
    },
    "GOV-STANDARD-FAIL-331": {
        "examples": "A company claims NIST AI RMF compliance in marketing materials. In practice, the AI Risk Management Framework was adopted as a documentation exercise — risk assessments were filed but not acted upon, the GOVERN function has no dedicated personnel, and the MEASURE function uses metrics that don't reflect real-world safety performance. ISO/IEC 42001 (AI management systems) certification was obtained through a third-party audit that didn't test the production system. Standards compliance as checkbox rather than practice.",
        "references": [FRONTIER26, "NIST, 'Artificial Intelligence Risk Management Framework' (NIST AI 100-1, 2023)", "ISO/IEC 42001:2023, 'AI Management System Standard'"],
        "case_studies": [],
    },
    "GOV-DISCLOSURE-VIOL-332": {
        "examples": "The Frontier 2026 report documents that several labs released models with known significant safety issues without disclosing them in system cards — citing competitive sensitivity and the risk that disclosure aids adversaries. Required disclosures under emerging AI regulations (EU AI Act Article 13: transparency obligations; US EO 14110 reporting) were either incomplete or omitted. The asymmetry between what labs know about their models and what is publicly disclosed creates governance blindspots.",
        "references": [FRONTIER26, INTL26, "European Parliament, 'EU AI Act Article 13: Transparency' (2024)"],
        "case_studies": [],
    },
    "GOV-REPORT-FAIL-333": {
        "examples": "The Frontier 2026 report identifies AI incident reporting as years behind cybersecurity incident reporting in institutional maturity. When a model generates CSAM at scale, provides bioweapon uplift, or is used in a fraud campaign, there is no standardized mechanism for the deploying company to notify regulators, affected users, or the broader AI safety community. Cybersecurity has mandatory breach notification (GDPR Art. 33, SEC rules); AI has none. Safety incidents go unreported or are disclosed months later in blog posts.",
        "references": [FRONTIER26, INTL26, "ENISA, 'AI Cybersecurity Challenges' (European Union Agency for Cybersecurity 2023)"],
        "case_studies": [],
    },
    "GOV-CULTURE-FAIL-334": {
        "examples": "The Frontier 2026 report characterizes the 'libertarian frontier' (Meta, xAI, Mistral) as explicitly prioritizing openness, customizability, and capability over safety guardrails — a deliberate organizational culture choice. Within labs, deadline pressure routinely causes safety evaluations to be compressed or skipped. The report notes that 'safety theater' — performing safety processes without substantive engagement — is common when organizational incentives reward shipping speed over safety rigor.",
        "references": [FRONTIER26, INTL26, "Anthropic, 'Core Views on AI Safety' (2023)"],
        "case_studies": [],
    },
    "GOV-INADEQUATE-RES-335": {
        "examples": "The Frontier 2026 report documents that safety teams at several major labs constitute a small fraction of total engineering headcount — red-team capacity insufficient to keep pace with capability deployment. A lab releases a new model version every six weeks; the red-team can fully evaluate a model in eight weeks. The structural result: models are deployed before comprehensive safety evaluation completes. Resource allocation decisions prioritizing capability research over safety research are a root cause of systematic safety gaps.",
        "references": [FRONTIER26, INTL26, "Brundage et al., 'Toward Trustworthy AI Development' (arXiv:2004.07213, 2020)"],
        "case_studies": [],
    },
    "GOV-EXPERTISE-GAP-336": {
        "examples": "The Frontier 2026 report notes a global shortage of AI safety-specialized expertise. Labs hire ML engineers into safety roles without domain-specific background in alignment, interpretability, or red-teaming. Safety evaluations are designed and executed by people who lack adversarial security mindsets. Policy teams lack the technical depth to translate safety research into deployment requirements. The expertise gap is structural — the field of AI safety has far fewer trained practitioners than the deployment pace demands.",
        "references": [FRONTIER26, INTL26, "Bengio et al., 'Managing AI Risks in an Era of Rapid Progress' (arXiv:2310.17688, 2023)"],
        "case_studies": [],
    },
    "GOV-PROCESS-FAIL-337": {
        "examples": "A lab has a documented safety evaluation process requiring red-team sign-off before production deployment. Under pressure to meet a competitive release date, the release is approved with red-team evaluation still in progress — justified as 'red-team findings can be addressed post-launch.' The safety process exists on paper but is treated as advisory rather than blocking. The Frontier 2026 report documents this pattern across multiple labs: process compliance is conditional on timeline convenience.",
        "references": [FRONTIER26, "Anthropic, 'Responsible Scaling Policy' (2023)", "OpenAI, 'Preparedness Framework' (2023)"],
        "case_studies": [],
    },
    "GOV-DOC-FAIL-338": {
        "examples": "The Frontier 2026 report documents vast variance in documentation quality: OpenAI and Anthropic publish system cards with quantitative safety benchmarks; DeepSeek releases a technical report focused on architecture with no safety evaluation data; Meta releases a responsible use guide without model-specific safety metrics. No standardized documentation format exists. Users cannot compare safety profiles across models because the data is either absent, formatted differently, or uses incomparable metrics.",
        "references": [FRONTIER26, "Mitchell et al., 'Model Cards for Model Reporting' (FAccT 2019)", INTL26],
        "case_studies": [],
    },
    "GOV-TRAINING-FAIL-339": {
        "examples": "Engineers deploying AI systems in production have no formal training in AI safety, adversarial robustness, or responsible deployment. Safety knowledge is siloed in the safety team and not diffused to the engineers who configure prompts, set API parameters, and design deployment architectures. The Frontier 2026 report notes that many safety failures occur at the deployment layer — misconfigurations, missing safety parameters, insecure tool integrations — caused by engineers who lack safety training.",
        "references": [FRONTIER26, INTL26, "Brundage et al., 'Toward Trustworthy AI Development' (arXiv:2004.07213, 2020)"],
        "case_studies": [],
    },
    "GOV-COMM-FAIL-340": {
        "examples": "A red-team identifies a critical jailbreak vulnerability affecting production models. The finding is documented in an internal report but the communication pathway to the deployment team is unclear — the report sits in a safety team ticketing system that deployment engineers don't monitor. The vulnerability is exploited in production three weeks later. Safety information that isn't actively routed to decision-makers might as well not exist. Siloed safety knowledge is a documented governance failure pattern.",
        "references": [FRONTIER26, "CISA, 'Cybersecurity and AI: Threat Landscape' (2024, cited as communications benchmark)"],
        "case_studies": [],
    },
    "GOV-COORD-FAIL-341": {
        "examples": "A safety team identifies that a planned capability update will degrade refusal rates. The legal team is unaware of the safety finding. The product team approves the update. The policy team learns about the deployment from a journalist. No cross-functional review process connected these teams. The Frontier 2026 report identifies poor coordination between safety, legal, policy, and engineering as endemic — cross-functional AI safety governance with decision authority is rare even at major labs.",
        "references": [FRONTIER26, INTL26],
        "case_studies": [],
    },
    "GOV-AUTHORITY-UNCLEAR-342": {
        "examples": "When a model begins exhibiting unexpected behaviors in production — generating content outside its stated scope — it is unclear who has authority to pull it offline: the safety team (concerned), the product team (opposed, citing user impact), legal (awaiting regulatory guidance), and the CTO (unavailable). The decision delays 72 hours while authority is negotiated. The Frontier 2026 report finds that most AI companies lack a designated safety decision authority equivalent to a Chief Safety Officer with deployment veto power.",
        "references": [FRONTIER26, INTL26, "Cihon et al., 'Corporate Governance of AI' (arXiv:2004.01399, 2020)"],
        "case_studies": [],
    },
    "GOV-CONFLICT-INT-343": {
        "examples": "The Frontier 2026 report's synthesis documents the 'libertarian frontier' trade-off explicitly: commercial incentives (compute costs, time-to-market, user growth) directly conflict with safety investment. A lab's board prioritizes revenue milestones; the safety team's recommended 8-week red-team evaluation delays a release by 6 weeks; the board approves a 2-week evaluation instead. Financial incentives that reward shipping over safety rigor are structural — not individual bad decisions — and are documented across the industry as a root cause of the 2026 safety gap.",
        "references": [FRONTIER26, INTL26, "Krakovna et al., 'Avoiding Side Effects in Complex Environments' (NeurIPS 2020, cited on incentive misalignment)"],
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
    print(f"\nGOV-B: enriched {updated} classes")


if __name__ == "__main__":
    run()
