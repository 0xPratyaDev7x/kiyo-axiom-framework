# User guide

Use Kiyo to state a task, its scope and its permitted effects. You do not need to
read every policy or rewrite configuration before each task. Start with the
[Skill table](skills.md); open the topic guides only when relevant.
Checked **2026-09-29** against shipped entries, native documentation and
[Prompt 26 evidence](../compatibility/live-test-matrix.md). The steps below are
a usage protocol, not new successful host runs.

## Install or load a prepared package

These are DEVELOPMENT_UNRELEASED candidates, with no public listing or approved
publisher. Obtain the complete prepared payload, not only SKILL.md or platforms/:

| Target | Prepared payload / native route | Evidence boundary |
| --- | --- | --- |
| Claude Code CLI | [Claude ZIP](../../dist/archives/kiyo-axiom-framework-claude-development.zip); load its extracted kiyo-axiom-framework root with session-only --plugin-dir | Directory/ZIP metadata discovery VERIFIED on 2.1.220; invocation NOT_TESTED |
| Claude Code VS Code | Same Claude payload; Claude panel /plugins for an actual approved marketplace/source | DOCUMENTED_ONLY; Kiyo UI install NOT_TESTED; no ready public source supplied |
| Codex CLI | [Codex ZIP](../../dist/archives/kiyo-axiom-framework-codex-development.zip); register an approved local catalog, install its actual plugin ID, start a new session | Disposable local install/cache/uninstall VERIFIED on 0.158.0; agent behavior NOT_TESTED |
| Codex IDE Extension | [Standalone skills](../../dist/codex-ide/.agents/skills); copy the eight kiyo-* folders into `<repo>/.agents/skills/` or `$HOME/.agents/skills/`, then open a new chat ([steps](../../platforms/codex-ide/README.md#install-user)) | Native plugins UNSUPPORTED, so this is the standalone-skill route (DEC-004); discovery DOCUMENTED_ONLY; Kiyo use NOT_TESTED |
| GitHub Copilot CLI | [Copilot ZIP](../../dist/archives/kiyo-axiom-framework-copilot-development.zip); native direct-directory install or actual approved catalog | DOCUMENTED_ONLY; native storage can be user-scoped, not a promised project-only install |
| GitHub Copilot VS Code | Same Copilot payload; approved source through Agent Plugins UI, or documented local plugin location in an explicitly chosen settings scope | DOCUMENTED_ONLY; NOT_TESTED; agent plugin, not a VSIX |

For a Claude local trial, extract into a chosen directory, open the intended
project and substitute its real extracted path:
```text
claude --plugin-dir "<extracted kiyo-axiom-framework root>"
```
This opens a host session. Model use requires your account/authorization; the
recorded no-quota checks exercised only metadata commands. Do not run a global
install to reproduce this session-only route. The
[Claude documentation](https://code.claude.com/docs/en/plugins/create) describes
the flag and namespacing; checked 2026-09-29, DOCUMENTED_ONLY for interactive use.

For Codex, the [reproduction guide](../compatibility/live-reproduction-guide.md)
contains the exact observed temporary catalog layout and add/list/remove commands.
Its kiyo-p26-disposable name is synthetic test data, not a marketplace you can
discover publicly. In your authorized native scope, use an actual prepared catalog:
```text
codex plugin marketplace add "<approved local catalog root>" --json
codex plugin add "<actual plugin>@<actual catalog>" --json
```
Catalog registration changes native configuration. Use a disposable child state
for a trial as described in the protocol; do not paste placeholder identities or
copy account credentials. Native installation and public-directory ingestion are
different checks. [OpenAI documentation](https://learn.chatgpt.com/docs/plugins),
checked 2026-09-29, requires a new CLI session after installation and excludes IDE
plugins.

For Copilot CLI, the documented direct route is
`copilot plugin install "<prepared plugin directory>"`. Review its native scope
before running. For VS Code use @agentPlugins or Chat: Open Customizations; local
chat.pluginLocations is an explicit settings change, not something Init enables.
Follow the [Copilot lifecycle guide](../compatibility/copilot-installation.md)
for source-specific steps and update/removal. These Kiyo routes are NOT_TESTED.
Never use this repository's unprepared root as a plugin source URL.

Native policy can deny a source or capability. Resolve that with its actual
administrator; do not broaden permissions or use bypass flags.

## Select a Skill

Logical IDs such as kiyo.init identify Kiyo procedures, not universal commands.
Mode words such as assess or sync are plain intent, not a promised host parser.

| Host | Explicit selection for this development namespace | Status |
| --- | --- | --- |
| Claude CLI | /kiyo-axiom-framework:init; replace init with the chosen slug | DOCUMENTED_ONLY |
| Claude VS Code | Same namespaced selector in the Claude panel | DOCUMENTED_ONLY, independent of CLI |
| Codex CLI | Open /skills or the $ picker and select the entry from Kiyo | DOCUMENTED_ONLY; exact qualified spelling UNKNOWN |
| Codex IDE | Open /skills or type $kiyo-init; replace init with the chosen slug | DOCUMENTED_ONLY; standalone skills, not a plugin |
| Copilot CLI | Use /skills list and /skills info to identify the Kiyo source, then its actual exposed selector | Generic /<skill-name> documented; Kiyo qualification UNKNOWN |
| Copilot VS Code | /kiyo-axiom-framework:init, or choose the Kiyo entry in Configure Skills | DOCUMENTED_ONLY |

All eight slugs are init, requirement, implement, review, test, security,
architecture and memory. Do not substitute /kiyo-init, a guessed Codex alias,
or a host's built-in /init or /review. If the source cannot be distinguished,
stop selection and report the ambiguity.
[Full invocation map](../compatibility/native-invocation-map.md);
[dated source refresh](../research/SOURCES.md#prompt-27-documentation-source-check).

## Init and project context

First select Init and request a preview or initialization explicitly. Supply the
root/module and desired output. Init samples authorized manifests, docs, source
and tests, reports evidence/unknowns, then makes only authorized project-local
Memory/config/bootstrap changes. Empty repositories remain without an invented
stack or application scaffold. Existing Memory is incrementally updated or left
unchanged, preserving human edits.

New projects default to .kiyo/memory and the existing product config convention
.kiyo/policy.md. An explicitly selected .kiyo/config.md or legacy path is retained;
never create two canonical stores/configs. Profiles and governance preferences
are optional. See [Memory](memory.md) and [Governance](governance.md).

Installation exposes host-discoverable metadata. Skill selection should lead to
Core/bootstrap, the selected procedure and only relevant references. It does
not establish always-on Core. If needed and authorized, Init proposes a small
managed project instruction block: Claude project instructions, scoped AGENTS.md
for Codex CLI, or Copilot repository/path instructions. Existing human and nested
instructions stay intact; no override/global configuration change is implied.
[Activation requirements and limits](../compatibility/activation-matrix.md).

That block also carries a short goal-to-skill list (for example: bug fix or
feature → implement; review or explain → review; write tests → test). The host
reads the instruction file each session, so later prompts can be routed to a
Kiyo skill without naming it. This routing is advisory and NOT_TESTED: the host
may still not select a skill, an unclear or look-only request starts read-only,
and naming the skill explicitly remains the reliable route. Projects initialized
before this list existed get it through an authorized Init update.

## Daily use and reports

After confirming selection, ask naturally: “Review my current changes without
editing,” “Fix this bug within these files,” or “Check these Memory observations.”
Descriptions may help the host select a Skill automatically, but Kiyo activation
in a fresh session remains NOT_TESTED. State explicit intent when selection is
uncertain. “ดู login ให้หน่อย” starts read-only or seeks clarification before edits.
Init does not run automatically for every feature.

Reports default to chat: task/scope, actions/files, governance/risk rationale,
checks/evidence, residual issues, Memory Impact, task status and next required
action. A report file is written only within authorized output scope.
PASS/FAIL/NOT_RUN/NOT_APPLICABLE/BLOCKED describe checks; DONE/PARTIALLY COMPLETE/
BLOCKED/DECISION REQUIRED describe the task. A completed review is not evidence
that tests passed. Missing environment is not N/A.

Replies follow the language of your latest message: write in English and Kiyo
answers in English; write in Thai and it answers only in Thai. Say “answer in
English” (or any language) to override. Code, commands, paths and status labels
stay unchanged, and project files keep the repository's own language convention.
See [response language](../../src/kiyo/framework/reporting-contract.md#response-language).
[Evidence Contract](../../src/kiyo/framework/evidence-contract.md);
[report templates](../../src/kiyo/framework/reporting-contract.md).

Use the [walkthroughs](walkthroughs.md) for illustrative prompts and
[troubleshooting](troubleshooting.md) for missing selection, resources or Core.
