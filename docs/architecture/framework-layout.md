# Kiyo Compass — Canonical framework layout

Decision date: **2026-09-29**. Status: architecture selected for this build in
[ADR-001](decisions/ADR-001-static-canonical-packages.md); product implementation
and package execution remain pending. Kiyo Compass is a working name.

## Inputs and evidence boundary

This design implements the structure requested in Prompt 03 under the
[Build Contract](../build/BUILD-CONTRACT.md) and
[requirements](../build/REQUIREMENTS.md), especially REQ-002/003/006/014/017,
REQ-025–027/037/054/076–080. Native facts come from the Prompt 02
[capability matrix](../compatibility/platform-capabilities.md),
[activation research](../compatibility/activation-modes.md) and
[source register](../research/SOURCES.md), checked **2026-09-28**.
Those facts remain DOCUMENTED_ONLY, UNKNOWN or UNSUPPORTED as recorded;
all six live targets remain NOT_TESTED. Prompt 03 adds design decisions, not
a fresh external-source check or a successful installation.

## Five ownership boundaries

| Boundary | Authoritative location | Ownership and lifetime | Installed? |
| --- | --- | --- | --- |
| Product content | `src/kiyo/` | Maintainer-authored, versioned, immutable within a released bundle | Selected product files and generated resource copies |
| Project-local state | Consumer repository's existing canonical memory/policy paths; new defaults below | User/project owned; mutable only with applicable authorization | Never part of a plugin payload |
| Platform overlays | `platforms/claude/`, `platforms/codex/`, `platforms/copilot/` | Maintainer-authored native metadata and instruction adapters | Only resulting host-required metadata/adapter content |
| Developer material | `docs/`, `tools/`, `tests/` and source scaffold README | Maintainer research, decisions, build/test/release tooling and redacted evidence | Excluded from consumer payload |
| Generated distributions | `dist/<ecosystem>/` | Disposable derivatives of canonical content plus an overlay; never hand-edited | The native package contained here |

Project policy is distinct from a shipped policy template. A template describes
fields; a populated policy identifies the user's owner, authority, constraints
and decisions. The latter cannot flow back into a general release.

## Intended tree

Prompt 03 planned the tree below. Prompt 04 implements `KIYO.md` and the shared
Core files indexed in [control-index](../../src/kiyo/framework/control-index.md),
plus expected response examples. Prompt 05 adds the Memory specification,
shared lifecycle and eight templates, with developer-only scenario specifications.
Prompt 06 adds nine governance policies, the shared Governance Review procedure
and 18 expected decision examples under governance/; no policy engine is added.
The README remains developer-only. Remaining
product, overlay, tool, test and distribution paths are **planned**, not features.
Create each directory when it receives real scoped content; no empty SKILL.md,
dummy manifests, .gitkeep forest or initial version is required in Prompt 03.

```text
src/kiyo/
  README.md                       authoring boundary; excluded from payload
  KIYO.md                         compact product bootstrap
  framework/                      core controls, authority, context, memory protocol
    control-index.md              stable Kiyo control ID register
  governance/                     shared advisory policies and Governance Review
  agent-security/                 trust boundaries, Skill Audit and Self-check
  workflows/                      Workflow Router and engineering procedures
  profiles/                       optional stack/company guidance
  templates/                      neutral memory/policy/report/artifact templates
  skills/
    init/SKILL.md
    requirement/SKILL.md
    implement/SKILL.md
    review/SKILL.md
    test/SKILL.md
    security/SKILL.md
    architecture/SKILL.md
    memory/SKILL.md
platforms/
  claude/                         Claude manifest/frontmatter/project adapter sources
  codex/                          supported Codex metadata; IDE gap retained
  copilot/                        common metadata plus explicit CLI/VS Code differences
docs/
  architecture/decisions/          architecture decision history
  build/                          requirement traceability and build continuity
  research/                       dated sources/standards, not normative runtime input
  compatibility/                  six independent target records
  evidence/                       future redacted check artifacts
tools/                            future developer-only validation/package/release tools
tests/
  static/                         future file/schema/reference/parity checks
  behavioral/                     future agent scenarios with controlled fixtures
  live/                           future six-target native checks
dist/                             future generated native bundles
```

`framework/` is the Core home; do not introduce a second `core/` specification.
The registry's older planned `core/` paths are historical proposals, resolved by
this architecture without renaming requirement IDs or rewriting their source text.
`KIYO.md` is an entry point, not a ninth skill or an executable router.

## Content responsibilities and allowed dependencies

| Content | Owns | References; never duplicates |
| --- | --- | --- |
| Core / `framework/` | Authority, evidence, scope, access-contract vocabulary, memory protocol, stable controls | Other core sections as needed; no native schema details |
| Policies / `governance/`, `agent-security/` | Kiyo governance/data/action policies, security review procedures and their limitations | Core IDs and relevant templates; no claim of host enforcement |
| Workflows | Routing, task sequence, repair limits, closure | Core, policies, applicable profiles and output templates |
| Profiles | Context-specific .NET/Angular/Python/PostgreSQL guidance and extension conventions | Shared engineering controls; no forced stack or default project facts |
| Templates | Neutral artifact structure and evidence/unknown fields | Stable IDs where useful; no embedded developer project knowledge |
| Skills | Intent, mode, read/write/execute contract, entry sequence and selected procedure | Bootstrap and shared procedure links; no eight copies of long rules |

There are exactly eight public skills listed in the tree. Workflow Router,
Governance Review, Skill Audit and Self-check are Markdown procedures/submodes.
They have no public SKILL.md, executable dispatcher, daemon or extra command.
All Kiyo access and approval contracts are advisory Markdown. Actual permissions
remain native host controls; overlays cannot elevate project text to system policy.

## Project-local state contract

For a **new, unconfigured consumer project**, the selected defaults are
`.kiyo/memory/` for durable memory and `.kiyo/policy.md` for project policy and
the optional repository-relative memory-location declaration. These are design
defaults, not files created by installation. Prompt 05 implements the
[Memory record format](../../src/kiyo/framework/memory-specification.md) and
[lifecycle](../../src/kiyo/workflows/memory-lifecycle.md) without initializing
project state. Project-policy template details remain for subsequent prompts.

Resolution occurs in the host agent's authorized read scope:

1. Inspect applicable existing project guidance/policy for an explicit canonical
   memory and policy location. Resolve relative to the declaring project file;
   establish repository/worktree identity before reading or writing.
2. Preserve an existing single store and its established path, including legacy
   `.kiyo/project/memory/` when actually used. Do not initialize a parallel default.
3. If declarations/stores conflict, report the candidates and ask only for the
   decision needed before dependent writes. Do not merge, migrate or choose by
   file timestamp. Missing/inaccessible evidence is UNKNOWN, not an empty project.
4. If none exists, an authorized Init may create the defaults and a small native
   project instruction block identifying them. Mere installation is not that authorization.
5. Re-read affected files before writes, preserve human edits and approved decisions,
   and scope branch/worktree/monorepo knowledge explicitly. No-change means no touch.

A native project instruction block points to the established project policy/memory
location using project-relative text. Existing guidance remains the locator when
it already declares an alternative; do not create competing locator records.
`.kiyo/` is not magically read by hosts. The
[loading contract](content-loading.md) describes the native adapter and skill's
explicit read instruction. Any legacy external location requires existing authority
and host access; it is never bundled or reached through a payload symlink.

Memory, populated policy, approvals and user reports never live in plugin cache,
`src/kiyo/`, `platforms/` or `dist/`. Native update/uninstall affects the bundle,
not ownership of project state. No Kiyo cleanup hook exists.

## Acceptance path and implementation boundary

The [packaging contract](packaging-contract.md#worked-reference-path) follows one
skill from its canonical bootstrap/shared rules through a neutral template to
an installed native payload. The [loading contract](content-loading.md) defines
what the agent reads; [naming and versioning](naming-and-versioning.md) defines
identity and maintenance. These documents specify the architecture; later
static, behavioral and live checks must establish that implemented files follow it.

Prompt 03's only source scaffold was [the authoring README](../../src/kiyo/README.md).
Prompts 04–06 add shared Core/Memory/governance content without exposing a callable skill. No consumer runtime dependency,
generator, MCP, hook, service, database, telemetry or Kiyo installer is introduced.
