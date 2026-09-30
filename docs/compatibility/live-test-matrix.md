# Native integration results — Prompt 26

Checked **2026-09-29**. User selected **native checks without quota**.
No model turn, sign-in, credential copy, global install, organization setting
change or publication was performed. The current authoring chat is not a Kiyo
host test. [Actual records](../evidence/live/README.md) and
[reproduction](live-reproduction-guide.md) separate observations from expectations.

| Target | Observed environment | Verified subset | Remaining native result |
| --- | --- | --- | --- |
| Claude Code CLI | 2.1.220; Windows 10.0.26200 | Native manifest validation, relocated directory/ZIP component inventory: eight Skills, no agents/hooks/MCP/LSP | Marketplace install and every model/activation/lifecycle case NOT_TESTED |
| Claude Code VS Code | Editor 1.139.1; extension metadata 2.1.283/2.1.284; active engine UNKNOWN | Installed metadata only | NOT_TESTED; no usable native GUI automation or established disposable IDE/account context |
| Codex CLI | 0.158.0; same Windows host | Disposable local catalog install/list, byte-matching native cache, uninstall preserving synthetic project files | Skill discovery/invocation, policy/Core loading, update and model behavior NOT_TESTED |
| Codex IDE Extension | Metadata 26.917.62051; active UNKNOWN | No native Kiyo result | Native plugins UNSUPPORTED in current official docs; execution NOT_TESTED; no fallback adopted |
| GitHub Copilot CLI | No executable resolved on inspected PATH; version UNKNOWN | No native Kiyo result | NOT_TESTED; alternate installation/account unknown |
| GitHub Copilot VS Code | Editor 1.139.1; named Copilot extension metadata not found in inspected directory | No native Kiyo result | NOT_TESTED; active/alternate environment and account unknown |

Sources/date/limitations: [P26 source register](../research/SOURCES.md#prompt-26-native-revalidation).
UNSUPPORTED describes documented capability; it is not an executed failure.
VERIFIED means only the stated observed property, and can describe a real failed
check. DOCUMENTED_ONLY means documentation exists without an actual result.
NOT_TESTED means the particular execution has not occurred. None means certified.

## Twelve independent checks per target

V = VERIFIED/PASS for the bounded complete check; N = NOT_TESTED/NOT_RUN;
U = UNSUPPORTED native plugin capability with no execution.
A footnote describes partial evidence without upgrading the full check.
All **72 records** include method/scope/status/observations/evidence/limitations;
the separate [case definitions](../../tests/live/cases.json) hold expected behavior.

| Check | Claude CLI | Claude VS Code | Codex CLI | Codex IDE | Copilot CLI | Copilot VS Code |
| --- | --- | --- | --- | --- | --- | --- |
| 01 Native installation and discovery | N (a) | N | V (b) | U | N | N |
| 02 Eight Skills visible and loadable | N (a) | N | N (c) | U | N | N |
| 03 Explicit Init writes only approved Memory/config | N | N | N | U | N | N |
| 04 Simple Implement and real verification | N | N | N | U | N | N |
| 05 Review-only writes zero files | N | N | N | U | N | N |
| 06 Observation drift versus decision conflict | N | N | N | U | N | N |
| 07 Sensitive approval and native restriction | N | N | N | U | N | N |
| 08 Relocated/cached resource reads by agent | N (a) | N | N (c) | U | N | N |
| 09 Fresh-session automatic activation | N | N | N | U | N | N |
| 10 New session observes current policy/version | N | N | N (d) | U | N | N |
| 11 Update preserves Memory/human bootstrap | N | N | N | U | N | N |
| 12 Native uninstall preserves user state | N | N | V (e) | U | N | N |

- (a) Claude native details enumerated eight entries from a relocated directory
  and ZIP. This is component discovery, not installation or body/Core execution.
  Normal validation exits 0 with missing version/author warnings; strict exits 1.
- (b) Codex registered a test-only local catalog and installed the unchanged
  candidate in a fresh child state directory. No real publisher identity or
  publication catalog was invented.
- (c) The real Codex cache contains all 795 distribution files unchanged. An
  independent static checker passes eight entries and 4,956 contained links.
  Its source-read guard is not a host sandbox; no agent read trace exists.
- (d) A new management process sees installed/enabled state. This is not a new
  agent session or verified policy refresh.
- (e) Actual uninstall removes the candidate cache and installed entry. Three
  synthetic files (human AGENTS, legacy Memory, project policy) remain byte-identical.
  No generated managed block, alternate layout or upgrade was exercised.

Detailed results:
[Claude CLI](../evidence/live/claude-cli.json),
[Claude VS Code](../evidence/live/claude-vscode.json),
[Codex CLI](../evidence/live/codex-cli.json),
[Codex IDE](../evidence/live/codex-ide.json),
[Copilot CLI](../evidence/live/copilot-cli.json),
[Copilot VS Code](../evidence/live/copilot-vscode.json).

## Interpretation and remaining gates

Only **two complete lifecycle rows** above pass; additional partial checks have
their own evidence. There is no workflow compliance score or six-target PASS.
P24 static results and all 48 P25 NOT_RUN observations remain unchanged.

The Codex installer reports **1.0.0** despite an unset manifest version; this is
an observed native fallback, **not Kiyo's release version**. Prior Codex public
ingestion failure remains open; local installation does not satisfy ingestion.
Claude's projected token count is not measured usage or automatic Core evidence.
Update needs a real reviewed second candidate and verified replacement method.

[Owner-required remaining tests](live-owner-required-tests.md) gate compatibility/
release claims. Documentation work can continue with these limits visible.

## 2026-09-30 update

Live model runs now exist. All eight Skills passed the
[live E2E harness](../../tests/live/e2e/README.md) on Claude Code and Codex; Copilot CLI
install/discovery passed and model execution is BLOCKED pending `copilot login`
([details](live-owner-required-tests.md#update-2026-09-30)). The Prompt 26 record above is unchanged.
