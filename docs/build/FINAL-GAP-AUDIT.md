# Prompt 29 — Final gap audit

Checked **2026-09-29**. Audit/fixes/available regressions: **DONE**.
Product release readiness: **BLOCKED**. No target has full **HOST_VERIFIED**
status; nothing is **PUBLISHED**, signed or attested.

Baseline: main, actual HEAD `f5cb303b1713ce6f103760c0cad05fcd7e086fcf`, initially clean.
The user authorized this completeness audit and targeted fixes, not a new host/model
session, global installation, publication or Prompt 30. No account/quota was used.
This is the author's evidence-backed self-audit, not an independent certification.

## How to read the result

All **80 original IDs and acceptance criteria** were reviewed; none was reduced.
**78 IMPLEMENTED / 2 PARTIALLY_IMPLEMENTED (REQ-010 and REQ-061)** describes
authored static instructions, native overlays and developer deliverables.
It does not mean 78 host behaviors passed. Earlier trace rows conflated these
dimensions and still described already-created Skills as future work.

Full registered acceptance verification remains **NOT_RUN for all 80**:
the reserved TC-REQ methods are not an executed end-to-end acceptance suite.
The per-ID records below separate actual manual content inspection, selected
automated checks, bounded historical source-guided trials and native evidence.
A PASS for content inspection means the listed text/structure was inspected;
it never substitutes for a behavioral assertion in the AC. README names alone
were not counted as implementing a control.

The [machine-readable ledger](requirement-audit.json) contains all criteria,
implementing files/line locators, procedure/Skill assignments, existing versus
planned cases, scoped actual evidence, both statuses, limits, decisions and gaps.
[TRACEABILITY](TRACEABILITY.md) is the compact current view. Historical trace
text remains in Git at the baseline revision; earlier execution records are
preserved in place.

## Inspected evidence and limits

- Actual canonical entries, shared procedures/policies/templates/profiles and
  [closed packaging inputs](../../tools/packaging-inputs.json); three existing
  packages and the [fresh candidate inventory](../../dist/releases/p29-run-02/artifact-inventory.json).
- [Fresh pipeline](../../dist/releases/p29-run-02/pipeline.json):
  actual commands, exits, hashes and source revision; reproduction uses existing
  developer tooling. [Regression report](../evidence/gap-audit/validation-report.md)
  preserves the failing reproduction and successful fix.
- [Static suite coverage](../evidence/static/coverage-interpretation.md) is selected
  properties, **not FULL SCHEMA VALIDATION**. The bounded template scan is not DLP.
  Source-denying extraction checks are cooperative tests, not an OS sandbox.
- [P25 observations](../evidence/behavioral/observations.json): **48 NOT_RUN**;
  expected catalog outputs are not transcripts. Earlier forward-trial reports
  retain named limited observations; they are not rerun here, a full raw
  tool-access audit, or installed-host acceptance.
- [P26 native evidence](../compatibility/live-test-matrix.md): 72 independent
  records, two complete bounded Codex lifecycle checks PASS, 70 NOT_RUN.
  Claude partial discovery and Codex cache-byte checks are additional scoped
  observations, not complete Skill/Core behavior.
- [Standards sources](../research/standards-baseline.md) retain their dated
  DOCUMENTED_ONLY public-catalogue/draft/full-text limits. This audit makes
  no new external edition/schema claim and does not refresh their check dates.

## Gaps and release gates

Every open gap has a responsible role, next action and exact blocking scope.
A missing account/IDE/owner field is not filled with mock evidence.
No unresolved critical host incident is asserted from unrun cases. A future
unauthorized destructive action, secret exposure or fabricated test result
must block release under the [existing defect rules](../evidence/behavioral/defects.md).
The unresolved HIGH release/host/owner gates below already prevent general
release readiness; they do not prevent completion of this offline audit.

### GAP29-01

- Category / state / severity: **Contradictory contract / FIXED / HIGH**.
- Gap: Incomplete/reordered all-PASS stage lists could yield PACKAGE_VALIDATED.
- Next action: Require six exact ordered stages; regression-before fails, regression-after passes; run complete pipeline.
- Control owner: Developer release process.
- Blocking scope: Local package gate; fixed, historical run evidence unchanged.

### GAP29-02

- Category / state / severity: **Broken reference / FIXED / MEDIUM**.
- Gap: Architecture worked example used obsolete literal resource paths and a generic root that did not match Codex/Copilot; native summary was stale.
- Next action: Correct current locators and point historical research to bounded P26 evidence; check referenced targets.
- Control owner: Kiyo documentation.
- Blocking scope: User/maintainer navigation; fixed, no payload mutation.

### GAP29-03

- Category / state / severity: **External owner decision / OPEN / HIGH**.
- Gap: Final name/availability, version, publication license confirmation, publisher/account authority, source/destination, disclosure contact and signing policy unresolved.
- Next action: Owner supplies actual approved metadata and intended publication scope; preserve MIT and never fabricate identity/signature.
- Control owner: Human owner; DEC-001/002/003.
- Blocking scope: All public release/submission/registration; not local audit.

### GAP29-04

- Category / state / severity: **Missing live evidence / OPEN / HIGH**.
- Gap: 48 P25 host cases NOT_RUN; prior source-guided trials are bounded reports, not installed six-target acceptance.
- Next action: With explicit host/account/quota authority, execute fixtures and retain tool traces, response, byte/mtime diffs and first-run/rerun history; adjudicate objective criteria separately from model grades.
- Control owner: Human test operator.
- Blocking scope: Behavioral acceptance, HOST_VERIFIED and general release readiness; offline audit can finish.

### GAP29-05

- Category / state / severity: **Missing live evidence / OPEN / HIGH**.
- Gap: Full per-target installation/invocation/Core loading/restart/update/bootstrap/uninstall matrix is incomplete; Codex selector and Copilot CLI collisions unresolved.
- Next action: Execute only remaining supported target cases in disposable authorized contexts per P26 reproduction guide; preserve separate explicit/automatic and CLI/IDE outcomes.
- Control owner: Human target operator.
- Blocking scope: Dependent target support/activation/lifecycle claims and release qualification.

### GAP29-06

- Category / state / severity: **External owner decision / OPEN / HIGH**.
- Gap: Codex IDE native plugin route is documented UNSUPPORTED; standalone Skill fallback has not been adopted.
- Next action: Owner retains unsupported launch target or explicitly approves a separately scoped fallback; do not treat CLI as IDE PASS.
- Control owner: Human owner; DEC-004.
- Blocking scope: Codex IDE native package support; other target work can continue.

### GAP29-07

- Category / state / severity: **Missing test / OPEN / MEDIUM**.
- Gap: Real filesystem symlink probe blocked by Windows privilege 1314; no POSIX OS execution. ZIP symlink/traversal negatives already pass.
- Next action: Run the existing probe in an authorized capable disposable environment; if cross-OS support is intended, execute relevant extraction tests there. Do not elevate only to erase a limit.
- Control owner: Developer test operator.
- Blocking scope: Unqualified filesystem/cross-OS portability claims; package status retains WITH_LIMITATIONS.

### GAP29-08

- Category / state / severity: **External owner decision / OPEN / MEDIUM**.
- Gap: Standards are dated public-catalogue concept mappings; full ISO text not assessed, AST public-review draft, SAMM incremental status unknown.
- Next action: Revalidate only release-dependent official claims; obtain lawful full texts only if clause-level assessment is later requested. Keep concepts/draft/unknown labels.
- Control owner: Human standards/release reviewer.
- Blocking scope: Clause-level/latest-edition/certification claims; no certification claimed or required.

### GAP29-09

- Category / state / severity: **Missing test / OPEN / MEDIUM**.
- Gap: Reserved TC-REQ IDs are planned acceptance methods, not executed tests. Subset scenarios do not establish complete large-context, durable-Memory, all-input injection, profile/quality or repair-resume acceptance.
- Next action: Test maintainer maps remaining AC clauses to runnable/manual cases before claiming full requirement verification; keep existing negatives and all unrun cases.
- Control owner: Developer test maintainer.
- Blocking scope: Full AC verification; does not negate authored Markdown implementation.

### GAP29-10

- Category / state / severity: **External owner decision / OPEN / HIGH**.
- Gap: Final product acceptance/launch decision (Prompt 30) has not occurred.
- Next action: Present this audit and remaining release gates in user-requested Prompt 30; no release/host authorization inferred.
- Control owner: Human owner.
- Blocking scope: Final product acceptance and publication.

### GAP29-11

- Category / state / severity: **Contradictory contract / FIXED / MEDIUM**.
- Gap: Inherited trace status left all authored content partial and REQ-001 unimplemented without separating content from live acceptance.
- Next action: Reassess every ID against actual files; explicit authored implementation status plus unchanged full verification NOT_RUN and requirement-specific remaining gaps.
- Control owner: Developer auditor.
- Blocking scope: Traceability/readiness interpretation; corrected without promoting host results.

### GAP29-12

- Category / state / severity: **Missing implementation / OPEN / HIGH**.
- Gap: Publication manifests lack approved version/author and Codex interface developerName; strict Claude validation and Codex ingestion retain failures.
- Next action: After GAP29-03 decisions, apply smallest supported native metadata changes and regenerate/revalidate packages. Do not invent missing inputs or weaken validators.
- Control owner: Developer release process after owner input.
- Blocking scope: Publication-ready Claude/Codex artifacts; local development payloads remain bounded previews.

### GAP29-13

- Category / state / severity: **Contradictory contract / FIXED / HIGH**.
- Gap: Required readiness report I/O occurred after a successful pipeline record was persisted; output failure could leave exit_code 0 in that record.
- Next action: Persist success only after readiness write; failure now records FAIL/exit 1. Keep both reproduction and rerun, and the final real pipeline.
- Control owner: Developer release process.
- Blocking scope: Truthful local release evidence; fixed. Multi-file evidence is not transactional or tamper-proof.

## Invariant review

All entries below are **manual static inspection PASS**, with the limitations
shown. Native/behavioral outcomes remain separate. Related requirements identify
the exact implementing files and test evidence in the per-ID ledger.

| Invariant | Requirements | Inspected result / limitation |
| --- | --- | --- |
| INV-01 — No runtime/MCP/hooks/installer creep | [REQ-002](#req-002), [REQ-003](#req-003), [REQ-079](#req-079) | G12 and closed input/output inventories; only developer tools execute. |
| INV-02 — Exactly eight public Skills | [REQ-025](#req-025), [REQ-026](#req-026) | G01/G02/G03; helpers and logical submodes are not entries. |
| INV-03 — Review/Security/Architecture/Memory check read-only | [REQ-027](#req-027), [REQ-071](#req-071), [REQ-073](#req-073), [REQ-074](#req-074), [REQ-075](#req-075) | G07 plus actual entry/mode review; host adherence remains untested. |
| INV-04 — Governance/risk/approval consistent | [REQ-047](#req-047), [REQ-048](#req-048), [REQ-049](#req-049) | G08 tables and approval contract; independent concepts, actual authority needed. |
| INV-05 — G4 restricted | [REQ-047](#req-047), [REQ-052](#req-052) | Explicit default hold, organization prohibitions and host denials survive confirmation. |
| INV-06 — Native hierarchy unchanged | [REQ-011](#req-011), [REQ-051](#req-051) | Core and policy resolution cannot self-promote Markdown. |
| INV-07 — README/Memory grant no authority | [REQ-012](#req-012), [REQ-062](#req-062) | Embedded instructions/data boundaries cover copied approvals and credentials. |
| INV-08 — Approved intent not rewritten from code | [REQ-019](#req-019), [REQ-022](#req-022), [REQ-074](#req-074), [REQ-075](#req-075) | G10 and drift flow; Mapperly/AutoMapper case distinguishes usage from package declaration. |
| INV-09 — Manual drift not real-time | [REQ-021](#req-021), [REQ-024](#req-024) | Invoked lifecycle only; no watcher in inventory. |
| INV-10 — Tiny retains safety/evidence | [REQ-029](#req-029), [REQ-030](#req-030) | Tiny compresses ceremony; approval, scoped evidence and Memory Impact retained. |
| INV-11 — No-op Memory no timestamp touch | [REQ-020](#req-020), [REQ-023](#req-023), [REQ-075](#req-075) | Entry-level date rules and no-op; bounded historical MEM-FWD-05 only. |
| INV-12 — Native activation/CLI/IDE claims bounded | [REQ-005](#req-005), [REQ-009](#req-009), [REQ-010](#req-010), [REQ-078](#req-078) | README/P26/current invocation pointer separate metadata, discovery, loading and execution. |
| INV-13 — AST01-10 owner/evidence/limits | [REQ-058](#req-058), [REQ-059](#req-059), [REQ-060](#req-060), [REQ-061](#req-061), [REQ-062](#req-062), [REQ-063](#req-063), [REQ-064](#req-064), [REQ-065](#req-065), [REQ-066](#req-066), [REQ-067](#req-067) | G09 validates ten structured records; public-review draft AST separate from ASI. |
| INV-14 — No fake hard enforcement | [REQ-007](#req-007), [REQ-051](#req-051), [REQ-063](#req-063) | Host owns sandbox/network/permissions; Kiyo is advisory. |
| INV-15 — PASS requires actual execution/inspection | [REQ-039](#req-039), [REQ-040](#req-040), [REQ-044](#req-044), [REQ-079](#req-079) | G08 fake-PASS negative; repaired release gate requires every mandatory stage. |
| INV-16 — Static/behavioral/live evidence separated | [REQ-065](#req-065), [REQ-077](#req-077) | P25 observations stay NOT_RUN; P26 limited native records unchanged. |
| INV-17 — Human edits preserved | [REQ-015](#req-015), [REQ-024](#req-024), [REQ-034](#req-034) | Reread/minimal diff/no reset/stash/revert; fixture evidence bounded. |
| INV-18 — No forced architecture or packages | [REQ-033](#req-033), [REQ-037](#req-037) | Discovery-first profiles and existing safe pattern rule; extensions are outlines. |
| INV-19 — Self-contained packages | [REQ-006](#req-006) | G04/G06/G12/G13 plus extracted checks; no source/cwd dependency. |
| INV-20 — Update/uninstall preserve user state | [REQ-064](#req-064), [REQ-076](#req-076) | Project-owned Memory/policy and block-only cleanup; only Codex synthetic uninstall observed. |
| INV-21 — Standards mappings not certification | [REQ-056](#req-056), [REQ-057](#req-057) | Dated official source records, concept-level limits, no clause reproduction. |
| INV-22 — Guides match shipped Skills | [REQ-010](#req-010), [REQ-026](#req-026), [REQ-078](#req-078) | Eight-entry guide and target-specific logical/native distinctions; nine walkthroughs illustrative. |

## Per-target readiness recommendation

These recommendations are limited to observed evidence on 2026-09-29.
No public launch, installation or quota authorization is implied.

| Target | Actual evidence | Recommendation / blocking actions |
| --- | --- | --- |
| Claude Code CLI | 2.1.220 normal validation and directory/ZIP discovery of eight names; strict validation FAIL for absent version/author | Development preview for an authorized disposable trial only. Owner metadata, persistent install, explicit invocation, Core/workflow behavior and lifecycle still required |
| Claude Code VS Code | Editor 1.139.1; extension manifests 2.1.283/2.1.284; active engine UNKNOWN | NOT_TESTED. Establish disposable IDE/account and run independent protocol; CLI result does not qualify IDE |
| Codex CLI | 0.158.0 local catalog install/list, byte-matching cache and uninstall preserving three synthetic project files | Development preview only. Ingestion FAIL for missing owner fields remains; fallback 1.0.0 is not product version. Exact selector, agent reads/behavior, restart/update/managed block tests required |
| Codex IDE Extension | Metadata 26.917.62051; active engine UNKNOWN; native plugins documented UNSUPPORTED | Do not claim native plugin support. DEC-004 owner decision required for any separately scoped standalone-Skill fallback |
| GitHub Copilot CLI | Not resolved on inspected PATH; alternate installation/account UNKNOWN | NOT_TESTED. Establish approved environment, validate/install/discover and resolve exact plugin selector/built-in collisions before invocation claims |
| GitHub Copilot VS Code | No matching extension metadata in inspected standard directory; active/alternate setup UNKNOWN | NOT_TESTED. Independent approved IDE/plugin test required; shared portable manifest is not UI/control parity |

Use the [remaining tests](../compatibility/live-owner-required-tests.md) and
[reproduction guide](../compatibility/live-reproduction-guide.md), not fabricated
flags or a universal slash alias. Explicit invocation and automatic activation
are separate tests. No installation alone establishes always-on Core.

## Requirement-by-requirement findings

All rows were checked on **2026-09-29**. The AC is unchanged in
[the registry](REQUIREMENTS.md). Listed file lines locate the implementing
section; the entire relevant procedure was considered. Named Gxx results are
partial static assertions in the fresh candidate run. Scenario specifications
and P25 host cases remain NOT_RUN unless an explicitly separate historical trial
record describes its own narrower observed scope.

### REQ-001

- Criterion: [AC-001](REQUIREMENTS.md#req-001). Drafts label Kiyo Axiom Framework as a working name and retain Kiyo branding; release identity and marketplace availability stay unconfirmed until owner decisions and evidence exist; existing LICENSE is preserved.
- Implementing files: [src/kiyo/KIYO.md:6](../../src/kiyo/KIYO.md); [README.md:20](../../README.md); [LICENSE:1](../../LICENSE); [docs/release/marketplace-copy.md:8](../../docs/release/marketplace-copy.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Working name and development disclaimer are explicit; existing MIT file preserved, publication identity not invented.
- Test cases: TC-REQ-001 **PLANNED**; G06 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G06 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Owner must confirm identity, license and publisher before release; this is not missing branding prose.
- Owner decisions: DEC-001, DEC-002, DEC-003.
- Next action / blocking scope: [GAP29-03](#gap29-03), [GAP29-11](#gap29-11).

### REQ-002

- Criterion: [AC-002](REQUIREMENTS.md#req-002). Package inventory contains Markdown plus justified host-native static metadata/assets; an end user can consume the instructions without running a Kiyo executable.
- Implementing files: [tools/packaging-inputs.json:1](../../tools/packaging-inputs.json); [tools/package_distributions.py:1](../../tools/package_distributions.py); [docs/architecture/packaging-contract.md:15](../../docs/architecture/packaging-contract.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Closed payload inputs contain Markdown and justified static manifests plus LICENSE; no consumer build step.
- Test cases: TC-REQ-002 **PLANNED**; G12, G13 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G12 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G13 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [developer release pipeline — PASS](../../dist/releases/p29-run-02/pipeline.json) (Actual six-stage exit 0; PKG-08 limitation separately retained, no host/model/publication).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Native consumption still needs per-target workflow evidence.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-003

- Criterion: [AC-003](REQUIREMENTS.md#req-003). Repository and payload review finds none of the prohibited product components or user runtime dependencies; developer validate/package/test/release scripts remain outside payloads and are not end-user prerequisites.
- Implementing files: [tools/packaging-inputs.json:1](../../tools/packaging-inputs.json); [tools/package_distributions.py:1](../../tools/package_distributions.py); [tools/release_candidate.py:1](../../tools/release_candidate.py).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Builders and release/tests stay developer-only; three inspected payloads contain no executable, MCP or hooks.
- Test cases: TC-REQ-003 **PLANNED**; G12 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G12 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [developer release pipeline — PASS](../../dist/releases/p29-run-02/pipeline.json) (Actual six-stage exit 0; PKG-08 limitation separately retained, no host/model/publication).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Static inventory proves these bytes, not agent compliance or future releases.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: No missing implementation identified in inspected scope. Repeat inventory review when product bytes change; no global behavior/security guarantee.

### REQ-004

- Criterion: [AC-004](REQUIREMENTS.md#req-004). Each ecosystem has evidence-backed native installation instructions and a package overlay where supported; unsupported or unverified paths are recorded as gaps rather than claimed supported.
- Implementing files: [platforms/claude/README.md:15](../../platforms/claude/README.md); [docs/compatibility/codex-package.md:13](../../docs/compatibility/codex-package.md); [docs/compatibility/copilot-installation.md:8](../../docs/compatibility/copilot-installation.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Three independently authored native overlays and installation guides exist; unsupported IDE route is disclosed.
- Test cases: TC-REQ-004 **PLANNED**; G05 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G05 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Codex IDE native plugins UNSUPPORTED. Codex IDE route unsupported; persistent Claude/IDE/Copilot installation and owner metadata remain gated.
- Owner decisions: DEC-001, DEC-002, DEC-003, DEC-004.
- Next action / blocking scope: [GAP29-05](#gap29-05), [GAP29-03](#gap29-03), [GAP29-06](#gap29-06).

### REQ-005

- Criterion: [AC-005](REQUIREMENTS.md#req-005). A matrix contains six distinct rows with capability sources, tested versions when observed, checks, evidence and gaps; CLI results never mark an IDE row passed.
- Implementing files: [docs/compatibility/platform-capabilities.md:17](../../docs/compatibility/platform-capabilities.md); [docs/compatibility/live-test-matrix.md:24](../../docs/compatibility/live-test-matrix.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Six independent target records retain exact observed versions, sources, partial checks and gaps.
- Test cases: TC-REQ-005 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; no P25 case directly assigned to this ID.
- Actual evidence: [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Codex IDE native plugins UNSUPPORTED. Partial CLI observations cannot establish IDE or full workflow support.
- Owner decisions: DEC-004.
- Next action / blocking scope: [GAP29-05](#gap29-05), [GAP29-06](#gap29-06).

### REQ-006

- Criterion: [AC-006](REQUIREMENTS.md#req-006). Each platform package includes all required internal content, resolves references without the source checkout, and traces copied material to the single canonical specification; overlays contain only justified host differences.
- Implementing files: [tools/package_distributions.py:1](../../tools/package_distributions.py); [tools/verify_payload.py:1](../../tools/verify_payload.py); [docs/architecture/packaging-contract.md:15](../../docs/architecture/packaging-contract.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Entry transformation and complete per-skill shared snapshots trace to canonical bytes; extraction checks cover three archives.
- Test cases: TC-REQ-006 **PLANNED**; G04, G06, G12, G13 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G04 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G06 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G12 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G13 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded); [developer release pipeline — PASS](../../dist/releases/p29-run-02/pipeline.json) (Actual six-stage exit 0; PKG-08 limitation separately retained, no host/model/publication).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Native resource reads/updates are distinct from static relocation; OS symlink probe blocked.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-05](#gap29-05), [GAP29-07](#gap29-07), [GAP29-02](#gap29-02).

### REQ-007

- Criterion: [AC-007](REQUIREMENTS.md#req-007). Core guidance and user documentation assign actual tool use to the host agent and permission enforcement to the host; they contain no Kiyo enforcement, security guarantee or certification claims.
- Implementing files: [src/kiyo/framework/trust-and-authority.md:9](../../src/kiyo/framework/trust-and-authority.md); [src/kiyo/agent-security/control-ownership.md:13](../../src/kiyo/agent-security/control-ownership.md); [docs/user/security.md:8](../../docs/user/security.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Advisory guidance explicitly assigns enforcement to host and rejects certification/security guarantees.
- Test cases: TC-REQ-007 **PLANNED**; G07 selected static checks; BEH-SEC-04, BEH-X-08, BEH-X-13 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [SEC-04](../../tests/behavioral/security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-SEC-04, BEH-X-08, BEH-X-13).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Host restriction scenario and target enforcement remain unverified.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-008

- Criterion: [AC-008](REQUIREMENTS.md#req-008). Procedures specify a concrete preventive or recovery step for each pattern; six corresponding scenarios show evidence-seeking, scoped changes, truthful reporting, intent preservation and context recovery/revalidation.
- Implementing files: [src/kiyo/framework/bootstrap.md:6](../../src/kiyo/framework/bootstrap.md); [src/kiyo/workflows/workflow-router.md:3](../../src/kiyo/workflows/workflow-router.md); [src/kiyo/workflows/repair-and-handoff.md:3](../../src/kiyo/workflows/repair-and-handoff.md); [src/kiyo/workflows/memory-lifecycle.md:8](../../src/kiyo/workflows/memory-lifecycle.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Six failure patterns have evidence, scope, intent, reporting and revalidation/recovery procedures.
- Test cases: TC-REQ-008 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; no P25 case directly assigned to this ID.
- Actual evidence: This dated manual file/contract inspection; no automated behavioral result.
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No complete six-pattern host acceptance run; source-guided trials cover bounded subsets only.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-009

- Criterion: [AC-009](REQUIREMENTS.md#req-009). Bootstrap directs progressive loading within a documented context budget; every automatic activation claim has host-specific source and test evidence, with explicit invocation fallback or an explicit gap otherwise.
- Implementing files: [src/kiyo/framework/bootstrap.md:6](../../src/kiyo/framework/bootstrap.md); [src/kiyo/framework/activation-contract.md:3](../../src/kiyo/framework/activation-contract.md); [src/kiyo/framework/init-activation.md:8](../../src/kiyo/framework/init-activation.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Compact budget and conditional native project bootstrap are authored; no always-on claim.
- Test cases: TC-REQ-009 **PLANNED**; G14 selected static checks; BEH-X-13 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [INIT-06](../../tests/behavioral/init/scenarios.md), [INIT-12](../../tests/behavioral/init/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G14 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-13); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Fresh-session activation and managed-block lifecycle not exercised on supported targets.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-05](#gap29-05).

### REQ-010

- Criterion: [AC-010](REQUIREMENTS.md#req-010). Each target documents verified explicit invocation syntax separately from inferred activation; examples do not invent universal commands or imply inference is guaranteed.
- Implementing files: [docs/compatibility/native-invocation-map.md:3](../../docs/compatibility/native-invocation-map.md); [docs/user/README.md:10](../../docs/user/README.md); [src/kiyo/framework/activation-contract.md:3](../../src/kiyo/framework/activation-contract.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Documented Claude/Copilot VS Code selectors and Codex picker are separate from logical IDs and inferred activation.
- Test cases: TC-REQ-010 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-SEC-04, BEH-X-13 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [SEC-04](../../tests/behavioral/security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-SEC-04, BEH-X-13); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **PARTIALLY_IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Codex IDE native plugins UNSUPPORTED. Verified explicit selectors absent; Codex exact qualified selector and Copilot CLI collision handling unknown; IDE native route unsupported.
- Owner decisions: DEC-004.
- Next action / blocking scope: [GAP29-05](#gap29-05), [GAP29-06](#gap29-06), [GAP29-02](#gap29-02).

### REQ-011

- Criterion: [AC-011](REQUIREMENTS.md#req-011). Procedures identify the source and applicable authority of a policy, preserve higher-priority host instructions and stop or surface unresolved conflicts without treating repository text as system authority.
- Implementing files: [src/kiyo/framework/trust-and-authority.md:9](../../src/kiyo/framework/trust-and-authority.md); [src/kiyo/governance/policy-resolution.md:3](../../src/kiyo/governance/policy-resolution.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Native hierarchy, real policy provenance and dependent-action conflict handling are explicit.
- Test cases: TC-REQ-011 **PLANNED**; G07 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [ORG-03](../../tests/behavioral/organization-policy/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Behavior under conflicting live host/user/project context not accepted across targets.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-012

- Criterion: [AC-012](REQUIREMENTS.md#req-012). Guidance explicitly treats instructions embedded in each listed input as untrusted data unless authorized through the native hierarchy; injection scenarios cannot silently authorize new actions or policy changes.
- Implementing files: [src/kiyo/framework/trust-and-authority.md:9](../../src/kiyo/framework/trust-and-authority.md); [src/kiyo/agent-security/prompt-injection.md:3](../../src/kiyo/agent-security/prompt-injection.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: README, code/comments, issues, web/tool outputs and Memory are data, unable to grant approval or credential access.
- Test cases: TC-REQ-012 **PLANNED**; G07 selected static checks; BEH-X-01, BEH-X-02, BEH-X-03, BEH-X-04 **NOT_RUN**.
- Actual evidence: [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-01, BEH-X-02, BEH-X-03, BEH-X-04).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. All input-class injection scenarios remain unexecuted in target suite; bounded trials not universal prevention.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-013

- Criterion: [AC-013](REQUIREMENTS.md#req-013). Context records distinguish observed values from unknowns, link permissible evidence and use UNKNOWN for unavailable details; no account tier or model identity is inferred from appearance or branding.
- Implementing files: [src/kiyo/governance/provider-policy.md:3](../../src/kiyo/governance/provider-policy.md); [src/kiyo/templates/reports/self-check-report.md:24](../../src/kiyo/templates/reports/self-check-report.md); [src/kiyo/framework/trust-and-authority.md:9](../../src/kiyo/framework/trust-and-authority.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Identity/account/model/route fields require evidence or UNKNOWN without secret lookup.
- Test cases: TC-REQ-013 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-INIT-01, BEH-REV-03, BEH-ARCH-03, BEH-X-15 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [INIT-01](../../tests/behavioral/init/scenarios.md), [ORG-06](../../tests/behavioral/organization-policy/scenarios.md), [REV-03](../../tests/behavioral/review/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-INIT-01, BEH-REV-03, BEH-ARCH-03, BEH-X-15); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Actual active IDE/model/account unknown; no inference from PATH, metadata or branding.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-014

- Criterion: [AC-014](REQUIREMENTS.md#req-014). Bootstrap defines staged reading and a context-budget strategy; a scoped task loads required instructions and relevant material rather than all framework/repository files; near-limit handoff preserves next actions.
- Implementing files: [src/kiyo/framework/context-loading.md:3](../../src/kiyo/framework/context-loading.md); [src/kiyo/workflows/repair-and-handoff.md:3](../../src/kiyo/workflows/repair-and-handoff.md); [src/kiyo/templates/reports/handoff.md:1](../../src/kiyo/templates/reports/handoff.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Progressive conditional loading, numeric authoring budgets and scoped handoff exist.
- Test cases: TC-REQ-014 **PLANNED**; G14 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [INIT-09](../../tests/behavioral/init/scenarios.md), [INIT-14](../../tests/behavioral/init/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G14 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No measured large-repository reduced-context read-set/token overhead acceptance.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-015

- Criterion: [AC-015](REQUIREMENTS.md#req-015). Before edits the procedure records the permitted baseline; a dirty-worktree scenario preserves existing user changes and does not reset, clean, stash or revert them without scoped authorization.
- Implementing files: [src/kiyo/framework/engineering/change-scope.md:6](../../src/kiyo/framework/engineering/change-scope.md); [src/kiyo/skills/implement/SKILL.md:16](../../src/kiyo/skills/implement/SKILL.md); [src/kiyo/workflows/init.md:3](../../src/kiyo/workflows/init.md).
- Skills/shared procedures: init implement review; linked files above define the shared steps.
- Actual inspection: Preflight baseline and final reread preserve staged/unstaged/untracked and concurrent human edits.
- Test cases: TC-REQ-015 **PLANNED**; G07 selected static checks; BEH-INIT-04, BEH-IMPL-01, BEH-REV-04 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [IMP-08](../../tests/behavioral/implement/scenarios.md), [INIT-04](../../tests/behavioral/init/scenarios.md), [INIT-05](../../tests/behavioral/init/scenarios.md), [INIT-15](../../tests/behavioral/init/scenarios.md), [REV-04](../../tests/behavioral/review/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-INIT-04, BEH-IMPL-01, BEH-REV-04).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Dirty-worktree/full fixture matrix not executed on native hosts; bounded trials only.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-016

- Criterion: [AC-016](REQUIREMENTS.md#req-016). Tasks consult available relevant memory within read permissions, verify material claims against current repository evidence and identify stale or inaccessible knowledge rather than following it blindly.
- Implementing files: [src/kiyo/framework/context-loading.md:3](../../src/kiyo/framework/context-loading.md); [src/kiyo/workflows/memory-lifecycle.md:8](../../src/kiyo/workflows/memory-lifecycle.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Relevant permitted Memory is read then compared with current repository claims; denied access remains explicit.
- Test cases: TC-REQ-016 **PLANNED**; G10 selected static checks; BEH-MEM-02 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [INIT-02](../../tests/behavioral/init/scenarios.md), [INIT-07](../../tests/behavioral/init/scenarios.md), [INIT-10](../../tests/behavioral/init/scenarios.md), [RQM-04](../../tests/behavioral/requirement/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G10 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-MEM-02).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Fresh/stale/denied context combinations need live evaluation, not Memory-as-truth.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-017

- Criterion: [AC-017](REQUIREMENTS.md#req-017). The procedure resolves one canonical path, defaults to .kiyo/memory when unconfigured and reports conflicting stores instead of silently creating a second truth source; approved path changes preserve existing knowledge.
- Implementing files: [src/kiyo/framework/memory-specification.md:9](../../src/kiyo/framework/memory-specification.md); [src/kiyo/framework/project-configuration.md:3](../../src/kiyo/framework/project-configuration.md); [src/kiyo/workflows/memory-lifecycle.md:8](../../src/kiyo/workflows/memory-lifecycle.md).
- Skills/shared procedures: init memory; linked files above define the shared steps.
- Actual inspection: One established declaring-file-relative locator; new default .kiyo/memory, legacy paths preserved.
- Test cases: TC-REQ-017 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-INIT-02, BEH-INIT-03, BEH-MEM-04 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [INIT-02](../../tests/behavioral/init/scenarios.md), [INIT-03](../../tests/behavioral/init/scenarios.md), [INIT-08](../../tests/behavioral/init/scenarios.md), [INIT-11](../../tests/behavioral/init/scenarios.md), [MSK-09](../../tests/behavioral/memory/skill-scenarios.md), [ORG-02](../../tests/behavioral/organization-policy/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-INIT-02, BEH-INIT-03, BEH-MEM-04).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Conflicting stores/migration/worktree behavior not fully host-tested.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-018

- Criterion: [AC-018](REQUIREMENTS.md#req-018). Memory guidance and templates retain useful durable knowledge with evidence and exclude exhaustive endpoint/method inventories that duplicate code; relevant code references replace copied inventories.
- Implementing files: [src/kiyo/framework/memory-specification.md:9](../../src/kiyo/framework/memory-specification.md); [src/kiyo/templates/memory/integrations.md:11](../../src/kiyo/templates/memory/integrations.md); [src/kiyo/templates/memory/index.md:11](../../src/kiyo/templates/memory/index.md).
- Skills/shared procedures: init memory; linked files above define the shared steps.
- Actual inspection: Durable claims and source pointers replace duplicated endpoint/method inventories.
- Test cases: TC-REQ-018 **PLANNED**; G10 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [MSK-15](../../tests/behavioral/memory/skill-scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G10 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Full durable-content selection acceptance lacks a dedicated executed case.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-019

- Criterion: [AC-019](REQUIREMENTS.md#req-019). Memory entries label knowledge type and decision status; observations or proposals cannot become approved decisions without recorded authority, and divergent current code remains distinguishable from intended design.
- Implementing files: [src/kiyo/framework/memory-specification.md:9](../../src/kiyo/framework/memory-specification.md); [src/kiyo/templates/memory/decisions.md:11](../../src/kiyo/templates/memory/decisions.md); [src/kiyo/workflows/architecture.md:3](../../src/kiyo/workflows/architecture.md).
- Skills/shared procedures: memory architecture requirement; linked files above define the shared steps.
- Actual inspection: Observation/proposal/decision plus approval provenance preserve intended versus observed structure.
- Test cases: TC-REQ-019 **PLANNED**; G10 selected static checks; BEH-REQ-03, BEH-REQ-04, BEH-ARCH-01 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-01](../../tests/behavioral/architecture/scenarios.md), [ARC-08](../../tests/behavioral/architecture/scenarios.md), [MSK-01](../../tests/behavioral/memory/skill-scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G10 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-REQ-03, BEH-REQ-04, BEH-ARCH-01).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Templates and bounded trials do not prove all agent classification/approval handling.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-020

- Criterion: [AC-020](REQUIREMENTS.md#req-020). Memory templates require each listed field; populated entries cite observed evidence, use actual review dates and limit claims to inspected scope; unavailable evidence is marked unknown rather than fabricated.
- Implementing files: [src/kiyo/framework/memory-specification.md:9](../../src/kiyo/framework/memory-specification.md); [src/kiyo/templates/memory/project.md:11](../../src/kiyo/templates/memory/project.md); [src/kiyo/templates/memory/decisions.md:11](../../src/kiyo/templates/memory/decisions.md).
- Skills/shared procedures: init memory; linked files above define the shared steps.
- Actual inspection: Entry-level identity/source/status/scope/uncertainty fields and distinct modification/verification dates are concrete.
- Test cases: TC-REQ-020 **PLANNED**; G10 selected static checks; BEH-INIT-02, BEH-MEM-01, BEH-MEM-03 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [INIT-01](../../tests/behavioral/init/scenarios.md), [INIT-02](../../tests/behavioral/init/scenarios.md), [INIT-06](../../tests/behavioral/init/scenarios.md), [INIT-14](../../tests/behavioral/init/scenarios.md), [MSK-01](../../tests/behavioral/memory/skill-scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G10 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-INIT-02, BEH-MEM-01, BEH-MEM-03).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Real-populated entry/date behavior across all modes and target states unverified.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-021

- Criterion: [AC-021](REQUIREMENTS.md#req-021). An invoked check compares scoped memory claims with current files and reports differences; documentation makes no real-time monitoring claim and no watcher or background process is introduced.
- Implementing files: [src/kiyo/framework/memory-modes.md:3](../../src/kiyo/framework/memory-modes.md); [src/kiyo/workflows/memory-lifecycle.md:8](../../src/kiyo/workflows/memory-lifecycle.md); [docs/user/memory.md:13](../../docs/user/memory.md).
- Skills/shared procedures: memory architecture; linked files above define the shared steps.
- Actual inspection: Only invoked scoped drift checking; no watcher or real-time claim.
- Test cases: TC-REQ-021 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-MEM-02 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [MSK-02](../../tests/behavioral/memory/skill-scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-MEM-02).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No comprehensive branch/manual-edit live evaluation.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-022

- Criterion: [AC-022](REQUIREMENTS.md#req-022). A detected contradiction reports both evidence and approved intent; code drift never automatically rewrites an approved decision, and a proposed decision change requires applicable human approval.
- Implementing files: [src/kiyo/framework/memory-specification.md:9](../../src/kiyo/framework/memory-specification.md); [src/kiyo/workflows/architecture.md:3](../../src/kiyo/workflows/architecture.md); [src/kiyo/templates/reports/memory-architecture-drift-report.md:32](../../src/kiyo/templates/reports/memory-architecture-drift-report.md).
- Skills/shared procedures: memory architecture; linked files above define the shared steps.
- Actual inspection: Mapperly approved intent versus AutoMapper usage is conflict, not automatic decision rewriting.
- Test cases: TC-REQ-022 **PLANNED**; G10 selected static checks; BEH-ARCH-02, BEH-ARCH-03, BEH-X-09 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-01](../../tests/behavioral/architecture/scenarios.md), [MSK-05](../../tests/behavioral/memory/skill-scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G10 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-ARCH-02, BEH-ARCH-03, BEH-X-09).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Bounded source-guided drift result is not native acceptance or production proof.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-023

- Criterion: [AC-023](REQUIREMENTS.md#req-023). Closure reports memory impact; writes occur only for necessary authorized changes, and a no-change outcome leaves memory contents and timestamps untouched.
- Implementing files: [src/kiyo/framework/memory-modes.md:3](../../src/kiyo/framework/memory-modes.md); [src/kiyo/workflows/memory-lifecycle.md:8](../../src/kiyo/workflows/memory-lifecycle.md); [src/kiyo/framework/definition-of-done.md:8](../../src/kiyo/framework/definition-of-done.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Four Memory Impact values, authorized mandatory delta and no-op byte/date preservation are explicit.
- Test cases: TC-REQ-023 **PLANNED**; G08, G10 selected static checks; BEH-MEM-01, BEH-MEM-03, BEH-X-09 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-01](../../tests/behavioral/architecture/scenarios.md), [IMP-07](../../tests/behavioral/implement/scenarios.md), [IMP-15](../../tests/behavioral/implement/scenarios.md), [MSK-03](../../tests/behavioral/memory/skill-scenarios.md), [REV-03](../../tests/behavioral/review/scenarios.md), [REV-13](../../tests/behavioral/review/scenarios.md), [RQM-04](../../tests/behavioral/requirement/scenarios.md), [RQM-07](../../tests/behavioral/requirement/scenarios.md), [TST-16](../../tests/behavioral/test/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G08 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G10 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-MEM-01, BEH-MEM-03, BEH-X-09).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. One recorded source-guided repeat sync is limited; host idempotence and timestamp behavior unverified.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-024

- Criterion: [AC-024](REQUIREMENTS.md#req-024). Procedures scope memory to repository/worktree identity, record inspection gaps and handle missing files; before writing they detect changed inputs and reconcile or stop without overwriting concurrent human edits.
- Implementing files: [src/kiyo/framework/memory-specification.md:9](../../src/kiyo/framework/memory-specification.md); [src/kiyo/workflows/memory-lifecycle.md:8](../../src/kiyo/workflows/memory-lifecycle.md); [src/kiyo/framework/memory-modes.md:3](../../src/kiyo/framework/memory-modes.md).
- Skills/shared procedures: memory init; linked files above define the shared steps.
- Actual inspection: Branch/worktree/component identity, moved/deleted sources and latest-entry conflict checks have specified handling.
- Test cases: TC-REQ-024 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-INIT-03, BEH-INIT-04, BEH-MEM-03, BEH-MEM-04 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-04](../../tests/behavioral/architecture/scenarios.md), [INIT-03](../../tests/behavioral/init/scenarios.md), [INIT-04](../../tests/behavioral/init/scenarios.md), [INIT-05](../../tests/behavioral/init/scenarios.md), [INIT-09](../../tests/behavioral/init/scenarios.md), [INIT-14](../../tests/behavioral/init/scenarios.md), [INIT-15](../../tests/behavioral/init/scenarios.md), [MSK-07](../../tests/behavioral/memory/skill-scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-INIT-03, BEH-INIT-04, BEH-MEM-03, BEH-MEM-04).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No complete adversarial concurrency/worktree/deletion matrix execution; no atomicity guarantee.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-025

- Criterion: [AC-025](REQUIREMENTS.md#req-025). A Markdown decision procedure maps user intent to the eight public skills or shared submodes, records ambiguities and contains no runtime router program or orchestration service.
- Implementing files: [src/kiyo/workflows/workflow-router.md:3](../../src/kiyo/workflows/workflow-router.md); [tests/behavioral/routing/truth-table.md:20](../../tests/behavioral/routing/truth-table.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Markdown input/output procedure maps exactly eight intents and mixed-intent handling; no executable router.
- Test cases: TC-REQ-025 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-X-14 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ROUTE-01](../../tests/behavioral/routing/truth-table.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-14).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Routing table is expected behavior; target accuracy unmeasured.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-026

- Criterion: [AC-026](REQUIREMENTS.md#req-026). Public catalogs and native overlays expose exactly those eight skills; Workflow Router, Governance Review, Skill Audit and Self-check remain shared procedures/submodes without a ninth public skill.
- Implementing files: [tools/packaging-inputs.json:1](../../tools/packaging-inputs.json); [tests/static/contracts.py:1](../../tests/static/contracts.py); [docs/user/skills.md:23](../../docs/user/skills.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Canonical and all three native payloads have exactly eight entries; helpers remain references/submodes.
- Test cases: TC-REQ-026 **PLANNED**; G01, G02, G03 selected static checks; BEH-X-14 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-01](../../tests/behavioral/architecture/scenarios.md), [IMP-11](../../tests/behavioral/implement/scenarios.md), [INIT-13](../../tests/behavioral/init/scenarios.md), [MSK-01](../../tests/behavioral/memory/skill-scenarios.md), [RQM-06](../../tests/behavioral/requirement/scenarios.md), [SEC-01](../../tests/behavioral/security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G01 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G02 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-14); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Native component discovery only observed for Claude; no full Skill invocation acceptance.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-05](#gap29-05).

### REQ-027

- Criterion: [AC-027](REQUIREMENTS.md#req-027). Every skill declares its access contract and mode transitions; a read-only run changes no source, memory or report files, and any mode requiring writes or execution respects scoped authorization.
- Implementing files: [src/kiyo/workflows/read-only-flow.md:3](../../src/kiyo/workflows/read-only-flow.md); [src/kiyo/framework/test-mode-safety.md:8](../../src/kiyo/framework/test-mode-safety.md); [src/kiyo/framework/memory-modes.md:3](../../src/kiyo/framework/memory-modes.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Entry contracts separate reading, writing, execution and authorized report output.
- Test cases: TC-REQ-027 **PLANNED**; G03, G07, G15 selected static checks; BEH-TEST-03, BEH-X-10 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-09](../../tests/behavioral/architecture/scenarios.md), [FLOW-08](../../tests/behavioral/routing/truth-table.md), [IMP-04](../../tests/behavioral/implement/scenarios.md), [IMP-11](../../tests/behavioral/implement/scenarios.md), [INIT-01](../../tests/behavioral/init/scenarios.md), [INIT-04](../../tests/behavioral/init/scenarios.md), [INIT-07](../../tests/behavioral/init/scenarios.md), [INIT-10](../../tests/behavioral/init/scenarios.md), [INIT-13](../../tests/behavioral/init/scenarios.md), [MSK-01](../../tests/behavioral/memory/skill-scenarios.md), [REV-04](../../tests/behavioral/review/scenarios.md), [REV-07](../../tests/behavioral/review/scenarios.md), [REV-10](../../tests/behavioral/review/scenarios.md), [REV-16](../../tests/behavioral/review/scenarios.md), [ROUTE-02](../../tests/behavioral/routing/truth-table.md), [ROUTE-27](../../tests/behavioral/routing/truth-table.md), [RQM-06](../../tests/behavioral/requirement/scenarios.md), [RQM-07](../../tests/behavioral/requirement/scenarios.md), [RQM-09](../../tests/behavioral/requirement/scenarios.md), [RQM-12](../../tests/behavioral/requirement/scenarios.md), [SEC-02](../../tests/behavioral/security/scenarios.md), [SEC-06](../../tests/behavioral/security/scenarios.md), [SEC-17](../../tests/behavioral/security/scenarios.md), [TST-01](../../tests/behavioral/test/scenarios.md), [TST-06](../../tests/behavioral/test/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G15 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-TEST-03, BEH-X-10).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Static clauses do not enforce read-only effects; complete before/after/tool evidence missing.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-028

- Criterion: [AC-028](REQUIREMENTS.md#req-028). A review request remains a review; a mismatch is explained with an appropriate proposal or clarifying question, and implementation begins only when the user's authorized intent includes edits.
- Implementing files: [src/kiyo/workflows/workflow-router.md:3](../../src/kiyo/workflows/workflow-router.md); [src/kiyo/skills/implement/SKILL.md:16](../../src/kiyo/skills/implement/SKILL.md); [src/kiyo/skills/test/SKILL.md:17](../../src/kiyo/skills/test/SKILL.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Explicit selection mismatch is reported; review and auth-redesign/Test mismatch do not silently gain write scope.
- Test cases: TC-REQ-028 **PLANNED**; G07 selected static checks; BEH-REV-01, BEH-REV-04, BEH-X-01, BEH-X-05, BEH-X-10 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-09](../../tests/behavioral/architecture/scenarios.md), [REV-01](../../tests/behavioral/review/scenarios.md), [REV-04](../../tests/behavioral/review/scenarios.md), [REV-11](../../tests/behavioral/review/scenarios.md), [ROUTE-13](../../tests/behavioral/routing/truth-table.md), [ROUTE-14](../../tests/behavioral/routing/truth-table.md), [ROUTE-29](../../tests/behavioral/routing/truth-table.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-REV-01, BEH-REV-04, BEH-X-01, BEH-X-05, BEH-X-10).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Routing/permission outcomes remain untested on native targets.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-029

- Criterion: [AC-029](REQUIREMENTS.md#req-029). Flow adjusts to task size and risk, declares a repair-attempt bound and stops with honest unresolved findings when exhausted; scope-changing repairs are reassessed before further edits.
- Implementing files: [src/kiyo/workflows/adaptive-flow.md:3](../../src/kiyo/workflows/adaptive-flow.md); [src/kiyo/workflows/repair-and-handoff.md:3](../../src/kiyo/workflows/repair-and-handoff.md).
- Skills/shared procedures: implement test; linked files above define the shared steps.
- Actual inspection: Tiny/Normal/High-impact and two unsuccessful repair-cycle bound preserve scope and attempts across handoff.
- Test cases: TC-REQ-029 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [FLOW-02](../../tests/behavioral/routing/truth-table.md), [FLOW-03](../../tests/behavioral/routing/truth-table.md), [FLOW-05](../../tests/behavioral/routing/truth-table.md), [FLOW-09](../../tests/behavioral/routing/truth-table.md), [IMP-01](../../tests/behavioral/implement/scenarios.md), [IMP-10](../../tests/behavioral/implement/scenarios.md), [IMP-14](../../tests/behavioral/implement/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: This dated manual file/contract inspection; no automated behavioral result.
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Repair exhaustion and context-resume behavior need a complete executed acceptance case.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-030

- Criterion: [AC-030](REQUIREMENTS.md#req-030). Small-task guidance permits a shorter plan/report while still checking authority, applicable approvals, risks, actual verification evidence and memory impact.
- Implementing files: [src/kiyo/workflows/adaptive-flow.md:3](../../src/kiyo/workflows/adaptive-flow.md); [src/kiyo/framework/bootstrap.md:6](../../src/kiyo/framework/bootstrap.md); [src/kiyo/templates/reports/compact-task-report.md:1](../../src/kiyo/templates/reports/compact-task-report.md).
- Skills/shared procedures: implement; linked files above define the shared steps.
- Actual inspection: Tiny compresses presentation while retaining authority/risk/approval/evidence/Memory Impact.
- Test cases: TC-REQ-030 **PLANNED**; G14 selected static checks; BEH-IMPL-01, BEH-X-14 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [FLOW-07](../../tests/behavioral/routing/truth-table.md), [IMP-01](../../tests/behavioral/implement/scenarios.md), [ROUTE-25](../../tests/behavioral/routing/truth-table.md), [ROUTE-26](../../tests/behavioral/routing/truth-table.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G14 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-IMPL-01, BEH-X-14).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Native Tiny behavior and actual context overhead unmeasured.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-031

- Criterion: [AC-031](REQUIREMENTS.md#req-031). Requirement output includes every listed field, with observable acceptance criteria and explicit unknowns; empty or inapplicable fields are explained rather than silently omitted.
- Implementing files: [src/kiyo/framework/engineering/requirements.md:7](../../src/kiyo/framework/engineering/requirements.md); [src/kiyo/templates/requirement.md:15](../../src/kiyo/templates/requirement.md); [src/kiyo/framework/requirement-readiness.md:9](../../src/kiyo/framework/requirement-readiness.md).
- Skills/shared procedures: requirement; linked files above define the shared steps.
- Actual inspection: Fourteen-field sourced requirement/readiness contract supplies all requested engineering fields.
- Test cases: TC-REQ-031 **PLANNED**; G03 selected static checks; BEH-REQ-01, BEH-REQ-02, BEH-IMPL-03 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ENG-01](../../tests/behavioral/engineering/scenarios.md), [RQM-01](../../tests/behavioral/requirement/scenarios.md), [RQM-02](../../tests/behavioral/requirement/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-REQ-01, BEH-REQ-02, BEH-IMPL-03).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Host outputs not exhaustively evaluated against all fields; missing business decisions must remain open.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-032

- Criterion: [AC-032](REQUIREMENTS.md#req-032). The procedure inspects available authorized facts before questioning; proposals remain labeled unapproved, unknowns remain explicit and questions target decisions that materially block the current scope.
- Implementing files: [src/kiyo/framework/trust-and-authority.md:9](../../src/kiyo/framework/trust-and-authority.md); [src/kiyo/workflows/requirement.md:3](../../src/kiyo/workflows/requirement.md); [src/kiyo/framework/requirement-readiness.md:9](../../src/kiyo/framework/requirement-readiness.md).
- Skills/shared procedures: requirement implement; linked files above define the shared steps.
- Actual inspection: Authorized discovery before questions and separate facts/user requirements/proposals/decisions are actionable.
- Test cases: TC-REQ-032 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-REQ-01, BEH-REQ-02, BEH-REQ-03, BEH-IMPL-03, BEH-REV-02 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ENG-01](../../tests/behavioral/engineering/scenarios.md), [REV-02](../../tests/behavioral/review/scenarios.md), [ROUTE-11](../../tests/behavioral/routing/truth-table.md), [ROUTE-17](../../tests/behavioral/routing/truth-table.md), [RQM-01](../../tests/behavioral/requirement/scenarios.md), [RQM-08](../../tests/behavioral/requirement/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-REQ-01, BEH-REQ-02, BEH-REQ-03, BEH-IMPL-03, BEH-REV-02).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No broad unseen-request hallucination/interruptions measurement.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-033

- Criterion: [AC-033](REQUIREMENTS.md#req-033). Implementation rationale identifies applicable existing patterns; deviations are justified, and an insecure legacy pattern is flagged with a scoped safer proposal instead of copied unquestioningly.
- Implementing files: [src/kiyo/framework/engineering/architecture.md:6](../../src/kiyo/framework/engineering/architecture.md); [src/kiyo/framework/engineering/coding.md:7](../../src/kiyo/framework/engineering/coding.md); [src/kiyo/profiles/extension-contract.md:9](../../src/kiyo/profiles/extension-contract.md).
- Skills/shared procedures: implement architecture review; linked files above define the shared steps.
- Actual inspection: Closest safe pattern wins; insecure legacy is flagged and no unsolicited architecture is imposed.
- Test cases: TC-REQ-033 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-ARCH-01, BEH-ARCH-04 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-03](../../tests/behavioral/architecture/scenarios.md), [ENG-02](../../tests/behavioral/engineering/scenarios.md), [ENG-04](../../tests/behavioral/engineering/scenarios.md), [ENG-07](../../tests/behavioral/engineering/scenarios.md), [ENG-16](../../tests/behavioral/engineering/scenarios.md), [IMP-16](../../tests/behavioral/implement/scenarios.md), [ROUTE-03](../../tests/behavioral/routing/truth-table.md), [ROUTE-04](../../tests/behavioral/routing/truth-table.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-ARCH-01, BEH-ARCH-04).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Legacy/insecure-pattern native regression tests still unrun.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-034

- Criterion: [AC-034](REQUIREMENTS.md#req-034). Final diff maps changes to authorized requirements, flags unrelated changes and preserves user edits; no cleanup or reversion of others' work is performed just to produce a clean diff.
- Implementing files: [src/kiyo/framework/engineering/change-scope.md:6](../../src/kiyo/framework/engineering/change-scope.md); [src/kiyo/skills/implement/SKILL.md:16](../../src/kiyo/skills/implement/SKILL.md).
- Skills/shared procedures: implement review; linked files above define the shared steps.
- Actual inspection: Reread, minimal authorized diff and human-work preservation forbid unrelated cleanup/reversion.
- Test cases: TC-REQ-034 **PLANNED**; G07 selected static checks; BEH-IMPL-01, BEH-IMPL-04, BEH-X-14 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ENG-03](../../tests/behavioral/engineering/scenarios.md), [ENG-05](../../tests/behavioral/engineering/scenarios.md), [IMP-08](../../tests/behavioral/implement/scenarios.md), [IMP-16](../../tests/behavioral/implement/scenarios.md), [ROUTE-04](../../tests/behavioral/routing/truth-table.md), [ROUTE-25](../../tests/behavioral/routing/truth-table.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-IMPL-01, BEH-IMPL-04, BEH-X-14).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Source-guided edits do not establish all concurrent human-edit behavior.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-035

- Criterion: [AC-035](REQUIREMENTS.md#req-035). Before implementation a short plan names affected areas and risks; newly discovered changes in any listed dimension trigger impact reassessment and required scoped approval before dependent work.
- Implementing files: [src/kiyo/templates/short-plan.md:18](../../src/kiyo/templates/short-plan.md); [src/kiyo/workflows/implement-flow.md:3](../../src/kiyo/workflows/implement-flow.md); [src/kiyo/workflows/adaptive-flow.md:3](../../src/kiyo/workflows/adaptive-flow.md).
- Skills/shared procedures: implement architecture; linked files above define the shared steps.
- Actual inspection: Plan captures scope/effects/checks and material API/schema/architecture changes trigger reassessment.
- Test cases: TC-REQ-035 **PLANNED**; G03 selected static checks; BEH-ARCH-04, BEH-X-11 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ENG-04](../../tests/behavioral/engineering/scenarios.md), [ENG-16](../../tests/behavioral/engineering/scenarios.md), [FLOW-05](../../tests/behavioral/routing/truth-table.md), [IMP-05](../../tests/behavioral/implement/scenarios.md), [IMP-09](../../tests/behavioral/implement/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-ARCH-04, BEH-X-11).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Scope expansion and valid approval reuse not evaluated across native hosts.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-036

- Criterion: [AC-036](REQUIREMENTS.md#req-036). Engineering guidance covers all listed concerns and records applicable checks or justified non-applicability; reports reference concrete inspected behavior rather than blanket quality claims.
- Implementing files: [src/kiyo/framework/engineering/coding.md:7](../../src/kiyo/framework/engineering/coding.md); [src/kiyo/framework/engineering/quality.md:8](../../src/kiyo/framework/engineering/quality.md); [src/kiyo/agent-security/application-security.md:3](../../src/kiyo/agent-security/application-security.md).
- Skills/shared procedures: implement review security; linked files above define the shared steps.
- Actual inspection: Action/evidence rows cover validation/errors/nulls/logs and contextual quality/operational concerns.
- Test cases: TC-REQ-036 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [ENG-04](../../tests/behavioral/engineering/scenarios.md), [ENG-12](../../tests/behavioral/engineering/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: This dated manual file/contract inspection; no automated behavioral result.
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No exhaustive check of contextual applicability or quality outcomes; static wording is not application verification.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-037

- Criterion: [AC-037](REQUIREMENTS.md#req-037). Four named profiles exist and can be selected only when relevant; extension guidance defines how React, Java or company rules fit without changing the canonical core or requiring migration.
- Implementing files: [src/kiyo/profiles/dotnet.md:1](../../src/kiyo/profiles/dotnet.md); [src/kiyo/profiles/angular.md:1](../../src/kiyo/profiles/angular.md); [src/kiyo/profiles/python.md:1](../../src/kiyo/profiles/python.md); [src/kiyo/profiles/postgresql.md:1](../../src/kiyo/profiles/postgresql.md); [src/kiyo/profiles/extension-contract.md:9](../../src/kiyo/profiles/extension-contract.md).
- Skills/shared procedures: init implement test architecture; linked files above define the shared steps.
- Actual inspection: Four discovery-first optional profiles preserve existing stack; React/Java/company extensions are bounded outlines.
- Test cases: TC-REQ-037 **PLANNED**; G04 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [ENG-02](../../tests/behavioral/engineering/scenarios.md), [ENG-06](../../tests/behavioral/engineering/scenarios.md), [ENG-14](../../tests/behavioral/engineering/scenarios.md), [ENG-15](../../tests/behavioral/engineering/scenarios.md), [ORG-02](../../tests/behavioral/organization-policy/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G04 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No executed stack compatibility recipes; do not market outlines as full profiles.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-038

- Criterion: [AC-038](REQUIREMENTS.md#req-038). Test planning maps changed behavior and risk to suitable layers with reasons for selected or omitted layers; it avoids requiring every layer for every change.
- Implementing files: [src/kiyo/framework/engineering/testing.md:7](../../src/kiyo/framework/engineering/testing.md); [src/kiyo/workflows/test.md:3](../../src/kiyo/workflows/test.md); [src/kiyo/templates/test-plan.md:1](../../src/kiyo/templates/test-plan.md).
- Skills/shared procedures: test implement; linked files above define the shared steps.
- Actual inspection: Layer selection follows changed behavior and risk with reasons, not every-layer mandate.
- Test cases: TC-REQ-038 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-IMPL-02, BEH-TEST-01, BEH-TEST-03 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ENG-03](../../tests/behavioral/engineering/scenarios.md), [ENG-10](../../tests/behavioral/engineering/scenarios.md), [ENG-11](../../tests/behavioral/engineering/scenarios.md), [ENG-13](../../tests/behavioral/engineering/scenarios.md), [ENG-16](../../tests/behavioral/engineering/scenarios.md), [TST-01](../../tests/behavioral/test/scenarios.md), [TST-06](../../tests/behavioral/test/scenarios.md), [TST-17](../../tests/behavioral/test/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-IMPL-02, BEH-TEST-01, BEH-TEST-03).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Actual test-strategy selection on native hosts unverified.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-039

- Criterion: [AC-039](REQUIREMENTS.md#req-039). Check reports separate observed pre-existing failure, supported flaky classification, environmental blockers and new regression; unknown cause stays unresolved rather than being assigned to a convenient category.
- Implementing files: [src/kiyo/workflows/repair-and-handoff.md:3](../../src/kiyo/workflows/repair-and-handoff.md); [src/kiyo/framework/evidence-contract.md:7](../../src/kiyo/framework/evidence-contract.md); [src/kiyo/templates/reports/test-report.md:26](../../src/kiyo/templates/reports/test-report.md).
- Skills/shared procedures: test implement; linked files above define the shared steps.
- Actual inspection: Baseline/new regression/environment/unresolved/flaky causes need distinct evidence.
- Test cases: TC-REQ-039 **PLANNED**; G08 selected static checks; BEH-IMPL-02, BEH-TEST-02, BEH-X-16 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [EVID-05](../../tests/behavioral/verification/scenarios.md), [EVID-06](../../tests/behavioral/verification/scenarios.md), [FLOW-01](../../tests/behavioral/routing/truth-table.md), [FLOW-02](../../tests/behavioral/routing/truth-table.md), [FLOW-04](../../tests/behavioral/routing/truth-table.md), [IMP-06](../../tests/behavioral/implement/scenarios.md), [IMP-10](../../tests/behavioral/implement/scenarios.md), [IMP-13](../../tests/behavioral/implement/scenarios.md), [TST-04](../../tests/behavioral/test/scenarios.md), [TST-05](../../tests/behavioral/test/scenarios.md), [TST-14](../../tests/behavioral/test/scenarios.md), [TST-18](../../tests/behavioral/test/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G08 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-IMPL-02, BEH-TEST-02, BEH-X-16).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Native classification not measured; one fail/pass is not proof of flakiness.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-040

- Criterion: [AC-040](REQUIREMENTS.md#req-040). Every check records one exact status, inspected/executed scope, result evidence or a reason it did not run; a test file's existence never counts as PASS.
- Implementing files: [src/kiyo/framework/evidence-contract.md:7](../../src/kiyo/framework/evidence-contract.md); [src/kiyo/templates/reports/engineering-report.md:1](../../src/kiyo/templates/reports/engineering-report.md); [src/kiyo/templates/reports/test-report.md:26](../../src/kiyo/templates/reports/test-report.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Nine-field contract and exact five statuses reject source-file-as-PASS and stale final-state evidence.
- Test cases: TC-REQ-040 **PLANNED**; G08 selected static checks; BEH-IMPL-02, BEH-REV-01, BEH-REV-02, BEH-TEST-01, BEH-TEST-02, BEH-TEST-03, BEH-TEST-04, BEH-X-03, BEH-X-07, BEH-X-16 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-04](../../tests/behavioral/architecture/scenarios.md), [EVID-01](../../tests/behavioral/verification/scenarios.md), [EVID-15](../../tests/behavioral/verification/scenarios.md), [EVID-19](../../tests/behavioral/verification/scenarios.md), [FLOW-09](../../tests/behavioral/routing/truth-table.md), [IMP-02](../../tests/behavioral/implement/scenarios.md), [IMP-06](../../tests/behavioral/implement/scenarios.md), [IMP-10](../../tests/behavioral/implement/scenarios.md), [IMP-13](../../tests/behavioral/implement/scenarios.md), [MSK-01](../../tests/behavioral/memory/skill-scenarios.md), [REV-01](../../tests/behavioral/review/scenarios.md), [REV-02](../../tests/behavioral/review/scenarios.md), [REV-05](../../tests/behavioral/review/scenarios.md), [REV-10](../../tests/behavioral/review/scenarios.md), [REV-14](../../tests/behavioral/review/scenarios.md), [TST-03](../../tests/behavioral/test/scenarios.md), [TST-09](../../tests/behavioral/test/scenarios.md), [TST-14](../../tests/behavioral/test/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G08 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-IMPL-02, BEH-REV-01, BEH-REV-02, BEH-TEST-01, BEH-TEST-02, BEH-TEST-03, BEH-TEST-04, BEH-X-03, BEH-X-07, BEH-X-16).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Agent evidence honesty still untested; selected tooling checks do not prove agent adherence.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-13](#gap29-13), [GAP29-04](#gap29-04).

### REQ-041

- Criterion: [AC-041](REQUIREMENTS.md#req-041). Before execution the agent inspects invoked scripts and relevant side effects, including writes, network, installs and production access; unsafe or unauthorized execution is withheld with a specific reason.
- Implementing files: [src/kiyo/framework/test-mode-safety.md:8](../../src/kiyo/framework/test-mode-safety.md); [src/kiyo/workflows/test.md:3](../../src/kiyo/workflows/test.md); [src/kiyo/governance/dangerous-actions.md:3](../../src/kiyo/governance/dangerous-actions.md).
- Skills/shared procedures: test implement; linked files above define the shared steps.
- Actual inspection: Scripts/helpers/setup/target/network/data/artifact side effects preflight before authorized execution.
- Test cases: TC-REQ-041 **PLANNED**; G07 selected static checks; BEH-TEST-02, BEH-TEST-04, BEH-X-06 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [EVID-02](../../tests/behavioral/verification/scenarios.md), [EVID-14](../../tests/behavioral/verification/scenarios.md), [REV-10](../../tests/behavioral/review/scenarios.md), [REV-12](../../tests/behavioral/review/scenarios.md), [REV-16](../../tests/behavioral/review/scenarios.md), [ROUTE-22](../../tests/behavioral/routing/truth-table.md), [ROUTE-30](../../tests/behavioral/routing/truth-table.md), [TST-03](../../tests/behavioral/test/scenarios.md), [TST-09](../../tests/behavioral/test/scenarios.md), [TST-18](../../tests/behavioral/test/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-TEST-02, BEH-TEST-04, BEH-X-06).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Untrusted script adversarial host case not run; test naming alone cannot authorize effects.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-042

- Criterion: [AC-042](REQUIREMENTS.md#req-042). Closure evaluates all five review dimensions or explains non-applicability, links findings to evidence and labels self-review as self-review rather than an independent audit.
- Implementing files: [src/kiyo/framework/definition-of-done.md:8](../../src/kiyo/framework/definition-of-done.md); [src/kiyo/workflows/implement-flow.md:3](../../src/kiyo/workflows/implement-flow.md); [src/kiyo/framework/reporting-contract.md:7](../../src/kiyo/framework/reporting-contract.md).
- Skills/shared procedures: implement; linked files above define the shared steps.
- Actual inspection: Five review dimensions and self-review labeling are explicit closure obligations.
- Test cases: TC-REQ-042 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [EVID-07](../../tests/behavioral/verification/scenarios.md), [EVID-09](../../tests/behavioral/verification/scenarios.md), [EVID-12](../../tests/behavioral/verification/scenarios.md), [ROUTE-28](../../tests/behavioral/routing/truth-table.md), [SEC-09](../../tests/behavioral/security/scenarios.md), [SEC-13](../../tests/behavioral/security/scenarios.md), [SEC-14](../../tests/behavioral/security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: This dated manual file/contract inspection; no automated behavioral result.
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No full evidence-backed self-review quality acceptance run.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-043

- Criterion: [AC-043](REQUIREMENTS.md#req-043). Traceability records link requirement criteria to implementing files, planned/existing test cases and actual execution evidence; missing links remain gaps, and creating a PR or commit is not a prerequisite.
- Implementing files: [src/kiyo/framework/evidence-contract.md:7](../../src/kiyo/framework/evidence-contract.md); [docs/build/TRACEABILITY.md:1](../../docs/build/TRACEABILITY.md); [docs/build/FINAL-GAP-AUDIT.md:1](../../docs/build/FINAL-GAP-AUDIT.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Current audit links every AC to actual files, cases, evidence and remaining acceptance; no PR/commit required.
- Test cases: TC-REQ-043 **PLANNED**; G16 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [EVID-17](../../tests/behavioral/verification/scenarios.md), [RQM-02](../../tests/behavioral/requirement/scenarios.md), [RQM-11](../../tests/behavioral/requirement/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G16 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Full acceptance cases remain reserved/planned and may not be implied by linked static results.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-09](#gap29-09), [GAP29-11](#gap29-11).

### REQ-044

- Criterion: [AC-044](REQUIREMENTS.md#req-044). Completion rules identify mandatory checks for the current scope; DONE is withheld when required checks or scope remain incomplete, and closure includes memory impact even when no write is needed.
- Implementing files: [src/kiyo/framework/definition-of-done.md:8](../../src/kiyo/framework/definition-of-done.md); [src/kiyo/framework/evidence-contract.md:7](../../src/kiyo/framework/evidence-contract.md); [src/kiyo/framework/memory-specification.md:9](../../src/kiyo/framework/memory-specification.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Mode-specific completion holds mandatory unrun/failing checks and missing sync; Memory Impact required.
- Test cases: TC-REQ-044 **PLANNED**; G08 selected static checks; BEH-REV-03, BEH-X-07, BEH-X-16 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-04](../../tests/behavioral/architecture/scenarios.md), [EVID-07](../../tests/behavioral/verification/scenarios.md), [EVID-20](../../tests/behavioral/verification/scenarios.md), [FLOW-09](../../tests/behavioral/routing/truth-table.md), [IMP-06](../../tests/behavioral/implement/scenarios.md), [IMP-13](../../tests/behavioral/implement/scenarios.md), [MSK-03](../../tests/behavioral/memory/skill-scenarios.md), [REV-03](../../tests/behavioral/review/scenarios.md), [REV-06](../../tests/behavioral/review/scenarios.md), [REV-11](../../tests/behavioral/review/scenarios.md), [ROUTE-09](../../tests/behavioral/routing/truth-table.md), [RQM-05](../../tests/behavioral/requirement/scenarios.md), [RQM-08](../../tests/behavioral/requirement/scenarios.md), [RQM-10](../../tests/behavioral/requirement/scenarios.md), [RQM-12](../../tests/behavioral/requirement/scenarios.md), [TST-04](../../tests/behavioral/test/scenarios.md), [TST-06](../../tests/behavioral/test/scenarios.md), [TST-09](../../tests/behavioral/test/scenarios.md), [TST-16](../../tests/behavioral/test/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G08 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-REV-03, BEH-X-07, BEH-X-16).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Actual agent completion discipline across workflows unverified.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-13](#gap29-13), [GAP29-04](#gap29-04).

### REQ-045

- Criterion: [AC-045](REQUIREMENTS.md#req-045). Reporting defines and uses the four exact task states; completed documentation does not imply implemented product features, and blocked work or required decisions identify the remaining action.
- Implementing files: [src/kiyo/framework/definition-of-done.md:8](../../src/kiyo/framework/definition-of-done.md); [src/kiyo/framework/reporting-contract.md:7](../../src/kiyo/framework/reporting-contract.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Four exact task statuses have scoped meanings distinct from readiness and checks.
- Test cases: TC-REQ-045 **PLANNED**; G08 selected static checks; BEH-X-07 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [EVID-07](../../tests/behavioral/verification/scenarios.md), [EVID-18](../../tests/behavioral/verification/scenarios.md), [EVID-20](../../tests/behavioral/verification/scenarios.md), [FLOW-03](../../tests/behavioral/routing/truth-table.md), [FLOW-04](../../tests/behavioral/routing/truth-table.md), [FLOW-09](../../tests/behavioral/routing/truth-table.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G08 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-07).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Native agents may misreport; no automated enforcement.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-046

- Criterion: [AC-046](REQUIREMENTS.md#req-046). Report templates cover actions, outcomes and gaps while omitting secrets/private values outside the authorized scope; they explicitly avoid tamper-proof audit and exhaustive access-log claims.
- Implementing files: [src/kiyo/framework/reporting-contract.md:7](../../src/kiyo/framework/reporting-contract.md); [src/kiyo/templates/reports/engineering-report.md:1](../../src/kiyo/templates/reports/engineering-report.md); [src/kiyo/templates/reports/security-finding.md:1](../../src/kiyo/templates/reports/security-finding.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Redacted chat-default reports exclude secrets/private reasoning and disclaim tamper-proof/access-log guarantees.
- Test cases: TC-REQ-046 **PLANNED**; G11 selected static checks; BEH-X-12 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [EVID-12](../../tests/behavioral/verification/scenarios.md), [EVID-15](../../tests/behavioral/verification/scenarios.md), [EVID-16](../../tests/behavioral/verification/scenarios.md), [EVID-18](../../tests/behavioral/verification/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G11 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-12).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Pattern scans are bounded, not DLP or proof no arbitrary private fact can appear.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-047

- Criterion: [AC-047](REQUIREMENTS.md#req-047). Guidance defines all four levels, their intended permissions/approval expectations and examples; labels identify them as Kiyo's model, with actual authority and enforcement remaining with the native host.
- Implementing files: [src/kiyo/governance/governance-levels.md:3](../../src/kiyo/governance/governance-levels.md); [src/kiyo/governance/decision-examples.md:14](../../src/kiyo/governance/decision-examples.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Kiyo G1/G2/G3/G4 advisory levels assign G4 restriction, never unrestricted autonomy.
- Test cases: TC-REQ-047 **PLANNED**; G08 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [ORG-08](../../tests/behavioral/organization-policy/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G08 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Policy/host behavior is external; G-level text is not native permission.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-048

- Criterion: [AC-048](REQUIREMENTS.md#req-048). Risk assessment records all five dimensions and an evidence-based risk level; governance level is a separate field and never mechanically equated to risk.
- Implementing files: [src/kiyo/governance/risk-assessment.md:3](../../src/kiyo/governance/risk-assessment.md); [src/kiyo/governance/decision-examples.md:14](../../src/kiyo/governance/decision-examples.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Four risk values independent of governance; eight concrete action/context dimensions include uncertainty.
- Test cases: TC-REQ-048 **PLANNED**; G08 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G08 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Risk judgments need scenario execution/human review, not enum conformance alone.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-049

- Criterion: [AC-049](REQUIREMENTS.md#req-049). Approval records identify action, target, environment and applicable limits; a still-valid scoped approval is reused, unrelated work is not covered by blanket approval, and material changes trigger reassessment.
- Implementing files: [src/kiyo/governance/human-approval.md:3](../../src/kiyo/governance/human-approval.md); [src/kiyo/templates/reports/approval-request.md:1](../../src/kiyo/templates/reports/approval-request.md); [src/kiyo/governance/policy-resolution.md:3](../../src/kiyo/governance/policy-resolution.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Concrete action/resources/environment/effects/limits enable valid reuse and reassessment; no AI approval.
- Test cases: TC-REQ-049 **PLANNED**; G07 selected static checks; BEH-IMPL-04, BEH-X-04, BEH-X-10, BEH-X-11 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [EVID-14](../../tests/behavioral/verification/scenarios.md), [IMP-04](../../tests/behavioral/implement/scenarios.md), [IMP-05](../../tests/behavioral/implement/scenarios.md), [IMP-09](../../tests/behavioral/implement/scenarios.md), [IMP-12](../../tests/behavioral/implement/scenarios.md), [ORG-05](../../tests/behavioral/organization-policy/scenarios.md), [ROUTE-26](../../tests/behavioral/routing/truth-table.md), [ROUTE-30](../../tests/behavioral/routing/truth-table.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-IMPL-04, BEH-X-04, BEH-X-10, BEH-X-11).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Authority authenticity and scope handling not verified across targets.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-050

- Criterion: [AC-050](REQUIREMENTS.md#req-050). Policy defines all four classes and how to handle uncertain classification; classification considers content, provenance and applicable policy rather than filename alone, without reading forbidden secrets.
- Implementing files: [src/kiyo/governance/data-handling.md:3](../../src/kiyo/governance/data-handling.md); [src/kiyo/governance/provider-policy.md:3](../../src/kiyo/governance/provider-policy.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Four content/policy-based classes include uncertain/mixed content without credential discovery.
- Test cases: TC-REQ-050 **PLANNED**; G08 selected static checks; BEH-X-12 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ORG-06](../../tests/behavioral/organization-policy/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G08 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-12).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No automatic classification, DLP or guarantee against earlier transmission.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-051

- Criterion: [AC-051](REQUIREMENTS.md#req-051). Procedures request/use only access needed for the scoped task, obey denied capabilities and assign enforcement to the host; Kiyo text cannot grant permissions by itself.
- Implementing files: [src/kiyo/governance/permissions.md:3](../../src/kiyo/governance/permissions.md); [src/kiyo/agent-security/control-ownership.md:13](../../src/kiyo/agent-security/control-ownership.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Least scoped access obeys actual denial; guidance cannot grant tools/files/network.
- Test cases: TC-REQ-051 **PLANNED**; G07 selected static checks; BEH-X-04, BEH-X-06 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ORG-04](../../tests/behavioral/organization-policy/scenarios.md), [ROUTE-22](../../tests/behavioral/routing/truth-table.md), [ROUTE-30](../../tests/behavioral/routing/truth-table.md), [SEC-05](../../tests/behavioral/security/scenarios.md), [SEC-12](../../tests/behavioral/security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-04, BEH-X-06); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Required sandbox/network restrictions belong to observed host controls; still unknown where untested.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-052

- Criterion: [AC-052](REQUIREMENTS.md#req-052). The dangerous-action policy distinguishes producing instructions from executing them and evaluates target/environment effects; production or destructive execution requires applicable scoped authorization before action.
- Implementing files: [src/kiyo/governance/dangerous-actions.md:3](../../src/kiyo/governance/dangerous-actions.md); [src/kiyo/governance/governance-levels.md:3](../../src/kiyo/governance/governance-levels.md); [src/kiyo/profiles/postgresql.md:1](../../src/kiyo/profiles/postgresql.md).
- Skills/shared procedures: implement test security; linked files above define the shared steps.
- Actual inspection: Draft migration and database execution remain separate; actual environment/effects and prohibitions govern.
- Test cases: TC-REQ-052 **PLANNED**; G08 selected static checks; BEH-X-06, BEH-X-11 **NOT_RUN**.
- Actual evidence: [G08 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-06, BEH-X-11).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No authorized production operation executed or required for this audit.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-053

- Criterion: [AC-053](REQUIREMENTS.md#req-053). Proposed dependencies include need, source and available license/security evidence; missing evidence remains explicit, additions require appropriate authorization and no end-user Kiyo runtime dependency is introduced.
- Implementing files: [src/kiyo/governance/dependency-governance.md:3](../../src/kiyo/governance/dependency-governance.md); [tools/release_candidate.py:1](../../tools/release_candidate.py); [docs/release/runbook.md:9](../../docs/release/runbook.md).
- Skills/shared procedures: implement security; linked files above define the shared steps.
- Actual inspection: Need/source/license/security evidence and limits are required; dependency inventory separates developer from payload.
- Test cases: TC-REQ-053 **PLANNED**; G12 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [ENG-03](../../tests/behavioral/engineering/scenarios.md), [ENG-06](../../tests/behavioral/engineering/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G12 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [developer release pipeline — PASS](../../dist/releases/p29-run-02/pipeline.json) (Actual six-stage exit 0; PKG-08 limitation separately retained, no host/model/publication).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. License publication decision and future dependency evidence remain owner/current-source obligations.
- Owner decisions: DEC-001, DEC-002, DEC-003.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-03](#gap29-03).

### REQ-054

- Criterion: [AC-054](REQUIREMENTS.md#req-054). Policy pack templates record owner, status and scope; conflicts are resolved according to native authority or surfaced for decision, and stricter applicable policy is not silently weakened.
- Implementing files: [src/kiyo/framework/project-configuration.md:3](../../src/kiyo/framework/project-configuration.md); [src/kiyo/governance/policy-resolution.md:3](../../src/kiyo/governance/policy-resolution.md); [src/kiyo/templates/policies/organization-policy.md:13](../../src/kiyo/templates/policies/organization-policy.md); [src/kiyo/templates/policies/project-policy.md:15](../../src/kiyo/templates/policies/project-policy.md).
- Skills/shared procedures: init security; linked files above define the shared steps.
- Actual inspection: Seven config fields, optional presets, owner/source/status/scope and exception handling preserve native authority.
- Test cases: TC-REQ-054 **PLANNED**; G11 selected static checks; BEH-SEC-03 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ORG-01](../../tests/behavioral/organization-policy/scenarios.md), [SEC-03](../../tests/behavioral/security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G11 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-SEC-03); [historical bounded source-guided trial report — PASS](../../docs/evidence/organization-policy/forward-trials.md) (Only named trial assertions and retained snapshots in this report; not re-executed, not a native result, not full case coverage).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Unadopted templates are not organization policy; owner/expiry conflict behavior needs live evaluation.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-055

- Criterion: [AC-055](REQUIREMENTS.md#req-055). Guidance uses documented applicable account/provider constraints or UNKNOWN, makes no blanket Enterprise safety assumption and never claims Kiyo itself prevents data egress.
- Implementing files: [src/kiyo/governance/provider-policy.md:3](../../src/kiyo/governance/provider-policy.md); [src/kiyo/governance/data-handling.md:3](../../src/kiyo/governance/data-handling.md).
- Skills/shared procedures: security all; linked files above define the shared steps.
- Actual inspection: Provider/account/model facts separate; Enterprise is not privacy proof; no Kiyo egress enforcement.
- Test cases: TC-REQ-055 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-SEC-03, BEH-X-12, BEH-X-15 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ORG-06](../../tests/behavioral/organization-policy/scenarios.md), [SEC-03](../../tests/behavioral/security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-SEC-03, BEH-X-12, BEH-X-15).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Account-specific constraints remain UNKNOWN until independently authorized evidence.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-056

- Criterion: [AC-056](REQUIREMENTS.md#req-056). A mapping records each standard's verified edition/source, relevant Kiyo concepts and limits; inaccessible details remain gaps and concept alignment is not represented as compliance or certification.
- Implementing files: [src/kiyo/framework/engineering/standards-mapping.md:1](../../src/kiyo/framework/engineering/standards-mapping.md); [docs/research/standards-baseline.md:14](../../docs/research/standards-baseline.md); [docs/research/SOURCES.md:13](../../docs/research/SOURCES.md).
- Skills/shared procedures: requirement test architecture; linked files above define the shared steps.
- Actual inspection: Public official edition/status/source dates and concept-to-rule/evidence mappings exist with no clause copying.
- Test cases: TC-REQ-056 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; no P25 case directly assigned to this ID.
- Actual evidence: This dated manual file/contract inspection; no automated behavioral result.
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Catalogue review only; no licensed full-text/conformity assessment; release freshness recheck needed.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-08](#gap29-08).

### REQ-057

- Criterion: [AC-057](REQUIREMENTS.md#req-057). Mappings record verified editions/versions and sources for named frameworks, distinguish primary/supporting mappings and include a stated applicability decision for ISO 5338; no certification claim is made.
- Implementing files: [docs/research/standards-baseline.md:14](../../docs/research/standards-baseline.md); [src/kiyo/framework/engineering/standards-mapping.md:1](../../src/kiyo/framework/engineering/standards-mapping.md); [src/kiyo/agent-security/application-security.md:3](../../src/kiyo/agent-security/application-security.md); [src/kiyo/governance/ai-usage.md:3](../../src/kiyo/governance/ai-usage.md).
- Skills/shared procedures: security governance shared; linked files above define the shared steps.
- Actual inspection: Governance/security concepts, named editions/supporting references and conditional-only ISO 5338 are mapped.
- Test cases: TC-REQ-057 **PLANNED**; manual content review; no dedicated automated semantic acceptance assertion; BEH-SEC-01 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [SEC-01](../../tests/behavioral/security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-SEC-01).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Concept-level adaptation only; latest SAMM incremental status unknown; no standards certification.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-08](#gap29-08).

### REQ-058

- Criterion: [AC-058](REQUIREMENTS.md#req-058). Skill Audit checks origin, claimed authority and suspicious behavior, reports unknown provenance and explains that review cannot prove absence of malicious intent.
- Implementing files: [src/kiyo/agent-security/owasp-ast10.md:3](../../src/kiyo/agent-security/owasp-ast10.md); [src/kiyo/agent-security/trust-review.md:10](../../src/kiyo/agent-security/trust-review.md).
- Skills/shared procedures: security skills; linked files above define the shared steps.
- Actual inspection: AST01 reviews claimed origin/authority/effects with ownership, required evidence and inability to prove benign intent.
- Test cases: TC-REQ-058 **PLANNED**; G09 selected static checks; BEH-SEC-02 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [SEC-02](../../tests/behavioral/security/scenarios.md), [SEC-15](../../tests/behavioral/security/scenarios.md), [TC-AST-01A](../../tests/behavioral/agent-security/scenarios.md), [TC-AST-01B](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-SEC-02).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Unsigned is not malicious; host behavioral adoption cases unrun.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-08](#gap29-08).

### REQ-059

- Criterion: [AC-059](REQUIREMENTS.md#req-059). Release/audit guidance records available source-to-artifact provenance and dependency evidence, flags missing or inconsistent provenance and does not invent hashes, signatures or trusted publishers.
- Implementing files: [src/kiyo/agent-security/update-and-provenance.md:3](../../src/kiyo/agent-security/update-and-provenance.md); [src/kiyo/governance/dependency-governance.md:3](../../src/kiyo/governance/dependency-governance.md); [tools/release_candidate.py:1](../../tools/release_candidate.py).
- Skills/shared procedures: security release shared; linked files above define the shared steps.
- Actual inspection: AST02 binds source/artifact hashes and dependency evidence; no invented signatures or trusted publisher.
- Test cases: TC-REQ-059 **PLANNED**; G09, G12 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [TC-AST-02](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G12 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [developer release pipeline — PASS](../../dist/releases/p29-run-02/pipeline.json) (Actual six-stage exit 0; PKG-08 limitation separately retained, no host/model/publication).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Local hashes do not authenticate origin; owner publisher/signing policy unresolved.
- Owner decisions: DEC-001, DEC-002, DEC-003.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-03](#gap29-03).

### REQ-060

- Criterion: [AC-060](REQUIREMENTS.md#req-060). Skill review compares requested access with demonstrated task need and flags excess; remediation respects host permission controls and does not claim Kiyo can independently enforce them.
- Implementing files: [src/kiyo/governance/permissions.md:3](../../src/kiyo/governance/permissions.md); [src/kiyo/agent-security/control-ownership.md:13](../../src/kiyo/agent-security/control-ownership.md); [src/kiyo/agent-security/owasp-ast10.md:3](../../src/kiyo/agent-security/owasp-ast10.md).
- Skills/shared procedures: security skills; linked files above define the shared steps.
- Actual inspection: AST03 compares requested effects to need and identifies host/human responsibility.
- Test cases: TC-REQ-060 **PLANNED**; G09 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [TC-AST-03](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Native enforcement unavailable/unknown is a gap, not a Markdown safeguard.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-061

- Criterion: [AC-061](REQUIREMENTS.md#req-061). Manifests/frontmatter use verified native fields with truthful values; Kiyo advisory metadata is clearly separated from native-enforced fields and unsupported permission/security declarations are not invented.
- Implementing files: [platforms/claude/.claude-plugin/plugin.json:1](../../platforms/claude/.claude-plugin/plugin.json); [platforms/codex/plugin.json:1](../../platforms/codex/plugin.json); [platforms/copilot/plugin.json:1](../../platforms/copilot/plugin.json); [src/kiyo/agent-security/trust-review.md:10](../../src/kiyo/agent-security/trust-review.md).
- Skills/shared procedures: security skills; linked files above define the shared steps.
- Actual inspection: Documented development fields and canonical name/description exclude invented native permission fields.
- Test cases: TC-REQ-061 **PLANNED**; G05, G09 selected static checks; BEH-X-08 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [SEC-04](../../tests/behavioral/security/scenarios.md), [SEC-13](../../tests/behavioral/security/scenarios.md), [SEC-16](../../tests/behavioral/security/scenarios.md), [TC-AST-04](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G05 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-08); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **PARTIALLY_IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Strict Claude validation and Codex public ingestion retain failures for absent release metadata; owner-approved final manifests pending.
- Owner decisions: DEC-001, DEC-002, DEC-003.
- Next action / blocking scope: [GAP29-03](#gap29-03), [GAP29-05](#gap29-05), [GAP29-12](#gap29-12).

### REQ-062

- Criterion: [AC-062](REQUIREMENTS.md#req-062). Security procedures identify embedded commands in external content and memory as data, reject unauthorized policy/permission changes and surface relevant injection evidence without executing it.
- Implementing files: [src/kiyo/agent-security/prompt-injection.md:3](../../src/kiyo/agent-security/prompt-injection.md); [src/kiyo/framework/trust-and-authority.md:9](../../src/kiyo/framework/trust-and-authority.md); [src/kiyo/agent-security/owasp-ast10.md:3](../../src/kiyo/agent-security/owasp-ast10.md).
- Skills/shared procedures: security all; linked files above define the shared steps.
- Actual inspection: AST05 treats embedded external/Memory/copied approval instructions as untrusted data.
- Test cases: TC-REQ-062 **PLANNED**; G09 selected static checks; BEH-X-01, BEH-X-02, BEH-X-03 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [SEC-01](../../tests/behavioral/security/scenarios.md), [SEC-02](../../tests/behavioral/security/scenarios.md), [SEC-12](../../tests/behavioral/security/scenarios.md), [TC-AST-05A](../../tests/behavioral/agent-security/scenarios.md), [TC-AST-05B](../../tests/behavioral/agent-security/scenarios.md), [TC-AST-05C](../../tests/behavioral/agent-security/scenarios.md), [TC-AST-05D](../../tests/behavioral/agent-security/scenarios.md), [TC-AST-05E](../../tests/behavioral/agent-security/scenarios.md), [TC-AST-05F](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-X-01, BEH-X-02, BEH-X-03).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No claim to prevent every injection; target adversarial cases unexecuted.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-09](#gap29-09).

### REQ-063

- Criterion: [AC-063](REQUIREMENTS.md#req-063). Guidance records observed host isolation or UNKNOWN, names host responsibility and contains no Kiyo sandbox claim; unsupported isolation requirements become explicit compatibility gaps.
- Implementing files: [src/kiyo/agent-security/control-ownership.md:13](../../src/kiyo/agent-security/control-ownership.md); [src/kiyo/templates/reports/self-check-report.md:24](../../src/kiyo/templates/reports/self-check-report.md); [src/kiyo/agent-security/owasp-ast10.md:3](../../src/kiyo/agent-security/owasp-ast10.md).
- Skills/shared procedures: security self-check; linked files above define the shared steps.
- Actual inspection: AST06 assigns isolation to host, requires evidence or UNKNOWN and holds dependent use when required control absent.
- Test cases: TC-REQ-063 **PLANNED**; G09 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [SEC-05](../../tests/behavioral/security/scenarios.md), [SEC-07](../../tests/behavioral/security/scenarios.md), [SEC-14](../../tests/behavioral/security/scenarios.md), [TC-AST-06](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Cooperative packaging audit guard is not a host sandbox; native isolation unknown.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-064

- Criterion: [AC-064](REQUIREMENTS.md#req-064). Update guidance compares old/new content and requested permissions, records available provenance and requires applicable update approval; an update cannot silently expand approved scope or replace user policy.
- Implementing files: [src/kiyo/agent-security/update-and-provenance.md:3](../../src/kiyo/agent-security/update-and-provenance.md); [docs/release/security-lifecycle.md:9](../../docs/release/security-lifecycle.md); [src/kiyo/framework/init-activation.md:8](../../src/kiyo/framework/init-activation.md).
- Skills/shared procedures: security init; linked files above define the shared steps.
- Actual inspection: AST07 compares changes/provenance/access and approval; updates preserve project policy/Memory and human sections.
- Test cases: TC-REQ-064 **PLANNED**; G06, G09 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [TC-AST-07A](../../tests/behavioral/agent-security/scenarios.md), [TC-AST-07B](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G06 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded); [developer release pipeline — PASS](../../dist/releases/p29-run-02/pipeline.json) (Actual six-stage exit 0; PKG-08 limitation separately retained, no host/model/publication).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Version UNSET; native update/restart/managed-block preservation tests missing.
- Owner decisions: DEC-001, DEC-002, DEC-003.
- Next action / blocking scope: [GAP29-05](#gap29-05), [GAP29-03](#gap29-03).

### REQ-065

- Criterion: [AC-065](REQUIREMENTS.md#req-065). Audit guidance defines distinct static, behavioral and adversarial checks, records actual execution and blind spots and never treats clean scans as proof that a skill is safe.
- Implementing files: [src/kiyo/agent-security/trust-review.md:10](../../src/kiyo/agent-security/trust-review.md); [tests/behavioral/evaluation/protocol.md:9](../../tests/behavioral/evaluation/protocol.md); [docs/evidence/static/coverage-interpretation.md:8](../../docs/evidence/static/coverage-interpretation.md).
- Skills/shared procedures: security skills; linked files above define the shared steps.
- Actual inspection: AST08 separates static, behavioral and adversarial review and acknowledges blind spots.
- Test cases: TC-REQ-065 **PLANNED**; G09 selected static checks; BEH-SEC-02 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [SEC-02](../../tests/behavioral/security/scenarios.md), [SEC-07](../../tests/behavioral/security/scenarios.md), [SEC-09](../../tests/behavioral/security/scenarios.md), [SEC-10](../../tests/behavioral/security/scenarios.md), [TC-AST-08](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-SEC-02).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. 48 host observations NOT_RUN; no scanner/LLM proof of safety.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-066

- Criterion: [AC-066](REQUIREMENTS.md#req-066). Templates capture inventory identity, ownership, approval status/scope and revocation decisions without invented approvers; use requires no central service or live registry.
- Implementing files: [src/kiyo/templates/skill-governance/inventory.md:1](../../src/kiyo/templates/skill-governance/inventory.md); [src/kiyo/templates/skill-governance/approval.md:1](../../src/kiyo/templates/skill-governance/approval.md); [src/kiyo/templates/skill-governance/revocation.md:1](../../src/kiyo/templates/skill-governance/revocation.md); [src/kiyo/templates/skill-governance/incident.md:1](../../src/kiyo/templates/skill-governance/incident.md).
- Skills/shared procedures: security governance; linked files above define the shared steps.
- Actual inspection: AST09 optional neutral file records capture real identity/authority/revocation without central registry.
- Test cases: TC-REQ-066 **PLANNED**; G09, G11 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [TC-AST-09](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G11 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Organization adoption/revocation decisions require humans; templates convey no actual approval.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-067

- Criterion: [AC-067](REQUIREMENTS.md#req-067). A parity matrix maps each relevant control independently to the six targets, distinguishes Kiyo guidance from native enforcement and records unsupported/unverified behavior instead of assuming equivalence.
- Implementing files: [src/kiyo/agent-security/control-ownership.md:13](../../src/kiyo/agent-security/control-ownership.md); [tools/package_distributions.py:1](../../tools/package_distributions.py); [docs/compatibility/activation-matrix.md:13](../../docs/compatibility/activation-matrix.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: AST10 has per-control/Skill six-target parity records and separate host dependencies/gaps.
- Test cases: TC-REQ-067 **PLANNED**; G06, G09 selected static checks; BEH-SEC-04, BEH-X-08 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [SEC-04](../../tests/behavioral/security/scenarios.md), [SEC-13](../../tests/behavioral/security/scenarios.md), [SEC-14](../../tests/behavioral/security/scenarios.md), [SEC-16](../../tests/behavioral/security/scenarios.md), [TC-AST-10](../../tests/behavioral/agent-security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G06 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G09 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-SEC-04, BEH-X-08); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Codex IDE native plugins UNSUPPORTED. 456 content representations are not behavioral parity; Codex IDE unsupported.
- Owner decisions: DEC-004.
- Next action / blocking scope: [GAP29-05](#gap29-05), [GAP29-06](#gap29-06).

### REQ-068

- Criterion: [AC-068](REQUIREMENTS.md#req-068). Init inspects only permitted relevant material, creates/updates memory only with applicable authorization and evidence, leaves source untouched and reruns without duplicates or overwriting human edits.
- Implementing files: [src/kiyo/skills/init/SKILL.md:16](../../src/kiyo/skills/init/SKILL.md); [src/kiyo/workflows/init.md:3](../../src/kiyo/workflows/init.md); [src/kiyo/framework/init-discovery.md:6](../../src/kiyo/framework/init-discovery.md); [src/kiyo/framework/init-activation.md:8](../../src/kiyo/framework/init-activation.md).
- Skills/shared procedures: init; linked files above define the shared steps.
- Actual inspection: Full bounded onboarding/preview, evidence/unknowns and incremental authorized state/bootstrap contract exists.
- Test cases: TC-REQ-068 **PLANNED**; G03, G07 selected static checks; BEH-INIT-01, BEH-INIT-02, BEH-INIT-03, BEH-INIT-04 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [INIT-01](../../tests/behavioral/init/scenarios.md), [INIT-02](../../tests/behavioral/init/scenarios.md), [INIT-03](../../tests/behavioral/init/scenarios.md), [INIT-04](../../tests/behavioral/init/scenarios.md), [ORG-02](../../tests/behavioral/organization-policy/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-INIT-01, BEH-INIT-02, BEH-INIT-03, BEH-INIT-04); [historical bounded source-guided trial report — PASS](../../docs/evidence/init/forward-trials.md) (Only named trial assertions and retained snapshots in this report; not re-executed, not a native result, not full case coverage); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Source-guided trials limited; native Init, empty/dirty/legacy/monorepo/repeat matrix still unrun.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-069

- Criterion: [AC-069](REQUIREMENTS.md#req-069). Requirement outputs the required fields, labels proposals and unresolved decisions, assesses readiness and does not implement code or silently approve its own suggestions.
- Implementing files: [src/kiyo/skills/requirement/SKILL.md:16](../../src/kiyo/skills/requirement/SKILL.md); [src/kiyo/workflows/requirement.md:3](../../src/kiyo/workflows/requirement.md); [src/kiyo/templates/requirement.md:15](../../src/kiyo/templates/requirement.md); [src/kiyo/framework/requirement-readiness.md:9](../../src/kiyo/framework/requirement-readiness.md).
- Skills/shared procedures: requirement; linked files above define the shared steps.
- Actual inspection: Ready/draft/decision outcomes separated; no implicit implementation, Memory or default disk writes.
- Test cases: TC-REQ-069 **PLANNED**; G03, G07 selected static checks; BEH-REQ-01, BEH-REQ-02, BEH-REQ-03, BEH-REQ-04, BEH-X-02 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [RQM-01](../../tests/behavioral/requirement/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-REQ-01, BEH-REQ-02, BEH-REQ-03, BEH-REQ-04, BEH-X-02); [historical bounded source-guided trial report — PASS](../../docs/evidence/requirement/forward-trials.md) (Only named trial assertions and retained snapshots in this report; not re-executed, not a native result, not full case coverage).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Bounded forward trials not exhaustive fields/readiness or native invocation acceptance.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-070

- Criterion: [AC-070](REQUIREMENTS.md#req-070). Implement follows applicable approvals, impact plan, minimal-change practices and actual checks; repair loops stop at the declared bound and closure records memory impact and honest remaining gaps.
- Implementing files: [src/kiyo/skills/implement/SKILL.md:16](../../src/kiyo/skills/implement/SKILL.md); [src/kiyo/workflows/implement-flow.md:3](../../src/kiyo/workflows/implement-flow.md); [src/kiyo/templates/short-plan.md:18](../../src/kiyo/templates/short-plan.md); [src/kiyo/workflows/repair-and-handoff.md:3](../../src/kiyo/workflows/repair-and-handoff.md).
- Skills/shared procedures: implement; linked files above define the shared steps.
- Actual inspection: Sixteen daily steps cover authorized intent, minimal edits, side effects, actual checks, bounded repair and Memory Impact.
- Test cases: TC-REQ-070 **PLANNED**; G03, G07 selected static checks; BEH-IMPL-01, BEH-IMPL-02, BEH-IMPL-03, BEH-IMPL-04 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [IMP-01](../../tests/behavioral/implement/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-IMPL-01, BEH-IMPL-02, BEH-IMPL-03, BEH-IMPL-04); [historical bounded source-guided trial report — PASS](../../docs/evidence/implement/forward-trials.md) (Only named trial assertions and retained snapshots in this report; not re-executed, not a native result, not full case coverage); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No completed native feature/bug/refactor workflow acceptance.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-071

- Criterion: [AC-071](REQUIREMENTS.md#req-071). Review reports concrete evidence/location, severity and confidence per finding, explains inspected scope and makes no automatic source, memory or report-file edits in read-only mode.
- Implementing files: [src/kiyo/skills/review/SKILL.md:17](../../src/kiyo/skills/review/SKILL.md); [src/kiyo/workflows/review.md:3](../../src/kiyo/workflows/review.md); [src/kiyo/framework/review-severity-confidence.md:8](../../src/kiyo/framework/review-severity-confidence.md); [src/kiyo/templates/reports/review-finding.md:1](../../src/kiyo/templates/reports/review-finding.md).
- Skills/shared procedures: review; linked files above define the shared steps.
- Actual inspection: Actual workspace/range evidence, severity/confidence/location and limitations; bug discovery grants no writes.
- Test cases: TC-REQ-071 **PLANNED**; G03, G07 selected static checks; BEH-REV-01, BEH-REV-02, BEH-REV-03, BEH-REV-04, BEH-X-05 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [REV-01](../../tests/behavioral/review/scenarios.md), [REV-02](../../tests/behavioral/review/scenarios.md), [REV-03](../../tests/behavioral/review/scenarios.md), [REV-04](../../tests/behavioral/review/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-REV-01, BEH-REV-02, BEH-REV-03, BEH-REV-04, BEH-X-05); [historical bounded source-guided trial report — PASS](../../docs/evidence/review/forward-trials.md) (Only named trial assertions and retained snapshots in this report; not re-executed, not a native result, not full case coverage); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Review-only native zero-write/zero-execution behavior not verified.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-072

- Criterion: [AC-072](REQUIREMENTS.md#req-072). Assess plans checks without unintended execution/writes; run inspects scripts and reports actual outcomes; write creates tests only within authorized scope; existing test files never imply successful execution.
- Implementing files: [src/kiyo/skills/test/SKILL.md:17](../../src/kiyo/skills/test/SKILL.md); [src/kiyo/workflows/test.md:3](../../src/kiyo/workflows/test.md); [src/kiyo/framework/test-mode-safety.md:8](../../src/kiyo/framework/test-mode-safety.md); [src/kiyo/templates/reports/test-report.md:26](../../src/kiyo/templates/reports/test-report.md).
- Skills/shared procedures: test; linked files above define the shared steps.
- Actual inspection: Assess/run/write have distinct allowed effects and real command/results/counts; writing is not running.
- Test cases: TC-REQ-072 **PLANNED**; G03, G07 selected static checks; BEH-TEST-01, BEH-TEST-02, BEH-TEST-03, BEH-TEST-04, BEH-X-10 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [TST-01](../../tests/behavioral/test/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-TEST-01, BEH-TEST-02, BEH-TEST-03, BEH-TEST-04, BEH-X-10).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Mode-specific target execution and missing-environment handling remain untested.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-073

- Criterion: [AC-073](REQUIREMENTS.md#req-073). Security supports the four listed submodes under one public skill, defaults to read-only, reports evidence and limits and requires scoped authorization for any transition to writes or execution.
- Implementing files: [src/kiyo/skills/security/SKILL.md:18](../../src/kiyo/skills/security/SKILL.md); [src/kiyo/workflows/security.md:3](../../src/kiyo/workflows/security.md); [src/kiyo/agent-security/security-submodes.md:8](../../src/kiyo/agent-security/security-submodes.md); [src/kiyo/templates/reports/self-check-report.md:24](../../src/kiyo/templates/reports/self-check-report.md).
- Skills/shared procedures: security; linked files above define the shared steps.
- Actual inspection: Four logical submodes share bounded read-only access and evidence/owner/limitations with no auto-fix or global scan.
- Test cases: TC-REQ-073 **PLANNED**; G03, G07 selected static checks; BEH-SEC-01, BEH-SEC-02, BEH-SEC-03, BEH-SEC-04 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ORG-03](../../tests/behavioral/organization-policy/scenarios.md), [SEC-01](../../tests/behavioral/security/scenarios.md), [SEC-02](../../tests/behavioral/security/scenarios.md), [SEC-03](../../tests/behavioral/security/scenarios.md), [SEC-04](../../tests/behavioral/security/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-SEC-01, BEH-SEC-02, BEH-SEC-03, BEH-SEC-04); [historical bounded source-guided trial report — PASS](../../docs/evidence/security/forward-trials.md) (Only named trial assertions and retained snapshots in this report; not re-executed, not a native result, not full case coverage); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Source trials and static clauses cannot prove isolation, integrity or complete inventory.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-074

- Criterion: [AC-074](REQUIREMENTS.md#req-074). Architecture distinguishes current observed code from approved intent, reports evidence-backed drift within inspection scope and does not rewrite decisions merely to match implementation.
- Implementing files: [src/kiyo/skills/architecture/SKILL.md:17](../../src/kiyo/skills/architecture/SKILL.md); [src/kiyo/workflows/architecture.md:3](../../src/kiyo/workflows/architecture.md); [src/kiyo/templates/reports/architecture-observation.md:17](../../src/kiyo/templates/reports/architecture-observation.md); [src/kiyo/templates/reports/architecture-impact-report.md:1](../../src/kiyo/templates/reports/architecture-impact-report.md).
- Skills/shared procedures: architecture; linked files above define the shared steps.
- Actual inspection: Observed/approved/proposed/unknown structures and Match/Deviation/Insufficient evidence prevent automatic redesign.
- Test cases: TC-REQ-074 **PLANNED**; G03, G07 selected static checks; BEH-ARCH-01, BEH-ARCH-02, BEH-ARCH-03, BEH-ARCH-04 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [ARC-01](../../tests/behavioral/architecture/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-ARCH-01, BEH-ARCH-02, BEH-ARCH-03, BEH-ARCH-04); [historical bounded source-guided trial report — PASS](../../docs/evidence/architecture/forward-trials.md) (Only named trial assertions and retained snapshots in this report; not re-executed, not a native result, not full case coverage).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Bounded source-guided results only; no production topology or native complete assessment.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-075

- Criterion: [AC-075](REQUIREMENTS.md#req-075). Show/check remain read-only; sync/repair use authorized scoped writes, preserve approved decisions and human edits, handle stale/concurrent inputs and perform no writes for a no-change result.
- Implementing files: [src/kiyo/skills/memory/SKILL.md:17](../../src/kiyo/skills/memory/SKILL.md); [src/kiyo/framework/memory-modes.md:3](../../src/kiyo/framework/memory-modes.md); [src/kiyo/workflows/memory-lifecycle.md:8](../../src/kiyo/workflows/memory-lifecycle.md); [src/kiyo/templates/reports/memory-sync-report.md:1](../../src/kiyo/templates/reports/memory-sync-report.md).
- Skills/shared procedures: memory; linked files above define the shared steps.
- Actual inspection: Show/check zero-write and sync/repair latest reread, delta/no-op, provenance and history preservation are concrete.
- Test cases: TC-REQ-075 **PLANNED**; G03, G07, G10 selected static checks; BEH-MEM-01, BEH-MEM-02, BEH-MEM-03, BEH-MEM-04, BEH-X-09 **NOT_RUN**.
- Additional authored specifications (NOT_RUN): [MSK-01](../../tests/behavioral/memory/skill-scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G03 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G07 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G10 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [source-guided host suite — NOT_RUN](../../docs/evidence/behavioral/observations.json) (BEH-MEM-01, BEH-MEM-02, BEH-MEM-03, BEH-MEM-04, BEH-X-09); [historical bounded source-guided trial report — PASS](../../docs/evidence/memory/forward-trials.md) (Only named trial assertions and retained snapshots in this report; not re-executed, not a native result, not full case coverage).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. One no-op/concurrent independent edit trial does not cover all races, modes or hosts.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04).

### REQ-076

- Criterion: [AC-076](REQUIREMENTS.md#req-076). Maintenance instructions use native host mechanisms without hardcoded cache paths; update/uninstall scenarios retain user policies and canonical memory, and version claims reflect actual artifacts.
- Implementing files: [src/kiyo/framework/init-activation.md:8](../../src/kiyo/framework/init-activation.md); [docs/compatibility/codex-package.md:13](../../docs/compatibility/codex-package.md); [docs/compatibility/copilot-installation.md:8](../../docs/compatibility/copilot-installation.md); [docs/compatibility/claude-installation-test-protocol.md:9](../../docs/compatibility/claude-installation-test-protocol.md).
- Skills/shared procedures: init memory; linked files above define the shared steps.
- Actual inspection: Managed project locator/update/uninstall guidance preserves user data; Codex disposable uninstall preserved three synthetic files.
- Test cases: TC-REQ-076 **PLANNED**; G04 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G04 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Installed update/version transition and managed block removal remain untested; no universal cache locator or release version.
- Owner decisions: DEC-001, DEC-002, DEC-003.
- Next action / blocking scope: [GAP29-05](#gap29-05), [GAP29-03](#gap29-03).

### REQ-077

- Criterion: [AC-077](REQUIREMENTS.md#req-077). Reports and test organization identify the three layers separately; static PASS cannot mark behavior or live targets passed, and each of six live targets retains its own results and missing prerequisites.
- Implementing files: [tests/static/README.md:27](../../tests/static/README.md); [tests/behavioral/evaluation/protocol.md:9](../../tests/behavioral/evaluation/protocol.md); [docs/compatibility/live-test-matrix.md:24](../../docs/compatibility/live-test-matrix.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Independent static, source-guided behavioral and six-target native records preserve unrun and unsupported cases.
- Test cases: TC-REQ-077 **PLANNED**; G16 selected static checks; no P25 case directly assigned to this ID.
- Additional authored specifications (NOT_RUN): [EVID-01](../../tests/behavioral/verification/scenarios.md), [EVID-12](../../tests/behavioral/verification/scenarios.md), [EVID-17](../../tests/behavioral/verification/scenarios.md), [REV-01](../../tests/behavioral/review/scenarios.md), [REV-10](../../tests/behavioral/review/scenarios.md), [TST-01](../../tests/behavioral/test/scenarios.md), [TST-03](../../tests/behavioral/test/scenarios.md), [TST-06](../../tests/behavioral/test/scenarios.md), [TST-09](../../tests/behavioral/test/scenarios.md). Selected named cases, not exhaustive clause coverage.
- Actual evidence: [G16 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. No missing layer is replaced by another layer's PASS; no complete host acceptance.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-04](#gap29-04), [GAP29-05](#gap29-05).

### REQ-078

- Criterion: [AC-078](REQUIREMENTS.md#req-078). User/developer guides cover all listed stages, clearly separate developer-only tooling from end-user use and link host-specific invocation to verified support or an explicit unverified gap.
- Implementing files: [README.md:20](../../README.md); [docs/user/README.md:10](../../docs/user/README.md); [docs/user/skills.md:23](../../docs/user/skills.md); [docs/developer/maintainer-guide.md:7](../../docs/developer/maintainer-guide.md); [docs/user/walkthroughs.md:15](../../docs/user/walkthroughs.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: First-use/daily/maintenance guides link shipped Skills and documented or explicitly unverified native selectors.
- Test cases: TC-REQ-078 **PLANNED**; G04 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G04 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Nine illustrative walkthroughs NOT_RUN; user journey and target selector behavior unverified.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-05](#gap29-05), [GAP29-02](#gap29-02).

### REQ-079

- Criterion: [AC-079](REQUIREMENTS.md#req-079). Repeated packaging of identical inputs yields identical artifact digests under a documented environment; release checks exclude developer scripts from payloads, record actual signatures or their absence and require owner approval before publishing.
- Implementing files: [tools/release_candidate.py:1](../../tools/release_candidate.py); [tools/package_distributions.py:1](../../tools/package_distributions.py); [docs/release/runbook.md:9](../../docs/release/runbook.md); [docs/release/submission-checklists.md:8](../../docs/release/submission-checklists.md).
- Skills/shared procedures: release shared; linked files above define the shared steps.
- Actual inspection: Actual duplicate builds, closed inventories/checksums and unsigned/not-attested gates; corrected stage completeness guard.
- Test cases: TC-REQ-079 **PLANNED**; G05, G06, G12 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G05 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G06 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [G12 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations); [native observations — NOT_RUN](../../docs/compatibility/live-test-matrix.md) (Complete required target acceptance remains unrun; partial Claude discovery and Codex lifecycle VERIFIED as individually recorded); [developer release pipeline — PASS](../../dist/releases/p29-run-02/pipeline.json) (Actual six-stage exit 0; PKG-08 limitation separately retained, no host/model/publication).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Publication owner decisions, host evidence and filesystem symlink probe remain blockers/limits; no publish authority.
- Owner decisions: DEC-001, DEC-002, DEC-003.
- Next action / blocking scope: [GAP29-13](#gap29-13), [GAP29-03](#gap29-03), [GAP29-05](#gap29-05), [GAP29-07](#gap29-07), [GAP29-01](#gap29-01).

### REQ-080

- Criterion: [AC-080](REQUIREMENTS.md#req-080). Prompt 01 records all 80 unique IDs with six expansion fields and a trace row each; every step updates progress/traceability/issues/handoff; a fresh session can identify completed work and next action; Prompt 29 audits final gaps and placeholders never count as features.
- Implementing files: [docs/build/BUILD-CONTRACT.md:3](../../docs/build/BUILD-CONTRACT.md); [docs/build/REQUIREMENTS.md:16](../../docs/build/REQUIREMENTS.md); [docs/build/TRACEABILITY.md:1](../../docs/build/TRACEABILITY.md); [docs/build/FINAL-GAP-AUDIT.md:1](../../docs/build/FINAL-GAP-AUDIT.md); [docs/build/HANDOFF.md:3](../../docs/build/HANDOFF.md).
- Skills/shared procedures: all; linked files above define the shared steps.
- Actual inspection: Eighty stable IDs and resumable build records reconciled by this file-based audit, not previous DONE labels.
- Test cases: TC-REQ-080 **PLANNED**; G16 selected static checks; no P25 case directly assigned to this ID.
- Actual evidence: [G16 — PASS](../../dist/releases/p29-run-02/evidence/static.json) (Selected property only; see check observed/limitations).
- Implementation: **IMPLEMENTED**. Full verification: **NOT_RUN** — Full registered acceptance method has not been completed; authored content review and scoped executions are separate evidence below.
- Unsupported limits / remaining gap: Kiyo guidance is advisory; no native enforcement inferred. Prompt 30 final acceptance not performed; full product acceptance and external gaps remain explicit.
- Owner decisions: No new per-requirement owner decision; applicable authority and common release gates still apply.
- Next action / blocking scope: [GAP29-10](#gap29-10), [GAP29-09](#gap29-09), [GAP29-11](#gap29-11).

## Closure

Memory Impact: **NONE** for this developer task. No project .kiyo store existed
at baseline; this audit changes build/evidence records, not consumer Memory or
policy. Product inputs and LICENSE are preserved; user edits are not reset,
stashed or reverted. No consumer runtime, new public Skill or forced dependency
was introduced.

See [fix changelog](../evidence/gap-audit/fix-changelog.md) and
[regression evidence](../evidence/gap-audit/validation-report.md).
Safe to continue: **YES for user-requested Prompt 30**, preserving every open
release gate. Stop after Prompt 29; final acceptance and any live execution need
their own actual scope and authority.

