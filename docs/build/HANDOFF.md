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

Observed for Prompt 05 on 2026-09-29:

- Root: C:/Users/praty/source/@0xPratya7x/kiyo-codejadee-framework/kiyo-codejadee-framework
- Branch: main; HEAD: b05f709fcad6836aa1fecc84175c3143c6cc9792.
- Initial working tree and index clean; tracked LICENSE, eight build files and
  five research/compatibility files, six architecture documents, source README and
  seven Core files (27 Markdown files total). Prompt 04 was committed before this work;
  previous checkout/HEAD/uncommitted snapshots are historical, not current facts.
- No applicable AGENTS.md found in repository or checked ancestors; no .kiyo
  project/product memory present.
- Git used a per-command safe.directory override for this exact root;
  global settings were not changed.
  The per-command empty core.excludesFile setting kept inventory independent of
  unreadable global ignores.
- LICENSE blob remains d2e60c5b160ed4f9ca096215e72efee5769936b1.
- No product version file, manifest or Git tag found in the scoped inventory.
- Prompt 05 creates eleven Markdown files and changes twelve existing Markdown files. No commits,
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

All source checks are dated 2026-09-28. Revalidate volatile schema details before
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
memory was created. No native
version, account availability or installed-tool absence is inferred from the
assistant session. Each of Claude CLI, Claude VS Code, Codex CLI, Codex IDE,
Copilot CLI and Copilot VS Code remains **NOT_TESTED** live.

Research-documentation implementation is partial for REQ-004/005/010/056/057/067;
REQ-080 continuity remains partial. Other cited IDs receive research/design inputs
only; Prompt 03 does not promote architecture into implemented product controls.
Prompt 04 adds partial product Core instruction coverage recorded in TRACEABILITY;
completed instruction text does not imply completed skills or behavioral proof.
Prompt 05 adds shared Memory coverage; totals are 41 PARTIALLY_IMPLEMENTED and
39 NOT_IMPLEMENTED. REQ-068/074 have scenario inputs only; future skills are absent.
All full requirement verifications remain NOT_RUN.

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
They do not block the next Governance scope under the selected architecture; they do block
dependent release identities, claims or unapproved fallback choices.

Memory Impact: **NONE for project memory**. Build continuity/specification choices
are recorded in docs/build; no .kiyo/memory initialized or changed.

## Architecture and Core decisions to retain

- Product source is `src/kiyo/`: compact `KIYO.md`, core `framework/`, policy
  `governance/` and `agent-security/`, shared `workflows/`, optional `profiles/`,
  neutral `templates/`, exactly eight planned `skills/<name>/SKILL.md` entries.
  Core now includes the Memory specification and shared lifecycle; eight neutral
  Memory templates exist. Other workflows/templates and all public skills remain
  unimplemented. Do not mistake synthetic scenarios for executed behavior.
- Core IDs use `KIYO-<DOMAIN>-<NNN>`, independent of standard clauses. The actual
  22-control index points to canonical definitions (16 Core plus six new Memory IDs). ACTIVE means authored, not
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

## Core and Memory boundaries for Prompt 06

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

## Exact next action

Prompt 05 is complete; stop after its closing report.
**Next: Prompt 06 Governance**, only when supplied by the user. Recheck the
repository and read the files above, then implement only that prompt's governance
scope under actual native authority and the established Core/Memory contracts.
Do not initialize developer-project memory or infer authorization for native
overlays, public skills, generators or release work.

Safe to continue: **YES for requested Prompt 06 Governance**. Shared Memory
content and scoped static checks are complete. Publication, unsupported native
routes and live support claims remain outside scope; await its user prompt.

