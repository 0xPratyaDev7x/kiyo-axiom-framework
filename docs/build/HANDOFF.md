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

Observed for Prompt 23 on 2026-09-29:

- Root: C:/Users/praty/source/@0xPratya7x/kiyo-codejadee-framework/kiyo-codejadee-framework
- Branch main; HEAD 90880886cfb6ad895cefceb478314ea6c3a031a7. Initial tree/index
  clean; Prompt 22 committed before this task. No scoped instructions or .kiyo
  found. Git uses per-command exact safe.directory/core.excludesFile only.
- LICENSE blob d2e60c5b160ed4f9ca096215e72efee5769936b1 preserved; no version/tag.
  Canonical inventory remains 105 product files/68 controls/eight public entries.
- Only canonical framework/init-activation.md changed, for explicit scope,
  outdated-Core handling and block-only cleanup; 24 generated copies match it.
  Other canonical files, native overlays and original builders remain unchanged.
- Three development ZIPs in dist/archives contain 794/795/794 files. Two fresh
  builds match inventories and ZIP bytes. Current P23 inventory includes actual
  input/tool/output hashes and 456 independent target parity records.
  P20–22 inventories remain historical snapshots, not current attestations.
- Final test report has ten PASS rows and PKG-08 BLOCKED (Windows symlink creation
  error 1314). ZIP symlink rejection/regular-member checks pass. Cooperative source
  read isolation is not an OS sandbox; native POSIX execution is NOT_RUN.
- Python 3.11.9 / Windows-10-10.0.26200-SP0 observed. No native host/account/version
  was inspected in P23. All native behavior remains NOT_TESTED. Historical Codex
  ingestion FAIL and IDE UNSUPPORTED remain unresolved.
- No user bootstrap/policy/Memory, global setting, install, dependency, runtime,
  commit/tag/push/PR, signature or publication was created.

Recheck root/branch/user edits on resume. Preserve LICENSE and all 80 requirements.
See [packaging checks](../evidence/packaging/package-checks.md) for exact limits.

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

19. [Test entry](../../src/kiyo/skills/test/SKILL.md),
    [procedure](../../src/kiyo/workflows/test.md),
    [mode/safety matrix](../../src/kiyo/framework/test-mode-safety.md),
    [plan](../../src/kiyo/templates/test-plan.md) and
    [report](../../src/kiyo/templates/reports/test-report.md),
    [scenario specifications](../../tests/behavioral/test/scenarios.md) and
    [bounded forward evidence](../evidence/test/forward-trials.md).

20. [Security entry](../../src/kiyo/skills/security/SKILL.md),
    [procedure](../../src/kiyo/workflows/security.md),
    [submode checklists](../../src/kiyo/agent-security/security-submodes.md),
    [finding](../../src/kiyo/templates/reports/security-finding.md) and
    [self-check report](../../src/kiyo/templates/reports/self-check-report.md),
    [scenario specifications](../../tests/behavioral/security/scenarios.md) and
    [bounded forward evidence](../evidence/security/forward-trials.md).

21. [Architecture entry](../../src/kiyo/skills/architecture/SKILL.md),
    [procedure](../../src/kiyo/workflows/architecture.md),
    [observation](../../src/kiyo/templates/reports/architecture-observation.md),
    [impact](../../src/kiyo/templates/reports/architecture-impact-report.md) and
    [shared drift report](../../src/kiyo/templates/reports/memory-architecture-drift-report.md),
    [scenarios](../../tests/behavioral/architecture/scenarios.md) and
    [bounded forward evidence](../evidence/architecture/forward-trials.md).

22. [Memory entry](../../src/kiyo/skills/memory/SKILL.md),
    [mode definitions](../../src/kiyo/framework/memory-modes.md),
    existing [lifecycle](../../src/kiyo/workflows/memory-lifecycle.md),
    [diff](../../src/kiyo/templates/reports/memory-diff.md),
    [sync](../../src/kiyo/templates/reports/memory-sync-report.md) and
    [repair](../../src/kiyo/templates/reports/memory-repair-report.md) templates,
    [skill scenarios](../../tests/behavioral/memory/skill-scenarios.md) and
    [bounded forward evidence](../evidence/memory/forward-trials.md).

23. [Project configuration](../../src/kiyo/framework/project-configuration.md),
    [policy resolution](../../src/kiyo/governance/policy-resolution.md),
    [presets](../../src/kiyo/governance/presets.md),
    [organization](../../src/kiyo/templates/policies/organization-policy.md) /
    [project](../../src/kiyo/templates/policies/project-policy.md) templates and
    extended [Init context](../../src/kiyo/templates/init/project-context.md),
    [scenarios](../../tests/behavioral/organization-policy/scenarios.md) and
    [bounded evidence](../evidence/organization-policy/forward-trials.md).

Prompts 10–19 do not refresh external research; retain each source's recorded date.
Prompt 02 native checks and unrefreshed standards remain dated 2026-09-28.
Prompt 09 rechecked S01–S07 and added E01–E06 on 2026-09-29; public documentation
only, not licensed ISO text or actual stack verification. Prompt 07
rechecked AST/ASVS and the separate ASI announcement on 2026-09-29; see SOURCES.
Revalidate volatile schema details before
implementing native packages; use native references, not old chat, local skill
scaffolds or the OWASP proposed universal format.

24. [Claude package field map](../compatibility/claude-package.md),
    [overlay](../../platforms/claude/README.md),
    [offline evidence](../evidence/claude/package-checks.md),
    [installation protocol](../compatibility/claude-installation-test-protocol.md)
    and [integration specifications](../../tests/integration/claude/scenarios.md).

25. [Codex field/invocation map](../compatibility/codex-package.md),
    [overlay](../../platforms/codex/README.md),
    [offline/failed-ingestion evidence](../evidence/codex/package-checks.md),
    [disposable protocol](../compatibility/codex-local-test-protocol.md) and
    [submission requirements](../compatibility/codex-submission.md).

26. [Copilot field/target delta](../compatibility/copilot-package.md),
    [overlay](../../platforms/copilot/README.md),
    [offline evidence](../evidence/copilot/package-checks.md),
    [installation/lifecycle](../compatibility/copilot-installation.md),
    [disposable protocol](../compatibility/copilot-local-test-protocol.md) and
    [integration specifications](../../tests/integration/copilot/scenarios.md).

## Completed work and evidence

Prompt 22 prepares one 794-file static Copilot bundle for independently documented
CLI/VS Code targets: eight skills, canonical parity and contained resources.
Actual offline checks pass, including 4,964 links, identical relocation/no-op and
nine rejection cases. Full sample project block is 116 words, not a live trial.
Twenty specifications remain NOT_RUN per target. See [P22 checks](BASELINE.md#prompt-22-checks).
No canonical product or earlier artifact change, consumer runtime, fake catalog
or global install. Counts remain 79 partial / 1 not implemented, all 80 full
verifications NOT_RUN and six native results NOT_TESTED. Earlier summaries below
are historical prompt scopes, not new verification claims.


Prompt 21 completes requested development packaging/documentation: 795 Codex files
and eight entries from unchanged canonical content, contained resources, independent
OpenAI metadata/AGENTS adapter and eighteen NOT_RUN integration specifications.
Offline checks pass; the full local ingestion validator FAILs for three absent
owner fields. Registration/submission readiness is BLOCKED, not part of a fabricated
successful native trial. See [P21 checks](BASELINE.md#prompt-21-checks).
Current totals remain 79 PARTIALLY_IMPLEMENTED / 1 NOT_IMPLEMENTED and all 80
full verifications NOT_RUN. All six native targets are NOT_TESTED; Codex IDE
plugins remain UNSUPPORTED. Earlier prompt counts/scope summaries are historical.


Prompt 20 adds the first generated native artifact, for Claude only. It contains
eight entries and shared resources; offline source parity, 4,956 local links,
relocation, reproducibility and negative checks passed. Native validator NOT_RUN;
both Claude targets and all other targets NOT_TESTED. Sixteen new integration
cases remain NOT_RUN per host. See [P20 checks](BASELINE.md#prompt-20-checks).
Current totals are 79 PARTIALLY_IMPLEMENTED / 1 NOT_IMPLEMENTED; all 80 full
verifications remain NOT_RUN. Subsequent paragraphs preserve prior prompt scopes
and historical counts, not current completion claims.

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

Prompt 15 authors canonical Test (name test; logical ID kiyo.test), shared
procedure, assess/run/write mode/safety matrix and test plan/report templates,
plus eighteen developer scenarios. Status: **DONE** for canonical authoring; see
[Prompt 15 checks](BASELINE.md#prompt-15-checks). Actual bounded mode trials are
separate from static/source portability and complete behavioral/native acceptance.
Three public skills remain pending.

Prompt 16 authors canonical Security (name security; logical ID kiyo.security),
one entry with four logical submodes, a shared procedure/checklists and neutral
finding/self-check templates, plus eighteen developer scenarios.
Status: **DONE** for canonical authoring; see [Prompt 16 checks](BASELINE.md#prompt-16-checks).
Four bounded read-only source trials and resource checks are separate from
payload behavioral execution, full acceptance and native activation.
Architecture and Memory are the two remaining public entries.

Prompt 17 authors canonical Architecture (name architecture; logical ID
kiyo.architecture), its shared procedure/control, observation/impact templates and
extended shared drift report, plus sixteen scenario specifications.
Status: **DONE** for canonical authoring; see [Prompt 17 checks](BASELINE.md#prompt-17-checks).
Source/resource checks and bounded read-only assessments are distinct from
complete matrix/native acceptance, architecture adoption and production behavior.
Only the public Memory entry remains pending.

Prompt 18 authors canonical Memory (name memory; logical ID kiyo.memory), explicit
mode definitions, three neutral diff/sync/repair reports and eighteen additional
scenario specifications, reusing the existing shared lifecycle.
Status: **DONE** for canonical authoring; see [Prompt 18 checks](BASELINE.md#prompt-18-checks).
All eight canonical public entries are now authored without extra router,
governance or self-check skills. Bounded fixture writes/read-only/no-op checks are
not full behavioral acceptance, native catalogs or installed host validation.

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
Prompt 15 adds partial Test instruction coverage for
REQ-023/027/038/039/040/041/044/072/077 and updates REQ-080.
Current totals: 71 PARTIALLY_IMPLEMENTED / 9 NOT_IMPLEMENTED; REQ-072 newly partial.
Prompt 16 adds partial Security instruction coverage for
REQ-026/027/042/051/058/061/062/063/065/067/073 and updates REQ-080.
Current totals: 72 PARTIALLY_IMPLEMENTED / 8 NOT_IMPLEMENTED; REQ-073 newly partial.
Prompt 17 adds partial Architecture/shared instruction coverage for
REQ-019/022/023/024/026/027/028/033/040/044/074 and updates REQ-080.
Current totals: 73 PARTIALLY_IMPLEMENTED / 7 NOT_IMPLEMENTED; REQ-074 newly partial.
Prompt 18 adds partial Memory/shared instruction coverage for
REQ-017/018/019/020/021/022/023/024/026/027/040/044/075 and updates REQ-080.
REQ-075 already had partial shared content, so current totals remain
73 PARTIALLY_IMPLEMENTED / 7 NOT_IMPLEMENTED.
Prompt 19 extends partial configuration/policy coverage for
REQ-011/013/017/037/047/049/050/051/054/055/068/073 and updates REQ-080.
Totals remain 73 PARTIALLY_IMPLEMENTED / 7 NOT_IMPLEMENTED; REQ-054 was already partial.
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
Static Organization Policies authoring did not require these decisions. For
Prompt 20, hold only native metadata/publication or compatibility decisions that
depend on them; do not invent release identities or unapproved fallback choices.

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
  contracts and sixteen report templates. Init now has its canonical entry, full
  procedure/references and a project-context template. Remaining workflows/templates and native artifacts remain unimplemented. Requirement now adds a
  canonical entry, shared procedure/readiness checklist and neutral template.
  Implement now adds its canonical entry, short plan and integration with existing
  implementation/repair/handoff/report references. Review adds its entry/shared
  procedure, severity/confidence guide and bounded report, refining finding fields.
  Test adds its entry/procedure, mode/safety matrix and test plan/report.
  Security adds one entry with four submodes, shared procedure/checklists,
  finding/self-check templates and integration with the assessment report.
  Architecture adds its entry/procedure, observation/impact templates and the
  extended shared drift report; no automatic migration or record sync.
  Memory adds its entry/modes and diff/sync/repair reports using the shared
  lifecycle. All eight public entries now exist; native catalogs remain pending.
  Do not mistake synthetic scenarios for executed behavior.
- Core IDs use `KIYO-<DOMAIN>-<NNN>`, independent of standard clauses. The actual
  66-control index points to canonical definitions (16 Core, seven Memory, nine
  governance, eleven security, six routing/flow, seven engineering/profile, four
  evidence/completion/reporting IDs, one Init ID, one Requirement ID, one Implement ID, one Review ID, one Test ID and one Architecture ID). ACTIVE means authored, not
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

## Shared boundaries for Prompt 23

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
and bounded source trials; Memory now adds its canonical entry and explicit modes.

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

Test has canonical name test and logical ID kiyo.test. assess/run/write are
logical modes, not native parser arguments or permissions. Unclear intent resolves
or begins assess within read scope. Explicit multi-mode requests may authorize
writing and execution; reuse matching scope without another ceremonial approval.

assess inspects requirements/changes/tests/Memory and reports gaps in chat; it
does not run discovery/collection scripts or write files. run inspects commands,
helpers/hooks/config/environment and actual non-production targets before named
authorized checks/artifacts; it cannot repair tracked source/tests/config. write
limits edits to requested tests/test-only fixtures, preserving human changes
and existing tools; production changes, dependencies and config need separate scope.

Use relevant unit/integration/API/E2E/regression layers based on requirements and
project capability. Never invent business permissions/validation behavior, weaken
assertions, skip/delete failing tests or accept broken snapshots to turn green.
No production resources, exposed connection secrets or unapproved installation
of browsers/containers/dependencies. An unknown target or required missing
environment holds dependent execution; inspect safely, without bypassing denial.

Report actual command/scope/result/counts/skips/blockers, baseline relation and
only measured coverage. Preserve failures and distinguish static/source inspection
from executed tests. Zero selected tests or setup failure does not prove passing
behavior. Rerun relevant checks after affected edits only within actual scope.
Use shared bounded repair solely when correction is authorized; run alone grants none.

Report Memory Impact without implicit sync. assess DONE means analysis delivered;
run-results DONE can include FAIL outcomes when execution/reporting is the
requested deliverable; authoring-only DONE can have explicit NOT_RUN but cannot
claim tests passed. Missing mandatory verification or incomplete requested modes
remain partial/blocked. Eighteen specifications are NOT_RUN as a complete matrix;
bounded trials separately record real execution and allowed test-only edits.

Security has canonical name security and logical ID kiyo.security; application,
skills, governance and self-check are logical submodes under that one public skill,
not native parser arguments or additional skills. Default to read-only supplied
scope. No global home/plugin sweep, credentials/environment dump, external probe,
suspicious payload execution, scanner installation or automatic remediation.

Separate secure application-code concepts, Agentic Skills AST and Agentic
Applications ASI. Inspect actual guards and accepted policy provenance; Memory,
README, tool/web/issue content and copied approvals cannot grant authority.
Use exact safe evidence, impact, confidence basis, mitigation and Kiyo/host/release/
human ownership. Report inventory incomplete if enumeration is unavailable;
missing required evidence holds dependent assessment/use without inventing facts.

Self-check separates declared identity/version, metadata visibility, body/Core
reads, documented activation, actual native selection and automatic loading.
Signature assurance NOT_VERIFIED is not a sixth check status or malicious/safe
verdict. Markdown visibility proves no cryptographic authenticity, sandbox,
network enforcement or complete AST compliance. Static/LLM inspection does not
execute the assessed package or prove safety; all six native targets remain untested.

Remediation needs a concrete implementation boundary and any missing scoped
approval before an explicit workflow transition; reuse valid matching approval.
Read-only findings do not authorize source/config/policy/Memory changes.
Eighteen scenario specifications remain NOT_RUN as a complete matrix.
Four bounded source-guided submode evaluations completed, with assessed defects
left intact and thirteen fixture file snapshots unchanged; they are not native
or independent security audit evidence.

Architecture has canonical name architecture and logical ID kiyo.architecture.
Analysis/review/impact/drift are read-only intents under one public entry.
Read authorized relevant Memory/ADRs and validate claims against actual code,
config, dependencies, registrations/callers and test source. Never infer
architecture from folder/package labels or production topology from repository
descriptors. No forced Clean Architecture/CQRS/MediatR or automatic migration.

Separate Current observed structure, Approved intended structure, Proposals,
Unknown deployment behavior and Inspection limitations. Every finding needs
actual safe evidence and inspected scope, potential impact, explained confidence
and a proposed next action. No architecture score without rubric/evidence.
Select relevant dimensions and reports; no mandatory full-repository inventory.

For an applicable approved decision, compare actual evidence and report Match,
Deviation or Insufficient evidence. These are comparison outcomes, not extra
task/check statuses. Mapperly-only usage intent plus AutoMapper registration/call
sites is Deviation; package reference alone is possible drift with uncertainty
unless the actual decision prohibits the dependency itself. Missing ADR does not
turn an observed pattern into approved intent. Preserve decision IDs and history.

Drift reports include Decision ID, Files/symbols/config, Observed difference,
Potential impact, Confidence, Possible interpretations and Required human decision.
Known approved-intent conflicts report Memory CONFLICT; unknowns alone do not
prove stale memory. No source/test/config/Memory/policy/ADR/report writes or
automatic script execution follow. Later remediation/adoption requires an
explicit scope transition and applicable approval, reusing valid matching scope.
Sixteen scenario specifications remain NOT_RUN as a complete matrix; bounded
source evaluations and immutable fixture snapshots are separately recorded.

Memory has canonical name memory and logical ID kiyo.memory. show/check/sync/repair
are logical effects, not native commands/settings or additional skills. show
summarizes selected stored claims/freshness without pretending to revalidate;
check compares current authorized evidence and reports outcomes. Both write zero
files, including dates, statuses and report artifacts. Previews also write nothing.

Sync updates only necessary authorized observations/provenance and pointers;
repair handles scoped links/duplicates/structural inconsistencies. Preserve
canonical/legacy paths, IDs, observed dates, decisions/history and human sections.
No whole-folder rewrite, duplicate store, forced Init after manual edits, cache
Memory, secrets/PII/raw logs/private reasoning or redundant endpoint inventories.

Prepare an entry delta, separate factual corrections from Architecture Drift and
UNVERIFIED gaps, reuse real scoped authority and reread latest entry/index/human
text/evidence immediately before writes. Recompute safe non-overlapping edits;
hold ambiguous overlap, decision conflict or identity uncertainty. No timestamp
winner, old-snapshot overwrite, reset/stash or atomicity guarantee.

Last_modified reflects changed entries; last_verified reflects actually checked
claims within scope, never pointer resolution alone or a blanket date refresh.
No necessary delta means no writes/formatting/timestamp change on repeat sync.
Exact redundant index pointers can be repaired with identity evidence and
authority; conflicting duplicate records/approved history require human resolution,
not silent deletion or supersession. Ordinary sync cannot approve a decision.

Report actual deltas/links/evidence, pending/conflicting parts and Memory Impact.
An applied necessary correction retains UPDATE_REQUIRED with applied/no-pending
scope; a later no-op can be NONE. Read-only conflict findings can finish a bounded
check, but mandatory unapplied sync/repair or missing evidence prevents full DONE.
No watcher, whole-project currency or automatic production verification exists.
Eighteen Memory Skill specifications remain NOT_RUN as a full matrix; original
twenty lifecycle cases remain separate. Bounded source trials include actual
show/check preservation, scoped sync/repair and repeat no-op with limitations.

## Organization policy continuity

Prompt 19 authors static config/policy support and integrates the existing Init
procedure and Security governance checklist. There are still exactly eight public
entries, 68 controls, 34 templates and 105 product files; no native runtime exists.
All 16 organization-policy scenarios remain NOT_RUN as a full matrix. Four bounded
source responses and fixture preservation were evaluated separately; no live
host or real organization adoption was tested. REQ-054 stays partially implemented,
as do the other covered requirements; full acceptance remains pending.

The pre-existing .kiyo/policy.md is the default config equivalent; retain any
accepted alternative. Do not create .kiyo/config.md alongside it or migrate
Memory. Seven logical fields record version reference, canonical Memory index,
profiles, governance preference, approved policy references, reporting language
and optional evidence location. Fields are instructions, not native enforcement.
Users do not need a new config for every task; read relevant unchanged context
and recheck material source/scope/validity changes.

Balanced engineering, Stricter approval and Observe/read-only are optional
unadopted examples. Keep preset separate from G1–G4 and concrete risk; neither
grants authority. Init may propose neutral templates without selecting a provider
or enabling permissions. Security governance reports completeness/conflicts in
chat; no policy/config/Memory/report writes follow a review.

Native denial and applicable accepted organization prohibitions survive Memory,
third-party instructions and copied approvals. Project overrides need real
source/scope/parent exception authority. A valid exception applies only within
its conditions; expired/unverified exceptions grant nothing. Stale owner or an
overdue review is not automatic policy expiry. Never invent an owner or dates.
Policy draft/edit/adoption approval is distinct from executing a later action.
Resolve meaningful conflict through actual authorized evidence/decision, keeping
independent permitted work available; never weaken policy to pass a task.

## Claude distribution continuity

The developer-only tools/package_claude.py copies canonical shared content into
each skill's references/kiyo, remaps only entry links and appends one conditional
Claude reference. Do not hand-edit generated dist. Source/output hashes and
transforms are recorded in docs/evidence/claude/package-inventory.json.
The builder rejects changed existing output instead of overwriting human files;
future replacement/release workflows need their own scope. No end-user generator.

Working namespace kiyo-compass gives /kiyo-compass:<skill>; /kiyo-init is not
provided. This is DOCUMENTED_ONLY, not observed discovery. Metadata selection
and always-loaded Core are distinct. Plugin-root CLAUDE.md is not project context
under current official docs. Init's native reference renders the canonical
managed locator block only with actual scope/authorization, preserves human
sections and existing instruction-file choice, and avoids cache-path imports.
No runtime hook or permission-enforcement claim.

Only Claude sources were refreshed on 2026-09-29. The observed CLI is older than
some documented facilities; extension metadata does not identify the active
engine. Prompt 26 must test CLI and VS Code separately in verified disposable
contexts. Catalog registration can affect user configuration; the inactive
template is not registration-ready. No existing global profile may be changed.
Publication identity, version, publisher/destination and license confirmation
remain pending; custom source metadata does not establish curated listing.

## Codex distribution continuity

The prepared root is dist/codex/kiyo-compass. tools/package_codex.py reads canonical
content and platforms/codex/plugin.json, derives the compatibility manifest and
copies a distinct native adapter. It reuses only audited developer filesystem/
hash helpers from the existing packager, not Claude schema or product artifacts.
No consumer runtime/MCP/app registration exists. Optional agents/openai.yaml
was omitted because no invocation override/tool dependency/UI requirement needs it.

Use actual /skills/$ picker discovery; exact plugin-qualified Kiyo spelling remains
UNKNOWN. Metadata/relevance, selected Core reads and per-run AGENTS guidance
are separate. Minimal managed text reuses init-locator-1 and stays within actual
authorized module scope. Preserve AGENTS.md/nested/human content; never change
AGENTS.override.md/global config or broaden a module block to force Kiyo.
Static sample 108 words is not verified Init/loading behavior.

Current docs prefer portable manifests and retain compatibility support, but
public ingestion requires real version/author/developerName. The actual bundled
validator returns FAIL for exactly those missing values. Do not fabricate a
publisher or 0.1.0 release to make it pass. Owner inputs, supported catalog scope,
native behavior and portal review remain separate prerequisites. The inactive
catalog template has unresolved name/label and must not be registered.

Local CLI 0.158.0 help exposes plugin add/remove; marketplace upgrade refreshes
Git snapshots, not proven installed-payload replacement. No add/remove/upgrade/
list action or native session ran. Prompt 26 needs verified disposable state and
actual CLI results. IDE native plugins remain excluded by official docs; do not
silently substitute standalone/global skill installation. DEC-004 stays open.

## Copilot distribution continuity

dist/copilot/kiyo-compass is generated from canonical source and independent
platforms/copilot input. Only $schema/name/description are needed. No permission
or component-path fields, client extension, VSIX, hook, MCP or Actions runtime.
Existing file/hash helpers are reused unchanged; old native manifests are not inputs.
Source/output digests and actual Git base remain outside the installed payload.

CLI generic slash syntax does not establish the exact Kiyo namespace or resolve
built-in init/review collisions. Inspect actual discovery; do not substitute a
built-in or copy VS Code's /kiyo-compass:<skill> syntax into CLI. Both native
results remain NOT_TESTED. Plugin rules are not used as an unverified Core loader.

The adapter reuses canonical Init guidance, preserves .github/copilot-instructions.md,
human sections/path-specific globs and established config/Memory, and limits
module-only insertion to real applicable scope. File writes need actual
authorization and a fresh reread. No bootstrap was installed by this build.

No marketplace JSON with fake owner values is emitted. The lifecycle guide
separates direct cached CLI installs from local-catalog live paths and VS Code
source/UI/local routes. Future independent disposable tests must observe reads,
scope, update/disable/uninstall and preservation rather than reuse static success.
No curated listing, version, publisher, signature or ready-to-publish status.

## Packaging and parity continuity

Read [distribution build](../architecture/distribution-build.md),
[final checks](../evidence/packaging/package-checks.md),
[artifact inventory](../evidence/packaging/artifact-inventory.json),
[parity](../evidence/packaging/parity-report.md) and
[activation matrix](../compatibility/activation-matrix.md).

Edit canonical rules only in src/kiyo and native differences in platforms.
The wrapper creates ZIPs from current source, not stale dist content. Inventory
is outside payloads. Equal output is a no-op; differing output/inventory requires
a fresh destination and is never overwritten. No consumer tooling is shipped.

The existing init-locator-1 format now describes explicit authorized scope and
cleanup limits. Existing human blocks are not regenerated automatically.
Final test-results-final.json covers current bytes; test-results.json records
the earlier pre-clarification snapshot. Keep those evidence scopes distinct.
The real filesystem symlink probe remains BLOCKED; regular ZIP inventory,
symlink rejection and extracted reference checks support artifact containment.
Native Init/update/uninstall and actual target loading remain unverified.

## Exact next action

Prompt 23 scoped packaging/parity is complete. Stop here.
**Next: Prompt 24 Static Tests**, only when supplied by the user.
Recheck root/branch/user edits, read Build Contract and current evidence, then
execute only that prompt. Reuse tooling; preserve independent static/behavioral/
native evidence and historical failures. Do not invent release identity or IDE fallback.

Safe to continue: **YES for a user-requested Prompt 24 Static Tests**.
Artifacts and tests are concrete inputs; owner/native gaps block dependent
release/compatibility claims, not static work. Memory Impact: NONE.
No later work, installation or publication is authorized by this handoff alone.

