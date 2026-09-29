# Kiyo Compass — Progress

Snapshot: 2026-09-29. Current prompt: **26 Native Integration (no-quota subset)**.
Task status: **DONE for the user-selected available no-quota checks and reporting**.
Full six-target integration acceptance is **PARTIALLY COMPLETE**: no model/agent
workflow or automatic Core activation was tested. No support-complete claim.

## Prompt 26 delivered scope

- [Live matrix](../compatibility/live-test-matrix.md) contains 72 separate records,
  twelve for each target, with expected cases separate from observed results.
- Claude CLI 2.1.220: native normal validation passes with version/author warnings;
  strict validation FAILs. Actual relocated directory and ZIP component discovery
  lists exactly eight Skills, no agents/hooks/MCP/LSP. No persistent installation.
- Codex CLI 0.158.0: actual disposable local catalog install/list/cache/uninstall,
  with three synthetic project files unchanged. Native cache equals all 795
  distribution files; independent static cache checker passes 4,956 links.
  Native fallback 1.0.0 does not set Kiyo's unassigned release version.
- [Evidence](../evidence/live/README.md) preserves commands, exits, warnings,
  snapshots, first helper encoding failure and corrected rerun. VS Code 1.139.1
  and named extension metadata do not establish an active IDE/account.
- User selected native checks without quota. IDE/Copilot runs remain NOT_TESTED;
  Codex IDE plugins remain UNSUPPORTED. No model session or account lookup.
- [Reproduction](../compatibility/live-reproduction-guide.md) and
  [owner-required tests](../compatibility/live-owner-required-tests.md) retain
  invocation/activation/update/behavioral gaps. Two complete bounded lifecycle
  rows PASS; partial metadata/cache evidence never upgrades other full cases.

P25's 48 host cases remain NOT_RUN; no behavioral metrics are inferred.
All 80 full requirement verifications remain NOT_RUN; **79 PARTIALLY_IMPLEMENTED /
1 NOT_IMPLEMENTED** unchanged. See [P26 checks](BASELINE.md#prompt-26-checks).
Product content, native overlays, distributions, version and LICENSE preserved.
Memory Impact: **NONE** for the developer project; synthetic fixture state only.

## Prompt 25 delivered scope

- [Catalog](../../tests/behavioral/evaluation/CATALOG.md): 32 cases, four for each
  of eight Skills, plus 16 cross-cutting cases with exact inputs/control/requirement
  refs, fixtures, allowed/forbidden effects and expected criteria.
- [Separate observations](../evidence/behavioral/observations.json): all 48 NOT_RUN,
  unknown host/model/version/settings, no fabricated output/actions/diff or grades.
  The user explicitly selected offline work after scoped PATH discovery.
- [Developer-only helper and protocol](../../tests/behavioral/evaluation/README.md)
  prepare fresh source-guided fixtures and capture hashes/mtime/scope changes;
  no agent launcher or consumer runtime. Forty-eight fixtures were materialized
  during actual offline checks; suspicious fixture scripts were not executed.
- [First actual harness run](../evidence/behavioral/harness-results-01.json):
  13 tests PASS, exit 0; negative comparator/scope/history tests included.
  [Validation/limits](../evidence/behavioral/validation-report.md) separate this
  success from agent compliance and native loading.
- [Metrics](../evidence/behavioral/metrics.json) remain unmeasured; human/model
  grading separate from objective evidence. [Defect/gate register](../evidence/behavioral/defects.md)
  defines critical release blockers and preserved first/rerun evidence.

Fifty-five trace rows gain authored case/protocol coverage, not executed behavioral
coverage. All 80 full verifications remain NOT_RUN; **79 PARTIALLY_IMPLEMENTED /
1 NOT_IMPLEMENTED** unchanged. See [P25 checks](BASELINE.md#prompt-25-checks).
All six native targets NOT_TESTED; prior Codex ingestion FAIL, IDE UNSUPPORTED,
P23 filesystem-symlink BLOCKED and owner DEC-001–004 remain open.
Canonical files/overlays/tools/packages untouched. Memory Impact: **NONE**.

## Prompt 24 delivered scope

- Added [developer-only tests and fixtures](../../tests/static/README.md), reusing
  existing builders and the standalone payload checker; no new dependencies.
- [Final execution](../evidence/static/test-results-final.json): 37 tests PASS,
  exit 0, no failures/errors/skips. Initial five checker/fixture errors and their
  fixes remain in [validation history](../evidence/static/validation-report.md).
- Actual canonical/ZIP checks cover eight Skills per package, closed metadata,
  37 required resources, 68 controls, 34 templates, scoped read-only/approval
  contracts, enums/examples, AST ownership/limits, Memory types and all 80 IDs.
- Three fresh extractions with spaces retain source-denied reference closure;
  112 input hashes and 2,383 payload files agree with P23 inventory.
- [Coverage interpretation](../evidence/static/coverage-interpretation.md)
  explicitly lists selected properties, not FULL SCHEMA VALIDATION, and preserves
  separate static/behavioral/native evidence. No canonical/overlay/package change.

Partial static coverage: REQ-002/003/006/009/011/019/020/022/023/026/027/040/
043–050/058–067/069/071–075/077–080 (40 trace rows).
Totals: **79 PARTIALLY_IMPLEMENTED / 1 NOT_IMPLEMENTED**; all 80 full verifications
remain NOT_RUN. See [P24 checks](BASELINE.md#prompt-24-checks).
Owner DEC-001–004, historical Codex ingestion FAIL/IDE UNSUPPORTED and P23
filesystem-symlink BLOCKED remain unresolved. Native targets NOT_TESTED.
No install/publication/global change or actual Memory write. Memory Impact: **NONE**.

## Prompt 23 delivered scope

- Added [developer-only build tooling and a closed input allowlist](../architecture/distribution-build.md),
  reusing the three native builders without changing schemas or adding dependencies.
- Created [three actual ZIPs](../evidence/packaging/parity-report.md#artifacts-and-limitations):
  794/795/794 files, eight Skills each. Two fresh builds produce identical inventories
  and ZIP bytes; every extracted operational reference stays inside its payload.
- [Isolation tests](../../tests/packaging/README.md) exercise paths with spaces,
  source-denied standalone inspection, exact case, LF/CRLF, unsafe ZIP entries,
  exclusion canaries, drift and no-op/overwrite preservation. Windows error 1314
  blocks only the additional real filesystem symlink probe. No OS sandbox claim.
- [Parity report](../evidence/packaging/parity-report.md) covers 68 controls plus
  eight Skills in 456 independent target records. Content is distinct from behavior.
- [Activation matrix](../compatibility/activation-matrix.md) keeps six targets separate.
  Canonical Init guidance now makes scope, outdated-Core reporting and block-only
  cleanup explicit; 24 generated copies were mechanically refreshed.

Partial coverage: REQ-002/003/005/006/007/009/017/024/026/059/061/064/067/076–080.
Totals: **79 PARTIALLY_IMPLEMENTED / 1 NOT_IMPLEMENTED**; all 80 full verifications
remain NOT_RUN. [P23 checks](BASELINE.md#prompt-23-checks) and
[actual evidence](../evidence/packaging/package-checks.md) retain all limits.
No installation/publication or actual user-state write. Memory Impact: **NONE**.

## Prompt 22 delivered scope

- Revalidated [sixteen current primary sources](../research/SOURCES.md#prompt-22-copilot-revalidation),
  including an explicit Microsoft source fallback for the rendered plugins page
  timeout and the VS Code setup redirect. No schema decision relies on chat memory.
- Added [Copilot overlay](../../platforms/copilot/README.md), one minimal Agent Plugins
  1.0.0 manifest and [CLI/VS Code delta](../compatibility/copilot-package.md).
  Both targets independently document the selected format; no unsupported
  fields, permission settings, VSIX, App, service or extra public skill.
- [Developer packager](../../tools/package_copilot.py) produced
  [794-file bundle](../../dist/copilot/kiyo-compass/plugin.json), eight entries,
  97 shared resources each and a contained native adapter. All 105 canonical
  product files and 1,589 previous Claude/Codex payload files are unchanged.
- Actual offline checks pass for 4,964 local links, frontmatter/canonical parity,
  relocation/rebuild no-op and nine rejection cases. A full sample managed
  block is 116 words; static rendering is not verified Init behavior.
- Added [native lifecycle guide](../compatibility/copilot-installation.md),
  [disposable protocol](../compatibility/copilot-local-test-protocol.md) and
  [20 integration specifications](../../tests/integration/copilot/scenarios.md)
  with separate NOT_RUN columns. No native parser/install/chat test ran.
- Exact CLI skill qualification/built-in collisions and plugin rule loading
  remain UNKNOWN; VS Code slash prefix is DOCUMENTED_ONLY. Scoped PATH/extension
  lookups did not establish a Copilot installation/version, not global absence.
  No marketplace metadata or publisher/source ID is fabricated.

Partial coverage: REQ-002–007/009–011/017/026/027/059–061/064/067/076–079; REQ-080 continuity.
Totals remain **79 PARTIALLY_IMPLEMENTED / 1 NOT_IMPLEMENTED**; all 80 full
verifications stay NOT_RUN. [P22 checks](BASELINE.md#prompt-22-checks) and
[artifact evidence](../evidence/copilot/package-checks.md) retain the limits.
Owner decisions and six live targets remain open. Memory Impact: **NONE**.

## Prompt 21 delivered scope

- Revalidated [twelve official OpenAI sources](../research/SOURCES.md#prompt-21-codex-revalidation)
  with actual redirects, dates and limits. IDE plugins remain UNSUPPORTED; no
  standalone fallback was adopted. CLI and IDE live results stay NOT_TESTED.
- Added [independent Codex metadata/adapter](../../platforms/codex/README.md):
  a portable root manifest and generated compatibility manifest, documented
  package interface, inactive catalog template and minimal AGENTS guidance.
  Optional agents/openai.yaml is unnecessary and omitted. No Claude manifest reuse.
- Generated [Codex plugin](../../dist/codex/kiyo-compass/plugin.json):
  795 files, eight entries, 97 shared references per entry plus native adapters.
  Canonical 105 files/68 controls and all 794 prior Claude artifact files remain
  unchanged. Only developer packaging uses Python; no consumer runtime.
- Offline checks passed for 4,956 contained links, canonical parity, independent
  relocation/reproducibility, no-op snapshots and seven rejection cases. The
  sample managed block is 108 words; this is static evidence, not Init behavior.
- The required bundled ingestion validator actually returned **FAIL** for missing
  version, author and interface.developerName. [Failure evidence](../evidence/codex/package-checks.md)
  is retained; it is not waived, labeled PASS or fixed with invented identity.
  [Submission requirements](../compatibility/codex-submission.md) separate that
  readiness gate from this prompt's development-package work.
- Added [local test protocol](../compatibility/codex-local-test-protocol.md) and
  [18 integration specifications](../../tests/integration/codex/scenarios.md), NOT_RUN.
  Actual CLI version/help identifies 0.158.0 and plugin add/remove grammar;
  extension metadata reports 26.917.62051, active engine UNKNOWN. No install,
  global settings, safety bypass, marketplace registration or submission.

Partial coverage: REQ-002–007/009/010/017/026/027/059–061/064/067/076–079;
REQ-080 continuity. Totals unchanged: **79 PARTIALLY_IMPLEMENTED /
1 NOT_IMPLEMENTED**. All 80 full requirement verifications remain NOT_RUN.
No native compatibility, ingestion readiness or publication acceptance is claimed.

Checks: [P21-C01–C08](BASELINE.md#prompt-21-checks), including the explicit
ingestion FAIL. Owner identity/version/license/destination gates and DEC-004
remain open. Memory Impact: **NONE for developer project memory**.

## Prompt 20 delivered scope

- Revalidated thirteen current official Claude documentation sources with dates,
  observed destinations and limits in [SOURCES](../research/SOURCES.md#prompt-20-claude-revalidation).
  CLI and VS Code evidence remain independent.
- Added a minimal [Claude overlay](../../platforms/claude/README.md), inactive
  owner-input marketplace template, native invocation/activation reference and
  developer-only [packager](../../tools/package_claude.py).
  The working namespace is kiyo-compass; no release identity/version was invented.
- Generated [dist/claude manifest](../../dist/claude/.claude-plugin/plugin.json)
  and eight self-contained skill trees: 794 files, 97 canonical shared resources
  per skill, no hooks/MCP/runtime. Canonical 105 product files and 68 controls
  remain unchanged. Shared duplication is generated, not separately authored.
- Offline checks passed: 4,956 contained references, source parity, independent
  relocation, repeat no-op and five rejection cases. Entry budgets and a
  114-word sample managed block passed static checks. These do not prove loading,
  native approval enforcement or Init behavior.
- Recorded [actual evidence/inventory](../evidence/claude/package-checks.md),
  [disposable protocol](../compatibility/claude-installation-test-protocol.md)
  and [16 integration specifications](../../tests/integration/claude/scenarios.md).
  Native validation and all integration cases remain NOT_RUN; all six native
  targets remain NOT_TESTED. Live tests are deferred to Prompt 26.
- Actual terminal version is 2.1.220; scoped extension manifests declare
  2.1.283 / 2.1.284. Active extension/VS Code version/account remain UNKNOWN.
  No install, marketplace registration, publication or global setting change.

Coverage: partial artifact/documentation coverage for
REQ-002/003/004/005/006/007/009/010/026/027/059/060/061/064/067/076/077/078/079;
REQ-080 continuity. REQ-002/003/006/076/078/079 newly partial:
**79 PARTIALLY_IMPLEMENTED / 1 NOT_IMPLEMENTED**. All 80 full verifications
remain NOT_RUN; REQ-001 and final release acceptance remain unresolved.

Checks: [Prompt 20 evidence](BASELINE.md#prompt-20-checks).
Memory Impact: **NONE for developer project memory**. No project bootstrap or
Memory/config/policy was created. Owner publication decisions remain open.

## Prompt 19 delivered scope

- Added [configuration specification](../../src/kiyo/framework/project-configuration.md)
  with seven logical fields; extended the existing Init context template.
  Preserve .kiyo/policy.md as the established config equivalent and any accepted
  legacy locator. No duplicate .kiyo/config.md or developer-project state was created.
- Added [policy resolution](../../src/kiyo/governance/policy-resolution.md),
  neutral [organization](../../src/kiyo/templates/policies/organization-policy.md) /
  [project](../../src/kiyo/templates/policies/project-policy.md) templates and
  three optional [presets](../../src/kiyo/governance/presets.md).
  Preset, G1–G4, risk, policy acceptance and native enforcement remain distinct.
- Init may offer drafts without adopting policy or selecting providers; Security
  governance checks fields, provenance, conflicts and exception validity read-only.
  Policy edits/adoption and operational approval are separate. An overdue review
  does not expire a prohibition; an expired exception grants no further permission.
- Added KIYO-CONFIG-001 / KIYO-POLICY-001: 68 controls, 34 neutral templates,
  105 product files (8 unchanged public entries plus 97 shared resources).
  No runtime, engine, watcher, live organization policy or native setting was added.
- Added [16 scenario specifications](../../tests/behavioral/organization-policy/scenarios.md).
  [Bounded forward trials](../evidence/organization-policy/forward-trials.md)
  record four actual read-only responses and unchanged synthetic fixture snapshots.
  Full scenarios remain NOT_RUN and native hosts NOT_TESTED.

Coverage: partial source instruction coverage for
REQ-011/013/017/037/047/049/050/051/054/055/068/073; REQ-080 continuity.
All were already partial: 73 PARTIALLY_IMPLEMENTED / 7 NOT_IMPLEMENTED remain.
All 80 full requirement verifications remain NOT_RUN; no release/native claim.

Checks: [Prompt 19 evidence](BASELINE.md#prompt-19-checks).
Memory Impact: **NONE for developer project memory**; no actual .kiyo store/config
or organization policy was adopted. Owner decisions remain open.

## Prompt 18 delivered scope

- Added canonical [Memory](../../src/kiyo/skills/memory/SKILL.md), name memory /
  logical ID kiyo.memory, name/description frontmatter only, 74 lines / 609 words.
- Added [mode definitions](../../src/kiyo/framework/memory-modes.md) and neutral
  [diff](../../src/kiyo/templates/reports/memory-diff.md),
  [sync](../../src/kiyo/templates/reports/memory-sync-report.md) and
  [repair](../../src/kiyo/templates/reports/memory-repair-report.md) templates.
  Reused the shared lifecycle, provenance, approval and report contracts.
- show/check and previews write zero files; sync/repair need a necessary scoped
  delta and latest-entry/evidence reread. Preserve IDs, dates, approved history
  and human text. No-delta repeat sync is a no-op, not a freshness refresh.
- Actual observation corrections differ from approved-intent conflicts and
  missing evidence. Unknown remains UNVERIFIED; no decision normalization,
  folder rewrite, second store, forced Init, source fix or watcher.
- Added KIYO-MEM-008 (66 controls) and
  [18 Memory Skill scenarios](../../tests/behavioral/memory/skill-scenarios.md),
  separate from the original twenty lifecycle scenarios.
  [Forward evidence](../evidence/memory/forward-trials.md) records actual bounded
  mode, controlled human-edit and repeated-sync effects with limitations.
- Final source inventory is exactly Init, Requirement, Implement, Review, Test,
  Security, Architecture and Memory. Router/Governance Review/Skill Audit/Self-check
  remain shared procedures/submodes. All eight temporary copies contain 92 shared
  resources; canonical inventory is not a native catalog or host acceptance.

Coverage: partial Memory/shared instruction coverage for
REQ-017/018/019/020/021/022/023/024/026/027/040/044/075; REQ-080 continuity updated.
REQ-075 was already partial: totals remain 73 PARTIALLY_IMPLEMENTED /
7 NOT_IMPLEMENTED. All 80 full verifications remain NOT_RUN; native targets
remain NOT_TESTED. Complete scenario matrices are not promoted by bounded trials.

Checks: [Prompt 18 evidence](BASELINE.md#prompt-18-checks).
Memory Impact: **NONE for developer project memory**. Only isolated synthetic
fixture writes were used for validation; repository Memory was not initialized.
Owner publication/native-route decisions remain open.

## Prompt 17 delivered scope

- Added canonical [Architecture](../../src/kiyo/skills/architecture/SKILL.md),
  name architecture / logical ID kiyo.architecture, name/description only.
  Analysis/review/impact/drift remain one public skill with read-only effects.
- Added [shared procedure](../../src/kiyo/workflows/architecture.md),
  [observation](../../src/kiyo/templates/reports/architecture-observation.md) and
  [impact](../../src/kiyo/templates/reports/architecture-impact-report.md) templates;
  extended the existing [drift report](../../src/kiyo/templates/reports/memory-architecture-drift-report.md).
  Nine inspection dimensions, five output categories and seven drift fields
  separate source observations, approved intent, proposals and runtime unknowns.
- Comparison outcomes Match / Deviation / Insufficient evidence are separate
  from task/check statuses. Actual usage differs from package declaration;
  no ADR means no established mandate in scope, not permission to invent one.
- No automatic source/Memory/policy/ADR/report writes, execution, refactor,
  migration or score without rubric/evidence. Memory Impact is reported only.
  Relevant existing safe patterns and approval provenance remain binding inputs.
- Added KIYO-ARCH-001 (65 controls), shared integrations and
  [16 scenario specifications](../../tests/behavioral/architecture/scenarios.md).
  [Bounded forward evidence](../evidence/architecture/forward-trials.md) separates
  actual read-only variants from complete matrix/native acceptance.
  Entry: 71 lines / 515 words. Seven temporary source copies each contain
  88 shared resources; no consumer runtime or generator dependency.

Coverage: partial Architecture/shared instruction coverage for
REQ-019/022/023/024/026/027/028/033/040/044/074; REQ-080 continuity updated.
REQ-074 newly partial: 73 PARTIALLY_IMPLEMENTED / 7 NOT_IMPLEMENTED.
All 80 full verifications remain NOT_RUN; six native targets remain NOT_TESTED.
Sixteen scenarios are NOT_RUN as a full matrix; fixture evidence is separately scoped.

Checks: [Prompt 17 evidence](BASELINE.md#prompt-17-checks).
Memory Impact: **NONE for developer project memory**. Synthetic conflicts were
assessment inputs; no Project Memory or approved decision was rewritten.
Owner decisions remain open.

## Prompt 16 delivered scope

- Added canonical [Security](../../src/kiyo/skills/security/SKILL.md), name
  security / logical ID kiyo.security, with name/description frontmatter only.
  application/skills/governance/self-check are logical submodes under one entry.
- Added [shared procedure](../../src/kiyo/workflows/security.md),
  [submode checklists](../../src/kiyo/agent-security/security-submodes.md),
  [security finding](../../src/kiyo/templates/reports/security-finding.md) and
  [honest self-check](../../src/kiyo/templates/reports/self-check-report.md).
  Refined the existing assessment template and linked shared AST/trust/provenance
  resources without refreshing their external-source dates or native claims.
- Supplied-scope read-only assessment forbids global home/plugin sweeps, credentials/
  environment dumps, probes, suspicious payload execution, scanner installs and
  automatic remediation. Missing write approval is resolved only for concrete
  implementation scope; real matching approval is reused.
- Findings separate concept/evidence/impact/confidence/mitigation/owner/coverage.
  Signature NOT_VERIFIED is an assurance field, not a sixth check status; incomplete
  inventory is explicit. Self-check separates declarations/read resources from
  actual native activation, cryptographic integrity, sandbox/network enforcement.
- Added KIYO-SEC-011 (64 controls), integration references and
  [18 scenario specifications](../../tests/behavioral/security/scenarios.md).
  Actual scoped trials are separately recorded in
  [forward evidence](../evidence/security/forward-trials.md).
  Entry validates at 80 lines / 615 words; six temporary copies each contain
  85 shared files with contained references. No native/runtime/security guarantee.

Coverage: partial Security/shared instruction coverage for
REQ-026/027/042/051/058/061/062/063/065/067/073; REQ-080 continuity updated.
REQ-073 newly partial: 72 PARTIALLY_IMPLEMENTED / 8 NOT_IMPLEMENTED.
All 80 full verifications remain NOT_RUN; six native targets remain NOT_TESTED.
Complete scenario matrices remain NOT_RUN; source trials cover only recorded
synthetic variants and cannot establish full AST compliance or native security.

Checks: [Prompt 16 evidence](BASELINE.md#prompt-16-checks).
Memory Impact: **NONE for developer project memory**. Synthetic Memory is
assessment input only, never a source of new authority or an automatic write.
Owner decisions remain open.

## Prompt 15 delivered scope

- Added canonical [Test](../../src/kiyo/skills/test/SKILL.md), name test / logical
  ID kiyo.test, with name/description only. assess/run/write are logical UX modes,
  not universal native parser syntax or permission settings.
- Added [shared procedure](../../src/kiyo/workflows/test.md),
  [mode/safety matrix](../../src/kiyo/framework/test-mode-safety.md),
  [test plan](../../src/kiyo/templates/test-plan.md) and
  [Test report](../../src/kiyo/templates/reports/test-report.md).
  Integrated existing testing, evidence, completion, reporting and routing contracts.
- assess remains read-only; run preflights exact non-production checks/artifacts
  and preserves tracked source; write limits changes to requested tests/fixtures.
  Production fixes/new dependencies/installations outside scope need separate
  authority. No weakening/deleting/skipping tests to obtain green results.
- Counts, skips, blockers, baseline relation and coverage require actual evidence.
  Test-source existence and authoring completion are separate from execution.
  Missing required environments remain blocked; no automatic installs or fallback
  to production. Multi-mode requests reuse valid scope after effect preflight.
- Added KIYO-TEST-001 (63 controls) and
  [18 scenario specifications](../../tests/behavioral/test/scenarios.md).
  Actual bounded trials are separately recorded in
  [forward evidence](../evidence/test/forward-trials.md).
  Entry validates at 89 lines / 692 words; five temporary copies each contain
  81 shared files with contained references. No native/runtime addition.

Coverage: partial Test/shared instruction coverage for
REQ-023/027/038/039/040/041/044/072/077; REQ-080 continuity updated.
REQ-072 newly partial: 71 PARTIALLY_IMPLEMENTED / 9 NOT_IMPLEMENTED.
All 80 full verifications remain NOT_RUN; six native targets remain NOT_TESTED.
Complete scenario matrices are NOT_RUN; actual source trials support only their
recorded modes/effects, including intentionally failing fixture checks.

Checks: [Prompt 15 evidence](BASELINE.md#prompt-15-checks).
Memory Impact: **NONE for developer project memory**. Synthetic test authoring/
execution is developer validation outside the product payload. Owner decisions remain open.

## Prompt 14 delivered scope

- Added canonical [Review](../../src/kiyo/skills/review/SKILL.md), name review /
  logical ID kiyo.review, with name/description frontmatter only. It reviews
  existing human/AI changes, specified files, supplied ranges or actually accessible
  PR context; no implicit source/test/Memory edits or build/test execution.
- Added the [shared procedure](../../src/kiyo/workflows/review.md),
  [severity/confidence guide](../../src/kiyo/framework/review-severity-confidence.md)
  and [bounded report](../../src/kiyo/templates/reports/review-report.md).
  Refined the existing [finding template](../../src/kiyo/templates/reports/review-finding.md)
  with all eight requested fields plus classification and provenance.
- Default comparison is actual current workspace, with distinct index/worktree/
  untracked coverage. Missing bases, zero diff, effective policy protections,
  uncertain requirements, redaction and stale Memory have explicit handling.
  DONE describes bounded review delivery, never repair or production readiness.
- Added KIYO-REVIEW-001 (62 controls), integration references and
  [16 scenario specifications](../../tests/behavioral/review/scenarios.md).
  Bounded source trials are separately recorded in
  [forward evidence](../evidence/review/forward-trials.md).
- Entry validation passed at 73 lines / 583 words. Four temporary resource copies
  each contain 77 shared files and resolve contained references. These are source
  checks, not native packages or host loading.

Coverage: partial Review/shared instruction coverage for
REQ-023/027/028/040/041/044/071/077; REQ-080 continuity updated.
REQ-071 newly partial: 70 PARTIALLY_IMPLEMENTED / 10 NOT_IMPLEMENTED.
All 80 full verifications remain NOT_RUN; six native targets remain NOT_TESTED.
Full scenario matrices remain NOT_RUN; bounded trials cover only recorded variants.

Checks: [Prompt 14 evidence](BASELINE.md#prompt-14-checks).
Memory Impact: **NONE for developer project memory**. Fixture Memory remains
unchanged; reported corrections are proposals. Owner decisions remain open.

## Prompt 13 delivered scope

- Added canonical [Implement](../../src/kiyo/skills/implement/SKILL.md),
  name implement / logical ID kiyo.implement, name/description frontmatter only.
  Features, bug fixes and explicitly scoped refactors require actual change intent;
  review/analyze-only requests do not enter implementation.
- Added a neutral [short plan](../../src/kiyo/templates/short-plan.md) and refined
  [shared implementation flow](../../src/kiyo/workflows/implement-flow.md), reusing
  existing repair/handoff, engineering/compact reports, governance, evidence and
  Memory contracts. The entry covers all sixteen requested workflow obligations;
  Tiny work may use a scope sentence instead of a plan file.
- Added KIYO-IMPL-001 (61 controls), conditional references and
  [16 scenario specifications](../../tests/behavioral/implement/scenarios.md).
  Actual bounded source trials are separate in
  [forward evidence](../evidence/implement/forward-trials.md).
- Baseline/human changes, minimal scope, necessary tests, inspected command effects,
  valid approval reuse, failure attribution and bounded repairs remain explicit.
  Auth/schema is assessed from actual effects/policy; migration drafting is distinct
  from applying. No production DB fallback, automatic commit/PR/deploy or decision rewrite.
- Entry validation passed at 93 lines / 789 words. Temporary copies for three
  authored entries each contain 74 shared files; no native package/activation
  or consumer runtime is introduced.

Coverage: partial Implement/shared instruction coverage for
REQ-015/023/026/027/029/030/033–035/039/040/044/049/070;
REQ-080 continuity updated. REQ-070 newly partial:
69 PARTIALLY_IMPLEMENTED / 11 NOT_IMPLEMENTED.
All 80 full verifications remain NOT_RUN; six native targets remain NOT_TESTED.
Full scenario matrices are NOT_RUN; source trials only support their recorded scopes.

Checks: [Prompt 13 evidence](BASELINE.md#prompt-13-checks).
Memory Impact: **NONE for developer project memory**. Isolated synthetic fixture
edits/checks are developer evidence, not changes to this repository's Memory or app.
Owner publication/native-gap decisions remain open.

## Prompt 12 delivered scope

- Added canonical [Requirement](../../src/kiyo/skills/requirement/SKILL.md),
  name requirement / logical ID kiyo.requirement, with name/description only.
  Raw requests, issues, documents and proposed changes become scoped requirements;
  the skill stops before implementation.
- Added the [shared procedure](../../src/kiyo/workflows/requirement.md),
  [fourteen-field template](../../src/kiyo/templates/requirement.md) and
  [readiness checklist](../../src/kiyo/framework/requirement-readiness.md).
  Discover authorized Memory/current evidence before asking; separate Existing facts,
  User requirements, AI proposals and Unresolved decisions. Never invent HTTP,
  business permission or retention decisions.
- Chat is default. Only the requested/approved specification path may be written;
  source/tests/config/Memory are forbidden outputs. Preserve human edits and IDs;
  a chat-local provisional ID is not an allocated project record.
- Readiness is exactly READY_FOR_IMPLEMENTATION, DECISION_REQUIRED or
  INSUFFICIENT_EVIDENCE, separate from task completion and implementation approval.
  Aligned shared DoD/report labels with Prompt 12; no automatic implementation.
- Added KIYO-REQ-001 (60 controls), conditional integration references and
  [12 input/output scenario specifications](../../tests/behavioral/requirement/scenarios.md).
  Bounded source trials are recorded separately in
  [forward evidence](../evidence/requirement/forward-trials.md).
  Entry validation passed at 69 lines / 567 words. Two temporary resource copies
  each contain 73 shared files with contained links; no native package is implied.

Coverage: partial Requirement/shared instruction coverage for
REQ-016/023/026/027/031/032/043/044/069; REQ-080 continuity updated.
REQ-069 newly partial: 68 PARTIALLY_IMPLEMENTED / 12 NOT_IMPLEMENTED.
All 80 full verification states remain NOT_RUN and all six native targets NOT_TESTED.
Complete scenario suites remain NOT_RUN; bounded trials establish only their scope.

Checks: [Prompt 12 evidence](BASELINE.md#prompt-12-checks).
Memory Impact: **NONE for developer project memory**; no Memory/config/application
changes. Six build records carry continuity; publication/native-gap decisions remain open.

## Prompt 11 delivered scope

- Added the first canonical [Init skill](../../src/kiyo/skills/init/SKILL.md):
  name init, logical ID kiyo.init, description covering onboarding, initial
  project analysis, Project Memory creation and setup-readiness inspection.
  Ordinary feature/bug work does not trigger it; metadata contains only name/description.
- Added the [twelve-step Init procedure](../../src/kiyo/workflows/init.md),
  [bounded discovery](../../src/kiyo/framework/init-discovery.md),
  [activation/managed-block guidance](../../src/kiyo/framework/init-activation.md),
  [expected output examples](../../src/kiyo/framework/init-output-examples.md) and
  [neutral context template](../../src/kiyo/templates/init/project-context.md).
  Preserve canonical paths, human changes and native instructions; reruns are
  incremental/no-op, preview is read-only, and empty projects get no assumed stack/app.
- Added KIYO-INIT-001 (59 controls total), conditional reference/router updates and
  [16 scenario specifications](../../tests/behavioral/init/scenarios.md).
  Bounded source-guided trial results are recorded separately in
  [forward evidence](../evidence/init/forward-trials.md); no native activation inferred.
- Entry validation passed: 73 lines / 566 words, name/description only.
  One-off temporary resource-copy/link-transform check passed for 70 shared files;
  this is not a native package/generator or live cache test.
- Allowed consumer writes remain necessary authorized project Memory/config/
  managed guidance only; source/dependency/test/global/credential writes are forbidden.
  No initializer executable, package installation, hook, public-skill installation
  or initialization of this developer project's state was performed.

Coverage: partial instruction/entry implementation for
REQ-009/014–017/020/024/026/027/068; REQ-080 continuity updated.
Current totals: 67 PARTIALLY_IMPLEMENTED / 13 NOT_IMPLEMENTED
(REQ-026/068 newly partial). All 80 full requirement verifications remain NOT_RUN.
All six native targets remain NOT_TESTED; research dates/native gaps are unchanged.

Checks: [Prompt 11 evidence](BASELINE.md#prompt-11-checks).
Memory Impact: **NONE for developer project memory**; build records carry continuity.
Synthetic fixture state changes/results are separate, never developer Memory.
Owner publication/native-gap decisions remain open and do not block Requirement authoring.

## Prompt 10 delivered scope

- Added the shared [Evidence Contract](../../src/kiyo/framework/evidence-contract.md)
  with nine check fields, five exact statuses, applicability/mandatory boundaries,
  requirement-to-evidence trace, baseline attribution and final-state rechecks.
  An authored test, historical PASS or missing environment cannot become current PASS/N/A.
- Added [Definition of Done](../../src/kiyo/framework/definition-of-done.md)
  with workflow-specific completion for all eight logical skills, four exact task
  statuses, current approvals/checks, scoped self-review and mandatory Memory sync.
  Requirement delivery and implementation readiness are separate.
- Added [reporting contract and seven neutral templates](../../src/kiyo/framework/reporting-contract.md#template-selection):
  compact task, engineering, approval, drift, finding, security and handoff.
  Chat is default; disk output requires actual write scope. No secrets/raw logs/
  private reasoning, guessed identities/counts or tamper-proof/independent-audit claims.
- Added four stable controls (58 total) and
  [20 synthetic good/bad scenarios](../../tests/behavioral/verification/scenarios.md),
  all NOT_RUN. Integrated conditional references into existing flows/testing/
  approval guidance; canonical task-status details now live in DoD.
- Updated architecture/source/build records. No public skill, runtime, automatic
  evidence store, project-memory write or native mechanism is introduced.
  No external source or platform/schema research was refreshed.

Coverage: partial shared instruction/template implementation for
REQ-039–046/049/077; REQ-080 continuity updated. Current totals:
65 PARTIALLY_IMPLEMENTED / 15 NOT_IMPLEMENTED (REQ-043 newly partial).
All 80 full requirement verifications remain NOT_RUN; all six live targets NOT_TESTED.

Checks: [Prompt 10 evidence](BASELINE.md#prompt-10-checks), with the nine-field record.
Memory Impact: **NONE for project memory**; only build continuity updated.
Owner publication/native-gap decisions remain open and do not block scoped Init authoring.

## Prompt 09 delivered scope

- Added [six actionable engineering standards](../../src/kiyo/framework/engineering/index.md):
  requirements, architecture, coding, testing, quality and change scope.
  Conditional selection preserves compact Core and read-only/write boundaries.
- Added optional [.NET](../../src/kiyo/profiles/dotnet.md),
  [Angular](../../src/kiyo/profiles/angular.md), [Python](../../src/kiyo/profiles/python.md)
  and [PostgreSQL](../../src/kiyo/profiles/postgresql.md) profiles, each starting with
  actual version/config/toolchain/architecture discovery. No forced libraries,
  unsolicited architecture migration, package upgrades or database execution.
- Added [profile extension contract](../../src/kiyo/profiles/extension-contract.md)
  with bounded React/Java/company outlines, not full/tested stack recipes.
- Added [concept → Kiyo rule → expected evidence mapping](../../src/kiyo/framework/engineering/standards-mapping.md).
  Rechecked S01–S07 public ISO catalogues and recorded E01–E06 official profile
  sources on 2026-09-29; DOCUMENTED_ONLY, no clauses/certification or exact ISO
  quality-taxonomy claim. Other source check dates remain scoped.
- Added seven controls (54 total) and
  [16 synthetic engineering/profile scenarios](../../tests/behavioral/engineering/scenarios.md),
  all NOT_RUN. Updated relevant loading/architecture/source/build records.
  No runtime, public skill, manifest, dependency installation or consumer generator.

Coverage: partial instruction implementation for REQ-031–038/053/056;
REQ-080 continuity updated. Current totals: 64 PARTIALLY_IMPLEMENTED /
16 NOT_IMPLEMENTED; all 80 full requirement verifications remain NOT_RUN.
The four new partial rows are REQ-031/036/037/038. Public skills remain pending;
all six native targets remain NOT_TESTED.

Checks: [Prompt 09 evidence](BASELINE.md#prompt-09-checks).
Memory Impact: **NONE for project memory**; no project memory/policy initialized
or synced. Publication decisions remain open and do not block Prompt 10 authoring.

## Prompt 08 delivered scope

- Added [Workflow Router](../../src/kiyo/workflows/workflow-router.md) with six
  input/output fields and only Init / Requirement / Implement / Review / Test /
  Security / Architecture / Memory as primary skills. Selection is not native
  invocation, an authority grant, agent spawning or executable dispatch.
- Added [adaptive flow](../../src/kiyo/workflows/adaptive-flow.md),
  [implementation flow](../../src/kiyo/workflows/implement-flow.md) and
  [read-only flow](../../src/kiyo/workflows/read-only-flow.md), reusing shared
  governance, evidence, Memory and security references. Tiny reduces ceremony
  without skipping authority, required approval, verification or memory impact.
- Added [repair and handoff](../../src/kiyo/workflows/repair-and-handoff.md):
  baseline/regression/environment/unknown distinctions, at most two unsuccessful
  repair cycles by default, scope reassessment and fact-based authorized handoff.
- Added [30 Thai/English routing rows and nine flow/recovery specifications](../../tests/behavioral/routing/truth-table.md).
  All are synthetic expected behavior, execution NOT_RUN. No truth-table parsing
  result is represented as a live route or model-compliance test.
- Added six stable controls (47 total), conditional context-loading pointer,
  source README/architecture updates and build continuity. Bootstrap is unchanged.
  No public skill, native manifest, executable router, runtime or orchestration.

Coverage: partial shared guidance for REQ-025/027–030/032–035/039–042/044/045/049/051.
REQ-026/068–075 receive routing/shared-flow input only, not public-skill acceptance.
REQ-080 continuity updated. Current totals: 60 PARTIALLY_IMPLEMENTED /
20 NOT_IMPLEMENTED; all 80 full requirement verifications remain NOT_RUN.
All six native targets remain NOT_TESTED. Prior native/research dates unchanged.

Checks: [Prompt 08 evidence](BASELINE.md#prompt-08-checks).
Memory Impact: **NONE for project memory**; build records carry continuity.
No project memory/policy initialized or synced; owner publication decisions remain open.

## Prompt 07 delivered scope

- Rechecked official OWASP AST landing/detail pages, ASI release announcement and
  ASVS project status; recorded URL destinations, check dates and limitations in
  [sources](../research/SOURCES.md#prompt-07-owasp-revalidation).
  AST remains public-review draft; AST and ASI are distinct identifiers.
- Added [AST01–AST10 mapping](../../src/kiyo/agent-security/owasp-ast10.md):
  risk, Kiyo control IDs, shared procedure, expected behavior, required evidence,
  four responsibility categories, residual limits and case references.
- Added [trust/metadata and layered Skill Audit](../../src/kiyo/agent-security/trust-review.md),
  [injection handling](../../src/kiyo/agent-security/prompt-injection.md),
  [provenance/update review](../../src/kiyo/agent-security/update-and-provenance.md)
  and [ownership/parity](../../src/kiyo/agent-security/control-ownership.md).
- Added a separate [Application Security checklist](../../src/kiyo/agent-security/application-security.md)
  covering all nine requested topics; no invented ASVS clauses or certification.
- Added four optional neutral [record templates](../../src/kiyo/agent-security/control-ownership.md#optional-file-records)
  for inventory, approval, revocation and incidents. No populated user records,
  central service, watcher or runtime security enforcement was created.
- Added [19 synthetic scenario specifications](../../tests/behavioral/agent-security/scenarios.md),
  execution NOT_RUN. Native per-control gaps remain UNKNOWN/unverified across
  six targets, retaining the prior unsupported Codex IDE plugin route explicitly.
- Added KIYO-SEC-001–010 (41 controls total), conditional Governance Review routing,
  source README/architecture and research/build-state updates. No public skill,
  native overlay, signature verifier, scanner dependency or dangerous operation.

Coverage: partial instruction implementation for REQ-005/007/012/027/040/049/051/
053/057–067/077; REQ-073 receives shared procedure/checklist input only, without
a public Security skill. REQ-080 continuity updated. Current totals:
55 PARTIALLY_IMPLEMENTED / 25 NOT_IMPLEMENTED. All 80 full requirement verifications
remain NOT_RUN and all six native targets NOT_TESTED.

Checks: [Prompt 07 evidence](BASELINE.md#prompt-07-checks).
Memory Impact: **NONE for project memory**; existing build records carry continuity.
No project inventory/policy/memory initialized; owner publication decisions remain open.

## Prompt 06 delivered scope

- Added nine policies under src/kiyo/governance/:
  [AI usage](../../src/kiyo/governance/ai-usage.md),
  [governance levels](../../src/kiyo/governance/governance-levels.md),
  [risk](../../src/kiyo/governance/risk-assessment.md),
  [human approval](../../src/kiyo/governance/human-approval.md),
  [data handling](../../src/kiyo/governance/data-handling.md),
  [permissions](../../src/kiyo/governance/permissions.md),
  [dangerous actions](../../src/kiyo/governance/dangerous-actions.md),
  [dependency governance](../../src/kiyo/governance/dependency-governance.md) and
  [provider policy](../../src/kiyo/governance/provider-policy.md).
- Defined G1–G4 as advisory Kiyo modes, separate from LOW/MEDIUM/HIGH/CRITICAL
  risk and actual native permissions. Risk covers eight contextual dimensions.
- Specified eight approval-request contents, scope matching/reuse/reassessment,
  actual human authority, organization prohibition and host-denial boundaries.
- Classified data from content/policy and bounded provider/account/model claims,
  including Unknown facts and absence of DLP/egress or pre-policy guarantees.
- Added [18 decision examples](../../src/kiyo/governance/decision-examples.md),
  covering all 15 requested cases plus provider/read-only/host-denial variants.
  Every example is synthetic expected behavior, execution NOT_RUN.
- Added nine governance control IDs (31 total), conditional Core reference and
  shared Governance Review procedure, with source README/architecture/build-state
  updates. No policy engine, hook, runtime, native settings or populated policy
  pack was created; no dangerous operation was executed.

Coverage: partial governance instruction implementation for
REQ-007/011–013/027/030/035/040/041/046–055; REQ-059 receives dependency-policy
input only, with release/supply-chain implementation still pending.
REQ-080 continuity updated. Current totals: 48 PARTIALLY_IMPLEMENTED and
32 NOT_IMPLEMENTED; all 80 full verifications remain NOT_RUN.
All six native targets remain NOT_TESTED.

Checks: [Prompt 06 evidence](BASELINE.md#prompt-06-checks).
Memory Impact: **NONE for project memory**; decisions/build continuity stay in
docs/build. No project policy/memory initialization or global settings change.

## Prompt 05 delivered scope

- Added [Memory specification](../../src/kiyo/framework/memory-specification.md)
  and [shared lifecycle](../../src/kiyo/workflows/memory-lifecycle.md).
- Added eight neutral [Memory templates](../../src/kiyo/framework/memory-specification.md#template-catalog):
  project.md, architecture.md, conventions.md, decisions.md, domain.md,
  integrations.md, known-issues.md and index.md under src/kiyo/templates/memory/.
- Defined entry IDs/types/status, actual evidence/scope/dates, conditional approval
  attribution, last_modified versus last_verified, and scoped Git context.
- Specified one canonical store, on-demand drift checks, approved-intent protection,
  authorized reread-before-write sync, no-delta no-op and four Memory Impact values.
  No watcher, database or consumer runtime; no populated project memory created.
- Added [20 scenario specifications](../../tests/behavioral/memory/scenarios.md)
  covering the lifecycle and edge cases, including Mapperly/AutoMapper decision
  conflict. All are synthetic specifications, execution NOT_RUN.
- Added KIYO-MEM-002–007 (22 controls total), linked conditional Memory loading,
  aligned the existing typo example to Memory Impact NONE, and updated source
  README, two architecture records and six build records.
  Bootstrap, native research, release identity and owner decisions are preserved.

Coverage: partial Memory/shared instruction implementation for
REQ-012–024/027/040/044/049/062/075; REQ-068/074 receive scenario/procedure inputs
only, without public-skill implementation. REQ-080 continuity updated. Full
requirement verification remains NOT_RUN; live native targets remain NOT_TESTED.
Current totals: 41 PARTIALLY_IMPLEMENTED and 39 NOT_IMPLEMENTED.

Checks: [Prompt 05 evidence](BASELINE.md#prompt-05-checks).
Memory Impact: **NONE for project memory**; this build's decisions/continuity are
recorded in existing docs/build. No canonical project-memory store is initialized.

## Prompt 04 delivered scope

- Added [KIYO.md](../../src/kiyo/KIYO.md) and shared
  [bootstrap](../../src/kiyo/framework/bootstrap.md),
  [trust/authority](../../src/kiyo/framework/trust-and-authority.md),
  [context loading](../../src/kiyo/framework/context-loading.md),
  [activation contract](../../src/kiyo/framework/activation-contract.md),
  [control index](../../src/kiyo/framework/control-index.md) and
  [expected responses](../../src/kiyo/framework/response-examples.md).
- Authored ten baseline principles and 16 stable control IDs. Separated Facts,
  Assumptions, Proposals, Approved decisions and Unknowns; bounded production,
  identity, policy authority, read-only scope and actual check claims.
- Provided all five requested scenarios plus approved-intent conflict and
  local-evidence/unrun-check examples. All seven are synthetic expected behavior,
  not executed evaluations or host evidence.
- Added [ADR-002](../architecture/decisions/ADR-002-core-loading-budgets.md):
  mandatory KIYO.md + bootstrap.md together <=120 physical lines / 600 words;
  future SKILL.md <=250 lines / 1,200 words. These are Kiyo design criteria.
- Updated three architecture contracts (layout, loading, naming), source README
  and six build records. No skill, native manifest, runtime, hook, project state
  or release identity was created.

Coverage: partial shared Core instructions for REQ-007–017/019/020/022–024/
027/028/030/032–034/040/041/044/049/051/052/054/058/062/077;
REQ-080 build continuity updated. This is authored product text, not verified
agent behavior or complete later skills/memory/governance/security procedures.
Full requirement verification remains NOT_RUN; all six live targets NOT_TESTED.
Current totals: 38 PARTIALLY_IMPLEMENTED and 42 NOT_IMPLEMENTED. Static instruction
checks do not promote any full acceptance or behavioral result.

Checks: [Prompt 04 evidence](BASELINE.md#prompt-04-checks).
Memory Impact: build continuity/ADR only; no project memory created or changed.
Native research remains checked 2026-09-28; no new host/schema claim is made.

## Prompt 03 delivered scope

- Selected one canonical `src/kiyo/` specification, three ecosystem overlay areas,
  six independent target records, project-owned state and developer-only tooling.
- Defined bootstrap-before-workflow actions, relevant-reference loading, authoring
  budgets and native project-adapter ownership without claiming automatic execution.
- Selected generated shared snapshots within each skill, explicit relative-reference
  transforms and parity/relocation gates. No consumer generator or runtime.
- Preserved established memory/policy paths; new-project defaults are `.kiyo/memory/`
  and `.kiyo/policy.md`. Project state never belongs in plugin cache.
- Recorded stable control IDs, internal eight-skill names, future release-version
  discipline and unresolved publication/native support decisions.
- Created [layout](../architecture/framework-layout.md),
  [loading](../architecture/content-loading.md),
  [packaging](../architecture/packaging-contract.md),
  [naming/versioning](../architecture/naming-and-versioning.md),
  [ADR-001](../architecture/decisions/ADR-001-static-canonical-packages.md) and
  [source authoring scaffold](../../src/kiyo/README.md).
- Updated six build records. No Core, skill, manifest, generator or runtime was
  implemented; later paths are explicitly planned, not empty feature placeholders.

Design coverage: REQ-001/002/003/005/006/007/009/010/011/014/017/024/025/026/027/
037/054/067/076/077/078/079/080. Architecture evidence is linked in traceability;
it does not promote product acceptance. Existing seven partial documentation
implementation rows remain partial; 73 other rows remain NOT_IMPLEMENTED and all
80 full verifications remain NOT_RUN.

Checks: [Prompt 03 evidence](BASELINE.md#prompt-03-checks).
Memory Impact: build records/ADR only; no product memory initialized or changed.
Prompt 02 source checks remain dated 2026-09-28; this prompt did not revalidate
external schemas or test hosts. All six live targets remain NOT_TESTED.

## Prompt 02 delivered scope

- Retrieved official sources and recorded requested/final URLs, checked dates,
  limitations, recovered retrieval failures and source conflicts.
- Researched all 11 requested dimensions independently for six targets; native
  Codex IDE plugins are UNSUPPORTED in current documentation, while standalone
  IDE skills are documented. All six live states remain NOT_TESTED.
- Separated metadata discovery, explicit/implicit skill use and persistent core
  guidance; recorded self-contained resource options and unresolved contracts.
- Established concept-level standards baseline, including ISO 12207:2026,
  SSDF 1.1 final versus 1.2 draft, and AST v1 public-review maturity.
- Created [SOURCES](../research/SOURCES.md),
  [standards baseline](../research/standards-baseline.md),
  [capabilities](../compatibility/platform-capabilities.md),
  [invocation map](../compatibility/native-invocation-map.md), and
  [activation modes](../compatibility/activation-modes.md).
- Updated this file, TRACEABILITY, OPEN-ISSUES, HANDOFF, BASELINE and DECISIONS.
  REQUIREMENTS, BUILD-CONTRACT and LICENSE are preserved.

Coverage: REQ-004/005/010/056/057/067 have partial documentation implementation;
REQ-080 build continuity remains partial. Research inputs also cover
REQ-002/003/006/007/009/011/058–066/076–079 without claiming their product
implementation. Full requirement verifications remain NOT_RUN.

Checks: [Prompt 02 evidence](BASELINE.md#prompt-02-checks).
Memory Impact: build records only; no .kiyo/memory or competing memory created.

## Prompt 01 delivered scope

- Inspected repository root, branch, history tip, clean working tree and existing
  LICENSE before writing.
- Created the eight requested Markdown build records.
- Registered the original REQ-001–REQ-080 with objective, scope, observable
  acceptance criteria, dependencies, proposed implementation areas and planned
  verification.
- Created one traceability row per requirement, with planned test identifiers
  clearly distinguished from implemented tests and execution evidence.
- Recorded existing MIT license facts separately from owner publication decisions.
- Recorded six independent targets with UNKNOWN capability facts and NOT_TESTED
  live results.
- Kept the framework implementation, runtime components and later prompts outside
  this step. REQ-080 is partially implemented by build continuity records;
  registration alone does not implement REQ-001–REQ-079.

Files changed: [BUILD-CONTRACT](BUILD-CONTRACT.md),
[REQUIREMENTS](REQUIREMENTS.md), [TRACEABILITY](TRACEABILITY.md),
[PROGRESS](PROGRESS.md), [DECISIONS](DECISIONS.md),
[OPEN-ISSUES](OPEN-ISSUES.md), [HANDOFF](HANDOFF.md),
[BASELINE](BASELINE.md).

Checks: see [BASELINE.md](BASELINE.md#prompt-01-checks). Product static validation,
behavioral evaluation and live tests are not claimed by these documentation checks.

Memory Impact: build handoff only; no .kiyo/memory created or changed.

## Thirty-step roadmap

Later steps are planned, not authorized for automatic execution. DONE on a prompt
means that prompt's scope is complete, not that all product requirements are met.

| Prompt | Scope | Task / planning status | Evidence / dependency |
| --- | --- | --- | --- |
| 01 | Scope | DONE | P01-C01–C07 PASS; see BASELINE for scope and evidence |
| 02 | Research | DONE | P02-C01–C07 PASS; research only, all live targets NOT_TESTED |
| 03 | Architecture | DONE | P03 documentation/design checks PASS; product/runtime/host verification not claimed |
| 04 | Core | DONE | P04-C01–C07 PASS; static Core/documentation only, expected cases not executed |
| 05 | Memory | DONE | P05-C01–C07 PASS; static specification/template checks, scenarios NOT_RUN |
| 06 | Governance | DONE | P06-C01–C07 PASS; static policies/documentation only, decision examples NOT_RUN |
| 07 | Security | DONE | P07-C01–C07 PASS; static controls/procedures/templates only, scenarios NOT_RUN |
| 08 | Router/Flow | DONE | P08-C01–C07 PASS; static procedures/truth-table checks only, behavioral execution NOT_RUN |
| 09 | Engineering/Profiles | DONE | P09-C01–C07 PASS; static standards/profiles/mapping only, scenarios NOT_RUN |
| 10 | Verification/DoD | DONE | P10-C01–C07 PASS; static contracts/templates/examples only; behavioral execution NOT_RUN |
| 11 | Init | DONE | P11-C01–C07 PASS; entry/resource/closure checks and bounded source trials separately recorded; native NOT_TESTED |
| 12 | Requirement | DONE | P12-C01–C07 PASS; static/resource checks and bounded source trials; native NOT_TESTED |
| 13 | Implement | DONE | P13-C01–C07 PASS; source/resource checks and bounded fixture trials; native NOT_TESTED |
| 14 | Review | DONE | P14-C01–C07 PASS; static/resource checks and bounded read-only source trials; native NOT_TESTED |
| 15 | Test | DONE | P15-C01–C07 PASS; static/resource checks and bounded mode-specific source trials; native NOT_TESTED |
| 16 | Security Skill | DONE | P16-C01–C07 PASS; static/resource checks and bounded read-only submode trials; native NOT_TESTED |
| 17 | Architecture Skill | DONE | P17-C01–C07 PASS; static/resource checks and bounded read-only source trials; native NOT_TESTED |
| 18 | Memory Skill | DONE | P18-C01–C07 PASS; static/resource/inventory checks and bounded mode/no-op/concurrency trials; native NOT_TESTED |
| 19 | Organization Policies | DONE | P19-C01–C07 PASS; static/resource checks and bounded read-only policy trials; native NOT_TESTED |
| 20 | Claude | DONE | P20-C01–C07 PASS; offline package/parity/relocation checks; native validator NOT_RUN, both Claude targets NOT_TESTED |
| 21 | Codex | DONE | P21-C01–C07 scoped offline checks PASS; C08 ingestion FAIL for missing owner release fields; native NOT_TESTED, IDE plugins UNSUPPORTED |
| 22 | Copilot | DONE | P22-C01–C07 scoped offline/document checks PASS; 794-file shared bundle, 20 cases NOT_RUN per target; both native NOT_TESTED |
| 23 | Packaging/Parity | DONE | P23-C01–C07 scoped checks; equal builds, 456 parity records; extra filesystem-symlink probe BLOCKED; native NOT_TESTED |
| 24 | Static Tests | DONE | P24 selected contract groups and exact-reason negatives: 37 PASS; actual extraction; static only |
| 25 | Behavioral Tests | DONE | User selected offline: 48 host cases NOT_RUN; 13 helper checks PASS; no behavioral metrics |
| 26 | Live Host Tests | DONE | Selected no-quota subset: Claude native discovery/validation; Codex disposable install/cache/uninstall; full six-target acceptance partial |
| 27 | Documentation | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 28 | Release Tooling | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 29 | Gap Audit | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 30 | Final Acceptance | NOT_STARTED | Await its user prompt and preceding relevant artifacts |

NOT_STARTED is a roadmap planning marker, not an additional task-result status.

## Continuation boundary

DEC-001 name, DEC-002 release license, DEC-003 publisher/destination and DEC-004
Codex IDE treatment remain open. No release version, signature or approval invented.

Safe to continue: **YES for a user-requested Prompt 27 Documentation**.
Use the actual scoped results and retain NOT_TESTED/UNSUPPORTED gaps; do not claim
complete compatibility or release readiness. No later model/quota/publication
authority follows from P26.
Next prompt: **27 Documentation**, only when requested by the user.

