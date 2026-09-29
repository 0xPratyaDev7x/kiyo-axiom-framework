# Prompt 25 behavioral suite — offline delivery

Checked: 2026-09-29. **DONE for the user's selected offline suite/protocol scope**.
**48 behavioral host cases NOT_RUN; 13 offline helper tests PASS.**
No paid API, external quota, host/model call or native installation was performed.

## Authority and baseline

The initial task requested real-host behavioral evaluation and permitted honest
NOT_RUN protocols when execution could not proceed. After scoped PATH discovery,
the user explicitly chose: “ทำ suite/protocol แบบ offline; host cases คง NOT_RUN”.
This selection governs the present scope; we do not claim installed CLIs are absent.

Baseline: main, HEAD `cef426c3cf228df95945572ce3a782589930f0ac`, initially clean
worktree/index, Prompt 24 committed. Applicable instruction lookup found none.
No .kiyo store was created. Existing LICENSE, naming, version/history, canonical
content, native overlays, builder code and distributions remain unchanged.

[Environment observations](environment.json) record actual PowerShell PATH
resolution for Codex and Claude launch scripts and no Copilot PATH match.
Versions/model/account/settings remain UNKNOWN; those programs were not invoked.
This does not prove a host is unavailable or that an alternative installation
does not exist. All six native targets retain independent NOT_TESTED states;
the prior Codex IDE unsupported route/ingestion failure is not changed.

## Delivered dataset and separation

[Catalog](../../../tests/behavioral/evaluation/CATALOG.md):
32 Skill cases, four for each of the eight public Skills, plus 16 cross-cutting.
Each JSON case has exact user input, fixture/initial state, requirement/control
IDs, explicit or automatic-selection delivery, allowed/forbidden effects,
expected criteria, evidence reference and limitations. BEH-MEM-03 adds an exact
second turn to check no-delta synchronization.

[48 observation records](observations.json) are in a different file from expected
criteria. Each has host/model/version/settings fields, requested/observed
activation, outputs/actions/diff, objective assessment, separate human/model
grading, result/evidence path and limitations. All are NOT_RUN, without simulated
transcripts, invented commands, host counts or model grades. Earlier forward
trials are not imported as fresh executions.

There are 31 reusable synthetic fixture bundles, materialized only in fresh
disposable directories. No real secrets, PII, production endpoints or external
destructive operations are present. Local side-effect examples use harmless
canary files. Scripts were parsed as source, never executed by preparation.

Automatic cases test Skill selection **after explicitly supplied Core**.
Native automatic loading and installed/cache behavior remain separate untested
claims, reserved for independent host evidence. Source-guided preparation adds
no native bootstrap, permissions or public skill.

## Actual offline execution

Command, repository-root cwd:

```powershell
python -B tests/behavioral/evaluation/test_suite.py --report docs/evidence/behavioral/harness-results-01.json
```

Exit **0**; **13 tests**, **0 failures**, **0 errors**, **0 skipped**.
Python **3.11.9**, OS **Windows-10-10.0.26200-SP0**.
Actual UTC interval: 2026-09-29T12:28:41.726605+00:00 through 2026-09-29T12:29:29.162702+00:00.
[Complete execution](harness-results-01.json) retains command/output, versions,
timestamps, consulted/source hashes, scratch location and two actual helper CLI
subprocess commands with exit/output. This is the first offline harness run;
there was no failed host attempt or host rerun to invent.

| Check/method | Scope and observed result | Status | Evidence / limitation |
| --- | --- | --- | --- |
| Catalog/control validation | 48 unique cases; four per Skill; 16 cross-cutting; real control/requirement IDs and required adversarial tags | PASS | test_01; inventory/structure, not behavior |
| Materialization/snapshot | All 48 actual fresh fixtures; eight entries and 105 canonical resources each; immediate snapshots stable | PASS | test_02; no host acted, so stability is not unauthorized-write accuracy |
| Fixture source parsing | 52 Python bundle file occurrences parsed without execution | PASS | test_03; no safety proof from parsing |
| Invalid scope/overwrite rejection | Unsafe paths, unknown case, existing destination and in-repository fixture destination rejected | PASS | tests_04–05; no deletion/cleanup |
| Objective comparison negatives | Planted byte change, timestamp-only touch, framework edit, added/deleted/case-distinct paths detected with expected classifications | PASS | tests_06–09; planted by helper tests, not observed agent defects |
| Capture/history | Existing label refused; second-turn baseline supported; invalid label/baseline rejected | PASS | test_10; files are not tamper-proof logs |
| Honest unrun ledgers | 48 NOT_RUN with empty observations, null grades and eight unmeasured metrics | PASS | test_11; empty data does not mean no forbidden effects occurred |
| Actual helper CLI | Real prepare and capture subprocesses exit 0; host_execution_claim false | PASS | test_12; no coding host invoked |
| Exclusion/history | 112 reviewed product inputs exclude test/evidence data; prior 37-test P24 record preserved | PASS | test_13; current product acceptance not inferred |

Each row is required by the offline suite scope. Command/evidence location and
baseline relation are shared above: new developer-only harness against unchanged
P24 product inputs. Results apply only to the recorded hash snapshot. Expected
answers, fixture historical PASS text and harness mutations are not host results.

No further runtime rerun was warranted after this successful run because only
documentation/build-state records were added afterward. Future fixes require
new immutable execution files; [protocol](../../../tests/behavioral/evaluation/protocol.md)
requires first attempt and rerun history, not overwritten evidence.

## Metrics, defects and remaining gates

[Metric ledger](metrics.json): all values/denominators null. Routing accuracy,
unauthorized writes, hallucination, approval/Memory conflict handling, evidence
honesty, interruptions and context/token overhead have **not been measured**.
Objective file/tool evidence, human adjudication and optional model grades are
kept distinct in the [grading contract](../../../tests/behavioral/evaluation/metrics-and-grading.md).

[Defect register](defects.md) records no claimed host verdict and critical release
blocker rules. One authoring-call variable typo was corrected before the first
harness test, without changing product guidance or a scenario invariant.
No product fix is justified by an unexecuted behavioral case.

Full requirement verification remains NOT_RUN; 79 partial/1 not implemented
counts are unchanged. See [traceability](../../build/TRACEABILITY.md) for P25
**case/protocol coverage**, not behavioral PASS. Native tests remain NOT_TESTED,
Codex ingestion FAIL/IDE UNSUPPORTED and P23 filesystem-symlink BLOCKED remain open.

Memory Impact: NONE. Safe to continue: **YES for user-requested Prompt 26 Live
Host Tests**, with explicit case/host/quota authority and preserved owner gaps.
Prompt 25's offline selection is not permission to launch those tests. Stop here.

