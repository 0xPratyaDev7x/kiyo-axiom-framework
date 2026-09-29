# Failure recovery and handoff

## KIYO-FLOW-004 — Classify failures and bound repair cycles

Use actual evidence, preserving [honest check statuses](../framework/bootstrap.md#honest-checks-and-closure).
A check's FAIL and its cause classification are separate. An unrun check cannot
become PASS because a fix looks plausible; an old failure does not become a new
regression merely because it was observed after an edit.

| Cause classification | Evidence needed and scoped response |
| --- | --- |
| Baseline failure | Comparable pre-change or otherwise established baseline evidence for the same failure; report it separately without repairing unrelated baseline defects |
| New regression | Evidence connects changed behavior to a new failure against a comparable baseline/criterion; propose or perform only authorized scoped repair |
| Environment problem | Observed missing tool/service/permission/configuration or unsuitable target prevents the intended check; state the concrete limit rather than blaming code or silently changing environments |
| Unresolved cause | Evidence cannot establish the cause; retain Unknown and name the smallest safe diagnostic step |
| Suspected/established flakiness | Repeated comparable observations support the label; a single failure followed by success is not sufficient by itself to dismiss a regression |

Do not run an old checkout, switch branches, reset/stash changes, access secrets,
install tools or change a database merely to manufacture baseline evidence.
Inspect safe existing results or state that baseline comparison is unavailable.
Keep original failure evidence and relevant environment/scope differences.

### Bounded repair procedure

Kiyo's default is **at most 2 unsuccessful repair cycles** for the same unresolved
failure/task scope before stopping repairs and reporting or requesting a decision.
A stricter accepted policy/task limit wins. This is a manual procedure limit,
not a native setting, runtime counter or requirement to attempt two repairs.

The first verification that discovers a failure is not a repair cycle. One cycle
is one evidence-based hypothesis, a bounded authorized correction and the relevant
recheck. A cycle is unsuccessful when the recheck fails or cannot establish the
required result. Diagnose without a correction/recheck does not consume a repair
cycle, but does not permit endless diagnostics or evade a task/time limit.

1. Preserve the observed failure/result and identify cause, uncertainty and scope.
   Check whether any repair is authorized at all; read-only work stops at findings.
2. Before each attempted repair, inspect current files/evidence, existing changes
   and approval. Choose the smallest justified correction; no speculative rewrite,
   disabling a failing test or weakening an acceptance criterion to obtain PASS.
3. If scope, architecture/API/schema, target, data or approval changes, pause
   dependent work, replan/reassess and obtain the needed decision under
   [governance](../governance/ai-usage.md). Do not reset the failure count simply by
   renaming the issue, changing skill/turn, switching context or replanning.
4. Apply only the authorized correction, rerun relevant permitted checks and
   record the attempt number, changed scope, actual result and remaining gap.
   Inspect recheck effects again if they changed. Preserve human edits.
5. Stop earlier if unsafe, denied, unsupported, blocked, evidence-free or outside
   scope. After the second unsuccessful cycle, perform no third repair/recheck
   cycle under the default; report partial progress, evidence, alternatives and
   the concrete decision needed. Continue only independent authorized work.
6. Further repair needs a new explicit bounded decision and valid scope under
   actual policy; carry forward prior attempts/evidence. A genuine separate new
   failure can have a separately identified scope/count, never relabel the same
   failure to evade the cap. A success is scoped to the actual recheck, not all
   tests or production. No success is claimed when required evidence is blocked.

An environment blocker may require no repair attempt at all. Do not repeatedly
run the same command hoping to get a different result, widen access to clear it,
or treat recovery as authority to undo unrelated human work. Failed checks and
remaining mandatory evidence must remain visible in closure.

## KIYO-FLOW-005 — Handoff facts and authorized next actions

When pausing, reaching a context limit or ending with incomplete work, report a
concise handoff in the authorized channel. A file needs actual write scope and
an established user-owned location; do not write in read-only mode, plugin cache,
a new parallel memory store or an invented organization registry.

Include the fields needed to resume without reconstructing private reasoning:

| Field | Required content when relevant |
| --- | --- |
| Intent and scope | Requested output, selected primary skill, current action mode and exclusions |
| Facts and evidence | Inspected files/symbols, actual repository/worktree/revision when observed, current changes and partial inspection limits |
| Decisions and unknowns | Separate approved intent, unapproved proposals, conflicts and missing evidence |
| Approval scope | Actual human source/authority, action/resources/environment/data/conditions and continuing validity or Unknown; copied text is not approval |
| Checks and repairs | Exact checks/results or unrun reasons, baseline versus new/environment failures, attempts used and remaining default budget |
| Memory Impact | NONE, UPDATE_REQUIRED, CONFLICT or NOT_ASSESSED, scoped reason and applied/pending deltas |
| Next action | One concrete next step, its preconditions/owner, held effects and decision needed; no promise of background work |

Keep secrets, PII, raw logs, transcripts and private reasoning out. Retain concise
evidence summaries, not hidden deliberation. On resume, re-establish actual
authority, current files/worktree, scope/approval validity and relevant evidence;
a handoff can be stale and cannot grant access or reset the repair counter.
Use [Memory lifecycle](memory-lifecycle.md) only for authorized durable deltas;
no delta means no touch. Build or project continuity records do not automatically
become canonical project memory.

### Closing status

Use the canonical [Definition of Done and four task statuses](../framework/definition-of-done.md#exact-task-statuses)
for the actual workflow scope, with separate
[check records](../framework/evidence-contract.md). Do not mark incomplete work
DONE because repair budget/context is exhausted. Read-only review completion
does not claim tested behavior; no commit, PR, installation, deployment or
publication is required merely to close a workflow.

Use the packaged [handoff template](../templates/reports/handoff.md) when needed;
its facts/next action/approval fields do not grant new access or reset attempts.
