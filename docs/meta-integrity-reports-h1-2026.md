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

## Live classifier run — official **PDF** (Adversarial Threat Report)

The Transparency URL serves a **PDF** (not an HTML article). This repo **does not commit** that binary; it is downloaded locally as `reports/meta-integrity-h1-2026/adversarial-h1-2026-live-official.pdf` (gitignored) when you run the script below.

**Reproduce (needs `curl` + Poppler `pdftotext` on `PATH`):**

```bash
python scripts/classify_external_report.py \
  --url https://transparency.meta.com/sr/first-half-2026-Adversarial-threat-report/ \
  --out-prefix reports/meta-integrity-h1-2026/adversarial-h1-2026-live
```

**Committed outputs** (from the real report text, chunked ~1400 chars, **keyword** `PeriodicTableClassifier` per chunk):

| Artifact | Role |
|----------|------|
| [`adversarial-h1-2026-live-source.txt`](../reports/meta-integrity-h1-2026/adversarial-h1-2026-live-source.txt) | `pdftotext -layout` extract + provenance header |
| [`adversarial-h1-2026-live-chunks.json`](../reports/meta-integrity-h1-2026/adversarial-h1-2026-live-chunks.json) | Every chunk → top matches, scores, previews |
| [`adversarial-h1-2026-live-summary.md`](../reports/meta-integrity-h1-2026/adversarial-h1-2026-live-summary.md) | Top-1 class histogram + chunk index |

**Interpretation:** the keyword classifier is tuned for **short incident-style mechanism descriptions**, not full PDF prose. Long chunks will **over-trigger** some classes (substring collisions). Use the histogram and per-chunk previews as **exploratory** signal; for cleaner mapping, paste **short excerpts** into `python -m src.cli` or `scripts/semantic_search.py`.

---

## Mapping hint (taxonomy, not a new case study)

Meta’s **Adversarial Threat Report** narratives (CIB, scam industrialization, **AI-generated** influence assets, **“nudify”** and non-consensual intimate imagery, etc.) typically align with **existing** ADVERSARIAL, DOMAIN, GOVERNANCE, and ARCHITECTURAL mechanism classes (e.g. coordinated inauthenticity, deepfake/synthetic media abuse, fraud/scams, CSAM-adjacent harm, geo/legal restriction pipelines). Treat Meta’s document as **primary source** for **what they claim**; the periodic table remains the **mechanism** lens.
