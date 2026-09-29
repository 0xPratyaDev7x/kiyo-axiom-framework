# Packaging and payload isolation tests

These are developer-only, offline tests for Prompt 23. Execute the existing
[runner](test_distributions.py) from the repository root with Python:

```text
python -B tests/packaging/test_distributions.py --report <fresh-evidence-path.json>
```

The runner uses only standard-library tools. It creates fresh temporary folders
with spaces, builds three ZIPs twice, compares full inventories, extracts regular
members safely and runs a copied standalone verifier with original-source reads
denied. It never launches a native AI host, installer or suspicious product code.

| IDs | Test contract |
| --- | --- |
| PKG-01 | Identical canonical/overlay/tool inputs produce byte-identical inventories and ZIPs |
| PKG-02-claude/codex/copilot | Fresh extracted payload matches canonical transform and generated tree; eight entries and contained references remain readable with source access denied |
| PKG-03 | Twelve invalid payload variants must fail: resource closure, exact case, absolute/encoded escape, metadata, disallowed content and shared-rule drift |
| PKG-04 | LF/CRLF variants retain reference semantics in each isolated extraction; byte hashes need not match across variants |
| PKG-05 | Traversal, absolute, symlink and case-collision ZIP members are refused before extraction |
| PKG-06 | Synthetic excluded secrets/state/dev content cannot enter output; unknown product input fails closed |
| PKG-07 | Equal build is a timestamp-preserving no-op; changed output is refused; separate synthetic human state remains untouched |
| PKG-08 | When OS privilege permits, a real source filesystem symlink is rejected; report BLOCKED otherwise, never PASS |
| PKG-09 | Canonical controls, templates, legal content, eight-skill inventory and fixed regular-file ZIP metadata are inspected |

A zero exit indicates required assertions completed and a report was written;
inspect every recorded status, including the extra OS-dependent PKG-08 probe.
Unexpected assertion failure exits nonzero. Results apply to the exact input/tool
hashes, not subsequent edits. See [actual results and limits](../../docs/evidence/packaging/package-checks.md).

The read guard tests a cooperative verifier and is not an OS security boundary.
Case-sensitive dictionary/ZIP tests are distinct from native POSIX execution.
Static directives, synthetic state preservation and file parity do not establish
agent compliance or native update/uninstall behavior. Those remain separately
scoped behavioral/live work; do not promote these PASS results.
