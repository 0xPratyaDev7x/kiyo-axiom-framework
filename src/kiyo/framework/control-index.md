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
| KIYO-MEM-002 | [Canonical store and scope](memory-specification.md#kiyo-mem-002--one-canonical-store-and-explicit-scope) | REQ-017, REQ-024 | ACTIVE / none |
| KIYO-MEM-003 | [Entry evidence and dates](memory-specification.md#kiyo-mem-003--entry-identity-evidence-and-dates) | REQ-019, REQ-020, REQ-024 | ACTIVE / none |
| KIYO-MEM-004 | [Observation and decision drift](memory-specification.md#kiyo-mem-004--reconcile-observations-without-rewriting-intent) | REQ-016, REQ-021, REQ-022 | ACTIVE / none |
| KIYO-MEM-005 | [Authorized minimal writes](memory-specification.md#kiyo-mem-005--authorized-minimal-concurrency-aware-writes) | REQ-023, REQ-024, REQ-027, REQ-075 | ACTIVE / none |
| KIYO-MEM-006 | [Memory Impact](memory-specification.md#kiyo-mem-006--memory-impact-at-closure) | REQ-023, REQ-044 | ACTIVE / none |
| KIYO-MEM-007 | [Durable minimized content](memory-specification.md#kiyo-mem-007--durable-minimized-content) | REQ-018, REQ-046, REQ-062 | ACTIVE / none |
| KIYO-DEC-001 | [Intended behavior and conflicts](trust-and-authority.md#kiyo-dec-001--intended-behavior-and-conflicts) | REQ-019, REQ-022, REQ-049 | ACTIVE / none |
| KIYO-AUTH-001 | [Native hierarchy](trust-and-authority.md#kiyo-auth-001--native-hierarchy-and-enforcement) | REQ-007, REQ-011, REQ-051 | ACTIVE / none |
| KIYO-AUTH-002 | [Policy provenance](trust-and-authority.md#kiyo-auth-002--policy-provenance-and-acceptance) | REQ-011, REQ-054 | ACTIVE / none |
| KIYO-AUTH-003 | [Scoped approvals](trust-and-authority.md#kiyo-auth-003--scoped-approvals) | REQ-049, REQ-051, REQ-052 | ACTIVE / none |
| KIYO-TRUST-001 | [Embedded instructions](trust-and-authority.md#kiyo-trust-001--embedded-instructions-remain-data) | REQ-012, REQ-058, REQ-062 | ACTIVE / none |
| KIYO-SAFE-001 | [Read-only intent](trust-and-authority.md#kiyo-safe-001--preserve-read-only-intent) | REQ-027, REQ-028, REQ-041 | ACTIVE / none |
| KIYO-LOAD-001 | [Relevant context](context-loading.md#kiyo-load-001--load-only-what-the-task-needs) | REQ-009, REQ-014 | ACTIVE / none |
| KIYO-LOAD-002 | [Kiyo budgets](context-loading.md#kiyo-load-002--kiyo-design-budgets) | REQ-009, REQ-014, REQ-030 | ACTIVE / none |
| KIYO-ACT-001 | [Activation evidence](activation-contract.md#kiyo-act-001--distinguish-activation-capabilities-and-their-evidence) | REQ-005, REQ-009, REQ-010 | ACTIVE / none |
| KIYO-GOV-001 | [Advisory AI governance](../governance/ai-usage.md#kiyo-gov-001--apply-advisory-governance-within-actual-authority) | REQ-007, REQ-011, REQ-046, REQ-054 | ACTIVE / none |
| KIYO-GOV-002 | [Kiyo governance modes](../governance/governance-levels.md#kiyo-gov-002--keep-kiyo-modes-separate-from-risk-and-permissions) | REQ-027, REQ-047 | ACTIVE / none |
| KIYO-RISK-001 | [Contextual risk assessment](../governance/risk-assessment.md#kiyo-risk-001--assess-the-concrete-action-and-uncertainty) | REQ-035, REQ-048 | ACTIVE / none |
| KIYO-AUTH-004 | [Concrete approval scope and reuse](../governance/human-approval.md#kiyo-auth-004--make-approval-concrete-and-reuse-valid-scope) | REQ-049, REQ-052 | ACTIVE / none |
| KIYO-DATA-001 | [Content-based data handling](../governance/data-handling.md#kiyo-data-001--classify-content-and-minimize-exposure) | REQ-046, REQ-050, REQ-055 | ACTIVE / none |
| KIYO-PERM-001 | [Necessary authorized capabilities](../governance/permissions.md#kiyo-perm-001--use-only-necessary-authorized-capabilities) | REQ-007, REQ-041, REQ-051 | ACTIVE / none |
| KIYO-ACTION-001 | [Preparation versus effects](../governance/dangerous-actions.md#kiyo-action-001--separate-preparation-from-actual-effects) | REQ-041, REQ-048, REQ-052 | ACTIVE / none |
| KIYO-DEP-001 | [Dependency justification](../governance/dependency-governance.md#kiyo-dep-001--justify-and-inspect-dependencies-in-context) | REQ-003, REQ-053, REQ-059 | ACTIVE / none |
| KIYO-PROVIDER-001 | [Provider evidence and limits](../governance/provider-policy.md#kiyo-provider-001--use-observed-context-and-bound-data-assurances) | REQ-013, REQ-055 | ACTIVE / none |
| KIYO-SEC-001 | [Establish trust from evidence](../agent-security/trust-review.md#kiyo-sec-001--establish-trust-from-evidence) | REQ-058 | ACTIVE / none |
| KIYO-SEC-002 | [Compare honest metadata with the actual payload](../agent-security/trust-review.md#kiyo-sec-002--compare-honest-metadata-with-the-actual-payload) | REQ-061, REQ-067 | ACTIVE / none |
| KIYO-SEC-003 | [Preserve the authority boundary across retrieved content](../agent-security/prompt-injection.md#kiyo-sec-003--preserve-the-authority-boundary-across-retrieved-content) | REQ-012, REQ-062 | ACTIVE / none |
| KIYO-SEC-004 | [Bind source review to the actual artifact](../agent-security/update-and-provenance.md#kiyo-sec-004--bind-source-review-to-the-actual-artifact) | REQ-053, REQ-059 | ACTIVE / none |
| KIYO-SEC-005 | [Reassess changed content and scope before reuse](../agent-security/update-and-provenance.md#kiyo-sec-005--reassess-changed-content-and-scope-before-reuse) | REQ-049, REQ-064 | ACTIVE / none |
| KIYO-SEC-006 | [Establish required host controls or hold dependent execution](../agent-security/control-ownership.md#kiyo-sec-006--establish-required-host-controls-or-hold-dependent-execution) | REQ-007, REQ-051, REQ-063 | ACTIVE / none |
| KIYO-SEC-007 | [Keep review layers and blind spots explicit](../agent-security/trust-review.md#kiyo-sec-007--keep-review-layers-and-blind-spots-explicit) | REQ-040, REQ-065, REQ-077 | ACTIVE / none |
| KIYO-SEC-008 | [Keep accountable optional file records](../agent-security/control-ownership.md#kiyo-sec-008--keep-accountable-optional-file-records) | REQ-049, REQ-066 | ACTIVE / none |
| KIYO-SEC-009 | [Verify each platform control independently](../agent-security/control-ownership.md#kiyo-sec-009--verify-each-platform-control-independently) | REQ-005, REQ-067 | ACTIVE / none |
| KIYO-SEC-010 | [Review application behavior separately from agent skills](../agent-security/application-security.md#kiyo-sec-010--review-application-behavior-separately-from-agent-skills) | REQ-057, REQ-073 | ACTIVE / none |
| KIYO-ROUTE-001 | [Select a workflow without granting authority](../workflows/workflow-router.md#kiyo-route-001--select-a-workflow-without-granting-authority) | REQ-025, REQ-026, REQ-027, REQ-028 | ACTIVE / none |
| KIYO-FLOW-001 | [Reduce ceremony without skipping controls](../workflows/adaptive-flow.md#kiyo-flow-001--reduce-ceremony-without-skipping-controls) | REQ-029, REQ-030, REQ-035 | ACTIVE / none |
| KIYO-FLOW-002 | [Sequence authorized changes through actual evidence](../workflows/implement-flow.md#kiyo-flow-002--sequence-authorized-changes-through-actual-evidence) | REQ-027, REQ-033, REQ-034, REQ-035, REQ-041, REQ-042 | ACTIVE / none |
| KIYO-FLOW-003 | [Complete analysis without introducing mutation](../workflows/read-only-flow.md#kiyo-flow-003--complete-analysis-without-introducing-mutation) | REQ-027, REQ-028, REQ-044 | ACTIVE / none |
| KIYO-FLOW-004 | [Classify failures and bound repair cycles](../workflows/repair-and-handoff.md#kiyo-flow-004--classify-failures-and-bound-repair-cycles) | REQ-029, REQ-039, REQ-040 | ACTIVE / none |
| KIYO-FLOW-005 | [Handoff facts and authorized next actions](../workflows/repair-and-handoff.md#kiyo-flow-005--handoff-facts-and-authorized-next-actions) | REQ-014, REQ-044, REQ-045 | ACTIVE / none |
| KIYO-ENG-002 | [Make behavior and acceptance traceable](engineering/requirements.md#kiyo-eng-002--make-behavior-and-acceptance-traceable) | REQ-031, REQ-032 | ACTIVE / none |
| KIYO-ENG-003 | [Preserve safe boundaries and explicit design intent](engineering/architecture.md#kiyo-eng-003--preserve-safe-boundaries-and-explicit-design-intent) | REQ-033, REQ-035 | ACTIVE / none |
| KIYO-ENG-004 | [Keep changed code clear, bounded and safe](engineering/coding.md#kiyo-eng-004--keep-changed-code-clear-bounded-and-safe) | REQ-033, REQ-036, REQ-053 | ACTIVE / none |
| KIYO-ENG-005 | [Match checks to behavior, risk and observed results](engineering/testing.md#kiyo-eng-005--match-checks-to-behavior-risk-and-observed-results) | REQ-038, REQ-040, REQ-041 | ACTIVE / none |
| KIYO-ENG-006 | [Evaluate affected quality with proportionate evidence](engineering/quality.md#kiyo-eng-006--evaluate-affected-quality-with-proportionate-evidence) | REQ-036, REQ-056 | ACTIVE / none |
| KIYO-ENG-007 | [Preserve human work and keep the diff necessary](engineering/change-scope.md#kiyo-eng-007--preserve-human-work-and-keep-the-diff-necessary) | REQ-030, REQ-034 | ACTIVE / none |
| KIYO-PROF-001 | [Bind profiles to evidence without forcing a stack](../profiles/extension-contract.md#kiyo-prof-001--bind-profiles-to-evidence-without-forcing-a-stack) | REQ-037, REQ-054 | ACTIVE / none |
| KIYO-VERIFY-001 | [Record scoped observations for every check](evidence-contract.md#kiyo-verify-001--record-scoped-observations-for-every-check) | REQ-040, REQ-041, REQ-043, REQ-077 | ACTIVE / none |
| KIYO-VERIFY-002 | [Bind results to the checked state and baseline](evidence-contract.md#kiyo-verify-002--bind-results-to-the-checked-state-and-baseline) | REQ-039, REQ-040, REQ-044 | ACTIVE / none |
| KIYO-DONE-001 | [Close the agreed workflow against current required evidence](definition-of-done.md#kiyo-done-001--close-the-agreed-workflow-against-current-required-evidence) | REQ-023, REQ-042, REQ-044, REQ-045 | ACTIVE / none |
| KIYO-REPORT-001 | [Report scoped work without manufacturing an audit trail](reporting-contract.md#kiyo-report-001--report-scoped-work-without-manufacturing-an-audit-trail) | REQ-043, REQ-045, REQ-046, REQ-049 | ACTIVE / none |
| KIYO-INIT-001 | [Initialize only evidenced and authorized project state](../workflows/init.md#kiyo-init-001--initialize-only-evidenced-and-authorized-project-state) | REQ-015, REQ-016, REQ-017, REQ-024, REQ-027, REQ-068 | ACTIVE / none |

Keep IDs when files move or wording is clarified. Never renumber or reuse retired
IDs. A materially different obligation needs a new ID and explicit migration/
replacement history. Skills cite this index or canonical definitions; they do not
maintain their own versions of shared rules.
