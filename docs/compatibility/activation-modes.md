# Kiyo Compass — Activation and resource loading

Checked: **2026-09-28**. Official source IDs:
[SOURCES](../research/SOURCES.md). Capability evidence is **DOCUMENTED_ONLY**;
all live activation, relocation and maintenance checks are **NOT_TESTED**.
Kiyo remains advisory and static.

## Installation is not core loading

Skill hosts use progressive disclosure: discover metadata, select a relevant
skill, read its instructions, then read referenced resources as needed.
C02, O02/O05, G03 and V02 document these stages for their respective hosts.
None demonstrates that installing a skills-only Kiyo plugin reads every core
file at the start of every task. The Codex IDE plugin route is explicitly
UNSUPPORTED (O04). Checked 2026-09-28; limitation: no runtime loading trace.

A skill can explicitly instruct the agent to read its packaged core before
performing its workflow. That is a proposed advisory procedure, not a new native
auto-loader or enforcement mechanism. Whether it is followed must be evaluated
behaviorally and in each host.

## Activation modes

| Mode | What activates it | Project bootstrap needed? | Evidence / checked / limit |
| --- | --- | --- | --- |
| Explicit skill | User selects native command/mention | No separate bootstrap for discovery on supported plugin surfaces; skill can read packaged core | C02/O05/G03/V02, 2026-09-28; install/enablement and readable resources still required. |
| Implicit skill | Host matches prompt to skill metadata | Not inherently; matching can work from installed skills alone | C02/O02/O05/G03/V02, 2026-09-28; model choice, metadata budget, policy and collisions can prevent it. |
| Persistent project guidance | Host discovers project instruction files | Yes for the proposed project-guidance mode, unless an already-authorized native user/organization instruction supplies equivalent guidance | C03/O03/G04/V03, 2026-09-28; Kiyo installation itself is not evidence this setup occurred. |
| Plugin-shipped rules | Host-specific rule component | Potential alternative on Copilot, but bootstrap replacement decision **UNKNOWN** | G01/V01, 2026-09-28; directory support documented, complete activation/precedence semantics not established. |
| Guaranteed automatic governance | Claimed execution on every relevant task | Not established by either bootstrap or skills | Build Contract plus source limits above; 2026-09-28; no Kiyo runtime/enforcement exists. |

Automatic **selection** therefore need not rely on project bootstrap. Consistent
project-wide **guidance** needs an explicit native loading arrangement. These
claims must remain separate; neither is a guarantee of agent compliance.

## Project loading boundaries per target

| Target | Candidate native project entry point | Loading facts / limits | Source / checked |
| --- | --- | --- | --- |
| Claude Code CLI | `CLAUDE.md` / `.claude/CLAUDE.md`, project `.claude/rules/` | Project guidance distinct from skills; plugin-root CLAUDE.md not loaded. Rules without paths load at launch; scoped rules conditional. | C03/C07, 2026-09-28 |
| Claude Code VS Code | Same Claude project mechanisms in extension session | C05 establishes shared engine/settings, not a tested workspace/remote loading result. | C05/C03/C07, 2026-09-28 |
| Codex CLI | `AGENTS.md` / `AGENTS.override.md` | Once-per-run discovery, global then root-to-CWD; default 32 KiB cap. No documented automatic expansion of arbitrary Markdown links. | O03, 2026-09-28 |
| Codex IDE Extension | Native Codex AGENTS guidance plus standalone skills | Project guidance can exist while plugin capability is unsupported; fallback does not satisfy native-plugin requirement. | O03/O04/O05, 2026-09-28 |
| GitHub Copilot CLI | `.github/copilot-instructions.md` / `AGENTS.md` | Supported `@relative-file` includes are read immediately, remain inside repository/instruction root. General file precedence not defined. | G04, 2026-09-28 |
| GitHub Copilot VS Code | `.github/copilot-instructions.md` / `AGENTS.md` | Selected harness determines discovery. Targeted instructions use applyTo/relevance; Local settings differ. Markdown paths resolve from instruction file. | V03, 2026-09-28 |

**Prompt 03 design proposal, not implemented:** Init can prepare a small,
reviewable project bootstrap using the host's native entry point and
project-local canonical guidance. Preserve existing instructions and record
source/version/update ownership. Avoid a stale absolute cache reference or a
second unmanaged copy of core. Decide copy/reference/update policy in
architecture; no project/global instruction file is written in Prompt 02.

## Resources after installation or cache relocation

| Target | Documented resolution mechanism | Safe static candidate / limitation | Source / checked |
| --- | --- | --- | --- |
| Claude Code CLI | Manifest paths relative to plugin root; skill body supports `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_SKILL_DIR}` | Package shared core within plugin root; expansion can locate it after versioned cache move. No hardcoded checkout/cache path. | C02/C04/C07, 2026-09-28; relocation NOT_TESTED |
| Claude Code VS Code | Claude plugin engine's same resource mechanism | Test independently in extension and any remote environment; don't use user's local absolute path. | C05/C02/C07, 2026-09-28; remote availability UNKNOWN |
| Codex CLI | Portable fixed skills directory; skill-root relative references; initial catalog exposes actual skill path | Package needed references within each skill or establish a tested shared-root overlay; exact CLI cache path/interpolation UNKNOWN. O01's desktop cache example is not a CLI guarantee. | O01/O05/A02, 2026-09-28; relocation NOT_TESTED |
| Codex IDE Extension | Standalone skill-relative references | No plugin cache contract; native plugin **UNSUPPORTED**. | O04/O05/A02, 2026-09-28 |
| GitHub Copilot CLI | Files in invoked skill directory discovered; skill-root resource convention | Keep resources beneath installed skill root; don't assume MCP/LSP PLUGIN_ROOT expansion applies to Markdown. | G01/G03/A02, 2026-09-28; relocation NOT_TESTED |
| GitHub Copilot VS Code | Markdown and `#file:` paths relative to SKILL.md | Packaged relative resources survive directory relocation in principle; verify actual read. Runtime hook/server variables are a different mechanism. | V02/V01, 2026-09-28; relocation NOT_TESTED |

Inference for architecture: a developer-only packaging step may materialize
canonical references into each payload/skill if needed, with parity checks.
That would preserve one source of truth without requiring users to run scripts.
It is not selected or implemented here. No external symlink, `../../..` escape,
runtime fetch or author's checkout should be required to read Kiyo instructions.

## Static packaging and actual rule support

A static payload needs only the accepted manifest plus SKILL.md and Markdown
resources; native host tools carry out the workflow. C07/O02/G02/V01 support this
composition (checked 2026-09-28, DOCUMENTED_ONLY). Avoid even empty optional
MCP/hook/runtime configurations: they have no demonstrated Kiyo purpose.

Claude's complete plugin component reference excludes project-context loading
of plugin-root CLAUDE.md. OpenAI's portable manifest offers no rules/core loader.
Copilot documents namespaced plugin rules but this research has not established
a complete grammar or always-on behavior. These distinctions are recorded in the
[capability matrix](platform-capabilities.md), not filled with a universal rules
file invented by Kiyo.

## Follow-up verification and stop boundary

Later target tests must show: metadata before invocation; explicit and implicit
selection; actual packaged core/resource reads; behavior with no bootstrap;
behavior with bootstrap and conflicting existing instructions; relocation to a
fresh install/cache directory; update/reinstall; disable/uninstall; remaining
project guidance after uninstall. Record each target/version/scope independently.

Uninstalling a bundle must not be assumed to remove project files previously
created by Init. Bootstrap ownership and safe maintenance need a separately
reviewable policy. No uninstall/cleanup was attempted here.

Prompt 02 stops at research. Prompt 03 may design around documented capabilities;
Codex IDE native packaging and unresolved rule/selector/cache contracts remain
gated. Later implementation and live evaluation cannot be replaced by these pages.

