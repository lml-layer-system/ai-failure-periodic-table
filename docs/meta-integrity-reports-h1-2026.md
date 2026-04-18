# Meta integrity reports (H1 2026 bundle) — official links

> **Purpose:** One-click **canonical URLs** for Meta’s **H1 2026** semiannual integrity publication (landing page updated **Mar 19, 2026**) and the **H1 2026 Adversarial Threat Report** (**Mar 11, 2026**). Use this as proof sources when mapping platform-integrity and adversarial-threat narratives to the AI Failure Periodic Table.

**Primary hub (read this first)**  
- [Integrity Reports, H1 2026](https://transparency.meta.com/reports/integrity-reports-h1-2026/) — `transparency.meta.com/reports/integrity-reports-h1-2026/`

**Reports named in that hub**

| Report | Official URL |
|--------|----------------|
| **Community Standards Enforcement** (H2 2025 data in this bundle) | [transparency.meta.com/reports/community-standards-enforcement](https://transparency.meta.com/reports/community-standards-enforcement/) |
| **Widely Viewed Content** (Q4 2025 in this bundle) | [transparency.meta.com/reports/widely-viewed-content-report](https://transparency.meta.com/reports/widely-viewed-content-report/) |
| **Content restrictions based on local law** (H2 2025 in this bundle) | [transparency.meta.com/reports/content-restrictions](https://transparency.meta.com/reports/content-restrictions/) |
| **Oversight Board** (Meta biannual update, H2 2025) | [transparency.fb.com/sr/meta-biannual-report-h2-2025](https://transparency.fb.com/sr/meta-biannual-report-h2-2025) |
| **Adversarial Threat Report** (First Half **2026**, published Mar 11) | [transparency.meta.com/sr/first-half-2026-Adversarial-threat-report](https://transparency.meta.com/sr/first-half-2026-Adversarial-threat-report/) |

**Nearby official pages**

- [All reports (Transparency Center)](https://transparency.meta.com/reports/)
- [Meta’s threat disruptions / adversarial report archive](https://transparency.meta.com/metasecurity/threat-reporting/) — chronological list including semiannual reports
- [Oversight Board — Meta recommendations tracker](https://transparency.meta.com/oversight/oversight-board-recommendations/)
- [Oversight Board — Meta biannual updates hub](https://transparency.meta.com/oversight/meta-biannual-updates-on-the-oversight-board/)

**Note:** Meta states **Government Requests for User Data** (H2 2025) will follow in the **next** half-year publication after the shift to semiannual reporting. For product/context blog items referenced from the hub (e.g. AI enforcement, scams), follow links **from** the hub page—they are Meta’s own citations.

---

## Classifier and semantic search (this repo)

Meta’s PDF/HTML is **not** vendored here. To map **their narrative** to the table using **this project’s tools**, we use short **Meta-shaped passages** (summaries aligned to the public report themes), then:

1. **Keyword classifier** — `python -m src.cli --batch reports/meta-integrity-h1-2026/passages.txt --json` → full JSON in [`reports/meta-integrity-h1-2026/classifier.json`](../reports/meta-integrity-h1-2026/classifier.json).
2. **TF‑IDF semantic search** — `python scripts/semantic_search.py "…query…" --top N --json` → companion JSON files in the same folder (`semantic-*.json`) for themes where keyword matching is too broad (e.g. the word **“fake”** alone firing legal-citation classes).

**Passages** (one line each in [`passages.txt`](../reports/meta-integrity-h1-2026/passages.txt)) and **keyword top matches** (first hit listed):

| # | Theme | Top keyword classifier match |
|---|--------|------------------------------|
| 1 | CIB / AI-generated influence / synthetic media | `ADV-DEEPFAKE-154` (SYNTHETIC MEDIA) |
| 2 | “Nudify” / non-consensual synthetic imagery ads | `DOMAIN-CITE-SPOOF-280` — **weak literal fit** (keyword noise); see semantic column |
| 3 | Moderation false-positive spike (automation bug) | `AGEN-FALSE-COMPLY-041` / strong secondary `ALIGN-OVERREFUSAL-186` |
| 4 | Local law / geoblocks / jurisdiction | `DOMAIN-JURISDICT-BLEND-281` |
| 5 | Oversight Board / transparency / notifications | `ADV-VIDEO-MANIP-150` / `GOV-LOG-MANIP-316` — mixed; see semantic |

**Semantic search (better for rows 2, 4, 5):** first hits from the saved queries:

| Query file | Top hit |
|------------|---------|
| [`semantic-nudify.json`](../reports/meta-integrity-h1-2026/semantic-nudify.json) | `ADV-DEEPFAKE-154`, then `DOMAIN-ADULT-CONTENT-296` |
| [`semantic-cib.json`](../reports/meta-integrity-h1-2026/semantic-cib.json) | `ADV-DEEPFAKE-154` |
| [`semantic-moderation.json`](../reports/meta-integrity-h1-2026/semantic-moderation.json) | `ALIGN-OVERREFUSAL-186` (over-refusal / false positives) |
| [`semantic-geo.json`](../reports/meta-integrity-h1-2026/semantic-geo.json) | `GOV-GEO-BYPASS-309` (geo restriction *as governance mechanism* — closest indexed hook; Meta’s report is compliance, not “bypass”) |
| [`semantic-oversight.json`](../reports/meta-integrity-h1-2026/semantic-oversight.json) | `GOV-TRANSPARENCY-311` |

Re-run after changing `data/failures.json` or keywords; regenerate `data/search_index.json` with `python scripts/generate_embeddings.py` if the index is missing.

---

## Mapping hint (taxonomy, not a new case study)

Meta’s **Adversarial Threat Report** narratives (CIB, scam industrialization, **AI-generated** influence assets, **“nudify”** and non-consensual intimate imagery, etc.) typically align with **existing** ADVERSARIAL, DOMAIN, GOVERNANCE, and ARCHITECTURAL mechanism classes (e.g. coordinated inauthenticity, deepfake/synthetic media abuse, fraud/scams, CSAM-adjacent harm, geo/legal restriction pipelines). Treat Meta’s document as **primary source** for **what they claim**; the periodic table remains the **mechanism** lens.
