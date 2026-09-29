# Codex submission requirements and owner inputs

Checked **2026-09-29**. This is a readiness record, not a submitted listing.
Sources: [submission](https://developers.openai.com/plugins/deploy/submission)
(CX21-09), [error reference](https://developers.openai.com/plugins/deploy/submission-errors)
(CX21-10), [packaging](https://developers.openai.com/plugins/build/plugins)
(CX21-01). All publication behavior is DOCUMENTED_ONLY; portal submission NOT_RUN.

## Appropriate submission track

Kiyo is skills-only. Use the documented Skills only upload track when actually
authorized to submit. The remote MCP quickstart is an example for another
architecture; it creates no need for an MCP server, registered app, public endpoint,
authentication service, tool scan, MCP-domain proof or MCP demo credentials here.

A prepared portable package, local catalog discovery, ingestion validation,
safety review, public approval and publication are separate gates. A repo/custom
catalog is not acceptance into the universal directory. Public review approval
also does not itself publish: the authorized developer chooses publication.
This prompt creates no portal draft or remote registration.

## Known requirements and current disposition

| Gate | Required evidence / owner input | Current state / limitation |
| --- | --- | --- |
| Identity | Confirm final package/display names, semantic release version and intended release license | Working kiyo-axiom-framework / Kiyo Axiom Framework only; no release number selected; existing LICENSE preserved; DEC-001/002 |
| Publisher | Real author.name, interface.developerName, verified developer/business identity and authorized submitting organization/account | UNKNOWN; DEC-003; local ingestion validator FAIL for missing publisher fields |
| Submission authority | Actual role granting submission write access; current portal labels it Apps Management | Not inspected or granted by this task; no account/role changes |
| Interface | Truthful display/short/long descriptions, category and applicable prompts/capabilities within current limits | Neutral draft copy exists; owner review pending; metadata grants no runtime permission |
| Archive | Recognized manifest and valid contained skills/resources; no undeclared runtime dependency | Offline closure/parity pass; portal archive ingestion NOT_RUN; local validator fails release fields |
| Security/review | Passing platform skill scans and real required policy attestations | NOT_RUN; LLM/static checks do not substitute; no pre-filled attestation |
| Availability/update | Owner-selected distribution destination/regions and update/version process | UNKNOWN; no inferred directory presence, reservation or automatic update |
| Optional listing assets/links | Approved real assets and HTTPS policy/support/website links if supplied | Omitted; skills-only ZIP URLs are optional under current error reference, not permission to invent them |
| Live evidence | Independent supported-surface results and honest limitations | CLI NOT_TESTED; IDE plugins UNSUPPORTED/NOT_TESTED, DEC-004 remains open |

CX21-10 distinguishes package-upload limits from stricter final listing limits.
Current final limits include display/short text up to 30 characters, long text up
to 4,000, developer text up to 80, and up to three distinct starter prompts of
128 characters each. Recheck at submission. Five positive/three negative tests,
public MCP endpoint/domain verification and OAuth reviewer credentials described
there belong to the remote MCP branch; do not impose them on Kiyo without an
applicable skills-only requirement.

## Explicit validation gap

Root portable packaging allows optional version metadata (CX21-01). The ingestion
reference requires version and publisher fields (CX21-10). The inspected bundled
plugin-creator validator reads .codex-plugin/plugin.json and enforces that
stricter profile; it does not validate the portable root as a complete JSON Schema.

The actual run returned exit 1 for absent version, author and
interface.developerName. See [recorded result](../evidence/codex/package-checks.md).
Do not relabel it PASS, fill Local developer as a publisher, choose 0.1.0 or
fabricate a release URL just to pass. This development artifact is not
registration/submission-ready. Supply owner evidence, regenerate a new candidate
without overwriting existing output, rerun validation and native tests, then
obtain publication authorization when release work is actually requested.

The local scaffold's defaults and validator are tooling evidence, not authority
over current official documentation or the user's no-fabrication constraint.
agents/openai.yaml remains optional; no unneeded tool dependency is introduced
to resemble an MCP-backed example. Exact signing status is NOT_VERIFIED: no
signature was produced or verified, and no certification or directory approval
is claimed.
