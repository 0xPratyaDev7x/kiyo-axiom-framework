# Prompt 26 actual native evidence

Date: **2026-09-29**. Baseline main:
cb4647c56c2ea0c711d9c35b861c0ad0fc76280a; initial index/tree clean.
User selected “ทำเฉพาะ native checks ที่ไม่ใช้ quota”.
No agent/model evaluation, sign-in, paid API call or synthetic transcript occurred.
This directory is developer evidence and is excluded from every plugin payload.

## Executions

| Evidence | Actual result | Interpretation / limit |
| --- | --- | --- |
| [Environment](environment.json) | Claude/Codex/Code launchers found; Copilot PATH lookup null; VS Code version exit 0; three named extension manifests read | Installed metadata is not active engine/account. VS Code stderr reports crashpad access denial |
| [Claude first attempt](claude-native-attempt-01.json) | Version and normal native validation exit 0; warnings retained | Harness console printing fails afterward with Python cp1252 UnicodeEncodeError for U+203C; partial evidence preserved |
| [Claude second attempt](claude-native-attempt-02.json) | Version 2.1.220; normal validation exit 0 with two warnings; strict validation exit 1; isolated list empty; directory details lists eight Skills | Rerun fixes console serialization only (ASCII-escaped output). No product or metadata change |
| [Claude ZIP](claude-zip-attempt-01.json) | Copied ZIP details lists the same eight entries; persistent list remains empty | Session metadata load only; no cache SKILL.md under inspected Claude state, no agent resource reads |
| [Codex installation](codex-native-attempt-01.json) | Version 0.158.0; local catalog registration/list/install each exit 0 | Fresh child configuration confirmed before install; local fixture catalog only; native helper-path warning retained |
| [Codex lifecycle](codex-lifecycle-attempt-01.json) | Fresh-process list shows installed/enabled; cache bytes equal distribution; static cache audit exit 0; remove/list/catalog remove exit 0 | Native cache removed; three synthetic project files unchanged; source retained; no model sessions/update |
| [Local help](native-help.json) | Actual help/version grammar captured before dependent commands | Some exploratory app-server help only; no app-server or daemon launched |
| [Editor diagnostic](vscode-crashpad.log) | Three crashpad access-denied lines produced by code version/help | Incidental debug.log moved from checkout root after checking its contents and containment; no IDE integration result |

Every command record preserves actual argv, exit code, stdout/stderr and available
UTC timing. No screenshot was captured. Absolute machine/temp paths belong only
to evidence, not product payloads. Incomplete first-attempt timestamps/snapshots
are not reconstructed as successful results.

## Isolation and identity

Native trials used new temporary paths containing spaces and synthetic project
files. Child-only configuration roots were passed through documented environment
mechanisms; parent HOME/environment/settings were not modified by the harness.
No credentials were inspected/copied; no broad permission option was passed.
This is scoped native state management, **not an OS sandbox or comprehensive
filesystem/network monitoring claim**. Actual generated paths/results are in JSON.

The Codex fixture catalog name kiyo-p26-disposable is a temporary test identifier,
not an owner/publisher/public listing. P26 authorizes disposable sources; it
does not fill the inactive release marketplace template or DEC-001/003. This
narrow test uses unchanged optional-metadata development bytes and tests native
acceptance directly. Public ingestion remains a separate, previously failed gate.

Manifest version remains UNSET. The native Codex add/list response's 1.0.0 is
recorded as a host fallback only. All three archive identities remain the P23
bytes; package signatures and release metadata have not been invented.

## Failures and remaining gaps

[First record audit](record-audit-01.json) passes seven developer checks of
evidence/structure/hash/link/trace consistency. It is not another host trial.
The final closure rerun uses the same audit with exact interpreter argv and
input/source hashes added, retaining attempt 01. The final file is
record-audit-02.json; no native test failure is deleted or reclassified.

- Native Claude strict validation FAIL: missing owner version/author. No fix
  fabricated; normal acceptance with warnings remains a separate result.
- Developer probe attempt 01 stopped while printing Unicode to a cp1252 pipe;
  attempt 02 uses ASCII-safe console JSON and preserves the first evidence.
- Codex warns it refuses helper binaries under a temp directory, while the
  tested plugin management commands still exit 0. No bypass/relocation was used
  to weaken that host restriction; no inference about later agent tools.
- VS Code version output is available despite a crashpad diagnostic. No elevated
  launch was needed for the successful metadata query; GUI operation untested.
- All model workflows, activation, native permissions and updates remain untested.
  IDE/Copilot gaps and Codex IDE unsupported capability are independently recorded.

See [matrix](../../compatibility/live-test-matrix.md),
[reproduction](../../compatibility/live-reproduction-guide.md) and
[remaining tests](../../compatibility/live-owner-required-tests.md).
