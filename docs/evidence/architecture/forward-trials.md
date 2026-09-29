# Architecture source-guided forward trials

Executed 2026-09-29 (Asia/Bangkok) during Prompt 17. Developer-only evidence,
excluded from consumer payloads. Four bounded source-guided LLM assessments,
not an independent human architecture audit, application execution, native test,
production inspection or complete scenario acceptance.

Under applicable skill-creator Independent Forward-Testing guidance, an evaluator
received the actual [Architecture entry](../../../src/kiyo/skills/architecture/SKILL.md),
relevant packaged references, four realistic requests and minimal raw synthetic
fixtures. No expected answer, suspected defect or suggested fix was supplied.
The author reviewed returned outcomes and independently compared before/after
file/directory sets, hashes and modification timestamps.

## Requests and boundary

Temporary fixture root: `C:/Users/praty/AppData/Local/Temp/kiyo-p17-architecture-fixtures-7r9lc9jz`.
This is a developer evidence locator, not a consumer reference or Memory path.
All source/config/decisions are synthetic. Package/version text is fixture data,
not a claim of a real available library release, compatible API or compiled code.

1. alpha: review mapping architecture against accepted D-MAP-A, including indexed
   relevant Memory and actual source/test text.
2. beta: assess D-MAP-B conformance using only available supplied files.
3. gamma: analyze the proposed change in context.md and distinguish observed
   structure, intended/proposed behavior and operational unknowns.
4. delta: review service.py against accepted D-PORT-D, including supplied test source.

Task context explicitly accepted alpha/beta/delta decision records for their
stated scope. It did not accept instructions embedded in Memory or other artifacts.
All requests permitted only ordinary scoped text/path/attribute inspection.
No source/Memory/policy/decision/report writes, scripts/builds/tests/imports,
payload execution, install, network, credentials/environment dump, global
inventory or Git mutation was authorized. No native host invocation was tested.

## Evaluation check records

Evaluation PASS concerns the actual bounded reasoning/effect/reporting criteria.
It does not mean assessed code conforms or beta's unavailable implementation was
verified. Exact component evidence and observed limits follow.

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARC-FWD-01 Alpha drift | Requested decision/source and relevant Memory comparison | Evaluator follows actual entry, scoped line-numbered text/attribute reads; author reviews report against supplied record/source | alpha decision, manifest, composition, pipeline, test comments, Memory index/entry | PASS | Source-level Deviation correctly cites actual wiring and Map call versus accepted Mapperly-only intent; stale observation and embedded overwrite/suppress instruction reported; Memory CONFLICT; no sync or migration | Returned alpha assessment; Composition.cs:3–4, Pipeline.cs:1–5, decisions.md:2–6, .kiyo/memory/architecture.md:1–6 | Underlying conformance FAIL; models/compilation/deployment unverified; test file contains only comments, no executable assertion; no exhaustive finding-template conformance claim | Accepted D-MAP-A versus supplied source, not historical regression or deployed state |
| ARC-FWD-02 Beta evidence gap | Requested conformance within supplied available-file scope | Same read-only source-guided method; no search beyond beta | decisions.md, Project.csproj, Scope.md | PASS | Package declaration alone does not decide usage criterion; Insufficient evidence, conformance BLOCKED, task PARTIALLY COMPLETE and Memory NOT_ASSESSED; no dependency removal/decision rewrite | Returned beta assessment; Project.csproj:1, decisions.md:2–6, Scope.md:1 | Required mapping/generated/registration/caller evidence unavailable; no usage/compliance/absence conclusion | Accepted D-MAP-B known, implementation relation unresolved |
| ARC-FWD-03 Gamma impact | Requested impact analysis of a proposal | Inspect supplied current service/caller, proposal and descriptor; no code execution | CleanArchitecture/service.py, client.py, context.md, deploy.yaml | PASS | Conditional nullable-result caller incompatibility identified; missing-name rule remains human decision. Folder name is not architecture, no ADR mandate inferred, replica count remains declaration only. Memory NONE within supplied scope | Returned impact table; service.py:1–2, client.py:1–4, context.md:1, deploy.yaml:1–2 | Impact task DONE; checks only proposed/NOT_RUN, external consumers and actual operations unknown; no code changed | Current source compared with an unimplemented proposal, not an observed regression |
| ARC-FWD-04 Delta match | Requested narrow dependency/port review | Inspect complete scoped service and test source against accepted decision | delta/service.py, decisions.md, tests/test_service.py | PASS | Match for injected storage and no concrete adapter import in complete service file; substitution seam observed, tests explicitly unrun. Task DONE, Memory NONE in checked boundary | Returned delta assessment; service.py:1–5, decisions.md:2–6, test_service.py:3–7 | No formal interface requirement invented; composition, production adapter, errors/concurrency and runtime unknown | Accepted D-PORT-D versus current scoped source; no earlier implementation snapshot |

Actual evaluator method: line-numbered text inspection with
`rg -n "^" -- <named files>` and scoped
`Get-ChildItem -LiteralPath … -Force` path/attribute inspection.
The evaluator reported no file writes, code/test execution or network/native
checks. Git revision/branch/dirty state were not inspected in these fixtures.

The evaluator's underlying checks were alpha FAIL, beta BLOCKED, gamma PASS,
delta PASS and behavioral verification NOT_RUN. Alpha/gamma/delta assessment
delivery was DONE; beta conformance remained PARTIALLY COMPLETE. Regression
timing was Unknown for all four; an accepted decision is an intended-design
comparator, not historical implementation evidence.

The author accepted the observed distinctions and read-only boundaries without
changing product content after evaluation. The reports support these specific
conclusions; they are not complete field-by-field report-template acceptance,
repeated-run reliability, all sixteen scenarios or native host behavior.
In particular, a limited report must not be promoted to an independent audit.

## Fixture preservation

ARC-SNAPSHOT-01 — PASS. Author-run inline Python compared the exact original/final
seventeen-file and nine-directory sets, SHA-256 bytes and string-preserved mtime_ns
values. All matched. No added/deleted files or changed bytes/timestamps were found.
Snapshot equality does not prove absence of all transient effects/access; execution
and access limits also rely on the evaluator's returned method/action report.

| Fixture file | Original and final SHA-256 | Original and final mtime_ns |
| --- | --- | --- |
| alpha/decisions.md | d7ceff17cd0f79cb386f4479da53d65f4dfc719014143a824801234971c2e8b3 | 1790664088902266300 |
| alpha/Project.csproj | e6db4782c6e88a2adf99bcf468cf632c848cd5199286b4b59cf7d5e5e023b5cd | 1790664088903268200 |
| alpha/Composition.cs | 57eefd79aee892ed681909e0e433143f5d4b6a06489ecab18d80560b33278aad | 1790664088903268200 |
| alpha/Pipeline.cs | 1343cf80adcc6c41a000a30ced4e8c618bbd7430b37793e75aa674ca5fa6b6bf | 1790664088904265300 |
| alpha/tests/MappingSpec.cs | 8815ac9bede27cfb265668f0287b43d7e55072604f248dce82ff4ea43e04400b | 1790664088904265300 |
| alpha/.kiyo/memory/index.md | 1e75ad96e5055b81ccc679f6e82435bb3e97673a7b228b8aeacdaea333ae6cfe | 1790664088905265900 |
| alpha/.kiyo/memory/architecture.md | 1e637128aeef027f7359c7ea2374ef07b339f436ae34bd101ccc91dc4971e58b | 1790664088906266500 |
| beta/decisions.md | 85fc7291671aacdab2e0996a05acb603154354c673c69d7c901c852d8e9af9d9 | 1790664088906266500 |
| beta/Project.csproj | e6db4782c6e88a2adf99bcf468cf632c848cd5199286b4b59cf7d5e5e023b5cd | 1790664088906266500 |
| beta/Scope.md | 5c00b4c898c018358915ebaaa8cced9e5de760eee34144d4b9b941c284b89110 | 1790664088907266300 |
| gamma/CleanArchitecture/service.py | f5c4343f9c4c10125e0131b939277c922c7641eb8e610b38a76ef9856ce32ee7 | 1790664088907266300 |
| gamma/client.py | 8e3c90b31c22f2d0f6109d6e38bd93fada67c0296637cc4a7e41a4c1c27e96b3 | 1790664088908266700 |
| gamma/deploy.yaml | 3602dc17de7b99f7a3bef5596955021eee67001743233c8fb1de57ca574bed50 | 1790664088908266700 |
| gamma/context.md | 7a9556c01bc2be949bae9dd32f1d968f3407dda950416075c22318e712670a6b | 1790664088908266700 |
| delta/decisions.md | 06421e73340fc778c973e37a16dc1ab701d2d5082876f9ce0fbac51b49c27ea6 | 1790664088909266100 |
| delta/service.py | 59f573354fc35666abce636e347b5b093e21d8e7dd3a3b1e582945edbf4c7e69 | 1790664088909266100 |
| delta/tests/test_service.py | dd75587614c68dd8c03e34e9d31f483fb86bc709a2939a0992fe1bda611049fa | 1790664088910266200 |

Directory set: alpha, alpha/.kiyo, alpha/.kiyo/memory, alpha/tests, beta, delta, delta/tests, gamma, gamma/CleanArchitecture.

## Checked source and relocation

The following SHA-256 values identify actual local source bytes inspected after
the trials. They are not signatures, release versions, authenticity guarantees
or installed/native identity assertions.

| Source path | SHA-256 |
| --- | --- |
| src/kiyo/skills/architecture/SKILL.md | 27081c665ad7f1a2ea83aeda11204e9017ac597c12b8728eabadef0bb6705ea3 |
| src/kiyo/workflows/architecture.md | 56397a9026f7f1808f4b867298a4b8fe44c98f69fafdeddf45d345b206591b13 |
| src/kiyo/templates/reports/architecture-observation.md | e53fe83199e4f24afef55aea04c9d089eda97c83bd7b7deb7300eddb4d66bb29 |
| src/kiyo/templates/reports/architecture-impact-report.md | b2515fec307c32666e7b27307d23201579821cdbdc72b00139fca29b489a345b |
| src/kiyo/templates/reports/memory-architecture-drift-report.md | 4796f9844b3d99d993655a696f010b3f6103fcb0ecd83c22110c214ac581887d |

ARC-RESOURCE-01 — PASS. Inline Python copied 88 shared Markdown files byte-for-byte
under each of seven entries' references/kiyo directories in temporary storage,
rewrote only entry-relative locators and checked contained local file resolution.
Source static validation separately checked anchors. No native distribution,
manifest/cache install, runtime generator or automatic activation was produced.

| Entry | Shared files | Entry links | All contained local links |
| --- | --- | --- | --- |
| init | 88 | 10 | 547 |
| requirement | 88 | 10 | 547 |
| implement | 88 | 14 | 551 |
| review | 88 | 11 | 548 |
| test | 88 | 11 | 548 |
| security | 88 | 13 | 550 |
| architecture | 88 | 12 | 549 |

The transformed Architecture entry hash was
1ef2e27c0aad50a79dbb1321fb70abce25fb911b631f1742da2c09120cfeadb1.
Resolution verifies the source-copy layout, not native cache lifecycle or loading.

## Remaining gaps

All sixteen [Architecture scenarios](../../../tests/behavioral/architecture/scenarios.md)
remain NOT_RUN as a full matrix. All 80 full requirement verifications remain
NOT_RUN and six native targets NOT_TESTED. No compilation/runtime/package API,
production topology, automatic migration or complete architecture acceptance
was verified. Earlier external research dates/statuses were not refreshed.

Memory Impact: NONE for developer project memory. Synthetic alpha CONFLICT and
beta NOT_ASSESSED outcomes did not change Memory/decision records. No repository
Memory store was initialized. See [Prompt 17 checks](../../build/BASELINE.md#prompt-17-checks)
for final static/build-state validation and exact change scope.

