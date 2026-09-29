# Prompt 28 — local release engineering evidence

Checked **2026-09-29**. DONE for developer-only tooling, local artifacts and
available offline checks. Publication readiness remains **BLOCKED**.
Runtime Verification: **Verified — developer pipeline only**.

## Actual executions

Both commands ran from the repository root with Python 3.11.9 on the recorded
Windows environment. No native host, model, signing or publication command ran.

| Actual command | Exit | Observed outcome |
| --- | --- | --- |
| python -B tools/release_candidate.py --output dist/releases/p28-run-01 | 0 | Six stages completed; 37 static tests, eight release-tool tests, ten packaging PASS and one BLOCKED |
| python -B tools/release_candidate.py --output dist/releases/p28-run-02 | 0 | Same scoped outcomes after reporting/empty-evidence guard corrections; PACKAGE_VALIDATED_WITH_LIMITATIONS |

[First execution](../../../dist/releases/p28-run-01/pipeline.json) is retained.
[Final execution](../../../dist/releases/p28-run-02/pipeline.json) records each
actual argv, cwd, start/end time, stdout/stderr and exit, plus source hashes.
The packaging runner's own JSON omits an exit-code field; final pipeline records
the real child-command exit instead of showing a null summary. Empty stage
evidence now cannot become PACKAGE_VALIDATED, with a regression assertion.
Unsigned status is not made an automatic vendor publication requirement; owner
policy and required controls must be resolved separately. No product invariant,
mandatory negative or historical failure was removed.

A read-only requirements-print command encountered Windows console encoding
error; it was rerun with English requirement fields. No files changed in that
failed inspection. The pipeline itself had no failed required checks in either run.

## Candidate and inspection

- Actual base revision: f368ecf736c3b4d9558e77ab030487a00f071602, main.
  [Source record](../../../dist/releases/p28-run-02/source-revision.json)
  separately hashes actual uncommitted inputs/tooling/contract/fixture bytes.
- Existing builders ran twice per pipeline; full inventories and all three
  archive bytes matched. Later run artifacts also retain the existing product
  hashes. No owner version was assigned: four manifest values consistently UNSET.
- [Artifact inventory](../../../dist/releases/p28-run-02/artifact-inventory.json)
  traces every file to canonical source/allowed transformation. Actual extraction
  into fresh space-containing paths yielded Claude 794, Codex 795 and Copilot 794
  files, eight Skills each and contained references.
- [Static tests](../../../dist/releases/p28-run-02/evidence/static.json):
  37 PASS, zero failures/errors/skips; includes 21 exact-reason negative fixtures.
  These read the new candidate, not the historical default ZIPs.
- [Packaging checks](../../../dist/releases/p28-run-02/evidence/packaging.json):
  ten PASS; PKG-08 BLOCKED by Windows symlink-creation error 1314. Existing ZIP
  symlink/traversal rejection and exact-case tests passed; no elevation attempted.
- [Release-tool regressions](../../../dist/releases/p28-run-02/evidence/release-tests.json):
  eight PASS, zero failures/errors/skips. Synthetic failure/escape/overwrite/
  version cases are expected negatives, not actual agent incidents.

These are selected static properties, **not FULL SCHEMA VALIDATION**. Forbidden
scripts, fixtures, private state and runtime components are excluded by closed
input/output selection plus inspected member hashes and negative tests. Bounded
template patterns do not prove absence of every possible secret or harmful prose.

## Actual archive SHA256

[Computed checksum file](../../../dist/releases/p28-run-02/SHA256SUMS):

| Candidate | SHA256 |
| --- | --- |
| Claude | 10bc505a083f86276d0ba78ebb4c06fa64f93143ff607eed63898ffafc711672 |
| Codex | 8c2594d3767dad46e66358b69afecbe0ce7787bfccb5dc3e035f5bb55522de5c |
| Copilot | 9a5130c9fd2f102b18ce7b0fa3dc42f20e660834c357703299f3a6d3a4e2e4df |

These identify bytes, not publisher identity. Artifacts are **NOT_SIGNED** and
provenance is **NOT_ATTESTED**. Git records/local hashes are not cryptographic
attestations or production evidence.

## Inventories and sensitive change review

[Dependency inventory](../../../dist/releases/p28-run-02/dependency-inventory.json)
records **no payload runtime dependencies**, no required third-party Python
packages, and separate standard-library/repository helper/Git developer inputs.
Native hosts/accounts are external prerequisites, not bundled software.
[Attribution inventory](../../../dist/releases/p28-run-02/attribution-inventory.json)
records the unchanged LICENSE heading/hash and 38 distinct canonical reference
citations. Neither inventory is a formal SBOM or license clearance.

[Security-change notes](../../../dist/releases/p28-run-02/security-change-notes.json)
find no allowlisted product delta against P23. Developer changes add a fresh-output
local coordinator, selected-candidate options to the existing static runner and
regressions for version/output/failure boundaries. They introduce local file
writes and subprocess execution of the reviewed existing checks, no consumer
scripts or new network/signing/install surface. Review is self-review, not an
independent security audit. AST02/07/08/09/10 responsibilities remain divided
between Markdown guidance, native host, release developer and authorized humans.

[Runbook](../../release/runbook.md), [submission checklists](../../release/submission-checklists.md)
and [disclosure/update/revocation](../../release/security-lifecycle.md) retain
owner metadata, contact, policy, lifecycle and approval gates.
[Six official source checks](../../research/SOURCES.md#prompt-28-release-source-check)
are DOCUMENTED_ONLY; no account/portal inspected. No license, publisher or author
email chosen. No production secret or credential requested.

## Limits and continuity

PACKAGE_VALIDATED_WITH_LIMITATIONS is narrower than HOST_VERIFIED or PUBLISHED.
All six host states stay independent; no new host acceptance is claimed.
P25's 48 host cases remain NOT_RUN; P26 partial discovery/lifecycle records and
strict/ingestion failures stay unchanged. Codex IDE native plugins remain
UNSUPPORTED. A disclosure contact and actual release decisions remain owner inputs.

REQ-006/053/059/064–067/076/077/079/080 gain partial tooling/documentation/evidence
coverage. All 80 full verifications remain NOT_RUN. After build-state updates,
the [actual closure audit](closure-audit.json) exits 0 with five checks PASS:
records/hashes, current G16/80-ID trace structure, 2,582 Markdown files and
18,812 local links, plus Git scope/preservation. Link counts precede this final
evidence-link edit. It does not rerun the native/behavioral layers.

Memory Impact: NONE. No commit/tag/push/publish/marketplace registration or
account/global/organization setting change. Safe to continue with user-requested
Prompt 29 Gap Audit while keeping publication and missing evidence gates open.
