# Prompt 29 — targeted fix changelog

Checked 2026-09-29; baseline main f5cb303b1713ce6f103760c0cad05fcd7e086fcf.
This is author self-review, not an independent audit. No product bytes, Skill
scope, manifest, license, dependency, user Memory or native setting changed.

## GAP29-01 — incomplete pipeline could validate

- Before: package_status accepted any nonempty list whose statuses were PASS,
  including one unnamed stage, missing mandatory stages or reordered/duplicates.
  Existing real P28 runs did complete all stages; this is a guard defect, not
  evidence that those runs skipped work.
- Fix: require exactly Validate → Package → Inspect payload → Run tests →
  Artifact inventory → Release-readiness report, all PASS. The allowed additional
  PKG-08 limitation remains visible as PACKAGE_VALIDATED_WITH_LIMITATIONS.
- Files: [release coordinator](../../../tools/release_candidate.py),
  [release regression source](../../../tests/release/test_release.py).
- Evidence: [before](release-before.json), exit 1, nine test methods and ten
  failing subtests; [after](release-after.json), exit 0, nine methods PASS.
  Existing failed/blocked/empty tests remain; test_05 now also rejects every
  non-PASS status in each mandatory stage, using a complete positive fixture.
  No negative or requirement was weakened.

## GAP29-13 — readiness I/O failure left a successful record

- Before: pipeline.json with exit_code 0 was written before readiness.md;
  a readiness output exception could leave contradictory success evidence.
- Fix: emit the required readiness file before persisting the success record;
  a write failure returns exit 1, PACKAGE_NOT_VALIDATED and a FAIL report stage.
  Final timestamps include report I/O. Multi-file output is still not atomic
  or tamper-proof; no integrity guarantee is added.
- Same two code files above. The regression stubs prior stages only to isolate
  report I/O in a disposable unit fixture. Those stubs are not actual package,
  host or behavioral results.
- Evidence: [before](report-write-before.json), exit 1, ten methods/one error;
  [after](report-write-after.json), exit 0, ten methods PASS. The
  [final real six-stage run](../../../dist/releases/p29-run-02/pipeline.json)
  independently exercises the normal pipeline without those stubs.

## GAP29-02 — obsolete worked paths / stale native summary

- [Packaging contract](../../architecture/packaging-contract.md) now uses the
  real evidence-contract.md, templates/reports/review-report.md and actual
  Claude versus Codex/Copilot roots. Literal draft paths were not Markdown links,
  so the old link validator did not flag them. They did not break shipped payloads.
- [Invocation map](../../compatibility/native-invocation-map.md) now points to
  bounded P26 native results while preserving dated research sections. Explicit
  Skill invocation and automatic Core remain untested.
- Current-path checks and repository reference checks are in the closure record.
  No new native syntax/schema or support claim was introduced.

## GAP29-11 — stale implementation labels

- The old trace still called REQ-001 NOT_IMPLEMENTED and every other row partial,
  with descriptions of public Skills that were already authored.
- Replaced current rows with actual implementing files and per-ID evidence/gaps:
  78 authored IMPLEMENTED, REQ-010/061 PARTIALLY_IMPLEMENTED. All full acceptance
  verifications remain NOT_RUN; this bookkeeping correction is not a host pass.
- [Ledger regressions](ledger-tests-final.json) validate all 80 unchanged criteria,
  real locators/cases, explicit gap ownership/actions and retained release gates.
  The prior trace is available in Git at the baseline revision. No historical
  execution record was overwritten or converted from failure/unrun into success.

The [audit](../../build/FINAL-GAP-AUDIT.md) lists every remaining gap, its next
action and blocking scope. Owner decisions and unavailable native tests are not
defects this patch can invent away.
