# Claude overlay — development, not published

The native manifest input is [.claude-plugin/plugin.json](.claude-plugin/plugin.json).
It contains only name and description. The working namespace kiyo-axiom-framework is
derived from the existing Kiyo Axiom Framework working name; it is not a final owner
publication decision. Optional release version, author, repository, homepage and
license metadata are omitted until evidenced/confirmed. Root LICENSE bytes are
preserved in the generated bundle without deciding a new publication license.

[Schema and native invocation evidence](../../docs/compatibility/claude-package.md)
records official sources checked 2026-09-29, actual local observations and limits.
The native manifest validator was NOT_RUN; missing optional author/version may
produce warnings. Do not describe this development artifact as release-ready.

## Developer build

Run from the repository, using a development Python with the standard library:

```text
python tools/package_claude.py
```

The script derives the source root from its own location, not the shell cwd.
It creates dist/claude and docs/evidence/claude/package-inventory.json.
It copies all shared canonical resources into each of eight entries, rewrites
only entry link destinations and appends one conditional reference to the native
[activation resource](resources/activation.md). That resource's ../kiyo links
resolve in its generated references/claude location; they are not author-checkout
operational links. Shared bytes and root LICENSE are unchanged.
No source Markdown is authored in dist. Identical output is a no-op; changed or
unexpected existing output is rejected instead of overwriting human content.
Use a new explicitly selected --output / --inventory destination for a changed
candidate; review older output separately. There is no destructive cleanup option.

Users receive the prepared static bundle; they never run this script, Python,
a Kiyo initializer or a build step. The overlay directory alone lacks final
resources and is not an install source. Full cross-platform packaging/release
automation remains later work.

## Marketplace metadata template

[marketplace.template.json](marketplace.template.json) is inactive developer
input, not installed or included in the plugin. Its required owner/name tokens
are deliberately unresolved. Before materializing .claude-plugin/marketplace.json
at an approved catalog root, obtain the real marketplace name/owner authority,
confirm the plugin namespace and copy the prepared bundle to plugins/kiyo-axiom-framework.
If the owner changes the plugin ID, update the manifest, entry name, path,
invocation documentation and derived package together through a reviewed change.

The relative source is interpreted from the catalog root. Do not insert guessed
repository URLs, domains, author names, signatures or Kiyo permission fields.
Custom catalog registration does not mean an official/curated listing accepted
the plugin. Publication, catalog registration and release identities remain
blocked by owner decisions; the template is not a valid ready-to-register catalog
while tokens remain. The builder never registers or publishes it.

Use the [disposable test protocol](../../docs/compatibility/claude-installation-test-protocol.md)
in Prompt 26 only. No global install, global permission edit or live test is
performed by the build.
