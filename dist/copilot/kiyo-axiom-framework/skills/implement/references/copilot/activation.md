# Copilot instruction and activation adapter

Checked **2026-09-29** against the official
[CLI skill guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills),
[VS Code skill guide](https://code.visualstudio.com/docs/agent-customization/agent-skills),
[CLI instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions)
and [VS Code instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions).
Native capabilities below are DOCUMENTED_ONLY. CLI and VS Code Kiyo loading
remain independently NOT_TESTED. This adapter adds no permissions or second Core.

## Select the intended installed entry

CLI: inspect /skills list and /skills info to establish the actual Kiyo source,
entry name and location. Documentation describes /<skill-name> in a prompt, but
does not establish a Kiyo plugin-qualified selector or collision resolution with
built-in commands. Exact safe Kiyo spelling remains UNKNOWN until observed.
In particular, do not substitute the host's bare /init or /review for Kiyo.
If discovery cannot disambiguate the entry, report the gap before dependent work;
a natural-language request alone is not verified explicit invocation.

VS Code: select the actual Kiyo plugin entry from the slash menu or Configure
Skills (/skills). The documented plugin convention yields the names below.
These are development-name mappings, not reserved/published or tested commands.

| Logical ID | CLI entry to inspect; exact selector UNKNOWN | VS Code documented selector |
| --- | --- | --- |
| kiyo.init | init | /kiyo-axiom-framework:init |
| kiyo.requirement | requirement | /kiyo-axiom-framework:requirement |
| kiyo.implement | implement | /kiyo-axiom-framework:implement |
| kiyo.review | review | /kiyo-axiom-framework:review |
| kiyo.test | test | /kiyo-axiom-framework:test |
| kiyo.security | security | /kiyo-axiom-framework:security |
| kiyo.architecture | architecture | /kiyo-axiom-framework:architecture |
| kiyo.memory | memory | /kiyo-axiom-framework:memory |

Do not add the plugin prefix to frontmatter, invent /kiyo-init, or copy VS Code
qualification into CLI. Logical modes remain request intent, not extra commands.
Selection authorizes only the actual requested read/write/execute scope.

## Loading and resource boundary

Description matching can select an installed skill without Init; it is not
guaranteed. Discovery/metadata, full entry reads and Core reads are different
observations. Once selected, read [Core](../kiyo/KIYO.md) and its bootstrap before
actions under [the activation contract](../kiyo/framework/activation-contract.md).
Follow links from the actual installed file location; never use a source checkout,
cwd, guessed cache path or shell-variable expansion in Markdown.

Neither installation nor KIYO.md makes this package always-on. No plugin rules,
hooks, automations, MCP, permission preapproval or executable are supplied.
A missing required reference holds dependent actions; report it without fetching
replacement policy or running a consumer generator.

## Authorized project guidance

Follow [canonical Init activation](../kiyo/framework/init-activation.md), preserving
[trust and authority](../kiyo/framework/trust-and-authority.md) and the existing
[project configuration](../kiyo/framework/project-configuration.md). Apply:

1. Establish authorized repository/module root, current directory, selected
   CLI or VS Code session/harness and existing applicable instructions. Do not
   infer instruction scope from the editor having a folder open.
2. For an authorized repository-wide block, prefer the established applicable
   .github/copilot-instructions.md or existing accepted equivalent. Preserve all
   human sections, nested AGENTS and .github/instructions/*.instructions.md files.
   Do not regenerate the file, change existing globs or create competing guidance.
3. A module-only request does not authorize repository-wide insertion. Consider
   an explicitly scoped .github/instructions/<chosen-name>.instructions.md with
   an evidenced applyTo glob relative to the actual workspace root. Confirm its
   applicability on each target; pattern matching may not activate for a read-only
   question. If reliable scope cannot be established, keep explicit invocation
   and report the limitation rather than widening scope or enabling settings.
4. Reuse init-locator-1 with actual instruction-file-relative project state paths,
   existing canonical Memory and evidenced version, otherwise UNKNOWN. Add:
   "Select the discovered Kiyo skill for this task using this host's native UI;
   report an unresolved selector instead of substituting a built-in command."
   Keep the block within 250 words (Kiyo budget). Do not import plugin cache paths.
5. Show the concrete proposed insertion and reuse matching authorization; ask
   only for missing scope. Reread immediately before writing. Preserve edits
   inside and outside markers; ambiguous markers/concurrent changes require
   reconciliation. Equivalent guidance means no-op, including timestamps.
6. CLI instruction files are combined without a general file precedence order;
   report conflicting guidance under actual authority. CLI relative @ includes
   have repository boundaries and do not apply to every instruction format.
   Use ordinary locators here, not an assumed automatic cross-target include.
7. VS Code instruction discovery depends on session/harness/settings; inspect
   those facts without changing them. A disabled native facility or organization
   restriction is not fixed by broad permissions or global configuration changes.
   Record a new-session requirement where applicable and verify loading later.

No project guidance or Memory is written by installation. An authorized Init task
may insert the bounded block; packaging alone does not approve a consumer edit.
Updates/uninstall do not authorize removing that user-owned state. Report
discovery separately from actual instruction use and compliance.
