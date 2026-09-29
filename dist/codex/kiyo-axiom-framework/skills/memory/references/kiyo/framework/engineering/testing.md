# Testing and evidence checklist

Load when assessing coverage, selecting verification or interpreting results.
Test assess is analysis; it does not authorize test creation, execution or
environment changes. Preserve the project's actual test tools and conventions.

## KIYO-ENG-005 — Match checks to behavior, risk and observed results

| Check type | Choose when it resolves a relevant uncertainty |
| --- | --- |
| Unit | Local logic, boundary/error paths or invariants can be exercised in isolation. |
| Integration | Real component boundaries, persistence or dependency behavior matter. |
| API / contract | A public request/response, error shape or consumer compatibility changes. |
| E2E | A critical user journey depends on assembled components; use a controlled target. |
| Regression | A defect or compatibility issue needs a focused reproducer/check at the appropriate level above. |

State why a layer is selected or omitted when material to the changed behavior/risk.
Do not require every type for every change or add tests that merely mirror the
implementation. For a typo, a focused diff/document check may be sufficient.
For high-impact behavior choose stronger evidence and state gaps; coverage
percentages or a successful build alone do not establish correctness.

Before execution, inspect the actual command/config/scripts, lifecycle hooks and
transitive setup for writes, network calls, installs, data resets or migrations.
Identify target, environment, data and authorization under
[permissions](../../governance/permissions.md) and
[dangerous actions](../../governance/dangerous-actions.md). “Test” is not a safety
guarantee. Unknown shared/production targets block dependent execution while
independent analysis can continue. Use synthetic data where possible.

Establish a relevant baseline if safe and practical. Compare actual before/after
evidence, not recollection. Classify failures as evidenced baseline failures,
new regressions or environment problems; when attribution is insufficient,
record Unknown. Report each failure even if unrelated, but repair only authorized
scope under [bounded recovery](../../workflows/repair-and-handoff.md).

Record every performed or unperformed check under the nine-field
[Evidence Contract](../evidence-contract.md), including applicability, inspected
state, actual result/evidence, limitations and baseline relation. Later affected
edits require rechecks; preserve an old PASS as historical, not final-state proof.
Report baseline failures without an “all tests pass” claim.

For an unrun check state NOT_RUN and why; use BLOCKED for a concrete prerequisite.
PASS/FAIL describe the actual scoped check only. Separate static review, executed
automated/manual checks, behavioral scenarios and native host tests. Never turn
an expected example into a passing result, hide failed checks, or imply all
acceptance passed from one green check. Complete with covered behavior, uncovered
risk and the next decision where needed, without fabricating command results.

For a Test task, select assess/run/write using the [shared Test procedure](../../workflows/test.md)
and [mode/safety matrix](../test-mode-safety.md). Assessment never runs discovery
or collection scripts; run preserves tracked source/tests/config; write stays
inside requested tests/test-only fixtures. Use the relevant
[test plan](../../templates/test-plan.md) or [report](../../templates/reports/test-report.md)
without treating a mode name as native parser syntax or permission.
