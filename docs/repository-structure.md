# Repository structure

```
ai-failure-periodic-table/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── data/
│   ├── failures.json          # 343 classes — fully enriched (examples, references, case_studies)
│   ├── search_index.json      # Pre-computed TF-IDF semantic search index (487KB)
│   └── embeddings_meta.json   # Search index metadata
├── src/
│   ├── classifier.py          # Core classification engine (low-ms, no ML deps)
│   ├── data_loader.py         # Load/validate failures.json
│   └── cli.py                 # CLI interface
├── index.html                 # Interactive visual periodic table (~420KB, self-contained)
├── scripts/
│   ├── generate_embeddings.py # Build TF-IDF search index from failures.json
│   ├── semantic_search.py     # CLI semantic search tool
│   ├── generate_taxonomy.py   # Auto-generate TAXONOMY.md
│   └── generate_visual.py     # Auto-generate index.html
├── tests/
│   ├── test_classifier.py     # Classifier correctness + performance tests
│   └── test_data_integrity.py # Data validation (all 343 present, schema valid)
├── .github/
│   ├── ISSUE_TEMPLATE/        # 5 structured issue templates
│   │   ├── bug_report.md
│   │   ├── propose_new_class.md
│   │   ├── challenge_classification.md
│   │   ├── report_real_incident.md
│   │   └── improve_keywords.md
│   └── PULL_REQUEST_TEMPLATE.md
├── COMPLETE_AI_FAILURE_PERIODIC_TABLE.md   # Groups 1–3 (154 failure classes)
└── PERIODIC_TABLE_CONTINUED.md            # Groups 4–7 (189 failure classes)
```

Heavy classifier outputs live under **`reports/`** (chunk JSON + Markdown summaries per source). Long-form methodology and corpus notes: **[proof.md](proof.md)**.
