# Kiyo Compass — Progress

Snapshot: 2026-09-28. Current prompt: **02 Research**.
Task status: **DONE** for Prompt 02 research; documentation checks passed.
Product status: research documentation implemented; no native payload or skills.

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
| 03 | Architecture | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
| 04 | Core | NOT_STARTED | Await its user prompt and preceding relevant artifacts |
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

Safe to continue: **YES for requested Prompt 03 Architecture**. Research and
documentation checks are complete; design may use documented capabilities while
leaving unsupported or unknown schema-dependent paths gated.
No release or host-acceptance readiness is implied.
Next prompt: **03 Architecture**, only when requested by the user.

