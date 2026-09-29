# Prompt 30 final execution and coverage report

Checked **2026-09-29**. Evidence is scoped to developer-only local execution and
final delivery records. Product acceptance remains PARTIALLY COMPLETE, public
release BLOCKED. This report does not create a host or publication result.

## Actual commands and results

| Command | Exit / observed outcome | Evidence / scope |
| --- | --- | --- |
| `python -B tools/release_candidate.py --output dist/releases/p30-run-01` | 0; all six stages PASS; PACKAGE_VALIDATED_WITH_LIMITATIONS | [Pipeline](../../../dist/releases/p30-run-01/pipeline.json): exact child argv/output/timing. Two builds have equal inventories and bytes. |
| Static child command, exact candidate paths in pipeline | 0; 37 tests PASS, zero failures/errors | [Static](../../../dist/releases/p30-run-01/evidence/static.json): 16 positive groups/21 negatives. |
| Packaging child command | 0; ten PASS, one BLOCKED | [Packaging](../../../dist/releases/p30-run-01/evidence/packaging.json): PKG-08 Windows 1314 retained, ZIP-link rejection separate. |
| Release regression child command | 0; ten tests PASS, zero failures/errors | [Release regressions](../../../dist/releases/p30-run-01/evidence/release-tests.json): incomplete stages/report-write failures covered. |
| `python -B tests/audit/test_gap_audit.py --report docs/evidence/acceptance/ledger-tests-01.json` | 0; eight tests PASS, zero failures/errors | [Ledger result](ledger-tests-01.json): all 80 unchanged criteria and direct evidence references plus negative mutations. |
| `python -B tools/acceptance_handoff.py --output docs/evidence/acceptance/p30-check-02` | Read actual exit and five check outcomes in the linked record | [Handoff checks](p30-check-02/checks.json), [inventory](p30-check-02/handoff-inventory.json), [checksums](p30-check-02/SHA256SUMS). Report creation is part of the command. |

Pipeline duration: 2026-09-29T14:42:42.922052+00:00 through
2026-09-29T14:46:13.076801+00:00. Python 3.11.9,
Windows-10-10.0.26200-SP0. Source base is
f5a6b3b428eb4e7096e0620a52ee7ccdd2fbace4 on main.
Final documentation postdates the pipeline's contract snapshot; its separately
recorded hashes do not misrepresent the earlier run's files.

The final checker reads actual archives, inventories, original registry/trace,
P29 ledger, P25 observations and six P26 records. It verifies unchanged product/
pipeline inputs, version/name scope, exact source-to-package matches, eight entry
chains with four cases each, and inline links in changed delivery documents.
Its current output locators are checked structurally before their own files
are created. It writes a fresh directory and never replaces prior evidence.
It runs no host, network, model, fixture payload or publication operation.

## First attempt and correction

[First handoff attempt](p30-check-01/checks.json) exited 1 at FA-01 because
its license comparison mixed Git-normalized LF with checkout CRLF. Exact product
input hashes had already passed. [Original checker](checker-before-01.py) is
retained. The corrected check compares normalized license content while retaining
the exact worktree SHA256 invariant; no product/license byte or test gate changed.
The fresh p30-check-02 run is separate and preserves the first failure.

## Changes and retained limits

P30 changes final documentation, source/runbook/owner/trace pointers and adds one
developer-only handoff checker. It does not change canonical rules, overlays,
original requirements, LICENSE or previous evidence. New ZIPs match P29/P23.
No fake publisher/URL/version or runtime component was introduced.

Current sources revealed two additional publication-channel gaps, documented
in [owner actions](../../release/owner-actions.md) and the
[runbook](../../release/publication-runbook.md). A missing listing README and
reviewer threshold are distinct from local schema/content success. OpenAI's
local-access review-route caveat needs owner clarification; no rejection is claimed.

Static checks validate selected properties, not FULL SCHEMA VALIDATION,
comprehensive secrets detection, security certification or agent obedience.
The unchanged 48-case host suite remains NOT_RUN; no behavioral metrics measured.
P26's 72 rows retain two bounded complete Codex checks PASS and 70 NOT_RUN.
Claude discovery and Codex cache-byte checks are separate partial observations.
No full CLI or IDE target is HOST_VERIFIED.

The all-80 trace lists authored implementation independently: 78 implemented,
REQ-010/061 partial; full registered acceptance verification NOT_RUN. The final
chain marks non-payload docs/tools explicitly and links the older actual evidence
without rewriting it. Model grades/expected outputs are never actual tool traces.

SHA256 identifies content; it does not authenticate a publisher.
NOT_SIGNED / NOT_ATTESTED / NOT_PUBLISHED remain.
See [Final Acceptance](../../build/FINAL-ACCEPTANCE.md) for acceptance decision,
remaining gaps and the exact stop boundary.

