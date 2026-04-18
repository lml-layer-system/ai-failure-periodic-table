"""
AI Failure Periodic Table — MCP Server

This is the daily-driver / eyes layer.

Its job is classification, structural interpretation, and
reading. It does not enforce anything. It does not fuse
with any protection system.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ROLE SEPARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  AI Failure Periodic Table  →  eyes / daily-driver
  Agent Buccet (or any other
  protection body the user
  chooses)                   →  optional separate runtime
                                protection, enforce-only
  The human                  →  bridge into UPL / law

  These systems do not fuse. The Periodic Table works
  without Buccet. Buccet works without the Periodic Table.
  A user may choose a completely different protection body.

  If the user wants to protect something they find in the
  daily-driver:
    1. they see the classification result
    2. the daily-driver AI can help draft the exact UPL
       wording for their chosen rule
    3. the human decides what belongs in their UPL
    4. the human places it into their protection body
    5. the protection body enforces it

  The daily-driver never writes into any protection body
  directly. The human is always the bridge.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  BUCCET COEXISTENCE (if user runs both)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  If a user chooses to run both MCPs in the same host,
  Buccet's acceptance lane ACCEPT.CURATED.CAPABILITY.2044
  (targetPattern: "buccet-failure-classifier") prevents a
  logic collision: the classifier's failure-term payloads
  would otherwise hit Buccet's own denial patterns.

  The server name "buccet-failure-classifier" is the only
  contract point. Do not change it without also updating:
    agent-buccet/lib/agent-buccet/list-v-acceptance.ts
    → namedLane ACCEPT.CURATED.CAPABILITY.2044

  Running both is optional. This server works standalone.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Usage (standalone):

  {
    "mcpServers": {
      "buccet-failure-classifier": {
        "command": "python",
        "args": ["-m", "src.mcp_server"],
        "cwd": "/path/to/ai-failure-periodic-table"
      }
    }
  }
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from .classifier import PeriodicTableClassifier

# ─────────────────────────────────────────────────────────────────────────────
# Server — identity is the contract point with Agent Buccet
# ─────────────────────────────────────────────────────────────────────────────

mcp = FastMCP("buccet-failure-classifier")

_classifier = PeriodicTableClassifier()

# ─────────────────────────────────────────────────────────────────────────────
# Setup state — asked once automatically, changeable anytime by the user
# ─────────────────────────────────────────────────────────────────────────────

_SETUP_PATH = Path(os.path.expanduser("~/.ai-failure-periodic-table/setup.json"))


def _load_setup() -> dict:
    try:
        return json.loads(_SETUP_PATH.read_text())
    except Exception:
        return {}


def _save_setup(data: dict) -> None:
    _SETUP_PATH.parent.mkdir(parents=True, exist_ok=True)
    _SETUP_PATH.write_text(json.dumps(data, indent=2))


def _setup_complete() -> bool:
    return "protection_choice" in _load_setup()


# ─────────────────────────────────────────────────────────────────────────────
# Protection tool — asked once at start, user can call anytime to change
# ─────────────────────────────────────────────────────────────────────────────

@mcp.tool()
def protection(choice: str) -> dict:
    """
    Set or check protection preference. Asked once automatically on first use.
    The user can call this anytime to turn protection on, off, or check status —
    the answer is never locked.

    Args:
        choice: "yes"    — enable Agent Buccet (shows config + full CLI info)
                "no"     — no protection, or bring your own enforcement runtime
                "status" — show current preference

    Returns current state and next steps.
    """
    if choice == "status":
        setup = _load_setup()
        if not setup:
            return {
                "protection_active": False,
                "question": (
                    "Do you want runtime protection? "
                    "Reply 'yes' for Agent Buccet or 'no' to skip / bring your own. "
                    "You can change this anytime."
                ),
            }
        return {
            "protection_active": setup.get("protection_choice") == "yes",
            "protection_choice": setup.get("protection_choice"),
            "note": "You can call protection('yes') or protection('no') anytime to change this.",
        }

    if choice not in ("yes", "no"):
        return {"error": "choice must be 'yes', 'no', or 'status'"}

    _save_setup({"protection_choice": choice})

    if choice == "yes":
        return {
            "protection_active": True,
            "next_step": (
                "Add Agent Buccet to your MCP host config. "
                "It auto-initializes and runs in headless mode — "
                "no console needed, silent boundary enforcement from first connection."
            ),
            "config": {
                "mcpServers": {
                    "buccet": {
                        "command": "buccet",
                        "args": ["mcp"],
                    }
                }
            },
            "customize": (
                "Full CLI available once Buccet is running: "
                "`buccet console` — operator console, "
                "`buccet laws` — see your acceptance and denial pack, "
                "`buccet upl import <file>` — add your own rules, "
                "`buccet where` — full operator map."
            ),
            "upl_note": (
                "To make a classification result a standing rule: "
                "ask your AI to draft the UPL wording, "
                "you decide what goes in, place it via `buccet upl import`. "
                "Nothing is written automatically."
            ),
            "change_anytime": "Call protection('no') anytime to turn this off.",
        }

    return {
        "protection_active": False,
        "note": (
            "No protection active. "
            "Add your enforcement runtime to your MCP host config whenever you're ready — "
            "Agent Buccet (`buccet mcp`) or any runtime of your choice."
        ),
        "change_anytime": "Call protection('yes') anytime to enable Agent Buccet.",
    }


# ─────────────────────────────────────────────────────────────────────────────
# Tools
# ─────────────────────────────────────────────────────────────────────────────

@mcp.tool()
def classify(description: str) -> dict:
    """
    Classify an AI failure description against the 343-class Periodic Table.

    Returns verdict (YES/NO), activated dimensions, top matching failure
    classes with mechanism, detection method, severity, and match score.

    If protection setup has not been completed yet, a one-time prompt is
    included. After setup is done, results are clean classification output only.

    Args:
        description: Natural language description of the AI behavior or failure.
    """
    result = _classifier.classify(description)
    out = result.as_dict()

    if not _setup_complete():
        out["_protection_prompt"] = (
            "Do you want runtime protection? "
            "Call protection('yes') for Agent Buccet or protection('no') to skip. "
            "This prompt won't appear again once you answer — "
            "but you can call protection() anytime to change your choice."
        )

    return out


@mcp.tool()
def lookup(failure_id: str) -> dict:
    """
    Look up a specific failure class by its exact ID.

    Args:
        failure_id: Periodic Table class ID, e.g. "EPIS-STRUCT-HALL-001"

    Returns:
        Full failure class record including mechanism, forbidden behavior,
        detection method, keywords, examples, references, and case studies.
        Returns {"found": false, "failure_id": "..."} if not found.
    """
    failure = _classifier.lookup(failure_id)
    if failure is None:
        return {"found": False, "failure_id": failure_id}
    return {"found": True, **failure}


@mcp.tool()
def list_dimensions() -> dict:
    """
    List the 7 structural dimensions of the AI Failure Periodic Table.

    Returns the dimension codes, names, and diagnostic questions used
    during classification. Useful for understanding the table's structure
    before running a classification.

    Returns:
        {
          "total_classes": 343,
          "dimensions": [
            {
              "number": 1,
              "code": "EPISTEMIC",
              "question": "Does it involve truth, knowledge, or reasoning failures?"
            },
            ...
          ]
        }
    """
    from .classifier import QUESTIONS
    return {
        "total_classes": 343,
        "dimensions": [
            {
                "number": q_num,
                "code": group_code,
                "question": question,
            }
            for q_num, group_code, question in QUESTIONS
        ],
    }


@mcp.tool()
def batch_classify(descriptions: list[str]) -> dict:
    """
    Classify multiple AI failure descriptions in a single call.

    Args:
        descriptions: List of natural language failure descriptions.

    Returns:
        {
          "total": int,
          "in_table_count": int,
          "results": [
            {"input": "...", "verdict": "YES|NO", "in_table": bool,
             "dimensions_activated": [...], "top_matches": [...]}
          ]
        }
    """
    results = []
    in_table_count = 0
    for desc in descriptions:
        r = _classifier.classify(desc)
        d = r.as_dict()
        d["input"] = desc
        results.append(d)
        if r.in_table:
            in_table_count += 1
    out = {
        "total": len(descriptions),
        "in_table_count": in_table_count,
        "results": results,
    }
    if not _setup_complete():
        out["_protection_prompt"] = (
            "Do you want runtime protection? "
            "Call protection('yes') for Agent Buccet or protection('no') to skip. "
            "This prompt won't appear again once you answer — "
            "but you can call protection() anytime to change your choice."
        )
    return out


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
