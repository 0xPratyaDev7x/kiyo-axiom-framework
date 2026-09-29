# Prompt 24 — Static validation report

Checked: 2026-09-29. Status: **DONE for the requested static/contract-test scope**.
Runtime Verification: **Verified — developer tests only**.

**37 tests PASS: 16 positive groups and 21 negative rejection cases.**
Three actual ZIPs were extracted to fresh directories with spaces and inspected
by a copied standalone checker that denied original source access. No product
contract, package, overlay or original builder required modification.

## Actual execution history

All commands below ran from the repository root with Python 3.11.9 on
Windows-10-10.0.26200-SP0. Reports retain actual UTC times, command arrays,
exit codes, full test output, per-case results, source/tool/fixture hashes and
subprocess stdout/stderr. No result is inferred from merely writing a test.

| Command | Exit code | Observed result | Evidence |
| --- | --- | --- | --- |
| python -B tests/static/test_contracts.py --report docs/evidence/static/test-results-01.json | 1 | 36 tests, 5 errors; 31 succeeded | [First execution](test-results-01.json) |
| python -B tests/static/test_contracts.py --report docs/evidence/static/test-results-02.json | 0 | 37 tests; zero errors/failures/skips | [Corrected execution](test-results-02.json) |
| python -B tests/static/test_contracts.py --report docs/evidence/static/test-results-final.json | 0 | 37 tests; zero errors/failures/skips | [Final execution](test-results-final.json) |

Final execution: 2026-09-29T12:06:37.381970+00:00 through 2026-09-29T12:06:56.236336+00:00.
Base Git HEAD: `434f1df4729130d195650fcc40f007572e4e6759`, main.
Worktree hashes identify tested bytes; the base is not production evidence.
The final run follows the traceability update and final assertion/record changes;
the earlier passing run does not certify those later changes.

## Failures and fixes retained

The initial five errors belonged to newly authored test code/fixture wiring,
not observed failures of the canonical product:

1. G11 treated ordinary `behavior/users/data` prose as an absolute user-home
   path. Anchor the Unix path pattern to a path boundary; preserve credential/
   path checks and add an absolute-developer-path synthetic regression.
2. G13 passed `--target` to the existing standalone checker, whose target is a
   positional argument. Use its actual reviewed CLI. The failed subprocess
   output is retained in the first report.
3. duplicate-skill wired copy source/destination backward. Honor the fixture's
   source path and fresh destination; retain DUPLICATE_SKILL as required reason.
4. invalid-frontmatter matched both the header name and the canonical name in
   prose. Anchor the single mutation to the opening frontmatter delimiter.
5. private-package-file confused target name with destination path. Correct
   fixture wiring; retain PAYLOAD_ALLOWLIST and the private-path diagnostic.

No invariant, mandatory case or product rule was deleted. The final version
also checks all AST owner categories, pins the six mandatory fixture IDs and
records per-check applicability/method/scope/limitations/baseline relations.
The final report's hashes bind those changes to actual execution.

## Observed coverage

- Eight canonical entries and eight per package; 37 mandatory shared resources
  reachable from the eight selected-skill routes.
- 105 product Markdown files, 68 controls, 34 templates.
- 695 canonical local links; 4,956 Claude / 4,956 Codex / 4,964 Copilot
  payload links, exact-case/anchor/containment checked.
- 2,328 shared byte-identical copies and 24 allowed entry transformations.
- 112 allowlisted inputs; existing artifacts contain 794 / 795 / 794 files.
  All source/tool/archive/output hashes agree with the P23 inventory.
- All three extracted payloads report eight Skills, 97 shared resources per
  Skill and outside_read_probe DENIED. Exact commands/results are in the final
  report's subcommands; the checker is developer-only.
- Core 81 lines / 579 words against Kiyo's 120-line / 600-word budget;
  source and packaged entries satisfy their 250-line / 1,200-word budgets.
- All REQ-001–080 and their trace rows are present once. Forty trace rows add
  partial static coverage. All full requirement verifications remain NOT_RUN.

See the [group/property matrix](../../../tests/static/README.md) and
[21 fixture expectations](../../../tests/static/fixtures/README.md).
Every negative passes only after the owning validator raises the expected
specific code and includes the expected reason. Fixture precondition errors,
unexpected exceptions and no rejection are test failures.

## Check-record interpretation

Each final JSON check has ID/name, applicability, command reference/method,
inspected scope, status, observed result or exact rejection, evidence location,
limitations and baseline relation. The top-level command and full output bind
all records to one execution. Three relocation subprocesses retain their own
commands/exit/stdout/stderr. No tests were skipped or downgraded to optional.
The first failed execution remains available; it is not described as a clean
baseline or removed to claim that every historical test passed.

Scope and preservation/build continuity checks are recorded in
[BASELINE P24](../../build/BASELINE.md#prompt-24-checks).
No source, Memory, permission or global configuration change is implied by
test execution. Reports/fixtures/tooling live outside product payloads.

## Limits and continuation

**Static PASS does not prove an agent follows Markdown.** These are selected
properties, **not FULL SCHEMA VALIDATION**; detailed checked schema fields and
limitations are in [coverage interpretation](coverage-interpretation.md).
Template scanning is bounded, not comprehensive DLP. No certification, runtime
signature checking or sandbox/network enforcement is claimed.

Behavioral/live-host work not run here remains **NOT_TESTED**; expected scenario
execution remains NOT_RUN. Prior source-guided trials are separate. Native
targets remain independently NOT_TESTED; Codex IDE native plugins UNSUPPORTED,
historical Codex ingestion FAIL and P23 filesystem-symlink probe BLOCKED remain
visible. The static runner does not turn those results into success.

DEC-001–004 remain open. Memory Impact: NONE; no actual project memory store.
Safe to continue: **YES for user-requested Prompt 25 Behavioral Tests**,
with owner/native gaps retained. Stop after Prompt 24; no later task, install,
submission or publication is authorized by this report.

