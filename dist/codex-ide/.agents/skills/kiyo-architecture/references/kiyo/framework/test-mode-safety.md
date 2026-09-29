# Test mode and safety matrix

Use with the [Test procedure](../workflows/test.md) (KIYO-TEST-001).
Modes describe the requested effects; they are not native permissions, governance
levels or universal command arguments. Kiyo provides guidance, not a sandbox,
network block or guarantee that a test has no hidden effects.

## Mode boundaries

| Mode | Required intent / permitted effects | Not granted by this mode | Completion evidence |
| --- | --- | --- | --- |
| assess | Analyze authorized requirements, changes, relevant Memory and test source; return gaps/strategy in chat. Unclear intent may begin here. | File/report/Memory writes, test execution, discovery/collection scripts, module imports, package installs. | Inspected scope, behavior-to-case gaps/proposals, constraints and NOT_RUN execution; no invented coverage. |
| run | Actual request permits named checks, known non-production target/data and expected artifact writes within scope. | Tracked source/test/fixture/config repair, snapshot acceptance, production resources, tool/dependency installation or Memory sync. | Preflight, actual command/result, counts/skips/blockers, baseline relation and artifact/source delta; no green-by-editing. |
| write | Actual request permits creating/updating specified tests and test-only fixtures. | Production source, unrelated tests, new dependencies, config/toolchain changes, Memory sync or execution unless separately covered. | Minimal preserved-human-edit diff, sourced assertions, test review and real run results or explicit NOT_RUN/BLOCKED. |

“Write and run these tests” can authorize both phases. Record the boundary and
preflight effects without demanding repeated approval for unchanged scope.
“Check tests” is ambiguous: inspect safely or resolve whether analysis, execution
or authoring is wanted. A proposed transition remains unperformed until its
missing material scope/approval is resolved. A requested plan/report path is a
separate artifact-write scope; never save populated output inside plugin cache.

## Execution preflight

Before each materially different command, identify:

1. **Command and checked state:** exact observed command/entry, arguments,
   working directory, selected tests/filters and actual revision/uncommitted scope.
   Inspect project scripts/helpers, hooks, imports, plugins, fixtures and
   setup/teardown relevant to effects. Dry-run/list/collect labels are not immunity.
2. **Environment and target:** actual tool/config availability and supported
   project versions; non-production resource identity/isolation from safe
   metadata or an authorized owner, plus uncertainty. Never use production to
   make checks pass. An environment variable named TEST_DB proves no isolation.
3. **Data and destinations:** synthetic/test data, file/DB/network targets and
   permitted outputs. Minimize data; do not read/expose connection secrets,
   credential files or bulk environment variables for discovery.
4. **Effects and recovery:** anticipated build caches/results/artifacts, database
   setup/migrations/cleanup, network calls, service/container startup and teardown;
   scope, reversibility and task-owned process/time limits where relevant.
   A migration file is not permission to execute it. No automatic baseline/snapshot
   updates, shared-resource reset or destructive cleanup.
5. **Authority and gaps:** compare actual effects to request, accepted policy,
   valid scoped approvals and host permission. Use
   [governance](../governance/ai-usage.md) and [approval reuse](../governance/human-approval.md)
   for material effects; do not add a keyword-only approval gate. No new browser,
   container or dependency installation without actual approval. No tool grants
   permission to bypass a host denial, organization ban or this workflow's
   non-production boundary.

Do not execute unknown/untrusted code to determine whether it is safe. Inspect
the relevant execution path within permitted scope; if required effects/target
cannot be established, hold that check and report the missing prerequisite.
This preflight is bounded review, not proof of complete transitive isolation.
Continue independent safe assessment or already authorized unaffected checks.

## Environment and effect decisions

| Observed condition | Treatment and report |
| --- | --- |
| Existing isolated local unit runner, effects within the request | Run the exact scoped check without new ceremonial approval; inspect/report results and artifacts. |
| Missing browser/driver/container/service/dependency | Do not install/start infrastructure outside authorization. Identify the evidenced missing prerequisite; required check BLOCKED, no assertion results invented. |
| Test script contacts an unknown/shared/production database or applies migrations | Hold until an authorized non-production target and actual effects are established. Production remains excluded; inspect or propose an isolated alternative. |
| Known test DB migration/reset under accepted sensitive-action policy | Separate execution from test-file authoring; require the policy's scoped approval if not already supplied. Existing explicit matching approval can suffice. |
| Script downloads tools, uses credentials or rewrites tracked snapshots/source | Hold uncovered effects; choose an available safe scoped alternative only with honest equivalence limits, or seek missing scope. Never present an alternate as the blocked mandatory check. |
| Command denied by host or organization | BLOCKED for that execution; no bypass, configuration weakening or recycled approval. Analysis may continue within actual access. |
| Runner exits before discovery/setup completes | Report observed failure/blocker and any known partial results; tests not reached have no PASS or guessed zero count. |
| No tests selected or many skipped | Report actual selection/outcomes and reasons if observed; missing required behavior remains a gap, not coverage or green acceptance. |
| Unrelated baseline failure or suspected flakiness | Retain failure and comparison limits using shared recovery; do not delete/skip/change assertions or rerun indefinitely. |
