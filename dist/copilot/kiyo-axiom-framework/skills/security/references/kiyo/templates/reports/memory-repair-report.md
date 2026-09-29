# Memory repair report template

Use for requested [repair](../../framework/memory-modes.md#apply-sync-or-repair-safely)
or explicit preview. Default output is chat. Repair changes only evidenced
authorized structural defects, not approved intent or the entire store.

- **Task/scope:** <canonical locator/store, defect types, permitted files/IDs, repository/worktree/module and preview/write effects>
- **Actions/files changed:** <actual minimal pointer/structure patches or no-op; no record/history deletion implied>
- **Governance/risk rationale:** <actual authority/data scope, valid approval reuse or missing necessary decision>
- **Verification/evidence:** <defect evidence, latest reread, identity checks, actual resulting links/IDs/diff and nine-field records>
- **Residual issues:** <unresolved target/duplicate identity, conflicting meaning, partial failures and unchecked parts>
- **Memory impact:** <scoped NONE / UPDATE_REQUIRED / CONFLICT / NOT_ASSESSED; applied versus pending effects explicit>
- **Status:** <DONE / PARTIALLY COMPLETE / BLOCKED / DECISION REQUIRED for the actual requested repair/preview>
- **Next required action:** <bounded missing decision/evidence, safe recovery or none; no reinitialization/migration by default>

| Defect / ID / path | Exact evidence and identity basis | Proposed / actual patch | Preserved content / latest reread | Validation / remaining gap |
| --- | --- | --- | --- | --- |
| <broken link, exact duplicate pointer, duplicate ID conflict or format defect> | <actual current target/anchor/claim/history, inspected scope and uncertainty> | <only authorized change, applied/held/no-op; no guessed replacement> | <record IDs, approved history, human annotations, dates; current reread outcome> | <actual local resolution/diff/check status, unverified facts and any partial failure> |

A link that resolves is not a freshly verified factual claim. Preserve last_verified
unless its specific claim was actually rechecked and persistence is authorized.
Missing evidence means UNVERIFIED; conflicting duplicate records need human
resolution, not deletion by recency. Use [Memory diff](memory-diff.md),
[drift report](memory-architecture-drift-report.md) and
[Evidence Contract](../../framework/evidence-contract.md) only as relevant.
