# Copilot native overlay

Prompt 22; checked **2026-09-29**. [Current field map and target delta](../../docs/compatibility/copilot-package.md)
documents the independent GitHub/Microsoft evidence for sharing this minimal
Agent Plugins 1.0 manifest between Copilot CLI and Copilot in VS Code.
This is a static agent plugin, not a VSIX, GitHub App or hosted extension service.

## Authored inputs and derived output

- [plugin.json](plugin.json): root schema marker, working name and description only.
- [Native adapter](resources/activation.md): target-specific selection/loading
  procedure, appended conditionally to each canonical entry.
- [Developer packager](../../tools/package_copilot.py): produces
  dist/copilot/kiyo-compass plus an external provenance inventory.

Use python -B tools/package_copilot.py only while developing this repository.
Existing identical output is a no-op; different output is rejected without
overwriting/deleting it. Future replacement tooling belongs to release scope.
Consumers use prepared files and native facilities, never Python or this generator.
Helper reuse is limited to existing filesystem/hash/link utilities; neither the
Claude nor Codex manifest is an input.

Canonical name/description remain unchanged; optional client-specific metadata
and per-skill permission/visibility fields are unnecessary and omitted.
The package includes all eight entries, 97 shared Markdown resources per entry,
the native adapter and unchanged LICENSE. It includes no rules/hooks/MCP,
VSIX/package.json, executable, workflow automation or mutable project state.

## Guides and evidence

Use the [installation/lifecycle guide](../../docs/compatibility/copilot-installation.md),
[disposable test protocol](../../docs/compatibility/copilot-local-test-protocol.md)
and [integration specifications](../../tests/integration/copilot/scenarios.md).
[Offline checks](../../docs/evidence/copilot/package-checks.md) and
[source/output inventory](../../docs/evidence/copilot/package-inventory.json)
are developer evidence outside the payload.

CLI and VS Code remain independently NOT_TESTED. Documentation establishes
capabilities, not successful Kiyo installation. Exact CLI qualification and
plugin rule-loader semantics remain UNKNOWN. The current local lookup did not
resolve copilot on PATH or matching Copilot extension metadata in the inspected
standard VS Code extension directory; this is not proof of system-wide absence.

## Owner-required inputs

No marketplace JSON or recommendation/settings file is activated or supplied
with fabricated values. Before catalog/curated publication obtain the real
publication name, version, owner/publisher, authorized repository/source/ref,
destination and release-license confirmation. Existing working kiyo-compass and
LICENSE do not establish these decisions. See [release gates](../../docs/compatibility/copilot-installation.md#owner-and-publication-gates).
The artifact is DEVELOPMENT_UNRELEASED; no listing, reservation, signature,
certification or six-target compatibility claim is made.
