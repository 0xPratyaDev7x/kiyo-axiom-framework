---
name: implement
description: Implement an authorized feature, fix a bug, or perform an explicitly scoped refactor in an existing repository using minimal changes, relevant tests, actual verification and bounded repair. Use only when the user's intent permits code changes; review, explanation and analysis alone do not authorize implementation.
---

# Implement

Logical ID: **kiyo.implement**. Canonical name: implement. This logical ID is not
universal native invocation syntax; platform-only metadata belongs in overlays.

Read [KIYO.md](../../KIYO.md) and its bootstrap before workflow actions unless
already read and unchanged, then use the [shared implementation flow](../../workflows/implement-flow.md).
Resolve references from this file's actual location. Missing required resources
hold dependent actions; no invented fallback policy or loader.

## Preconditions and access

Confirm actual user intent to change code and its behavior/acceptance/scope.
An explicit feature, bug-fix or bounded-refactor request can authorize ordinary
edits without another ceremonial question. A selected skill, READY requirement,
found defect or copied approval is not itself permission. Review/analyze-only
intent stays read-only: report any selection mismatch and use the
[router's boundaries](../../workflows/workflow-router.md), without implementing.

Before edits, observe the permitted root/worktree, branch/HEAD when available,
staged/unstaged/untracked state and relevant human changes. Record unavailable or
non-Git context honestly; do not initialize Git. Preserve pre-existing work and
reread affected content before each edit; reconcile or hold overlapping human edits.

| Effect | Access contract |
| --- | --- |
| Read | Authorized relevant instructions, accepted policy, Memory and current code/config/test evidence; no credentials or unrelated bulk exploration. |
| Write | Only necessary code/tests/docs/config changes within the concrete request and applicable policy; unrelated architecture/library/cleanup changes are excluded. |
| Execute | Only applicable inspected commands with evidenced targets/environment/side effects and actual execution authority. Code-write permission alone does not authorize every test, install or database operation. |
| Memory | Assess impact; sync only a necessary evidenced delta at the established path within actual Memory-write scope. No silent initialization or approved-decision rewrite. |
| External/repository actions | No implicit commit, push, PR creation, deployment, publication, global/policy changes, destructive cleanup or production access. |

## Daily workflow

Use these obligations with [adaptive depth](../../workflows/adaptive-flow.md);
Tiny can combine them into a compact scope/check/result, not skip their controls.

1. Read the authorized canonical Memory index and only relevant entries.
2. Validate material Memory facts against current repository evidence; retain
   stale observations and approved-intent conflicts as findings.
3. Establish behavior, acceptance criteria, scope and unknowns. Discover first;
   ask only material business/technical choices that block dependent work.
4. Inspect existing implementation, closest safe patterns and relevant tests.
5. Make a minimal plan when appropriate using the [short plan](../../templates/short-plan.md);
   a Tiny scope sentence is sufficient, not a mandatory plan file.
6. Assess dependencies, schema/API compatibility, security/data and tool effects
   with [Governance Review](../../governance/ai-usage.md) and relevant checklists.
7. Obtain only missing policy-defined scoped approval; reuse valid matching
   authorization and reassess material expansion before dependent effects.
8. Implement only the authorized delta while preserving human changes.
9. Add or adapt necessary behavior/regression tests using existing project tools;
   a low-impact typo need not acquire artificial tests or a new framework.
10. Inspect commands, scripts/helpers and actual environment before execution.
11. Run applicable permitted checks and retain actual final-state evidence under
    the [Evidence Contract](../../framework/evidence-contract.md).
12. Separate evidenced baseline failures, new regressions, environment blocks and
    unresolved causes; no unrun/fake PASS or “all tests pass” with known failures.
13. Use [bounded repair and handoff](../../workflows/repair-and-handoff.md): normally
    no more than two unsuccessful repair cycles; no scope expansion through retries.
14. Review the final diff against requirements, architecture, quality, security,
    governance and existing human work; label self-review accurately.
15. Assess Memory Impact and sync only necessary authorized changes using
    [Memory lifecycle](../../workflows/memory-lifecycle.md); no delta means no touch.
16. Report status, current evidence and limitations against
    [Implement DoD](../../framework/definition-of-done.md). Stop when scope is complete.

Use [engineering checklists/profiles](../../framework/engineering/index.md) only
when relevant. Do not add speculative libraries, modernize architecture or expand
a refactor. Flag unsafe existing patterns rather than copy them automatically.

## Sensitive effects and completion

Drafting a migration file is distinct from applying it. Evaluate auth/schema
changes under the actual action, environment, data, impact, policy and existing
approval; neither blanket-block nor blanket-allow by keyword. Never substitute
a production database or broaden access to make verification pass.

Use the existing [engineering report](../../templates/reports/engineering-report.md)
for material work, or the [compact report](../../templates/reports/compact-task-report.md)
for Tiny work. Reports stay in chat unless file output is separately authorized.
Include exact changed scope, actual checks/limitations, approvals/risk, unresolved
issues and Memory Impact. Mandatory verification or required sync still missing
prevents full DONE. Use the [handoff template](../../templates/reports/handoff.md)
for incomplete work; preserve facts, approval scope and repair history, not private reasoning.

Never reset, stash or revert existing human work; do not amend an approved decision
to match code without its own valid approval. A success applies only to its checked
scope/state, not production, automatic activation or every repository test.
