# Copilot native installation and maintenance

Checked **2026-09-29**. Procedures are DOCUMENTED_ONLY, not executed installation
results. Sources [CP22-01/02/05/06/07/08](../research/SOURCES.md#prompt-22-copilot-revalidation).
Both live targets remain NOT_TESTED. The development artifact is
dist/copilot/kiyo-axiom-framework; consumers never run the developer generator.

## Before native changes

Review the actual prepared artifact, source and applicable policy. Confirm the
specific target, version, account authority and intended storage/config scope.
Do not install into the current global profile for this build. Prompt 26's
[disposable protocol](copilot-local-test-protocol.md) defines later testing.

Instructions below are planned forms, not commands already run. Angle-bracket
tokens require real observed/owner-supplied values. No marketplace or publisher
is claimed available. Working identity kiyo-axiom-framework is provisional.

## Copilot CLI

| Action | Documented form | Scope / limitation |
| --- | --- | --- |
| Direct local install | `copilot plugin install <prepared-plugin-directory>` | Native state/cache mutation; local source does not mean project-scoped install |
| Discover | copilot plugin list; session /skills list and /skills info | Inspect identity/source; metadata visibility is not body/Core loading |
| Register catalog | `copilot plugin marketplace add <approved-catalog-source>` | Separate configuration mutation, only after owner/source review |
| Catalog install | `copilot plugin install <plugin>@<marketplace>` | Use actual registered identifiers, not guessed Kiyo listing |
| Update plugin | `copilot plugin update <installed-name>` | Review changed bytes/permissions; avoid unrelated --all updates |
| Refresh catalog | `copilot plugin marketplace update <registered-name>` | Catalog refresh is not evidence that installed payload changed |
| Disable / enable | `copilot plugin disable <installed-name>`; `copilot plugin enable <installed-name>` | Managed/repository activation can deny local changes; do not bypass |
| Uninstall | `copilot plugin uninstall <installed-name>` | Name from native inventory, not a path; verify project state survives |
| Remove catalog | `copilot plugin marketplace remove <registered-name>` | Resolve remaining dependents; do not use force to remove unrelated plugins |

CP22-02 distinguishes direct local cached installs (reinstall to consume changed
source) from CP22-01's local-directory marketplace path sources (live directory,
restart/new session). Record the actual route before selecting an update action.
Do not generalize either behavior to all sources or to VS Code.

## Copilot in VS Code

1. Confirm the actual Copilot session/harness and agent-plugin support without
   changing permission settings. Use Extensions filter @agentPlugins or the
   Plugins tab in Chat: Open Customizations.
2. An approved catalog appears through native marketplace configuration/trust.
   Review that source before Install. Alternatively Chat: Install Plugin From
   Source takes a Git repository URL; obtain a real prepared source first.
   A monorepo checkout without root plugin.json is not this prepared plugin root.
3. For a disposable local trial, chat.pluginLocations maps the actual prepared
   directory to its enabled state. Use only the separately authorized isolated
   settings scope, preserve existing entries and record storage effects.
   This is configuration guidance; Kiyo ships no active settings.json.
4. Inspect Configure Skills and select the discovered Kiyo slash entry.
   The documented selectors are in the [adapter](../../platforms/copilot/resources/activation.md).
5. Enable/disable for the intended workspace using the UI. Update through
   Extensions: Check for Extension Updates; documented periodic checks depend
   on extensions.autoUpdate. Do not change that setting just to run this test.
6. Uninstall the exact candidate in Agent Plugins - Installed. External-source
   copies and catalog-inline copies have different disk-retention behavior.
   Do not manually delete guessed cache directories to force success.

CP22-07 documents CLI-installed-plugin discovery by VS Code. Keep that route
separate from VS Code source/local registration in test results. A clean profile
alone may not isolate CLI stores; inspect the actual test boundary first.

## Project bootstrap and residual state

Installation, update and removal are separate from authorized Init writes.
Preserve .github/copilot-instructions.md, existing path-specific instructions,
AGENTS/human sections, accepted config and canonical Memory. Never put mutable
Project Memory into plugin storage. Cleanup of a project block requires its own
bounded request; a missing plugin should produce an honest limitation.

Use the [instructions adapter](../../platforms/copilot/resources/activation.md)
for exact scope/prewrite/no-op rules. No broad tool/network/approval settings,
GitHub App, service, VSIX activation, automation or hook is part of installation.

## Owner and publication gates

| Input / gate | Why it is needed | Current state |
| --- | --- | --- |
| Final name and version | Consistent package/catalog identity and update history | OWNER_REQUIRED; working name only |
| Publisher/owner and destination | Actual authority for sharing/catalog/listing | OWNER_REQUIRED; no fabricated ID/account |
| Source repository/ref and prepared path | Catalog entries must resolve to shipped resources | OWNER_REQUIRED; no guessed remote from local path |
| Release license | Confirm intended publication while preserving existing LICENSE | OWNER_REQUIRED |
| Native compatibility and scans/review | Results for the actual artifact/target | NOT_TESTED / NOT_RUN |
| Curated acceptance | Destination-specific maintainer process and actual acceptance | UNKNOWN; no application/submission made |

CP22-06 describes a custom catalog with name, owner and plugins; a plugin entry
has name/source, with a relative source resolved from the catalog repository root.
Its GitHub convention is .github/plugin/marketplace.json; CP22-01 lists additional
lookup locations. CP22-07 links a marketplace schema separately from plugin.json.
These facts permit a future owner-filled catalog, not a fake ready manifest.
No active catalog or incomplete marketplace JSON is emitted in Prompt 22.

Default/community marketplace presence is different from private/custom source
registration and from GitHub Marketplace's App/VSIX products. Do not claim
curated approval from installing locally. Revalidate a chosen destination's
contribution/publication procedure once the owner selects it; no listing is
promised by this guide.
