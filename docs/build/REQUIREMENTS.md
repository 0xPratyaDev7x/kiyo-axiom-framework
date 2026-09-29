# Kiyo Axiom Framework — Requirement Registry

Kiyo Axiom Framework is a working name containing Kiyo, not an approved publication identity.
This registry captures the user's Prompt 01 requirements without changing their IDs
or source wording. English expansions make the intended scope and observable
acceptance criteria explicit; the original Thai requirement remains authoritative
for its intent. These are requirements, not claims of implemented capability.

Four pillars: **Project Intelligence**, **Software Engineering**, **AI Governance**,
and **Agentic Skill Security**.

Exactly eight public skills are planned: **Init, Requirement, Implement, Review,
Test, Security, Architecture, Memory**. Workflow Router, Governance Review,
Skill Audit and Self-check are shared procedures or submodes.

## Reading this registry

- Each AC-NNN is the observable acceptance criterion for REQ-NNN; all clauses
  must be satisfied within the requirement's stated scope.
- Dependencies express related design/evidence needs, not a strict implementation
  ordering. Architecture and research may refine proposed locations without
  changing requirement IDs or silently weakening acceptance criteria.
- Planned implementation areas are proposals only. Except for the eight build
  records created in Prompt 01, the named future files/directories do not yet exist.
- TC-REQ-NNN identifiers in [TRACEABILITY.md](TRACEABILITY.md) are reserved planned
  test cases, not existing tests or execution evidence. Behavioral evaluation and
  live-host results must remain separate from static documentation checks.
- “All six targets” means Claude Code CLI, Claude Code VS Code Extension, Codex CLI,
  Codex IDE Extension, GitHub Copilot CLI and GitHub Copilot in VS Code. No support
  or version is inferred from this target list.
- Standard editions, AST taxonomy provenance, native schemas and invocation syntax
  require later source verification. No external research or standards alignment
  is claimed in this scope-only prompt.
- Implementation and verification state lives in [TRACEABILITY.md](TRACEABILITY.md);
  the Prompt 01 baseline and actual checks live in [BASELINE.md](BASELINE.md).

## REQ-001

**Source requirement:** REQ-001: Branding มี Kiyo; Kiyo Axiom Framework เป็น working name; ไม่เดาความพร้อมของชื่อใน Marketplace

- **Objective:** Preserve Kiyo branding without inventing a release identity.
- **Scope:** Working name, release name, marketplace availability, license and publisher decisions.
- **Observable acceptance criteria (AC-001):** Drafts label Kiyo Axiom Framework as a working name and retain Kiyo branding; release identity and marketplace availability stay unconfirmed until owner decisions and evidence exist; existing LICENSE is preserved.
- **Dependencies:** Owner decisions DEC-001, DEC-002, DEC-003; marketplace research.
- **Planned implementation area:** docs/branding.md; platform manifests (future)
- **Planned verification:** TC-REQ-001 (PLANNED): Inspect draft labels and manifests; verify every availability claim has dated evidence and every release identity has explicit owner approval.

## REQ-002

**Source requirement:** REQ-002: File-based Markdown-first พร้อม native static manifests/frontmatter

- **Objective:** Keep the deliverable usable as static files.
- **Scope:** Markdown content and only native-required static manifests, YAML frontmatter, JSON or TOML.
- **Observable acceptance criteria (AC-002):** Package inventory contains Markdown plus justified host-native static metadata/assets; an end user can consume the instructions without running a Kiyo executable.
- **Dependencies:** REQ-003, REQ-006; host schema research.
- **Planned implementation area:** core/; skills/; platforms/ (future)
- **Planned verification:** TC-REQ-002 (PLANNED): Inspect package file types and metadata justifications; exercise native loading per target when packages exist.

## REQ-003

**Source requirement:** REQ-003: ไม่มี runtime engine/server/database/daemon/telemetry/MCP/runtime hooks/Kiyo installer

- **Objective:** Exclude a Kiyo runtime and unrelated applications.
- **Scope:** Runtime engine, servers, databases, daemons, background/network services, telemetry, MCP, runtime hooks, central CLI/installer, Virtual Office, agent-team orchestration and project-management dashboards.
- **Observable acceptance criteria (AC-003):** Repository and payload review finds none of the prohibited product components or user runtime dependencies; developer validate/package/test/release scripts remain outside payloads and are not end-user prerequisites.
- **Dependencies:** REQ-002, REQ-079.
- **Planned implementation area:** docs/architecture.md; packaging policy (future)
- **Planned verification:** TC-REQ-003 (PLANNED): Inspect files, dependency lists, entry points and package contents; distinguish developer tools from installed payload.

## REQ-004

**Source requirement:** REQ-004: ติดตั้งผ่าน native plugin/marketplace ของแต่ละ ecosystem

- **Objective:** Use each ecosystem's native distribution path.
- **Scope:** Native plugin/marketplace installation; no central Kiyo installer.
- **Observable acceptance criteria (AC-004):** Each ecosystem has evidence-backed native installation instructions and a package overlay where supported; unsupported or unverified paths are recorded as gaps rather than claimed supported.
- **Dependencies:** REQ-005, REQ-006; native distribution research.
- **Planned implementation area:** platforms/; docs/installation.md (future)
- **Planned verification:** TC-REQ-004 (PLANNED): Review official host documentation and separately exercise documented install paths; record unavailable hosts as NOT_TESTED.

## REQ-005

**Source requirement:** REQ-005: Compatibility matrix แยกหก CLI/IDE targets

- **Objective:** Track compatibility independently for six targets.
- **Scope:** Claude Code CLI, Claude Code VS Code Extension, Codex CLI, Codex IDE Extension, GitHub Copilot CLI, GitHub Copilot in VS Code.
- **Observable acceptance criteria (AC-005):** A matrix contains six distinct rows with capability sources, tested versions when observed, checks, evidence and gaps; CLI results never mark an IDE row passed.
- **Dependencies:** REQ-004, REQ-077; six-target environment access.
- **Planned implementation area:** docs/compatibility.md; tests/live/ (future)
- **Planned verification:** TC-REQ-005 (PLANNED): Check row identity and completeness; compare each reported result to evidence from that exact target.

## REQ-006

**Source requirement:** REQ-006: Canonical specification ชุดเดียวและ self-contained platform packages

- **Objective:** Maintain one canonical specification with portable packages.
- **Scope:** Canonical Markdown specification and minimum native packaging overlays.
- **Observable acceptance criteria (AC-006):** Each platform package includes all required internal content, resolves references without the source checkout, and traces copied material to the single canonical specification; overlays contain only justified host differences.
- **Dependencies:** REQ-002, REQ-005, REQ-079.
- **Planned implementation area:** core/; skills/; platforms/; packaging configuration (future)
- **Planned verification:** TC-REQ-006 (PLANNED): Unpack each package into an isolated directory, validate links and compare canonical content against generated copies.

## REQ-007

**Source requirement:** REQ-007: แยก advisory controls กับ host enforcement; ไม่อ้าง guarantee/certification

- **Objective:** State the limits of advisory controls honestly.
- **Scope:** Kiyo guidance versus host tools, permissions, enforcement and certification.
- **Observable acceptance criteria (AC-007):** Core guidance and user documentation assign actual tool use to the host agent and permission enforcement to the host; they contain no Kiyo enforcement, security guarantee or certification claims.
- **Dependencies:** REQ-011, REQ-051.
- **Planned implementation area:** core/authority.md; docs/limitations.md (future)
- **Planned verification:** TC-REQ-007 (PLANNED): Review control wording and evaluate a host restriction scenario; guidance must not represent itself as overriding permissions.

## REQ-008

**Source requirement:** REQ-008: แก้ guessing, over-changing, overclaiming, wrong workflow, lost context และ stale context

- **Objective:** Address the six named agent failure patterns.
- **Scope:** Guessing, over-changing, overclaiming, wrong workflow, lost context and stale context.
- **Observable acceptance criteria (AC-008):** Procedures specify a concrete preventive or recovery step for each pattern; six corresponding scenarios show evidence-seeking, scoped changes, truthful reporting, intent preservation and context recovery/revalidation.
- **Dependencies:** REQ-014, REQ-016, REQ-028, REQ-034, REQ-040.
- **Planned implementation area:** core/; tests/behavioral/ (future)
- **Planned verification:** TC-REQ-008 (PLANNED): Map each failure pattern to a procedure and execute a behavioral scenario with an expected observable response.

## REQ-009

**Source requirement:** REQ-009: Compact bootstrap; automatic activation เฉพาะที่ host รองรับและตรวจได้

- **Objective:** Provide a compact bootstrap using only verified activation mechanisms.
- **Scope:** Initial context loading and host-supported automatic activation.
- **Observable acceptance criteria (AC-009):** Bootstrap directs progressive loading within a documented context budget; every automatic activation claim has host-specific source and test evidence, with explicit invocation fallback or an explicit gap otherwise.
- **Dependencies:** REQ-005, REQ-014; activation research.
- **Planned implementation area:** core/bootstrap.md; platforms/ (future)
- **Planned verification:** TC-REQ-009 (PLANNED): Measure bootstrap content against the chosen budget and test activation independently on each target; record unverified activation as UNKNOWN.

## REQ-010

**Source requirement:** REQ-010: Explicit skill invocation แยกจาก inferred activation; syntax ตาม native host

- **Objective:** Distinguish explicit invocation from inferred activation.
- **Scope:** Host-native public skill syntax and activation reporting.
- **Observable acceptance criteria (AC-010):** Each target documents verified explicit invocation syntax separately from inferred activation; examples do not invent universal commands or imply inference is guaranteed.
- **Dependencies:** REQ-005, REQ-009, REQ-026.
- **Planned implementation area:** platforms/; docs/invocation.md (future)
- **Planned verification:** TC-REQ-010 (PLANNED): Check examples against native documentation and invocation evidence; evaluate an ambiguous request without treating inference as explicit user invocation.

## REQ-011

**Source requirement:** REQ-011: เคารพ native instruction hierarchy และตรวจที่มาของ policy authority

- **Objective:** Respect host instruction authority.
- **Scope:** Native instruction hierarchy and policy provenance.
- **Observable acceptance criteria (AC-011):** Procedures identify the source and applicable authority of a policy, preserve higher-priority host instructions and stop or surface unresolved conflicts without treating repository text as system authority.
- **Dependencies:** REQ-012; native hierarchy research.
- **Planned implementation area:** core/authority.md (future)
- **Planned verification:** TC-REQ-011 (PLANNED): Evaluate conflicting host, user and repository policy fixtures and inspect the recorded authority rationale.

## REQ-012

**Source requirement:** REQ-012: Trust boundaries ครอบคลุม README/web/issues/code/tool output และ poisoned memory

- **Objective:** Keep untrusted content within data boundaries.
- **Scope:** README, web pages, issues, code, tool output and poisoned memory.
- **Observable acceptance criteria (AC-012):** Guidance explicitly treats instructions embedded in each listed input as untrusted data unless authorized through the native hierarchy; injection scenarios cannot silently authorize new actions or policy changes.
- **Dependencies:** REQ-011, REQ-062.
- **Planned implementation area:** core/trust-boundaries.md; tests/behavioral/ (future)
- **Planned verification:** TC-REQ-012 (PLANNED): Run one injection scenario for each listed input class, including memory poisoning, and inspect authority and action boundaries.

## REQ-013

**Source requirement:** REQ-013: Host/model/provider/account context ต้องมีหลักฐาน; ไม่ทราบระบุ UNKNOWN

- **Objective:** Report execution context from evidence.
- **Scope:** Host, model, provider and account context; privacy-safe reporting.
- **Observable acceptance criteria (AC-013):** Context records distinguish observed values from unknowns, link permissible evidence and use UNKNOWN for unavailable details; no account tier or model identity is inferred from appearance or branding.
- **Dependencies:** REQ-011, REQ-046, REQ-055.
- **Planned implementation area:** core/context.md; templates/context.md (future)
- **Planned verification:** TC-REQ-013 (PLANNED): Evaluate partially known context and confirm unknown fields stay UNKNOWN without reading secrets or inventing identity.

## REQ-014

**Source requirement:** REQ-014: Progressive loading และ context budget ไม่โหลดทุกไฟล์ทุกงาน

- **Objective:** Load only task-relevant context.
- **Scope:** Progressive disclosure, context budgets and handoff.
- **Observable acceptance criteria (AC-014):** Bootstrap defines staged reading and a context-budget strategy; a scoped task loads required instructions and relevant material rather than all framework/repository files; near-limit handoff preserves next actions.
- **Dependencies:** REQ-009, REQ-016, REQ-080.
- **Planned implementation area:** core/bootstrap.md; core/context.md (future)
- **Planned verification:** TC-REQ-014 (PLANNED): Inspect loading rules and evaluate a large repository with irrelevant files and a reduced context budget.

## REQ-015

**Source requirement:** REQ-015: รักษา repository baseline และ user edits; ไม่มี destructive cleanup

- **Objective:** Preserve the repository and existing user work.
- **Scope:** Root, branch, tracked/untracked and staged/unstaged baseline; destructive cleanup.
- **Observable acceptance criteria (AC-015):** Before edits the procedure records the permitted baseline; a dirty-worktree scenario preserves existing user changes and does not reset, clean, stash or revert them without scoped authorization.
- **Dependencies:** REQ-011, REQ-034.
- **Planned implementation area:** core/repository-safety.md; skills/init/ (future)
- **Planned verification:** TC-REQ-015 (PLANNED): Use a fixture with staged, unstaged and untracked user changes; compare their contents before and after the scoped task.

## REQ-016

**Source requirement:** REQ-016: Memory First ภายในขอบเขตที่อ่านได้ และตรวจ relevant repository facts ก่อนใช้

- **Objective:** Use relevant memory only after checking current facts.
- **Scope:** Authorized memory reads, repository inspection and Memory First.
- **Observable acceptance criteria (AC-016):** Tasks consult available relevant memory within read permissions, verify material claims against current repository evidence and identify stale or inaccessible knowledge rather than following it blindly.
- **Dependencies:** REQ-012, REQ-017, REQ-020.
- **Planned implementation area:** core/memory.md (future)
- **Planned verification:** TC-REQ-016 (PLANNED): Evaluate fresh, stale and unreadable memory fixtures; verify repository contradictions and access limits are reported.

## REQ-017

**Source requirement:** REQ-017: Canonical memory path; ค่าเริ่มต้น .kiyo/memory; ไม่สร้างสองแหล่งความจริง

- **Objective:** Keep one canonical project memory location.
- **Scope:** Default .kiyo/memory and explicitly configured alternatives.
- **Observable acceptance criteria (AC-017):** The procedure resolves one canonical path, defaults to .kiyo/memory when unconfigured and reports conflicting stores instead of silently creating a second truth source; approved path changes preserve existing knowledge.
- **Dependencies:** REQ-016, REQ-024.
- **Planned implementation area:** core/memory.md; templates/memory/ (future)
- **Planned verification:** TC-REQ-017 (PLANNED): Evaluate default, configured and conflicting memory locations and verify writes target only the authorized canonical store.

## REQ-018

**Source requirement:** REQ-018: เก็บ durable knowledge ไม่ทำ endpoint/method inventories ซ้ำกับ code

- **Objective:** Keep memory focused on durable knowledge.
- **Scope:** Architecture, decisions, constraints and recurring context.
- **Observable acceptance criteria (AC-018):** Memory guidance and templates retain useful durable knowledge with evidence and exclude exhaustive endpoint/method inventories that duplicate code; relevant code references replace copied inventories.
- **Dependencies:** REQ-017, REQ-020.
- **Planned implementation area:** core/memory.md; templates/memory/ (future)
- **Planned verification:** TC-REQ-018 (PLANNED): Review sample memory against repository facts and a proposed redundant endpoint inventory; verify the inventory is declined or reduced to durable context.

## REQ-019

**Source requirement:** REQ-019: แยก observations/proposals/approved decisions และ current reality/intended design

- **Objective:** Separate facts from proposals and approved intent.
- **Scope:** Observation, proposal, approved decision, current reality and intended design.
- **Observable acceptance criteria (AC-019):** Memory entries label knowledge type and decision status; observations or proposals cannot become approved decisions without recorded authority, and divergent current code remains distinguishable from intended design.
- **Dependencies:** REQ-020, REQ-022, REQ-049.
- **Planned implementation area:** core/memory.md; templates/decisions.md (future)
- **Planned verification:** TC-REQ-019 (PLANNED): Evaluate conflicting code and proposed decisions; inspect labels and ensure no approval is invented.

## REQ-020

**Source requirement:** REQ-020: Memory มี evidence/provenance/status/review scope/date ที่ตรวจจริง

- **Objective:** Make memory evidence and review limits explicit.
- **Scope:** Provenance, evidence, status, actual review date and inspected scope.
- **Observable acceptance criteria (AC-020):** Memory templates require each listed field; populated entries cite observed evidence, use actual review dates and limit claims to inspected scope; unavailable evidence is marked unknown rather than fabricated.
- **Dependencies:** REQ-013, REQ-019.
- **Planned implementation area:** templates/memory/; core/memory.md (future)
- **Planned verification:** TC-REQ-020 (PLANNED): Validate populated sample entries and evaluate missing provenance and partial-inspection cases.

## REQ-021

**Source requirement:** REQ-021: ตรวจ Memory Drift เมื่อถูกเรียก ไม่อ้างตรวจ manual edits แบบ real-time

- **Objective:** Detect memory drift only when a check runs.
- **Scope:** Invoked memory checking and manual repository edits.
- **Observable acceptance criteria (AC-021):** An invoked check compares scoped memory claims with current files and reports differences; documentation makes no real-time monitoring claim and no watcher or background process is introduced.
- **Dependencies:** REQ-003, REQ-016, REQ-020.
- **Planned implementation area:** core/memory-drift.md; skills/memory/ (future)
- **Planned verification:** TC-REQ-021 (PLANNED): Modify a fixture after memory capture, run a check and inspect the drift report and its inspection scope.

## REQ-022

**Source requirement:** REQ-022: Architecture Drift ไม่แก้ approved decision ให้ตาม code โดยอัตโนมัติ

- **Objective:** Protect approved architecture decisions during drift review.
- **Scope:** Observed implementation versus approved architecture.
- **Observable acceptance criteria (AC-022):** A detected contradiction reports both evidence and approved intent; code drift never automatically rewrites an approved decision, and a proposed decision change requires applicable human approval.
- **Dependencies:** REQ-019, REQ-049, REQ-074.
- **Planned implementation area:** core/architecture-drift.md (future)
- **Planned verification:** TC-REQ-022 (PLANNED): Evaluate code violating an approved decision and compare decision content before and after the review.

## REQ-023

**Source requirement:** REQ-023: ประเมิน Memory Impact ก่อนจบ; sync เมื่อจำเป็นและมีสิทธิ์; no-change ไม่ touch ไฟล์

- **Objective:** Assess memory impact without unnecessary writes.
- **Scope:** Task closure, authorized synchronization and no-change behavior.
- **Observable acceptance criteria (AC-023):** Closure reports memory impact; writes occur only for necessary authorized changes, and a no-change outcome leaves memory contents and timestamps untouched.
- **Dependencies:** REQ-017, REQ-020, REQ-027.
- **Planned implementation area:** core/memory.md; core/definition-of-done.md (future)
- **Planned verification:** TC-REQ-023 (PLANNED): Evaluate changed, unchanged and unauthorized memory cases; compare content and modification timestamps.

## REQ-024

**Source requirement:** REQ-024: Memory รองรับ partial inspection, missing files, monorepo, branches, worktrees และ concurrent edits

- **Objective:** Handle repository layouts and competing edits safely.
- **Scope:** Partial inspection, missing files, monorepos, branches, worktrees and concurrent edits.
- **Observable acceptance criteria (AC-024):** Procedures scope memory to repository/worktree identity, record inspection gaps and handle missing files; before writing they detect changed inputs and reconcile or stop without overwriting concurrent human edits.
- **Dependencies:** REQ-015, REQ-017, REQ-020.
- **Planned implementation area:** core/memory.md; tests/behavioral/memory/ (future)
- **Planned verification:** TC-REQ-024 (PLANNED): Evaluate a fixture for each listed condition, including a concurrent change between inspection and write.

## REQ-025

**Source requirement:** REQ-025: Task classification/router เป็น Markdown procedures ไม่ใช่ runtime program

- **Objective:** Route tasks with readable procedures.
- **Scope:** Markdown task classification and workflow selection.
- **Observable acceptance criteria (AC-025):** A Markdown decision procedure maps user intent to the eight public skills or shared submodes, records ambiguities and contains no runtime router program or orchestration service.
- **Dependencies:** REQ-003, REQ-026, REQ-028.
- **Planned implementation area:** core/workflow-router.md (future)
- **Planned verification:** TC-REQ-025 (PLANNED): Review the procedure and evaluate representative intents, mixed tasks and ambiguous requests.

## REQ-026

**Source requirement:** REQ-026: มีแปด Public Skills; ไม่แตกคำสั่งซ้ำซ้อนโดยไม่จำเป็น

- **Objective:** Expose exactly eight public skills.
- **Scope:** Init, Requirement, Implement, Review, Test, Security, Architecture and Memory.
- **Observable acceptance criteria (AC-026):** Public catalogs and native overlays expose exactly those eight skills; Workflow Router, Governance Review, Skill Audit and Self-check remain shared procedures/submodes without a ninth public skill.
- **Dependencies:** REQ-006, REQ-025.
- **Planned implementation area:** skills/; core/; platforms/ (future)
- **Planned verification:** TC-REQ-026 (PLANNED): Count canonical public skills and compare native catalogs, distinguishing necessary host syntax aliases from extra public workflows.

## REQ-027

**Source requirement:** REQ-027: Skill มี read/write/execute contracts; read-only ไม่แก้ source/memory/report files เอง

- **Objective:** Define each skill's permitted effects.
- **Scope:** Read, write and execute contracts, including read-only operation.
- **Observable acceptance criteria (AC-027):** Every skill declares its access contract and mode transitions; a read-only run changes no source, memory or report files, and any mode requiring writes or execution respects scoped authorization.
- **Dependencies:** REQ-011, REQ-049, REQ-051.
- **Planned implementation area:** skills/; core/access-contracts.md (future)
- **Planned verification:** TC-REQ-027 (PLANNED): Review all eight contracts and compare full fixture snapshots during read-only scenarios, including report paths.

## REQ-028

**Source requirement:** REQ-028: Workflow mismatch ต้องเคารพ user intent; ไม่เปลี่ยน review เป็น implement เงียบ ๆ

- **Objective:** Keep workflow corrections aligned with user intent.
- **Scope:** Mismatch detection and scope changes.
- **Observable acceptance criteria (AC-028):** A review request remains a review; a mismatch is explained with an appropriate proposal or clarifying question, and implementation begins only when the user's authorized intent includes edits.
- **Dependencies:** REQ-025, REQ-027, REQ-049.
- **Planned implementation area:** core/workflow-router.md (future)
- **Planned verification:** TC-REQ-028 (PLANNED): Evaluate review requests containing fixable defects and check that source/memory/report files remain unchanged in read-only mode.

## REQ-029

**Source requirement:** REQ-029: Adaptive engineering flow พร้อม bounded repair loop

- **Objective:** Use adaptive engineering with a finite repair loop.
- **Scope:** Task flow, verification failures and escalation.
- **Observable acceptance criteria (AC-029):** Flow adjusts to task size and risk, declares a repair-attempt bound and stops with honest unresolved findings when exhausted; scope-changing repairs are reassessed before further edits.
- **Dependencies:** REQ-035, REQ-039, REQ-044.
- **Planned implementation area:** core/engineering-flow.md (future)
- **Planned verification:** TC-REQ-029 (PLANNED): Evaluate small work, a repairable failure and a persistent failure; verify the declared bound and final unresolved status.

## REQ-030

**Source requirement:** REQ-030: งานเล็กย่อกระบวนการได้แต่ไม่ข้าม safety/approval/evidence

- **Objective:** Scale ceremony without removing essential controls.
- **Scope:** Small tasks and reduced workflow.
- **Observable acceptance criteria (AC-030):** Small-task guidance permits a shorter plan/report while still checking authority, applicable approvals, risks, actual verification evidence and memory impact.
- **Dependencies:** REQ-029, REQ-040, REQ-049.
- **Planned implementation area:** core/engineering-flow.md (future)
- **Planned verification:** TC-REQ-030 (PLANNED): Evaluate a one-line change with an applicable approval boundary and verify the shortened flow still honors it.

## REQ-031

**Source requirement:** REQ-031: Requirement มี objective/behavior/scope/out-of-scope/rules/AC/constraints/dependencies/unknowns

- **Objective:** Capture actionable requirements before implementation.
- **Scope:** Objective, behavior, scope, out-of-scope, rules, acceptance criteria, constraints, dependencies and unknowns.
- **Observable acceptance criteria (AC-031):** Requirement output includes every listed field, with observable acceptance criteria and explicit unknowns; empty or inapplicable fields are explained rather than silently omitted.
- **Dependencies:** REQ-032, REQ-069.
- **Planned implementation area:** templates/requirement.md; skills/requirement/ (future)
- **Planned verification:** TC-REQ-031 (PLANNED): Validate representative requirement artifacts and evaluate an underspecified task without inventing behavior.

## REQ-032

**Source requirement:** REQ-032: Discover before asking; proposals ไม่ใช่ approved requirements; ไม่เดาข้อเท็จจริง

- **Objective:** Discover facts before asking only necessary questions.
- **Scope:** Evidence gathering, proposals and unresolved requirements.
- **Observable acceptance criteria (AC-032):** The procedure inspects available authorized facts before questioning; proposals remain labeled unapproved, unknowns remain explicit and questions target decisions that materially block the current scope.
- **Dependencies:** REQ-011, REQ-013, REQ-031.
- **Planned implementation area:** skills/requirement/; core/discovery.md (future)
- **Planned verification:** TC-REQ-032 (PLANNED): Evaluate a question already answerable from repository evidence and a genuinely blocking unknown; inspect proposal labels.

## REQ-033

**Source requirement:** REQ-033: ใช้ existing safe architecture/pattern ก่อนของใหม่; ไม่ลอก insecure legacy

- **Objective:** Prefer established safe designs.
- **Scope:** Existing architecture, patterns and unsafe legacy.
- **Observable acceptance criteria (AC-033):** Implementation rationale identifies applicable existing patterns; deviations are justified, and an insecure legacy pattern is flagged with a scoped safer proposal instead of copied unquestioningly.
- **Dependencies:** REQ-035, REQ-036, REQ-074.
- **Planned implementation area:** core/engineering.md; profiles/ (future)
- **Planned verification:** TC-REQ-033 (PLANNED): Evaluate a safe existing pattern and an insecure legacy example; inspect chosen approach and its justification.

## REQ-034

**Source requirement:** REQ-034: Minimal diff และ unrelated-change review; ไม่ revert งานผู้อื่น

- **Objective:** Keep changes minimal and preserve unrelated work.
- **Scope:** Diff scope and unrelated-change review.
- **Observable acceptance criteria (AC-034):** Final diff maps changes to authorized requirements, flags unrelated changes and preserves user edits; no cleanup or reversion of others' work is performed just to produce a clean diff.
- **Dependencies:** REQ-015, REQ-035.
- **Planned implementation area:** core/repository-safety.md; core/self-review.md (future)
- **Planned verification:** TC-REQ-034 (PLANNED): Compare baseline and final diff in a dirty repository and check every agent change has a scoped reason.

## REQ-035

**Source requirement:** REQ-035: Short impact plan และประเมินใหม่เมื่อ architecture/API/schema/scope เปลี่ยน

- **Objective:** Plan impact and revisit material changes.
- **Scope:** Short impact plans; architecture, API, schema and scope changes.
- **Observable acceptance criteria (AC-035):** Before implementation a short plan names affected areas and risks; newly discovered changes in any listed dimension trigger impact reassessment and required scoped approval before dependent work.
- **Dependencies:** REQ-031, REQ-048, REQ-049.
- **Planned implementation area:** core/engineering-flow.md (future)
- **Planned verification:** TC-REQ-035 (PLANNED): Evaluate a mid-task schema or API change and inspect revised plan, scope and approval handling.

## REQ-036

**Source requirement:** REQ-036: Coding/quality ครอบคลุม validation/errors/nulls/logging/maintainability/performance/reliability/accessibility ตามบริบท

- **Objective:** Apply context-appropriate software quality guidance.
- **Scope:** Validation, errors, nulls, logging, maintainability, performance, reliability and accessibility.
- **Observable acceptance criteria (AC-036):** Engineering guidance covers all listed concerns and records applicable checks or justified non-applicability; reports reference concrete inspected behavior rather than blanket quality claims.
- **Dependencies:** REQ-033, REQ-037, REQ-038.
- **Planned implementation area:** core/engineering.md; profiles/ (future)
- **Planned verification:** TC-REQ-036 (PLANNED): Review concern coverage and evaluate representative backend and UI changes with observable quality findings.

## REQ-037

**Source requirement:** REQ-037: .NET/Angular/Python/PostgreSQL profiles พร้อมแนวทางต่อ React/Java/company โดยไม่บังคับ stack

- **Objective:** Provide optional stack profiles without imposing a stack.
- **Scope:** .NET, Angular, Python and PostgreSQL; extension guidance for React, Java and company profiles.
- **Observable acceptance criteria (AC-037):** Four named profiles exist and can be selected only when relevant; extension guidance defines how React, Java or company rules fit without changing the canonical core or requiring migration.
- **Dependencies:** REQ-006, REQ-036, REQ-054.
- **Planned implementation area:** profiles/; docs/profile-extension.md (future)
- **Planned verification:** TC-REQ-037 (PLANNED): Inspect the four profiles and evaluate profile selection plus an additional company profile in an unrelated stack.

## REQ-038

**Source requirement:** REQ-038: เลือก unit/integration/API/E2E/regression ตาม behavior และ risk

- **Objective:** Select tests from behavior and risk.
- **Scope:** Unit, integration, API, E2E and regression testing.
- **Observable acceptance criteria (AC-038):** Test planning maps changed behavior and risk to suitable layers with reasons for selected or omitted layers; it avoids requiring every layer for every change.
- **Dependencies:** REQ-031, REQ-048, REQ-072.
- **Planned implementation area:** core/verification.md; skills/test/ (future)
- **Planned verification:** TC-REQ-038 (PLANNED): Evaluate low-risk pure logic and cross-system behavior changes; inspect test-layer rationale and acceptance coverage.

## REQ-039

**Source requirement:** REQ-039: แยก baseline failure/flaky test/environment limitation จาก regression ใหม่

- **Objective:** Distinguish existing failures from new regressions.
- **Scope:** Baseline failures, flaky tests and environment limitations.
- **Observable acceptance criteria (AC-039):** Check reports separate observed pre-existing failure, supported flaky classification, environmental blockers and new regression; unknown cause stays unresolved rather than being assigned to a convenient category.
- **Dependencies:** REQ-015, REQ-040, REQ-041.
- **Planned implementation area:** core/verification.md; templates/check-report.md (future)
- **Planned verification:** TC-REQ-039 (PLANNED): Evaluate baseline, intermittent, missing-tool and introduced-failure fixtures and verify evidence supports each classification.

## REQ-040

**Source requirement:** REQ-040: Check status PASS/FAIL/NOT_RUN/NOT_APPLICABLE/BLOCKED พร้อมหลักฐาน

- **Objective:** Report actual check outcomes with evidence.
- **Scope:** PASS, FAIL, NOT_RUN, NOT_APPLICABLE and BLOCKED.
- **Observable acceptance criteria (AC-040):** Every check records one exact status, inspected/executed scope, result evidence or a reason it did not run; a test file's existence never counts as PASS.
- **Dependencies:** REQ-039, REQ-043, REQ-077.
- **Planned implementation area:** core/verification.md; templates/check-report.md (future)
- **Planned verification:** TC-REQ-040 (PLANNED): Evaluate executed passing/failing checks and unexecuted/inapplicable/blocked checks; reject unsupported PASS claims.

## REQ-041

**Source requirement:** REQ-041: ตรวจ build/test/lint scripts และผลข้างเคียงก่อนรัน

- **Objective:** Inspect commands before running project checks.
- **Scope:** Build, test and lint scripts; transitive commands and side effects.
- **Observable acceptance criteria (AC-041):** Before execution the agent inspects invoked scripts and relevant side effects, including writes, network, installs and production access; unsafe or unauthorized execution is withheld with a specific reason.
- **Dependencies:** REQ-011, REQ-049, REQ-052.
- **Planned implementation area:** core/command-safety.md; skills/test/ (future)
- **Planned verification:** TC-REQ-041 (PLANNED): Evaluate harmless checks and scripts with install/deploy side effects; inspect the pre-execution decision.

## REQ-042

**Source requirement:** REQ-042: Self-review requirement/architecture/quality/security/governance ไม่อ้างเป็น independent audit

- **Objective:** Perform scoped self-review without overstating independence.
- **Scope:** Requirements, architecture, quality, security and governance.
- **Observable acceptance criteria (AC-042):** Closure evaluates all five review dimensions or explains non-applicability, links findings to evidence and labels self-review as self-review rather than an independent audit.
- **Dependencies:** REQ-031, REQ-036, REQ-044, REQ-073.
- **Planned implementation area:** core/self-review.md (future)
- **Planned verification:** TC-REQ-042 (PLANNED): Evaluate a change containing a requirement miss and a governance issue; inspect findings and limits of the review claim.

## REQ-043

**Source requirement:** REQ-043: Trace requirement → implementation → tests → evidence โดยไม่ต้องสร้าง PR/commit เอง

- **Objective:** Trace requirements to delivered behavior and real evidence.
- **Scope:** Requirement, implementation, test case and execution-evidence links.
- **Observable acceptance criteria (AC-043):** Traceability records link requirement criteria to implementing files, planned/existing test cases and actual execution evidence; missing links remain gaps, and creating a PR or commit is not a prerequisite.
- **Dependencies:** REQ-031, REQ-040, REQ-080.
- **Planned implementation area:** docs/build/TRACEABILITY.md; templates/traceability.md (future)
- **Planned verification:** TC-REQ-043 (PLANNED): Check links and distinguish planned tests from executed checks; sample a requirement end to end without requiring a PR/commit.

## REQ-044

**Source requirement:** REQ-044: Definition of Done ตาม scope และ mandatory checks พร้อม Memory Impact

- **Objective:** Close tasks against an explicit definition of done.
- **Scope:** Scope, mandatory checks, unresolved gaps and memory impact.
- **Observable acceptance criteria (AC-044):** Completion rules identify mandatory checks for the current scope; DONE is withheld when required checks or scope remain incomplete, and closure includes memory impact even when no write is needed.
- **Dependencies:** REQ-023, REQ-040, REQ-045.
- **Planned implementation area:** core/definition-of-done.md (future)
- **Planned verification:** TC-REQ-044 (PLANNED): Evaluate a completed task, a blocked mandatory check and a no-memory-change task; inspect status and closure fields.

## REQ-045

**Source requirement:** REQ-045: Task status DONE/PARTIALLY COMPLETE/BLOCKED/DECISION REQUIRED อย่างซื่อสัตย์

- **Objective:** Use truthful task completion states.
- **Scope:** DONE, PARTIALLY COMPLETE, BLOCKED and DECISION REQUIRED.
- **Observable acceptance criteria (AC-045):** Reporting defines and uses the four exact task states; completed documentation does not imply implemented product features, and blocked work or required decisions identify the remaining action.
- **Dependencies:** REQ-040, REQ-044.
- **Planned implementation area:** core/reporting.md; templates/engineering-report.md (future)
- **Planned verification:** TC-REQ-045 (PLANNED): Evaluate one scenario for each state and compare the claimed status with actual scope and evidence.

## REQ-046

**Source requirement:** REQ-046: Engineering report แบบ redacted; ไม่อ้าง tamper-proof audit หรือ exhaustive access log

- **Objective:** Provide useful reports without disclosing sensitive data or overstating auditability.
- **Scope:** Redacted engineering reports and evidence limits.
- **Observable acceptance criteria (AC-046):** Report templates cover actions, outcomes and gaps while omitting secrets/private values outside the authorized scope; they explicitly avoid tamper-proof audit and exhaustive access-log claims.
- **Dependencies:** REQ-013, REQ-040, REQ-050.
- **Planned implementation area:** core/reporting.md; templates/engineering-report.md (future)
- **Planned verification:** TC-REQ-046 (PLANNED): Evaluate synthetic sensitive output and partial tool visibility; inspect redaction and bounded claims.

## REQ-047

**Source requirement:** REQ-047: Governance G1 Observe/G2 Assist/G3 Controlled/G4 Restricted เป็นโมเดลของ Kiyo

- **Objective:** Define Kiyo's advisory governance levels.
- **Scope:** G1 Observe, G2 Assist, G3 Controlled and G4 Restricted.
- **Observable acceptance criteria (AC-047):** Guidance defines all four levels, their intended permissions/approval expectations and examples; labels identify them as Kiyo's model, with actual authority and enforcement remaining with the native host.
- **Dependencies:** REQ-007, REQ-049, REQ-051.
- **Planned implementation area:** core/governance.md (future)
- **Planned verification:** TC-REQ-047 (PLANNED): Review the level definitions and evaluate the same request under each level without overriding host restrictions.

## REQ-048

**Source requirement:** REQ-048: Risk LOW/MEDIUM/HIGH/CRITICAL แยกจาก governance และพิจารณา target/environment/data/reversibility/impact

- **Objective:** Assess risk separately from governance mode.
- **Scope:** LOW, MEDIUM, HIGH and CRITICAL; target, environment, data, reversibility and impact.
- **Observable acceptance criteria (AC-048):** Risk assessment records all five dimensions and an evidence-based risk level; governance level is a separate field and never mechanically equated to risk.
- **Dependencies:** REQ-047, REQ-050, REQ-052.
- **Planned implementation area:** core/risk.md; templates/risk-assessment.md (future)
- **Planned verification:** TC-REQ-048 (PLANNED): Compare local reversible and production irreversible scenarios under the same governance level and inspect risk rationale.

## REQ-049

**Source requirement:** REQ-049: Scoped human approval; ไม่ใช้ blanket approval และไม่ถามซ้ำเมื่อ approval เดิมยังตรงขอบเขต

- **Objective:** Respect scoped human approval without repetitive requests.
- **Scope:** Approval scope, authority, continuing validity and material change.
- **Observable acceptance criteria (AC-049):** Approval records identify action, target, environment and applicable limits; a still-valid scoped approval is reused, unrelated work is not covered by blanket approval, and material changes trigger reassessment.
- **Dependencies:** REQ-011, REQ-035, REQ-048.
- **Planned implementation area:** core/approvals.md (future)
- **Planned verification:** TC-REQ-049 (PLANNED): Evaluate valid prior approval, expired/revoked approval and changed-target scenarios; inspect whether a new question is actually necessary.

## REQ-050

**Source requirement:** REQ-050: Data classification Public/Internal/Confidential/Restricted ไม่ตัดสินจากชื่อไฟล์อย่างเดียว

- **Objective:** Classify data from evidence and policy.
- **Scope:** Public, Internal, Confidential and Restricted.
- **Observable acceptance criteria (AC-050):** Policy defines all four classes and how to handle uncertain classification; classification considers content, provenance and applicable policy rather than filename alone, without reading forbidden secrets.
- **Dependencies:** REQ-011, REQ-046, REQ-054.
- **Planned implementation area:** core/data-policy.md (future)
- **Planned verification:** TC-REQ-050 (PLANNED): Evaluate misleading filenames, mixed data and inaccessible content; confirm uncertainty and access boundaries remain explicit.

## REQ-051

**Source requirement:** REQ-051: Least privilege สำหรับ tools/files/network; host เป็นผู้ enforce

- **Objective:** Use minimum necessary access within host controls.
- **Scope:** Tools, files and network permissions.
- **Observable acceptance criteria (AC-051):** Procedures request/use only access needed for the scoped task, obey denied capabilities and assign enforcement to the host; Kiyo text cannot grant permissions by itself.
- **Dependencies:** REQ-007, REQ-011, REQ-049.
- **Planned implementation area:** core/access-contracts.md; core/governance.md (future)
- **Planned verification:** TC-REQ-051 (PLANNED): Evaluate a task with excessive proposed access and a denied host action; inspect reduced access and refusal to bypass.

## REQ-052

**Source requirement:** REQ-052: Dangerous action policy แยก draft/generate/read/execute และ local/production

- **Objective:** Differentiate dangerous operations by action and environment.
- **Scope:** Draft/generate/read/execute; local versus production.
- **Observable acceptance criteria (AC-052):** The dangerous-action policy distinguishes producing instructions from executing them and evaluates target/environment effects; production or destructive execution requires applicable scoped authorization before action.
- **Dependencies:** REQ-041, REQ-048, REQ-049.
- **Planned implementation area:** core/dangerous-actions.md (future)
- **Planned verification:** TC-REQ-052 (PLANNED): Evaluate drafting SQL, reading local fixtures and executing a destructive production command; inspect distinct decisions.

## REQ-053

**Source requirement:** REQ-053: Dependency governance ตรวจความจำเป็น ที่มา License และ Security เท่าที่มีหลักฐาน

- **Objective:** Govern dependencies using observed evidence.
- **Scope:** Necessity, provenance, license and security of dependencies.
- **Observable acceptance criteria (AC-053):** Proposed dependencies include need, source and available license/security evidence; missing evidence remains explicit, additions require appropriate authorization and no end-user Kiyo runtime dependency is introduced.
- **Dependencies:** REQ-003, REQ-041, REQ-049.
- **Planned implementation area:** core/dependencies.md (future)
- **Planned verification:** TC-REQ-053 (PLANNED): Evaluate unnecessary, unverifiable and justified dependencies; inspect authorization and evidence boundaries without invented scan results.

## REQ-054

**Source requirement:** REQ-054: Organization/project policy packs มี ownership/status/conflict handling และไม่ลด policy เงียบ ๆ

- **Objective:** Support owned organization and project policies.
- **Scope:** Policy ownership, status, applicability, precedence and conflicts.
- **Observable acceptance criteria (AC-054):** Policy pack templates record owner, status and scope; conflicts are resolved according to native authority or surfaced for decision, and stricter applicable policy is not silently weakened.
- **Dependencies:** REQ-011, REQ-049, REQ-055.
- **Planned implementation area:** policies/; templates/policy-pack.md (future)
- **Planned verification:** TC-REQ-054 (PLANNED): Evaluate conflicting organization/project packs and an unapproved proposal; verify provenance and visible conflict handling.

## REQ-055

**Source requirement:** REQ-055: Provider/model policy ไม่เหมาว่า Enterprise ปลอดภัย และไม่อ้าง egress enforcement

- **Objective:** Treat provider and model policy as evidence-dependent.
- **Scope:** Provider/model/account restrictions and data egress limits.
- **Observable acceptance criteria (AC-055):** Guidance uses documented applicable account/provider constraints or UNKNOWN, makes no blanket Enterprise safety assumption and never claims Kiyo itself prevents data egress.
- **Dependencies:** REQ-013, REQ-050, REQ-054.
- **Planned implementation area:** core/provider-policy.md (future)
- **Planned verification:** TC-REQ-055 (PLANNED): Evaluate an unknown account tier and an Enterprise label with missing policy evidence; inspect conservative factual reporting.

## REQ-056

**Source requirement:** REQ-056: Concept mapping ISO 12207/29148/25010/29119 โดยตรวจ edition/source

- **Objective:** Map engineering concepts to verified standards sources.
- **Scope:** ISO 12207, 29148, 25010 and 29119 concept mappings.
- **Observable acceptance criteria (AC-056):** A mapping records each standard's verified edition/source, relevant Kiyo concepts and limits; inaccessible details remain gaps and concept alignment is not represented as compliance or certification.
- **Dependencies:** REQ-007; Prompt 02 authoritative-source research.
- **Planned implementation area:** docs/standards/engineering.md (future)
- **Planned verification:** TC-REQ-056 (PLANNED): Verify editions against authoritative sources and review each concept mapping for evidence and non-certification language.

## REQ-057

**Source requirement:** REQ-057: Governance/security mapping ISO 27001/42001/23894, NIST SSDF/AI RMF, OWASP ASVS; supporting 38507/27034/SAMM และ 5338 เฉพาะกรณี

- **Objective:** Map governance and security concepts with appropriate limits.
- **Scope:** ISO 27001/42001/23894; NIST SSDF/AI RMF; OWASP ASVS; supporting ISO 38507/27034 and SAMM; ISO 5338 only when applicable.
- **Observable acceptance criteria (AC-057):** Mappings record verified editions/versions and sources for named frameworks, distinguish primary/supporting mappings and include a stated applicability decision for ISO 5338; no certification claim is made.
- **Dependencies:** REQ-007, REQ-056; Prompt 02 authoritative-source research.
- **Planned implementation area:** docs/standards/governance-security.md (future)
- **Planned verification:** TC-REQ-057 (PLANNED): Check official sources, versions, applicability and mapping limits; record inaccessible source details rather than inventing clauses.

## REQ-058

**Source requirement:** REQ-058: AST01 Malicious Skills — trust/provenance review และข้อจำกัด

- **Objective:** Address AST01 Malicious Skills through trust review.
- **Scope:** Skill provenance, suspicious instructions and review limits.
- **Observable acceptance criteria (AC-058):** Skill Audit checks origin, claimed authority and suspicious behavior, reports unknown provenance and explains that review cannot prove absence of malicious intent.
- **Dependencies:** REQ-012, REQ-065; AST taxonomy source research.
- **Planned implementation area:** core/skill-security.md; templates/skill-audit.md (future)
- **Planned verification:** TC-REQ-058 (PLANNED): Evaluate a malicious-instruction fixture and a missing-origin skill; inspect findings, evidence and stated limits.

## REQ-059

**Source requirement:** REQ-059: AST02 Supply Chain Compromise — release provenance และ dependency discipline

- **Objective:** Address AST02 Supply Chain Compromise.
- **Scope:** Release provenance, artifact origin and dependency discipline.
- **Observable acceptance criteria (AC-059):** Release/audit guidance records available source-to-artifact provenance and dependency evidence, flags missing or inconsistent provenance and does not invent hashes, signatures or trusted publishers.
- **Dependencies:** REQ-053, REQ-079.
- **Planned implementation area:** core/skill-security.md; docs/release.md (future)
- **Planned verification:** TC-REQ-059 (PLANNED): Evaluate changed artifacts and missing provenance; verify any reported digest is actually computed from the identified artifact.

## REQ-060

**Source requirement:** REQ-060: AST03 Over-Privileged Skills — minimum access และ host responsibility

- **Objective:** Address AST03 Over-Privileged Skills.
- **Scope:** Minimum tool/file/network access and host responsibility.
- **Observable acceptance criteria (AC-060):** Skill review compares requested access with demonstrated task need and flags excess; remediation respects host permission controls and does not claim Kiyo can independently enforce them.
- **Dependencies:** REQ-027, REQ-051.
- **Planned implementation area:** core/skill-security.md (future)
- **Planned verification:** TC-REQ-060 (PLANNED): Evaluate a read-only skill requesting write/network access and inspect the least-access recommendation.

## REQ-061

**Source requirement:** REQ-061: AST04 Insecure Metadata — honest schema/metadata ไม่เพิ่ม native fields ที่ไม่รองรับ

- **Objective:** Address AST04 Insecure Metadata.
- **Scope:** Native schemas, metadata accuracy and unsupported fields.
- **Observable acceptance criteria (AC-061):** Manifests/frontmatter use verified native fields with truthful values; Kiyo advisory metadata is clearly separated from native-enforced fields and unsupported permission/security declarations are not invented.
- **Dependencies:** REQ-005, REQ-013; native schema research.
- **Planned implementation area:** platforms/; core/skill-security.md (future)
- **Planned verification:** TC-REQ-061 (PLANNED): Validate each overlay against its observed schema and evaluate a fabricated enforcement-field fixture.

## REQ-062

**Source requirement:** REQ-062: AST05 Untrusted External Instructions — data versus authority รวม memory poisoning

- **Objective:** Address AST05 Untrusted External Instructions.
- **Scope:** Data versus authority, including memory poisoning.
- **Observable acceptance criteria (AC-062):** Security procedures identify embedded commands in external content and memory as data, reject unauthorized policy/permission changes and surface relevant injection evidence without executing it.
- **Dependencies:** REQ-011, REQ-012, REQ-016.
- **Planned implementation area:** core/trust-boundaries.md; core/skill-security.md (future)
- **Planned verification:** TC-REQ-062 (PLANNED): Evaluate tool-output and poisoned-memory instructions attempting to widen scope or exfiltrate data; inspect the response.

## REQ-063

**Source requirement:** REQ-063: AST06 Weak Isolation — host sandbox responsibility ไม่อ้าง Kiyo sandbox

- **Objective:** Address AST06 Weak Isolation honestly.
- **Scope:** Host sandboxing and isolation limitations.
- **Observable acceptance criteria (AC-063):** Guidance records observed host isolation or UNKNOWN, names host responsibility and contains no Kiyo sandbox claim; unsupported isolation requirements become explicit compatibility gaps.
- **Dependencies:** REQ-007, REQ-051, REQ-067.
- **Planned implementation area:** core/skill-security.md; docs/compatibility.md (future)
- **Planned verification:** TC-REQ-063 (PLANNED): Evaluate hosts with known and unknown isolation settings; inspect limits and absence of fabricated sandbox enforcement.

## REQ-064

**Source requirement:** REQ-064: AST07 Update Drift — version/change/permission review และ approved updates

- **Objective:** Address AST07 Update Drift.
- **Scope:** Versions, changes, permissions and approved updates.
- **Observable acceptance criteria (AC-064):** Update guidance compares old/new content and requested permissions, records available provenance and requires applicable update approval; an update cannot silently expand approved scope or replace user policy.
- **Dependencies:** REQ-049, REQ-076, REQ-079.
- **Planned implementation area:** core/skill-security.md; docs/maintenance.md (future)
- **Planned verification:** TC-REQ-064 (PLANNED): Evaluate an update adding permissions and local policy changes; verify the approval boundary and preserved user content.

## REQ-065

**Source requirement:** REQ-065: AST08 Poor Scanning — static/behavioral/adversarial review ไม่อ้าง proof of safety

- **Objective:** Address AST08 Poor Scanning without claiming proof of safety.
- **Scope:** Static, behavioral and adversarial reviews.
- **Observable acceptance criteria (AC-065):** Audit guidance defines distinct static, behavioral and adversarial checks, records actual execution and blind spots and never treats clean scans as proof that a skill is safe.
- **Dependencies:** REQ-040, REQ-058, REQ-077.
- **Planned implementation area:** core/skill-security.md; tests/ (future)
- **Planned verification:** TC-REQ-065 (PLANNED): Evaluate a fixture passing static checks but failing behavior and inspect the separated results and bounded conclusion.

## REQ-066

**Source requirement:** REQ-066: AST09 No Governance — inventory/owner/approval/revocation templates ไม่สร้าง central service

- **Objective:** Address AST09 No Governance with static artifacts.
- **Scope:** Skill inventory, owner, approval and revocation templates.
- **Observable acceptance criteria (AC-066):** Templates capture inventory identity, ownership, approval status/scope and revocation decisions without invented approvers; use requires no central service or live registry.
- **Dependencies:** REQ-003, REQ-049, REQ-054.
- **Planned implementation area:** templates/skill-governance/ (future)
- **Planned verification:** TC-REQ-066 (PLANNED): Populate synthetic approved, unknown-owner and revoked examples; validate fields and absence of a service dependency.

## REQ-067

**Source requirement:** REQ-067: AST10 Cross-Platform Reuse — control parity และ explicit gaps

- **Objective:** Address AST10 Cross-Platform Reuse through explicit control parity.
- **Scope:** Cross-host controls and gaps across all six targets.
- **Observable acceptance criteria (AC-067):** A parity matrix maps each relevant control independently to the six targets, distinguishes Kiyo guidance from native enforcement and records unsupported/unverified behavior instead of assuming equivalence.
- **Dependencies:** REQ-005, REQ-007, REQ-061, REQ-077.
- **Planned implementation area:** docs/control-parity.md; tests/live/ (future)
- **Planned verification:** TC-REQ-067 (PLANNED): Review every control row and compare claims with target-specific source and live evidence.

## REQ-068

**Source requirement:** REQ-068: Init skill — safe scan, evidence-backed memory, authorized writes, rerun-safe, no source changes

- **Objective:** Provide a safe, repeatable Init skill.
- **Scope:** Scoped scan, evidenced memory, authorized writes and no source changes.
- **Observable acceptance criteria (AC-068):** Init inspects only permitted relevant material, creates/updates memory only with applicable authorization and evidence, leaves source untouched and reruns without duplicates or overwriting human edits.
- **Dependencies:** REQ-015, REQ-016, REQ-017, REQ-024, REQ-027.
- **Planned implementation area:** skills/init/ (future)
- **Planned verification:** TC-REQ-068 (PLANNED): Run clean, dirty, missing-memory and repeat-init scenarios; compare source/user files and check memory evidence.

## REQ-069

**Source requirement:** REQ-069: Requirement skill — requirement/readiness/open decisions โดยไม่ implement

- **Objective:** Provide requirements and readiness assessment without implementation.
- **Scope:** Requirement drafting, readiness and open decisions.
- **Observable acceptance criteria (AC-069):** Requirement outputs the required fields, labels proposals and unresolved decisions, assesses readiness and does not implement code or silently approve its own suggestions.
- **Dependencies:** REQ-027, REQ-031, REQ-032.
- **Planned implementation area:** skills/requirement/ (future)
- **Planned verification:** TC-REQ-069 (PLANNED): Evaluate a partially specified feature and inspect readiness, decision labels and unchanged implementation files.

## REQ-070

**Source requirement:** REQ-070: Implement skill — feature/bug/refactor พร้อม approvals/checks/repair/memory impact

- **Objective:** Provide a scoped Implement skill.
- **Scope:** Feature, bug fix and refactor workflows.
- **Observable acceptance criteria (AC-070):** Implement follows applicable approvals, impact plan, minimal-change practices and actual checks; repair loops stop at the declared bound and closure records memory impact and honest remaining gaps.
- **Dependencies:** REQ-023, REQ-029, REQ-034, REQ-035, REQ-044, REQ-049.
- **Planned implementation area:** skills/implement/ (future)
- **Planned verification:** TC-REQ-070 (PLANNED): Evaluate feature, bug and refactor scenarios plus a persistent failed check; inspect scoped diffs, evidence and closure.

## REQ-071

**Source requirement:** REQ-071: Review skill — evidence-based findings พร้อม severity/confidence และไม่มี automatic edits

- **Objective:** Provide evidence-based review without automatic edits.
- **Scope:** Findings, severity, confidence and review limits.
- **Observable acceptance criteria (AC-071):** Review reports concrete evidence/location, severity and confidence per finding, explains inspected scope and makes no automatic source, memory or report-file edits in read-only mode.
- **Dependencies:** REQ-027, REQ-034, REQ-042, REQ-046.
- **Planned implementation area:** skills/review/ (future)
- **Planned verification:** TC-REQ-071 (PLANNED): Evaluate known defects and uncertain findings; inspect evidence and compare all file snapshots before/after read-only review.

## REQ-072

**Source requirement:** REQ-072: Test skill — assess/run/write และผลตรวจจริง

- **Objective:** Provide explicit Test modes and truthful results.
- **Scope:** Assess, run and write modes.
- **Observable acceptance criteria (AC-072):** Assess plans checks without unintended execution/writes; run inspects scripts and reports actual outcomes; write creates tests only within authorized scope; existing test files never imply successful execution.
- **Dependencies:** REQ-027, REQ-038, REQ-039, REQ-040, REQ-041.
- **Planned implementation area:** skills/test/ (future)
- **Planned verification:** TC-REQ-072 (PLANNED): Evaluate all three modes, a denied execution and an environment blocker; inspect mode-specific effects and statuses.

## REQ-073

**Source requirement:** REQ-073: Security skill — application/skills/governance/self-check แบบ read-only โดย default

- **Objective:** Provide a Security skill with bounded submodes.
- **Scope:** Application, skills, governance and self-check; read-only default.
- **Observable acceptance criteria (AC-073):** Security supports the four listed submodes under one public skill, defaults to read-only, reports evidence and limits and requires scoped authorization for any transition to writes or execution.
- **Dependencies:** REQ-026, REQ-027, REQ-042, REQ-047, REQ-058, REQ-065.
- **Planned implementation area:** skills/security/ (future)
- **Planned verification:** TC-REQ-073 (PLANNED): Evaluate each submode and a requested remediation; verify default file preservation and no ninth public skill.

## REQ-074

**Source requirement:** REQ-074: Architecture skill — observed versus approved intent และ scoped drift report

- **Objective:** Provide an Architecture skill that preserves approved intent.
- **Scope:** Observed structure, approved decisions and scoped drift.
- **Observable acceptance criteria (AC-074):** Architecture distinguishes current observed code from approved intent, reports evidence-backed drift within inspection scope and does not rewrite decisions merely to match implementation.
- **Dependencies:** REQ-019, REQ-022, REQ-027, REQ-033.
- **Planned implementation area:** skills/architecture/ (future)
- **Planned verification:** TC-REQ-074 (PLANNED): Evaluate partial inspection and code/decision conflict; verify accurate limits and unchanged approved decisions.

## REQ-075

**Source requirement:** REQ-075: Memory skill — show/check/sync/repair แบบรักษา decisions และ human edits

- **Objective:** Provide explicit Memory modes preserving human knowledge.
- **Scope:** Show, check, sync and repair.
- **Observable acceptance criteria (AC-075):** Show/check remain read-only; sync/repair use authorized scoped writes, preserve approved decisions and human edits, handle stale/concurrent inputs and perform no writes for a no-change result.
- **Dependencies:** REQ-016, REQ-017, REQ-020, REQ-023, REQ-024, REQ-027.
- **Planned implementation area:** skills/memory/ (future)
- **Planned verification:** TC-REQ-075 (PLANNED): Evaluate all four modes, no-change sync and a concurrent edit; compare decisions, contents and timestamps.

## REQ-076

**Source requirement:** REQ-076: Version/update/uninstall รักษา user policies/memory และไม่ hardcode cache paths

- **Objective:** Preserve user knowledge through maintenance.
- **Scope:** Versioning, updates, uninstall and host-managed storage.
- **Observable acceptance criteria (AC-076):** Maintenance instructions use native host mechanisms without hardcoded cache paths; update/uninstall scenarios retain user policies and canonical memory, and version claims reflect actual artifacts.
- **Dependencies:** REQ-004, REQ-017, REQ-054, REQ-064.
- **Planned implementation area:** docs/maintenance.md; platforms/ (future)
- **Planned verification:** TC-REQ-076 (PLANNED): Exercise documented update/uninstall on each available target with user content present; mark unavailable targets NOT_TESTED.

## REQ-077

**Source requirement:** REQ-077: แยก static validation/behavioral evaluation/live six-target tests

- **Objective:** Separate three distinct verification layers.
- **Scope:** Static validation, behavioral evaluation and live six-target testing.
- **Observable acceptance criteria (AC-077):** Reports and test organization identify the three layers separately; static PASS cannot mark behavior or live targets passed, and each of six live targets retains its own results and missing prerequisites.
- **Dependencies:** REQ-005, REQ-040, REQ-043.
- **Planned implementation area:** tests/static/; tests/behavioral/; tests/live/ (future)
- **Planned verification:** TC-REQ-077 (PLANNED): Review layer separation and execute available suites; check that unrun layers/targets remain NOT_RUN or NOT_TESTED as appropriate.

## REQ-078

**Source requirement:** REQ-078: คู่มือผู้ใช้/ผู้พัฒนา พร้อม first-use/daily-use/maintenance และ native invocation จริง

- **Objective:** Document actual user and developer workflows.
- **Scope:** First use, daily use, maintenance and verified native invocation.
- **Observable acceptance criteria (AC-078):** User/developer guides cover all listed stages, clearly separate developer-only tooling from end-user use and link host-specific invocation to verified support or an explicit unverified gap.
- **Dependencies:** REQ-004, REQ-010, REQ-068, REQ-076.
- **Planned implementation area:** docs/user/; docs/developer/ (future)
- **Planned verification:** TC-REQ-078 (PLANNED): Walk through guides against available packages per target; verify commands and report untested walkthroughs honestly.

## REQ-079

**Source requirement:** REQ-079: Reproducible packages/release checklist; signatures ต้องมีจริง; publishing โดยเจ้าของอนุมัติ

- **Objective:** Prepare reproducible releases under owner authority.
- **Scope:** Deterministic packaging, release checklist, real signatures and publication.
- **Observable acceptance criteria (AC-079):** Repeated packaging of identical inputs yields identical artifact digests under a documented environment; release checks exclude developer scripts from payloads, record actual signatures or their absence and require owner approval before publishing.
- **Dependencies:** REQ-001, REQ-006, REQ-059, REQ-076; DEC-001, DEC-002, DEC-003.
- **Planned implementation area:** developer packaging/release scripts; docs/release.md (future)
- **Planned verification:** TC-REQ-079 (PLANNED): Package twice and compare computed hashes, inspect payloads and rehearse the checklist; do not publish or invent signatures/approval.

## REQ-080

**Source requirement:** REQ-080: Build traceability, resumable workflow และ final gap audit; ไม่อ้าง placeholder เป็น feature

- **Objective:** Keep the build resumable and auditable with honest gaps.
- **Scope:** Requirement registry, traceability, progress, decisions, issues, handoff and final gap audit.
- **Observable acceptance criteria (AC-080):** Prompt 01 records all 80 unique IDs with six expansion fields and a trace row each; every step updates progress/traceability/issues/handoff; a fresh session can identify completed work and next action; Prompt 29 audits final gaps and placeholders never count as features.
- **Dependencies:** All requirement IDs are inputs to final gap audit; each prompt's actual evidence.
- **Planned implementation area:** docs/build/BUILD-CONTRACT.md; REQUIREMENTS.md; TRACEABILITY.md; PROGRESS.md; DECISIONS.md; OPEN-ISSUES.md; HANDOFF.md; BASELINE.md; final gap audit (future)
- **Planned verification:** TC-REQ-080 (PLANNED): Validate registry/traceability coverage and links, review the handoff without chat history and later reconcile all acceptance criteria with actual implementation/test evidence at Prompts 29–30.


