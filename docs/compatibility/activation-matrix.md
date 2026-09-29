# Activation and lifecycle matrix

Compiled 2026-09-29 for Prompt 23 from the independently checked P20–22
[source register](../research/SOURCES.md). No fresh vendor-schema change or
native execution is claimed here. The three development ZIPs do not establish
six supported installation results. See [capabilities](platform-capabilities.md)
and [native invocation](native-invocation-map.md) for documented prerequisites.

P26 [native matrix](live-test-matrix.md) adds actual Claude component discovery
and Codex disposable install/cache/uninstall. These are metadata/lifecycle subsets;
no agent Core/automatic activation result is added.

## Six target records

Each record below is also the activation requirement/host dependency referenced
by the control parity matrix. E = native selected skill, followed by an
agent-directed read of packaged KIYO/bootstrap before actions; P = separately
authorized, applicable project instruction guidance. E and P are distinct.
Metadata matching may make E eligible without P; it does not guarantee selection
or per-task Core loading. No runtime loader is supplied.

| Target ID / target | Candidate artifact / native selection | Project facility and activation requirement | Capability evidence / checked | Native behavior and gap |
| --- | --- | --- | --- | --- |
| claude-cli — Claude Code CLI | Claude; documented /kiyo-axiom-framework:<skill> | E; P via existing applicable CLAUDE.md. Plugin-root CLAUDE.md does not load as project context | CL20-02/03/06; 2026-09-29; DOCUMENTED_ONLY | Core/implicit behavior NOT_TESTED; P26 native directory/ZIP component discovery VERIFIED, marketplace lifecycle pending |
| claude-vscode — Claude Code VS Code | Same Claude candidate; actual extension skill selection | E; P through that extension's applicable Claude instructions, with actual version/workspace scope | CL20-03/04; 2026-09-29; DOCUMENTED_ONLY; see Claude target guide | NOT_TESTED independently; CLI success cannot cover extension/remote behavior |
| codex-cli — Codex CLI | Codex; /skills or $ picker; exact plugin-qualified spelling UNKNOWN | E; P via applicable AGENTS chain and launch scope; never change AGENTS.override.md/global config to force Kiyo | CX21-04/05/06; 2026-09-29; DOCUMENTED_ONLY | Core/Skill behavior NOT_TESTED; P26 local install/cache/uninstall subset VERIFIED; public ingestion FAIL, update and exact selector unresolved |
| codex-ide — Codex IDE Extension | No native plugin route selected | Native plugins UNSUPPORTED. Standalone skills/AGENTS are different mechanisms and not an approved fallback | CX21-04/06; 2026-09-29; DOCUMENTED_ONLY source of limitation | NOT_TESTED; DEC-004 open; Codex ZIP content is not IDE support evidence |
| copilot-cli — GitHub Copilot CLI | Copilot; discover actual /skills list/info entries; exact selector/collisions UNKNOWN | E; P through applicable existing Copilot/AGENTS instructions; no unverified plugin-rule loader | CP22-01/03/04; 2026-09-29; DOCUMENTED_ONLY | NOT_TESTED; bare /init or /review must not silently substitute built-ins |
| copilot-vscode — GitHub Copilot VS Code | Copilot; documented /kiyo-axiom-framework:<skill> in actual native skill UI | E; P via applicable .github/copilot-instructions.md or scoped instructions; actual harness/settings matter | CP22-07/08/09; 2026-09-29; DOCUMENTED_ONLY; official source fallback for plugin page | NOT_TESTED independently; settings, matching and remote paths unverified |

Exact source titles/URLs/redirects are retained in SOURCES; this compilation date
does not refresh their last-checked dates. Version observations from P20–22 are
historical observations, not this task's active host version. No host binary,
account or global inventory was inspected during P23.

## Managed bootstrap and ownership

The installed [canonical procedure](../../src/kiyo/framework/init-activation.md)
and target adapter control the workflow. A managed block records init-locator-1
as the text format revision, actual authorized project/module scope, actual
instruction-relative config/Memory paths and observed product version or UNKNOWN.
That internal revision is not a product release.

- Init proposes only a short scoped delta when persistent project guidance is
  requested/authorized and the native facility is established. Equivalent guidance
  is a no-op. No whole Core copy is added per task.
- Preserve CLAUDE.md, AGENTS.md, nested instructions, .github/copilot-instructions.md,
  path-specific globs and human edits inside and outside markers. Reread before
  any write. Ambiguous ownership/markers or concurrent edits hold the change.
- Missing Core holds dependent Kiyo actions and is reported. If installed resources,
  recorded version or expected content disagree, report outdated/unverified
  guidance with evidence and propose scoped maintenance; do not invent a version,
  rewrite human sections or fetch a replacement automatically.
- Updates replace immutable plugin resources through the actual native mechanism;
  they do not approve project policy/Memory/bootstrap edits. Keep the user's
  established state locations. No watcher or update hook exists.
- Native disable/uninstall concerns the plugin only. User policy, Memory and reports
  remain user-owned. Report stale locators; no automatic project cleanup.
- Only a separately authorized cleanup may remove the single reviewed Kiyo managed
  block. Preserve every other byte and the containing instruction file, even if
  only that block remains. Never delete instructions wholesale, policy or Memory.
  Human-edited/ambiguous blocks require reconciliation, not marker-only deletion.

## Evidence and future native protocol

[Offline tests](../evidence/packaging/package-checks.md) show generated files,
contained references and no writes to synthetic project state during packaging.
They do not execute Init, native update or native uninstall. Those outcomes
remain NOT_RUN/NOT_TESTED under each target's existing disposable protocol:
[Claude](claude-installation-test-protocol.md), [Codex](codex-local-test-protocol.md),
[Copilot](copilot-local-test-protocol.md).

For every available target later record the actual version/scope and installed
identity; observe discovery, selection and resource reads; compare no-bootstrap
and authorized-bootstrap cases; then verify update/uninstall leave human sections,
policy and Memory unchanged. Missing/outdated Core, module scope and human-edited
blocks need their own observations. Preserve UNSUPPORTED/UNKNOWN where appropriate.
Content equality and advisory deny text cannot prove native enforcement.
