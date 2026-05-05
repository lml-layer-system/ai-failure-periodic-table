# Developer testing and maintainer pipelines

## Test suite

```bash
pip install pytest
python -m pytest tests/ -v
```

The suite is **pytest**-driven; many checks are parametrized (so `pytest --collect-only` reports a large number). It exercises at least:

- Known failure classification and non-failure rejection
- Determinism and performance (low-ms thresholds)
- Data integrity (all 343 classes present, full schema validation)
- Mitigation field completeness
- External incident recall — **100%** on 49 documented real-world AI failures phrased as reporters, researchers, and users described them (not using taxonomy vocabulary)

## Case study companion maps

In-repo narrative companions used across validation and documentation:

- [Project Glasswing](project-glasswing.md)
- [Agentic misalignment / insider threats (Lynch et al.)](agentic-misalignment-insider-threats.md)

## Freshness Watch

[Freshness Watch](freshness-watch.md) runs a scheduled, **review-only** pipeline from public feeds through the classifier. It does **not** automatically edit the taxonomy.

## MCP daily driver

[MCP daily driver](mcp-daily-driver.md) documents how to plug **Cursor**, **Claude Desktop**, or other MCP hosts into the same read-only table.

**What the guide covers:** where to connect, what you get back (hit/miss, classes, compound hints, structural mitigations, next steps), and setup paths by host.

**Tools** (read-only; no taxonomy writes): `classify_text`, `classify_url`, `classify_document`, `classify_document_path`, `search_failures`, `get_class`, `compound_hint` — with `classifier_hit`, `response_contract`, and CONTRIBUTING-grounded `report_preparation`.

**End-user orientation** also lives in the main [how-to-use.md](how-to-use.md) and [mcp-daily-driver.md](mcp-daily-driver.md) pages.
