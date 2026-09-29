# Marketplace copy — owner review draft

**DRAFT / DEVELOPMENT_UNRELEASED / NOT SUBMITTED.**
Checked **2026-09-29** against real overlay metadata and
[release decisions](../build/DECISIONS.md). This file is copy for review, not
an active manifest, catalog entry, public listing or publication authorization.

## Existing metadata

| Field | Observed value / source | Publication boundary |
| --- | --- | --- |
| Working display name | Kiyo Compass, [Codex interface](../../platforms/codex/plugin.json) | Final name and availability require DEC-001 |
| Working native name | kiyo-compass in all three overlays | Not a reserved namespace or publisher identity |
| Claude description | Eight static Kiyo engineering and governance skills with shared guidance and project-owned memory. | Actual [manifest](../../platforms/claude/.claude-plugin/plugin.json) text |
| Codex/Copilot description | Eight static engineering and governance skills with shared guidance and project-owned memory. | Actual [Codex](../../platforms/codex/plugin.json) / [Copilot](../../platforms/copilot/plugin.json) text |
| Codex short description | Engineering workflow guidance | Actual interface metadata |
| Codex category | Productivity | Actual interface metadata, not a universal host field |
| Codex default prompt | Review the supplied changes without editing files. | Suggestion, not native permission enforcement |
| Version | UNSET | Obtain real release version/history; ignore native fallback 1.0.0 as identity |
| License | Existing root MIT LICENSE | Preserve it; obtain release confirmation under DEC-002 |
| Publisher, URLs, signature | Not supplied/established | Do not infer identity, remote URL or signing from local paths |

## Proposed description

Kiyo Compass provides eight Markdown Skills for repository onboarding,
requirements, implementation, review, testing, security, architecture and
project-owned Memory. Shared guidance asks the host agent to inspect evidence,
keep changes within scope, preserve read-only intent and report actual checks
and uncertainty.

The prepared packages contain static guidance and native metadata. They add no
Kiyo runtime, hooks, MCP server or consumer generator. Host permissions and
organization policy remain authoritative within their actual scope.

This is a development preview: Claude CLI metadata discovery and Codex CLI
disposable installation/cache/removal have bounded evidence. Kiyo agent-workflow
and automatic activation tests remain unexecuted; other targets have documented
or unsupported capabilities as shown in the
[support matrix](../../README.md#support-and-evidence).

## Owner-required before publication

- Final name/native identifiers and marketplace availability.
- Actual release version and approved release history.
- Intended publication license confirmation, preserving current history.
- Real publisher/account authority and authorized destination.
- Real source repository, prepared payload path/ref and any homepage/support/privacy URLs actually required by that destination.
- Truthful support scope, unresolved Codex IDE decision and required test evidence.
- Destination-specific submission requirements and real approval to submit.
- Signing/provenance claims only if their artifacts and verification actually exist.

A custom/local source allows native discovery within its configured scope; it
does not establish acceptance into Anthropic/OpenAI/GitHub/Microsoft curated
listings. No public Kiyo source URL is asserted here. The inactive
[Claude marketplace template](../../platforms/claude/marketplace.template.json),
[Codex template](../../platforms/codex/marketplace.template.json) and
[Copilot owner gates](../compatibility/copilot-installation.md#owner-and-publication-gates)
remain review inputs, never paste-ready public registrations.

Do not add “guaranteed always-on,” “blocks all dangerous commands,”
“ISO certified,” “all providers private,” or “verified on all six targets.”
No logo, website, dashboard or new marketing runtime is included.
