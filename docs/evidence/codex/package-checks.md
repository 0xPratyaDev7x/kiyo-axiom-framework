# Prompt 21 Codex package checks

Checked **2026-09-29**. Offline packaging and local version/help inspection only.
No native session, plugin install, catalog registration or public submission.
Current official sources: [CX21-01–12](../../research/SOURCES.md#prompt-21-codex-revalidation).
CLI and IDE live Kiyo results remain NOT_TESTED; IDE native plugins are documented
UNSUPPORTED. The active coding session is not a Kiyo installation trial.

Initial main HEAD: 5102892d7c82f8c9a0301d3146219d4eaf894bba; clean tree/index;
105 canonical product files/68 controls; no applicable scoped AGENTS.md or .kiyo.
LICENSE blob remains d2e60c5b160ed4f9ca096215e72efee5769936b1.
No owner release version or publisher has been supplied.

## Executed checks

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CODEX-STATIC-01 Package | Required static distribution | python -B tools/package_codex.py | Actual canonical input, Codex overlay, LICENSE; output/inventory | PASS | 795 files, eight entries, 97 shared resources per entry and eight native-reference copies; 4,956 contained local links | Build stdout, [inventory](package-inventory.json) | Selected-field check, not complete native/portal schema acceptance | First Codex artifact; Claude source/artifact not used as native metadata |
| CODEX-STATIC-02 Parity | Required single canonical source | Source/output SHA-256 and independent reverse-entry transform; bundled skill parser and quick_validate.py | 108 source inputs, eight entries, all copied references/templates | PASS | Shared/LICENSE/adapter bytes match sources; rendered entries reverse to canonical; eight parser checks and eight quick validations pass | Inline Python stdout and inventory | Text parity does not prove model behavior or host enforcement | 105 canonical product files unchanged |
| CODEX-STATIC-03 Relocation/rebuild | Required path independence and reproducibility | Invoke same script from temporary cwd into new kiyo-compass root; compare trees/inventories; repeat original | Two 795-file trees and original file/mtime snapshots | PASS | Equal bytes/digest/inventory; repeat leaves 795 file bytes/mtimes and inventory unchanged | Mutation/snapshot stdout, digest below | Standalone filesystem relocation, not actual native cache loading | Direct before/after snapshot |
| CODEX-STATIC-04 Negative cases | Required reject unsafe/divergent output | Seven in-memory/isolated invalid cases | Missing Core, escaping link, permission field, divergent fallback, hook, human output, wrong outer name | PASS | All seven rejected; synthetic human bytes preserved; wrong-name output not created | Inline test stdout | Bounded cases, not exhaustive security or race/symlink testing | Invalid fixtures only; existing project files untouched |
| CODEX-STATIC-05 Budgets/preservation | Required compact adapter and unchanged earlier artifact | Static block rendering, entry counts, prior Claude output hashes | One sample block, eight entries, 794 Claude files | PASS | Block 108 words; all entries within 250 lines/1,200 words; all earlier Claude bytes unchanged | Metrics below and existing Claude inventory | Sample is not Init behavior, native instruction loading or approval evidence | Core/bootstrap unchanged at 81 lines/579 words |
| CODEX-INGEST-01 Bundled validator | Required tooling check; publication readiness gate | python -B plugin-creator/scripts/validate_plugin.py dist/codex/kiyo-compass using the inspected installed script | .codex-plugin/plugin.json and eight skill entries | FAIL | Exit 1: missing version, author object and interface.developerName | Exact diagnostics below; validator digest | Stricter compatibility-ingestion profile; does not validate portable root schema or perform native install | Owner release metadata was already unresolved |
| CODEX-LIVE-CLI | Deferred Prompt 26 | Planned isolated native protocol | Install/discover/select/Core/cache/AGENTS/lifecycle | NOT_RUN | Target NOT_TESTED | [Protocol](../../compatibility/codex-local-test-protocol.md), [18 cases](../../../tests/integration/codex/scenarios.md) | Version/help/static checks are not a live Kiyo trial | No prior native result |
| CODEX-LIVE-IDE | Unsupported native plugin path | No plugin install attempted | Independent IDE capability boundary | NOT_RUN | Capability UNSUPPORTED; live result NOT_TESTED | CX21-06 and protocol | Standalone skills are a different unapproved fallback | No CLI-to-IDE inference |
| CODEX-SUBMIT-01 Portal | Outside current task authority | No portal upload/scan/attestation/publication | Public ingestion/review | NOT_RUN | Readiness BLOCKED by real owner fields and unperformed release checks | [Submission gates](../../compatibility/codex-submission.md) | No fabricated listing, scan result or signature | No published version claimed |

## Ingestion failure retained

The unchanged bundled validator returned exactly:

- plugin.json field `version` must be a non-empty string
- plugin.json field `author` must be an object
- plugin.json field `interface.developerName` must be a non-empty string

No validator rule was removed or loosened. The selected-field development checker
does not replace it. Eight independent skill-parser checks pass, but the complete
ingestion result remains FAIL. The user requires real owner inputs; no Local
developer publisher, initial version or guessed URLs were inserted.

The public packaging and submission docs describe different gates. This artifact
is DEVELOPMENT_UNRELEASED; registration/submission readiness is blocked. Correct
the identity fields only with actual owner evidence, rebuild a new candidate and
rerun relevant validators before dependent work. Passing an offline structural
check is not proof that native 0.158.0 accepts this current candidate.

Validator SHA-256: `1e6cb914505b458856c2cfab7d18a224731c743ef47e0c9d78afe64f35b67f7c`.
Identifier helper SHA-256: `680ce5b775ee5410ecf808fad40350dc4df2cc4a7003363f4c4c7f9d7c0be918`.
Both installed files were read before execution; Python -B avoided local bytecode
writes. Existing PyYAML was used; no dependency was installed. Full validator is
developer tooling outside the payload, not a consumer prerequisite.

The inspected skill-creator/scripts/quick_validate.py was also run separately
for each of the eight rendered skill directories with python -B -X utf8.
All eight returned exit 0, "Skill is valid!", with empty stderr. Its SHA-256 was
`6068513d924ed3559e186dfcdead7439129828dcf402167fd925c06dffbf2806`.
These are skill text/frontmatter checks; the complete plugin ingestion failure
above is unchanged.

## Artifact identity and measured budgets

Artifact: **3658481 bytes**, **795 files**.
Payload digest: `d8f04fab527109ec5e097d72c5a8fc3e6942002ba13804b9fd1a02db0672fdd7`.
Method: SHA-256 of sorted "relative-path space file-sha256" lines joined by LF
with no trailing LF. Inventory records actual source/output digests, transforms,
byte sizes, both developer tooling hashes and the observed Git base. The base
revision does not imply these new worktree files are committed or deployed.

Codex builder: `be65187fcb802253310704409cf60d0099c71e7d555811e1f53299d1a4a38309`.
Reused filesystem/hash helper module: `b2aee831d19406ba61cdd0598cc6f6194b18da0e1b76e650310615d636bb3c6b`.
Inactive catalog template: `c0199919d84f0c77123c77ca684007a957132e6a06a8d7021786fa469675e35a`.
No signature produced or verified.

| Rendered skill | Lines | Words |
| --- | --- | --- |
| init | 78 | 584 |
| requirement | 74 | 585 |
| implement | 98 | 807 |
| review | 78 | 601 |
| test | 94 | 710 |
| security | 85 | 633 |
| architecture | 75 | 533 |
| memory | 79 | 627 |

Actual methods: initial build; same script by absolute path from a different cwd;
new --output/--inventory build; inline Python byte/hash/mtime/link/parity and
seven-rejection checks; eight skill-parser calls; eight quick_validate.py runs;
complete bundled validator.
Temporary test root basename: kiyo-p21-checks-1y4p8f1z. Isolated fixtures were
synthetic; no application commands, runtime scanner or suspicious payload ran.
The builder refuses different existing output and uses exclusive creation,
without deletion. This is not an atomic multi-file or concurrent-write guarantee.

## Observed local versions and command grammar

The scoped PATH wrapper/npm package inspection identified a terminal binary.
Executing that binary with --version returned **codex-cli 0.158.0**, exit 0.
plugin --help and add/remove/marketplace add/marketplace upgrade --help also
returned exit 0. Only help ran: no add/remove/list/upgrade action was performed.

Observed grammar: add/remove take PLUGIN@MARKETPLACE (or a marketplace option);
marketplace add takes a source; marketplace upgrade optionally takes a catalog
name and describes refreshing Git snapshots. No exact installed-skill selector,
cache path, update behavior or account entitlement was observed. Help output
is VERIFIED only as command documentation for that installed binary.

Named extension package.json declares **26.917.62051**, publisher openai,
engines.vscode **^1.96.2**. This is on-disk metadata only: active extension,
bundled engine and running editor version UNKNOWN. No IDE was launched.
OS API: Windows 10.0.26200; developer Python **3.11.9**.
Provider/model/account/credentials were not inspected.

Eighteen integration rows remain NOT_RUN for CLI with IDE applicability explicitly
UNSUPPORTED. No behavioral/native result is derived from those specifications.
Memory Impact: **NONE** for developer project memory; no project bootstrap,
AGENTS.override.md, .kiyo or global setting was created/changed.
