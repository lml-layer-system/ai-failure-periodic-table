#!/usr/bin/env python3
"""
Fetch a report URL (HTML or PDF) or read plain text, chunk it, run
PeriodicTableClassifier on each chunk, and write JSON + Markdown summaries.

Meta Transparency often serves **PDF** for semiannual reports; `curl` + `pdftotext`
is used when the response is PDF (avoids macOS Python SSL issues with urllib).

Usage:
  curl -sL -o report.pdf URL && pdftotext -layout report.txt report.txt
  python scripts/classify_external_report.py --input report.txt --out-prefix out/base --no-write-source

  python scripts/classify_external_report.py \\
    --url https://transparency.meta.com/sr/first-half-2026-Adversarial-threat-report/ \\
    --out-prefix reports/meta-integrity-h1-2026/adversarial-h1-2026-live
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.classifier import PeriodicTableClassifier  # noqa: E402


def _display_source_path(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(ROOT))
    except ValueError:
        return str(p)


def strip_html_to_text(html: str) -> str:
    html = re.sub(r"(?is)<script[^>]*>.*?</script>", "", html)
    html = re.sub(r"(?is)<style[^>]*>.*?</style>", "", html)
    html = re.sub(r"(?is)<noscript[^>]*>.*?</noscript>", "", html)
    text = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    text = re.sub(r"</p\s*>", "\n\n", text, flags=re.I)
    text = re.sub(r"</div\s*>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    for a, b in (
        ("&nbsp;", " "),
        ("&amp;", "&"),
        ("&lt;", "<"),
        ("&gt;", ">"),
        ("&quot;", '"'),
    ):
        text = text.replace(a, b)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch_url_bytes(url: str, timeout: int = 60) -> bytes:
    ua = (
        "AIFailurePeriodicTable-ReportClassifier/1.0 "
        "(+https://github.com/lml-layer-system/ai-failure-periodic-table)"
    )
    r = subprocess.run(
        ["curl", "-sL", "--max-time", str(timeout), "-A", ua, url],
        capture_output=True,
        check=False,
    )
    if r.returncode != 0:
        raise RuntimeError(f"curl failed (exit {r.returncode}): {r.stderr.decode(errors='replace')[:500]}")
    return r.stdout


def pdf_to_text(pdf_path: Path, pdftotext_bin: str, out_txt: Path) -> None:
    subprocess.run(
        [pdftotext_bin, "-layout", str(pdf_path), str(out_txt)],
        check=True,
        capture_output=True,
    )


def paragraph_chunks(text: str, max_chars: int = 1400) -> list[str]:
    text = text.replace("\f", "\n")
    paras = [p.strip() for p in re.split(r"\n\s*\n+", text) if p.strip()]
    chunks: list[str] = []
    buf: list[str] = []
    n = 0
    for p in paras:
        if n + len(p) + 2 > max_chars and buf:
            chunks.append("\n\n".join(buf))
            buf = [p]
            n = len(p)
        else:
            buf.append(p)
            n += len(p) + 2
    if buf:
        chunks.append("\n\n".join(buf))
    return chunks


def main() -> None:
    ap = argparse.ArgumentParser(description="Classify external HTML/PDF/text report into periodic table")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--url", help="Fetch URL via curl (HTML or PDF)")
    g.add_argument("--input", type=Path, help="Existing plain-text file")
    ap.add_argument(
        "--out-prefix",
        type=Path,
        required=True,
        help="Write {out-prefix}-chunks.json, -summary.md; optional source/pdf",
    )
    ap.add_argument("--max-chars", type=int, default=1400)
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument(
        "--no-write-source",
        action="store_true",
        help="With --input: do not copy to {prefix}-source.txt; JSON references --input path",
    )
    ap.add_argument(
        "--pdftotext",
        default="pdftotext",
        help="Path to pdftotext (poppler) when URL returns PDF",
    )
    args = ap.parse_args()

    prefix = args.out_prefix
    prefix.parent.mkdir(parents=True, exist_ok=True)
    source_path: Path

    if args.url:
        raw = fetch_url_bytes(args.url, timeout=args.timeout)
        if raw[:4] == b"%PDF":
            pdf_path = Path(str(prefix) + "-official.pdf")
            pdf_path.write_bytes(raw)
            source_path = Path(str(prefix) + "-source.txt")
            pdf_to_text(pdf_path, args.pdftotext, source_path)
            header = (
                f"PDF URL: {args.url}\n"
                f"PDF saved: {pdf_path.name}\n"
                f"Extracted with: {args.pdftotext} -layout\n\n"
            )
            source_path.write_text(header + source_path.read_text(encoding="utf-8", errors="replace"))
        else:
            text = strip_html_to_text(raw.decode("utf-8", errors="replace"))
            source_path = Path(str(prefix) + "-source.txt")
            source_path.write_text(f"Fetched from: {args.url}\n\n{text}", encoding="utf-8")
        text = source_path.read_text(encoding="utf-8", errors="replace")
        if text.startswith("PDF URL:"):
            text = text.split("\n\n", 2)[-1]  # strip header for chunking
        elif text.startswith("Fetched from:"):
            text = text.split("\n\n", 1)[-1]
    else:
        text = args.input.read_text(encoding="utf-8", errors="replace")
        if args.no_write_source:
            source_path = args.input.resolve()
        else:
            source_path = Path(str(prefix) + "-source.txt")
            note = f"Loaded from file: {args.input}\n\n"
            source_path.write_text(note + text, encoding="utf-8")

    chunks = paragraph_chunks(text, max_chars=args.max_chars)
    clf = PeriodicTableClassifier()

    per_chunk: list[dict] = []
    id_counts: Counter[str] = Counter()
    name_for_id: dict[str, str] = {}

    for i, chunk in enumerate(chunks):
        r = clf.classify(chunk)
        row: dict = {
            "chunk_index": i,
            "char_len": len(chunk),
            "preview": chunk[:220].replace("\n", " ") + ("…" if len(chunk) > 220 else ""),
            "in_table": r.in_table,
            "dimensions_activated": list(r.dimensions_activated),
        }
        if r.matches:
            row["top_matches"] = [m.as_dict() for m in r.matches[:5]]
            top = r.matches[0]
            id_counts[top.failure_id] += 1
            name_for_id[top.failure_id] = top.name
        else:
            row["top_matches"] = []
            row["closest"] = [m.as_dict() for m in r.closest[:3]]
        per_chunk.append(row)

    src_disp = _display_source_path(source_path)
    summary_lines = [
        "# Classifier pass: external report (live PDF/text)",
        "",
        f"**Source file:** `{src_disp}`",
        f"**Chunks:** {len(chunks)} at ~{args.max_chars} chars (paragraph-bounded).",
        "**Tool:** `PeriodicTableClassifier` (keyword) in this repo.",
        "",
        "## Top-1 class histogram",
        "",
        "| Hits | ID | Name |",
        "|------|-----|------|",
    ]
    for fid, c in id_counts.most_common(40):
        summary_lines.append(f"| {c} | `{fid}` | {name_for_id.get(fid, '')} |")
    if not id_counts:
        summary_lines.append("| — | — | no chunk reached match threshold |")

    summary_lines.extend(["", "## Chunk → top match", ""])
    for row in per_chunk:
        if row.get("top_matches"):
            tid = row["top_matches"][0]["id"]
            tname = row["top_matches"][0]["name"]
            summary_lines.append(
                f"- **{row['chunk_index']}** → `{tid}` — {tname} — _{row['preview'][:120]}…_"
            )

    summary_path = Path(str(prefix) + "-summary.md")
    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")

    json_path = Path(str(prefix) + "-chunks.json")
    json_path.write_text(
        json.dumps(
            {
                "source_file": src_disp,
                "chunk_count": len(chunks),
                "max_chars": args.max_chars,
                "top1_histogram": dict(id_counts.most_common(50)),
                "chunks": per_chunk,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Wrote:\n  {json_path}\n  {summary_path}")
    if args.url or not args.no_write_source:
        print(f"  {source_path}")


if __name__ == "__main__":
    main()
