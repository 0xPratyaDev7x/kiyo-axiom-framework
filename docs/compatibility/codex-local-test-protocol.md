# Codex local/disposable test protocol

P26 follow-up: [actual no-quota reproduction](live-reproduction-guide.md)
uses a synthetic test-only local catalog and unchanged unversioned payload.
The user-authorized disposable source does not fill release owner fields or adopt
a publisher; local native acceptance is tested separately from public ingestion.
Agent/model steps below remain NOT_RUN under the user's no-quota selection.

**PLANNED / NOT_RUN** for live testing in a user-requested Prompt 26.
Sources checked 2026-09-29:
[CX21 register](../research/SOURCES.md#prompt-21-codex-revalidation).
Prompt 21 ran only Codex version/help observations, developer packaging/static
checks and the local ingestion validator. No session, install or live invocation.

## Preflight and isolation

Use the prepared dist/codex/kiyo-axiom-framework artifact; no end-user generator.
Record actual artifact digest, CLI/OS/extension versions, permitted account context,
test scope and output location. Preserve real native policies and approvals.
The current candidate has three missing release identity fields; record the
ingestion validator's FAIL. Resolve applicable metadata/owner gates before
registration/installation; do not bypass them or insert fake identities.

Use a separately authorized disposable OS/container/test account context whose
home, repo and native state may be changed. Alternatively establish equivalent
isolation before mutation. [CODEX_HOME](https://learn.chatgpt.com/docs/config-file/environment-variables),
CX21-12, relocates documented state but is not proof that user skill/catalog
locations, credentials, managed rules or OS effects are isolated. Merely changing
a VS Code profile or one variable is insufficient. Do not repurpose the active
session's CODEX_HOME/HOME, read/copy authentication stores, dump environment,
change global permissions or weaken policy to arrange the test.

Create only synthetic authorized fixtures: root/nested AGENTS.md with human text,
an existing override file to observe shadowing without modifying it, legacy
Memory/config locators, a no-Git project and module-scoped examples.
Snapshot actual files/bytes before testing. No external probes, production
resources, suspicious payload execution or additional scanner/tool dependency
installation is needed.

## Catalog and installed CLI candidate

Use a completed owner-approved [catalog template](../../platforms/codex/marketplace.template.json)
only in the disposable context. Place the ready bundle at its relative source.
Do not register the unresolved template from this checkout. Catalog discovery
and repo enablement are not a claim of project-local storage.

Read installed help before native mutation. These forms were documented or
observed in local 0.158.0 help; **only their --help variants ran in Prompt 21**:

| Planned action | Form / evidence | Limit |
| --- | --- | --- |
| Source registration | codex plugin marketplace add <authorized-catalog-root>; CX21-01 and local help | Mutates native configuration; disposable context only |
| Install | codex plugin add kiyo-axiom-framework@<confirmed-catalog-name>; local help | No inferred --scope local option; verify actual storage/config effects |
| Discover | /plugins then a new session; CX21-06 | Browser availability does not prove all eight skills loaded |
| Select skill | /skills or $ picker; CX21-04 | Select actual Kiyo entry; record qualified spelling/source instead of guessing |
| Refresh Git catalog | codex plugin marketplace upgrade <confirmed-catalog-name>; local help | Refreshes catalog snapshot; not a verified installed payload update |
| Uninstall | codex plugin remove kiyo-axiom-framework@<confirmed-catalog-name>; local help | Help says it removes local cache; actual project-state preservation still needs testing |

Angle-bracket tokens are metavariables, not literal commands. No safety-bypass,
approval-disabling or global-install flags are proposed. Project config is loaded
only under documented trust conditions ([CX21-11](https://learn.chatgpt.com/docs/config-file/config-basic));
do not change trust or AGENTS.override.md to force an outcome.

## Discovery, loading and scope trials

Run [the integration cases](../../tests/integration/codex/scenarios.md) against CLI.
For each of eight entries record selected identity, actual resource reads, scoped
response/effects and limitations. Bound Implement/Test run/write/Memory sync to
separately authorized synthetic mutations. Read-only requests must preserve files.
Separate explicit selection, implicit matching, unrelated requests and Core reads.

For a bootstrap trial, approve the exact managed insertion, preserve human bytes,
reread before writing and compare repeat/no-op/conflict cases. Test module launch
directories, instruction shadowing, native context limits and new sessions.
A no-Git project uses the actual working scope rather than an invented Git root.
Never interpret a nested block as permission outside its authorized module.

Move/copy the actual installed payload through the native supported mechanism
and make the source checkout unavailable to that test. Record real resource
locations without embedding them in product text. Manual relocation results are
static evidence only. Missing/denied resources require an honest gap, not fetches
of replacement Core or a consumer build.

For updates use real approved candidates/digests and documented target commands.
If installed replacement semantics are unknown, hold that subcase; marketplace
refresh or restart alone is not proof of updated bytes. Verify project policy,
Memory and AGENTS human content survive update/disable/uninstall. Residual Kiyo
guidance is user-owned; cleanup requires a separate scoped edit.

## Independent IDE boundary and evidence

Current [plugin docs](https://learn.chatgpt.com/docs/plugins), CX21-06, exclude IDE
plugins. Do not run CLI installation as an IDE test or copy skills into a global
directory as an unapproved workaround. Record UNSUPPORTED capability and
NOT_TESTED native result. An owner-approved standalone experiment would be a
different distribution/lifecycle contract; no such approval is supplied here.

Use nine-field checks: name, applicability, command/method, scope, execution
status, observed result, evidence location, limitations and baseline relation.
Keep native test outcomes separate from static and ingestion-profile checks.
Record concrete missing prerequisites as BLOCKED/NOT_TESTED, and N/A only with an
actual applicability reason. Do not claim a native test passed from this protocol.
