# Memory diff template

Use before a scoped [sync/repair](../../framework/memory-modes.md), or to describe
check findings. Neutral chat proposal, not a populated store, approval or applied
patch. In show mode no diff is required; no-delta work can use one concise sentence.

- **Mode / canonical scope:** <actual request, resolved store/locator, repository/worktree/module, selected IDs and permitted effects>
- **Baseline / freshness:** <entry/index/evidence actually read, observed revision/dirty scope if available, stored versus current assessment dates>
- **Proposed deltas:** <table below; no whole-folder rewrite>
- **Decision conflicts / held changes:** <approved intent with source/scope versus implementation; unknowns and required human choice>
- **Authorization:** <actual requested/approved path/entry effects and still-valid policy scope; missing approval only where required>
- **Latest reread / merge plan:** <current entry/index/human text/evidence to recheck immediately before writing; no promise of a lock>
- **Validation / no-op condition:** <affected links/IDs/provenance/preserved sections to check; if no necessary delta, no writes or date refresh>

| ID / type / path | Before → proposed after meaning | Evidence / inspected scope / uncertainty | Date and provenance handling | Required pointer edit / permitted effect |
| --- | --- | --- | --- | --- |
| <actual record ID and observation/proposal/decision> | <minimal supported correction or structural change; not an adopted decision> | <safe file:line/symbol, actual observation method/date and gaps> | <keep observed_date/history; actual last_modified/last_verified changes only when justified; Git actually observed or Unknown> | <actual affected index/reference, or none; hold if outside authority> |

Mark each delta proposed, applied, held or no-op according to actual work.
In check mode all corrections stay proposed. UNVERIFIED is honest evidence
absence, not permission to invent or delete a decision.
Preserve [entry fields](../../framework/memory-specification.md#kiyo-mem-003--entry-identity-evidence-and-dates)
and [approved intent](../../framework/trust-and-authority.md#kiyo-dec-001--intended-behavior-and-conflicts).
Do not persist secrets, PII, raw logs/private reasoning or redundant code inventories.
