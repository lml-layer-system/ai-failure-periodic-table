# Security Policy

## Scope

This repository contains a taxonomy of AI failure modes, a keyword-based classifier, a CLI tool, an **MCP server** (`src.ai_failure_mcp`), and maintainer scripts.
Security issues relevant to this project are:

- **Code execution vulnerabilities** in the Python classifier, CLI, MCP layer, or scripts (e.g., injection via malformed `failures.json`)
- **Dependency vulnerabilities** in packages listed in `requirements.txt` / `pyproject.toml` (including optional `mcp`)
- **Data integrity attacks** that could allow malicious actors to corrupt the `failures.json` taxonomy in ways that evade test detection
- **CI/CD pipeline vulnerabilities** in the GitHub Actions workflows
- **MCP / network exposure**: `classify_url` only allows public `http`/`https` and rejects private/link-local hosts (see `bridge.fetch_url_text`). **`classify_document`** only reads paths under the repo root and/or directories set via `AI_FAILURE_MCP_DOCUMENT_ROOT` / `AI_FAILURE_MCP_DOCUMENT_ROOTS`. The **`protection`** tool writes user preference JSON under **`~/.ai-failure-periodic-table/`** (not the repo); treat that path like other dotfile config if auditing user machines.

## Out of Scope

- Vulnerabilities in AI systems **documented** in this taxonomy — this repo describes those failures, it does not contain the AI systems themselves
- Safety issues with third-party models or APIs referenced in the enrichment data
- GitHub platform security (report those to [GitHub Security](https://github.com/security))

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Report privately to: **ryangat@lmlsystemlayer.com**

Include:
- Description of the vulnerability and its potential impact
- Steps to reproduce
- Affected files or components
- Any suggested fix if you have one

**Response SLA:**
- Acknowledgement within 48 hours
- Assessment and triage within 7 days
- Fix or workaround within 30 days for confirmed issues

## Safe Harbor

We consider good-faith security research and responsible disclosure under this policy to be:
- Authorized and conducted in a manner consistent with this policy
- Exempt from restriction under our terms of service
- Lawful activity that will not be pursued legally

We will not take legal action against researchers who discover and report vulnerabilities
in good faith, provided they do not exploit the vulnerability or expose user data.

## Acknowledgements

Confirmed security issues will be credited in the relevant release notes unless the reporter
requests anonymity.
