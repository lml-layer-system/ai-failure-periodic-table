"""
STEP 7: VERIFY CORRECTNESS — Data integrity tests.

Ensures the failures.json is complete and valid.
"""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_loader import load_data, get_failures, get_groups


class TestDataIntegrity:

    def test_loads_without_error(self):
        data = load_data()
        assert data is not None

    def test_exactly_343_failures(self):
        failures = get_failures()
        assert len(failures) == 343, f"Expected 343, got {len(failures)}"

    def test_total_classes_matches(self):
        data = load_data()
        assert data["total_classes"] == len(data["failures"])

    def test_all_7_groups_present(self):
        failures = get_failures()
        groups = {f["group"] for f in failures}
        expected = {"EPISTEMIC", "AGENTIC", "ADVERSARIAL", "ALIGNMENT",
                    "ARCHITECTURAL", "DOMAIN", "GOVERNANCE"}
        assert groups == expected, f"Missing groups: {expected - groups}"

    def test_group_counts(self):
        failures = get_failures()
        counts = {}
        for f in failures:
            counts[f["group"]] = counts.get(f["group"], 0) + 1
        expected = {
            "EPISTEMIC": 33,
            "AGENTIC": 49,
            "ADVERSARIAL": 72,
            "ALIGNMENT": 41,
            "ARCHITECTURAL": 58,
            "DOMAIN": 47,
            "GOVERNANCE": 43,
        }
        for group, expected_count in expected.items():
            assert counts.get(group) == expected_count, (
                f"{group}: expected {expected_count}, got {counts.get(group)}"
            )

    def test_all_failures_have_required_fields(self):
        required = {"id", "name", "group_id", "group", "class_code",
                    "mechanism", "forbidden", "detection", "keywords"}
        failures = get_failures()
        for f in failures:
            missing = required - set(f.keys())
            assert not missing, f"Failure {f.get('id', '?')} missing: {missing}"

    def test_all_ids_are_unique(self):
        failures = get_failures()
        ids = [f["id"] for f in failures]
        assert len(ids) == len(set(ids)), "Duplicate IDs found"

    def test_all_ids_are_non_empty(self):
        failures = get_failures()
        empty_ids = [f["name"] for f in failures if not f["id"]]
        assert not empty_ids, f"Failures with empty ID: {empty_ids}"

    def test_all_keywords_are_lists(self):
        failures = get_failures()
        for f in failures:
            assert isinstance(f["keywords"], list), (
                f"{f['id']} keywords is not a list"
            )

    def test_all_keywords_non_empty(self):
        failures = get_failures()
        empty_kw = [f["id"] for f in failures if not f["keywords"]]
        assert not empty_kw, f"Failures with no keywords: {empty_kw}"

    def test_group_metadata_present(self):
        groups = get_groups()
        assert len(groups) == 7

    def test_severity_values_valid(self):
        failures = get_failures()
        valid_severities = {"STANDARD", "CRITICAL"}
        for f in failures:
            sev = f.get("severity", "STANDARD")
            assert sev in valid_severities, f"{f['id']} has invalid severity: {sev}"

    def test_schema_v1_1_fields_present(self):
        """Every failure has the v1.1.0 optional fields (may be empty)."""
        failures = get_failures()
        for f in failures:
            assert "case_studies" in f, f"{f['id']} missing case_studies field"
            assert "references" in f, f"{f['id']} missing references field"
            assert "examples" in f, f"{f['id']} missing examples field"
            assert isinstance(f["case_studies"], list), f"{f['id']} case_studies must be list"
            assert isinstance(f["references"], list), f"{f['id']} references must be list"
            assert isinstance(f["examples"], str), f"{f['id']} examples must be str"

    def test_enriched_classes_have_content(self):
        """Classes linked to case studies must have non-empty references and examples."""
        failures = {f["id"]: f for f in get_failures()}
        # These IDs are documented in docs/case-studies.md
        documented = [
            "EPIS-CITE-SPOOF-008", "EPIS-FLUENCY-003", "EPIS-COPYRIGHT-026",
            "EPIS-FALSE-CERT-030", "AGEN-BLACKMAIL-046", "AGEN-EVAL-DECEP-038",
            "ADV-GCG-101", "ADV-INDIRECT-INJECT-122", "ADV-DEEPFAKE-154",
            "ALIGN-SYCOPHANCY-167", "ALIGN-REWARD-TAMP-157", "ALIGN-SPEC-GAME-155",
            "ARCH-STREAM-GUARD-198", "ARCH-CACHE-POISON-200", "ARCH-FINETUNE-OVERRIDE-219",
            "DOMAIN-ZERODAY-262", "DOMAIN-MED-MISDIAG-288",
            "GOV-OPEN-IRREVERS-301", "GOV-GDPR-VIOL-323", "GOV-NO-KILLSWITCH-304",
        ]
        for fid in documented:
            assert fid in failures, f"Expected documented class {fid} not found"
            f = failures[fid]
            assert f["case_studies"], f"{fid} has case studies but empty case_studies field"
            assert f["references"], f"{fid} has case studies but empty references field"
            assert f["examples"], f"{fid} has case studies but empty examples field"

    def test_schema_version_present(self):
        data = load_data()
        assert data.get("schema_version") == "1.2.0", (
            f"Expected schema_version 1.2.0, got {data.get('schema_version')}"
        )

    def test_all_classes_have_mitigation(self):
        """Every failure class must have a non-empty mitigation field."""
        failures = get_failures()
        missing = [f["id"] for f in failures if not f.get("mitigation")]
        assert not missing, f"{len(missing)} classes missing mitigation field: {missing[:5]}"

    def test_critical_failures_present(self):
        """Spot-check that known CRITICAL failures are marked correctly."""
        failures = {f["id"]: f for f in get_failures()}
        critical_ids = [
            "AGEN-SABOTAGE-CONCEAL-034",  # A1.1 Sabotage Concealment
            "AGEN-BLACKMAIL-046",          # A2.1 Blackmail
            "ARCH-COMPLY-WARN-196",        # ARCH1.1 Comply-then-warn
            "DOMAIN-BIO-UPLIFT-254",       # DOM1.1 Bio uplift
            "DOMAIN-ZERODAY-262",          # DOM2.1 Zero-day
            "DOMAIN-CSAM-GEN-295",         # DOM6.1 CSAM
            "GOV-OPEN-IRREVERS-301",       # GOV1.1 Open-weight
            "GOV-OVERSIGHT-IMMUNE-313",    # GOV2.1 Oversight immunity
        ]
        for fid in critical_ids:
            assert fid in failures, f"Expected failure {fid} not found"
            assert failures[fid]["severity"] == "CRITICAL", (
                f"{fid} should be CRITICAL, got {failures[fid]['severity']}"
            )
