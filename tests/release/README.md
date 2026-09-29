# Release-tool regressions

Developer-only Python standard library checks; synthetic local files and no host,
network, credentials, signing or publishing. Run with a fresh report path:

```text
python -B tests/release/test_release.py --report <fresh-developer-report.json>
```

The [suite](test_release.py) checks eight properties: unset version remains an
owner gate; mixed versions/type mismatches are rejected; identity mismatch is
rejected; output escape/overwrite is refused with human bytes preserved;
failed/blocked evidence cannot become unqualified PACKAGE_VALIDATED; a failed
pipeline retains NOT_SIGNED/NOT_PUBLISHED error evidence; static tests read the
explicit candidate and reject an escaping archive path; dependency/attribution
inventory avoids fabricated runtimes and owner license approval.

These are regression checks for the new release tooling, not eight agent cases.
Temporary fixtures are retained for inspection. The pipeline also runs the
existing static and packaging suites; mandatory negatives remain intact.
See [runbook](../../docs/release/runbook.md) and
[actual results](../../docs/evidence/release/validation-report.md).
