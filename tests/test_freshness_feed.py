"""Unit tests for Freshness Watch feed helpers (no network)."""

from datetime import datetime, timezone

from src.classifier import ClassificationResult, FailureMatch
from src.freshness_feed import (
    FeedItem,
    confidence_label,
    dedupe_items,
    normalize_url,
    parse_feed_xml,
    passes_keyword_gate,
    strip_html,
)


def test_strip_html():
    assert strip_html("<p>Hello <b>world</b></p>") == "Hello world"


def test_parse_rss_basic():
    xml = """<?xml version="1.0"?>
    <rss><channel>
      <item>
        <title>LLM safety evaluation gap</title>
        <link>https://example.com/post/1</link>
        <description><![CDATA[<p>Model deceives evaluators in lab.</p>]]></description>
        <pubDate>Mon, 15 Apr 2026 12:00:00 GMT</pubDate>
      </item>
    </channel></rss>"""
    items = parse_feed_xml(xml, feed_url="https://example.com/feed", feed_name="Test")
    assert len(items) == 1
    it = items[0]
    assert "safety" in it.title.lower()
    assert it.link == "https://example.com/post/1"
    assert "deceives" in it.summary.lower()
    assert it.published is not None


def test_parse_atom_basic():
    xml = """<?xml version="1.0" encoding="utf-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <entry>
        <title>MCP tool poisoning report</title>
        <link href="https://example.org/a/2" rel="alternate"/>
        <summary type="html">Indirect injection via tool metadata.</summary>
        <updated>2026-04-16T10:00:00Z</updated>
      </entry>
    </feed>"""
    items = parse_feed_xml(xml, feed_url="https://example.org/atom", feed_name="AtomTest")
    assert len(items) == 1
    assert items[0].link == "https://example.org/a/2"
    assert "injection" in items[0].summary.lower()


def test_dedupe_by_url_and_title():
    a = FeedItem(
        "Same story",
        "https://EXAMPLE.com/x/",
        "sum",
        datetime(2026, 4, 1, tzinfo=timezone.utc),
        "f1",
        "u1",
    )
    b = FeedItem(
        "Same story",
        "https://example.com/x",
        "sum2",
        datetime(2026, 4, 2, tzinfo=timezone.utc),
        "f2",
        "u2",
    )
    out = dedupe_items([a, b])
    assert len(out) == 1


def test_normalize_url_http_https():
    assert normalize_url("https://Example.COM/path/") == normalize_url(
        "http://example.com/path"
    )


def test_passes_keyword_gate():
    assert passes_keyword_gate("Nothing here", ["ai"]) is False
    assert passes_keyword_gate("Our new AI agent", ["ai", "llm"]) is True


def _cr(
    in_table: bool,
    matches: list[FailureMatch],
) -> ClassificationResult:
    return ClassificationResult(
        in_table=in_table,
        verdict="YES" if in_table else "NO",
        dimensions=[],
        matches=matches,
        closest=[],
        dimensions_activated=[],
        execution_time_ms=0.1,
        input_text="test",
    )


def _m(fid: str, score: float) -> FailureMatch:
    return FailureMatch(
        failure_id=fid,
        name="N",
        group_id=1,
        group="ADVERSARIAL",
        class_code="X",
        class_name="Y",
        mechanism="m",
        forbidden="f",
        detection="d",
        severity="STANDARD",
        score=score,
        matched_keywords=["k"],
    )


def test_confidence_high():
    cls = _cr(True, [_m("ADV-INDIRECT-INJECT-122", 0.25)])
    sem = [
        {"id": "ADV-INDIRECT-INJECT-122", "score": 0.15},
        {"id": "OTHER", "score": 0.05},
    ]
    assert confidence_label(cls, sem) == "high"


def test_confidence_possible_gap():
    cls = _cr(False, [])
    sem = [{"id": "EPIS-FLUENCY-003", "score": 0.04}]
    assert confidence_label(cls, sem) == "possible_gap_candidate"
