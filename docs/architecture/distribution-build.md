# Reproducible development distributions

Prompt 23, checked 2026-09-29. This implements the
[packaging contract](packaging-contract.md), using the existing three native
builders. Canonical product content is authored only in src/kiyo; native-only
metadata and adapters are authored in platforms. Never edit a generated skill
to change policy. All tooling below is developer-only and excluded from ZIPs.

## Build and review

Run from the repository root with the existing Python standard-library toolchain:

```text
python -B tools/package_distributions.py
python -B tests/packaging/test_distributions.py --report <fresh-developer-evidence-path.json>
```

The default build creates three development ZIPs under dist/archives and an
[artifact inventory](../evidence/packaging/artifact-inventory.json) outside them.
--output and --inventory may select fresh developer paths. Existing identical
output is a no-op; changed output/inventory is refused. No deletion, installation,
network request, global setting or project bootstrap occurs. Interrupted writes
may leave an incomplete new destination; inspect it and choose a fresh destination.
There is no automatic repair/cleanup or multi-file atomic transaction.

The test command builds twice through the real command-line entry point into
fresh directories, compares complete inventories and ZIP bytes, extracts them
and invokes a copied standalone checker. It creates only temporary synthetic
fixtures and its explicitly chosen developer report. Temporary directories are
left for inspection; no recursive cleanup or production resources are used.

Python was observed in the [test record](../evidence/packaging/test-results-final.json);
this is an exercised developer environment, not a promised minimum version.
Consumers neither install Python nor run these commands. Native hosts load the
already prepared files using their own documented mechanisms.

## Closed payload selection

[packaging-inputs.json](../../tools/packaging-inputs.json) is the reviewed path
allowlist: canonical Markdown, three selected static native manifests, three
activation adapters and the preserved LICENSE. No additional asset is approved.
The native builders still own their schema-specific rendering. The wrapper checks
the product tree's names before reading content and rejects an unlisted product
file; additions require review and a deliberate allowlist change.

Never package an entire checkout. .git, .env, credentials, actual project memory,
private notes, build logs, fixtures, developer scripts, node_modules and generator
source are outside selection. Synthetic exclusion tests do not prove all allowed
prose is free of secrets: content review remains a release responsibility.

Each ZIP has one kiyo-axiom-framework/ root, eight public SKILL.md files, a full shared
snapshot beneath each skill, the respective activation adapter, legal material
and native metadata. Inventory/test/parity reports remain outside the ZIP.
There is no hook, MCP, executable, VSIX, Actions runtime or consumer generator.

## Allowed transformations

| Input | Permitted output difference | Check |
| --- | --- | --- |
| Shared Markdown and templates | Byte copy preserving internal relative layout | Every output hash and actual bytes compared with canonical source |
| Canonical SKILL.md | CRLF to LF; trim terminal whitespace as existing builder does; local ../../ link destinations to ./references/kiyo/; append one conditional native adapter reference | Remove declared suffix and reverse link remap, then compare entire body/frontmatter |
| Native manifest and adapter | Byte copy from that target's reviewed overlay | Input/output inventory and existing target validator |
| Codex compatibility manifest | Existing derivation from portable identity/interface, plus documented ./skills/ | Existing Codex selected-field validator; this is not public ingestion acceptance |
| ZIP | Sorted members; kiyo-axiom-framework/ prefix; regular 0644 mode; ZIP_STORED; fixed 1980-01-01 epoch; no extra/comment data | Inspect member metadata and compare two archive digests |

The fixed ZIP epoch is a serialization constant, never a claimed creation date.
Content inventory hashes sorted relative paths plus actual file SHA-256 values.
Git HEAD is the observed base commit; worktree input hashes identify the actual
bytes. Neither Git nor hashes attest production state, authorship or signature.
Changed LF/CRLF input bytes can change archive hashes; identical bytes and tooling
must reproduce exactly. No invented release version is added.

## Resource and state boundaries

Resolve a selected skill's references from its installed location, then load its
Core/bootstrap and relevant procedures/templates. Shared Markdown stays byte
identical; its preserved directory structure closes all operational references.
HTTPS research citations are optional attribution, never an operational fetch.
User-specific path placeholders are resolved from authorized project evidence,
not from the plugin installation. Current inline-link syntax is checked; adding
other operational link/import syntax requires extending review and validation.

Project Memory defaults to .kiyo/memory only for new projects; retain established
locations. Mutable config, policy, reports and memory belong to the user's repository,
never the plugin cache. Template bodies copied to user state must use project
locators, not installed-resource links.

See the [activation/lifecycle matrix](../compatibility/activation-matrix.md) for
managed-block scope, version checks, human edits and uninstall cleanup. Packaging
does not execute that advisory procedure. Native lifecycle remains NOT_TESTED.

## Evidence limits

[Packaging checks](../evidence/packaging/package-checks.md) distinguish exact-case
path resolution, ZIP safety and cooperative process read isolation from an OS
sandbox, real POSIX execution and native host behavior. Content parity does not
establish behavioral parity. A Markdown deny is not permission enforcement.

These are unsigned DEVELOPMENT_UNRELEASED artifacts. Existing Codex ingestion
failure and unsupported IDE native plugins are preserved; publication name,
version, license confirmation, publisher and source destination remain owner gates.
No listing, signature, installability test or publication approval is asserted.
