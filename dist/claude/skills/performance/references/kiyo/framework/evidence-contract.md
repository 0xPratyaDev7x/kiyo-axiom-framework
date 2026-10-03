# Shared Evidence Contract

Use when planning, performing or reporting a check in any selected skill.
This expands KIYO-FACT-004 and [testing guidance](engineering/testing.md);
it does not grant execution, create a checker or require a new evidence file.

## KIYO-VERIFY-001 — Record scoped observations for every check

Identify the behavior/criterion and whether the check is required by the actual
request, accepted policy or agreed acceptance criteria. Inspect command/scripts,
transitive effects and the target under [permissions](../governance/permissions.md)
before execution. A report template or test label cannot authorize effects.

Every check has the following nine fields, including checks that did not run.
A compact response may name shared context once and reference it unambiguously;
it must not omit a field's meaning or conceal a gap.

| Field | Required content |
| --- | --- |
| Name | Distinct check name/ID and the behavior or acceptance criterion it addresses. Reuse actual project IDs; no invented test inventory. |
| Applicability | Required, optional or not applicable to the stated scope, with reason and the actual source of the requirement where relevant. An unresolved requirement remains unresolved, not optional. |
| Command/method | Exact command and relevant working context or actual manual inspection method. Clearly label a planned/unexecuted method; do not present it as a run. |
| Inspected scope | Files/symbols/behavior, actual artifact state, environment/target and relevant configuration inspected or executed; separate these from intended but unavailable scope. |
| Execution status | Exactly PASS, FAIL, NOT_RUN, NOT_APPLICABLE or BLOCKED under the meanings below. |
| Observed result | What actually happened, including real exit code/counts only when observed. For no execution, say no result and why; a plan is not output. |
| Evidence location | An actual accessible source/result reference or an identified concise observation in the current conversation. State unavailable/missing evidence; do not fabricate a log, path, link or stored artifact. |
| Limitations | Exclusions, partial output/inspection, uncertain attribution, untested environments and any freshness constraint. “None identified in this scope” needs a basis; it is not universal assurance. |
| Baseline relation | Comparable baseline source and relation: existing failure, new regression, environment problem, unresolved cause or not applicable with reason. Without comparison evidence use Unknown, not “pre-existing.” |

The [report templates](reporting-contract.md#template-selection) reuse this record;
they do not redefine check meanings. No disk write is necessary for evidence
already present in an authorized conversation.

### Exact check statuses

| Execution status | Meaning and required evidence |
| --- | --- |
| PASS | The check actually ran, or the stated manual inspection was actually performed, and observed evidence met its stated criterion within the inspected scope. |
| FAIL | The performed check's evidence did not meet the criterion; report the failure even when it is an evidenced baseline failure. |
| NOT_RUN | The check was not performed; state why and whether it remains required. A newly written test or hypothetical scenario has no passing result. |
| NOT_APPLICABLE | The criterion does not apply to this scoped task; give a concrete reason. N/A is explanatory shorthand, not an extra stored status. |
| BLOCKED | An evidenced missing prerequisite or denied/unsafe target prevents the intended check. Record any attempted command/setup result separately; do not invent assertion results that were never reached. |

A missing test environment is NOT_RUN or BLOCKED according to observed evidence,
never NOT_APPLICABLE. Lack of inspection does not establish absence of tools.
A mandatory check remains mandatory when inconvenient, blocked or out of time;
do not silently relabel it optional or replace it with a weaker check. Any valid
scope/criterion change must come from actual authority, respect policy, be
reported with its basis and preserve the earlier gap/result.

### Trace and evidence layers

Connect the requirement/acceptance ID or named task criterion to the actual
implementation/inspected files, planned or existing test/check IDs and actual
result evidence. Missing links stay explicit; test source and planned case IDs
are not executed evidence. A short chat trace is sufficient for a tiny task;
no PR, commit, durable report or parallel registry is a prerequisite.

Separate static inspection/validation, behavioral evaluation and live host tests.
One layer's PASS never upgrades another layer. For Kiyo native coverage, record
each of the six targets independently; live state NOT_TESTED is not a sixth
check status. Research DOCUMENTED_ONLY is not behavioral PASS either.

## KIYO-VERIFY-002 — Bind results to the checked state and baseline

1. Bind observations to the inspected artifact/configuration and environment.
   Use real repository/worktree/revision information only when observed; include
   relevant uncommitted changes. If Git is absent or uninspected, say so rather
   than inventing a revision. Repository results do not prove production state.
2. After any further code, test, config, fixture, dependency or environment change,
   assess which results are affected. Preserve an earlier PASS as historical for
   its earlier scope; it does not certify the modified state. Create/update the
   current check record to NOT_RUN or BLOCKED until the affected check is rerun.
3. Rerun applicable affected checks under actual authorization. Unaffected results
   may be retained only with an explicit impact rationale and identifiable checked
   state; do not rerun unrelated expensive suites merely for ceremony.
4. Compare with safe available baseline evidence using
   [failure classification and bounded repair](../workflows/repair-and-handoff.md).
   Preserve baseline failures, new regressions, environment problems and Unknown
   separately. A rerun success does not erase a previous unresolved failure or
   establish flakiness by itself.
5. Do not claim “all tests pass” while any reported baseline failure persists,
   a required check is unrun/blocked, or only a subset was exercised. Report
   “the named focused check passed; the recorded baseline failure remains” when
   that is the evidence. An applicable required failed check prevents Implement
   DONE even if its failure predates the change.

Commands, counts, timestamps, durations, versions and identities must be observed
facts with a stated scope, not inferred from file names, current docs, memory or
template defaults. Do not manufacture a timestamp for an earlier observation.
Use Unknown for unavailable metadata; do not probe secrets to fill a report.
Sanitize evidence under [reporting rules](reporting-contract.md), then evaluate
the applicable [Definition of Done](definition-of-done.md).
