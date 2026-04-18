"""
Freshness Watch — feed parsing, deduplication, and classification heuristics.

No network I/O here. Reports are built by scripts/freshness_watch.py.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import urlparse

from src.classifier import ClassificationResult


def strip_html(text: str) -> str:
    if not text:
        return ""
    t = re.sub(r"<[^>]+>", " ", text)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def _localname(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[-1]
    return tag


def _text(el: ET.Element | None) -> str:
    if el is None or el.text is None:
        return ""
    return (el.text or "").strip()


def _atom_text(el: ET.Element | None) -> str:
    if el is None:
        return ""
    parts = []
    if el.text:
        parts.append(el.text.strip())
    for child in el:
        parts.append(_atom_text(child))
        if child.tail:
            parts.append(child.tail.strip())
    return " ".join(p for p in parts if p)


def parse_feed_xml(
    content: str, *, feed_url: str, feed_name: str
) -> list["FeedItem"]:
    """
    Parse RSS 2.0 or Atom XML into FeedItem records (best-effort).
    """
    root = ET.fromstring(content)
    tag = _localname(root.tag)
    items: list[FeedItem] = []

    if tag == "rss":
        channel = root.find("channel")
        if channel is None:
            return []
        for node in channel.findall("item"):
            title = _text(node.find("title"))
            link_el = node.find("link")
            link = _text(link_el) if link_el is not None else ""
            if not link:
                guid_el = node.find("guid")
                link = _text(guid_el) if guid_el is not None else ""
            desc_el = node.find("description")
            if desc_el is None:
                desc_el = node.find("{http://purl.org/rss/1.0/modules/content/}encoded")
            raw_desc = _atom_text(desc_el) if desc_el is not None else ""
            summary = strip_html(raw_desc)
            pub = None
            pub_el = node.find("pubDate")
            if pub_el is not None and pub_el.text:
                try:
                    pub = parsedate_to_datetime(pub_el.text.strip())
                    if pub.tzinfo is None:
                        pub = pub.replace(tzinfo=timezone.utc)
                except (TypeError, ValueError, OverflowError):
                    pub = None
            items.append(
                FeedItem(
                    title=title or "(no title)",
                    link=link or feed_url,
                    summary=summary[:8000],
                    published=pub,
                    feed_name=feed_name,
                    feed_url=feed_url,
                )
            )
        return items

    if tag == "feed":
        for entry in root:
            if _localname(entry.tag) != "entry":
                continue
            title_el = next(
                (c for c in entry if _localname(c.tag) == "title"), None
            )
            title = _atom_text(title_el) or "(no title)"
            link = ""
            for ln in entry:
                if _localname(ln.tag) != "link":
                    continue
                href = ln.get("href") or ""
                rel = ln.get("rel") or "alternate"
                if rel == "alternate" and href:
                    link = href
                    break
            if not link:
                for ln in entry:
                    if _localname(ln.tag) != "link":
                        continue
                    href = ln.get("href") or ""
                    if href:
                        link = href
                        break
            summ_el = next(
                (
                    c
                    for c in entry
                    if _localname(c.tag) in ("summary", "content")
                ),
                None,
            )
            summary = strip_html(_atom_text(summ_el))[:8000]
            pub = None
            for cand in ("updated", "published"):
                el = next(
                    (c for c in entry if _localname(c.tag) == cand),
                    None,
                )
                if el is not None and el.text:
                    try:
                        raw = el.text.strip()
                        if raw.endswith("Z"):
                            raw = raw[:-1] + "+00:00"
                        pub = datetime.fromisoformat(raw)
                        if pub.tzinfo is None:
                            pub = pub.replace(tzinfo=timezone.utc)
                        break
                    except ValueError:
                        continue
            items.append(
                FeedItem(
                    title=title,
                    link=link or feed_url,
                    summary=summary,
                    published=pub,
                    feed_name=feed_name,
                    feed_url=feed_url,
                )
            )
        return items

    return []


@dataclass
class FeedItem:
    title: str
    link: str
    summary: str
    published: datetime | None
    feed_name: str
    feed_url: str
    unknown_date: bool = field(default=False)


def normalize_url(url: str) -> str:
    """Stable key for dedupe: scheme-normalized host + path (trailing slash stripped)."""
    try:
        p = urlparse(url.strip())
        netloc = (p.netloc or "").lower()
        path = (p.path or "").rstrip("/").lower()
        return f"{netloc}{path}"
    except Exception:
        return url.strip().lower()


def normalize_title(title: str) -> str:
    t = re.sub(r"\s+", " ", title.strip().lower())
    return t[:500]


def dedupe_items(items: list[FeedItem]) -> list[FeedItem]:
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    out: list[FeedItem] = []
    for it in sorted(
        items,
        key=lambda x: (x.published or datetime.min.replace(tzinfo=timezone.utc)),
        reverse=True,
    ):
        nu, nt = normalize_url(it.link), normalize_title(it.title)
        if nu in seen_urls or nt in seen_titles:
            continue
        seen_urls.add(nu)
        seen_titles.add(nt)
        out.append(it)
    return out


def passes_keyword_gate(text: str, keywords: list[str]) -> bool:
    blob = text.lower()
    return any(k.lower() in blob for k in keywords)


def title_keyword_candidates(title: str, max_terms: int = 12) -> list[str]:
    """Novel terms from title for optional keyword enrichment (human filters)."""
    from src.tfidf_search import STOPWORDS, tokenize

    seen: set[str] = set()
    out: list[str] = []
    for tok in tokenize(title):
        if len(tok) < 4 or tok in STOPWORDS:
            continue
        if tok not in seen:
            seen.add(tok)
            out.append(tok)
        if len(out) >= max_terms:
            break
    return out


def confidence_label(
    cls: ClassificationResult, semantic_hits: list[dict[str, Any]]
) -> str:
    sem_score = semantic_hits[0]["score"] if semantic_hits else 0.0
    sem_ids = [h["id"] for h in semantic_hits[:5]]
    in_tab = cls.in_table
    top = cls.matches[0] if cls.matches else None

    if in_tab and top:
        agree = top.failure_id in sem_ids[:3]
        if top.score >= 0.2 and sem_score >= 0.11 and agree:
            return "high"
        if top.score >= 0.15 and sem_score >= 0.09:
            return "medium"
        if top.score >= 0.13 or sem_score >= 0.09:
            return "medium"
    if in_tab:
        return "medium"
    if sem_score >= 0.09:
        return "medium"
    if sem_score >= 0.06:
        return "low"
    return "possible_gap_candidate"


def build_suggestions(
    item: FeedItem,
    conf: str,
    cls: ClassificationResult,
    semantic_hits: list[dict[str, Any]],
) -> list[str]:
    tips: list[str] = []
    tips.append(f"Verify source and paraphrase before any repo edit: {item.link}")
    if conf == "possible_gap_candidate":
        tips.append(
            "Classifier + semantic search found no strong match — manual triage only; "
            "do not invent a new class from this item alone."
        )
        return tips

    tips.append(
        "If verified: consider enriching an existing class (reference, case_study, keywords) — not a new taxonomy ID."
    )
    if cls.matches:
        m0 = cls.matches[0]
        tips.append(
            f"Primary class candidate: `{m0.failure_id}` (keyword score {m0.score:.3f})"
        )
    for h in semantic_hits[1:6]:
        if h["score"] >= 0.06:
            tips.append(
                f"Secondary / compound candidate: `{h['id']}` — TF-IDF {h['score']}"
            )
    cand_kw = title_keyword_candidates(item.title)
    if cand_kw:
        tips.append(f"Headline tokens to consider as keywords (manual): {', '.join(cand_kw)}")
    tips.append(
        "Compound-failure note: if multiple mechanisms clearly co-occur, map as primary + secondaries in docs, not as a new class."
    )
    return tips
