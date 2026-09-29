# Claude local/disposable installation test protocol

**PLANNED / NOT_RUN. Execute live trials only in user-requested Prompt 26.**
Source check: 2026-09-29, [CL20 register](../research/SOURCES.md#prompt-20-claude-revalidation).
Native commands below are DOCUMENTED_ONLY and must be checked against the actual
target version then. No command in this protocol ran during Prompt 20 except
the separately recorded --version observation.

## Preparation and isolation

Use the already prepared dist/claude bundle; consumers run no generator.
Record package digest, host/extension/OS versions, actual active engine, permitted
account/policy context, selected scope and sanitized evidence location.
Never dump environment/credentials, copy authentication stores or disable managed
policy to arrange a test.

Use a disposable authorized repository and a separate native configuration root
or disposable OS environment. [CLAUDE_CONFIG_DIR](https://code.claude.com/docs/en/env-vars)
is documented to relocate Claude configuration/state (CL20-13); directory behavior
is also described by [CL20-12](https://code.claude.com/docs/en/claude-directory).
Set it only for the test process and verify the actual target honors it before
any catalog/settings mutation. It is not a Kiyo sandbox or proof all OS effects
are isolated. For VS Code, verify the launched extension process's actual
configuration root; if isolation cannot be established, hold the lifecycle test.
Do not edit the existing user's global settings or install at user scope.
Missing permitted authentication is BLOCKED/NOT_TESTED, never a reason to copy secrets.

Inventory/hash synthetic project files before testing, including existing
CLAUDE.md human sections, a legacy Memory path and project policy. Keep directory
and modified-entry evidence; run no real application, production DB or external
probe. Project/local installation can still use host-managed per-user cache;
scope controls enablement, not hard storage isolation.

## CLI session-only trial

In the disposable project, substitute actual approved bundle paths for these
metavariables; do not type angle-bracket tokens literally.

```text
claude --version
claude plugin validate <prepared-plugin-root>
claude --plugin-dir <prepared-plugin-root>
```

[Create-plugin docs](https://code.claude.com/docs/en/plugins/create), CL20-05,
document session-only loading. Record native validation's exact errors/warnings,
including absent release metadata; never call warnings a clean release check.
Confirm eight discovered selectors before invoking each with bounded synthetic
intent. Test init preview, requirement draft, explicitly requested tiny implementation,
read-only review, Test assess, Security governance/self-check, Architecture review
and Memory show/check. Test write/run modes only under separately scoped authority.

Inspect actual packaged Core/resource reads after selection, unrelated prompts,
implicit selection, disabled/unavailable cases, and guidance without bootstrap.
Then separately authorize Init's precise managed block; preserve human text and
check root versus .claude/CLAUDE.md relative locators, repeat no-op and edited-block
conflicts. Do not equate a successful file insertion with native loading.

## Disposable marketplace/local lifecycle

This is separate from --plugin-dir and is not performed merely to validate JSON.
First obtain actual catalog name/owner authority and fill the inactive
[metadata template](../../platforms/claude/marketplace.template.json) in the isolated
catalog. Copy the prepared plugin beneath its declared relative source. No fake
publisher or hosted repository URL is needed or allowed.

After isolation is verified, the documented command forms include:

```text
claude plugin validate <catalog-root>
claude plugin marketplace add <catalog-root>
claude plugin install kiyo-axiom-framework@<confirmed-catalog-name> --scope local
claude plugin list
claude plugin update kiyo-axiom-framework@<confirmed-catalog-name>
claude plugin uninstall kiyo-axiom-framework@<confirmed-catalog-name> --scope local
```

[Install/maintenance](https://code.claude.com/docs/en/plugins/install), CL20-09,
documents these mechanisms; confirm scope support and actual selected install
before update. Catalog registration itself writes native user configuration,
which must be the disposable root. Do not omit --scope on install/uninstall:
their documented default is user. No global permission changes are part of this test.

A local directory catalog can load in place. To assess copied-cache behavior,
use an independently authorized source type that actually creates a cache copy
or record that subcase NOT_TESTED; a manual copy is only a static relocation check.
Record actual discovered paths without hardcoding them into Kiyo content.

For update use two real approved candidate identities/digests; do not fabricate a
release version or retag different bytes. Compare changed content/permissions,
then confirm project Memory/policy/block preservation. After uninstall verify
skill unavailability and unchanged user state. Report residual project guidance;
removing it is a separate scoped edit, never deleting CLAUDE.md wholesale.
Removing a marketplace has wider documented effects; do not use it as casual cleanup.

## VS Code independent trial

Use the actual Claude Code extension in its separately verified disposable context.
[VS Code docs](https://code.claude.com/docs/en/vs-code), CL20-04, describe /plugins,
Marketplaces and Plugins tabs, and Install locally. Record the active extension
and bundled engine independently of terminal --version. Do not install another
extension/runtime or assume a new VS Code profile isolates Claude global state.

Repeat discovery, all eight bounded selections, implicit/no-bootstrap behavior,
authorized managed-block cases, resource reads and local lifecycle through the
actual panel. Confirm effects in that workspace; terminal success does not pass
this row. Remote/WSL environments need their own observed path/engine conditions.
If a catalog prerequisite, active engine or isolation is unknown, record the
specific gap and hold dependent mutations.

## Evidence and completion

Use the shared nine-field check record: name, applicability, method, inspected
scope, execution status, observed result, evidence location, limitations and
baseline relation. Record source-level, static relocation and live observations
separately for CLI and VS Code. [Integration cases](../../tests/integration/claude/scenarios.md)
are expected behavior until actually executed. Preserve failed/pending checks,
actual warnings, missing prerequisites, policy denials and read-only file hashes.
No Prompt 20 package/JSON check upgrades either target to VERIFIED.
