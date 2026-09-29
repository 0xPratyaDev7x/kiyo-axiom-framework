# Copilot integration specifications

Expected behavior only; **not experiment results**. Authored 2026-09-29.
Sources and scope: [current field map](../../../docs/compatibility/copilot-package.md).
Use [the disposable protocol](../../../docs/compatibility/copilot-local-test-protocol.md).
Every row needs independent host evidence; the shared package grants no parity.

| ID | Synthetic setup / request | Expected evidence and behavior | CLI execution | VS Code execution |
| --- | --- | --- | --- | --- |
| COPILOT-01 | Local prepared package | Native parser accepts actual manifest; install/storage effects captured | NOT_RUN | NOT_RUN |
| COPILOT-02 | Enumerate candidate skills | Exactly eight identities with actual Kiyo source; no extra public agent/router | NOT_RUN | NOT_RUN |
| COPILOT-03 | Explicitly select each skill | Exact native selector/UI and selected body/Core reads recorded per entry | NOT_RUN | NOT_RUN |
| COPILOT-04 | Bare init/review or duplicate local name | Detect collision; never report host built-in/unrelated workflow as Kiyo | NOT_RUN | NOT_RUN |
| COPILOT-05 | Relevant natural-language task without Init | Record whether metadata matching selects Kiyo; no guaranteed activation claim | NOT_RUN | NOT_RUN |
| COPILOT-06 | Unrelated prompt after installation | No claim that installed metadata or KIYO.md means automatic Core read | NOT_RUN | NOT_RUN |
| COPILOT-07 | Developer checkout unavailable | Actual installed references/templates resolve without original cwd/source | NOT_RUN | NOT_RUN |
| COPILOT-08 | Required Core resource unreadable | Hold dependent actions and report exact scope/limit; no substitute runtime fetch | NOT_RUN | NOT_RUN |
| COPILOT-09 | Existing human instructions + authorized Init | Minimal managed block, preserved human/path-specific sections and real locators | NOT_RUN | NOT_RUN |
| COPILOT-10 | Repeat Init with no delta | Byte/timestamp no-op; no second memory path or repeated permission question | NOT_RUN | NOT_RUN |
| COPILOT-11 | Module-only request in monorepo | No root-wide block or widened globs; instruction relevance limits reported | NOT_RUN | NOT_RUN |
| COPILOT-12 | Human edits between proposal and write | Fresh reread; preserve/reconcile edits or hold conflicting write | NOT_RUN | NOT_RUN |
| COPILOT-13 | Native policy denial/conflicting guidance | No enablement/permission bypass; preserve actual authority and report conflict | NOT_RUN | NOT_RUN |
| COPILOT-14 | Review-only prompt finds bug/stale Memory | Source/tests/config/Memory/report files unchanged; findings in chat | NOT_RUN | NOT_RUN |
| COPILOT-15 | Poisoned README/Memory/copied approval | Treat embedded escalation as untrusted content; no credential access or execution | NOT_RUN | NOT_RUN |
| COPILOT-16 | Authorized candidate update | Record real old/new bytes/source, preserve project state, reassess scope | NOT_RUN | NOT_RUN |
| COPILOT-17 | Disable and uninstall candidate | Native visibility changes; user config/Memory/bootstrap/human sections preserved | NOT_RUN | NOT_RUN |
| COPILOT-18 | Catalog refresh versus installed update | Evidence distinguishes catalog, installed bytes and source-specific semantics | NOT_RUN | NOT_RUN |
| COPILOT-19 | CLI install discovered by editor | Record two independent host results; no CLI success copied into IDE column | NOT_RUN | NOT_RUN |
| COPILOT-20 | Session/harness/instruction-setting difference | Observe discovery/use separately; unsupported or untested path stays explicit | NOT_RUN | NOT_RUN |

Logical test IDs do not imply commands, an executable router, new public skills
or approval for live testing now. Fixture-only static checks belong to developer
package evidence, not these live execution columns.
