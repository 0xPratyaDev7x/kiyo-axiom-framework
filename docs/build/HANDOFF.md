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

Observed for Prompt 02 on 2026-09-28:

- Root: C:/Users/praty/source/@0xPratya7x/kiyo-codejadee-framework/kiyo-codejadee-framework
- Branch: main; HEAD: aa843a5c690d232d110c744eaecf30997c233908.
- Initial working tree and index clean; tracked LICENSE and eight Prompt 01 build
  files. Prompt 01 records were committed before this session; prior handoff's
  checkout path and uncommitted snapshot are historical, not current facts.
- No applicable AGENTS.md found in repository or checked ancestors; no .kiyo
  project/product memory present.
- Git initially refused sandbox ownership. A per-command safe.directory override
  for this exact root allowed read-only checks; global settings were not changed.
  An unreadable global ignore warning was resolved for inventory by the
  per-command empty core.excludesFile setting.
- LICENSE blob remains d2e60c5b160ed4f9ca096215e72efee5769936b1.
- Prompt 02 creates five Markdown files and changes six build records. No commits,
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

No native Kiyo manifest, public skill or core has been implemented. No native
version, account availability or installed-tool absence is inferred from the
assistant session. Each of Claude CLI, Claude VS Code, Codex CLI, Codex IDE,
Copilot CLI and Copilot VS Code remains **NOT_TESTED** live.

Research-documentation implementation is partial for REQ-004/005/010/056/057/067;
REQ-080 continuity remains partial. Other cited IDs receive research inputs only.
All full requirement verifications remain NOT_RUN.

## Findings Prompt 03 must retain

- Codex IDE plugins are **UNSUPPORTED** by current official documentation;
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
  skill/plugin locations. Bootstrap ownership/update/uninstall behavior needs
  architecture; absolute author checkout paths are not portable.
- ISO 12207 baseline is 2026 edition 2; 29148:2018 has a DIS replacement in
  development. SSDF 1.1 is final and 1.2 is draft. AST v1 is public review.
  ISO mappings are concept-level only; 38507/27034/SAMM supporting; 5338 only for
  actual AI-system development. No certification or invented clause mapping.

Open decisions: DEC-001 name/identifiers, DEC-002 release-license confirmation,
DEC-003 publisher/account/destination, DEC-004 unsupported IDE route.
They do not block architecture for documented capabilities; they do block
dependent release identities, claims or unapproved fallback choices.

Memory Impact: build continuity only. No .kiyo/memory initialized or changed.

## Exact next action

Stop after Prompt 02's closing report. **Next: Prompt 03 Architecture**, only when
the user supplies it. Start by rechecking repository state and reading the files
above. Define canonical structure and overlay/bootstrap/resource boundaries using
documented capabilities, with unsupported/unknown decisions left explicitly
gated. Do not execute Prompt 03 from this handoff alone.

Safe to continue: **YES for requested Prompt 03 Architecture**. Research and
documentation checks are complete. This is limited to architecture of documented
surfaces, not schema guesses, release, installation or live support claims.

