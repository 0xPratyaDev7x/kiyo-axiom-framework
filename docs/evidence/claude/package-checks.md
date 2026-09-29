# Prompt 20 Claude package checks

Checked **2026-09-29**. Offline development packaging and local version inspection;
no native installation, session, catalog registration or Kiyo live invocation.
Official claims use [CL20-01–13](../../research/SOURCES.md#prompt-20-claude-revalidation).
CLI and VS Code remain independently NOT_TESTED, as do the other four targets.

Initial main HEAD f5b6f57bbda7ea0f33d7726312357b4e5d690a65; clean tree/index;
105 canonical product Markdown files, 68 controls; no applicable AGENTS.md or
project .kiyo in scoped inventory. LICENSE blob preserved:
d2e60c5b160ed4f9ca096215e72efee5769936b1.

PowerShell located claude.ps1; the inspected wrapper/package metadata identified
the executable. Running that executable with --version returned
**2.1.220 (Claude Code)**, exit 0. Named extension package.json files declared
2.1.283 / 2.1.284 and engines.vscode ^1.94.0. No IDE was launched; active extension,
running VS Code version/bundled engine and account/provider/model remain UNKNOWN.
OS API reported Windows 10.0.26200 AMD64; developer Python 3.11.9.
These observations are VERIFIED only within command/file scope, not compatibility.

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CLAUDE-STATIC-01 Build | Required native-layout artifact | python tools/package_claude.py; inspected standard-library script | dist/claude and developer inventory | PASS | 794 files, eight entries, 97 shared resources per entry, eight native-reference copies, manifest and LICENSE; 4,956 contained local links | Build stdout and [inventory](package-inventory.json) | Selected-field/structure checks are not authoritative native validation | First Claude artifact, no prior package baseline |
| CLAUDE-STATIC-02 Reproducibility/relocation | Required self-contained output independent of cwd | Run same script by absolute path from temporary cwd into new output/inventory; compare all bytes and payload-only link resolution | Two 794-file trees | PASS | Equal package/inventory bytes and digests; all references/anchors contained | Inline Python stdout and digest below | Static filesystem relocation, not a native cache/session test | Identical actual inputs and interpreter |
| CLAUDE-STATIC-03 Source parity | Required canonical/overlay provenance | SHA-256/source comparisons; independent reverse-entry transform and YAML parse | 108 source inputs; all outputs and eight rendered entries | PASS | Shared/overlay/LICENSE bytes unchanged; entry bodies reverse to canonical after declared suffix/remapping/LF normalization; name/description only | Inventory and parity stdout | Hashes are not signatures, trusted origin or enforcement proof | Actual worktree hashes, observed Git base |
| CLAUDE-STATIC-04 Rejection/no-op | Required preserve existing output and reject invalid payload | Five deliberate in-memory/isolated mutations; identical rebuild with before/after snapshots | Missing Core, escaping link, extra manifest field, hook component, human output; 794-file repeat | PASS | Five cases rejected; human file unchanged; repeat output_created false, all 794 bytes/mtimes unchanged | Mutation/snapshot stdout | Not exhaustive security, symlink or race testing | Direct before/after baseline |
| CLAUDE-STATIC-05 Budgets/catalog | Required compact entries and honest metadata | Sample canonical block rendering plus native selector sentence; field/budget checks | Eight entries, one sample block and inactive template | PASS | All entries within 250 lines/1,200 words; block 114 words; catalog shape valid as template, unresolved owner/name excluded from payload | Metrics below and parity stdout | Rendering is not Init behavior/approval; unresolved catalog is not registerable/release-ready | Core/bootstrap unchanged at 81 lines/579 words |
| CLAUDE-NATIVE-01 Authoritative validator | Deferred native check | Planned claude plugin validate | Plugin and future completed disposable catalog | NOT_RUN | No native validator output; missing optional author/version may warn per documentation | [Protocol](../../compatibility/claude-installation-test-protocol.md) | Own JSON checks do not prove host acceptance | No prior native result |
| CLAUDE-LIVE-CLI | Deferred Prompt 26 | Planned isolated CLI protocol | Discovery/eight selections/Core/cache/Init/lifecycle | NOT_RUN | Target NOT_TESTED | [Scenarios](../../../tests/integration/claude/scenarios.md) | Version command is not a live Kiyo trial | No live baseline |
| CLAUDE-LIVE-VSCODE | Independent deferred Prompt 26 | Planned isolated Claude extension protocol | Active engine/panel/discovery/Core/cache/Init/lifecycle | NOT_RUN | Target NOT_TESTED | Protocol/scenarios above | On-disk metadata is not activation or CLI parity | No live baseline |

Artifact size: **3651629 bytes**. Payload digest:
`dd1a6c3f12988b9e946a9656fab01294f4a1a04bfa9236355ff56b008d26a854`.
Digest method: SHA-256 of sorted “relative-path space file-sha256” lines joined
with LF, no trailing LF. Inventory holds every source/output digest, transform
and size. HEAD identifies the base commit; hashes identify new worktree inputs,
not a claim those bytes were committed or deployed.

Builder SHA-256: `b2aee831d19406ba61cdd0598cc6f6194b18da0e1b76e650310615d636bb3c6b`.
Inactive marketplace template SHA-256: `0c1172a1598b84a2d2ec8cfa83d15aeb2d1c3115d31d6e3e1bfefb2a3c76e8f0`.
No signature produced or verified.

| Rendered entry | Lines | Words |
| --- | --- | --- |
| init | 78 | 584 |
| requirement | 74 | 585 |
| implement | 98 | 807 |
| review | 78 | 601 |
| test | 94 | 710 |
| security | 85 | 633 |
| architecture | 75 | 533 |
| memory | 79 | 627 |

Executed developer methods: python tools/package_claude.py; same script with
explicit --output / --inventory from a different temporary cwd; inline Python
mutation/snapshot/provenance/link checks; independent YAML and reverse-entry parity.
Temporary root basename: kiyo-p20-checks-urv0pg8j. No consumer generator or test
executable enters the payload. The native validator and protocol commands were
not executed; --version is the only Claude process invocation.

The builder rejects differing existing output/inventory and uses exclusive file
creation. It performs no deletion, installation, publication or native execution.
This is not an atomic multi-file update guarantee. Inspected code rejects
symlink/reparse inputs/outputs; no native hostile-symlink trial was run.
Static regex/link checks are not a security audit.

Sixteen integration cases remain NOT_RUN for each host. No behavioral simulation
was used as a substitute for deferred live tests. Publication inputs remain
blocked by owner decisions; current docs contain features newer than terminal
2.1.220. Memory Impact: NONE; no developer config/Memory/bootstrap was created.
