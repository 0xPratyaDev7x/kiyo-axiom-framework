# Completeness-audit ledger checks

Developer-only standard-library tests for the Prompt 29 audit record. They read
the 80 unchanged acceptance criteria, actual files/case IDs, current static
results and product hashes. They do not launch a host, evaluate an agent or
certify the meaning of Markdown.

```text
python -B tests/audit/test_gap_audit.py --report <fresh-developer-report.json>
```

Eight tests cover complete IDs and assessment fields, actual references/cases,
omission/duplicate rejection, weakened criteria, unowned gaps, false full PASS,
missing/escaping paths, unauthorized release promotion and unchanged product
input/archive hashes. Negative mutations are in-memory synthetic data, never
changes to the requirements or installed product. This checker is deliberately
pinned to the P29 ledger and final candidate; future acceptance needs a deliberate
new record, not replacement of historical results.

See [audit](../../docs/build/FINAL-GAP-AUDIT.md) and
[actual regression evidence](../../docs/evidence/gap-audit/validation-report.md).
