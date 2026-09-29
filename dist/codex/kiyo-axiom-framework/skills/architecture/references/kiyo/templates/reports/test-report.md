# Test report template

Use in chat by default with the [reporting contract](../../framework/reporting-contract.md)
and [Test procedure](../../workflows/test.md). A compact report may combine fields;
keep scope, actual results and required gaps explicit. No report file, artifact
archive, provider/model identity or tool-access count is implied.

- **Task/scope:** <requested assess/run/write phases, criteria, component, inspected/
  executed state, chosen test layers and included/excluded cases>
- **Actions/files changed:** <actual inspections, authored test/fixture paths,
  executed checks and observed artifacts; source/human changes preserved or
  unexpected effects reported; distinguish proposals from completed actions>
- **Governance/risk rationale:** <actual mode/effects, independent G-level and
  action risk/reason, non-production target/data, approval reuse or held effects>
- **Verification/evidence:** <nine-field records below; actual command, scope and
  result, measured counts/coverage or explicit absence; source inspection is not run>
- **Residual issues:** <skipped/blocked cases, baseline failures/new regressions/
  environment problems/Unknown cause, required unrun checks and unassessed areas>
- **Memory impact:** <NONE / UPDATE_REQUIRED / CONFLICT / NOT_ASSESSED with scope,
  evidence and proposed pending correction; no implicit sync in any Test mode>
- **Status:** <DONE / PARTIALLY COMPLETE / BLOCKED / DECISION REQUIRED for the
  original mode deliverable, separately from each check's outcome>
- **Next required action:** <specific authorized next step or missing decision/
  prerequisite; no automatic production fix, install or widening of the suite>

## Check records

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <criterion/check> | <required/optional/inapplicable with reason> | <actual command and working context; proposed unrun commands labeled> | <state, tests/filters, non-production target and artifacts> | <PASS/FAIL/NOT_RUN/NOT_APPLICABLE/BLOCKED> | <actual output/exit, meaningful counts or not available> | <safe result/source location or conversation observation> | <partial/uninspected/blocked scope> | <evidenced baseline/new/environment/Unknown; no inferred regression> |

Follow [Evidence Contract](../../framework/evidence-contract.md) status meanings.
Missing environment is BLOCKED/NOT_RUN, not N/A. Tests written but unexecuted
remain NOT_RUN. A later affected edit makes an earlier result historical until
the relevant check is rerun. Keep baseline failures even when a focused check passes.

## Counts and coverage when observed

- **Runner outcomes:** <actual selected/collected/executed/passed/failed/skipped/
  expected-failure/retry counts as reported, with suite/filter and source; unavailable
  values remain Unknown; planned case count is separate>
- **Skipped/blocked:** <named affected check/case and observed reason; do not infer
  zero skips from silence or mark unexecuted cases passed>
- **Coverage:** <measured metric/value, actual tool/method, checked state and included/
  excluded files or branches, evidence location; otherwise “not measured”>
- **Baseline/freshness:** <comparable result and relevant environment/state differences;
  earlier results after later edits or reruns do not automatically establish current
  success, regression or flakiness>

Do not invent a denominator, percentage, duration, version or command result.
A runner's exit zero with no relevant tests selected does not meet a required
behavior criterion. Assess DONE is analysis delivered; run-report DONE may include
FAIL results if the requested output was execution and reporting. Authoring-only
DONE may have NOT_RUN checks when execution was not required; authored tests do
not establish passing behavior. Missing mandatory verification or requested phases
prevent full completion under [DoD](../../framework/definition-of-done.md).
