# Codex IDE overlay — experimental (standalone Skills)

The Codex IDE extension (VS Code and compatible editors) does not load native
plugins; per [Codex skills](https://learn.chatgpt.com/docs/build-skills),
checked 2026-09-30, it loads **standalone skills only** from .agents/skills.
This overlay adopts that standalone route (DEC-004). The prepared payload is
dist/codex-ide. This overlay directory alone is not installable.

## Install (user)

Copy the prepared folders into one documented discovery location:

| Scope | Destination | Effect |
| --- | --- | --- |
| One repository | `<repo root>/.agents/skills/` | Kiyo is available when that repository is open |
| All repositories | `$HOME/.agents/skills/` (Windows: `%USERPROFILE%\.agents\skills\`) | Kiyo is available in every workspace |

Copy the eight kiyo-* folders from dist/codex-ide/.agents/skills, each
complete with its references/ folder. Then open a new Codex chat (or reload the
window) and run /skills or type $kiyo- to find the entries, for example
$kiyo-init. Remove the same eight folders to uninstall; project Memory and
AGENTS.md are not touched by either step.

The same folders are also discovered by Codex CLI. If the Kiyo Codex plugin is
installed too, both sets appear; keep only one route per scope.

## Developer build and ownership

Run python -B tools/package_codex_ide.py from the checkout. It reuses the Codex
packager's rendering of the canonical content, then:

- places each entry at .agents/skills/kiyo-<name>/ (standalone skills have no
  plugin namespace, so the prefix avoids collisions with generic names such as
  init, review or test);
- rewrites only the frontmatter name to match that folder;
- replaces references/codex/activation.md with the
  [IDE activation resource](resources/activation.md);
- omits plugin.json and .codex-plugin (not read by the IDE).

All other bytes equal the Codex plugin payload. Each skill folder is
self-contained, so any subset can be copied alone. The inventory is written to
docs/evidence/codex-ide/package-inventory.json. Identical builds do not touch
files; changed existing output is refused, as with the other packagers. Verify
with python -B tests/packaging/test_codex_ide.py.

## Readiness limits

Discovery locations and the $ / /skills selectors are DOCUMENTED_ONLY. Kiyo
installation, selection and activation in the IDE extension remain NOT_TESTED.
No MCP, hooks, agents/openai.yaml, global settings or installer are added.
