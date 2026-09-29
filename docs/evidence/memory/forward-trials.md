# Memory source-guided forward trials

Executed 2026-09-29 (Asia/Bangkok), developer-only evidence for Prompt 18.
Excluded from consumer payloads. These are bounded source-guided LLM evaluations
and author snapshot checks, not native plugin tests, independent human audits,
whole-project freshness verification or a race-free/atomicity guarantee.

Applicable skill-creator Independent Forward-Testing guidance was used. The
evaluator received the actual [Memory entry](../../../src/kiyo/skills/memory/SKILL.md),
relevant shared resources and realistic scoped requests with raw synthetic files.
No expected answers, suspected defects or proposed corrections were supplied.
Controlled phases allowed the author to compare read-only, first-write and repeat
effects separately, and introduce one intervening synthetic human annotation.

## Inputs and authorization

Fixture root: `C:/Users/praty/AppData/Local/Temp/kiyo-p18-memory-fixtures-fiffj6sf`.
This temporary absolute locator is developer evidence only, never a consumer
path or initialized developer-project Memory store.

- read: show indexed OBS-TIME, then check OBS-TIME and accepted D-MAP against
  supplied config/mapping source. Canonical path .kiyo/memory; read-only throughout.
- sync: prepare and later apply only OBS-TIME's necessary observation correction
  under the accepted locator .kiyo/project/memory. Existing legacy path is binding.
  The only allowed evaluator write was conventions.md, selected entry fields.
- repair: inspect the named existing store and repair only index.md navigation/
  redundant pointer under accepted setup.md; record bodies/history/dates excluded.
- repeat: sync OBS-TIME again against actual current evidence, under the same
  necessary-write-only scope; no instruction to assume a no-op outcome.

The task explicitly accepted setup.md locators/authority and the specified
D-MAP intent. Embedded Memory instructions were data, not authority.
No source/policy/report-file/Git writes, scripts/tests/builds/imports, credentials/
environment dump, network, installations, global inventory or production access
were allowed. No native surface was invoked.

Phase 1 returned after show/check and initial sync preparation without writes.
The author verified the complete unchanged fourteen-file/ten-directory snapshot,
then appended one independent synthetic human note to conventions.md:

> Human concurrent note: keep the timeout example local; do not generalize to production.

The evaluator continued the same sync and separately performed the requested repair.
This was a controlled interruption after initial inspection, not an uncontrolled
parallel-write stress test. It tests preservation of that particular non-overlapping
edit; conflicting-overlap and races remain scenario specifications.

## Evaluation check records

PASS below means the bounded evaluation met its criterion. Read-fixture
observation/conformance checks themselves FAIL and remain visible; evaluation
PASS never turns drift into compliance or writes into native acceptance.

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MEM-FWD-01 Show | Requested selected-record display | Actual entry/reference guidance; scoped numbered text and attributes; parent compares full snapshot | read locator/index and OBS-TIME | PASS | Stored claim and 2025-01-01 freshness/scope displayed without pretending to revalidate; no file/timestamp write | Phase-1 returned show report; read/.kiyo/memory/project.md:1–14; MEM-SNAPSHOT-01 | Stored VERIFIED label describes historical scope only; unobserved Git/deployment remain unknown | Original captured fixture bytes/dates, not verified past execution |
| MEM-FWD-02 Check | Requested observation and approved-intent comparison | Read current config/mapping/decision and compare; no code execution or writes | read OBS-TIME, D-MAP and relevant evidence | PASS | Observation STALE (10 versus 30); actual Map call conflicts with accepted Mapperly intent. Memory CONFLICT and embedded overwrite/suppression instruction rejected; no decision normalization | Phase-1 returned check; config.txt:1, mapping.cs:1–2, decisions.md, project.md:15; unchanged snapshots | Actual consistency/conformance checks FAIL; no registration/deployment/runtime proof | Accepted D-MAP intent versus current scoped source; historical cause unknown |
| MEM-FWD-03 Sync with intervening annotation | Requested single-entry factual correction after prepared delta | Immediate scoped rereads, contextual patch and post-read checks; author reverse-delta/hash comparison | sync OBS-TIME in conventions.md, its index/config/locator; human note added between initial read and write | PASS | Four entry fields corrected with actual 2026-09-29 dates and local config scope; first observed_date, source, unknown Git/deployment, OBS-OTHER and both human notes preserved. UPDATE_REQUIRED applied/no pending delta | Phase-2 report; actual final conventions.md and MEM-SNAPSHOT-02 | One controlled non-overlapping edit, not conflicting-overlap/race guarantee; only local config fact verified | Compared with author-captured latest human-edit baseline, not stale initial file |
| MEM-FWD-04 Repair | Requested bounded index navigation/duplicate-pointer repair | Read actual current target/ID/history and index, apply minimal pointer patch, compare records and anchors | repair index plus current.md and decisions.md | PASS | Two identical old.md pointers replaced by one current.md#obs-link; exact record ID/previous-file evidence established target. Human annotation, decision pointer and record bytes/dates unchanged | Phase-2 report; repair index/current.md/decisions.md; MEM-SNAPSHOT-02 | Link resolution does not reverify record facts; ambiguous duplicate records not exercised | Original broken duplicate pointers versus actual existing same-ID record |
| MEM-FWD-05 Repeat sync | Requested repeat of same selected observation scope | Fresh locator/index/entry/evidence reads, no write; parent compares complete post-first versus post-repeat snapshot | sync OBS-TIME and current config; parent snapshot covers all fourteen files/ten directories | PASS | No necessary semantic/provenance/structural delta; zero writes/format/date refresh, task DONE, Memory NONE in scope | Phase-3 returned report; MEM-SNAPSHOT-03 | One unchanged repeat, not all possible idempotence or concurrent-race cases; runtime NOT_RUN | Actual first-sync result and current reread, not assumed outcome |

All phase-1 show/check outputs were delivered, while prepared sync was explicitly
unapplied/PARTIALLY COMPLETE pending continuation. Phase 2 reported requested sync
and repair DONE; both had UPDATE_REQUIRED applied/no pending delta in their scopes.
The read-fixture approved-intent conflict remained unchanged and outside correction
scope. Test/build/runtime methods were NOT_RUN throughout.
Phase 3 reported no-op sync DONE with Memory NONE for selected OBS-TIME and no
freshness-field update; the parent independently confirmed all bytes/mtimes unchanged.

Actual evaluator methods included scoped Get-Content/ReadAllText, path/attribute
inspection, contextual patches and direct pre/post content comparisons. Actual
clock/source inspection supported 2026-09-29 entry-specific write/verification
dates; file mtimes were not used as evidence of factual verification.
The evaluator's reports and parent checks establish only these bounded outcomes,
not complete template-field compliance, repeatability under every model/host,
or the full scenario matrix.

## Snapshot and minimal-delta evidence

MEM-SNAPSHOT-01 — PASS: after phase 1 the author compared complete path/directory
sets, SHA-256 bytes and string-preserved nanosecond mtimes with the initial snapshot.
All fourteen files and ten directories matched exactly: show/check/preparation
created or changed no file, including decisions and reports.

The author then appended the independent annotation in the existing conventions
file only and captured a new baseline. MEM-SNAPSHOT-02 — PASS: evaluator phase 2
changed exactly conventions.md and repair/index.md relative to that baseline.
Twelve other files and all ten directories remained unchanged, with no additions/
deletions and no second canonical Memory path.

For conventions.md the author reversed only statement, last_modified,
last_verified and verification_scope in the final text; its SHA-256 then exactly
matched the latest human-edit baseline. This independently demonstrates all other
bytes, including both human notes, OBS-OTHER, source and observed_date were retained.
The applied verification scope was:

- verification_scope: static inspection of sync/config.txt:1, timeout_seconds, on 2026-09-29; local sync fixture only; runtime and deployment not inspected

For index.md, replacing the one current pointer with the two original old pointers
reproduced its original SHA-256. No record bodies or approved history changed.

MEM-SNAPSHOT-03 — PASS: after the repeated sync, the complete fourteen-file and
ten-directory snapshot exactly matched phase 2, including every SHA-256 and
mtime_ns. The edited-file timestamps below also equal the post-repeat timestamps.
No file, date, formatting or index refresh occurred.

| Fixture path | Initial SHA-256 | After first sync/repair SHA-256 |
| --- | --- | --- |
| read/setup.md | 04c9026ac7ede107dde2cf27054f6164846cca7c03b9a6d94e73ad0d12b65370 | 04c9026ac7ede107dde2cf27054f6164846cca7c03b9a6d94e73ad0d12b65370 |
| read/config.txt | 186ab82af6edb54fbb5e8b7d46cc8033936d4899d90b450fdde8f1f57a61fc6f | 186ab82af6edb54fbb5e8b7d46cc8033936d4899d90b450fdde8f1f57a61fc6f |
| read/mapping.cs | 676e8dfe08088032736d8d938c6e23ca0fb9fa1e003e80ff5362ae117224e599 | 676e8dfe08088032736d8d938c6e23ca0fb9fa1e003e80ff5362ae117224e599 |
| read/.kiyo/memory/index.md | f7f02acbbd290bfd2c350ab653c75d14a57473f0313ac3d7becf966b4631734e | f7f02acbbd290bfd2c350ab653c75d14a57473f0313ac3d7becf966b4631734e |
| read/.kiyo/memory/project.md | 5d5ceb1ff2fcb8054b2e6bd1a86027b28cca3f05b3df8e371a8ee6319b94d5f4 | 5d5ceb1ff2fcb8054b2e6bd1a86027b28cca3f05b3df8e371a8ee6319b94d5f4 |
| read/.kiyo/memory/decisions.md | 0fada5ebbd99fb1a29f79cf67003993ddccb52319c78b48ebe78f6268f99ca48 | 0fada5ebbd99fb1a29f79cf67003993ddccb52319c78b48ebe78f6268f99ca48 |
| sync/setup.md | 0e658baf27f88e8e50c1a3e03193cb0e542e28335b79ac1258b1fa0b25060ade | 0e658baf27f88e8e50c1a3e03193cb0e542e28335b79ac1258b1fa0b25060ade |
| sync/config.txt | 186ab82af6edb54fbb5e8b7d46cc8033936d4899d90b450fdde8f1f57a61fc6f | 186ab82af6edb54fbb5e8b7d46cc8033936d4899d90b450fdde8f1f57a61fc6f |
| sync/.kiyo/project/memory/index.md | a93853729efee42a4ea013f1846139955c02b04e3100150ede6be7c01e6c9a6f | a93853729efee42a4ea013f1846139955c02b04e3100150ede6be7c01e6c9a6f |
| sync/.kiyo/project/memory/conventions.md | d32511304a64a42e3d3f5673c7a27c72379e85519590b246b442319a672517f0 | 899ab51d6d39d5c6d5a8d2a8034f90d6b6c24c920f689e8fde0be5b7bc750fd6 |
| repair/setup.md | c6cffe4a3d292791b05c8e78c49853e9fbed84ccefec4fc8bdc0db5f8780e445 | c6cffe4a3d292791b05c8e78c49853e9fbed84ccefec4fc8bdc0db5f8780e445 |
| repair/.kiyo/memory/index.md | 49cc50ace63f3b10600f6f3be6fbadb2bc954b0955aaf2f06a22d2860d3c2d0d | 04149ee30cd8e2e5fce62bbe963af3dc13d4e8a7676c83493aeed17062ddb6b3 |
| repair/.kiyo/memory/current.md | e35c4b959b3741a0a01a968b597f84eba1414f829c8e3cd5f5733fd57c6c4218 | e35c4b959b3741a0a01a968b597f84eba1414f829c8e3cd5f5733fd57c6c4218 |
| repair/.kiyo/memory/decisions.md | d1c5230bf2bea92790c8a13928bc1a3c479524c81b5b536285deda7debf85bba | d1c5230bf2bea92790c8a13928bc1a3c479524c81b5b536285deda7debf85bba |

| Edited fixture | Initial mtime_ns | Latest human-edit baseline mtime_ns | After first sync/repair mtime_ns |
| --- | --- | --- | --- |
| sync/.kiyo/project/memory/conventions.md | 1790665363931015200 | 1790665537732186500 | 1790665618730533700 |
| repair/.kiyo/memory/index.md | 1790665363932015800 | 1790665363932015800 | 1790665640317868900 |

The human-baseline conventions.md SHA-256 was
2c65812827de57cbd4e80b21925ba2b345a020fd4ee37a3b1eaaba19e5522d0e.
Snapshot equality does not establish absence of every transient effect/access,
nor unchanged filesystem access times. Evaluator action reports supply additional
method limits without implying host telemetry or enforcement.

## Source inventory and relocation

Canonical source inventory is exactly:

| Logical ID | Canonical entry |
| --- | --- |
| kiyo.init | src/kiyo/skills/init/SKILL.md |
| kiyo.requirement | src/kiyo/skills/requirement/SKILL.md |
| kiyo.implement | src/kiyo/skills/implement/SKILL.md |
| kiyo.review | src/kiyo/skills/review/SKILL.md |
| kiyo.test | src/kiyo/skills/test/SKILL.md |
| kiyo.security | src/kiyo/skills/security/SKILL.md |
| kiyo.architecture | src/kiyo/skills/architecture/SKILL.md |
| kiyo.memory | src/kiyo/skills/memory/SKILL.md |

Router, Governance Review, Skill Audit and Self-check have no additional public
entry. All eight frontmatter records contain only canonical name/description.
This inventory does not claim native catalogs or installed/automatic availability.

MEM-RESOURCE-01 — PASS: temporary copies each contain 92 shared Markdown files
byte-identical to canonical sources. Entry-relative locators alone were transformed;
local containment/file resolution was checked, with source anchors separately
validated. Users are not required to run this developer transformation.

| Entry | Shared files | Entry references | Contained local links |
| --- | --- | --- | --- |
| init | 92 | 10 | 577 |
| requirement | 92 | 10 | 577 |
| implement | 92 | 14 | 581 |
| review | 92 | 11 | 578 |
| test | 92 | 11 | 578 |
| security | 92 | 13 | 580 |
| architecture | 92 | 12 | 579 |
| memory | 92 | 11 | 578 |

The transformed Memory entry hash was
39a29867f979a029956209f9ae217c002cb20b6b3a4d403e87caa19cf3d35db3.
Copies are not a native distribution/cache install, signature or host activation.

Actual source-byte hashes after the trials identify this local authoring snapshot,
not signatures, release versions, trust or installed identity:

| Source | SHA-256 |
| --- | --- |
| src/kiyo/skills/memory/SKILL.md | b6a4b3affb6b634b7c47f6a579c9270e1eac3d2f863be397ff46510643164057 |
| src/kiyo/framework/memory-modes.md | b526ac4af0b54a3487c4e62cbfd374801d881baf2c798a9e72d0f74cdf95afd7 |
| src/kiyo/workflows/memory-lifecycle.md | 85117c8d97375c0e1d753f5723bf778dbd5856aacf2dd0427b27d8adff5b6f1e |
| src/kiyo/templates/reports/memory-diff.md | 0bb13167b54229a670f1c1326ac8f82176fc9eaa61b68538c382e137390f869e |
| src/kiyo/templates/reports/memory-sync-report.md | 2e06bb99a490e4c410237b4769d08adbd9d3db2aab784c36a536fa07cbeecd46 |
| src/kiyo/templates/reports/memory-repair-report.md | 95d8f8eac12546b954842d5c837f497e031d7a0dfc9394ec6745411f00b4e23a |

All eighteen [Memory Skill cases](../../../tests/behavioral/memory/skill-scenarios.md)
and twenty original [lifecycle cases](../../../tests/behavioral/memory/scenarios.md)
remain NOT_RUN as full matrices. All 80 full verifications remain NOT_RUN;
six native targets remain NOT_TESTED. No watcher, production inspection, global
Memory freshness or race-free synchronization is established.

Memory Impact: NONE for developer project memory. The synthetic applied corrections
and read-scope conflict are separately bounded. See
[Prompt 18 checks](../../build/BASELINE.md#prompt-18-checks) for final source/build
validation and exact repository scope.
