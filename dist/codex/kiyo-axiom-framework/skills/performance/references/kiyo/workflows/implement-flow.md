# Shared implementation flow

## KIYO-FLOW-002 — Sequence authorized changes through actual evidence

Use this flow for the Implement primary skill and relevant authorized write
portions of another selected skill, without relabeling it or expanding scope.
Test authoring can use the same change/check discipline. Analysis-only work uses
[read-only flow](read-only-flow.md); do not run these implementation stages there.
This procedure is advisory Markdown, not a runnable pipeline.

Logical order:

**Permission preflight → Authorized Memory orientation → Understand →
Inspect + validate relevant memory → Plan → Assess risk/governance →
Human decision when required → Implement → Verify → Review →
Memory impact/sync → Complete**

[Adaptive depth](adaptive-flow.md) may combine explanations and omit inapplicable
ceremony, never the controls behind these stages. If evidence invalidates an
earlier premise, return to the affected stage before dependent effects.

| Stage | Action and required scoped evidence |
| --- | --- |
| Permission preflight | Establish intent, permitted reads/writes/execution, accepted policy and actual host limits. Observe current repository/worktree and human changes where authorized. Identify immediately apparent sensitive/forbidden effects before reading or acting. |
| Authorized Memory orientation | Discover the existing canonical path and read the index/relevant entries within read permission. Note scope, approved intent and unknowns; do not treat this first read as verification or initialize missing memory. |
| Understand | Identify requested behavior/output, acceptance evidence, constraints and genuine unknowns. Separate Facts, Assumptions, Proposals, Approved decisions and Unknowns where material; ask only blocking questions after permitted discovery. |
| Inspect + validate relevant memory | Inspect current relevant code/config/tests and accepted records, closest safe patterns and command effects. Compare material memory claims; report stale observations or approved-decision conflict without rewriting intent. |
| Plan | Name the minimal intended change, affected areas, scope exclusions and applicable checks; use the [short plan](../templates/short-plan.md) only at useful depth. A Tiny task can use a compact scope sentence; a plan is not approval. |
| Assess risk/governance | Use actual action/target/environment/data/reversibility/blast radius/users/uncertainty. Apply separate G-mode, risk and relevant security checklist. Reassess findings that change scope or evidence requirements. |
| Human decision when required | Resolve material business/approved-intent conflicts and missing policy-defined scope approval. Prepare the concrete permitted proposal first; reuse authentic still-matching human authorization. Hold only dependent work; native denial and organization prohibition remain binding. |
| Implement | Re-read affected current content, preserve human/unrelated changes and apply only the authorized delta using established safe patterns. Add/adapt necessary behavior or regression tests with the project's existing tools; use focused inspection for a typo when sufficient. Do not add speculative abstractions, modify policy to remove restrictions or widen resources silently. |
| Verify | Select checks tied to changed behavior and risk, inspect scripts/transitive effects and actual targets, then run only authorized applicable checks. Record exact method, scope and observed result; distinguish unrun/inapplicable/blocked checks. No automatic install, migration or production access. |
| Review | Self-review the resulting diff against requested behavior, existing architecture, applicable quality/security concerns and governance/approval scope. Check unrelated edits and evidence gaps. This is not an independent audit or a claim all tests passed. |
| Memory impact/sync | Apply the shared lifecycle; report NONE, UPDATE_REQUIRED, CONFLICT or NOT_ASSESSED with scope. Sync only a necessary evidenced delta under actual memory-write authority, immediately rereading to preserve concurrent edits. Otherwise report pending drift; no delta means no touch. |
| Complete | Match actual output/check evidence to the agreed scope, report changes, limits, remaining decisions and Memory Impact. Do not call unperformed required work complete or imply commit/PR/deploy/publish is part of closure. |

The later risk stage never postpones an obvious approval or sensitive-data check
until after an unsafe read. Preflight bounds orientation and inspection too.
Mutation and execution are separate operations: permitted code edits may coexist
with a held test command or deployment. Reuse only authorization that actually
covers the check's effects; do not ask again merely because the stage changed.

Reuse [Core authority](../framework/trust-and-authority.md),
[Memory lifecycle](memory-lifecycle.md), [Governance Review](../governance/ai-usage.md)
and the relevant [application security checklist](../agent-security/application-security.md).
Select the relevant [engineering checks and stack profile](../framework/engineering/index.md)
from inspected task/component evidence; do not load all standards/profiles.
Do not duplicate their detailed policies or load irrelevant references.
Existing insecure patterns should be flagged with a scoped safer proposal.

Use the [Evidence Contract](../framework/evidence-contract.md) to record checks
against the final affected state and the Implement row of
[Definition of Done](../framework/definition-of-done.md) before closing.
Choose the smallest [report template](../framework/reporting-contract.md#template-selection);
required checks or mandatory Memory sync cannot be waived to claim DONE.

When a check fails, use [repair and handoff](repair-and-handoff.md). A failed
verification does not authorize unrelated repairs, blanket cleanup, policy changes
or an endless retry loop. If mandatory evidence is unavailable, report partial or
blocked completion for the affected scope.

## KIYO-IMPL-001 — Bind daily engineering to intent, baseline and checked scope

The canonical Implement skill covers features, bug fixes and explicitly scoped
refactors. An analysis/review request never enters the mutation stages because
the skill was selected or a bug was found. An explicit change request can already
authorize its ordinary bounded edits; approval reuse follows actual policy.

Capture permitted root/worktree/Git and staged/unstaged/untracked human changes
before editing. In a non-Git or partially accessible repository, state what was
actually observed; never initialize Git, reset, stash, revert or clean existing
work to manufacture a baseline. Reread affected content and reconcile human edits.
Early Memory orientation is context only: validate each material fact against
current evidence before using it to decide behavior; continue targeted pattern/
test inspection as scope becomes clear.

Assess dependency, schema/API, security/data and tool effects separately from
file edits. Preparing a migration is not applying one; auth/schema work needs the
actual action/environment/policy and valid approval, not a keyword-based blanket
allow or block. Never use a production DB or widen access to make checks pass.
Inspect setup/helpers/targets before permitted execution and recheck affected
behavior after later edits; preserve baseline failures and Unknown attribution.

After a failure use the existing repair procedure, retaining its default maximum
of two unsuccessful cycles and actual attempt history. A scope-changing repair
needs reassessment and any missing approval before the dependent edit/check.
Do not disable tests, weaken requirements or silently expand architecture/libraries
to obtain PASS. Report unperformed required verification as partial/blocked under DoD.

The [engineering report](../templates/reports/engineering-report.md) integrates
the final diff/criterion/evidence links, self-review, approvals/risk, residual issues
and Memory Impact; Tiny may use the [compact report](../templates/reports/compact-task-report.md).
Incomplete work uses [handoff](../templates/reports/handoff.md) with current facts,
next action and actual approval/repair scope. Chat remains default for all three.
These templates create no PR/commit, deployment, automatic log or project-memory
write. Mandatory sync requires actual authority and a necessary delta; preserve
approved decisions and leave no-delta records/timestamps untouched.
