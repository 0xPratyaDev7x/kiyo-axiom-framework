# PostgreSQL profile

**First inspect actual versions, configuration, toolchain and architecture:**
repository database/driver declarations, migrations and runner configuration,
CI and data-access boundaries, plus authorized observed server/client versions
when available. Distinguish declared, local test and deployed state. Do not
connect to discover an unknown target or expose credentials. A package/folder
name alone cannot establish a PostgreSQL server or production schema.

Apply [KIYO-PROF-001](extension-contract.md), relevant
[engineering checks](../framework/engineering/index.md) and
[dangerous-action boundaries](../governance/dangerous-actions.md).

- **Creating a migration file and executing a database operation are separate
  actions.** Preserve the project's migration naming/history/tool. A request to
  draft a migration does not authorize apply, rollback, seed, drop or a test that
  performs those operations.
- Before execution, establish the exact target/environment, authorized data,
  effects, reversibility, blast radius and applicable approval. Inspect test
  setup and migration hooks. Unknown targets or unmet required controls hold
  dependent execution; production restrictions still apply despite “approval.”
- Inspect data invariants, nullability, keys/constraints and current consumers.
  Consider existing data/backfill, concurrency, lock duration and compatibility
  for the specific change; do not infer schema/business rules from names.
- Use parameter binding through the actual driver rather than concatenating
  untrusted values into SQL. Dynamic identifiers require the driver's supported
  safe handling/allowlisting, not an assumption that value parameters cover them.
- Inspect transaction boundaries, error handling and retry/idempotency needs.
  Verify operation/runner/version support; never promise every migration can be
  rolled back or is safe merely because it is wrapped in a transaction.
- Choose controlled integrity/transaction/regression checks as justified; do not
  tune indexes, change server versions or modernize persistence for a tiny fix.

Completion evidence: scoped migration/query diff or findings, verified version/
target facts and Unknowns, integrity/compatibility reasoning, authorized checks,
actual effects observed, rollback limits and unrun operations.

Optional provenance, **checked 2026-09-29, DOCUMENTED_ONLY**:
[PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
and [libpq parameter execution](https://www.postgresql.org/docs/current/libpq-exec.html).
The current aliases displayed documentation 18 on that date; they do not establish
the target server version. The latter documents libpq, not every driver's API.
Use version/driver-specific official references when needed. No database operation,
PostgreSQL fixture or native-host profile execution is claimed.
