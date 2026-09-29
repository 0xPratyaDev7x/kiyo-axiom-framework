# Review finding template

Use with the [reporting contract](../../framework/reporting-contract.md), in chat
unless a separate report-file write is authorized. A found bug does not permit a fix.

- **Task/scope:** <agreed review boundary/mode, inspected versus unavailable areas>
- **Actions/files changed:** <actual inspections/checks; no edit implied>
- **Governance/risk rationale:** <authority, relevant impact/data/uncertainty and risk basis>
- **Verification/evidence:** <nine-field records for actual review/check methods; tests not run remain explicit>
- **Residual issues:** <findings, uninspected areas, uncertain attribution and limitations>
- **Memory impact:** <value and scoped drift/no-delta assessment; no sync in review>
- **Status:** <review-delivery status, distinct from application correctness>
- **Next required action:** <proposed scoped fix/decision/check or none within the review scope>

**Finding ID/title:** <existing or locally assigned identifier, not a fabricated issue link>.
**Classification:** <Confirmed defect / Plausible risk / Improvement suggestion>.
**Severity:** <project scale or CRITICAL/HIGH/MEDIUM/LOW/INFO; impact-based reason>.
**Confidence:** <HIGH/MEDIUM/LOW with inspected evidence and remaining premises;
not a probability, permission or execution status>.
**File:line or range:** <actual inspected safe location and working-tree/index/
revision view; old-side revision for deletions, redaction limitation when needed>.
**Observed behavior:** <supported trigger/path and observation versus inference;
expected behavior with its source, baseline/new/unknown attribution>.
**Impact:** <affected behavior/users/data within evidence; qualify uncertain reachability>.
**Requirement/control reference:** <actual sourced ID/record or explicitly unavailable;
do not invent a business rule, acceptance criterion or clause>.
**Suggested fix:** <bounded proposal, not an applied repair or approved decision>.
**Verification idea:** <meaningful proposed check and expected outcome, marked NOT_RUN
unless actually executed within separately established scope; cite real evidence if so>.
**Review provenance:** <self-review when applicable; no independent-audit claim without evidence>.

Use the [classification/severity/confidence guide](../../framework/review-severity-confidence.md)
and [bounded review report](review-report.md). For multiple findings, put the
shared report fields once in that report rather than repeating them per issue.

If no issue is identified, state “No findings in the inspected scope” with scope
and limitations; do not invent a finding or say “no bugs” / “all tests pass.”
A completed inspection with reported findings can be DONE as Review; an
unperformed mandatory part of the agreed review cannot be hidden as a limitation.
