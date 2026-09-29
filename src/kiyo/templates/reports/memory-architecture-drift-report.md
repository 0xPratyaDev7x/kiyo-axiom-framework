# Memory / architecture drift report template

Use the [reporting contract](../../framework/reporting-contract.md) and
[Memory lifecycle](../../workflows/memory-lifecycle.md). Default output is chat;
a drift finding grants no write or architecture-migration permission.

- **Task/scope:** <checked entry IDs/component, mode, exclusions and actual repository/worktree scope>
- **Actions/files changed:** <inspection versus actual authorized edits; preserve human attribution>
- **Governance/risk rationale:** <read/write limits, authority, risk/uncertainty and relevant decision conflict>
- **Verification/evidence:** <nine-field check records with actual inspected scope, current result and baseline relation>
- **Residual issues:** <unverified claims, missing sources, conflicts and unchecked entries>
- **Memory impact:** <NONE / UPDATE_REQUIRED / CONFLICT / NOT_ASSESSED; reason and applied/pending delta>
- **Status:** <bounded check/sync task status; no whole-project certification>
- **Next required action:** <scoped correction proposal or needed decision/precondition>

| Entry / decision ID | Recorded claim and type | Current scoped evidence | Finding / proposed action |
| --- | --- | --- | --- |
| <existing ID> | <observation/proposal/decision; real approval source only if known> | <actual path/symbol/result or unavailable> | <matching/stale/unverified/Architecture Drift; proposed correction separate> |

**Dates/state:** <entry's actual last_modified and last_verified if inspected;
new verification scope/date only when actually performed; no whole-file refresh>.
**Authority:** <approved intent source/scope versus implementation evidence;
unconfirmed approval remains Unknown>.
**Write outcome:** <none in check mode; for authorized sync actual changed entries,
preserved concurrent edits and remaining mandatory delta>.

A Mapperly approved decision conflicting with observed AutoMapper usage is
Architecture Drift; do not rewrite the decision from code. Separate the current
assessment from persisted status. A read-only check can finish with a conflict
finding while any requested implementation/sync remains pending.
