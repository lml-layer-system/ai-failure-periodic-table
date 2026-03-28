"""
AI Failure Periodic Table Classifier — CLI

Usage:
  Single query:    python -m src.cli "describe the AI failure here"
  Interactive:     python -m src.cli
  Lookup by ID:    python -m src.cli --lookup EPIS-STRUCT-HALL-001
  JSON output:     python -m src.cli --json "describe the failure"
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
    print(f"  Severity:  {failure.get('severity', 'STANDARD')}")
    print()
    print(f"  Mechanism: {failure['mechanism']}")
    print(f"  Forbidden: {failure['forbidden']}")
    print(f"  Detection: {failure['detection']}")
    print()
    print(f"  Keywords:  {', '.join(failure.get('keywords', [])[:12])}")
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
        help="Output result as JSON",
    )
    p.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Force interactive mode even if description is provided",
    )
    return p


def run_interactive(classifier: PeriodicTableClassifier):
    print_header()
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
        result = classifier.classify(text)
        print_result(result)


def main():
    parser = build_parser()
    args = parser.parse_args()

    classifier = PeriodicTableClassifier()

    # Lookup mode
    if args.lookup:
        failure = classifier.lookup(args.lookup)
        print_lookup(failure, args.lookup)
        sys.exit(0 if failure else 1)

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
        sys.exit(0 if result.in_table else 1)

    # Interactive mode
    run_interactive(classifier)


if __name__ == "__main__":
    main()
