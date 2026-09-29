# Skill guide

Checked **2026-09-29** against the eight canonical entries and generated packages.
These are authored behavior contracts, not observed native agent results.
Select through the [host-specific UI/syntax](README.md#select-a-skill), then give
the task and scope. All examples here are **illustrative/synthetic, NOT_RUN**.

| Skill / trigger | Input | Expected output | Write / execution boundary |
| --- | --- | --- | --- |
| [Init](../../src/kiyo/skills/init/SKILL.md): onboard, initial analysis, create Memory, inspect readiness | Root/module, explicit onboarding intent, optional preferences | Evidence-backed summary, unknowns, local changes/proposals, activation readiness | Preview reads only; initialize may write authorized Memory/config/managed bootstrap; no source/tests/dependencies/global settings |
| [Requirement](../../src/kiyo/skills/requirement/SKILL.md): turn a raw request/issue into an engineering requirement | Request/document/proposed change plus authorized context | ID, objective/problem/behavior, scope/exclusions, rules/AC, validation, dependencies, security/data, constraints, decisions and evidence | Chat default; only a requested specification path may be written; no source/tests/config/Memory or project-script execution |
| [Implement](../../src/kiyo/skills/implement/SKILL.md): feature, bug fix, explicitly scoped refactor | Change intent, behavior/AC and boundaries | Scoped diff, actual verification, review, Memory Impact and remaining work | Authorized code/tests/docs changes and preflighted checks; no implicit commit/push/PR/deploy, production DB or policy rewrite |
| [Review](../../src/kiyo/skills/review/SKILL.md): assess human/AI changes | Staged/unstaged diff, files, explicit commit range or accessible PR | Findings with severity/confidence, exact location, impact, control/requirement, fix idea and verification idea | Read-only, chat default; no source/tests/Memory writes, installs or automatic build/test execution |
| [Test](../../src/kiyo/skills/test/SKILL.md): gaps, checks or test authoring | Requirement/change/tests plus selected effects | Plan/gaps or actual check results or test diff, with limits | assess/run/write have distinct boundaries below |
| [Security](../../src/kiyo/skills/security/SKILL.md): bounded application/Skill/policy/resource assessment | Supplied target and permitted inspection scope | Evidence, impact/confidence, mitigation, owner and coverage gaps | Read-only; no global scan, credentials, external probes, suspicious execution, scanner install or auto-fix |
| [Architecture](../../src/kiyo/skills/architecture/SKILL.md): design question, impact or drift | Module/boundary, proposed change or approved decision | Observed structure, approved intent, proposals, unknown deployment behavior and inspection limits | Read-only; no refactor/migration, policy/ADR/Memory updates or automatic build/test |
| [Memory](../../src/kiyo/skills/memory/SKILL.md): show/check/sync/repair selected context | Canonical store, entries, repository/worktree/module and requested mode | Bounded summary, factual delta, conflict or repair report | show/check write zero files; sync/repair only authorized affected entries, no project source/policy changes |

Read-only permits necessary authorized inspection, not arbitrary commands.
A separate requested report-file output is its own write scope. Read-only
inspection never authorizes modifying the assessed code or Memory.

## Modes and example inputs

| Skill | Mode / intent | Illustrative user input and expected boundary |
| --- | --- | --- |
| Init | preview / initialize | “Preview onboarding only.” Then, separately: “Create the proposed local Memory/config; preserve existing instructions.” No application scaffolding |
| Requirement | drafting / readiness | “เพิ่ม export Excel; identify missing fields and permissions before implementation.” Discover existing constraints; ask material remaining decisions; do not invent HTTP behavior |
| Implement | feature / bug / scoped refactor | “Fix the supplied boundary error and add its regression test; preserve unrelated edits.” Minimal change with actual checks |
| Review | supplied change review | “Review my unstaged changes; do not edit or run project scripts.” Report an obvious bug without fixing it |
| Test | assess | “Assess authorization test gaps in this module; no writes or execution.” Read tests as source |
| Test | run | “Run the existing approved unit suite after inspecting its script and environment.” Authorized artifacts allowed; no tracked source/test changes or repair |
| Test | write | “Add tests for these agreed cases in the existing framework.” Only tests/test-only fixtures; writing alone does not authorize running them |
| Security | application | “Assess this supplied handler for validation and authorization risks.” Bounded code inspection |
| Security | skills | “Review this supplied Skill package against AST01–AST10 without executing it.” No install or global inventory |
| Security | governance | “Check this selected policy for missing authority and conflicts.” No policy edits |
| Security | self-check | “Report exposed Kiyo identity, readable resources and activation evidence.” No integrity/sandbox guarantee |
| Architecture | analysis / impact / drift | “Compare ADR-007 with this module; report deviations only.” Approved intent does not get rewritten |
| Memory | show | “Summarize the selected entries with stored freshness and unknowns.” No new verification claim |
| Memory | check | “Compare these observations and decisions with this branch.” Report drift; no writes |
| Memory | sync | “Apply only these evidence-backed observation corrections.” Reread current entries; preserve decisions and human edits |
| Memory | repair | “Repair these moved-file links where their targets are established.” Hold ambiguous merges; preserve history |

An explicit Test selection with a request to redesign authentication is a workflow
mismatch. Explain it and establish implementation scope before changing effects.
Adding a security checklist to Implement does not create another Skill or agent.

Requirement separates **Existing facts, User requirements, AI proposals and
Unresolved decisions**. Its readiness is READY_FOR_IMPLEMENTATION,
DECISION_REQUIRED or INSUFFICIENT_EVIDENCE. Delivering a draft can complete the
drafting task; READY is not permission to begin coding.

All Skills share [Core](../../src/kiyo/KIYO.md), relevant
[workflows](../../src/kiyo/workflows/workflow-router.md) and
[Definition of Done](../../src/kiyo/framework/definition-of-done.md).
Tiny tasks stay compact. Mandatory safety, approval and evidence checks remain.
