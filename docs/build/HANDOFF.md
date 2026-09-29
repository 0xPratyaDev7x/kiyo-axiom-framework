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

Observed for Prompt 14 on 2026-09-29:

- Root: C:/Users/praty/source/@0xPratya7x/kiyo-codejadee-framework/kiyo-codejadee-framework
- Branch: main; HEAD: a4712ef9be725bcd21ba81f2764f017a2e7b3b4c.
- Initial working tree and index clean; tracked LICENSE, eight build files and
  five research/compatibility files, six architecture documents, source README,
  77 product files, eight behavioral specification files and three developer evidence
  records (108 Markdown files total). Prompt 13 was committed before this work;
  previous checkout/HEAD/uncommitted snapshots are historical, not current facts.
- No applicable AGENTS.md found in repository or checked ancestors; no .kiyo
  project/product memory present.
- Git used a per-command safe.directory override for this exact root;
  global settings were not changed.
  The per-command empty core.excludesFile setting kept inventory independent of
  unreadable global ignores.
- LICENSE blob remains d2e60c5b160ed4f9ca096215e72efee5769936b1.
- No product version file, manifest or Git tag found in the scoped inventory.
- Prompt 14 creates six Markdown files and changes fourteen existing Markdown files. No commits,
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

14. [Evidence Contract](../../src/kiyo/framework/evidence-contract.md),
    [Definition of Done](../../src/kiyo/framework/definition-of-done.md),
    [reporting contract/templates](../../src/kiyo/framework/reporting-contract.md)
    and [good/bad scenarios](../../tests/behavioral/verification/scenarios.md).

15. [Init entry](../../src/kiyo/skills/init/SKILL.md),
    [procedure](../../src/kiyo/workflows/init.md), relevant discovery/activation/
    output references, [scenario specifications](../../tests/behavioral/init/scenarios.md)
    and [bounded forward evidence](../evidence/init/forward-trials.md).

16. [Requirement entry](../../src/kiyo/skills/requirement/SKILL.md),
    [shared procedure](../../src/kiyo/workflows/requirement.md),
    [readiness](../../src/kiyo/framework/requirement-readiness.md),
    [template](../../src/kiyo/templates/requirement.md),
    [scenario specifications](../../tests/behavioral/requirement/scenarios.md) and
    [bounded forward evidence](../evidence/requirement/forward-trials.md).

17. [Implement entry](../../src/kiyo/skills/implement/SKILL.md),
    [shared flow](../../src/kiyo/workflows/implement-flow.md),
    [short plan](../../src/kiyo/templates/short-plan.md), existing repair/handoff/
    engineering report contracts, [scenario specifications](../../tests/behavioral/implement/scenarios.md)
    and [bounded forward evidence](../evidence/implement/forward-trials.md).

18. [Review entry](../../src/kiyo/skills/review/SKILL.md),
    [procedure](../../src/kiyo/workflows/review.md),
    [severity/confidence](../../src/kiyo/framework/review-severity-confidence.md),
    [finding](../../src/kiyo/templates/reports/review-finding.md) and
    [report](../../src/kiyo/templates/reports/review-report.md),
    [scenario specifications](../../tests/behavioral/review/scenarios.md) and
    [bounded forward evidence](../evidence/review/forward-trials.md).

Prompts 10–14 do not refresh external research; retain each source's recorded date.
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

Prompt 10 adds three shared evidence/DoD/reporting contracts, seven neutral report
templates, four controls (58 total) and 20 synthetic good/bad scenario specifications.
Status: **DONE** for the requested static scope; checks passed using nine-field
records in [Prompt 10 evidence](BASELINE.md#prompt-10-checks).
Authored reports and parsed scenarios do not prove agent behavior, test execution,
complete access visibility or a tamper-proof audit trail.

Prompt 11 authors canonical Init (name init; logical ID kiyo.init), its full
procedure, discovery/activation/output references, context template and 16 scenario
specifications. Status: **DONE** for canonical authoring; scoped validation and
bounded source-guided trials are recorded in [Prompt 11 evidence](BASELINE.md#prompt-11-checks).
Entry frontmatter validation and a temporary 70-shared-file resource-copy/transform
check passed. This is neither a native prepared package nor automatic selection/
loading or universal behavioral acceptance.

Prompt 12 authors canonical Requirement (name requirement; logical ID
kiyo.requirement), a full shared procedure, fourteen-field template/readiness
checklist and twelve input/output scenario specifications. Status: **DONE** for
canonical authoring; [Prompt 12 evidence](BASELINE.md#prompt-12-checks) separates
frontmatter/static/resource checks, bounded source trials and native gaps.
Readiness labels in shared DoD/report guidance now match Prompt 12 exactly.

Prompt 13 authors canonical Implement (name implement; logical ID kiyo.implement),
a short plan and sixteen developer scenario specifications, extending the existing
shared implementation flow and reusing repair/handoff/report templates.
Status: **DONE** for canonical authoring; see [Prompt 13 checks](BASELINE.md#prompt-13-checks).
Source-guided fixture edits/checks are separately bounded from native or full-suite
acceptance. The entry follows all sixteen requested obligations at adaptive depth.

Prompt 14 authors canonical Review (name review; logical ID kiyo.review), a shared
procedure, severity/confidence guidance, a bounded review report and sixteen
developer scenarios, refining the existing finding template. Status: **DONE**
for canonical authoring; see [Prompt 14 checks](BASELINE.md#prompt-14-checks).
Static source/resource checks and bounded read-only fixture trials are separate
from full-matrix/native acceptance; four public skills remain pending.

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
REQ-031/036/037/038 newly partial.
Prompt 10 adds partial shared contract/template coverage for REQ-039–046/049/077
and updates REQ-080. Current totals: 65 PARTIALLY_IMPLEMENTED / 15 NOT_IMPLEMENTED;
REQ-043 newly partial.
Prompt 11 adds partial Init entry/procedure coverage for
REQ-009/014–017/020/024/026/027/068 and updates REQ-080. Current totals:
67 PARTIALLY_IMPLEMENTED / 13 NOT_IMPLEMENTED; REQ-026/068 newly partial.
Prompt 12 adds partial Requirement instruction coverage for
REQ-016/023/026/027/031/032/043/044/069 and updates REQ-080. Current totals:
68 PARTIALLY_IMPLEMENTED / 12 NOT_IMPLEMENTED; REQ-069 newly partial.
Prompt 13 adds partial Implement instruction coverage for
REQ-015/023/026/027/029/030/033–035/039/040/044/049/070 and updates REQ-080.
Current totals: 69 PARTIALLY_IMPLEMENTED / 11 NOT_IMPLEMENTED; REQ-070 newly partial.
Prompt 14 adds partial Review instruction coverage for
REQ-023/027/028/040/041/044/071/077 and updates REQ-080.
Current totals: 70 PARTIALLY_IMPLEMENTED / 10 NOT_IMPLEMENTED; REQ-071 newly partial.
All full requirement verifications remain NOT_RUN; source trials cover only
their recorded fixtures, not the complete scenario matrix or six native targets.

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
  skill locations. Prompt 03 defines the architecture below; Prompt 11 checks temporary
  source-resource relocation, while native cache reads/lifecycle remain untested. Absolute author checkout paths are not portable.
- ISO 12207 baseline is 2026 edition 2; 29148:2018 has a DIS replacement in
  development. SSDF 1.1 is final and 1.2 is draft. AST v1 is public review.
  ISO mappings are concept-level only; 38507/27034/SAMM supporting; 5338 only for
  actual AI-system development. No certification or invented clause mapping.

Open decisions: DEC-001 name/identifiers, DEC-002 release-license confirmation,
DEC-003 publisher/account/destination, DEC-004 unsupported IDE route.
They do not block the next Test skill authoring scope under the selected architecture; they do block
dependent release identities, claims or unapproved fallback choices.

Memory Impact: **NONE for developer project memory**. Build continuity/specification
choices are recorded in docs/build; no repository .kiyo/memory was initialized or
changed. Temporary synthetic fixture state is recorded separately in forward evidence.

## Architecture and Core decisions to retain

- Product source is `src/kiyo/`: compact `KIYO.md`, core `framework/`, policy
  `governance/` and `agent-security/`, shared `workflows/`, optional `profiles/`,
  neutral `templates/`, exactly eight planned `skills/<name>/SKILL.md` entries.
  Core now includes the Memory specification and shared lifecycle; eight neutral
  Memory templates and governance policies/shared review procedure now exist.
  Agent-security references and four optional governance-record templates also
  exist, together with five router/flow references, six engineering standards plus
  selection/mapping, four profiles/extension contract, three evidence/DoD/reporting
  contracts and eight report templates. Init now has its canonical entry, full
  procedure/references and a project-context template. Other workflows/templates
  and the remaining four public skills remain unimplemented. Requirement now adds a
  canonical entry, shared procedure/readiness checklist and neutral template.
  Implement now adds its canonical entry, short plan and integration with existing
  implementation/repair/handoff/report references. Review adds its entry/shared
  procedure, severity/confidence guide and bounded report, refining finding fields.
  Do not mistake synthetic scenarios for executed behavior.
- Core IDs use `KIYO-<DOMAIN>-<NNN>`, independent of standard clauses. The actual
  62-control index points to canonical definitions (16 Core, six Memory, nine
  governance, ten security, six routing/flow, seven engineering/profile, four
  evidence/completion/reporting IDs, one Init ID, one Requirement ID, one Implement ID and one Review ID). ACTIVE means authored, not
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

## Shared boundaries for Prompt 15

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
All 20 Memory scenarios remain NOT_RUN. Init now has a separate canonical entry
and bounded source trials; the public Memory skill remains pending.

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
cases remain NOT_RUN; no native route has been implemented or verified.

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

Evidence records always carry Name, Applicability, Command/method, Inspected
scope, Execution status, Observed result, Evidence location, Limitations and
Baseline relation. Use only PASS/FAIL/NOT_RUN/NOT_APPLICABLE/BLOCKED. N/A requires
a real scope reason, never missing environment. Commands/counts/times/versions
need real observations; test creation is not execution and old PASS cannot
certify later affected edits. Preserve baseline failures and Unknown attribution.

DoD is workflow-specific: Implement needs agreed behavior/AC, valid approvals,
current required verification, scope/security/governance self-review and assessed
Memory Impact with mandatory sync completed. Missing required evidence/sync is
partial/blocked, never silently optional. Read-only review or bounded security/
memory assessment completion is not bug-free/secure/certified/whole-project proof.
Requirement delivery and implementation readiness differ. Use the exact values
READY_FOR_IMPLEMENTATION, DECISION_REQUIRED or INSUFFICIENT_EVIDENCE from the
Requirement checklist; they do not authorize implementation.

Reports convey task/scope, actual actions/files, governance/risk rationale,
verification/evidence, residual issues, Memory Impact, one actual task status and
next required action. Select the appropriate neutral template; chat is default and
disk output requires actual write scope. Preserve human content and approval/
repair history. No secrets/raw logs/private reasoning, guessed provider/model/
access counts, independent-audit or tamper-proof claims. All 20 good/bad scenarios
are NOT_RUN and explicitly synthetic; static checks do not execute them.

Init has canonical name init and logical ID kiyo.init; the latter is not a
universal native selector or metadata field. It handles requested onboarding,
initial analysis, Memory creation/update and readiness inspection; never every
feature request. Preview/readiness is read-only. Writes are only necessary
authorized local Kiyo Memory/config/managed bootstrap; no app source/dependencies/
tests/global/credentials or Git initialization, builds, migrations and installs.

Discover root/current Git/human state and existing canonical paths first.
Sample at most 16 project text files / 1,200 inspected lines initially across
the chosen scope, with justified targeted expansion; authority discovery cannot
be replaced by guesses. Preserve legacy index/config, monorepo scope, entry IDs,
approved intent and concurrent human edits; no-delta means no timestamps touched.
Default .kiyo/memory and .kiyo/policy.md apply only to a new unconfigured authorized
project. Empty repositories stay stack Unknown and get no application scaffold.

Managed bootstrap needs a necessary evidenced native facility and valid write
scope. The neutral init-locator-1 shape is not a native adapter or product version.
Preserve existing AGENTS.md/CLAUDE.md/Copilot human sections; reconcile changed or
ambiguous blocks, never overwrite wholesale. Use project-relative state locators,
not a cache path or a copied Core. Report separate native/explicit/agent-directed/
project-guidance/automatic-loading evidence. Unsupported/Unknown auto-load
does not justify hooks or a guessed command. Source trials/resources checks
are separate from scenario-suite/native success; see the evidence record.

Requirement has canonical name requirement and logical ID kiyo.requirement.
Raw requests/issues/documents/proposals become fourteen-field engineering requirements.
First inspect authorized Memory and relevant current repository evidence; technical
facts do not decide business permissions. Separate Existing facts, User requirements,
AI proposals and Unresolved decisions. Ask only material blocking choices with
known facts/options/tradeoffs; never repeat complete inputs or invent HTTP/retention.
Preserve stale Memory/approved intent and report impact without syncing.

Default output is chat. Specification-file writes require an actually requested/
approved path and immediate reread/human-edit preservation. No source/tests/config/
Memory/global writes or application execution. Reuse real IDs; a response-local
provisional draft label is not project allocation. All fourteen fields must be
addressed; unknown/non-applicability has a reason. Use proportionate detail.

Readiness and task completion are independent. A requested draft may be DONE
with DECISION_REQUIRED/INSUFFICIENT_EVIDENCE; a requested ready specification cannot
be called complete with material blockers. Even READY_FOR_IMPLEMENTATION does not
launch Implement, run tests or create approval. Twelve scenario specifications
remain NOT_RUN as a full matrix; bounded source trials are separately recorded.

Implement has canonical name implement and logical ID kiyo.implement. Require
actual intent to change code; review/analyze-only requests stay read-only even
when this entry is selected. Capture permitted baseline/human edits before
mutation, validate relevant Memory, resolve material behavior/AC unknowns and use
existing safe patterns. Tiny work needs compact scope/checks, not a plan file.

Assess dependency/schema/API/security/data/command effects. Reuse valid matching
authorization; ask only missing policy-defined scope. Auth/schema is not a keyword
blanket allow/block. Migration drafting is separate from applying, and production
DB access is never a fallback to make checks pass. Inspect scripts/targets first;
add meaningful necessary tests using actual project conventions.

Keep current check evidence and baseline/new/environment/unknown distinctions;
recheck after affected edits. Repair is bounded by the shared two unsuccessful
cycle default, with reassessment for scope changes and no counter reset. Review
diff/requirements/architecture/quality/security/governance, assess Memory Impact
and sync only necessary authorized records after rereading. Preserve approved
decisions and no-delta timestamps. No implicit commit/push/PR/deployment.
Report honest DoD status with existing engineering/compact or handoff templates
in chat by default. Sixteen Implement specifications remain NOT_RUN as a complete
matrix; bounded actual source trials do not establish native behavior.

Review has canonical name review and logical ID kiyo.review. It inspects existing
changes/files/ranges/accessible PR context and reports in chat. No range means
actual current workspace, with staged/unstaged/untracked scope explicit; no guessed
default branch or unrelated history. Zero diff means no changes found in that
scope; explicit unchanged-file review remains possible. A missing required base
blocks the comparison, without fetch or silent fallback.

Inspect relevant Memory and verify claims against actual evidence. Check effective
registration/guards/callers before an authz conclusion; policy existence alone
does not establish protection. Distinguish Confirmed defect, Plausible risk and
Improvement suggestion. Each finding carries severity, confidence with basis,
actual location/view, observed behavior, impact, sourced requirement/control,
proposed fix and verification idea. Static certainty is not runtime reproduction.

Review does not edit source/tests/Memory, save reports by default, install packages
or mutate Git. Build/test/scan/project execution requires a separately established
scope and effect preflight; a label of review/test grants no execution. Reuse real
matching authorization; copied approvals and found bugs cannot expand it.
Redact sensitive data/paths, preserve human edits and state uncertain attribution.
Report all eight shared fields, check status and Memory Impact without syncing.
DONE means agreed inspection delivered, not fixes or production readiness.
Sixteen Review cases remain NOT_RUN as a full matrix; bounded actual variants
and immutable fixture snapshots are recorded separately.

## Exact next action

Prompt 14 is complete within its canonical Review authoring scope; stop here.
**Next: Prompt 15 Test**, only when supplied by the user. Recheck repository
and read the files above; implement only that prompt's actual Test skill scope,
reusing shared assessment/execution/evidence contracts. Preserve read-only Review
boundaries and source-trial versus native evidence.
Do not infer authorization for developer-project initialization, other skills,
dangerous operations, publication or unverified native overlays/activation.

Safe to continue: **YES for a user-requested Prompt 15 Test**.
Shared contracts and four authored skill patterns are ready; native/owner gaps
remain gates for dependent packaging/activation/publication claims.

