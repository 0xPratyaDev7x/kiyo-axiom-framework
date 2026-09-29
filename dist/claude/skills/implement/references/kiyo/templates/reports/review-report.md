# Bounded review report template

Use in chat by default under the [reporting contract](../../framework/reporting-contract.md).
Populate only observed evidence. Compact reviews may combine fields; keep scope,
unrun checks, limitations and status visible. No report file is implicitly created.

- **Task/scope:** <request, root/component, supplied comparison/files; actual
  index/working-tree/revision views and included staged/unstaged/untracked scope;
  unavailable/excluded material; known baseline versus missing comparison>
- **Actions/files changed:** <files/context actually inspected; no changes made
  by this review; distinguish pre-existing human/AI edits without guessed authorship>
- **Governance/risk rationale:** <read authority, G1 Observe, separate contextual
  risk/data/uncertainty rationale; any held execute/output transition>
- **Verification/evidence:** <the check record below; test source inspected versus
  execution, actual methods/results and baseline relation>
- **Residual issues:** <prioritized findings, dimension coverage/gaps, unresolved
  requirements, unavailable safeguards and limits>
- **Memory impact:** <NONE / UPDATE_REQUIRED / CONFLICT / NOT_ASSESSED, relevant
  checked entries/evidence, proposed correction or conflict; no Memory writes>
- **Status:** <DONE / PARTIALLY COMPLETE / BLOCKED / DECISION REQUIRED for the
  original review scope, with reason; not application or repair completion>
- **Next required action:** <bounded proposed fix/check/decision and missing scope,
  or none for the completed review deliverable; no automatic implementation>

## Findings and coverage

Use the [finding template](review-finding.md) for each issue. Keep Confirmed
defect, Plausible risk and Improvement suggestion identifiable; order by supported
impact and state confidence with its basis. For no findings say “No findings
identified in <actually inspected scope>”; for zero diff say “No changes found
in <inspected change sets>.” Include limitations in either case.

Account for the ten [review dimensions](../../workflows/review.md#ten-review-dimensions)
at proportional depth: inspected evidence, uninspected gaps, or reason for genuine
non-applicability. Group unaffected dimensions for a tiny change rather than
filling a large empty table. Missing requirements/environment are evidence gaps.

## Check record

Repeat/combine as needed; semantics come from the
[Evidence Contract](../../framework/evidence-contract.md).

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <check> | <required/relevant/inapplicable with reason> | <actual method, or proposed and not run> | <view/revision/files> | <PASS/FAIL/NOT_RUN/NOT_APPLICABLE/BLOCKED> | <actual observation or no execution> | <safe source/location> | <uninspected/uncertain> | <known baseline/new/unknown/inapplicable with reason> |

Build/tests not executed in Review stay **NOT_RUN — read-only scope**. A separate
requested execution that cannot proceed identifies its blocker honestly. Test
files and old/supplied successes do not prove this state passed. Mandatory missing
review scope prevents DONE; a delivered bounded review can be DONE with findings.
