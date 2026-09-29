# Prompt 23 packaging evidence

Checked 2026-09-29. Scope: three development distributions, developer packaging
and payload inspection. **Static artifact checks PASS** within the boundaries
below; one additional OS-dependent negative test is BLOCKED. Native loading,
agent behavior and native update/uninstall were not executed.

Source baseline: main at 90880886cfb6ad895cefceb478314ea6c3a031a7; initial index
and worktree clean. Existing LICENSE preserved. Actual worktree inputs, tooling
hashes, archive/member digests and 456 parity records are in the
[artifact inventory](artifact-inventory.json). Git describes a base revision,
not production state or a signature.

## Actual commands and results

```text
python -B tests/packaging/test_distributions.py --report docs/evidence/packaging/test-results.json
python -B tests/packaging/test_distributions.py --report docs/evidence/packaging/test-results-final.json
python -B tools/package_distributions.py
```

The first retained report covers the pre-clarification snapshot. After canonical
managed-block scope/cleanup wording and parity inventory generation changed, the
entire suite was rerun; only [test-results-final.json](test-results-final.json)
covers final package bytes. Both completed commands returned exit 0 while preserving
PKG-08 BLOCKED in their result data; exit 0 does not mean all checks passed.

Before those retained reports, two runs exited 1 because the new verifier
mistook https:// for a drive path and a neutral <a locator ...> placeholder for
an HTML link. These were new checker false positives, corrected by narrowing
the patterns after inspecting the matching text. No product rule was weakened
to pass them. An initial requirements-print command also encountered console
encoding error and was repeated with UTF-8; it made no files.

Final environment: Python 3.11.9, Windows-10-10.0.26200-SP0. The report records
actual UTC time, tool hashes and base commit. No native host/version/account was
rechecked in this prompt; P20–22 observations retain their own dates and limits.

A final read-only inline Python audit and git diff --check passed after correcting
one documentation link to the existing Claude protocol. They checked 32 modified
and 15 new files, 2,549 Markdown files, 18,178 local links, 80 requirement rows,
112 allowlisted inputs and all 456 parity records. The wrapper was also rerun
against the final destination: output_created false, with identical digests.

| Check | Applicability / method / inspected scope | Status / observed result | Baseline relation and limitations |
| --- | --- | --- | --- |
| PKG-01 | Two fresh CLI builds; all three complete output inventories and archives | PASS: inventories and ZIP bytes identical | Final canonical/overlay inputs identical between builds; not a cross-toolchain determinism claim |
| PKG-02-claude | Fresh space-containing extraction; standalone -I/-B verifier; input/body/copy comparisons | PASS: 794 files, eight skills, 97 shared files per skill, 4,956 contained links; outside source probe DENIED | Canonical parity including updated managed guidance; no Claude invocation |
| PKG-02-codex | Same independent offline procedure for Codex | PASS: 795 files, eight skills, 97 shared files per skill, 4,956 links; source probe DENIED | Selected-field checks only; historical ingestion FAIL remains; IDE plugins UNSUPPORTED |
| PKG-02-copilot | Same independent offline procedure for Copilot | PASS: 794 files, eight skills, 97 shared files per skill, 4,964 links; source probe DENIED | Neither CLI nor VS Code behavior inferred |
| PKG-03 | Twelve synthetic invalid payloads: missing Core, case mismatch, traversal/encoded escape, absolute path, metadata, forbidden components and copy drift | PASS: all rejected | Synthetic tests, no actual credentials; lexical validation is not a security proof |
| PKG-04 | Extract LF and CRLF variants for each artifact and run isolated verifier | PASS: all six variants retain expected contained-link counts | Input bytes/digests differ by design; not a claim of identical hashes for different input bytes |
| PKG-05 | Synthetic ZIP traversal, absolute path, symlink and case-collision entries | PASS: all four refused before extraction | Published ZIP members are regular 0644 files only; no native installer exercised |
| PKG-06 | Synthetic source with nine excluded canaries; unlisted product Markdown | PASS: canaries cannot affect ZIPs; unknown product file refused | Exact allowlist does not replace human review for sensitive prose within approved files |
| PKG-07 | Identical output rerun, differing output, five synthetic project state files | PASS: no-op preserves hashes/timestamps; overwrite refused; state unchanged | Proves developer tools' write boundaries, NOT native update/uninstall or Init behavior |
| PKG-08 | Additional real filesystem source-symlink negative probe | BLOCKED: Windows error 1314 creating a symlink | No privilege elevation attempted; ZIP symlink rejection and actual regular-file inventory passed independently |
| PKG-09 | Canonical inventory, legal copy and fixed ZIP metadata | PASS: 105 product files, 68 controls, 34 templates, eight skills per artifact | Counts are inspected values; fixed archive epoch is not a real build timestamp |

## Isolation and reference interpretation

The copied standalone verifier imports no repository modules. During inspection,
its cooperative Python audit guard denies content and directory reads outside the
extracted payload; a deliberate read of original src/kiyo/KIYO.md fails with
PermissionError. It also denies subprocess/network side effects. The parent
test harness separately compares canonical hashes; it is not the isolated reader.

This establishes the checker did not need original source files. It is **not an
OS sandbox**, a hostile-code containment claim or native host isolation evidence.
All inspected outputs are regular files; ZIP symlink members are rejected. The
extra real filesystem symlink probe was unavailable and remains BLOCKED.

Paths use exact-case ZIP/member dictionaries and a POSIX-style lexical resolver;
wrong-case links and case collisions are rejected even on Windows. This is an
actual case-sensitive path test, not an actual Linux/macOS filesystem or host run.
Native POSIX execution is NOT_RUN. No source directory was renamed or hidden,
no ACLs changed, and no global settings were modified.

The verifier checks current inline Markdown links/fragments, selected frontmatter,
shared snapshots, budgets, absolute developer/home locators and closed component
paths. Prose/example project locators are not blindly treated as payload links.
Optional HTTPS citations are never fetched. It does not scan every possible
secret format or prove benign semantic behavior.

## Final artifacts and parity

[Three ZIPs and full hashes](parity-report.md#artifacts-and-limitations) total
2,383 files across the three payloads. The
[parity matrix](parity-report.md) maps every control/skill independently to six
targets through 456 generated inventory records. All packaged behavioral records
remain NOT_RUN. Native mechanisms retain DOCUMENTED_ONLY/UNKNOWN/UNSUPPORTED
from [the activation matrix](../../compatibility/activation-matrix.md);
all six Kiyo live target results are still NOT_TESTED.

One canonical file changed for explicit managed scope, outdated-Core reporting
and block-only cleanup; its 24 distributed copies were mechanically refreshed
after confirming they matched the pre-task source bytes. All other canonical
content, native overlays, old builders and other previous payload files remain
unchanged. Prior P20–22 inventories are dated historical snapshots; they do not
certify the updated files. The P23 inventory is the current comparison authority.

No developer tool or test ships in a payload. User policy/Memory remain outside
installed cache, no consumer bootstrap was written, no release version selected,
and no plugin was installed, signed or published. Owner name/license/publisher/
destination decisions and Codex IDE treatment remain open. Full native release
acceptance is not the completion criterion of this scoped packaging task.
