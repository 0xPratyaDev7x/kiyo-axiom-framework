# Prompt 22 Copilot package checks

Checked **2026-09-29**. Scope: developer-only packaging and static tests, current
primary-source review and bounded local availability inspection.
[CP22 sources](../../research/SOURCES.md#prompt-22-copilot-revalidation) distinguish
the failed rendered VS Code page retrieval from the successful Microsoft source
fallback. Neither Copilot CLI nor VS Code Kiyo was installed or invoked.

Baseline: main HEAD 46e70a52cb105b9cb83646000e4f4652115b42fc, clean tree/index,
no tags, no scoped AGENTS/override/CLAUDE instructions and no .kiyo.
LICENSE blob d2e60c5b160ed4f9ca096215e72efee5769936b1 remains unchanged.
Prompt 21 was committed before this task. Canonical product: 105 Markdown files,
68 controls and eight entries; previous payloads: Claude 794 files, Codex 795.

## Actual executed checks

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COPILOT-STATIC-01 Build | Required distribution | python -B tools/package_copilot.py | Canonical source, native input/adapter, LICENSE | PASS | 794 files, eight skills, 97 shared resources each, 4,964 local links | Build stdout and [inventory](package-inventory.json) | Local selected-field/link checker, not native parser | First Copilot artifact |
| COPILOT-STATIC-02 Parity/frontmatter | Required canonical source | Independent reverse-entry transform, byte/SHA comparisons and existing PyYAML parsing | 108 distinct source inputs and all output bytes | PASS | Eight exact name/description frontmatters; shared/LICENSE/adapter copies exact; bodies reverse to source | Inline Python stdout, inventory | Text parity does not prove agent behavior | Canonical product bytes unchanged |
| COPILOT-STATIC-03 Rebuild/relocation | Required path independence | Same script from different cwd; second output/inventory; repeat snapshots | Two 794-file trees and original bytes/mtimes | PASS | Payload/inventory identical; repeated original leaves bytes and mtimes unchanged | Inline Python stdout and digest below | Filesystem relocation, not native cache consumption | Compared actual before/after snapshots |
| COPILOT-STATIC-04 Rejections | Required invalid-output protection | Nine isolated/in-memory negative cases | Missing Core, escape, permission field, schema, ninth skill, hook, executable, human output, wrong name | PASS | All rejected; human bytes retained; invalid output/inventory not created in tested cases | Inline Python stdout | Bounded tests, no exhaustive race/symlink/security assurance | Synthetic fixtures only |
| COPILOT-STATIC-05 Budgets/prior artifacts | Required continuity | Render canonical block body and native sentence; measure entries; compare prior inventories | Sample block, eight entries, 1,589 old payload files | PASS | Body 108 words, full block 116 including markers; entry budgets pass; old payloads unchanged | Metrics below, prior inventories | Static rendering is not Init behavior or authorization | Core remains 81 lines/579 words |
| COPILOT-NATIVE-CLI | Prompt 26 live gate | No native command/session/install executed | CLI install, discovery, selector, loading, lifecycle | NOT_RUN | Target NOT_TESTED; copilot unresolved on inspected PATH | [Protocol](../../compatibility/copilot-local-test-protocol.md) | Alternative installation/account availability UNKNOWN | No prior live result |
| COPILOT-NATIVE-VSCODE | Independent Prompt 26 gate | No editor/plugin registration/session launched | VS Code native parser/UI/harness/loading/lifecycle | NOT_RUN | Target NOT_TESTED; matching extension metadata not found in scoped directory | Protocol and [cases](../../../tests/integration/copilot/scenarios.md) | No system-wide absence or active-version claim | No CLI result substituted |
| COPILOT-PUBLISH | Outside current authority | No catalog/submission/publication | Real identity/source/listing | NOT_RUN | Release readiness BLOCKED by owner inputs and unperformed live/release checks | [Owner gates](../../compatibility/copilot-installation.md#owner-and-publication-gates) | Optional schema metadata does not remove release gates | Existing owner decisions remain open |

The native manifest's three used fields were checked against CP22-01/07/10.
No authoritative CLI/VS Code parser or downloaded full-schema validator ran.
The JSON schema was actually read; the local code checks its selected subset.
No full native schema/operational acceptance is claimed from that check.

The unchanged historical Codex ingestion FAIL remains in
[its own evidence](../codex/package-checks.md); Copilot's different native schema
does not repair, bypass or inherit that result.

## Artifact and methods

Output: dist/copilot/kiyo-compass, **3662843 bytes / 794 files**.
Digest: **9bd92a57a13bb0c47081d83802b0bf4e4dd72aec16859b1fddfc7c39dbd25ecd**.
Method: SHA-256 of sorted relative-path + space + file-SHA256 records joined
with LF and no trailing LF. A hash is not a signature or trusted publisher proof.

Codex/Claude manifests and payloads are not Copilot build inputs. Shared helper
reuse is developer-only. Tool digests:

- Copilot builder: 9b62d5ec367fddf1ccf68cf05cbbb20ed07bc4421fb54e1b5c83612b39c8c4ac
- Existing file/hash helper: b2aee831d19406ba61cdd0598cc6f6194b18da0e1b76e650310615d636bb3c6b

The actual inline Python tests used pathlib/subprocess/tempfile/hashlib/json/re
and existing PyYAML; no dependency installation. Temporary fixture basename:
kiyo-p22-checks-slpxcb0a. The builder ran first from this repository, then by
absolute tool path from a different cwd with explicit --output and --inventory,
then repeated the original output. Fixtures did not invoke a native host or
execute the synthetic forbidden executable content.

| Skill | Rendered lines | Rendered words |
| --- | --- | --- |
| init | 78 | 584 |
| requirement | 74 | 585 |
| implement | 98 | 807 |
| review | 78 | 601 |
| test | 94 | 710 |
| security | 85 | 633 |
| architecture | 75 | 533 |
| memory | 79 | 627 |

Budgets are Kiyo design criteria, not vendor token limits. The packager rejects
different pre-existing output instead of deleting/replacing it. Exclusive file
creation is not an atomic multi-file write or concurrent-edit guarantee.

## Local observation boundary

The bounded Get-Command copilot,code,pwsh lookup returned code.cmd and pwsh.exe
locations but no copilot result (command exit 1 because a requested name was
unresolved). No Copilot binary/help was run; its local version remains UNKNOWN.
A named github.copilot* package.json search only in the standard VS Code extension
directory returned zero matches. A probe of the standard editor app/package.json
also found no file. Active editor/extension/harness and alternative installation
locations remain UNKNOWN; no global plugin/configuration inventory was read.

Python APIs reported **3.11.9** and Windows **10.0.26200**. No model/provider/account,
credentials or environment dump was inspected. The 20 native case specifications
remain NOT_RUN in both columns, independently of these actual developer checks.

Memory Impact: **NONE for developer project memory**. No .kiyo, project instruction
bootstrap, native settings/catalog, VSIX, service, Actions runtime, install,
commit/tag/push/PR or publication was created.
