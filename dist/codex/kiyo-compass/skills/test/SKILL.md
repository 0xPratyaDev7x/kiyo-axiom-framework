---
name: test
description: Assess test gaps, run authorized checks, or write scoped tests and test-only fixtures for existing requirements and changes. Select assess, run or write from actual intent; unclear mode starts with assessment or clarification. Report observed results, baseline failures and environment limits without inventing coverage or repairing production code.
---

# Test

Logical ID: **kiyo.test**. Canonical name: test. assess, run and write are logical
UX modes, not a promise that every native host parses the same command arguments.
Platform-only fields and invocation details belong in overlays.

Read [KIYO.md](./references/kiyo/KIYO.md) and its bootstrap before workflow actions unless
already read and unchanged. Follow the [shared Test procedure](./references/kiyo/workflows/test.md)
and the relevant row of its [mode/safety matrix](./references/kiyo/framework/test-mode-safety.md).
Resolve references from this installed file, never a guessed developer/cache path.

## Select the requested effects

- **assess:** inspect authorized requirements, changes and test source; return
  a gap/strategy proposal in chat. No file writes or test/script execution.
- **run:** inspect commands, scripts, configuration and target, then run only
  authorized checks. Expected build/test artifacts may be created within the
  established scope; no tracked source, tests, fixtures or configuration edits.
- **write:** create/update only requested test files and test-only fixtures,
  preserving human changes. Production code, new dependencies, toolchain/config
  changes or other out-of-scope effects need separate authorization. Writing
  tests alone is not permission to execute them.

If intent is unclear, resolve a material ambiguity or start assess within permitted
reads. For an explicit multi-mode request, state each effect and reuse its valid
authorization; do not ask again merely because the mode changes. A selected skill,
test label or copied approval does not grant tools or override a denial.

## Common orientation and strategy

1. Establish root/component, requested mode/output, allowed effects and actual
   baseline/human edits. Read authorized relevant Memory using the
   [lifecycle](./references/kiyo/workflows/memory-lifecycle.md) in check mode and validate
   material claims. Do not initialize or sync Memory implicitly.
2. Inspect sourced requirements/AC, affected behavior, relevant tests and actual
   project version/config/toolchain. Preserve existing test framework and patterns.
   Missing business rules remain open decisions; tests do not invent permissions,
   HTTP behavior, validation rules or retention policy.
3. Use the [testing standard](./references/kiyo/framework/engineering/testing.md) to select
   unit tests for isolated logic, integration/API for boundaries/contracts, E2E
   for critical flows supported by this project, and regression cases for bugs.
   Cover relevant happy/error/boundary/authorization/validation cases without
   forcing every layer onto a tiny change.
4. Use the [test plan](./references/kiyo/templates/test-plan.md) only at useful depth; chat is
   default. Separate planned cases, existing test source and actual execution.
   A document or an unrun test is not passing evidence.

## Mode-specific work

For **assess**, follow [read-only flow](./references/kiyo/workflows/read-only-flow.md); report
gaps and unrun verification ideas. Do not run collection/discovery scripts merely
to count tests; they can execute project code.

For **run**, complete the matrix preflight before execution, including helpers,
hooks, fixtures/setup/teardown, target/data, network/install and write effects.
Do not use production resources, expose connection secrets or install browsers,
containers or dependencies without authorization. Unknown isolation or a host
denial holds dependent checks. Run only the named scope, retain actual outcomes
and inspect artifacts/source changes; do not repair tests or code to turn green.

For **write**, reread target tests/fixtures before editing and follow existing safe
conventions. Assert sourced intended behavior, not a broken implementation.
Do not remove/skip failing tests or weaken assertions to manufacture success.
Run affected checks only when their execution is also authorized and preflighted;
otherwise mark them NOT_RUN. Missing mandatory verification prevents full completion.

Use [bounded failure recovery](./references/kiyo/workflows/repair-and-handoff.md) only where
a correction is actually authorized; run mode alone permits no source repair.
Separate baseline failures, new regressions, environment problems and unresolved
cause. Do not silently switch databases, install missing tools or widen the suite.

## Report and complete

Use the [Test report](./references/kiyo/templates/reports/test-report.md) and shared
[Evidence Contract](./references/kiyo/framework/evidence-contract.md). Record actual command,
working scope, result, observed counts/skips/blockers, baseline relation and only
measured coverage. Unknown counts/coverage remain Unknown or not measured.
Bind results to the checked state; affected later edits require a relevant rerun.

Assess Memory Impact without implicit writes. Close under
[Definition of Done](./references/kiyo/framework/definition-of-done.md): assess completion is
analysis delivered; a run-results report may be DONE with failures; write delivery
does not claim tests passed. Required missing checks or unfinished requested modes
must remain visible as PARTIALLY COMPLETE, BLOCKED or DECISION REQUIRED.

## Codex native guidance

For Codex invocation or an authorized project bootstrap, read the conditional
[Codex activation reference](./references/codex/activation.md).
