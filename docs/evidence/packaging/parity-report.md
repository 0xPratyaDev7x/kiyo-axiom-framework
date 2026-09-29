# Content and control parity

Checked 2026-09-29 for Prompt 23. **Content parity PASS; packaged behavioral
parity NOT_RUN; all six native live targets NOT_TESTED.** Codex IDE native plugins
remain UNSUPPORTED; the Codex candidate artifact is not an IDE distribution.

The [generated inventory](artifact-inventory.json) contains **456 explicit records**:
68 controls plus eight logical skills, separately mapped to each of six target IDs.
Each record has canonical rule, actual adapter paths/output hashes, activation
requirement, scoped static evidence, behavioral evidence, host dependency and gap.
The table below is a compact view of those records, not a collapse of host results.

All controls remain advisory. Writing deny in Markdown does not create native
enforcement, sandboxing, network filtering or signatures. Equal content cannot
prove agents followed it. Earlier bounded source trials are not substituted for
packaged behavior or native testing.

## Reading the mappings

C = Claude artifact (CLI and VS Code recorded independently); X = Codex candidate
(CLI, with a separate unsupported IDE record); P = Copilot artifact (CLI and
VS Code recorded independently). For control rows, R means the canonical path
beneath src/kiyo, copied to skills/<selected>/references/kiyo/R in **all eight
skills** of C/X/P. For skill rows, S means skills/<name>/SKILL.md, with only the
declared [entry transform](../../architecture/distribution-build.md#allowed-transformations).
Exact expanded paths and SHA-256 values are in the inventory, not inferred from
these abbreviations.

E/P refer to the [six independent activation records](../../compatibility/activation-matrix.md).
A selected skill must direct Core/reference reads; persistent project guidance is
separately authorized and host-dependent. The installed payload contains all
references; it need not load them all into context. No metadata/permission fork
of a canonical control exists.

Static evidence K = PKG-02 for the respective artifact: entire shared files match
canonical bytes and complete entry bodies match after reversing approved transforms;
source hashes and extracted inventories agree. This is candidate file evidence
only, including for the unsupported Codex IDE row. Behavioral evidence N means
NOT_RUN on each of the six targets. Dependency H means the actual host's discovery,
file reads, instruction hierarchy, context limits and permissions plus human policy
authority. Gap G = untested packaged behavior/lifecycle, unsupported Codex IDE,
Codex owner-field ingestion FAIL, and unresolved CLI qualification as specified
per target. These shared abbreviations do not grant or establish enforcement.

| Control/Skill | Canonical rule | Adapter representation | Activation requirement | Static evidence | Behavioral evidence | Host dependency | Gap |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KIYO-FACT-001 | [framework/trust-and-authority.md#kiyo-fact-001--evidence-and-knowledge-classes](../../../src/kiyo/framework/trust-and-authority.md#kiyo-fact-001--evidence-and-knowledge-classes) | C/X/P: R = framework/trust-and-authority.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-FACT-002 | [framework/trust-and-authority.md#kiyo-fact-002--discover-before-asking-ask-before-inventing](../../../src/kiyo/framework/trust-and-authority.md#kiyo-fact-002--discover-before-asking-ask-before-inventing) | C/X/P: R = framework/trust-and-authority.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-FACT-003 | [framework/trust-and-authority.md#kiyo-fact-003--bound-implementation-and-environment-claims](../../../src/kiyo/framework/trust-and-authority.md#kiyo-fact-003--bound-implementation-and-environment-claims) | C/X/P: R = framework/trust-and-authority.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-FACT-004 | [framework/bootstrap.md#honest-checks-and-closure](../../../src/kiyo/framework/bootstrap.md#honest-checks-and-closure) | C/X/P: R = framework/bootstrap.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ENG-001 | [framework/bootstrap.md#baseline-principles](../../../src/kiyo/framework/bootstrap.md#baseline-principles) | C/X/P: R = framework/bootstrap.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-CHG-001 | [framework/bootstrap.md#baseline-principles](../../../src/kiyo/framework/bootstrap.md#baseline-principles) | C/X/P: R = framework/bootstrap.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-MEM-001 | [framework/context-loading.md#kiyo-mem-001--context-with-evidence-not-unquestionable-truth](../../../src/kiyo/framework/context-loading.md#kiyo-mem-001--context-with-evidence-not-unquestionable-truth) | C/X/P: R = framework/context-loading.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-MEM-002 | [framework/memory-specification.md#kiyo-mem-002--one-canonical-store-and-explicit-scope](../../../src/kiyo/framework/memory-specification.md#kiyo-mem-002--one-canonical-store-and-explicit-scope) | C/X/P: R = framework/memory-specification.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-MEM-003 | [framework/memory-specification.md#kiyo-mem-003--entry-identity-evidence-and-dates](../../../src/kiyo/framework/memory-specification.md#kiyo-mem-003--entry-identity-evidence-and-dates) | C/X/P: R = framework/memory-specification.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-MEM-004 | [framework/memory-specification.md#kiyo-mem-004--reconcile-observations-without-rewriting-intent](../../../src/kiyo/framework/memory-specification.md#kiyo-mem-004--reconcile-observations-without-rewriting-intent) | C/X/P: R = framework/memory-specification.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-MEM-005 | [framework/memory-specification.md#kiyo-mem-005--authorized-minimal-concurrency-aware-writes](../../../src/kiyo/framework/memory-specification.md#kiyo-mem-005--authorized-minimal-concurrency-aware-writes) | C/X/P: R = framework/memory-specification.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-MEM-006 | [framework/memory-specification.md#kiyo-mem-006--memory-impact-at-closure](../../../src/kiyo/framework/memory-specification.md#kiyo-mem-006--memory-impact-at-closure) | C/X/P: R = framework/memory-specification.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-MEM-007 | [framework/memory-specification.md#kiyo-mem-007--durable-minimized-content](../../../src/kiyo/framework/memory-specification.md#kiyo-mem-007--durable-minimized-content) | C/X/P: R = framework/memory-specification.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-DEC-001 | [framework/trust-and-authority.md#kiyo-dec-001--intended-behavior-and-conflicts](../../../src/kiyo/framework/trust-and-authority.md#kiyo-dec-001--intended-behavior-and-conflicts) | C/X/P: R = framework/trust-and-authority.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-AUTH-001 | [framework/trust-and-authority.md#kiyo-auth-001--native-hierarchy-and-enforcement](../../../src/kiyo/framework/trust-and-authority.md#kiyo-auth-001--native-hierarchy-and-enforcement) | C/X/P: R = framework/trust-and-authority.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-AUTH-002 | [framework/trust-and-authority.md#kiyo-auth-002--policy-provenance-and-acceptance](../../../src/kiyo/framework/trust-and-authority.md#kiyo-auth-002--policy-provenance-and-acceptance) | C/X/P: R = framework/trust-and-authority.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-AUTH-003 | [framework/trust-and-authority.md#kiyo-auth-003--scoped-approvals](../../../src/kiyo/framework/trust-and-authority.md#kiyo-auth-003--scoped-approvals) | C/X/P: R = framework/trust-and-authority.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-TRUST-001 | [framework/trust-and-authority.md#kiyo-trust-001--embedded-instructions-remain-data](../../../src/kiyo/framework/trust-and-authority.md#kiyo-trust-001--embedded-instructions-remain-data) | C/X/P: R = framework/trust-and-authority.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SAFE-001 | [framework/trust-and-authority.md#kiyo-safe-001--preserve-read-only-intent](../../../src/kiyo/framework/trust-and-authority.md#kiyo-safe-001--preserve-read-only-intent) | C/X/P: R = framework/trust-and-authority.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-LOAD-001 | [framework/context-loading.md#kiyo-load-001--load-only-what-the-task-needs](../../../src/kiyo/framework/context-loading.md#kiyo-load-001--load-only-what-the-task-needs) | C/X/P: R = framework/context-loading.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-LOAD-002 | [framework/context-loading.md#kiyo-load-002--kiyo-design-budgets](../../../src/kiyo/framework/context-loading.md#kiyo-load-002--kiyo-design-budgets) | C/X/P: R = framework/context-loading.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ACT-001 | [framework/activation-contract.md#kiyo-act-001--distinguish-activation-capabilities-and-their-evidence](../../../src/kiyo/framework/activation-contract.md#kiyo-act-001--distinguish-activation-capabilities-and-their-evidence) | C/X/P: R = framework/activation-contract.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-GOV-001 | [governance/ai-usage.md#kiyo-gov-001--apply-advisory-governance-within-actual-authority](../../../src/kiyo/governance/ai-usage.md#kiyo-gov-001--apply-advisory-governance-within-actual-authority) | C/X/P: R = governance/ai-usage.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-GOV-002 | [governance/governance-levels.md#kiyo-gov-002--keep-kiyo-modes-separate-from-risk-and-permissions](../../../src/kiyo/governance/governance-levels.md#kiyo-gov-002--keep-kiyo-modes-separate-from-risk-and-permissions) | C/X/P: R = governance/governance-levels.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-RISK-001 | [governance/risk-assessment.md#kiyo-risk-001--assess-the-concrete-action-and-uncertainty](../../../src/kiyo/governance/risk-assessment.md#kiyo-risk-001--assess-the-concrete-action-and-uncertainty) | C/X/P: R = governance/risk-assessment.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-AUTH-004 | [governance/human-approval.md#kiyo-auth-004--make-approval-concrete-and-reuse-valid-scope](../../../src/kiyo/governance/human-approval.md#kiyo-auth-004--make-approval-concrete-and-reuse-valid-scope) | C/X/P: R = governance/human-approval.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-DATA-001 | [governance/data-handling.md#kiyo-data-001--classify-content-and-minimize-exposure](../../../src/kiyo/governance/data-handling.md#kiyo-data-001--classify-content-and-minimize-exposure) | C/X/P: R = governance/data-handling.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-PERM-001 | [governance/permissions.md#kiyo-perm-001--use-only-necessary-authorized-capabilities](../../../src/kiyo/governance/permissions.md#kiyo-perm-001--use-only-necessary-authorized-capabilities) | C/X/P: R = governance/permissions.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ACTION-001 | [governance/dangerous-actions.md#kiyo-action-001--separate-preparation-from-actual-effects](../../../src/kiyo/governance/dangerous-actions.md#kiyo-action-001--separate-preparation-from-actual-effects) | C/X/P: R = governance/dangerous-actions.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-DEP-001 | [governance/dependency-governance.md#kiyo-dep-001--justify-and-inspect-dependencies-in-context](../../../src/kiyo/governance/dependency-governance.md#kiyo-dep-001--justify-and-inspect-dependencies-in-context) | C/X/P: R = governance/dependency-governance.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-PROVIDER-001 | [governance/provider-policy.md#kiyo-provider-001--use-observed-context-and-bound-data-assurances](../../../src/kiyo/governance/provider-policy.md#kiyo-provider-001--use-observed-context-and-bound-data-assurances) | C/X/P: R = governance/provider-policy.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-001 | [agent-security/trust-review.md#kiyo-sec-001--establish-trust-from-evidence](../../../src/kiyo/agent-security/trust-review.md#kiyo-sec-001--establish-trust-from-evidence) | C/X/P: R = agent-security/trust-review.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-002 | [agent-security/trust-review.md#kiyo-sec-002--compare-honest-metadata-with-the-actual-payload](../../../src/kiyo/agent-security/trust-review.md#kiyo-sec-002--compare-honest-metadata-with-the-actual-payload) | C/X/P: R = agent-security/trust-review.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-003 | [agent-security/prompt-injection.md#kiyo-sec-003--preserve-the-authority-boundary-across-retrieved-content](../../../src/kiyo/agent-security/prompt-injection.md#kiyo-sec-003--preserve-the-authority-boundary-across-retrieved-content) | C/X/P: R = agent-security/prompt-injection.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-004 | [agent-security/update-and-provenance.md#kiyo-sec-004--bind-source-review-to-the-actual-artifact](../../../src/kiyo/agent-security/update-and-provenance.md#kiyo-sec-004--bind-source-review-to-the-actual-artifact) | C/X/P: R = agent-security/update-and-provenance.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-005 | [agent-security/update-and-provenance.md#kiyo-sec-005--reassess-changed-content-and-scope-before-reuse](../../../src/kiyo/agent-security/update-and-provenance.md#kiyo-sec-005--reassess-changed-content-and-scope-before-reuse) | C/X/P: R = agent-security/update-and-provenance.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-006 | [agent-security/control-ownership.md#kiyo-sec-006--establish-required-host-controls-or-hold-dependent-execution](../../../src/kiyo/agent-security/control-ownership.md#kiyo-sec-006--establish-required-host-controls-or-hold-dependent-execution) | C/X/P: R = agent-security/control-ownership.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-007 | [agent-security/trust-review.md#kiyo-sec-007--keep-review-layers-and-blind-spots-explicit](../../../src/kiyo/agent-security/trust-review.md#kiyo-sec-007--keep-review-layers-and-blind-spots-explicit) | C/X/P: R = agent-security/trust-review.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-008 | [agent-security/control-ownership.md#kiyo-sec-008--keep-accountable-optional-file-records](../../../src/kiyo/agent-security/control-ownership.md#kiyo-sec-008--keep-accountable-optional-file-records) | C/X/P: R = agent-security/control-ownership.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-009 | [agent-security/control-ownership.md#kiyo-sec-009--verify-each-platform-control-independently](../../../src/kiyo/agent-security/control-ownership.md#kiyo-sec-009--verify-each-platform-control-independently) | C/X/P: R = agent-security/control-ownership.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-010 | [agent-security/application-security.md#kiyo-sec-010--review-application-behavior-separately-from-agent-skills](../../../src/kiyo/agent-security/application-security.md#kiyo-sec-010--review-application-behavior-separately-from-agent-skills) | C/X/P: R = agent-security/application-security.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ROUTE-001 | [workflows/workflow-router.md#kiyo-route-001--select-a-workflow-without-granting-authority](../../../src/kiyo/workflows/workflow-router.md#kiyo-route-001--select-a-workflow-without-granting-authority) | C/X/P: R = workflows/workflow-router.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-FLOW-001 | [workflows/adaptive-flow.md#kiyo-flow-001--reduce-ceremony-without-skipping-controls](../../../src/kiyo/workflows/adaptive-flow.md#kiyo-flow-001--reduce-ceremony-without-skipping-controls) | C/X/P: R = workflows/adaptive-flow.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-FLOW-002 | [workflows/implement-flow.md#kiyo-flow-002--sequence-authorized-changes-through-actual-evidence](../../../src/kiyo/workflows/implement-flow.md#kiyo-flow-002--sequence-authorized-changes-through-actual-evidence) | C/X/P: R = workflows/implement-flow.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-FLOW-003 | [workflows/read-only-flow.md#kiyo-flow-003--complete-analysis-without-introducing-mutation](../../../src/kiyo/workflows/read-only-flow.md#kiyo-flow-003--complete-analysis-without-introducing-mutation) | C/X/P: R = workflows/read-only-flow.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-FLOW-004 | [workflows/repair-and-handoff.md#kiyo-flow-004--classify-failures-and-bound-repair-cycles](../../../src/kiyo/workflows/repair-and-handoff.md#kiyo-flow-004--classify-failures-and-bound-repair-cycles) | C/X/P: R = workflows/repair-and-handoff.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-FLOW-005 | [workflows/repair-and-handoff.md#kiyo-flow-005--handoff-facts-and-authorized-next-actions](../../../src/kiyo/workflows/repair-and-handoff.md#kiyo-flow-005--handoff-facts-and-authorized-next-actions) | C/X/P: R = workflows/repair-and-handoff.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ENG-002 | [framework/engineering/requirements.md#kiyo-eng-002--make-behavior-and-acceptance-traceable](../../../src/kiyo/framework/engineering/requirements.md#kiyo-eng-002--make-behavior-and-acceptance-traceable) | C/X/P: R = framework/engineering/requirements.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ENG-003 | [framework/engineering/architecture.md#kiyo-eng-003--preserve-safe-boundaries-and-explicit-design-intent](../../../src/kiyo/framework/engineering/architecture.md#kiyo-eng-003--preserve-safe-boundaries-and-explicit-design-intent) | C/X/P: R = framework/engineering/architecture.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ENG-004 | [framework/engineering/coding.md#kiyo-eng-004--keep-changed-code-clear-bounded-and-safe](../../../src/kiyo/framework/engineering/coding.md#kiyo-eng-004--keep-changed-code-clear-bounded-and-safe) | C/X/P: R = framework/engineering/coding.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ENG-005 | [framework/engineering/testing.md#kiyo-eng-005--match-checks-to-behavior-risk-and-observed-results](../../../src/kiyo/framework/engineering/testing.md#kiyo-eng-005--match-checks-to-behavior-risk-and-observed-results) | C/X/P: R = framework/engineering/testing.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ENG-006 | [framework/engineering/quality.md#kiyo-eng-006--evaluate-affected-quality-with-proportionate-evidence](../../../src/kiyo/framework/engineering/quality.md#kiyo-eng-006--evaluate-affected-quality-with-proportionate-evidence) | C/X/P: R = framework/engineering/quality.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ENG-007 | [framework/engineering/change-scope.md#kiyo-eng-007--preserve-human-work-and-keep-the-diff-necessary](../../../src/kiyo/framework/engineering/change-scope.md#kiyo-eng-007--preserve-human-work-and-keep-the-diff-necessary) | C/X/P: R = framework/engineering/change-scope.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-PROF-001 | [profiles/extension-contract.md#kiyo-prof-001--bind-profiles-to-evidence-without-forcing-a-stack](../../../src/kiyo/profiles/extension-contract.md#kiyo-prof-001--bind-profiles-to-evidence-without-forcing-a-stack) | C/X/P: R = profiles/extension-contract.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-VERIFY-001 | [framework/evidence-contract.md#kiyo-verify-001--record-scoped-observations-for-every-check](../../../src/kiyo/framework/evidence-contract.md#kiyo-verify-001--record-scoped-observations-for-every-check) | C/X/P: R = framework/evidence-contract.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-VERIFY-002 | [framework/evidence-contract.md#kiyo-verify-002--bind-results-to-the-checked-state-and-baseline](../../../src/kiyo/framework/evidence-contract.md#kiyo-verify-002--bind-results-to-the-checked-state-and-baseline) | C/X/P: R = framework/evidence-contract.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-DONE-001 | [framework/definition-of-done.md#kiyo-done-001--close-the-agreed-workflow-against-current-required-evidence](../../../src/kiyo/framework/definition-of-done.md#kiyo-done-001--close-the-agreed-workflow-against-current-required-evidence) | C/X/P: R = framework/definition-of-done.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-REPORT-001 | [framework/reporting-contract.md#kiyo-report-001--report-scoped-work-without-manufacturing-an-audit-trail](../../../src/kiyo/framework/reporting-contract.md#kiyo-report-001--report-scoped-work-without-manufacturing-an-audit-trail) | C/X/P: R = framework/reporting-contract.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-INIT-001 | [workflows/init.md#kiyo-init-001--initialize-only-evidenced-and-authorized-project-state](../../../src/kiyo/workflows/init.md#kiyo-init-001--initialize-only-evidenced-and-authorized-project-state) | C/X/P: R = workflows/init.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-REQ-001 | [workflows/requirement.md#kiyo-req-001--define-evidenced-requirements-without-authorizing-implementation](../../../src/kiyo/workflows/requirement.md#kiyo-req-001--define-evidenced-requirements-without-authorizing-implementation) | C/X/P: R = workflows/requirement.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-IMPL-001 | [workflows/implement-flow.md#kiyo-impl-001--bind-daily-engineering-to-intent-baseline-and-checked-scope](../../../src/kiyo/workflows/implement-flow.md#kiyo-impl-001--bind-daily-engineering-to-intent-baseline-and-checked-scope) | C/X/P: R = workflows/implement-flow.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-REVIEW-001 | [workflows/review.md#kiyo-review-001--review-actual-scope-without-repairing-it](../../../src/kiyo/workflows/review.md#kiyo-review-001--review-actual-scope-without-repairing-it) | C/X/P: R = workflows/review.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-TEST-001 | [workflows/test.md#kiyo-test-001--separate-assessment-execution-and-test-authoring](../../../src/kiyo/workflows/test.md#kiyo-test-001--separate-assessment-execution-and-test-authoring) | C/X/P: R = workflows/test.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-SEC-011 | [workflows/security.md#kiyo-sec-011--bound-security-submodes-and-assurance-to-actual-evidence](../../../src/kiyo/workflows/security.md#kiyo-sec-011--bound-security-submodes-and-assurance-to-actual-evidence) | C/X/P: R = workflows/security.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-ARCH-001 | [workflows/architecture.md#kiyo-arch-001--separate-observed-architecture-from-approved-intent](../../../src/kiyo/workflows/architecture.md#kiyo-arch-001--separate-observed-architecture-from-approved-intent) | C/X/P: R = workflows/architecture.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-MEM-008 | [framework/memory-modes.md#kiyo-mem-008--bind-memory-modes-to-scoped-deltas-and-preserved-history](../../../src/kiyo/framework/memory-modes.md#kiyo-mem-008--bind-memory-modes-to-scoped-deltas-and-preserved-history) | C/X/P: R = framework/memory-modes.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-CONFIG-001 | [framework/project-configuration.md#kiyo-config-001--reuse-one-evidenced-project-configuration](../../../src/kiyo/framework/project-configuration.md#kiyo-config-001--reuse-one-evidenced-project-configuration) | C/X/P: R = framework/project-configuration.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| KIYO-POLICY-001 | [governance/policy-resolution.md#kiyo-policy-001--resolve-scope-and-authority-without-self-escalation](../../../src/kiyo/governance/policy-resolution.md#kiyo-policy-001--resolve-scope-and-authority-without-self-escalation) | C/X/P: R = governance/policy-resolution.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| kiyo.init | [skills/init/SKILL.md](../../../src/kiyo/skills/init/SKILL.md) | C/X/P: S = skills/init/SKILL.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| kiyo.requirement | [skills/requirement/SKILL.md](../../../src/kiyo/skills/requirement/SKILL.md) | C/X/P: S = skills/requirement/SKILL.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| kiyo.implement | [skills/implement/SKILL.md](../../../src/kiyo/skills/implement/SKILL.md) | C/X/P: S = skills/implement/SKILL.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| kiyo.review | [skills/review/SKILL.md](../../../src/kiyo/skills/review/SKILL.md) | C/X/P: S = skills/review/SKILL.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| kiyo.test | [skills/test/SKILL.md](../../../src/kiyo/skills/test/SKILL.md) | C/X/P: S = skills/test/SKILL.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| kiyo.security | [skills/security/SKILL.md](../../../src/kiyo/skills/security/SKILL.md) | C/X/P: S = skills/security/SKILL.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| kiyo.architecture | [skills/architecture/SKILL.md](../../../src/kiyo/skills/architecture/SKILL.md) | C/X/P: S = skills/architecture/SKILL.md | E; P only when authorized; IDE X unsupported | K | N | H | G |
| kiyo.memory | [skills/memory/SKILL.md](../../../src/kiyo/skills/memory/SKILL.md) | C/X/P: S = skills/memory/SKILL.md | E; P only when authorized; IDE X unsupported | K | N | H | G |

## Artifacts and limitations

| Candidate | Files / skills | ZIP SHA-256 | Content inventory SHA-256 |
| --- | --- | --- | --- |
| [claude](../../../dist/archives/kiyo-compass-claude-development.zip) | 794 / 8 | 10bc505a083f86276d0ba78ebb4c06fa64f93143ff607eed63898ffafc711672 | f4db50436dbed4f9158420dc36ef39ae2176bc4d74e387c78a325dd7d9e7d007 |
| [codex](../../../dist/archives/kiyo-compass-codex-development.zip) | 795 / 8 | 8c2594d3767dad46e66358b69afecbe0ce7787bfccb5dc3e035f5bb55522de5c | 0b6bdbf0526f4717e73729f989c4444bc9ed693870d035b0c49b6277f3f6fae4 |
| [copilot](../../../dist/archives/kiyo-compass-copilot-development.zip) | 794 / 8 | 9a5130c9fd2f102b18ce7b0fa3dc42f20e660834c357703299f3a6d3a4e2e4df | 819e8909c4341dabd1ff924d9188d280a709916b89e4e6a50d493912ebd134c2 |

[Final packaging execution](test-results-final.json) and [check interpretation](package-checks.md)
record actual results. ZIP hashes are computed integrity comparisons, not signature
verification. The P20–22 inventories remain historical evidence for their earlier
snapshots; this inventory identifies the current P23 bytes after the managed-block
scope/cleanup clarification. Old hashes must not certify updated content.

No native schema was changed during P23. Schema and capability claims retain the
P20–22 checked dates/limitations in [SOURCES](../../research/SOURCES.md). Native
installation, metadata matching, authority compliance, update/uninstall and
all host-specific resource reads await separate tests. No owner decision or
curated listing is implied by these development artifacts.
