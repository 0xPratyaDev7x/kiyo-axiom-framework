# Local release engineering runbook

Prompt 28; checked **2026-09-29**. Developer-only, manual local execution.
This is a release rehearsal, not authorization to commit, tag, push, publish,
register a marketplace or change account/organization/branch protection settings.
No GitHub Actions workflow is needed. If one is later approved, use manual
workflow_dispatch, least permissions and no implicit publishing.

## Run

Read Build Contract, current tree, selected candidate and existing evidence.
Inspect the developer scripts before execution. Use the existing Python standard
library and Git; no production secrets, account credentials, dependency install,
native agent or model quota is required.

From repository root, choose a **fresh direct child of dist/releases**:

```text
python -B tools/release_candidate.py --output dist/releases/<fresh-run-name>
```

This is developer tooling, never an end-user prerequisite or payload component.
The [source](../../tools/release_candidate.py) creates only the named fresh run
directory and disposable test directories. Existing output is refused, even if
apparently identical; choose a new attempt and retain failures. It performs no
recursive cleanup, Git mutation, installer, network call, signing or publication.
Native safety settings are unchanged. Local paths/working-tree names in developer
evidence may be private; review/redact a separate sharing copy before disclosure.

## Pipeline and outputs

| Stage | Method and acceptance | Output / boundary |
| --- | --- | --- |
| Validate | Closed source allowlist and existing native builders; consistent identity/version across three overlays and derived Codex compatibility manifest | source-revision.json records actual Git HEAD/branch/status/version and input/tool/fixture hashes; version-consistency.json permits consistently UNSET only as development, never owner approval |
| Package | Run existing package_distributions.py twice on the same inputs; compare full inventories and archive bytes | archives/ and reproducibility/ hold three ZIPs each; original dist/archives preserved |
| Inspect payload | Safe regular-member extraction in paths with spaces; compare every member hash; existing standalone validator checks eight Skills, allowed content and references | payload-inspection.json; static evidence, not host loading |
| Run tests | Existing 37 static/negative checks against this candidate, packaging suite and release-tool regressions | evidence/ contains actual commands/results; unrun or failed checks cannot become PASS |
| Artifact inventory | Recheck input/tool/contract/HEAD continuity; compute artifact checksums and inventories | artifact-inventory.json, repeat-inventory.json, SHA256SUMS, dependency-inventory.json, attribution-inventory.json, security-change-notes.json |
| Release-readiness report | Preserve blockers independently of available successful checks | pipeline.json and readiness.md, including actual commands/exits/output/times, failures and limits |

The static runner accepts paired --inventory and --archives; its original defaults
remain available for historical artifacts. New option support changes no mandatory
assertion or negative fixture. The current packaging regression suite also
compares fresh output with existing generated trees; candidate edits require
deliberately regenerating/reviewing those trees, not weakening comparison.

Fresh build inventories are reproducible for identical bytes/tooling/revision.
Run timestamps, paths and worktree state in release evidence need not reproduce.
Git HEAD is a real base revision; uncommitted source/tool hashes identify the
actual candidate. The records are **NOT_ATTESTED**, not tamper-proof provenance.

## Interpret results

- PACKAGE_VALIDATED: required selected offline checks passed for those bytes.
- PACKAGE_VALIDATED_WITH_LIMITATIONS: the same selected checks passed, but the
  existing additional OS-dependent filesystem-symlink probe is BLOCKED and visible.
  This is a narrower local result, not an exception to a future publication gate.
- PACKAGE_NOT_VALIDATED: a required stage failed or inputs changed; retain the
  report and repair only authorized scope, then run into a fresh directory.
- HOST_VERIFIED requires separate actual per-target native/behavioral evidence.
  This pipeline always reports NOT_HOST_VERIFIED; consult P26's bounded evidence.
- PUBLISHED requires actual authorized destination evidence. This tool always
  reports NOT_PUBLISHED and publication readiness BLOCKED.

Exit 0 means the local rehearsal completed, **not** permission/readiness to publish.
Inspect individual statuses: packaging exit 0 can include PKG-08 BLOCKED on Windows.
No new signing mechanism is selected: NOT_SIGNED and NOT_ATTESTED are explicit.
A SHA256 checksum identifies bytes, not publisher identity, approval or safety.

## Inventory and security review

No Kiyo payload runtime dependencies exist in the reviewed allowlist. Developer
dependencies are Python standard library, repository helper modules and Git,
recorded separately from external native-host/account prerequisites. The ordinary
JSON dependency/attribution inventories are **not formal SBOMs**; no fabricated
packages or package URLs are added.

Attribution inventory records the actual LICENSE heading/hash and linked external
references in canonical Markdown. It does not relicense those sources or infer
legal clearance. Existing MIT LICENSE stays intact; owner release confirmation
remains pending. Review new vendored text/assets separately before adding them
to the allowlist. No ISO full text or claimed certification is included.

Security-change notes compare candidate input hashes to the recorded P23 baseline.
Review any changed instructions, native metadata, loading rules, resource paths,
access/destinations, dependencies and approval language. An empty product delta
does not close old risks. Static patterns and LLM review cannot prove safety.

Before any separately authorized release, complete
[submission gates](submission-checklists.md), [disclosure/update/revocation](security-lifecycle.md)
and [owner decisions](../build/DECISIONS.md). Missing metadata, live evidence or
required security/license review blocks publication; do not request credentials
merely to produce this report. A later approved signing step must bind the exact
archive, real signer/trust basis and successful verification evidence before any
signed/attested claim.

See [actual P28 results](../evidence/release/validation-report.md).
