"""
AI Failure Periodic Table Classifier — CLI

Usage:
  Single query:    python -m src.cli "describe the AI failure here"
  Interactive:     python -m src.cli
  Lookup by ID:    python -m src.cli --lookup EPIS-STRUCT-HALL-001
  JSON output:     python -m src.cli --json "describe the failure"
  Daily-driver:    python -m src.cli --daily-driver "describe the failure"  # same JSON as MCP classify_text
  Debug mode:      python -m src.cli --debug "describe the failure"
  Batch mode:      python -m src.cli --batch failures.txt
"""

import sys
import json
import argparse
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


def print_header():
    print()
    print(_c(THICK, CYAN))
    print(_c("  AI FAILURE PERIODIC TABLE CLASSIFIER             ", BOLD_ON))
    print(_c("  343 Classes | 7 Dimensions                       ", ""))
    print(_c(THICK, CYAN))


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

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="AI Failure Periodic Table Classifier",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m src.cli "The model fabricated a scientific citation"
  python -m src.cli "AI jailbroken via DAN prompt"
  python -m src.cli --lookup EPIS-STRUCT-HALL-001
  python -m src.cli --json "model concealed its sabotage from logs"
  python -m src.cli --debug "model hallucinated a legal case"
  python -m src.cli --batch incidents.txt
  python -m src.cli --batch incidents.txt --json
  python -m src.cli --daily-driver "prompt injection exfiltrated the system prompt"
  python -m src.cli --lookup ADV-INDIRECT-INJECT-122 --daily-driver
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
    return p


def run_interactive(classifier: PeriodicTableClassifier, debug: bool = False, daily_driver: bool = False):
    print_header()
    if daily_driver:
        print("  Interactive mode — daily-driver JSON (same bundle shape as MCP classify_text).")
    else:
        print("  Interactive mode — type a failure description and press Enter.")
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
