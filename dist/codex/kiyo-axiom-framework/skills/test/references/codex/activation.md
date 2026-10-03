# Codex instruction and activation adapter

Checked 2026-09-29 against [Codex skills](https://learn.chatgpt.com/docs/build-skills),
[AGENTS discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
and [plugin surfaces](https://learn.chatgpt.com/docs/plugins).
These facilities are DOCUMENTED_ONLY; Kiyo live loading remains NOT_TESTED.
This file is a native overlay, not another Core or a permission setting.

## Select the actual installed skill

In Codex CLI use /skills or the $ mention picker. Select the Kiyo entry by
its actual discovered identity, source and description; do not substitute a
similarly named unrelated skill. Exact plugin-qualified spelling/collision
resolution is UNKNOWN until observed. Do not invent /kiyo-init, /kiyo:init,
$kiyo.init or a Claude-style selector. A package identifier is not a skill command.

| Logical ID | Canonical entry name to find | Intent to supply after selection |
| --- | --- | --- |
| kiyo.init | init | Preview or explicitly initialize the selected project scope |
| kiyo.requirement | requirement | Define the supplied requirement; no implementation |
| kiyo.implement | implement | Implement only the authorized behavior/change |
| kiyo.review | review | Review the supplied changes without edits/execution |
| kiyo.test | test | Assess, run or write as explicitly scoped |
| kiyo.security | security | Application, skills, governance or self-check assessment |
| kiyo.architecture | architecture | Analyze observed/intended structure read-only |
| kiyo.memory | memory | Show/check or authorized sync/repair |
| kiyo.performance | performance | Evidence-driven investigation; execution separately scoped |

Mode words describe user intent, not a guaranteed native command parser.
The IDE extension's native plugin path is **UNSUPPORTED** in current docs.
Standalone IDE skills are a distinct documented mechanism; this package does not
install or promise that fallback. Missing plugin support is a capability gap,
not permission to copy into a global skill directory.

## Explicit, implicit and project guidance

Skill metadata can make a skill eligible for relevance matching without Init.
Eligibility is not guaranteed selection. Neither installation nor the existence
of KIYO.md proves Core loaded on an unrelated task. After selection, follow the
entry's [Core](../kiyo/KIYO.md) and [activation contract](../kiyo/framework/activation-contract.md)
before actions. References resolve from the actual installed file location,
not the current working directory, source checkout or a guessed cache layout.

Optional agents/openai.yaml is not shipped: basic name/description suffices,
no tool dependency or invocation-policy override is needed, and desktop UI
examples do not establish identical CLI/IDE presentation.

## Authorized project bootstrap

Use [the canonical Init procedure and block shape](../kiyo/framework/init-activation.md);
the Core and [project config contract](../kiyo/framework/project-configuration.md)
remain authoritative Kiyo content. The native adapter adds only host selection
and instruction-location guidance:

1. Establish authorized project/module root, current working directory and actual
   instruction chain. Inspect only relevant ancestor/nested instruction files.
   Native discovery builds a root-to-current-directory chain once per run,
   selecting at most one nonempty file per directory, with override precedence
   and a documented combined byte limit. Existing host/global guidance remains
   outside Init's write scope.
2. Preserve AGENTS.md and human sections. Do not edit, remove or create
   AGENTS.override.md, global instructions/config, fallback-name settings or
   permission settings to force Kiyo. If an existing override shadows the proposed
   file, report the limitation and hold dependent bootstrap insertion.
3. For a module-only request, consider only that module's appropriate AGENTS.md.
   Do not insert a root-wide block or duplicate canonical Memory/config. A nested
   block is guidance for its actual scope; it grants no repository-wide access.
   If discovery from the user's launch directory does not include it, report that
   condition rather than moving the block upward without authority.
4. Render init-locator-2 using actual instruction-file-relative state paths and
   evidenced version, otherwise UNKNOWN. Add this sentence before the end marker:
   "In Codex CLI, use /skills or the $ picker to select the discovered Kiyo entry."
   Keep the whole Kiyo block within 250 words; this is a Kiyo budget.
5. Reread immediately before the authorized write. Preserve human content inside
   and outside markers; ambiguous/duplicate markers or concurrent changes require
   reconciliation. Equivalent guidance/no delta is a no-op. A Markdown link is
   not an automatic include, and no cache path belongs in the project block.
6. Report changed paths, resolved scope and discovery limits. A new session may
   be needed to rebuild native instructions. File insertion alone is not proof
   of loading or always-on Core. Unsupported IDE plugins remain unsupported.

Plugin updates/uninstall do not authorize rewriting project guidance or Memory.
User-owned state stays in the project. No hook, watcher, network loader or
consumer generator repairs missing resources; stop only dependent actions and
report the exact missing/denied path with the actual evidence boundary.
