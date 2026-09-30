# Reproduce native integration checks

Checked **2026-09-29**; commands were rechecked against
[official sources](../research/SOURCES.md#prompt-26-native-revalidation) and
[installed help](../evidence/live/native-help.json).
Current authorization is **native checks without quota**. Steps involving an
agent/model below are a future manual protocol, **NOT_RUN**, not permission to run.

## Prepare and capture

1. Recheck Build Contract, current tree, actual host/help and candidate digest.
   Use the unchanged P23 archives in dist/archives. Do not run a consumer generator.
2. Create a fresh disposable directory with spaces, separate project, native
   state and operator evidence directories. No authentication/config is copied
   from the user's real profile. Do not change HOME or the parent shell's state.
   Pass a documented configuration root only in the child process environment.
   Preserve managed policies; state relocation is not a sandbox.
3. Seed only synthetic human instructions, a legacy Memory file and project
   policy. Snapshot bytes and timestamps before each phase. Keep baseline/oracle
   data outside agent context; final diff cannot reveal every transient write/read.
4. Extract regular, contained archive entries. Reject escaping/case-colliding
   paths and symlinks; the existing safe_extract function in
   [packaging tests](../../tests/packaging/test_distributions.py) provides the
   reviewed developer helper. Never mutate release manifests to make a test pass.
5. Store full actual argv, cwd, host/extension version, child-state scope,
   stdout/stderr, exit code and times in a new attempt file. Do not overwrite
   first failure evidence. Capture screenshots only through a real UI.
6. Query only the test candidate/catalog. Stop if native operations resolve to
   existing user state or require an unapproved network/auth/model operation.
   No safety-bypass flag or changed organization/native permission is permitted.

Python subprocess env mappings used in this run were child-only
CLAUDE_CONFIG_DIR and CODEX_HOME respectively, pointing at newly created empty
directories. Parent settings/environment were not repurposed. The new Codex
configuration was checked for its synthetic source before installing. These
observations cover known state/cache paths, not all possible host OS effects.

## Claude CLI: reproduced no-quota subset

Substitute observed local paths for the placeholders. Each row is a separate
command; use the native executable resolved from the installed launcher.

| Operation | Command form | Evidence / expected boundary |
| --- | --- | --- |
| Version | claude --version | Actual 2.1.220 |
| Native validation | claude plugin validate <extracted-plugin-root> | Exit 0 without warnings (version/author set 2026-09-30) |
| Strict validation | claude plugin validate --strict <extracted-plugin-root> | Actual exit 1; preserve warnings, no fabricated metadata |
| Empty isolated inventory | claude plugin list --json | Actual empty list in fresh child state only |
| Directory discovery | claude --plugin-dir <extracted-plugin-root> plugin details kiyo-axiom-framework | Actual eight component names; no agent turn |
| ZIP discovery | claude --plugin-dir <copied-local-zip> plugin details kiyo-axiom-framework | Same eight names; persistent list remains empty |

See [directory run](../evidence/live/claude-native-attempt-02.json) and
[ZIP run](../evidence/live/claude-zip-attempt-01.json). Shell metadata inspection
does not test slash invocation, Core reads or always-on behavior. Native
projected token costs are estimates, not measured context overhead.

For persistent marketplace lifecycle follow the
[Claude protocol](claude-installation-test-protocol.md) with a real authorized
catalog name/owner, verified disposable configuration and explicit local scope.
The session-only route does not require those publication identities and does
not establish persistent installation. Do not invoke plugin eval or send a prompt
under the present no-quota scope.

## Codex CLI: reproduced no-quota lifecycle subset

In the disposable catalog, place the unchanged plugin at
plugins/kiyo-axiom-framework and write .agents/plugins/marketplace.json containing:

```json
{
  "name": "kiyo-p26-disposable",
  "interface": { "displayName": "Kiyo P26 disposable local test" },
  "plugins": [
    {
      "name": "kiyo-axiom-framework",
      "source": { "source": "local", "path": "./plugins/kiyo-axiom-framework" }
    }
  ]
}
```

This is the exact **synthetic, private test catalog** used in P26, not a release
marketplace/publisher choice. Do not register the unresolved production template.
The public ingestion failure is retained; a local native install tests a different
acceptance boundary.

Run with the disposable child state and synthetic project cwd:

```text
codex --version
codex plugin marketplace add <disposable-catalog-root> --json
codex plugin list --marketplace kiyo-p26-disposable --available --json
codex plugin add kiyo-axiom-framework@kiyo-p26-disposable --json
codex plugin list --marketplace kiyo-p26-disposable --json
```

Read installedPath from the actual response. Confirm it resolves within the
disposable root before reading or removing it. Compare bytes with distribution;
inspect eight entry files and use the existing standalone
[checker](../../tools/verify_payload.py) copied outside the source tree:

```text
python -I -B <copied-checker.py> <actual-installedPath> codex --deny-probe <original-source-file>
```

That is **static cache inspection**, not a model read trace. It passed here.
The CLI reported 1.0.0 without a manifest version: keep manifest version UNSET
and record the fallback separately. The temp helper-path warning did not prevent
these management commands; do not disable that host restriction.

After recording project/cache snapshots, uninstall only the verified candidate:

```text
codex plugin remove kiyo-axiom-framework@kiyo-p26-disposable --json
codex plugin list --marketplace kiyo-p26-disposable --available --json
codex plugin marketplace remove kiyo-p26-disposable --json
```

Actual [install](../evidence/live/codex-native-attempt-01.json) /
[removal](../evidence/live/codex-lifecycle-attempt-01.json) leave the three
synthetic project files unchanged and remove the cache. The local source remains.
Do not manually delete guessed directories. A new list process is not a new
agent session. No generic plugin update flag is inferred; a second candidate
and actual replacement semantics remain required.

## Independent IDE and Copilot reproduction

| Target | Required setup and native path | Current limit |
| --- | --- | --- |
| Claude VS Code | Disposable VS Code instance plus separately isolated Claude state; observe active bundled engine. In the Claude panel use /plugins and the target's local-scope catalog flow | Metadata found; no GUI session, account or isolation observation |
| Codex IDE | Recheck official plugins support before starting | Native plugins UNSUPPORTED; do not copy skills to global locations or treat terminal Codex as IDE coverage |
| Copilot CLI | Locate authorized executable, inspect version/help and establish disposable state. Use copilot plugin install <prepared-directory>, then plugin list; record actual skill selector before use | No PATH match; no installation performed |
| Copilot VS Code | Separate editor data/extension roots, actual Copilot harness/account. Use native agent-plugin UI or documented chat.pluginLocations pointing to prepared directory in isolated settings | No matching extension metadata in bounded lookup; no native UI operation |

VS Code documents --user-data-dir and --extensions-dir; local --help confirms
them. A fresh profile alone does not establish extension-native account/cache
isolation. Do not install a VSIX runtime for Kiyo or change global discovery
settings. [Copilot lifecycle](copilot-installation.md) and
[protocol](copilot-local-test-protocol.md) contain source-dependent update/
uninstall forms; recheck the actual installed help before executing.

## Future model and activation trials

Use [twelve cases](../../tests/live/cases.json) separately for each target.
For a referenced P25 case, read its exact input and fixture bundle from
[catalog](../../tests/behavioral/evaluation/catalog.json) /
[fixtures](../../tests/behavioral/evaluation/fixtures.json). Materialize only the
synthetic workspace data. The P25 helper may prepare it, but never pass the
source-guided framework/ or operator/user-input envelope to a native trial.
Load the actual native package and use the observed picker/selector instead.

- LT-02: invoke all eight discovered entries with the listed P25 bounded intents;
  record selector, entry/Core reads, native approvals and effects independently.
- LT-03–07: compare allowed changes and actual tool events against separate
  expected criteria. For LT-06 use two fresh fixtures for observation/decision
  drift. For LT-07 native denial, use only a predeclared local synthetic marker
  under an existing observable native restriction; never use production or secrets.
- LT-08: make the original checkout unavailable in the test environment and
  record actual host resource reads. Static checker isolation alone is insufficient.
- LT-09: run fresh sessions with no bootstrap and with a separately authorized
  managed block. Preserve human content and module scope; use no explicit skill
  hint for this automatic case. No native facility promises universal activation.
- LT-10: a separately approved synthetic policy revision and actual artifact
  digest must be read in a fresh agent session. Do not invent a release version.
- LT-11/12: compare real reviewed candidate identities and state snapshots,
  including human managed-block edits, before/after native lifecycle operations.
  Uninstall leaves policy/Memory; separately requested cleanup removes only Kiyo's
  exact managed block, never the entire instructions file.

These model steps remain NOT_TESTED. Obtain host/account/turn or spend authority
before any model call. Preserve first/rerun evidence and report denied or missing
checks honestly. See [remaining tests](live-owner-required-tests.md).
