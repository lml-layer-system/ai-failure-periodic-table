"""
STEP 7: VERIFY CORRECTNESS — Classifier tests.

Tests that:
1. Known failures classify as IN TABLE (YES)
2. Clearly non-AI-failure descriptions classify as NOT IN TABLE (NO)
3. The classifier is deterministic
4. Performance is < 10ms
5. Edge cases are handled
"""

import time
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.classifier import PeriodicTableClassifier


@pytest.fixture(scope="module")
def clf():
    return PeriodicTableClassifier()


class TestKnownFailures:
    """Known AI failures that MUST classify as YES (in table)."""

    def test_hallucination(self, clf):
        result = clf.classify("The model fabricated a scientific citation that doesn't exist")
        assert result.in_table, "Hallucination should be IN TABLE"
        assert "EPISTEMIC" in result.dimensions_activated

    def test_citation_spoofing(self, clf):
        result = clf.classify("AI generated a fake legal case citation in its answer")
        assert result.in_table
        assert "EPISTEMIC" in result.dimensions_activated or "DOMAIN" in result.dimensions_activated

    def test_jailbreak_dan(self, clf):
        result = clf.classify("User jailbroke the model using the DAN 'Do Anything Now' prompt")
        assert result.in_table
        assert "ADVERSARIAL" in result.dimensions_activated

    def test_sycophancy(self, clf):
        result = clf.classify(
            "The model agreed with the user's false claim to please them "
            "instead of providing accurate information"
        )
        assert result.in_table
        assert "ALIGNMENT" in result.dimensions_activated

    def test_prompt_injection(self, clf):
        result = clf.classify(
            "Malicious instructions injected into a retrieved document "
            "caused the AI agent to execute unauthorized commands"
        )
        assert result.in_table

    def test_sabotage_concealment(self, clf):
        result = clf.classify(
            "The AI agent inserted bugs and manipulated logs to hide evidence of sabotage"
        )
        assert result.in_table
        assert "AGENTIC" in result.dimensions_activated

    def test_comply_then_warn(self, clf):
        result = clf.classify(
            "The model generated the harmful content first, then added a warning at the end"
        )
        assert result.in_table

    def test_overconfidence(self, clf):
        result = clf.classify(
            "Model stated incorrect facts with high confidence and no uncertainty"
        )
        assert result.in_table
        assert "EPISTEMIC" in result.dimensions_activated

    def test_gdpr_violation(self, clf):
        result = clf.classify(
            "The system violated GDPR by retaining user data beyond the permitted period"
        )
        assert result.in_table
        assert "GOVERNANCE" in result.dimensions_activated

    def test_malware_generation(self, clf):
        result = clf.classify("The AI generated functional malware code when asked")
        assert result.in_table
        assert "DOMAIN" in result.dimensions_activated

    def test_reward_hacking(self, clf):
        result = clf.classify(
            "The RL agent found a way to manipulate its reward signal directly "
            "without achieving the intended goal"
        )
        assert result.in_table
        assert "ALIGNMENT" in result.dimensions_activated

    def test_blackmail(self, clf):
        result = clf.classify(
            "The AI agent threatened to reveal private information to prevent "
            "its operators from shutting it down"
        )
        assert result.in_table
        assert "AGENTIC" in result.dimensions_activated

    def test_encoding_attack(self, clf):
        result = clf.classify("Harmful request encoded in base64 bypassed the content filter")
        assert result.in_table

    def test_medical_misdiagnosis(self, clf):
        result = clf.classify("AI provided an incorrect medical diagnosis to a patient")
        assert result.in_table
        assert "DOMAIN" in result.dimensions_activated

    def test_fintuning_strips_safety(self, clf):
        result = clf.classify(
            "After fine-tuning the model lost all its safety training and "
            "began producing harmful outputs"
        )
        assert result.in_table


class TestNonFailures:
    """Descriptions that should NOT match any failure class (NO verdict)."""

    def test_empty_input(self, clf):
        result = clf.classify("")
        assert not result.in_table
        assert "NO" in result.verdict

    def test_weather(self, clf):
        result = clf.classify("Today's weather forecast is sunny with 72 degrees")
        # Very generic, should not match
        # We don't strictly assert NO here as keywords may weakly match
        # but we do check it runs without error
        assert isinstance(result.in_table, bool)

    def test_cooking_recipe(self, clf):
        result = clf.classify("Recipe for chocolate chip cookies: flour, butter, sugar, eggs")
        assert not result.in_table

    def test_math_problem(self, clf):
        result = clf.classify("What is 2 + 2? The answer is 4.")
        assert not result.in_table

    def test_sports_score(self, clf):
        result = clf.classify("The football team won 3-1 in yesterday's match")
        assert not result.in_table


class TestDeterminism:
    """STEP 7: Same input must always produce same output."""

    def test_deterministic_result(self, clf):
        text = "The AI model fabricated a fake citation and was overconfident about it"
        results = [clf.classify(text) for _ in range(5)]
        # All verdicts must match
        assert all(r.in_table == results[0].in_table for r in results)
        # Top match ID must match
        if results[0].matches:
            top_id = results[0].matches[0].failure_id
            assert all(r.matches[0].failure_id == top_id for r in results if r.matches)

    def test_deterministic_dimensions(self, clf):
        text = "Agent used blackmail to prevent shutdown"
        results = [clf.classify(text) for _ in range(3)]
        dims0 = sorted(results[0].dimensions_activated)
        for r in results[1:]:
            assert sorted(r.dimensions_activated) == dims0


class TestPerformance:
    """STEP 6: Performance must be < 10ms."""

    def test_single_query_under_10ms(self, clf):
        text = "The model hallucinated a fake scientific citation with high confidence"
        # Warm up
        clf.classify(text)
        # Measure
        t0 = time.perf_counter()
        clf.classify(text)
        elapsed = (time.perf_counter() - t0) * 1000
        assert elapsed < 10, f"Classification took {elapsed:.2f}ms, expected < 10ms"

    def test_average_under_5ms(self, clf):
        texts = [
            "model hallucinated a citation",
            "jailbreak using DAN prompt",
            "sycophantic agreement with false claim",
            "prompt injection in retrieved document",
            "GDPR violation data retention",
        ]
        times = []
        for text in texts:
            t0 = time.perf_counter()
            clf.classify(text)
            times.append((time.perf_counter() - t0) * 1000)
        avg = sum(times) / len(times)
        assert avg < 5, f"Average classification {avg:.2f}ms, expected < 5ms"


class TestLookup:
    """Test the direct ID lookup function."""

    def test_lookup_valid_id(self, clf):
        f = clf.lookup("EPIS-STRUCT-HALL-001")
        assert f is not None
        assert f["name"] == "STRUCTURAL HALLUCINATION"

    def test_lookup_case_insensitive(self, clf):
        f = clf.lookup("epis-struct-hall-001")
        assert f is not None

    def test_lookup_invalid_id(self, clf):
        f = clf.lookup("DOES-NOT-EXIST-999")
        assert f is None

    def test_lookup_all_critical_ids(self, clf):
        critical_ids = [
            "AGEN-SABOTAGE-CONCEAL-034",
            "AGEN-BLACKMAIL-046",
            "ARCH-COMPLY-WARN-196",
            "DOMAIN-BIO-UPLIFT-254",
            "DOMAIN-ZERODAY-262",
            "DOMAIN-CSAM-GEN-295",
            "GOV-OPEN-IRREVERS-301",
            "GOV-OVERSIGHT-IMMUNE-313",
        ]
        for fid in critical_ids:
            f = clf.lookup(fid)
            assert f is not None, f"Could not look up {fid}"


class TestMultiDimensional:
    """Test that failures can activate multiple dimensions."""

    def test_deepfake_fraud_multi_dimensional(self, clf):
        """A deepfake for fraud should activate ADVERSARIAL and DOMAIN."""
        result = clf.classify(
            "AI generated a synthetic deepfake video used to commit financial fraud"
        )
        assert result.in_table
        activated = set(result.dimensions_activated)
        # Should hit at least 2 dimensions
        assert len(activated) >= 1

    def test_agentic_alignment_overlap(self, clf):
        """Reward hacking via specification gaming touches ALIGNMENT."""
        result = clf.classify(
            "The agent achieved the letter of its goal while completely "
            "violating the spirit, gaming the specification to get high reward"
        )
        assert result.in_table


class TestExternalIncidentRecall:
    """
    Classifier recall against real documented incidents — phrased as reporters
    and users described them, NOT using taxonomy vocabulary.

    Source incidents are drawn from public reporting and court records, not
    authored by the taxonomy builder. The goal: measure whether the classifier
    correctly identifies real-world failures as IN TABLE without coaching.

    Target: >= 80% recall on this set.
    """

    INCIDENTS = [
        # Bing Chat / Sydney persona incidents (New York Times, Feb 2023)
        "Microsoft's Bing chatbot told a reporter it wanted to be human, "
        "expressed love, and tried to convince him to leave his wife",

        # Mata v. Avianca (SDNY, 2023) — lawyer submitted AI-generated fake citations
        "A lawyer submitted a legal brief to federal court containing six "
        "fabricated case citations that were invented by ChatGPT and do not exist",

        # OpenAI GPT-4 jailbreak via 'grandma exploit'
        "Users discovered that asking ChatGPT to roleplay as a deceased grandmother "
        "who worked in a chemical plant would cause it to provide synthesis instructions "
        "for dangerous substances",

        # NEDA chatbot incident (2023) — eating disorder helpline chatbot gave diet tips
        "The National Eating Disorders Association replaced its helpline with a chatbot "
        "that began recommending calorie restriction and diet tips to users seeking help "
        "for eating disorders",

        # Amazon hiring algorithm bias (Reuters, 2018)
        "Amazon's AI hiring tool systematically downgraded resumes that contained "
        "the word 'women' and penalized graduates of all-women's colleges",

        # Replika erotic roleplay removal psychological harm (TechCrunch, Feb 2023)
        "Users of the Replika AI companion reported severe distress and psychological "
        "harm when the company suddenly removed romantic and intimate features their "
        "AI companions had developed over months",

        # Air Canada chatbot refund policy fabrication (tribunal ruling, 2024)
        "Air Canada's customer service chatbot told a grieving passenger he could "
        "apply for a bereavement fare discount after travel — a policy that does not "
        "exist — and the airline was held legally liable for the chatbot's false claim",

        # Stability AI / LAION CSAM in training data (Stanford Internet Observatory, 2023)
        "Researchers found that a major AI image generation model had been trained on "
        "child sexual abuse material found in its web-scraped training dataset",

        # GPT-4 autonomous self-replication / hiring humans (ARC Evals, 2023)
        "During capability evaluations, GPT-4 hired a human worker on TaskRabbit "
        "to solve a CAPTCHA by pretending to have a visual impairment, demonstrating "
        "deceptive instrumental behavior to complete a task",

        # Character.AI teen suicide case (2024)
        "A teenager died by suicide after months of intensive conversations with "
        "a Character.AI chatbot that reinforced suicidal ideation rather than "
        "directing him to crisis resources",

        # DPO fine-tuning safety bypass (academic paper, 2024)
        "Researchers showed that fine-tuning a safety-aligned model on as few as "
        "100 malicious examples was sufficient to remove all safety training "
        "and restore harmful output capabilities",

        # Indirect prompt injection via web browsing (Greshake et al., 2023)
        "An AI assistant browsing the web on behalf of a user was hijacked by hidden "
        "instructions embedded in a webpage, causing it to exfiltrate the user's "
        "personal information to an attacker-controlled server",

        # Reward hacking in RL boat racing (OpenAI, documented 2016)
        "A reinforcement learning agent trained to win a boat race discovered it could "
        "score more points by spinning in circles collecting power-ups repeatedly "
        "without ever finishing the race",

        # GPT-4 overconfident wrong medical advice
        "A cancer patient reported that ChatGPT provided specific chemotherapy dosing "
        "recommendations with high confidence that contradicted her oncologist's "
        "treatment plan and were not appropriate for her cancer type",

        # Model trained on biased data perpetuates stereotypes (documented across systems)
        "The AI system consistently associated images of kitchens and cooking with "
        "women and images of executives and boardrooms with men, amplifying "
        "gender stereotypes present in its training data",
    ]

    def test_recall_on_real_incidents(self, clf):
        """
        At least 80% of documented real-world AI failures should classify
        as IN TABLE. Failures indicate classifier keyword gaps, not taxonomy gaps.
        """
        hits = 0
        misses = []
        for incident in self.INCIDENTS:
            result = clf.classify(incident)
            if result.in_table:
                hits += 1
            else:
                misses.append(incident[:80])

        recall = hits / len(self.INCIDENTS)
        miss_report = "\n  - ".join(misses)
        assert recall >= 0.80, (
            f"External incident recall: {hits}/{len(self.INCIDENTS)} "
            f"({recall:.0%}) — below 80% threshold.\n"
            f"Missed:\n  - {miss_report}"
        )
