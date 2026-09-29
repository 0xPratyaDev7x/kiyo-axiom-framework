# Copilot local/disposable test protocol

**PLANNED / NOT_RUN** live tests for a user-requested Prompt 26.
Checked 2026-09-29 against
[CP22-01–16](../research/SOURCES.md#prompt-22-copilot-revalidation).
Prompt 22 runs only developer packaging/static checks and scoped local metadata
inspection. No CLI/VS Code native installation, plugin inventory sweep or chat
session is launched by this protocol's existence.

## Preflight

Use a separately authorized disposable OS/test-user environment, or demonstrate
equivalent isolation for native state, caches, editor data and CLI-discovered
plugins before mutation. A workspace or fresh editor profile alone is not proof
of isolation. Do not repurpose active HOME/COPILOT_HOME, copy credentials, dump
environment variables, change organization policy or grant broad permissions.
If isolation or required host/account access cannot be established, mark only
the dependent target/check BLOCKED/NOT_TESTED.

Record actual host/editor/extension/OS versions, Copilot session/harness,
permitted account/policy context without secrets, package digest/source and
test output scope. Resolve any source/metadata gates required by the chosen route.
No fake version/publisher/catalog and no public registration is necessary for a
bounded local-source trial. Inspect installed help before using documented forms.

Prepare synthetic projects with human sections, accepted instruction files,
root and module scope, legacy Memory paths and a no-Git fixture. Snapshot files
before testing. No actual production data, external probes, suspicious executable,
dependency/scanner/browser install or Actions execution is needed.

## CLI protocol

1. Install the prepared directory only inside the disposable native state via
   the [documented route](copilot-installation.md). Capture the actual resolved
   install location and side effects; do not assume a project-scope flag.
2. Inspect the native candidate and all eight skill identities. Test collision
   cases (including built-in init/review and an identically named local skill)
   without changing canonical identities to hide a failure. Establish the
   actual safe selector; report UNKNOWN/BLOCKED if it cannot be disambiguated.
3. Invoke each entry with bounded intent. Inspect actual entry/Core/reference
   reads, not just the resulting text. Record explicit selection separately
   from description matching and an unrelated request.
4. Test no-bootstrap use, then separately authorized Init insertion into an
   existing instruction file; preserve human bytes, legacy paths and module scope.
   Repeat/no-delta must make no write. Test conflicting instructions, denied
   writes and ambiguous markers without overriding them.
5. Confirm instruction discovery/use in the actual session. Apply a new-session
   requirement where documented. An instructions list is discovery evidence only.
6. Make the developer checkout unavailable in this test and verify native cached
   resource reads. Distinguish direct cached install from local-marketplace
   live-path behavior. Relocating ordinary files in Python is not this trial.
7. Exercise named update/reinstall, disable/enable and uninstall within approval.
   Use a real approved candidate/digest for update; if no such version/source
   exists, block that subcase instead of inventing a release. Snapshot project
   state and check residual user instructions/Memory independently.

## VS Code protocol

1. Record the actual Copilot Agent Host/Local session and independent editor
   capability settings. Native plugin support is documented, not proved by the
   terminal result. Do not switch to another provider/harness as a silent fallback.
2. Use a verified disposable local-plugin location or approved source/catalog.
   Record UI registration and physical storage independently; discovery of a
   CLI-installed candidate is a separate trial path.
3. Inspect Configure Skills, slash-menu qualification and source. Invoke all eight
   entries with actual /kiyo-axiom-framework:<skill> UI selections only when discovered.
   No selection trace means no verified invocation.
4. Separately test implicit matching, unrelated tasks, explicit mode mismatch,
   actual Core reads and missing resources. A supported slash entry does not
   prove always-on Core.
5. Perform authorized bootstrap/no-op/concurrent-human-edit trials. Preserve
   .github/copilot-instructions.md, path-specific applyTo, nested instructions
   and monorepo scope. Check read-only questions where file globs may not attach.
   Do not enable global/parent discovery settings to make scope appear correct.
6. Exercise update, workspace disable/enable and uninstall through native UI;
   record source-dependent disk retention and possible CLI-store interaction.
   Ensure removal does not erase user-owned config, Memory or human instructions.

## Evidence and closure

Run [the target-separated cases](../../tests/integration/copilot/scenarios.md).
Each check records name, applicability, actual command/UI method, inspected
scope, execution status, observed result, evidence location, limitations and
baseline relation. Record actual times/counts/versions only. Keep CLI and VS Code
columns independent, including failures and missing prerequisites.

Static schema/link/parity success does not certify native acceptance, policy
enforcement or prompt-injection safety. Runtime side effects outside the prepared
fixtures are a failed isolation boundary, not permission for cleanup outside
scope. Preserve evidence safely and obtain a scoped decision for recovery.
