# Codex overlay — 1.0.0 (stable for Codex CLI, not listed in an official directory)

The authored [portable manifest](plugin.json) follows current
[OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins),
checked 2026-09-29. The prepared plugin root is dist/codex/kiyo-axiom-framework.
This overlay directory alone is not installable.

The packager copies root plugin.json and derives .codex-plugin/plugin.json for
the documented compatibility path. It never reads a Claude manifest or adapter.
Portable identity/components remain primary; the inline OpenAI interface replaces
the compatibility interface on hosts that recognize it, rather than merging.
The compatibility file serves older/compatibility readers; their acceptance is
NOT_TESTED, not a promised minimum-version fallback.

## Developer build and ownership

Run python -B tools/package_codex.py from the checkout, or invoke that script by
its actual path from another working directory. This creates the distribution
and docs/evidence/codex/package-inventory.json. Shared filesystem/hash helpers
are reused from the existing developer packager; no Claude schema or artifact
is used as Codex input. Both tooling hashes are recorded outside the payload.

The generated eight skill trees contain the canonical shared snapshot plus the
[Codex activation resource](resources/activation.md). Its ../kiyo links resolve
at the rendered references/codex location. Only entry relative links, LF
normalization and one conditional adapter link differ from canonical entries.
Do not edit generated output. Identical builds do not touch files; changed
existing output is refused. Use a new explicit --output ending in kiyo-axiom-framework
and a separate --inventory for a changed candidate. No deletion or installer.

Users receive prepared files and run no Python, generator or Kiyo executable.
There is no agents/openai.yaml because it is optional and unnecessary here;
manifest-level interface metadata supplies the documented package presentation.
No MCP, app registration, hooks, network service or global settings are added.

## Readiness limits

The working name is not an owner-approved release identity. Version 1.0.0 and
author are owner-supplied (2026-09-30); interface.developerName is still absent
pending real publisher evidence. The bundled plugin-creator ingestion validator
reported **FAIL** for the three fields on 2026-09-29 and was not rerun. Offline layout/parity checks do not erase that result. See
[actual evidence](../../docs/evidence/codex/package-checks.md).

[marketplace.template.json](marketplace.template.json) is inactive, outside the
payload, with unresolved catalog name/label. Its source path is relative to a
future approved catalog root containing plugins/kiyo-axiom-framework. No marketplace
entry has been registered, discovered or installed. Availability/authentication
metadata describes the catalog, not Kiyo action approval or account access.

Read [native field/invocation guidance](../../docs/compatibility/codex-package.md),
[local test protocol](../../docs/compatibility/codex-local-test-protocol.md) and
[submission requirements](../../docs/compatibility/codex-submission.md).
CLI live behavior remains NOT_TESTED. IDE plugins remain documented UNSUPPORTED;
no standalone fallback was silently adopted. No submission or publication.
