# Kiyo Compass — Progress

Snapshot: 2026-09-29. Current prompt: **06 Governance**.
Task status: **DONE** for Prompt 06; scoped static governance/documentation checks passed.
Product status: shared Core/Memory and Markdown governance policies authored;
native packages/public skills remain unimplemented. A policy engine is outside the product boundary.

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
| 07 | Security | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 08 | Router/Flow | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 09 | Engineering/Profiles | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 10 | Verification/DoD | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 11 | Init | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 12 | Requirement | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 13 | Implement | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 14 | Review | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 15 | Test | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 16 | Security Skill | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 17 | Architecture Skill | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 18 | Memory Skill | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 19 | Organization Policies | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 20 | Claude | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 21 | Codex | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 22 | Copilot | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 23 | Packaging/Parity | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 24 | Static Tests | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 25 | Behavioral Tests | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 26 | Live Host Tests | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 27 | Documentation | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 28 | Release Tooling | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 29 | Gap Audit | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 30 | Final Acceptance | NOT_STARTED | Await its user prompt and preceding relevant artifacts |

NOT_STARTED is a roadmap planning marker, not an additional task-result status.

## Continuation boundary

Outstanding owner decisions: DEC-001 final name, DEC-002 release license,
DEC-003 publisher/destination and DEC-004 treatment of Codex IDE's native-plugin
gap before compatibility/release claims. See OPEN-ISSUES for technical gaps.

Safe to continue: **YES for a user-requested Prompt 07 Security**. Core, Memory
and governance references are ready for that scope; owner/native support
decisions do not block it. This does not authorize later work or dangerous execution.
Next prompt: **07 Security**, only when requested by the user.

