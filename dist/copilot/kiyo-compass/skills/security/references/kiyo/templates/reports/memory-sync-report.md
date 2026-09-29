# Memory sync report template

Use for requested [sync](../../framework/memory-modes.md) or its explicit preview.
Default output is chat; a report-file path needs separate actual write scope.
This is neutral report guidance, not a second Memory store.

- **Task/scope:** <mode/preview, canonical path, selected IDs, repository/worktree/module, exclusions and actual write authority>
- **Actions/files changed:** <actual entry/index deltas or explicit zero writes/no-op; use the diff table below>
- **Governance/risk rationale:** <permitted data/effects, policy-defined approval or valid reuse, held conflicts>
- **Verification/evidence:** <latest reread outcome, actual source/provenance and nine-field checks; methods not run stay explicit>
- **Residual issues:** <pending corrections, approved-decision conflicts, unavailable evidence, unchecked entries and concurrent-change limits>
- **Memory impact:** <NONE / UPDATE_REQUIRED / CONFLICT / NOT_ASSESSED, scoped reason; after necessary update say applied/no pending delta instead of hiding it as NONE>
- **Status:** <DONE / PARTIALLY COMPLETE / BLOCKED / DECISION REQUIRED for requested deliverable; preview is not applied sync>
- **Next required action:** <specific missing evidence/decision or none for completed scoped work; no automatic Init or source fix>

| Entry / path | Proposed versus actual delta | Evidence and provenance | Latest reread / human preservation | Result and scoped checks |
| --- | --- | --- | --- | --- |
| <actual ID/file> | <minimal before/after, applied/held/no-op; decision history preserved> | <safe source/symbol, actual observation/verification dates, scope/uncertainty and observed Git context> | <what current entry/index/evidence was reread; non-overlap retained or conflict held> | <actual diff/links/IDs checks, PASS/FAIL/NOT_RUN/NOT_APPLICABLE/BLOCKED with limits> |

Use [Memory diff](memory-diff.md) for proposed changes and the
[Evidence Contract](../../framework/evidence-contract.md) for all nine check fields.
Never claim reverified whole Memory, production state or a watcher.
No-delta means no write/timestamp refresh; do not persist this report just to log it.
