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

## Architecture decision comparison

For an Architecture task, use the [shared procedure](../../workflows/architecture.md#compare-approved-intent-and-detect-drift)
and keep the [five output categories](architecture-observation.md) distinct.
This section extends the shared report above, not a second mutable decision store.

- **Decision ID:** <actual existing ID and statement, approval source/scope/
  applicability if established; Unknown rather than an invented approved ADR>
- **Files/symbols/config:** <exact safe locations actually inspected, snapshot/
  component scope and relevant registration/callers/tests; unread areas separate>
- **Observed difference:** <comparison outcome Match / Deviation / Insufficient
  evidence; actual implementation versus intended criterion, not deployment claims>
- **Potential impact:** <supported consequences and conditional risks, affected
  boundary/consumers and unknown reachability>
- **Confidence:** <HIGH/MEDIUM/LOW, concrete evidence basis and remaining premises
  using the shared guide; confidence in source comparison is not runtime proof>
- **Possible interpretations:** <evidence-compatible explanations, such as
  unauthorized drift, an unrecorded approved exception, unused dependency or
  incomplete inspection; none becomes a fact without evidence>
- **Required human decision:** <specific unresolved choice and authorized scope
  needed, or none for a scoped Match; existing matching authority is not discarded>

For a usage-only Mapperly decision, an AutoMapper package reference alone means
possible drift / Insufficient evidence, unless actual usage is established.
An explicit dependency prohibition can be contradicted by the reference itself.
No ADR in inspected scope means observed pattern without established mandate.
Do not infer a new decision, rewrite decisions.md, or treat an unverified
explanation as approval. Known decision conflict is Memory CONFLICT.
Use the [confidence guide](../../framework/review-severity-confidence.md).
Comparison outcomes do not replace the five check or four task statuses.
