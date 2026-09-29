# Prompt 29 — actual audit and regression evidence

Checked **2026-09-29**. Runtime Verification: **Verified — developer tooling only**.
Audit/fix scope DONE; general release BLOCKED. This is self-review, not an
independent audit or native/behavioral acceptance.

Baseline: main, HEAD f5cb303b1713ce6f103760c0cad05fcd7e086fcf, initially clean.
Commands ran from the repository root. Python 3.11.9;
Windows-10-10.0.26200-SP0. The user's earlier no-quota restriction remains in force.
No host/model, global installation, credentials, network probe, signing,
publication, commit/tag/push or consumer Memory operation occurred.

## Actual executions and retained failures

All report paths below are fresh; prior results were not overwritten. Command
argv/output/exit/times are in the linked JSON. Tests of rejected synthetic input
are distinct from actual agent behavior. Unit mocks never count as a real build.

| Actual command | Exit | Observed result / evidence |
| --- | --- | --- |
| python -B tests/release/test_release.py --report docs/evidence/gap-audit/release-before.json | 1 | Nine methods, ten failing subtests expose incomplete/reordered stage acceptance; [record](release-before.json) |
| python -B tests/release/test_release.py --report docs/evidence/gap-audit/release-after.json | 0 | Nine methods PASS after exact-stage guard; [record](release-after.json) |
| python -B tools/release_candidate.py --output dist/releases/p29-run-01 | 0 | First real rehearsal: six stages, 37 static and nine release regressions PASS; packaging ten PASS/one BLOCKED; [record](../../../dist/releases/p29-run-01/pipeline.json) |
| python -B tests/audit/test_gap_audit.py --report docs/evidence/gap-audit/ledger-tests-01.json | 0 | Eight ledger tests PASS against first candidate and then-current ledger; [record](ledger-tests-01.json) |
| python -B tests/release/test_release.py --report docs/evidence/gap-audit/report-write-before.json | 1 | Ten methods, one error proves readiness I/O failure escapes after success record; [record](report-write-before.json) |
| python -B tests/release/test_release.py --report docs/evidence/gap-audit/report-write-after.json | 0 | Ten methods PASS after honest report-output failure handling; [record](report-write-after.json) |
| python -B tools/release_candidate.py --output dist/releases/p29-run-02 | 0 | Final real rehearsal: six stages, 37 static and ten release regressions PASS; packaging ten PASS/one BLOCKED; [record](../../../dist/releases/p29-run-02/pipeline.json) |
| python -B tests/audit/test_gap_audit.py --report docs/evidence/gap-audit/ledger-tests-final.json | 0 | Eight ledger tests PASS against final candidate/current ledger; [record](ledger-tests-final.json) |

Final pipeline UTC interval: **2026-09-29T14:28:56.893334+00:00** through
**2026-09-29T14:31:14.763330+00:00**. Its child commands, actual exits and raw
developer test output are in pipeline.json; individual reports preserve exact
assertions. The final source snapshot binds current tools/fixtures/trace and
actual Git base. Later build-state/report edits do not change product or tooling;
the closure audit rechecks current references, trace and source hashes.

Two preliminary read-only inspection commands failed (an omitted UTF-8 decoding
argument and Bash brace syntax in PowerShell); corrected reads succeeded. These
were inspection-tool errors, not product/test failures, and changed no files.
The two release defects above are independently reproduced developer defects,
not baseline application failures, flaky tests or native agent incidents.

## Check scope, interpretation and residual limits

All checks in this table are required for the P29 delivered audit/fix scope.
Exact method/command and evidence location are linked above or in the table.
Baseline relation: unchanged P23 product input bytes; changed developer guards
tested against retained pre-fix failures. No unrelated failing test was removed.

| Check | Inspected scope / observed outcome | Status | Evidence / limitations |
| --- | --- | --- | --- |
| Requirement completeness | 80 original criteria, implementing locations, procedures, cases and scoped evidence; 22 invariants; 13 gaps with action/owner/blocking scope | PASS | [Audit](../../build/FINAL-GAP-AUDIT.md), [ledger](../../build/requirement-audit.json), eight ledger tests; human semantic self-review, not agent adherence |
| Release failure guards | Each required stage, order, duplicates, unnamed/unknown entries and non-PASS outcomes; readiness-write error now records exit 1/FAIL | PASS | Ten release tests, failing records retained; synthetic local tests do not prove host safety |
| Static contracts | 16 positive groups and all 21 existing exact-reason negatives; three actual fresh candidate archives | PASS | [Static results](../../../dist/releases/p29-run-02/evidence/static.json); selected properties, not FULL SCHEMA VALIDATION |
| Reproducible packaging / isolation | Two builds produce equal complete inventories/ZIP bytes; extracted 794/795/794 files, eight Skills each, contained references and shared canonical parity | PASS | [Inventory](../../../dist/releases/p29-run-02/artifact-inventory.json), [inspection](../../../dist/releases/p29-run-02/payload-inspection.json), [packaging checks](../../../dist/releases/p29-run-02/evidence/packaging.json); cooperative source guard is not OS sandbox |
| Real filesystem symlink probe PKG-08 | Windows denied local symlink creation, winerror 1314 | BLOCKED | Existing ZIP symlink/traversal rejection passes; do not claim this probe or POSIX OS execution passed |
| Product identity / runtime exclusion | 112 product inputs unchanged; source/overlay/LICENSE and archive hashes match P23; runtime dependencies empty, no hooks/MCP/executables/fixtures/scripts/private project state shipped | PASS | Final inventory, closed allowlist and 21 negatives; bounded pattern checks are not exhaustive secret detection |
| Source/context budgets | 68 controls, eight entries, all measured canonical/native entry/bootstrap budgets retained | PASS | G06/G14 actual observations; word/line budgets are Kiyo criteria, not measured token overhead or host limits |
| Current docs / build closure | Case-sensitive relative references, corrected literal worked paths, current 80 trace rows, owner/next-prompt markers, preserved index/HEAD/LICENSE/product/historical evidence | PASS | [Closure record](closure-audit-final.json); local Markdown/hash review, external URLs not freshly revalidated |
| P25 behavior / complete native workflows | No new agent/model turn or host invocation performed | NOT_RUN | Existing 48 host cases and per-target records remain unchanged; native live state NOT_TESTED or documented UNSUPPORTED, with prior bounded subsets retained |

The checksums in [SHA256SUMS](../../../dist/releases/p29-run-02/SHA256SUMS)
identify actual bytes, not publisher identity. Both P29 real runs retain P23
archive hashes. Version UNSET; signature NOT_SIGNED; attestation NOT_ATTESTED;
NOT_PUBLISHED. The dependency/attribution inventories are ordinary inventories,
not formal SBOMs or license clearance.

Implementation status now reflects authored content (78 IMPLEMENTED, two partial),
while every full registered acceptance method remains NOT_RUN. Nine open gaps
retain release/target/owner/test limits. Static PASS cannot upgrade those outcomes.
No critical host incident is fabricated from missing execution; actual future
unauthorized destruction, secret exposure or fake results remain release blockers.

Memory Impact **NONE**; no developer-project Memory existed or was initialized.
[Fix changelog](fix-changelog.md) and [target recommendations](../../build/FINAL-GAP-AUDIT.md#per-target-readiness-recommendation)
bound the result. Safe to continue: **YES for requested Prompt 30**; release stays
BLOCKED and no further host/quota/publication authorization is inferred.


The first inline closure check exited 1 while writing its report because a loop
variable shadowed the destination path. [Failure record](closure-audit.json)
retains the executed audit source and observed exception; no successful closure
is inferred from that attempt. The corrected writer uses a distinct destination
variable and writes the [fresh final record](closure-audit-final.json).
