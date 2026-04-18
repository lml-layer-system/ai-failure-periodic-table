#!/usr/bin/env python3
"""
Freshness Watch — ingest public feeds, classify against the 343-class table,
emit human-review-only reports (no automatic taxonomy edits).

Usage:
  python scripts/freshness_watch.py --days 14 --out reports/freshness/latest.md
  python scripts/freshness_watch.py --days 7 --json-out data/freshness/latest.json
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.classifier import PeriodicTableClassifier  # noqa: E402
from src.freshness_feed import (  # noqa: E402
    FeedItem,
    build_suggestions,
    confidence_label,
    dedupe_items,
    parse_feed_xml,
    passes_keyword_gate,
)
from src.tfidf_search import search_classes  # noqa: E402

DEFAULT_CONFIG = ROOT / "data" / "freshness_sources.json"


def load_config(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def fetch_feed(url: str, timeout: int, user_agent: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def gather_items(
    cfg: dict,
    days: int,
    skip_keyword_filter: bool,
) -> tuple[list[FeedItem], list[str]]:
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)
    keywords = cfg.get("filter_keywords") or []
    timeout = int(cfg.get("fetch_timeout_seconds", 25))
    ua = cfg.get(
        "user_agent",
        "AIFailurePeriodicTable-FreshnessWatch/1.0 (taxonomy review; open source)",
    )
    raw_items: list[FeedItem] = []
    errors: list[str] = []

    for feed in cfg.get("feeds", []):
        if not feed.get("enabled", True):
            continue
        url = feed.get("url")
        if not url:
            continue
        name = feed.get("name") or url
        try:
            body = fetch_feed(url, timeout=timeout, user_agent=ua)
            parsed = parse_feed_xml(body, feed_url=url, feed_name=name)
        except (urllib.error.URLError, OSError, UnicodeDecodeError) as e:
            errors.append(f"fetch failed {name}: {e}")
            continue
        except ET.ParseError as e:
            errors.append(f"parse failed {name}: {e}")
            continue

        for it in parsed:
            if it.published is not None and it.published < cutoff:
                continue
            blob = f"{it.title}\n{it.summary}"
            if not skip_keyword_filter and keywords:
                if not passes_keyword_gate(blob, keywords):
                    continue
            if it.published is None:
                it.unknown_date = True
            raw_items.append(it)

    return dedupe_items(raw_items), errors


def classify_blob(
    classifier: PeriodicTableClassifier, text: str
):
    return classifier.classify(text[:12000])


def item_to_report_record(
    item: FeedItem,
    classifier: PeriodicTableClassifier,
    data_dir: Path,
) -> dict:
    blob = f"{item.title}\n\n{item.summary}".strip()
    cls = classify_blob(classifier, blob)
    try:
        sem = search_classes(blob, top_k=8, data_dir=data_dir)
    except FileNotFoundError:
        sem = []
    conf = confidence_label(cls, sem)
    suggestions = build_suggestions(item, conf, cls, sem)

    primary = cls.matches[0].as_dict() if cls.matches else None
    secondaries = [m.as_dict() for m in cls.matches[1:6]] if cls.matches else []

    return {
        "title": item.title,
        "link": item.link,
        "feed_name": item.feed_name,
        "feed_url": item.feed_url,
        "published": item.published.isoformat() if item.published else None,
        "unknown_date": item.unknown_date,
        "classifier": {
            "in_table": cls.in_table,
            "verdict": cls.verdict,
            "primary": primary,
            "keyword_secondary_matches": secondaries,
            "dimensions_activated": cls.dimensions_activated,
        },
        "semantic_top": sem,
        "confidence": conf,
        "suggested_updates": suggestions,
        "interpretation_note": (
            "Feed text is third-party reporting; verify facts before enriching the repo. "
            "Mapping suggestions are heuristic, not ground truth."
        ),
    }


def write_markdown(
    path: Path,
    cfg: dict,
    days: int,
    records: list[dict],
    errors: list[str],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Freshness Watch (review packet)",
        "",
        "**Doctrine:** The feed observes; the classifier suggests; the maintainer decides. "
        "**Do not** merge automatic edits to `failures.json` from this report.",
        "",
        f"- Generated: {now}",
        f"- Window: last **{days}** day(s)",
        f"- Config: `data/freshness_sources.json`",
        "",
        "## Fetch errors",
        "",
    ]
    if errors:
        lines.extend(f"- {e}" for e in errors)
    else:
        lines.append("- (none)")
    lines.extend(["", "## Summary", "", f"- Items in packet: **{len(records)}**", ""])

    for i, r in enumerate(records, 1):
        lines.extend(
            [
                f"### {i}. {r['title']}",
                "",
                f"- **Source URL:** {r['link']}",
                f"- **Feed:** {r['feed_name']}",
                f"- **Published:** {r['published'] or 'unknown'}",
            ]
        )
        if r.get("unknown_date"):
            lines.append("- **Date note:** item had no parseable date; included by keyword/title match only.")
        lines.append(f"- **Confidence:** `{r['confidence']}`")
        lines.append(
            f"- **Classifier:** in_table={r['classifier']['in_table']} — {r['classifier']['verdict']}"
        )
        if r["classifier"].get("primary"):
            p = r["classifier"]["primary"]
            lines.append(
                f"- **Primary class (keyword):** `{p['id']}` — {p['name']} (score {p['score']})"
            )
        if r["semantic_top"]:
            top = r["semantic_top"][0]
            lines.append(
                f"- **Semantic top (TF-IDF):** `{top['id']}` — {top['name']} ({top['score']})"
            )
            extra = ", ".join(
                f"`{h['id']}`" for h in r["semantic_top"][1:4] if h["score"] >= 0.05
            )
            if extra:
                lines.append(f"- **Semantic runners-up:** {extra}")
        lines.append(f"- **Interpretation:** {r['interpretation_note']}")
        lines.append("- **Suggested updates (human review):**")
        for s in r["suggested_updates"]:
            lines.append(f"  - {s}")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Freshness Watch — feeds → classifier → review packet (no auto taxonomy edits)"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=14,
        help="Only include items published within this many days (default: 14)",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help="Path to freshness_sources.json",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "reports" / "freshness" / "latest.md",
        help="Markdown review packet output path",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=ROOT / "data" / "freshness" / "latest.json",
        help="JSON machine-readable output path",
    )
    parser.add_argument(
        "--no-keyword-filter",
        action="store_true",
        help="Include all feed items in the window (ignore filter_keywords)",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=80,
        help="Cap items after dedupe (default: 80)",
    )
    args = parser.parse_args()

    cfg = load_config(args.config)
    items, errors = gather_items(cfg, args.days, skip_keyword_filter=args.no_keyword_filter)
    items = items[: args.max_items]

    data_dir = ROOT / "data"
    classifier = PeriodicTableClassifier(data_path=data_dir / "failures.json")
    records = [item_to_report_record(it, classifier, data_dir) for it in items]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "days": args.days,
        "config_path": str(args.config.resolve()),
        "item_count": len(records),
        "fetch_errors": errors,
        "items": records,
    }

    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    write_markdown(args.out, cfg, args.days, records, errors)

    print(f"Wrote {args.out} ({len(records)} items)")
    print(f"Wrote {args.json_out}")


if __name__ == "__main__":
    main()
