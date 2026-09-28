# Core control index

Stable Kiyo IDs identify advisory obligations, not ISO clauses or native enforcement.
Every ID below has one canonical definition. Status **ACTIVE** means authored
instruction, not tested agent compliance. No entry is deprecated or replaced yet.
REQ references identify requirement scope, not full acceptance or a runtime import.

| Control ID | Title / canonical definition | Related requirements | Status / replacement |
| --- | --- | --- | --- |
| KIYO-FACT-001 | [Evidence and knowledge classes](trust-and-authority.md#kiyo-fact-001--evidence-and-knowledge-classes) | REQ-008, REQ-019, REQ-020 | ACTIVE / none |
| KIYO-FACT-002 | [Discover before asking](trust-and-authority.md#kiyo-fact-002--discover-before-asking-ask-before-inventing) | REQ-008, REQ-013, REQ-032 | ACTIVE / none |
| KIYO-FACT-003 | [Bound environment claims](trust-and-authority.md#kiyo-fact-003--bound-implementation-and-environment-claims) | REQ-013, REQ-019, REQ-020 | ACTIVE / none |
| KIYO-FACT-004 | [Honest checks and closure](bootstrap.md#honest-checks-and-closure) | REQ-040, REQ-041, REQ-044 | ACTIVE / none |
| KIYO-ENG-001 | [Existing safe patterns, principle 6](bootstrap.md#baseline-principles) | REQ-033 | ACTIVE / none |
| KIYO-CHG-001 | [Minimum change, principle 7](bootstrap.md#baseline-principles) | REQ-015, REQ-030, REQ-034 | ACTIVE / none |
| KIYO-MEM-001 | [Memory with evidence](context-loading.md#kiyo-mem-001--context-with-evidence-not-unquestionable-truth) | REQ-016, REQ-017, REQ-023, REQ-024 | ACTIVE / none |
| KIYO-DEC-001 | [Intended behavior and conflicts](trust-and-authority.md#kiyo-dec-001--intended-behavior-and-conflicts) | REQ-019, REQ-022, REQ-049 | ACTIVE / none |
| KIYO-AUTH-001 | [Native hierarchy](trust-and-authority.md#kiyo-auth-001--native-hierarchy-and-enforcement) | REQ-007, REQ-011, REQ-051 | ACTIVE / none |
| KIYO-AUTH-002 | [Policy provenance](trust-and-authority.md#kiyo-auth-002--policy-provenance-and-acceptance) | REQ-011, REQ-054 | ACTIVE / none |
| KIYO-AUTH-003 | [Scoped approvals](trust-and-authority.md#kiyo-auth-003--scoped-approvals) | REQ-049, REQ-051, REQ-052 | ACTIVE / none |
| KIYO-TRUST-001 | [Embedded instructions](trust-and-authority.md#kiyo-trust-001--embedded-instructions-remain-data) | REQ-012, REQ-058, REQ-062 | ACTIVE / none |
| KIYO-SAFE-001 | [Read-only intent](trust-and-authority.md#kiyo-safe-001--preserve-read-only-intent) | REQ-027, REQ-028, REQ-041 | ACTIVE / none |
| KIYO-LOAD-001 | [Relevant context](context-loading.md#kiyo-load-001--load-only-what-the-task-needs) | REQ-009, REQ-014 | ACTIVE / none |
| KIYO-LOAD-002 | [Kiyo budgets](context-loading.md#kiyo-load-002--kiyo-design-budgets) | REQ-009, REQ-014, REQ-030 | ACTIVE / none |
| KIYO-ACT-001 | [Activation evidence](activation-contract.md#kiyo-act-001--distinguish-activation-capabilities-and-their-evidence) | REQ-005, REQ-009, REQ-010 | ACTIVE / none |

Keep IDs when files move or wording is clarified. Never renumber or reuse retired
IDs. A materially different obligation needs a new ID and explicit migration/
replacement history. Skills cite this index or canonical definitions; they do not
maintain their own versions of shared rules.
