# Codex IDE standalone-skill activation adapter

Checked 2026-09-30 against [Codex skills](https://learn.chatgpt.com/docs/build-skills),
[AGENTS discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
and [plugin surfaces](https://learn.chatgpt.com/docs/plugins).
These facilities are DOCUMENTED_ONLY; Kiyo live loading remains NOT_TESTED.
This file is a native overlay, not another Core or a permission setting.

## Route and installed location

The Codex IDE extension does not load native plugins; it loads **standalone
skills only**. This package ships the eight Kiyo entries as standalone skills
under .agents/skills. Documented discovery covers the repository scope
($CWD/.agents/skills, parent folders inside the Git repository, and
$REPO_ROOT/.agents/skills) and the user scope ($HOME/.agents/skills).
Which location the user chose is their decision; do not move, copy or delete
skill folders to "fix" discovery. The same folders are also visible to Codex CLI
from those locations; if the Kiyo plugin is installed as well, report the
duplicate entries instead of guessing which one is active.

## Select the actual installed skill

In the IDE extension (or CLI) use /skills or type $ to open the mention picker.
Standalone skills have no plugin namespace, so each entry carries a kiyo- prefix.
Select the Kiyo entry by its actual discovered name, location and description;
do not substitute a similarly named unrelated skill. Do not invent /kiyo-init,
/kiyo:init, $kiyo.init or a Claude-style selector.

| Logical ID | Standalone skill name | Intent to supply after selection |
| --- | --- | --- |
| kiyo.init | kiyo-init | Preview or explicitly initialize the selected project scope |
| kiyo.requirement | kiyo-requirement | Define the supplied requirement; no implementation |
| kiyo.implement | kiyo-implement | Implement only the authorized behavior/change |
| kiyo.review | kiyo-review | Review the supplied changes without edits/execution |
| kiyo.test | kiyo-test | Assess, run or write as explicitly scoped |
| kiyo.security | kiyo-security | Application, skills, governance or self-check assessment |
| kiyo.architecture | kiyo-architecture | Analyze observed/intended structure read-only |
| kiyo.memory | kiyo-memory | Show/check or authorized sync/repair |

The entry body names its canonical name (for example init); that is the Kiyo
identity, while the kiyo- form is the native selector. Mode words describe user
intent, not a guaranteed native command parser.

## Explicit, implicit and project guidance

Skill metadata can make a skill eligible for relevance matching without Init.
Eligibility is not guaranteed selection. Neither installation nor the existence
of KIYO.md proves Core loaded on an unrelated task. After selection, follow the
entry's [Core](../kiyo/KIYO.md) and [activation contract](../kiyo/framework/activation-contract.md)
before actions. References resolve from the actual installed file location,
not the current working directory, source checkout or a guessed location.

Optional agents/openai.yaml is not shipped: basic name/description suffices,
no tool dependency or invocation-policy override is needed.

## Authorized project bootstrap

Use [the canonical Init procedure and block shape](../kiyo/framework/init-activation.md);
the Core and [project config contract](../kiyo/framework/project-configuration.md)
remain authoritative Kiyo content. The native adapter adds only host selection
and instruction-location guidance:

1. Establish authorized project/module root, the IDE workspace folder and actual
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
4. Render init-locator-2 using actual instruction-file-relative state paths and
   evidenced version, otherwise UNKNOWN. Add this sentence before the end marker:
   "In Codex (IDE or CLI), type $kiyo-<skill> (for example $kiyo-implement) or use /skills."
   Keep the whole Kiyo block within 250 words; this is a Kiyo budget.
5. Reread immediately before the authorized write. Preserve human content inside
   and outside markers; ambiguous/duplicate markers or concurrent changes require
   reconciliation. Equivalent guidance/no delta is a no-op. A Markdown link is
   not an automatic include, and no skill-folder path belongs in the project block.
6. Report changed paths, resolved scope and discovery limits. A new chat or
   window reload may be needed before new skills or instructions are discovered.
   File insertion alone is not proof of loading or always-on Core.

Skill folders under .agents/skills are Kiyo payload, not Project Memory. Updating
or removing them does not authorize rewriting project guidance or Memory.
No hook, watcher, network loader or consumer generator repairs missing resources;
stop only dependent actions and report the exact missing/denied path with the
actual evidence boundary.
