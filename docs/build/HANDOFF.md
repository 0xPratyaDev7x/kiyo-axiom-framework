# Kiyo Compass — Handoff

## Resume without the prior chat

Kiyo Compass is the working-name AI Engineering & Governance Framework for coding
agents. It is static, Markdown-first, vendor-neutral and advisory. Native hosts
use tools and enforce permissions. No Kiyo runtime, hooks, MCP, daemon, telemetry,
central installer, Virtual Office or agent-team orchestration is authorized.

Four pillars: Project Intelligence, Software Engineering, AI Governance, Agentic
Skill Security. Exactly eight public skills: Init, Requirement, Implement,
Review, Test, Security, Architecture, Memory. Workflow Router, Governance Review,
Skill Audit and Self-check remain shared procedures/submodes.
One canonical specification with necessary self-contained native overlays.

## Current repository observation

Observed for Prompt 09 on 2026-09-29:

- Root: C:/Users/praty/source/@0xPratya7x/kiyo-codejadee-framework/kiyo-codejadee-framework
- Branch: main; HEAD: 372fd7a58ee51bbb98aef1c95940b84c39b8fe49.
- Initial working tree and index clean; tracked LICENSE, eight build files and
  five research/compatibility files, six architecture documents, source README,
  42 product files and three behavioral specification files (65 Markdown files total).
  Prompt 08 was committed before this work;
  previous checkout/HEAD/uncommitted snapshots are historical, not current facts.
- No applicable AGENTS.md found in repository or checked ancestors; no .kiyo
  project/product memory present.
- Git used a per-command safe.directory override for this exact root;
  global settings were not changed.
  The per-command empty core.excludesFile setting kept inventory independent of
  unreadable global ignores.
- LICENSE blob remains d2e60c5b160ed4f9ca096215e72efee5769936b1.
- No product version file, manifest or Git tag found in the scoped inventory.
- Prompt 09 creates fourteen Markdown files and changes fourteen existing Markdown files. No commits,
  tags, pushes, installs, publication or global settings changes were made here.

Recheck root, branch, index, unstaged/untracked changes and user edits on resume.
Preserve LICENSE and the 80 original requirements. See BASELINE for check results.

## Read order

1. [BUILD-CONTRACT](BUILD-CONTRACT.md).
2. [PROGRESS](PROGRESS.md), this handoff, [OPEN-ISSUES](OPEN-ISSUES.md).
3. Relevant [REQUIREMENTS](REQUIREMENTS.md), [TRACEABILITY](TRACEABILITY.md),
   [DECISIONS](DECISIONS.md), [BASELINE](BASELINE.md).
4. [Sources and redirects](../research/SOURCES.md).
5. [Standards baseline](../research/standards-baseline.md).
6. [Platform capabilities](../compatibility/platform-capabilities.md),
   [native invocation](../compatibility/native-invocation-map.md),
   [activation modes](../compatibility/activation-modes.md).
7. [Framework layout](../architecture/framework-layout.md),
   [content loading](../architecture/content-loading.md),
   [packaging contract](../architecture/packaging-contract.md),
   [naming/versioning](../architecture/naming-and-versioning.md),
   [ADR-001](../architecture/decisions/ADR-001-static-canonical-packages.md).
8. [ADR-002](../architecture/decisions/ADR-002-core-loading-budgets.md),
   [Core entry](../../src/kiyo/KIYO.md),
   [control index](../../src/kiyo/framework/control-index.md) and its relevant definitions.
9. [Memory specification](../../src/kiyo/framework/memory-specification.md),
   [shared lifecycle](../../src/kiyo/workflows/memory-lifecycle.md), relevant
   [templates](../../src/kiyo/framework/memory-specification.md#template-catalog) and
   [scenario specifications](../../tests/behavioral/memory/scenarios.md).
10. [Governance entry/procedure](../../src/kiyo/governance/ai-usage.md), relevant
    linked policies and [decision examples](../../src/kiyo/governance/decision-examples.md).

11. [AST mapping](../../src/kiyo/agent-security/owasp-ast10.md),
    [Skill Audit](../../src/kiyo/agent-security/trust-review.md), relevant security
    references/templates and [security scenarios](../../tests/behavioral/agent-security/scenarios.md).

12. [Workflow Router](../../src/kiyo/workflows/workflow-router.md),
    [adaptive depth](../../src/kiyo/workflows/adaptive-flow.md),
    [implementation](../../src/kiyo/workflows/implement-flow.md),
    [read-only](../../src/kiyo/workflows/read-only-flow.md),
    [repair/handoff](../../src/kiyo/workflows/repair-and-handoff.md) and
    [routing/flow specifications](../../tests/behavioral/routing/truth-table.md).

13. [Engineering selection](../../src/kiyo/framework/engineering/index.md), relevant
    standards/profiles, [concept mapping](../../src/kiyo/framework/engineering/standards-mapping.md)
    and [engineering/profile scenarios](../../tests/behavioral/engineering/scenarios.md).

Prompt 02 native checks and unrefreshed standards remain dated 2026-09-28.
Prompt 09 rechecked S01–S07 and added E01–E06 on 2026-09-29; public documentation
only, not licensed ISO text or actual stack verification. Prompt 07
rechecked AST/ASVS and the separate ASI announcement on 2026-09-29; see SOURCES.
Revalidate volatile schema details before
implementing native packages; use native references, not old chat, local skill
scaffolds or the OWASP proposed universal format.

## Completed work and evidence

Prompt 01 registered all REQ-001–080 and the build contract/roadmap.
Prompt 02 researched 11 dimensions for each of six targets and created the five
files above. Official metadata and behavior descriptions are DOCUMENTED_ONLY;
static repository/document checks alone can be VERIFIED.
Prompt 02 status: **DONE** for research; documentation checks passed. See
[Prompt 02 evidence](BASELINE.md#prompt-02-checks).

Prompt 03 adds the four architecture contracts, ADR and a single developer-only
source README scaffold. Status: **DONE** for architecture; documentation/design
checks passed. See [Prompt 03 evidence](BASELINE.md#prompt-03-checks).

Prompt 04 authors the shared Core with 16 controls and seven expected-response
examples. Status: **DONE** for Core; scoped static/document checks passed; see
[Prompt 04 evidence](BASELINE.md#prompt-04-checks). Expected responses are not
executed behavioral tests. No native Kiyo manifest or public skill is implemented.

Prompt 05 authors the Memory specification, shared lifecycle and eight templates,
plus 20 developer-only scenario specifications. Status: **DONE** for Memory;
scoped static checks passed; see [Prompt 05 evidence](BASELINE.md#prompt-05-checks).
Memory scenarios are NOT_RUN; no watcher/database/runtime or populated project
memory was created.

Prompt 06 adds nine governance policies and 18 synthetic decision examples,
with nine additional controls (31 total). Status: **DONE** for governance;
scoped static checks passed; see [Prompt 06 evidence](BASELINE.md#prompt-06-checks). No policy
engine, native settings, runtime or dangerous execution is introduced.

Prompt 07 adds six agent-security references, ten controls (41 total), four
optional neutral file templates and 19 synthetic scenario specifications.
Status: **DONE** for security guidance; scoped static checks passed; see
[Prompt 07 evidence](BASELINE.md#prompt-07-checks). AST taxonomy/status and ASI
separation were rechecked; no host/schema refresh or behavioral success is claimed.

Prompt 08 adds five workflow references, six controls (47 total), 30 Thai/English
routing rows and nine flow/recovery specifications. Status: **DONE** for shared
router/flow guidance; scoped static checks passed; see [Prompt 08 evidence](BASELINE.md#prompt-08-checks).
Router and flows are Markdown only; examples are NOT_RUN, not native dispatch.

Prompt 09 adds eight engineering references (six standards, selection and mapping),
four stack profiles plus an extension contract, seven controls (54 total) and
16 synthetic developer scenarios. Status: **DONE** for engineering/profile
guidance; static checks passed; see [Prompt 09 evidence](BASELINE.md#prompt-09-checks).
S01–S07 official catalogue metadata and E01–E06 profile sources were checked.
No full ISO text, exact taxonomy, certification, executed stack support or
automatic package installation is claimed.

No native version, account availability or installed-tool absence is inferred from the
assistant session. Each of Claude CLI, Claude VS Code, Codex CLI, Codex IDE,
Copilot CLI and Copilot VS Code remains **NOT_TESTED** live.

Research-documentation implementation is partial for REQ-004/005/010/056/057/067;
REQ-080 continuity remains partial. Other cited IDs receive research/design inputs
only; Prompt 03 does not promote architecture into implemented product controls.
Prompt 04 adds partial product Core instruction coverage recorded in TRACEABILITY;
completed instruction text does not imply completed skills or behavioral proof.
Prompt 05 adds shared Memory coverage; totals are 41 PARTIALLY_IMPLEMENTED and
39 NOT_IMPLEMENTED. REQ-068/074 have scenario inputs only; future skills are absent.
Prompt 06 adds shared governance coverage; current totals are 48 PARTIALLY_IMPLEMENTED
and 32 NOT_IMPLEMENTED. Dependency-policy input does not complete REQ-059 release checks.
Prompt 07 adds partial security guidance; current totals are 55 PARTIALLY_IMPLEMENTED
and 25 NOT_IMPLEMENTED. REQ-073 has shared input only; public Security skill pending.
Prompt 08 adds partial router/flow guidance; current totals are 60 PARTIALLY_IMPLEMENTED
and 20 NOT_IMPLEMENTED. REQ-026/068–075 get routing/shared-flow inputs only;
no public skill acceptance is promoted.
Prompt 09 adds partial instruction coverage for REQ-031–038/053/056 and updates
REQ-080 continuity. Current totals: 64 PARTIALLY_IMPLEMENTED / 16 NOT_IMPLEMENTED;
REQ-031/036/037/038 newly partial. All full requirement verifications remain NOT_RUN.

## Research findings to retain

- Codex IDE plugins are **UNSUPPORTED** in the 2026-09-28 official-source baseline;
  standalone IDE skills are separately documented. DEC-004 has no approved
  fallback/scope reduction. Do not claim six-target native-plugin compatibility.
- OpenAI and both Copilot targets document Agent Plugins 1.0 root plugin.json.
  Legacy manifests have different semantics. Claude documents its own manifest.
- Installing skills exposes metadata; full skill/core instructions are not
  automatically loaded every turn. Distinguish explicit invocation, inferred
  matching and persistent native project guidance.
- Claude explicitly does not load plugin-root CLAUDE.md as project context.
  Copilot documents namespaced plugin rules but their complete trigger/grammar
  semantics are unresolved. Do not invent a universal rules/core manifest field.
- Exact Codex/Copilot CLI plugin-qualified skill spelling, Codex custom-source
  lifecycle/cache behavior and minimum supported host versions need follow-up.
- Cache-independent resources must be packaged and resolved from actual installed
  skill locations. Prompt 03 defines the architecture below; resource reads and
  lifecycle remain untested. Absolute author checkout paths are not portable.
- ISO 12207 baseline is 2026 edition 2; 29148:2018 has a DIS replacement in
  development. SSDF 1.1 is final and 1.2 is draft. AST v1 is public review.
  ISO mappings are concept-level only; 38507/27034/SAMM supporting; 5338 only for
  actual AI-system development. No certification or invented clause mapping.

Open decisions: DEC-001 name/identifiers, DEC-002 release-license confirmation,
DEC-003 publisher/account/destination, DEC-004 unsupported IDE route.
They do not block the next Verification/DoD scope under the selected architecture; they do block
dependent release identities, claims or unapproved fallback choices.

Memory Impact: **NONE for project memory**. Build continuity/specification choices
are recorded in docs/build; no .kiyo/memory initialized or changed.

## Architecture and Core decisions to retain

- Product source is `src/kiyo/`: compact `KIYO.md`, core `framework/`, policy
  `governance/` and `agent-security/`, shared `workflows/`, optional `profiles/`,
  neutral `templates/`, exactly eight planned `skills/<name>/SKILL.md` entries.
  Core now includes the Memory specification and shared lifecycle; eight neutral
  Memory templates and governance policies/shared review procedure now exist.
  Agent-security references and four optional governance-record templates also
  exist, together with five router/flow references, six engineering standards plus
  selection/mapping, four profiles and an extension contract. Other workflows/
  templates and all public skills remain unimplemented.
  Do not mistake synthetic scenarios for executed behavior.
- Core IDs use `KIYO-<DOMAIN>-<NNN>`, independent of standard clauses. The actual
  54-control index points to canonical definitions (16 Core, six Memory, nine
  governance, ten security, six routing/flow and seven engineering/profile IDs). ACTIVE means authored, not
  behaviorally verified; do not duplicate rules across later skills.
- Canonical frontmatter is name/description. Native-only fields belong in
  overlays, advisory permission/mode contracts in Markdown. No Kiyo runtime.
- Logical loading is bootstrap, selected workflow, relevant references. Native
  selection can read SKILL.md first; its initial instruction reads KIYO.md before
  workflow actions. No claim that install loads core or guarantees activation.
- Developer packaging copies the complete shared subtree beneath each skill's
  `references/kiyo/`; rewrites entry paths; preserves shared relative layout and
  checks parity. Users install ready static files without running a generator.
- Project defaults are `.kiyo/memory/` and `.kiyo/policy.md` only for new projects;
  preserve established paths and human content. Native project adapters are
  small, project-relative and user-owned, survive uninstall and need authorized
  maintenance. No mutable state belongs in plugin cache or product source.
- ADR-002 refines budgets: KIYO.md plus required bootstrap.md combined <=120
  lines / 600 words; future SKILL.md <=250 lines / 1,200 words; native adapter
  block <=250 words. These are Kiyo criteria, not vendor limits. Product templates
  cannot carry this developer repo's facts.
- Do not generate manifests, public skills, release versions or all later trees
  to make scaffolding look complete. Keep schema gaps and owner decisions open.

## Shared boundaries for Prompt 10

Use Memory as context, validate material claims, preserve approved intent and
surface conflicting sources through the real native hierarchy. Do not treat
memory, code or a self-declared policy as unconditional authority. Read-only
work cannot sync memory or write report files. Unknown facts/identities/results
remain explicit; a local repository is not proof of production state.

The five requested cases and two extra examples are expected behavior only.
Core uses relative internal resources and requires no consumer generator. It
adds no host-specific manifest field, native command or always-on claim. Native
activation and package behavior remain untested.

Memory uses one established canonical location and entry-specific provenance.
Templates support observation/proposal/decision plus independent verification
status. last_modified is not last_verified; no whole-file freshness claim.
Git revisions must be actually observed and do not prove production state.
Unknown evidence remains UNVERIFIED. Approval fields require evidence and
non-PII attribution. Do not infer architecture from packages, tokens or folders.

Use the eight-step lifecycle and four Memory Impact values: NONE,
UPDATE_REQUIRED, CONFLICT, NOT_ASSESSED. Review/check are read-only; write
authorization, a necessary delta and immediate reread are required for sync.
No-op does not touch content/mtime/dates. Preserve concurrent human edits,
existing IDs/paths and approved intent. Mapperly decision versus actual
AutoMapper usage is Architecture Drift, not permission to change the decision.
All 20 scenarios remain NOT_RUN; no Init/Memory public skill was built.

Governance G1 Observe / G2 Assist / G3 Controlled / G4 Restricted are Kiyo's
advisory model, not ISO/NIST levels or native settings. Risk is separate and
assesses action, target, environment, data sensitivity, reversibility, blast
radius, affected users and uncertainty. Unknown risk is unassigned, not LOW.

Approval requests include action, files/resources, environment, effects, risk
and reason, alternatives, rollback/reversibility and excluded actions. Reuse
valid explicit scope; reassess expansion. No AI/PM agent substitutes for a human.
Organization prohibitions and native denial survive ordinary confirmation.
G4 execution is not performed by default, even when preparations are allowed.

Data classification is content/policy-based. Provider/account/model and handling
claims require evidence; Enterprise is not assurance. Kiyo is not DLP/egress
control and cannot guarantee that no data was sent before loading policy.
Read-only and test labels do not prove safety; dependency addition is not
always HIGH; migration drafting is not applying to production. All 18 examples
remain NOT_RUN and express expected decisions, not agent/host test outcomes.

Agentic Skills AST01–AST10 uses a public-review taxonomy, distinct from ASI
Agentic Applications and application-code security. Skill Audit, injection and
update review are shared procedures, not extra public skills. Each mapped risk
has explicit control owners, evidence requirements, residual limits and scenario IDs.
Unsigned does not prove malicious; hashes/signatures do not prove safe behavior.

Required but unverified host isolation means HOLD dependent execution/disclosure.
Native denial/organization prohibition cannot be bypassed by a record. Kiyo has
no sandbox/network block/runtime signature verifier or complete injection defense.
Static, behavioral/adversarial and per-target checks remain separate. Regex/LLM
review is not proof of safety. All 19 security scenarios remain NOT_RUN.

Optional records use actual human scope/evidence and existing user-owned locations.
Do not initialize them merely by loading a template; revocation text is not native
disablement. The ten-row/six-target parity matrix records UNKNOWN/NOT_TESTED
controls and the historical unsupported IDE route, with freshness limits.

Router output separates one of eight primary skills from read-only/write/execute
effects, relevant shared checklists, risk treatment, decisions and completion evidence.
Explicit mismatch is reported with a proposed route; it cannot silently replace
invocation or authorize effects. Bug fixes use Implement; reviews/explanations
stay read-only, coverage assessment uses Test assess and memory audit Memory check.
Ambiguous login requests begin read-only. No agent/team orchestration exists.

Implementation orders preflight, authorized Memory orientation, understanding,
current inspection/validation, plan, risk/governance, required human decision,
edits, verification, self-review, memory impact/sync and completion. Read-only
flow has seven analysis stages, no implementation or Memory writes. A requested
report-file output is separately scoped write, not a hidden read-only side effect.

Tiny/Normal/High-impact scales ceremony, not safety or evidence. A tiny sensitive
change still needs applicable approval. Repair distinguishes baseline, regression,
environment and Unknown; at most two unsuccessful correction/recheck cycles by
default, excluding initial discovery. Do not reset by changing turn/skill/scope
labels. Replan material changes; further attempts require a bounded valid decision.
Handoff keeps facts, next action, true approval scope and attempt history, never
private reasoning or a write in read-only mode. All 30 routing rows and nine flow
cases remain NOT_RUN; no public/native route has been implemented or verified.

Engineering standards are conditional shared references in framework/engineering.
Use existing safe architecture, minimal diff and human-edit preservation; flag
insecure patterns instead of copying them. Quality grouping is Kiyo's adaptation,
not exact ISO taxonomy. Distinguish requirements/proposals from approved intent
and actual checks from expected evidence. No new textbook or mandatory full read.

Every profile starts with actual version/config/toolchain/architecture discovery.
Retain project-selected .NET packages/tests, Angular forms/state/style, Python
manager/framework/tests and PostgreSQL migration tooling. Presets are opt-in;
migration-file authoring is separate from execution. React/Java/company examples
are extension outlines only. All 16 engineering cases remain NOT_RUN; source
containment checks do not establish relocated-cache behavior or actual stack support.

## Exact next action

Prompt 09 is complete within its static engineering/profile scope; stop here.
**Next: Prompt 10 Verification/DoD**, only when supplied by the user. Recheck
repository and read the files above; implement only that prompt's verification/
completion scope, reusing shared Core/Memory/governance/security/flows/engineering.
Do not infer authorization for dangerous execution, project policy/memory
initialization, public skills, native overlays, generators or release work.

Safe to continue: **YES for a user-requested Prompt 10 Verification/DoD**.
Its shared instruction inputs are ready. Publication, unsupported native routes,
dangerous execution and live support claims remain outside scope.

