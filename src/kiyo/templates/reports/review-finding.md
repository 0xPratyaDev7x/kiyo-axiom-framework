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
**Location/evidence:** <actual safe file/line/symbol and observation>.
**Trigger and impact:** <concrete affected behavior, supported severity and uncertainty>.
**Expected versus observed:** <criterion/source and actual discrepancy; label inference>.
**Reproduction/check:** <actual observation or clearly proposed/unrun method>.
**Recommendation:** <bounded proposal, not an applied fix or approved decision>.
**Review provenance:** <self-review when applicable; no independent-audit claim without evidence>.

If no issue is identified, state “No findings in the inspected scope” with scope
and limitations; do not invent a finding or say “no bugs” / “all tests pass.”
A completed inspection with reported findings can be DONE as Review; an
unperformed mandatory part of the agreed review cannot be hidden as a limitation.
