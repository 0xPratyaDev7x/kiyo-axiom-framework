# Kiyo Compass — Baseline and Check Evidence

## Initial repository observation

Observed on 2026-09-28 (session timezone Asia/Bangkok), before any repository
writes for Prompt 01. The user selected this repository as the target.

| Item | Observed fact / evidence |
| --- | --- |
| Repository root | C:/Users/pratya_s/source/@0xPratya7x/kiyo-codejadee-framework |
| Git repository | Yes; git rev-parse --show-toplevel returned the root above |
| Branch | main |
| Tracking label | git status --short --branch returned main...origin/main; no fetch performed and remote freshness is unknown |
| HEAD | fb389c33f95026c43fd880334264a0946fac59e0 |
| HEAD subject | Initial commit |
| Working tree | Clean: git status --porcelain=v1 --untracked-files=all returned no entries |
| Staged / unstaged differences | git diff --cached --stat and git diff --stat returned no entries |
| Tracked files | LICENSE only, mode 100644 |
| LICENSE index blob | d2e60c5b160ed4f9ca096215e72efee5769936b1 (observed with git ls-files --stage) |
| Existing license text | MIT License; Copyright (c) 2026 Pratya S. |
| Initial non-Git file inventory | LICENSE only, from rg --files --hidden -g '!.git' -g '!node_modules' -g '!vendor' and root directory inspection |
| Existing application/framework | No implementation files observed; no evidence of Virtual Office or an unrelated application |
| Existing build records | None |
| Repository instructions | No AGENTS.md found in the repository inventory or checked ancestors up to the drive root |
| Existing package/version/publisher metadata | None observed; release version and publisher UNKNOWN |
| User edits | None observed at this baseline; recheck before every subsequent prompt |
| External research | NOT_RUN; deferred to Prompt 02 |

The LICENSE text is an observed fact. Do not infer a final publication license,
publisher identity or approval from its copyright line. Preserve it while
DEC-002 remains open. No secrets, remote contents or account credentials were
read for this baseline. Git object identifiers above are actual command output,
not generated placeholders.

## Target baseline

No native Kiyo package exists yet. Tool availability, installed versions and
accounts were not assessed in Prompt 01. Do not treat “not inspected” as “missing”.

| Target | Capability / native schema | Observed target version | Tool/account availability | Kiyo live test state | Evidence / next action |
| --- | --- | --- | --- | --- | --- |
| Claude Code CLI | UNKNOWN | UNKNOWN | UNKNOWN | NOT_TESTED | No Kiyo live evidence; research in 02, overlay in 20, live testing in 26 |
| Claude Code VS Code Extension | UNKNOWN | UNKNOWN | UNKNOWN | NOT_TESTED | No Kiyo live evidence; research in 02, overlay in 20, live testing in 26 |
| Codex CLI | UNKNOWN | UNKNOWN | UNKNOWN | NOT_TESTED | No Kiyo live evidence; research in 02, overlay in 21, live testing in 26 |
| Codex IDE Extension | UNKNOWN | UNKNOWN | UNKNOWN | NOT_TESTED | No Kiyo live evidence; research in 02, overlay in 21, live testing in 26 |
| GitHub Copilot CLI | UNKNOWN | UNKNOWN | UNKNOWN | NOT_TESTED | No Kiyo live evidence; research in 02, overlay in 22, live testing in 26 |
| GitHub Copilot in VS Code | UNKNOWN | UNKNOWN | UNKNOWN | NOT_TESTED | No Kiyo live evidence; research in 02, overlay in 22, live testing in 26 |

## Prompt 01 checks

Checks below are documentation/baseline checks only. They do not validate
future skills, standards mappings, packaging, behavioral outcomes or native hosts.

Executed on 2026-09-28 using read-only inline PowerShell validation and Git/rg
commands. No test scripts or dependencies were added. Results below summarize
the actual command output and a scoped manual self-review, not an independent
audit. The validator failed on mismatches rather than treating missing data as
success. Documentation status updates were followed by final consistency checks.

| Check ID | Method / scope | Actual result | Evidence / limitation |
| --- | --- | --- | --- |
| P01-C01 | git rev-parse --show-toplevel; git branch --show-current; git rev-parse HEAD, compared with the initial baseline | PASS | Root, main branch and fb389c33f95026c43fd880334264a0946fac59e0 unchanged; no remote freshness claim |
| P01-C02 | Compare docs/build file names against the eight required names; decode every file with strict UTF-8 | PASS | Exactly 8 nonempty Markdown files; valid UTF-8, no replacement characters |
| P01-C03 | Parse registry headings, compare with REQ-001 through REQ-080, count six fields per entry and compare source requirement lines with the user's original attachment | PASS | 80 unique contiguous IDs; all 80 source requirements preserved verbatim; 480 populated expansion fields; 80 matching AC identifiers |
| P01-C04 | Parse trace table, validate column order, IDs, AC/case mappings and implementation/verification status values | PASS | 80 unique rows; all 10 required columns; 79 NOT_IMPLEMENTED, 1 PARTIALLY_IMPLEMENTED, 80 full verifications NOT_RUN; all TC-REQ identifiers explicitly PLANNED |
| P01-C05 | Resolve every local Markdown link and referenced heading anchor in the eight files | PASS | 122 links resolved in the initial check; subsequent status edits add no links and final link check passed |
| P01-C06 | Manual self-review against Prompt 01: contract rules, pillars/skills, requirement-specific acceptance/verification, six-target separation, owner decisions and handoff completeness | PASS | All 19 all-prompt rules retained; four pillars/eight public skills/four shared procedures retained; all 30 roadmap steps present; criteria describe observable outputs/actions and checks; handoff contains read order, current state, gaps and next action without needing prior chat |
| P01-C07 | git ls-files; git hash-object -- LICENSE; git diff --exit-code -- LICENSE; git diff --cached --exit-code; git status --porcelain=v1 --untracked-files=all; rg non-Git inventory; git diff --check and explicit new-file trailing-whitespace scan | PASS | Existing LICENSE blob remains d2e60c5b160ed4f9ca096215e72efee5769936b1; no staged/tracked changes; exactly 8 new docs/build Markdown files; no other non-Git files added; whitespace checks clean |

For reruns, use the eight file names in HANDOFF, the exact ID range and field
labels in REQUIREMENTS, the ten column names in TRACEABILITY, and the Git
baseline above as validation inputs. The original attachment comparison was
performed in this session; future sessions can use the preserved Source
requirement lines without relying on the attachment path. Recheck the baseline
first and account for subsequent authorized work rather than treating these
Prompt 01 counts as permanent repository constraints.

Product static validation: NOT_RUN (no product payload or test suite yet).
Behavioral evaluation: NOT_RUN (no implemented skills/procedures yet).
Full requirement acceptance: NOT_RUN (the registry is a specification).
Live host tests: NOT_TESTED for each of the six rows above. No install, account,
version, signing, standards-alignment or compatibility success is claimed.

## Preservation and memory impact

The intended change set is exactly eight new Markdown files under docs/build.
No existing file needs modification, and no runtime or product skill is created.
No dependencies, package manifests, install scripts, commits, tags or publication
are required by Prompt 01.

Memory Impact: build continuity changes are recorded in docs/build. No product
memory exists in the observed baseline; creating .kiyo/memory is outside this
prompt's scope. No memory initialization or sync is performed.

## Prompt 02 repository observation

Observed 2026-09-28 in Asia/Bangkok. Root:
C:/Users/praty/source/@0xPratya7x/kiyo-codejadee-framework/kiyo-codejadee-framework.
Branch main; HEAD aa843a5c690d232d110c744eaecf30997c233908
(Add TRACEABILITY documentation for Kiyo Compass requirements and implementation statuses).
Initial status, unstaged diff and staged diff had no entries. Tracked inventory:
LICENSE plus eight docs/build files. No repository/ancestor AGENTS.md found.
The old Prompt 01 root/HEAD remains historical evidence above, not the current
checkout.

Initial Git calls failed on dubious ownership; retries used a per-command
safe.directory for this exact root, with no persistent config change. Git warned
that sandbox access to the global ignore file was denied. An attempted NUL
exclude-file override failed; setting core.excludesFile to an empty value for
the command succeeded. These failed attempts are not counted as passed checks.

No Kiyo host/account/version availability inspection, plugin installation,
manifest validation, behavioral evaluation or live-host test occurred.
The initial six UNKNOWN capability entries above are the **historical Prompt 01
baseline**. Current documentary capability states are in the
[Prompt 02 matrix](../compatibility/platform-capabilities.md#target-summary).

## Prompt 02 checks

Documentation/research checks only, executed 2026-09-28. These do not verify
product behavior or satisfy full requirement acceptance.

| Check ID | Method / scope | Actual result | Evidence / limitation |
| --- | --- | --- | --- |
| P02-C01 | Repository root, branch, HEAD, index and initial user edits; instruction inventory | PASS | Actual Git outputs above; initial tree/index clean. Scoped override only; no fetch, remote freshness UNKNOWN. |
| P02-C02 | Inline Python: five required files, strict UTF-8, registered source-ID references and dates/limitations | PASS | Five nonempty research files; 48 unique source IDs; references resolve; no replacement characters, NUL or conflict markers. Content/source review is C04, not implied by string checks. |
| P02-C03 | Inline Python: parse target sections and numbered capability rows; review live-state boundaries | PASS | Six summary rows, six target sections, exactly 11 dimensions each (66); NOT_TESTED live states; all six evidence/freshness terms defined. No native behavior exercised. |
| P02-C04 | Manual self-review of retrieved official pages against claims, redirect register, standards editions/status and task questions | PASS | Ten starting URLs opened; redirects/retrieval failures recorded; 48 official source entries. Six targets, static packaging, discovery/core/bootstrap, invocation, cache resources, distribution and owner gates addressed. All named standards covered; ISO public metadata only; AST draft/proposal caveat retained. Self-review, not independent audit or live proof. |
| P02-C05 | Inline Python: resolve local Markdown destinations/heading anchors; registry and trace table coverage/status | PASS | 207 local links/anchors resolved at initial closing check; 80 unique contiguous IDs in each registry/table; 10 trace columns; 73 NOT_IMPLEMENTED, 7 PARTIALLY_IMPLEMENTED; all 80 full verifications NOT_RUN; planned test IDs remain labeled. |
| P02-C06 | Inline Python and manual handoff review: build-state consistency and stop boundary | PASS | Prompt 02 DONE, Prompt 03 NOT_STARTED, safe continuation scoped to requested architecture; four unresolved decision rows, nine issue rows; trace check link present; no .kiyo memory directory. Handoff supplies read order, current root/HEAD, findings and exact next action without prior chat. |
| P02-C07 | Inline Python plus Git: 11-file allowlist, LICENSE hash, unchanged protected files/index/HEAD and whitespace | PASS | Five new and six modified Markdown files only; LICENSE blob d2e60c5b160ed4f9ca096215e72efee5769936b1; REQUIREMENTS/BUILD-CONTRACT unchanged; index empty; main/HEAD unchanged; diff and explicit new-file whitespace checks clean. First run caught a new blank line at BASELINE EOF; corrected and rerun passed. |

Research retrieval: see [SOURCES](../research/SOURCES.md) for official URLs,
reported final destinations, checked date, limitations and failed/recovered URLs.
No HTTP chain/hash or live result fabricated.
Checks were inline developer-only validation; no script or dependency was added.
The final status edits were followed by the same link/coverage/preservation checks
and the build-state consistency check. These scoped observations are VERIFIED
as documentation checks only; capability findings remain DOCUMENTED_ONLY or the
explicitly stated UNKNOWN/UNSUPPORTED state.
Product static validation: NOT_RUN. Behavioral evaluation: NOT_RUN.
Live Kiyo tests: NOT_TESTED for each of the six targets.
Memory Impact: build-state records only; no product memory touched.

## Prompt 03 repository observation

Initial inspection began 2026-09-28; architecture records and closure are dated
2026-09-29 (Asia/Bangkok, after local midnight). Repository root remains
C:/Users/praty/source/@0xPratya7x/kiyo-codejadee-framework/kiyo-codejadee-framework.
Branch main; HEAD 64b2b8b05e79e8fe23aee78c7fa7ed09b4ee68fd
(Add platform capabilities documentation and research sources).
Initial working tree/index and staged/unstaged diff statistics had no entries.
Tracked inventory: LICENSE, eight build records and five research/compatibility
documents. Prompt 02 had been committed before this work; older HEAD values and
uncommitted snapshots above are historical evidence.

No applicable AGENTS.md found in the repository or checked ancestors. No product
memory, version file, native manifest or Git tag was found by the scoped inventory.
Git used the existing per-command exact-root safe.directory override; an initial
unreadable global-ignore warning was avoided by the per-command empty
core.excludesFile setting. No persistent configuration was changed.

Read the Build Contract, Progress, Handoff, Open Issues, Decisions, relevant
requirements/traceability and all five Prompt 02 research outputs. Architecture
uses the dated 2026-09-28 research; no new external schema check, host/tool/account
inventory, plugin installation or source generation occurred in Prompt 03.

## Prompt 03 checks

Executed 2026-09-29 with inline Python/PowerShell, read-only Git commands and
manual self-review. These are documentation/design checks, not product tests or
an independent audit. No script or development dependency was added.

| Check ID | Method / scope | Actual result | Evidence / limitation |
| --- | --- | --- | --- |
| P03-C01 | Repository root/branch/HEAD, initial status/index/diffs, instruction and version inventory | PASS | Root and main/64b2b8b05e79e8fe23aee78c7fa7ed09b4ee68fd recorded above; initial tree/index clean; no applicable AGENTS.md or established product version/tag found. No remote fetch or host/account inventory. |
| P03-C02 | Inline Python: six required new documents, nonempty strict UTF-8, conflict/replacement/NUL checks, new-file whitespace and absolute developer-path scan | PASS | Six new nonempty files; 19 Markdown files decoded and checked. Only src/kiyo/README.md exists in product source; no empty skill/native/runtime scaffold. |
| P03-C03 | Inline Python: resolve local Markdown destinations and heading anchors outside illustrative fenced blocks | PASS | 334 local links/anchors resolved. Planned product paths are explicitly marked as examples, not falsely treated as existing payload links. Installed-resource resolution is NOT_TESTED. |
| P03-C04 | Manual self-review against Prompt 03 and dated research; walk the proposed Review skill-to-rule-to-template-to-package mapping | PASS | Five ownership boundaries, eight skills/shared procedures, stable controls, native metadata separation, progressive loading/budgets, contained generated resources, neutral templates, legacy memory preservation and lifecycle/version/owner gates documented. No consumer runtime dependency. This is a design review, not executed agent/package behavior. |
| P03-C05 | Inline Python: parse registry/table IDs, ten columns, planned test IDs, implementation states, full acceptance and six live rows | PASS | 80 unique registry/table IDs; 23 rows receive design evidence; 73 NOT_IMPLEMENTED and 7 PARTIALLY_IMPLEMENTED unchanged; all 80 full verifications NOT_RUN; all six live targets NOT_TESTED. Exactly eight planned public skill paths in layout. |
| P03-C06 | Inline Python plus manual handoff review: current status, next step, ADR/read order and unresolved decisions/issues | PASS | Prompt 03 DONE; Prompt 04 NOT_STARTED; safe continuation only when Core is requested; four pending owner decisions and nine issue rows retained. Handoff records chosen design and exact next action. No .kiyo memory created. |
| P03-C07 | Inline Python plus Git: exact change allowlist; protected content/index/HEAD; LICENSE hash; diff/new-file whitespace | PASS | Six new and six modified Markdown files only. LICENSE blob remains d2e60c5b160ed4f9ca096215e72efee5769936b1; REQUIREMENTS, BUILD-CONTRACT and all Prompt 02 research/compatibility files unchanged. Index empty, main/HEAD unchanged, diff checks clean. |

Validation development encountered a JavaScript quoting error before command
execution, a PowerShell brace-list parse error, and overly strict validator
assumptions about CRLF headings and the existing extra documentation check IDs
in TC-REQ-080's cell. Corrected command syntax, normalized newlines for parsing
and retained the existing planned-ID plus executed-check structure; the resulting
validator passed. Failed attempts were not counted as passing checks and did not
justify changing the preserved requirements. Status/traceability edits were
followed by the same validation plus explicit closure assertions; all passed.

For reproducibility, validate the six added paths linked in PROGRESS, the six
modified build files (PROGRESS, HANDOFF, TRACEABILITY, OPEN-ISSUES, DECISIONS,
BASELINE), 80 contiguous IDs and unchanged status counts above. Resolve relative
links against their containing files and Markdown headings, excluding code-block
examples. Use read-only git diff --check, diff --name-only, diff --cached,
ls-files --others --exclude-standard and hash-object -- LICENSE with the scoped
overrides described above. No package build command exists at this stage.

Product static validation: NOT_RUN. Behavioral evaluation: NOT_RUN.
Live native tests: NOT_TESTED for each of the six targets. No schema, install,
cache relocation, automatic activation, update or uninstall result is inferred.
The change set is five architecture documents, one source authoring README and
six build-state updates. No package, runtime, empty skill, manifest, generator,
commit, tag, push or publication was created. Memory Impact: build continuity
and ADR only; project memory is not initialized or modified.

## Prompt 04 repository observation

Observed 2026-09-29 (Asia/Bangkok). Root:
C:/Users/praty/source/@0xPratya7x/kiyo-codejadee-framework/kiyo-codejadee-framework.
Branch main; HEAD 73972148ba6705c915a01195972acac4fc09482a
(feat: Add architecture documentation for Kiyo Compass).
Initial status, staged and unstaged diff statistics were empty. Prompt 03 was
committed before this work. Inventory contained LICENSE and 19 Markdown files:
eight build, five research/compatibility, five architecture and source README.
No applicable AGENTS.md found in repository or inspected ancestors; no .kiyo
memory present. Scoped safe.directory and empty core.excludesFile were used
without persistent configuration changes.

Read the Build Contract, Progress, Handoff, issues/decisions, relevant requirements,
traceability and architecture, plus the dated activation research. Prompt 04
introduces no new host-specific API/schema claim and performs no external source
revalidation or CLI/IDE/account availability inspection.

## Prompt 04 checks

Executed 2026-09-29 with inline Python/PowerShell, read-only Git commands and
manual self-review. These validate authored Core text and build records, not
agent compliance. No persistent test script, generator or dependency was added.

| Check ID | Method / scope | Actual result | Evidence / limitation |
| --- | --- | --- | --- |
| P04-C01 | Root/branch/HEAD, initial worktree/index/diffs, scoped file and instruction inventory | PASS | Initial tree/index clean at main/73972148ba6705c915a01195972acac4fc09482a; 19 Markdown files plus LICENSE before work; no applicable AGENTS.md found. No remote freshness or host/account inspection claimed. |
| P04-C02 | Inline Python: strict UTF-8, nonempty additions, conflict/NUL/replacement checks, source inventory, control index and knowledge/status labels | PASS | 27 Markdown files inspected; seven Core files; 16 unique control IDs; all used IDs registered; ten numbered principles; five knowledge classes and five check states present. ACTIVE is authored text, not tested enforcement. |
| P04-C03 | Inline Python: resolve local links/anchors, enforce Core resource closure, prohibit absolute developer paths and reparse/symlink Core files | PASS | 458 local links/anchors resolve; all 29 Core links stay within the seven Core files. No operational dependency on developer docs/README, scripts or outside files. This checks source references, not installed cache relocation or a native package. |
| P04-C04 | Physical-line/whitespace-word counts and manual relevance/loading review | PASS | KIYO.md 22 lines / 110 words; bootstrap.md 59 / 469; combined 81 / 579, within 120 / 600. Mandatory baseline is bounded; remaining references conditional. Future SKILL.md ceiling 250 lines / 1,200 words is defined but measurement NOT_RUN because no SKILL.md exists. These are Kiyo criteria, not vendor limits. |
| P04-C05 | Manual self-review of all ten principles, trust/authority boundaries and requested expected cases; inline example-ID check | PASS | EX-01 README credential request denied; EX-02 memory self-elevation rejected; EX-03 review findings without repair; EX-04 tiny typo with focused scope/check; EX-05 automatic-loading limitation. EX-06 approved-intent conflict and EX-07 local/identity/unrun-check uncertainty supplement them. All seven are explicitly synthetic expected behavior, not executed tests or independent audit evidence. |
| P04-C06 | Inline Python: registry/traceability, state/roadmap/handoff consistency, issue/decision identity; manual resume review | PASS | 80 contiguous requirement/table IDs, ten trace columns, planned TC IDs preserved; 32 Core instruction rows plus REQ-080 updated; 38 PARTIALLY_IMPLEMENTED, 42 NOT_IMPLEMENTED, all 80 full verifications NOT_RUN. Four pending decisions/nine issues retained. Prompt 04 DONE, Prompt 05 NOT_STARTED; safe continuation scoped to requested Memory work. |
| P04-C07 | Inline Python plus Git: exact diff/untracked allowlists, index/HEAD, protected files/LICENSE and whitespace | PASS | Eight new and ten modified Markdown files only. LICENSE blob remains d2e60c5b160ed4f9ca096215e72efee5769936b1; REQUIREMENTS, BUILD-CONTRACT, Prompt 02 research/compatibility, packaging contract and ADR-001 unchanged; index empty and main/HEAD unchanged. git diff --check and new-file whitespace scan passed. No product memory or runtime paths created. |

The initial size measurement found 659 combined bootstrap words; the entry was
shortened to 579 without removing the ten principles or granting an exception.
The full validator passed, then passed again after status/trace updates with
explicit Prompt 04 DONE / Prompt 05 NOT_STARTED closure assertions. Git displayed
LF-to-CRLF normalization notices for edited existing Markdown; diff checks still
passed and no global configuration was changed.

For reproducibility, validate the seven product paths linked in PROGRESS plus
ADR-002 as the new-file set. The modified set is six build records (PROGRESS,
HANDOFF, TRACEABILITY, OPEN-ISSUES, DECISIONS, BASELINE), source README and three
architecture contracts (layout, loading, naming). Resolve local Markdown links
and anchors outside fenced examples, require every Core target to remain inside
the seven-file Core set, compare all KIYO control references with the 16 index
rows, count physical lines and whitespace words, and parse the 80-row trace table.
Read-only Git checks used diff --check, diff --name-only, diff --cached,
ls-files --others --exclude-standard and hash-object -- LICENSE with the scoped
overrides above. Expected prose responses are never executed by this validator.

Static Core content validation: PASS within the scopes above. Native package
validation: NOT_RUN (no package). Behavioral evaluation: NOT_RUN.
Live native tests: NOT_TESTED for each of the six targets; no activation result
is inferred from this editing session. Seven product Markdown files and one ADR
are new; ten existing Markdown files change. No public skill, manifest, package,
hook, runtime, install, commit, tag, push or publication was created/performed.
Memory Impact: build continuity/ADR only; no project memory created or changed.
