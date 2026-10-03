# Claude native invocation and project guidance

Checked **2026-09-29** against official Claude documentation linked below.
Native capabilities are DOCUMENTED_ONLY; CLI and VS Code live behavior are
separately NOT_TESTED. kiyo-axiom-framework is this development bundle's working namespace,
not a reserved marketplace identity, approved publisher or product release.

## Selecting a skill

The [native skill convention](https://code.claude.com/docs/en/skills) is
/plugin-name:skill-name. With this manifest the nine explicit selectors are:

| Logical skill | Documented selector for this bundle |
| --- | --- |
| kiyo.init | /kiyo-axiom-framework:init |
| kiyo.requirement | /kiyo-axiom-framework:requirement |
| kiyo.implement | /kiyo-axiom-framework:implement |
| kiyo.review | /kiyo-axiom-framework:review |
| kiyo.test | /kiyo-axiom-framework:test |
| kiyo.security | /kiyo-axiom-framework:security |
| kiyo.architecture | /kiyo-axiom-framework:architecture |
| kiyo.memory | /kiyo-axiom-framework:memory |
| kiyo.performance | /kiyo-axiom-framework:performance |

Confirm the actual discovered namespace before invocation. /kiyo-init is not
an alias supplied by this package. Test/Memory/Security modes are natural-language
intent after selection, not a custom command parser. Installation/selection
does not approve writes, execution or all future actions.

## Core and resource use

Before workflow actions follow the selected entry's
[Core](../kiyo/KIYO.md) and shared bootstrap, then only relevant references.
Resolve from the installed entry/resource path even after the bundle moves.
No checkout path, shell working directory, environment interpolation, hook or
consumer generator is required. Missing resources hold dependent actions.

Metadata matching can select a skill without project bootstrap; selection is
conditional and untested here. Installation does not load all Core every turn.
The [component documentation](https://code.claude.com/docs/en/plugins/components)
excludes plugin-root CLAUDE.md from project-context loading. Do not copy Core
there or claim an always-on loader. Markdown restrictions are advisory, not a
sandbox, tool deny policy or network control.

## Authorized Init project block

Use the canonical [managed-block procedure](../kiyo/framework/init-activation.md)
and [Init workflow](../kiyo/workflows/init.md). Read existing native/project
guidance first. A CLAUDE.md in the project root or .claude/ is a documented native
entry point ([project instructions](https://code.claude.com/docs/en/memory)).
Preserve the existing choice, surrounding human bytes and human-edited blocks.
Do not create competing CLAUDE.md/AGENTS.md files merely to force Kiyo loading.
Newer host instruction-selection settings can change which file loads; inspect
the actual target. Equivalent existing guidance means no new block.

For a requested and authorized block, render the canonical init-locator-2 shape
with actual config/index paths relative to that instruction file, actual reviewed
version or UNKNOWN, and the following Claude-specific selector sentence:
“When Kiyo is available, select the appropriate discovered /kiyo-axiom-framework:<skill>
entry before Kiyo workflow actions; that entry directs its packaged Core read.”
Replace the namespace if an actual installed identity differs. This sentence is
a rendering addition, not a ninth skill or an import of plugin cache files.

Keep the complete rendered block within Kiyo's 250-word budget. Preview writes
nothing. Propose the exact delta, reuse valid authorization, reread the latest
file immediately before a scoped insertion and reconcile ambiguous markers/
human edits rather than overwriting. No automatic settings change, hook, Core
copy, provider choice or policy adoption follows. Project .kiyo/policy.md is the
default config equivalent; retain any accepted legacy config/Memory location.
For .claude/CLAUDE.md, recompute relative paths instead of reusing root-file paths.

The user owns the inserted block, policy and Memory. Plugin update/uninstall
does not authorize changing them. If the skill is unavailable, report it and
preserve state; do not claim the Core ran. Report native project guidance,
agent-directed Core reads and automatic activation separately under the
[activation contract](../kiyo/framework/activation-contract.md).

## CLI and VS Code remain separate

CLI management uses /plugin; the
[Claude VS Code panel](https://code.claude.com/docs/en/vs-code) uses /plugins.
This package adds no VS Code extension runtime. A CLI outcome does not establish
the extension's active version, instruction loading, remote access or cache reads.
Current documentation is a design source, not evidence this package ran on either.
