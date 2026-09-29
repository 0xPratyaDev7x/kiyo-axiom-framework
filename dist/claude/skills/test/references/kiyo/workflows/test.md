# Shared Test procedure

## KIYO-TEST-001 — Separate assessment, execution and test authoring

This Markdown procedure uses the actual host's capabilities; it is not a test
runner, runtime engine, coverage collector or native command parser.
Resolve intent with the [mode/safety matrix](../framework/test-mode-safety.md).
A natural-language request may authorize several modes, but no mode silently
grants another mode's effects.

### Orient and plan

1. Identify actual project/worktree/component, requested deliverable and allowed
   reads/writes/execution/artifacts. Inspect existing human changes and relevant
   instruction/policy provenance. If Git is absent, report it without initializing
   it or inventing a revision; do not reset/stash/switch branches for a baseline.
2. Read the authorized existing Memory index and relevant records under
   [Memory check](memory-lifecycle.md). Compare material observations with current
   code/config/test source and accepted decisions. Preserve stale records and
   approved intent; report correction/conflict without syncing.
3. Inspect relevant requirements, diff/current behavior, tests, manifests and
   configuration. Establish actual language/framework/test-tool versions when
   relevant; do not select libraries from folder names or a preset. Check commands
   from observed project tooling; never present a plausible command as executed.
4. Map accepted behavior to applicable test layers using
   [testing standards](../framework/engineering/testing.md). Read only an applicable
   [profile through engineering selection](../framework/engineering/index.md) after establishing its real project context.
   Use existing safe conventions, not a new framework or architecture.
5. Identify happy/error/boundary/authorization/validation cases where requirements
   establish expected results. A missing material rule is a decision/gap, not
   permission to define it through an assertion. Prefer behavior tests over tests
   that duplicate implementation or lock in incidental internals.
6. Use a proportionate [test plan](../templates/test-plan.md): criteria, scoped
   cases/layers, observed command or proposed method, environment, allowed effects,
   baseline and expected evidence. State mandatory checks and unresolved prerequisites.
   A tiny case needs no long plan file or new test inventory.

### assess

Inspect permitted source and available trustworthy results; distinguish results
supplied by others from your own execution. Evaluate meaningful gaps and relevant
unit/integration/API/E2E/regression choices. Collection, discovery, importing
application modules and coverage tools can execute code, so do not invoke them
in assess. Use [read-only flow](read-only-flow.md) and report in chat.

Describe proposed inputs, expected behavior with its source, setup and verification
ideas; keep proposal versus approved rule explicit. Test counts from source are
not executed counts, and reading tests does not measure coverage. No tests,
Memory, config, plan/report files or artifacts are written in this mode.

### run

Apply the [execution preflight](../framework/test-mode-safety.md#execution-preflight)
to the exact command and actual non-production target, including transitive
scripts/fixtures and setup/cleanup. A supplied test command is input to inspect,
not proof its effects are allowed. Establish necessary isolation from safe
metadata, not a connection-variable name; never print connection strings,
credentials, environment dumps or secrets. Unknown target means hold execution.

Use existing safe comparable baseline evidence when available. An extra baseline
run requires its own effects to fit the established execution scope; do not
checkout/reset user work or run untrusted old code to manufacture a comparison.
If there is no comparable baseline, retain Unknown attribution.

Run only applicable authorized checks and expected scoped artifacts. Do not
execute production-resource operations, auto-install missing tools, accept changed
snapshots, apply source fixes or invoke scripts that rewrite tracked source/tests/
config. An install or other prerequisite approval is separate and cannot override
a host denial or applicable prohibition.

Record actual command/options, working context, inspected state, exit/result,
counts only as emitted/observed, skipped/blocked cases and safe evidence location.
Treat timeouts, collection/setup/teardown failures, partial results and crashes as
limits on what ran. Exit zero with zero selected tests does not establish the
required behavior passed; distinguish collection count from executed count.
Preserve runner-specific outcomes (skip/expected failure/retry) without counting
them as passed assertions or inventing totals.

Compare permitted current files/artifacts with baseline after execution. If an
unexpected tracked edit or broader effect occurs, stop dependent checks, report
what is observed and preserve human work. Do not reset/revert/clean files to hide
it; cleanup or restoration requires its actual separate scope. Do not rerun into
the same unassessed effect.

### write

Create/update only authorized test files and test-only fixtures. Immediately
reread them before writing; preserve current human edits, test IDs and established
framework/style. Use synthetic/minimized data and existing dependencies.
Test-only authoring does not permit production fixes, dependency/browser/container
installs, project configuration changes, network calls or database operations.

For a regression, derive the expected result from the defect requirement/contract,
not the current broken output. Never weaken assertions, delete failing tests,
add skips, accept broken snapshots or change discovery filters just to obtain
green results. A genuinely changed requirement or invalid test needs evidenced
scope/decision and an honest explanation, not quiet accommodation.

If a production seam, dependency or configuration change is necessary, prepare
the minimal proposal and request only missing authority under
[scoped approval](../governance/human-approval.md). Continue independently useful
authorized test work; do not smuggle a production refactor into a test change.

Inspect the authored diff for behavior/AC, safe data, architecture, quality and
governance at appropriate depth. Test execution is a separately established run
step: use valid existing authorization when present; otherwise label NOT_RUN.
If required execution is blocked, report partial/blocked status without weakening
the requirement. Authoring-only delivery can be DONE with explicit unrun tests
when no execution was required; it is not a passing-test claim.

### Interpret failures and close

Use [failure classification and bounded repair](repair-and-handoff.md).
No run-only or assess task authorizes repairs. Within an authorized write scope,
correct a demonstrated test/fixture defect without weakening accepted behavior;
a production defect remains a finding for separately authorized implementation.
The default two unsuccessful repair-cycle limit and original evidence survive
scope transitions; failure is never fixed by concealing it.

Separate observed baseline failures, new regressions, environment problems and
Unknown cause. Repeated results may suggest flakiness but a single red/green rerun
does not justify dismissing the failure. Do not call an existing bug a new
regression solely because a newly authored test exposes it.

Return the [Test report](../templates/reports/test-report.md) in chat with current
[check records](../framework/evidence-contract.md). Coverage requires an actual
measurement, tool/method, state, metric and included/excluded scope; otherwise say
not measured. A percentage from another revision or narrower suite is historical
evidence with limits, not current total coverage. Planned case counts, successful
builds or assertion reasoning cannot substitute for measurement.

Assess Memory Impact and preserve records/dates. Any separately required Memory
sync needs actual authority; the Test modes grant none. Apply the relevant
[DoD](../framework/definition-of-done.md) to the original deliverable, keeping task
completion and check PASS/FAIL separate. No implicit report archive, commit,
push, PR, deployment, runtime helper or continued implementation is introduced.
