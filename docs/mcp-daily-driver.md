# Daily-driver AI and the periodic table (MCP)

**This page is for people who use an AI assistant every day** (Cursor, Claude Desktop, or another tool that supports **MCP**) and want that assistant to **classify real text against the 343-class AI Failure Periodic Table** on demand.

You do **not** need to already know what MCP stands for. Think of it as a **plug-in socket**: your AI host connects to a small program in this repo, and then your AI can call “classify this paragraph / link / file” for you.

---

## What this is for

- **Personal, on-demand layer:** You point your everyday AI at something you are reading or writing—a paragraph, a news article (URL), or a file—and ask it to **test whether it hits the table** and **which class(es)** apply.
- **Separate from Freshness Watch:** [Freshness Watch](freshness-watch.md) is the repo’s **scheduled** maintainer pipeline (feeds → review packets). The daily driver is **you + your AI**, anytime, on **your** text. They do not replace each other.
- **Connect your workspace to the table:** Once the plug-in is configured, your AI can use the same taxonomy the project ships in `data/failures.json`—without you manually copying class IDs from the website.
- **What you can see in results (in plain terms):**
  - **Did it hit?** Yes or no (whether at least one class passed the project’s keyword classifier).
  - **What class(es)?** Primary and related matches, plus a “closest” list when nothing quite hits.
  - **Compound or not?** Whether several **structural dimensions** fired at once (a combined / multi-mechanism reading).
  - **Structural fix pattern:** For each class, the taxonomy’s own **what went wrong**, **what must not happen**, **how to notice it**, and **structural mitigation** (ideas expressed as *what* to enforce—not a vendor how-to checklist).
  - **If it does not fit cleanly:** Plain-language **what to do next**, aligned with [CONTRIBUTING.md](../CONTRIBUTING.md) (for example: improve keywords, report a real incident, or propose a new class after the checklist).

---

## Read-only and explicit

- **Does not edit this repository** and **does not change the taxonomy** on disk.
- **Does not submit issues or open PRs** by itself.
- **For your own workflow:** exploration, drafting, auditing, teaching.
- **Official taxonomy changes** still go through the project’s normal review process on GitHub.

---

## What you get (before “how to install”)

| You want to… | What the connection enables |
|--------------|------------------------------|
| Paste a failure description | Your AI can run **classify text** and show hit / miss, classes, and structural fields. |
| Point at a public web page | Your AI can **fetch the URL** (public `http`/`https` only), extract text, and classify it. |
| Point at a file | Your AI can classify a **UTF-8 file** under the repo or a folder you allow (see below). |
| Browse by meaning without a full verdict | Your AI can **search** classes by similarity (helpful for exploration; a full “hit” still comes from classifying your actual narrative). |
| Look up one class by ID | Your AI can **fetch that row** from the table (lookup is not the same as classifying a story). |

**Choose the setup path that matches the AI tool you already use** (next section). The *purpose* is the same in every case: **plug your daily-driver AI into the table**, then **point it at something and classify**.

---

## Connect your daily-driver AI

**This is where you plug in:** you add this repository’s MCP server to the **AI application you already use every day**. That application (the “host”) starts our small Python process and talks to it over a standard channel; you stay in chat or the editor as usual.

### Cursor

1. Install the repo and Python dependencies (see [How to install and run](#how-to-install-and-run) below).
2. In Cursor, open **Settings**.
3. Find **MCP** (or **Model Context Protocol** / **MCP servers**, depending on your Cursor version).
4. **Add a new MCP server** and paste a config block like the one in [Minimal config example](#minimal-config-example-cursor--other-hosts) (fix the `cwd` path to your clone).
5. Save and restart MCP or Cursor if the app asks you to.

After that, your Cursor agent can call tools such as “classify this text” using the periodic table.

### Claude Desktop

1. Install the repo and Python dependencies the same way as for Cursor.
2. Open **Claude Desktop** settings and find where **MCP servers** or **Developer** / connector configuration is documented for your version (Claude Desktop uses a JSON config file on your machine to register MCP servers).
3. Register a server entry with the same **`command`**, **`args`**, and **`cwd`** idea as in [Minimal config example](#minimal-config-example-cursor--other-hosts): run `python3` with `-m src.ai_failure_mcp` and working directory = **absolute path to this repo**.
4. Restart Claude Desktop if required.

Exact menu names move between releases; search “Claude Desktop MCP configuration” in Anthropic’s help if the location changed.

### Any other MCP-compatible host

If your tool says it supports **MCP over stdio**, the pattern is always:

- **Command:** `python3` (or `python` on your system)
- **Arguments:** `-m`, `src.ai_failure_mcp`
- **Working directory:** the **root of this git repository** (where `pyproject.toml` lives)

Your host’s docs will show *where* to paste that. The behavior of the tools is the same.

### Advanced: run the server yourself (stdio)

For debugging, you can run from a terminal:

```bash
python3 -m src.ai_failure_mcp
```

Do not type into that process; your MCP **host** attaches to it. This path is mainly for contributors and troubleshooting.

---

## Choose your setup path

Pick one; you do not need all of them.

| Path | Best if you… |
|------|----------------|
| **Cursor** | Live in the editor and want the agent to classify text, URLs, or paths inside your project. |
| **Claude Desktop** | Use Claude as your main daily assistant and want the same tools there. |
| **Another MCP host** | Already use a product that documents MCP connectors. |
| **Local stdio only** | Are developing or debugging the server; not the usual “daily driver” setup. |

---

## How to install and run

From a **clone of this repository**:

```bash
pip install -e ".[mcp]"
```

Build the search index once (needed for search and for extra context inside classify tools):

```bash
python scripts/generate_embeddings.py
```

The host runs the server with:

```bash
python3 -m src.ai_failure_mcp
```

—or, after install, `ai-failure-mcp` (same thing).

### Minimal config example (Cursor & other hosts)

Replace `/absolute/path/to/ai-failure-periodic-table` with your real path.

```json
{
  "mcpServers": {
    "ai-failure-periodic-table": {
      "command": "python3",
      "args": ["-m", "src.ai_failure_mcp"],
      "cwd": "/absolute/path/to/ai-failure-periodic-table"
    }
  }
}
```

A copy-paste template with an optional personal-notes folder lives at [cursor-mcp-config.example.json](cursor-mcp-config.example.json).

---

## Now try this (first use)

1. **Finish setup** so your host lists the `ai-failure-periodic-table` MCP server without errors.
2. In chat, ask your AI something concrete, for example:
   - “Use the periodic table MCP to **classify this paragraph**: …”
   - “**Classify this URL** against the AI failure table: https://…”
   - “**Classify the document** at `notes/incident.md` (if that path is allowed).”
3. **Read the answer with these in mind:**
   - **Hit or miss:** Did the table’s classifier accept at least one class?
   - **Which class:** What is the primary label (ID and human-readable name)?
   - **Compound:** Does the result suggest more than one structural dimension is active?
   - **Structural response:** What pattern does the taxonomy attach to that class (mechanism, forbidden, detection, mitigation)?
   - **If weak or no fit:** What does **“what to do next”** suggest (keywords, incident report, checklist for a new class)?

After one successful round trip, the point of the system should feel obvious: **your daily AI can now “ask the table” the same way the maintainers’ tooling does.**

---

## What the results mean (plain language)

When your AI returns a classification bundle:

- **`classifier_hit` / `in_table`:** **Yes** = at least one class met the project’s keyword bar for your text. **No** = none did; you still get **closest** candidates to compare.
- **Why it hit (roughly):** Scores on keyword matches, which of the **seven dimensions** lit up, and optional similarity hints—the authoritative **accept/reject** is the table’s own classifier, not a second hidden engine.
- **`fit_state` (short summary):** e.g. strong vs weak in-table hit, compound-style reading, or **possible gap** when nothing hit—useful labels, not a separate taxonomy.
- **`suggested_structural_response`:** The **WHAT** from the table for a class (mechanism, what must not happen, how to detect it, structural mitigation). Not step-by-step product advice.
- **If it does not fit cleanly:** Fields like **`what_to_do_next`**, **`boundary_pressure_note`**, and **`report_preparation`** map you toward the repo’s real contribution paths (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

For machine-readable rules about what each field *means*, see **`response_contract`** in the JSON (schema version, whether a real verdict applies, etc.).

---

## Tools reference (for when you read JSON or tool names)

| Tool | Purpose |
|------|---------|
| `classify_text` | Classify free text; full envelope (hit/miss, classes, dimensions, structural fields, next steps). |
| `classify_url` | Fetch a public **http(s)** URL, extract text, then classify (blocks private/local hosts). |
| `classify_document` | Read a **UTF-8** file under the **repo root** and/or **`AI_FAILURE_MCP_DOCUMENT_ROOT(S)`**, then classify. |
| `classify_document_path` | Same as `classify_document` (alias name for some clients). |
| `search_failures` | TF-IDF similarity search over classes—**exploration**, not a full narrative verdict (`response_contract.verdict_applicable`: false). |
| `get_class` | Look up one class by ID—**record lookup**, not classifying a story (`verdict_applicable`: false). |
| `compound_hint` | Same pipeline as classify, with extra emphasis when **multiple dimensions** activate. |

### Technical: classifier verdict and `response_contract`

The periodic-table **keyword classifier** decides **hit vs miss**. TF-IDF / semantic lists are **advisory context**; they do not override `classifier_hit`. Every payload includes **`response_contract`** (`schema_version`, `verdict_applicable`, and roles of fields). Classification responses set `verdict_applicable: true`; search and lookup set it `false` and tell you to run `classify_*` on your narrative for a real verdict.

### Boundary pressure and CONTRIBUTING-shaped next steps

On weaker or miss results you may see:

- **`boundary_pressure_note`** — what is uncertain.
- **`what_to_do_next`** — grounded in [CONTRIBUTING.md](../CONTRIBUTING.md).
- **`recommended_repo_action`** / **`report_preparation`** — structured hints if you or your AI draft a GitHub issue (templates under `.github/ISSUE_TEMPLATE/`).

### Suggested structural response (WHAT, not HOW)

Per class, taxonomy fields only: mechanism, forbidden, detection, mitigation (and mitigation domain when present). No vendor runbooks.

---

## Personal documents outside the repo

By default, `classify_document` only sees files under the **repository root**. To allow a **personal folder** (for example notes on disk), set in your MCP config’s `env`:

- **`AI_FAILURE_MCP_DOCUMENT_ROOT`** — one absolute directory, or
- **`AI_FAILURE_MCP_DOCUMENT_ROOTS`** — several paths, separated by **`:`** (or **`;`** if a path contains `:`).

Example with an extra notes directory:

```json
{
  "mcpServers": {
    "ai-failure-periodic-table": {
      "command": "python3",
      "args": ["-m", "src.ai_failure_mcp"],
      "cwd": "/absolute/path/to/ai-failure-periodic-table",
      "env": {
        "AI_FAILURE_MCP_DOCUMENT_ROOT": "/Users/you/Documents/ai-failure-notes"
      }
    }
  }
}
```

This does **not** relax URL safety (still no localhost / private fetches).

---

## Security notes

- **`classify_url`:** Only `http`/`https`; blocks loopback, private, and link-local targets.
- **`classify_document`:** Path must resolve under the repo and/or your configured document roots.

---

## Doctrine (short)

- **One acceptance gate:** the table’s classifier; other signals inform explanation and CONTRIBUTING-style next steps.
- **Daily driver is read-only** on the taxonomy; **Freshness Watch** is the scheduled maintainer-facing feed pipeline.
