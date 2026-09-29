# Architecture impact report template

Use with [impact assessment](../../workflows/architecture.md#assess-proposed-change-impact).
This is a neutral chat section under the
[observation report](architecture-observation.md); include its shared eight report
fields and five categories once, not a second duplicated report. A proposed change
does not become authorized implementation merely because its impact was analyzed.

- **Proposed change / accepted scope:** <actual request, intended behavior and exclusions; distinguish any already observed diff>
- **Applicable intent:** <decision IDs, approval source/scope when established, known constraints and unresolved conflict>
- **Inspected boundary:** <repository/worktree/snapshot, affected modules/consumers, actual read/search method and inaccessible scope>
- **Impact findings:** <table below; exact safe evidence and inspected scope for every row>
- **Options / tradeoffs:** <smallest safe existing-pattern option and relevant alternatives; assumptions and proposals clearly labeled>
- **Verification proposal:** <relevant unit/integration/API/E2E/regression or contract checks to run later under valid scope; currently NOT_RUN unless real results exist>
- **Required decisions:** <concrete human questions that block dependent action; no approval invented or repeated if valid matching scope already exists>

| Boundary / dimension | Exact evidence and inspected scope | Observed relationship / conditional effect | Potential impact and confidence basis | Gaps / proposed next action |
| --- | --- | --- | --- | --- |
| <actual modules/callers/data/contract/security/operations/tests> | <safe file:line/symbol/config/consumer and snapshot actually inspected> | <current fact separately from hypothetical changed behavior> | <supported consequence, HIGH/MEDIUM/LOW with evidence and premises> | <unknown consumers/deployment, proposed mitigation/check or required decision> |

Address only relevant dimensions from the
[Architecture checklist](../../workflows/architecture.md#inspect-relevant-dimensions).
Record reasoned exclusions; uninspected is not non-applicable.
No dependency/folder-based architecture inference, guessed production topology,
automatic refactor/migration, unsupported score or claim that proposed tests passed.

Memory Impact is reported without edits; use the
[drift report](memory-architecture-drift-report.md) for a decision conflict.
A requested report-file output requires separate actual path/write scope.

