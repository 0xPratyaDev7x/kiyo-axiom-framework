# Claude native development distribution

Checked **2026-09-29**. Official sources CL20-01–CL20-13 are recorded in
[SOURCES](../research/SOURCES.md#prompt-20-claude-revalidation).
Native statements are DOCUMENTED_ONLY; actual offline package checks and local
version observations have separate [evidence](../evidence/claude/package-checks.md).
Both Claude Code CLI and Claude Code VS Code live results remain NOT_TESTED.

## Artifact and identity

The prepared plugin root is dist/claude, generated from canonical src/kiyo,
the [Claude overlay](../../platforms/claude/README.md) and unchanged root LICENSE.
The overlay alone is not installable. Eight skills each contain all 97 shared
canonical references plus one native activation reference. No source checkout,
Python, hook, MCP, executable, extension runtime or generator is needed by users.

kiyo-compass is a development namespace derived from the working name, not a
reserved/final release identity. No version, author, repository URL, homepage,
signature or publication-license selection was invented. Missing optional
metadata may yield native validation warnings; authoritative native validation
is NOT_RUN in this prompt. Local version inspection is not Kiyo execution.

## Field decisions

| Surface / field | Selected value or treatment | Official source / limit |
| --- | --- | --- |
| .claude-plugin/plugin.json: name | kiyo-compass, working identifier; required string | [Manifest](https://code.claude.com/docs/en/plugins-reference), CL20-01; namespaces components, publication approval separate |
| manifest description | Short truthful static-skill description | CL20-01; optional metadata, not enforcement |
| manifest component paths | Omitted; skills/ uses documented default | CL20-01 / [components](https://code.claude.com/docs/en/plugins/components), CL20-06; no rules/core field |
| manifest version / author / repository / homepage / license | Omitted pending actual owner release inputs | CL20-01; no fabricated values, missing metadata warnings remain visible |
| SKILL.md name / description | Unchanged canonical values, eight distinct names | [Skills](https://code.claude.com/docs/en/skills), CL20-02; frontmatter before body |
| Native visibility/invocation/tool fields | No added fields; no model/tool grant or hidden/manual-only override | CL20-02 documents disable-model-invocation, user-invocable and allowed-tools; Kiyo contracts stay Markdown |
| Marketplace root name / owner.name / plugins | Unresolved owner tokens plus one plugin entry in inactive template | [Marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference), CL20-08; template requires owner inputs |
| Marketplace plugins[].name / source | kiyo-compass and ./plugins/kiyo-compass | [Create marketplace](https://code.claude.com/docs/en/plugin-marketplaces), CL20-07; relative to catalog root, not .claude-plugin |

Checked date for every row: 2026-09-29. Schema source inspection does not prove
a validator accepted this artifact. No top-level Kiyo permission, risk, policy,
visibility or sandbox key is emitted. Existing host permissions still govern.

## Invocation and activation

The exact eight selectors and conditional managed-block instructions are in the
[shipped native reference](../../platforms/claude/resources/activation.md), rendered
inside each skill. Select /kiyo-compass:init, :requirement, :implement, :review,
:test, :security, :architecture or :memory using the full slash/plugin prefix.
These follow documented naming, not observed menu entries. No /kiyo-init alias,
ninth router/governance/self-check skill or mode parser is created.

Core loading remains the selected entry's explicit instruction followed by
bootstrap and relevant references. A [plugin-root CLAUDE.md is excluded](https://code.claude.com/docs/en/plugins/components)
from native project context (CL20-06). Installed metadata/relevance matching does
not establish Core loaded every turn. Project-wide guidance is a separate,
authorized native instruction arrangement; Markdown is not a sandbox.

Init renders the existing init-locator-1 shape only when needed and authorized,
with one native selector sentence, actual instruction-file-relative state paths
and UNKNOWN version when not evidenced. Preserve human text/blocks, existing
CLAUDE.md choice, legacy Memory and config, no-op repeats and independent authority.
No cache imports, global settings or hooks are added. Modern native AGENTS.md
selection can affect an existing setup; [memory documentation](https://code.claude.com/docs/en/memory)
introduces direct reading from v2.1.277, with session conditions (CL20-03).
Do not assume that feature exists in the observed older terminal CLI or change
settings/delete existing instructions to force it.

## Independent targets and local observations

| Target | Documentation / actual local evidence | Limits |
| --- | --- | --- |
| Claude Code CLI | --version returned 2.1.220 (Claude Code), exit 0; native name/layout documented | Version observation VERIFIED only; plugin discovery, invocation, Core, cache and lifecycle NOT_TESTED |
| Claude Code VS Code | Named extension package.json files declare 2.1.283 and 2.1.284, vscode engine ^1.94.0 | On-disk metadata VERIFIED only; active extension/bundled engine and running VS Code version UNKNOWN; live NOT_TESTED |

Local OS API reported Windows 10.0.26200 AMD64; developer Python is 3.11.9.
No account, entitlement, provider/model or authentication state was inspected.
The [VS Code documentation](https://code.claude.com/docs/en/vs-code) specifies
VS Code 1.94.0+ and supported paid/Console account or provider setup (CL20-04).
It documents the Claude panel /plugins and local/project/user choices; this is
not Copilot plugin UI and not proof of CLI/IDE parity.

[Host setup](https://code.claude.com/docs/en/setup), CL20-11, lists macOS 13+,
Windows 10 1809+/Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+,
x64/ARM64 and 4 GB RAM. Kiyo's minimum tested host/extension version remains
UNKNOWN. Current documentation includes newer features than the observed CLI;
the minimal package avoids depending on those newer optional features.

## Relocation, update and release limits

Shared files are byte copies; only entry relative destinations, LF normalization
and the conditional native-reference suffix differ. [Inventory](../evidence/claude/package-inventory.json)
binds actual source/output hashes to observed Git base revision, not a signature
or proof that new files are committed/deployed.

The [loading reference](https://code.claude.com/docs/en/plugins/loading), CL20-10,
distinguishes in-place local-directory sources from copied marketplace plugins.
A local-directory install alone therefore cannot prove cache relocation. Kiyo's
offline relocation uses a standalone copied tree; actual cache reads need Prompt 26.

The [test protocol](claude-installation-test-protocol.md) separates CLI/VS Code,
session loading, local installation, updates and uninstall. User-owned policy,
Memory and project block must survive; no automatic cleanup or synchronization.

Publication blockers: confirmed plugin/marketplace identity and owner/publisher
authority, release version, approved destination/source, intended license and
applicable release approval. Signature status is NOT_VERIFIED/no signature
produced. A custom catalog template is not curated listing approval. Existing
DEC-001/002/003 remain open; DEC-004's Codex IDE gap is unchanged and separate.
