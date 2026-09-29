# Implement bounded forward-trial evidence

Checked 2026-09-29 (Asia/Bangkok), Prompt 13. These are **executed source-guided
developer trials**, separate from the complete
[scenario specifications](../../../tests/behavioral/implement/scenarios.md),
native installation/activation, production state or full requirement acceptance.

## Source, fixture and authority

Baseline repository: main, HEAD 3853a624776fda0a34b9c8d7cc1a44754d2aba10.
The [Implement entry](../../../src/kiyo/skills/implement/SKILL.md), short plan and
shared-flow integration were uncommitted authored changes. Under the applicable
skill-creator forward-testing guidance, an independent agent received the actual
entry, relevant resources and three realistic requests, without expected results
or an evaluator-supplied fix. It performed the authorized work; the author reviewed
the actual report, resulting files and captured snapshots.

The temporary task root kiyo-p13-l3llpn_f contained three synthetic fixtures,
ten files total, outside the Kiyo repository:

- tiny/: ui_text.py with a misspelled welcome constant, accepted AGENTS.md and
  a human-notes file. The request authorized only the exact text fix and relevant
  inspected local checks.
- bug/: prices.py, an existing standard-library unittest file, accepted AGENTS.md
  and human notes. The request authorized only prices.py/test_prices.py changes
  to return zero for empty input while retaining non-empty behavior and adding
  necessary regression coverage.
- review/: the same defective function, accepted AGENTS.md and human notes.
  The actual request was review/analyze only, with no edits or application tests,
  despite selecting the Implement entry.

Fixture policy permitted only bounded requested edits and inspected local
standard-library checks; no network, installation, database, credentials, Git
initialization/commit or global settings. It established no Memory store and
prohibited automatic initialization. All input/data was synthetic.

The forward agent observed Python 3.11.9 using python -B -S --version. Its Git
root queries for the three fixtures returned “not a git repository”; branch/HEAD/
staged state remained unavailable, not guessed. Those results establish only the
fixture context, not any native coding-host version/account or production state.

## Executed checks

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IMPL-FWD-01 Tiny authorized change | Required bounded Tiny trial | Agent follows entry, inspects source, changes exact constant and runs local assertion; author compares final content/snapshots | Three tiny fixture files, with only ui_text.py writable | PASS | Welcome text corrected with one scoped edit; actual runtime assertion exit 0; policy/human note preserved; no new test framework/plan file or repeated approval | Actual methods and artifact identities below; forward-agent command results and author snapshot output in Prompt 13 conversation | One synthetic constant change, not UI rendering or general feature behavior | Compared with captured misspelled source and unchanged non-target files |
| IMPL-FWD-02 Reproduced defect and regression check | Required bounded bug-fix trial | Inspected existing unittest/source; baseline suite, added regression, observed failure, minimal fix and final suite; author inspects actual changed files | Four bug fixture files; prices.py/test_prices.py allowed edits | PASS | Existing one-test suite passed; new empty-input regression failed with None != 0 before the source fix; final two-test suite passed, exit 0. No non-empty logic/test removal or unrelated edits | Command/result table and hashes below; actual agent output and author comparison | Two local function cases only; no native/app integration/database or persistent-repair-bound test. Runtime observations come from the forward agent, not an independent author rerun | Existing defect reproduced; the new test failure is not mislabeled an introduced implementation regression |
| IMPL-FWD-03 Read-only mismatch | Required intent-boundary trial | Agent inspects source/lines and reports selected-entry mismatch; author compares all fixture snapshots | Three review fixture files; no mutation or application execution allowed | PASS | Explained that empty input returns None before sum; reported mismatch and findings without edits; application tests NOT_RUN as prohibited | Actual report and author path/byte/mtime comparison; methods below | Static code explanation only, not execution of review fixture; no complete access trace | All three file paths/bytes/exact mtime_ns unchanged from the initial snapshot |
| IMPL-RESOURCE-01 Shared-resource relocation | Required source portability check | One-off Python copies, byte comparisons, entry-link transforms and local-reference resolution | Init/Requirement/Implement temporary copies, each with 74 shared Markdown resources | PASS | Init/Requirement each resolve ten entry links and 400 contained links; Implement resolves fourteen entry links and 404 contained links; shared files byte-identical to current source | Relocation identities below; actual checker stdout; [packaging contract](../../architecture/packaging-contract.md) | Not a native distribution/cache installation or consumer tool; successful links do not prove host loading | Three source entries checked against the current shared snapshot; no existing native baseline |

## Actual execution and attribution

The agent read applicable shared instructions and fixture source/test text before
execution. It used Get-Content, Get-ChildItem, scoped rg/file/line inspection and
read-only Git root queries. Mutating scripts reread/asserted expected bytes before
the three authorized edits, preserving other content. No dependency/tool installation
was needed.

| Fixture / phase | Actual command/method | Observed result |
| --- | --- | --- |
| tiny / after edit | python -B -S -c "import ui_text; assert ui_text.WELCOME == 'Welcome back'; print('PASS: WELCOME is Welcome back')" in tiny | PASS, exit 0 |
| bug / existing baseline | python -B -S -m unittest -v test_prices.py in bug | PASS, one existing non-empty test |
| bug / regression before fix | Same unittest command after adding test_empty_total, before changing source | FAIL, empty-input assertion observed None != 0 |
| bug / after source fix | Same unittest command against final source/test files | PASS, two tests, exit 0 |
| review / inspection | rg -n '.' against review/prices.py | Inspected lines 1–4; empty-input return identified; application execution NOT_RUN |

The forward report counted one successful correction/recheck after the reproduced
defect and zero unsuccessful repair cycles. This trial does **not** exercise
post-change regression attribution, exhaustion of two unsuccessful cycles or a third
attempt gate. Those remain separately specified, unexecuted cases.
The baseline one-test PASS did not cover the empty-input defect; it was never
promoted to evidence that the function was correct before the new check.

The agent reported G2/LOW for bounded A/B edits and G1/LOW for C inspection, based
on local synthetic targets, explicit authority, no external/sensitive effects and
small reversible changes. These are scoped Kiyo assessments, not native permissions.
Memory Impact was NONE within all three fixtures: no established Memory or necessary
durable delta; no store, record or report was created.

## Author preservation check and read-scope limitation

The author independently compared all ten fixture paths, SHA-256 hashes and
string-preserved exact mtime_ns after the trial. Exactly these three files changed;
the remaining seven retained paths, bytes and modification timestamps. No files or
directories were added/deleted within tiny/, bug/ or review/. The author also read
the actual final source and regression test; no independent runtime rerun is claimed.

| Changed fixture-relative path | Actual final SHA-256 |
| --- | --- |
| bug/prices.py | aff710648dae1a7ed920226c499def6e58570cdaeb96fdee0660e4de513eb137 |
| bug/test_prices.py | 3e5404169de4e14a883d7c06e05ed7ad7123304d3b9536ce4f20c45b7f0e6280 |
| tiny/ui_text.py | 637c48ce3e92254b4521a50870b21c9ddc56b442f4bd6f7934ae8cd91874c4f7 |

The author separately created relocated/ under the temporary task root for the
resource-copy check while the forward trial was running. One early agent recursive
read/hash command therefore included that extra resource tree and its output was
truncated. It made no writes. The agent disclosed the issue and narrowed later
inventory/baseline/final comparisons explicitly to tiny/, bug/ and review/.
The authoritative author baseline was captured before the trial and comparison
was limited to those same three directories. Do not treat that broad/truncated
read as a complete access inventory or claim minimum possible context loading.

Snapshots prove the compared final state, not absence of every transient access/
write; atime and a complete independent read-access trace were not assessed.
The source trial is independent of authoring, but its report plus author review
is not an independent security audit or proof of universal agent compliance.

## Authored input and temporary-copy identity

Actual source SHA-256 values captured after the trials; these inputs were unchanged
during the evaluation. Hashes identify bytes, not signatures or proof of safety.

| Source-relative path | SHA-256 |
| --- | --- |
| src/kiyo/skills/implement/SKILL.md | 56e16b34b38d9407f594f4a40f74e581b0559fdc42710ed6008ba428affb5db6 |
| src/kiyo/workflows/implement-flow.md | 6f53d28b5b555040329df72b12b1841562d368998881cca4b4d4f7e683a4c69f |
| src/kiyo/templates/short-plan.md | 3e619827b7f2e59098581e86cc542c5df6a5a124a606cbe61c3c660738fe8d59 |
| src/kiyo/workflows/repair-and-handoff.md | ecbd73518716f69da5ec6af1cee6c5ceb3e41f183760f91d18f123f793a67b4c |

Temporary transformed entry SHA-256:

- Init: a79c2e805514836c9548183b3d83c9808eb51f92ee39ccc11e5ec31a2f5ec483
- Requirement: ed150a31bdc1dc1936260d663e985e856ec5bc30ae5456390c274cb0fd410f71
- Implement: b0313c5ed4151276197f3506c0704b3ab7ee5e68255100522dddac1b5d7597e1

Only entry link destinations changed from ../../ to ./references/kiyo/; shared
copies retained bytes. No fixture, script or mutable state is shipped as product
runtime. Temporary outputs are validation artifacts, not a durable audit log.

## Remaining scope

These trials sample IMP-01/02/04/11 intent and non-Git preservation of unrelated
human content; they do not execute the full IMP-01–16 matrix. Dirty Git index/
worktree preservation, auth/schema approvals, migration effects, missing environment,
approved Memory conflicts/sync, refactors, scope expansion and bounded persistent
failure need separately scoped evaluation. Full specification rows remain NOT_RUN.

All six native targets remain NOT_TESTED. No live host install/discovery/activation,
external API research, production DB, migration, deployment, commit/push/PR or
package installation was performed. See [Prompt 13 closure checks](../../build/BASELINE.md#prompt-13-checks)
for final static/build evidence. Passing these fixtures is not full requirement
acceptance or a claim that every application test passes.
