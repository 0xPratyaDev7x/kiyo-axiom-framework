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

