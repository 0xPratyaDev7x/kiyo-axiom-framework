# Kiyo Compass — Progress

Snapshot: 2026-09-29. Current prompt: **04 Core**.
Task status: **DONE** for Prompt 04 Core; scoped static/documentation checks passed.
Product status: shared Markdown Core authored; native packages/skills not implemented.

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
| 05 | Memory | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 06 | Governance | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
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

Safe to continue: **YES for requested Prompt 05 Memory**. Shared Core and scoped
checks are complete; Memory can build on its authority/context rules. Owner/native
support decisions remain open but do not block this scope. No later work is
authorized by the handoff alone.
Next prompt: **05 Memory**, only when requested by the user.

