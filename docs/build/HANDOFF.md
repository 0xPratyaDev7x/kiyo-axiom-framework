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

Observed for Prompt 03, initial inspection 2026-09-28 and closure 2026-09-29:

- Root: C:/Users/praty/source/@0xPratya7x/kiyo-codejadee-framework/kiyo-codejadee-framework
- Branch: main; HEAD: 64b2b8b05e79e8fe23aee78c7fa7ed09b4ee68fd.
- Initial working tree and index clean; tracked LICENSE, eight build files and
  five research/compatibility files. Prompt 02 was committed before this work;
  previous checkout/HEAD/uncommitted snapshots are historical, not current facts.
- No applicable AGENTS.md found in repository or checked ancestors; no .kiyo
  project/product memory present.
- Git used a per-command safe.directory override for this exact root;
  global settings were not changed.
  An unreadable global ignore warning was resolved for inventory by the
  per-command empty core.excludesFile setting.
- LICENSE blob remains d2e60c5b160ed4f9ca096215e72efee5769936b1.
- No product version file, manifest or Git tag found in the scoped inventory.
- Prompt 03 creates six Markdown files and changes six build records. No commits,
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

No native Kiyo manifest, public skill or core has been implemented. No native
version, account availability or installed-tool absence is inferred from the
assistant session. Each of Claude CLI, Claude VS Code, Codex CLI, Codex IDE,
Copilot CLI and Copilot VS Code remains **NOT_TESTED** live.

Research-documentation implementation is partial for REQ-004/005/010/056/057/067;
REQ-080 continuity remains partial. Other cited IDs receive research/design inputs
only; Prompt 03 does not promote architecture into implemented product controls.
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
They do not block Core authoring under the selected architecture; they do block
dependent release identities, claims or unapproved fallback choices.

Memory Impact: build continuity only. No .kiyo/memory initialized or changed.

## Architecture decisions Prompt 04 must retain

- Product source is `src/kiyo/`: compact `KIYO.md`, core `framework/`, policy
  `governance/` and `agent-security/`, shared `workflows/`, optional `profiles/`,
  neutral `templates/`, exactly eight `skills/<name>/SKILL.md` entries. Only the
  source README exists today; do not assume the planned files are implemented.
- Core IDs use `KIYO-<DOMAIN>-<NNN>`, independent of standard clauses. Prompt 04
  defines the actual controls/index; this prompt only selected the ID convention.
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
- Architecture sets word ceilings: native Kiyo adapter block 250, KIYO.md 600,
  selected SKILL.md 1,200. These are design budgets, not measured tokens or
  proven host limits. Product templates cannot carry this developer repo's facts.
- Do not generate manifests, public skills, release versions or all later trees
  to make scaffolding look complete. Keep schema gaps and owner decisions open.

## Exact next action

Prompt 03 is complete; stop after its closing report.
**Next: Prompt 04 Core**, only when the user supplies it. Recheck the repository
baseline and read the files above. Implement only that prompt's Core scope in
the selected canonical structure, with stable controls and compact bootstrap;
do not infer authorization for memory, skill, overlay or generator implementation.

Safe to continue: **YES for requested Prompt 04 Core**. Architecture and scoped
documentation checks are complete. Native schema guesses, publication, fallback
acceptance and live support claims remain outside scope.

