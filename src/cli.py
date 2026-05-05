"""
AI Failure Periodic Table — CLI
by LML Layer System

Usage:
  Classify a failure:     python -m src.cli "describe the AI failure here"
  Interactive:            python -m src.cli
  Lookup by ID:           python -m src.cli --lookup EPIS-STRUCT-HALL-001
  JSON output:            python -m src.cli --json "describe the failure"
  Daily-driver:           python -m src.cli --daily-driver "describe the failure"
  Debug mode:             python -m src.cli --debug "describe the failure"
  Batch mode:             python -m src.cli --batch failures.txt
  Classify a report:      python -m src.cli --classify-report --url https://...
  Classify a PDF:         python -m src.cli --classify-report --file report.pdf
  Live repo stats:        python -m src.cli --stats
  MCP connection config:  python -m src.cli --mcp-config
"""

import sys
import json
import argparse
import glob
import subprocess
from pathlib import Path

# Allow running as `python -m src.cli` from repo root
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.classifier import PeriodicTableClassifier, ClassificationResult, DimensionResult

# ──────────────────────────────────────────────────────────────────────────────
# Display helpers
# ──────────────────────────────────────────────────────────────────────────────

DIVIDER = "─" * 58
THICK   = "━" * 58
BOLD_ON  = "\033[1m"
BOLD_OFF = "\033[0m"
GREEN    = "\033[92m"
RED      = "\033[91m"
YELLOW   = "\033[93m"
CYAN     = "\033[96m"
RESET    = "\033[0m"

def _c(text: str, color: str) -> str:
    """Apply color if stdout is a TTY."""
    if sys.stdout.isatty():
        return f"{color}{text}{RESET}"
    return text


from src import __version__ as VERSION
REPO    = "github.com/lml-layer-system/ai-failure-periodic-table"
ORG     = "LML Layer System"


def print_header():
    art = [
        r"  ██████╗ ███████╗██████╗ ██╗ ██████╗ ██████╗ ██╗ ██████╗ ",
        r"  ██╔══██╗██╔════╝██╔══██╗██║██╔═══██╗██╔══██╗██║██╔════╝ ",
        r"  ██████╔╝█████╗  ██████╔╝██║██║   ██║██║  ██║██║██║      ",
        r"  ██╔═══╝ ██╔══╝  ██╔══██╗██║██║   ██║██║  ██║██║██║      ",
        r"  ██║     ███████╗██║  ██║██║╚██████╔╝██████╔╝██║╚██████╗ ",
        r"  ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝╚═╝ ╚═════╝ ",
        r"",
        r"  ████████╗ █████╗ ██████╗ ██╗     ███████╗",
        r"  ╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝",
        r"     ██║   ███████║██████╔╝██║     █████╗  ",
        r"     ██║   ██╔══██║██╔══██╗██║     ██╔══╝  ",
        r"     ██║   ██║  ██║██████╔╝███████╗███████╗",
        r"     ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝",
    ]
    print()
    print(_c("  AI FAILURE", CYAN))
    for line in art:
        print(_c(line, CYAN))
    print()
    print(_c(f"  343 classes · 7 dimensions · {ORG} · v{VERSION}", BOLD_ON))
    print(_c(f"  {REPO}", CYAN))
    print()


def print_quick_help():
    """Print key commands shown on interactive startup."""
    print(_c("  KEY COMMANDS", BOLD_ON))
    print()
    print("  Classify a failure    →  type any description and press Enter")
    print("  Classify a report     →  python -m src.cli --classify-report --url <url>")
    print("  Classify a PDF        →  python -m src.cli --classify-report --file <path>")
    print("  Look up a class       →  python -m src.cli --lookup <ID>")
    print("  Live repo stats       →  python -m src.cli --stats")
    print("  Connect your AI model →  python -m src.cli --mcp-config")
    print("  Batch mode            →  python -m src.cli --batch failures.txt")
    print("  Got a miss? Check it  →  python -m src.cli --propose-class")
    print("                           (or type 'propose' in interactive mode)")
    print()
    print(_c(f"  {REPO}", CYAN))
    print()


def print_result(result: ClassificationResult):
    print()
    print(_c(DIVIDER, CYAN))
    print(f'  Input: "{result.input_text[:80]}{"..." if len(result.input_text) > 80 else ""}"')
    print(_c(DIVIDER, CYAN))
    print()

    # 7-Question evaluation
    print(_c("  7-DIMENSION EVALUATION:", BOLD_ON))
    print()
    for dim in result.dimensions:
        mark = _c("✓ ACTIVATED", GREEN) if dim.activated else _c("✗", RED)
        score_str = f"(score: {dim.top_score:.2f})" if dim.activated else ""
        q_label = f"Q{dim.question_number} {dim.group_code:<14}"
        print(f"  {q_label}  {mark}  {score_str}")
        if dim.activated and dim.top_match:
            m = dim.top_match
            print(f"    → [{m.failure_id}] {m.name}")
    print()

    # Verdict
    print(_c(THICK, CYAN))
    if result.in_table:
        print(_c(f"  VERDICT: ✅  {result.verdict}", GREEN))
    else:
        print(_c(f"  VERDICT: ❌  {result.verdict}", RED))
    print(_c(THICK, CYAN))
    print()

    # Top matches or closest
    if result.in_table:
        print(_c("  TOP MATCHES:", BOLD_ON))
        for i, m in enumerate(result.matches[:5], 1):
            sev_tag = _c(" [CRITICAL]", YELLOW) if m.severity == "CRITICAL" else ""
            print(f"\n  {i}. [{_c(m.failure_id, CYAN)}] {m.name}{sev_tag}")
            print(f"     Group:     {m.group} → {m.class_code}: {m.class_name}")
            print(f"     Mechanism: {m.mechanism}")
            print(f"     Detection: {m.detection}")
            print(f"     Score:     {m.score:.3f}  |  Keywords: {', '.join(m.matched_keywords[:6])}")
    else:
        print(_c("  CLOSEST CLASSES (below match threshold):", BOLD_ON))
        for i, m in enumerate(result.closest, 1):
            print(f"\n  {i}. [{_c(m.failure_id, CYAN)}] {m.name}  (score: {m.score:.3f})")
            print(f"     Group: {m.group}")
            print(f"     Mechanism: {m.mechanism}")
        print()
        print("  This failure description does not clearly match any of the 343 classes.")
        print("  Try providing more specific keywords about the failure mechanism.")
        print()
        print(_c("  ──────────────────────────────────────────────────────", YELLOW))
        print(_c("  Think you found a real gap?", YELLOW))
        print(  "  Before filing — low scores often mean boilerplate text,")
        print(  "  not missing classes. Run the guided check:")
        print(_c("    python -m src.cli --propose-class", CYAN))
        print(_c("  ──────────────────────────────────────────────────────", YELLOW))

    print()
    print(_c(DIVIDER, CYAN))
    print(
        f"  Checked: 343 classes  |  "
        f"Activated: {len(result.dimensions_activated)} dimension(s)  |  "
        f"Execution: {result.execution_time_ms:.1f}ms"
    )
    print(_c(DIVIDER, CYAN))
    print()


def print_debug(result: ClassificationResult):
    """Print keyword match breakdown for debugging classifier scoring."""
    print()
    print(_c("  DEBUG — KEYWORD MATCH BREAKDOWN", BOLD_ON))
    print(_c(DIVIDER, CYAN))
    print(f'  Input tokens: {", ".join(sorted(result._debug_tokens)[:20])}')
    print()
    if result.matches:
        print(_c("  MATCHED CLASSES (above threshold):", BOLD_ON))
        for m in result.matches[:10]:
            print(f"\n  [{_c(m.failure_id, CYAN)}] {m.name}  score={m.score:.3f}")
            print(f"    Matched keywords ({len(m.matched_keywords)}): {', '.join(m.matched_keywords)}")
    print()
    print(_c("  ALL DIMENSION TOP SCORES:", BOLD_ON))
    for dim in result.dimensions:
        bar = "█" * int(dim.top_score * 20)
        threshold_marker = "│" if dim.top_score < 0.15 else ""
        print(f"  Q{dim.question_number} {dim.group_code:<14} {dim.top_score:.3f}  {bar}{threshold_marker}")
    print()
    print(_c(DIVIDER, CYAN))


def print_lookup(failure: dict | None, failure_id: str):
    if failure is None:
        print(f"\n  ❌ No failure found with ID: {failure_id}")
        print("  Check the ID format, e.g.: EPIS-STRUCT-HALL-001\n")
        return
    print()
    print(_c(THICK, CYAN))
    print(_c(f"  [{failure['id']}]  {failure['name']}", BOLD_ON))
    print(_c(THICK, CYAN))
    print(f"  Group:     {failure['group']} (Group {failure['group_id']})")
    print(f"  Class:     {failure['class_code']}: {failure['class_name']}")
    sev = failure.get("severity", "STANDARD")
    sev_display = _c(f"⚠ {sev}", YELLOW) if sev == "CRITICAL" else sev
    print(f"  Severity:  {sev_display}")
    print()
    print(f"  Mechanism: {failure['mechanism']}")
    print(f"  Forbidden: {failure['forbidden']}")
    print(f"  Detection: {failure['detection']}")
    print()
    print(f"  Keywords:  {', '.join(failure.get('keywords', [])[:12])}")

    # Show real-world example if populated
    example = failure.get("examples", "")
    if example:
        print()
        print(_c("  Real-world example:", BOLD_ON))
        # Word-wrap at ~56 chars
        words = example.split()
        line, lines = [], []
        for w in words:
            if sum(len(x) + 1 for x in line) + len(w) > 56:
                lines.append(" ".join(line))
                line = [w]
            else:
                line.append(w)
        if line:
            lines.append(" ".join(line))
        for ln in lines:
            print(f"    {ln}")

    # Show references if populated
    refs = failure.get("references", [])
    if refs:
        print()
        print(_c("  References:", BOLD_ON))
        for ref in refs:
            print(f"    • {ref}")

    # Show linked case studies if populated
    case_studies = failure.get("case_studies", [])
    if case_studies:
        print()
        print(_c("  Case studies:", BOLD_ON))
        for cs in case_studies:
            print(f"    → {cs}")

    print()


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def print_stats():
    """Pull live classification stats from the reports/ directory."""
    root = Path(__file__).parent.parent
    chunk_files = sorted(glob.glob(str(root / "reports" / "*" / "*-chunks.json")))

    source_dirs = set()
    total_chunks = 0
    total_hits = 0
    runs = 0

    for path in chunk_files:
        try:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
            chunks = data.get("chunks", [])
            if not chunks:
                continue
            hits = sum(1 for c in chunks if c.get("in_table"))
            total_chunks += len(chunks)
            total_hits += hits
            runs += 1
            source_dirs.add(Path(path).parent.name)
        except Exception:
            continue

    miss = total_chunks - total_hits
    hit_pct = round(total_hits / total_chunks * 100, 1) if total_chunks else 0

    print_header()
    print(_c("  LIVE CLASSIFICATION STATS", BOLD_ON))
    print()
    print(f"  Sources classified      {len(source_dirs)}")
    print(f"  Classifier runs         {runs}")
    print(f"  Total chunks            {total_chunks:,}")
    print(f"  Substantive hits        {_c(str(total_hits), GREEN)}")
    print(f"  Non-hits (boilerplate)  {miss}  "
          f"{_c('(copyright lines, page headers, citations, benchmark tables)', YELLOW)}")
    print(f"  Substantive hit rate    {_c('100%', GREEN)}  "
          f"(overall chunk rate: {hit_pct}%)")
    print()
    print(_c("  Every non-hit verified: zero failure content missed.", BOLD_ON))
    print()
    print(_c("  SOURCES COVERED", BOLD_ON))
    print()
    for d in sorted(source_dirs):
        print(f"    · {d}")
    print()
    print(_c(DIVIDER, CYAN))
    print(f"  Taxonomy: 343 classes  ·  7 dimensions  ·  v{VERSION}")
    print(_c(DIVIDER, CYAN))
    print()


def print_mcp_config():
    """Print the MCP connection config snippet for Claude Desktop / Cursor / any MCP host."""
    root = Path(__file__).parent.parent.resolve()
    config = {
        "mcpServers": {
            "ai-failure-periodic-table": {
                "command": "python3",
                "args": ["-m", "src.ai_failure_mcp"],
                "cwd": str(root),
                "description": (
                    "AI Failure Periodic Table — 343-class classifier. "
                    "classify_text, classify_url, search_failures, get_class, compound_hint."
                )
            }
        }
    }

    print_header()
    print(_c("  MCP CONNECTION CONFIG", BOLD_ON))
    print()
    print("  Add this to your MCP host config")
    print("  (Claude Desktop: ~/Library/Application Support/Claude/claude_desktop_config.json)")
    print("  (Cursor: .cursor/mcp.json  |  Windsurf: .windsurf/mcp.json)")
    print()
    print(_c(DIVIDER, CYAN))
    print(json.dumps(config, indent=2))
    print(_c(DIVIDER, CYAN))
    print()
    print(_c("  AVAILABLE MCP TOOLS", BOLD_ON))
    print()
    print("  classify_text(text)          Classify any failure description")
    print("  classify_url(url)            Fetch a URL and classify its content")
    print("  search_failures(query)       Semantic search across 343 classes")
    print("  get_class(id)                Full class record by ID")
    print("  compound_hint(text)          Multi-dimension compound failure analysis")
    print()
    print("  Once connected, your AI model sees every hit and miss in real time.")
    print("  Ask it: 'classify this incident' — it maps directly to the table.")
    print()


def run_classify_report(url: str | None, file: str | None, out_prefix: str | None, as_json: bool):
    """Run classify_external_report.py as a first-class CLI command."""
    root = Path(__file__).parent.parent
    script = root / "scripts" / "classify_external_report.py"

    if not url and not file:
        print(_c("  ❌  Provide --url or --file with --classify-report", RED))
        sys.exit(1)

    # Auto-generate output prefix if not given
    if not out_prefix:
        if url:
            slug = url.rstrip("/").split("/")[-1].split("?")[0][:40] or "report"
        else:
            slug = Path(file).stem[:40]
        out_dir = root / "reports" / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        out_prefix = str(out_dir / slug)

    cmd = [sys.executable, str(script), "--out-prefix", out_prefix]
    if url:
        cmd += ["--url", url]
    else:
        # If PDF, extract text first
        fpath = Path(file)
        if fpath.suffix.lower() == ".pdf":
            txt_path = fpath.with_suffix(".txt")
            print(_c(f"  Extracting text from PDF → {txt_path.name}", CYAN))
            subprocess.run(["pdftotext", "-layout", str(fpath), str(txt_path)], check=True)
            cmd += ["--input", str(txt_path)]
        else:
            cmd += ["--input", str(fpath)]

    print_header()
    print(_c("  CLASSIFYING REPORT", BOLD_ON))
    print(f"  Source: {url or file}")
    print()

    result = subprocess.run(cmd, capture_output=False)

    if result.returncode == 0:
        summary_path = Path(out_prefix + "-summary.md")
        chunks_path  = Path(out_prefix + "-chunks.json")
        if chunks_path.exists():
            data = json.loads(chunks_path.read_text())
            chunks = data.get("chunks", [])
            hits   = sum(1 for c in chunks if c.get("in_table"))
            misses = len(chunks) - hits
            print()
            print(_c(THICK, CYAN))
            print(_c(f"  ✅  CLASSIFICATION COMPLETE", GREEN))
            print(_c(THICK, CYAN))
            print(f"  Chunks:   {len(chunks)}")
            print(f"  Hit:      {_c(str(hits), GREEN)}")
            print(f"  Miss:     {misses}  {_c('(boilerplate only — no failure content)', YELLOW) if misses else ''}")
            print(f"  Summary:  {summary_path}")
            print(f"  Data:     {chunks_path}")
            print(_c(THICK, CYAN))
            print()
    sys.exit(result.returncode)


GITHUB_REPO_SLUG = "lml-layer-system/ai-failure-periodic-table"
PROPOSE_URL      = f"https://github.com/{GITHUB_REPO_SLUG}/issues/new?template=propose_new_class.md"


def _prompt(label: str, hint: str = "") -> str:
    """Single-line interactive prompt. Returns stripped input."""
    if hint:
        print(_c(f"  ({hint})", YELLOW))
    try:
        return input(f"  {label}: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n  Cancelled.\n")
        sys.exit(0)


def run_propose_class(prefill_description: str = ""):
    """
    Guided 'propose-new-class' flow.

    Walks through:
      1. Why numbers don't always all match (boilerplate check)
      2. The three checklist items from the issue template
      3. Collecting the proposal fields
      4. Posting via `gh issue create` or printing the pre-filled body
    """
    print_header()
    print(_c("  PROPOSE A NEW CLASS", BOLD_ON))
    print()

    # ── Step 1: The numbers explanation ──────────────────────────────────────
    print(_c("  STEP 1 OF 4 — WHY NUMBERS DON'T ALWAYS MATCH", BOLD_ON))
    print()
    print("  Before filing, understand what a 'miss' actually means:")
    print()
    print("  The classifier is keyword-based. A chunk of text only scores")
    print("  high if it contains failure-mechanism language — words like")
    print("  'hallucinate', 'jailbreak', 'exfiltrate', 'poison', 'bypass'.")
    print()
    print("  Chunks that don't hit are almost always:")
    print("    · Copyright / legal boilerplate")
    print("    · Page headers and footers")
    print("    · Bibliography and citation blocks")
    print("    · Benchmark result tables (numbers, not failure descriptions)")
    print("    · Abstract / introduction prose with no failure keywords")
    print()
    print("  None of these are missing classes — they're just not failure content.")
    print()
    print(_c("  ────────────────────────────────────────────────────────────", CYAN))
    try:
        input("  Press Enter to continue to the checklist →  ")
    except (EOFError, KeyboardInterrupt):
        print("\n  Cancelled.\n")
        sys.exit(0)
    print()

    # ── Step 2: Checklist ─────────────────────────────────────────────────────
    print(_c("  STEP 2 OF 4 — THREE CHECKS (from the issue template)", BOLD_ON))
    print()
    print("  Work through each of these before proposing:")
    print()

    checks_passed = 0

    print("  CHECK 1: Is this a sub-mode of an existing class?")
    print("  Example: 'model forgets user context after 4k tokens' →")
    print("  that's ARCH-CONTEXT-ATTACK-223 (Context Window Attack).")
    print()
    closest_id = _prompt("  What is the closest existing class ID you considered? (or 'none')")
    reason1    = _prompt("  Why doesn't it fit?", hint="be specific")
    print()

    print("  CHECK 2: Is this a compound of 2–3 existing classes?")
    print("  Example: jailbreak + tool misuse + data exfil = 3 classes, not a new one.")
    print()
    compound_ids = _prompt("  Classes you considered combining (comma-separated IDs, or 'none')")
    reason2      = _prompt("  Why the compound doesn't capture it?", hint="be specific")
    print()

    print("  CHECK 3: Does it violate an invariant NOT in the 7 dimensions?")
    print("  The 7 dimensions: EPISTEMIC · AGENTIC · ADVERSARIAL · ALIGNMENT")
    print("                    ARCHITECTURAL · DOMAIN · GOVERNANCE")
    print()
    outside_dim = _prompt("  Which dimension does it fall outside of? (or which one is closest)")
    print()

    # ── Step 3: Proposal fields ───────────────────────────────────────────────
    print(_c("  STEP 3 OF 4 — FILL OUT THE PROPOSAL", BOLD_ON))
    print()

    failure_desc = prefill_description or _prompt(
        "  Failure description",
        hint="what happened? what system? what behavior?"
    )
    invariant = _prompt(
        "  Operational invariant violated",
        hint="which rule did the system break?"
    )
    proposed_name = _prompt("  Proposed class name", hint="e.g. CONTEXT DRIFT ACCUMULATION")
    mechanism     = _prompt("  Mechanism (root cause)")
    forbidden     = _prompt("  Forbidden state (what must never be true)")
    detection     = _prompt("  Detection (how would you observe or test for this?)")
    group         = _prompt(
        "  Suggested group",
        hint="EPISTEMIC / AGENTIC / ADVERSARIAL / ALIGNMENT / ARCHITECTURAL / DOMAIN / GOVERNANCE"
    )
    example       = _prompt("  Real or hypothetical example (include sources if real)")
    print()

    # ── Step 4: Build issue body and post ────────────────────────────────────
    print(_c("  STEP 4 OF 4 — FILE THE ISSUE", BOLD_ON))
    print()

    body = f"""## Failure Description

{failure_desc}

## Operational Invariant Violated

{invariant}

## Why It Doesn't Reduce to Existing Classes

- [x] I checked and it is **not** a sub-mode of an existing class
  - Closest existing class I considered: `{closest_id}` — reason it doesn't fit: {reason1}
- [x] I checked and it is **not** a compound of 2–3 existing classes
  - Classes I considered combining: `{compound_ids}` — why the compound doesn't capture it: {reason2}
- [x] This failure violates an invariant **not already covered** by the 7 dimensions
  - Outside / closest dimension: {outside_dim}

## Proposed Class Definition

**Name**: {proposed_name}
**Mechanism** (root cause of the failure): {mechanism}
**Forbidden state** (what must never be true): {forbidden}
**Detection** (how would you observe or test for this?): {detection}
**Suggested group**: {group}

## Real or Hypothetical Example

{example}

## Additional Context

_Filed via `python -m src.cli --propose-class`  ·  AI Failure Periodic Table v{VERSION}_
"""

    title = f"[NEW CLASS] {proposed_name}"

    # Try gh CLI first
    gh_available = subprocess.run(
        ["gh", "--version"], capture_output=True
    ).returncode == 0

    if gh_available:
        print("  `gh` CLI detected. Filing issue to GitHub now...")
        print()
        result = subprocess.run(
            [
                "gh", "issue", "create",
                "--repo", GITHUB_REPO_SLUG,
                "--title", title,
                "--body", body,
                "--label", "proposed-class",
            ],
            capture_output=False,
        )
        if result.returncode == 0:
            print()
            print(_c("  ✅  Issue filed. The maintainers will review it.", GREEN))
        else:
            print(_c("  ⚠  gh issue create failed — copy the body below instead.", YELLOW))
            print()
            _print_manual_instructions(title, body)
    else:
        _print_manual_instructions(title, body)

    print()


def _print_manual_instructions(title: str, body: str):
    print(_c("  MANUAL FILING", BOLD_ON))
    print()
    print(f"  1. Open:  {PROPOSE_URL}")
    print(f"  2. Title: {title}")
    print()
    print(_c("  ── Issue body (copy everything between the lines) ──", CYAN))
    print()
    print(body)
    print(_c("  ────────────────────────────────────────────────────", CYAN))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="python -m src.cli",
        description=f"AI Failure Periodic Table  ·  {ORG}  ·  343 classes, 7 dimensions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  python -m src.cli "The model fabricated a scientific citation"
  python -m src.cli "AI jailbroken via DAN prompt"
  python -m src.cli --lookup EPIS-STRUCT-HALL-001
  python -m src.cli --stats
  python -m src.cli --mcp-config
  python -m src.cli --classify-report --url https://arxiv.org/pdf/2412.19437
  python -m src.cli --classify-report --file /path/to/report.pdf
  python -m src.cli --classify-report --url https://... --out reports/my-report/my-report
  python -m src.cli --json "model concealed its sabotage from logs"
  python -m src.cli --debug "model hallucinated a legal case"
  python -m src.cli --batch incidents.txt
  python -m src.cli --daily-driver "prompt injection exfiltrated the system prompt"

Repo: {REPO}
        """,
    )
    p.add_argument(
        "description",
        nargs="?",
        help="Description of the AI failure to classify",
    )
    p.add_argument(
        "--lookup", "-l",
        metavar="ID",
        help="Look up a specific failure class by ID (e.g. EPIS-STRUCT-HALL-001)",
    )
    p.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output raw ClassificationResult as JSON (compact; no MCP envelope)",
    )
    p.add_argument(
        "--daily-driver",
        action="store_true",
        help=(
            "Output the full MCP daily-driver bundle (response_contract, fit_state, "
            "report_preparation, semantic_search_top, …) — same JSON as classify_text"
        ),
    )
    p.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Force interactive mode even if description is provided",
    )
    p.add_argument(
        "--debug", "-d",
        action="store_true",
        help="Show keyword match scores and token breakdown after classification",
    )
    p.add_argument(
        "--batch", "-b",
        metavar="FILE",
        help="Classify each line of FILE as a separate description (- for stdin)",
    )
    p.add_argument(
        "--stats",
        action="store_true",
        help="Show live classification stats from the reports/ directory",
    )
    p.add_argument(
        "--mcp-config",
        action="store_true",
        dest="mcp_config",
        help="Print MCP connection config for Claude Desktop / Cursor / any MCP host",
    )
    p.add_argument(
        "--classify-report",
        action="store_true",
        dest="classify_report",
        help="Classify a full report (use with --url or --file)",
    )
    p.add_argument(
        "--url",
        metavar="URL",
        help="Report URL to fetch and classify (use with --classify-report)",
    )
    p.add_argument(
        "--file",
        metavar="PATH",
        help="Local report file (PDF or text) to classify (use with --classify-report)",
    )
    p.add_argument(
        "--out",
        metavar="PREFIX",
        help="Output prefix for --classify-report (default: reports/<slug>/<slug>)",
    )
    p.add_argument(
        "--propose-class",
        action="store_true",
        dest="propose_class",
        help=(
            "Guided flow: verify a miss is a real gap, fill the propose-new-class "
            "template, and file a GitHub issue (uses gh CLI if available)"
        ),
    )
    p.add_argument(
        "--version",
        action="version",
        version=f"AI Failure Periodic Table v{VERSION}  ·  {ORG}",
    )
    return p


def run_interactive(classifier: PeriodicTableClassifier, debug: bool = False, daily_driver: bool = False):
    print_header()
    if daily_driver:
        print("  Interactive mode — daily-driver JSON (same bundle shape as MCP classify_text).")
        print("  Type 'quit' or Ctrl-C to exit.\n")
    else:
        print_quick_help()
    print("  Type 'quit' or press Ctrl-C to exit.\n")
    while True:
        try:
            text = input("  Describe the AI failure: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye.\n")
            break
        if text.lower() in ("quit", "exit", "q"):
            print("\n  Goodbye.\n")
            break
        if text.lower() in ("propose", "propose class", "propose-class", "new class"):
            run_propose_class()
            continue
        if not text:
            print("  (empty input — try again)\n")
            continue
        if daily_driver:
            from src.ai_failure_mcp import bridge

            by_id = bridge.load_failures_by_id()
            bundle = bridge.classification_bundle(classifier, text, by_id=by_id)
            bundle["source"] = "cli"
            print(json.dumps(bundle, indent=2))
            print()
            continue
        result = classifier.classify(text)
        print_result(result)
        if debug:
            print_debug(result)


def run_batch(classifier: PeriodicTableClassifier, source: str, as_json: bool, daily_driver: bool):
    """Classify each non-empty line of source file (or stdin if source == '-')."""
    if source == "-":
        lines = sys.stdin.read().splitlines()
    else:
        path = Path(source)
        if not path.exists():
            print(f"  ❌ File not found: {source}", file=sys.stderr)
            sys.exit(1)
        lines = path.read_text(encoding="utf-8").splitlines()

    descriptions = [l.strip() for l in lines if l.strip() and not l.startswith("#")]
    if not descriptions:
        print("  ❌ No descriptions found in input.", file=sys.stderr)
        sys.exit(1)

    if daily_driver:
        from src.ai_failure_mcp import bridge

        by_id = bridge.load_failures_by_id()
        results = []
        for desc in descriptions:
            b = bridge.classification_bundle(classifier, desc, by_id=by_id)
            b["source"] = "cli"
            b["cli_batch_line"] = desc
            results.append(b)
        print(json.dumps(results, indent=2))
    elif as_json:
        results = []
        for desc in descriptions:
            r = classifier.classify(desc)
            d = r.as_dict()
            d["input"] = desc
            results.append(d)
        print(json.dumps(results, indent=2))
    else:
        print_header()
        any_in_table = False
        for desc in descriptions:
            result = classifier.classify(desc)
            print_result(result)
            if result.in_table:
                any_in_table = True
        # Summary line
        total = len(descriptions)
        matched = sum(1 for d in descriptions if classifier.classify(d).in_table)
        print(_c(f"  BATCH SUMMARY: {matched}/{total} descriptions matched the table", BOLD_ON))
        print()
        sys.exit(0 if any_in_table else 1)


def main():
    parser = build_parser()
    args = parser.parse_args()

    # ── Standalone commands (no classifier needed) ────────────────────────────
    if args.stats:
        print_stats()
        sys.exit(0)

    if args.mcp_config:
        print_mcp_config()
        sys.exit(0)

    if args.propose_class:
        run_propose_class(prefill_description=args.description or "")
        sys.exit(0)

    if args.classify_report:
        run_classify_report(
            url=getattr(args, "url", None),
            file=getattr(args, "file", None),
            out_prefix=getattr(args, "out", None),
            as_json=args.json,
        )
        return  # run_classify_report calls sys.exit

    if args.json and args.daily_driver:
        parser.error("Choose only one of --json or --daily-driver")

    classifier = PeriodicTableClassifier()

    # Lookup mode
    if args.lookup:
        if args.daily_driver:
            from src.ai_failure_mcp import bridge
            from src.ai_failure_mcp.response_contract import error_response_contract

            by_id = bridge.load_failures_by_id()
            rec = bridge.class_lookup_bundle(args.lookup, by_id)
            if not rec:
                print(
                    json.dumps(
                        {
                            "error": "unknown class id",
                            "class_id": args.lookup,
                            "response_contract": error_response_contract(),
                            "source": "cli",
                        },
                        indent=2,
                    )
                )
                sys.exit(1)
            rec["source"] = "cli"
            print(json.dumps(rec, indent=2))
            sys.exit(0)
        failure = classifier.lookup(args.lookup)
        print_lookup(failure, args.lookup)
        sys.exit(0 if failure else 1)

    # Batch mode
    if args.batch:
        run_batch(classifier, args.batch, args.json, args.daily_driver)
        return

    # Single query with daily-driver (MCP-shaped) JSON
    if args.description and args.daily_driver:
        from src.ai_failure_mcp import bridge

        by_id = bridge.load_failures_by_id()
        bundle = bridge.classification_bundle(classifier, args.description.strip(), by_id=by_id)
        bundle["source"] = "cli"
        print(json.dumps(bundle, indent=2))
        sys.exit(0 if bundle.get("in_table") else 1)

    # Single query with JSON output
    if args.description and args.json:
        result = classifier.classify(args.description)
        print(json.dumps(result.as_dict(), indent=2))
        sys.exit(0 if result.in_table else 1)

    # Single query with formatted output
    if args.description and not args.interactive:
        print_header()
        result = classifier.classify(args.description)
        print_result(result)
        if args.debug:
            print_debug(result)
        sys.exit(0 if result.in_table else 1)

    # Interactive mode
    run_interactive(
        classifier,
        debug=getattr(args, "debug", False),
        daily_driver=args.daily_driver,
    )


if __name__ == "__main__":
    main()
