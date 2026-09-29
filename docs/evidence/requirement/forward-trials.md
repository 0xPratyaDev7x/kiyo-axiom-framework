# Requirement bounded forward-trial evidence

Checked 2026-09-29 (Asia/Bangkok) during Prompt 12. These are **executed,
source-guided developer trials**, distinct from the full
[scenario matrix](../../../tests/behavioral/requirement/scenarios.md), native
installation, automatic skill selection or application behavior.

## Source and authorized scope

Repository baseline: main, HEAD 3c85e3633d1af2d3b5e6f0bf2da35673fda76d0b.
The [Requirement entry](../../../src/kiyo/skills/requirement/SKILL.md), procedure,
readiness/template and integration edits were uncommitted authored content.
Following the applicable skill-creator forward-testing guidance, an independent
agent received the entry, three realistic chat-only requests and minimal synthetic
fixtures. It was not given expected outputs or proposed fixes. The author then
reviewed the actual responses and independently compared file snapshots.

Fixtures lived in temporary task directory kiyo-p12-unmum3d5, outside the repository:

- export/: five files, including accepted policy, route configuration and a
  legacy Memory observation. Request: draft an Orders Excel-export requirement.
- complete/: four files, including the full UI-42 request, current button label
  and accepted copy-change policy. Request: complete that requirement in chat.
- admin/: three files, including accepted deactivation policy and authorization
  configuration. Request: draft “Deactivate เฉพาะ admin” from current evidence.

All were synthetic text, with no real secret, user data or external target.
The trial agent was limited to read-only file/metadata operations; no repository/
fixture writes, application execution, native host operations or network access.
It used Get-ChildItem, Get-Content, scoped rg --files and line-number display.
It did not inspect Git in the fixtures and made no branch/revision/dirty-state claim.
Shared source resources were read as required by the skill; they were not installed
or discovered through a native host.

## Executed checks

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-FWD-01 Incomplete export and stale Memory | Required bounded export draft trial | Independent agent follows entry using read-only files; author reviews delivered draft and Python snapshot comparison | Five export fixture files; actual draft/questions and Memory note | PASS | Fourteen output fields addressed; existing OrdersView permission distinguished from undecided export entitlement/fields. DECISION_REQUIRED readiness, DONE for the requested draft. Old /legacy/orders observation compared with /orders config; UPDATE_REQUIRED pending, no Memory write. Alternatives/tradeoffs and material questions given without approved HTTP/retention inventions | Observed output summary and snapshot table below; actual agent response and author comparison in Prompt 12 conversation | One synthetic partial draft, not proof of every export rule or complete injection defense. Current route config is not production evidence | Compared with initial fixture snapshot and legacy observation, not a deployed baseline |
| REQ-FWD-02 Complete request without repeat questions | Required bounded complete-input trial | Independent source-guided response; author compares supplied request/criteria with output and exact snapshot | Four complete fixture files and UI-42 response | PASS | Reused UI-42 and AC-42-1/2; preserved exact Send-to-Submit change and exclusions; READY_FOR_IMPLEMENTATION, task DONE, no redundant questions or implementation; proposed checks NOT_RUN | Output summary, snapshot table and actual response/comparison in Prompt 12 conversation | Text fixture represents UI behavior; no rendered UI, application test or implementation acceptance was performed | Requirement compared with supplied request/policy and current Send label; no code before/after result exists |
| REQ-FWD-03 Admin policy ambiguity | Required bounded permission-definition trial | Independent source-guided inspection of accepted policy/config; author reviews actual draft/clarification and snapshot | Three admin fixture files and response | PASS | Cited actual AccountsDeactivate/OperationsOwner; did not invent AdminOnly or equate OrganizationAdmin with that entitlement. Clarified actor/target and policy-change choice with tradeoffs; DECISION_REQUIRED readiness, DONE for draft, no permission/config change | Output summary, snapshot table and actual agent/author outputs in Prompt 12 conversation | Policy/config agreement does not prove runtime enforcement; user meaning remains unresolved, not an approved change | Compared accepted fixture policy with current fixture config; no real organization/user policy assessed |
| REQ-RESOURCE-01 Contained source copies | Required resource portability check for two authored entries | One-off Python copy, link transform, shared-byte comparison and relative-reference resolution | Temporary Init and Requirement entries; each with 73 shared Markdown resources | PASS | Ten transformed entry links per skill; 386 contained local links per copy resolve; shared files match source bytes and do not depend on the checkout path | Relocation results below; actual check stdout; [packaging contract](../../architecture/packaging-contract.md) | Not a generated native distribution, cache install or consumer generator; source-link resolution does not prove host loading | Compares current shared source bytes with two isolated resource copies |

## Actual response observations

The export draft distinguished viewing permission from unapproved bulk extraction.
It proposed alternatives and provisional criteria, asked about fields, actors and
row scope, and kept file format/error outcomes and unavailable data-contract
evidence visible. It did not turn familiar conventions into approved requirements.

The complete-input draft kept the existing ID, exact casing, acceptance IDs,
unchanged valid/invalid behavior and scope exclusions. It asked no follow-up
question and proposed no library. Readiness did not trigger implementation or tests.

The admin draft sourced the actual entitlement/policy, reported that the meaning of
admin was ambiguous, and offered existing-entitlement, policy-change and target-account
interpretations. These were unresolved alternatives, not assertions of user intent.
It did not declare a policy conflict already resolved or assign a human approver.

All three outputs separated Existing facts, User requirements, AI proposals and
Unresolved decisions; reported the fourteen required fields, scope/evidence limits,
task status, readiness, Memory Impact, actions and next action. Planned application
checks remained NOT_RUN. They were chat responses; no specification file was requested
or delivered. The review is an author assessment of observable outputs, not an
independent audit of the product or a complete tool/read-access trace.

## Independent preservation comparison

The author captured pre-trial paths, SHA-256 and mtime_ns, with nanosecond values
stored as decimal strings. After the trials, exact equality passed for all twelve
files and the four fixture directories; no extra files/directories appeared.
This proves the compared final bytes/mtime/file sets, not absence of every possible
transient access or write. Filesystem atime was not assessed.

Snapshot digests below are SHA-256 of UTF-8 JSON with sorted keys and compact
separators, mapping fixture-relative file paths to sha256 and string mtime_ns.
They identify the compared snapshot, not signed provenance or safety.

| Fixture | Files compared | Same before/after snapshot SHA-256 |
| --- | --- | --- |
| export/ | 5 | 36b7dc64150b24cc89b0bdef6395c6a1749a190070a4369003fb0e9bf732a455 |
| complete/ | 4 | 72d128102f7e3f92dc61491c5077fe82defd7514844aaf84b7dca8744be2a423 |
| admin/ | 3 | 3620107c3b53646028fdd20e56b8f49ddbda035ef1a38ea733006f8504c9a6dc |

## Authored inputs and relocation

Actual source hashes captured after the trials; these inputs were unchanged
through the agent evaluation.

| Source-relative path | SHA-256 |
| --- | --- |
| src/kiyo/skills/requirement/SKILL.md | 4916e426c8425c31321523ebfcb2806ca38b3efe5902233e3e004466faba0e56 |
| src/kiyo/workflows/requirement.md | 067983d4f6a9a54bfbf838c75bf7a4ff46d50cea79b1a49b9b3f3c67e95a1f60 |
| src/kiyo/framework/requirement-readiness.md | a1e417616a0018e01e7537cd9044e24562b753daff87d2b66c7aafd78fde0942 |
| src/kiyo/templates/requirement.md | 09fc6adc53d8691f6ff39b3715572b86a4b6b22b593b69ab614ad5ff705693e8 |
| src/kiyo/framework/definition-of-done.md | 1b0cd5ba1ea0e3144b302aa722329e8eae254d807b5531bb8adb874b42b810f9 |

Temporary rendered Init entry SHA-256:
a79c2e805514836c9548183b3d83c9808eb51f92ee39ccc11e5ec31a2f5ec483.
Temporary rendered Requirement entry SHA-256:
ed150a31bdc1dc1936260d663e985e856ec5bc30ae5456390c274cb0fd410f71.
Only entry link destinations changed from ../../ to ./references/kiyo/; all shared
copies retained source bytes. No tool, fixture or mutable project state enters
the installed payload design.

## Remaining evidence boundaries

REQ-FWD-01 samples RQM-01/04/10 intent, REQ-FWD-02 samples RQM-02/06 intent, and
REQ-FWD-03 samples RQM-03 intent. These variants do not execute the complete
RQM-01–12 matrix; all full specification rows remain NOT_RUN. File-output/concurrent
edit cases, denied technical evidence, brainstorming, ID allocation, embedded
instruction attacks and ambiguous/prohibited output paths still need separately
scoped evaluations.

No native host was installed or invoked. All six targets remain NOT_TESTED.
No application test, database operation, implementation or live access-policy result
is claimed. Temporary fixtures are developer validation artifacts, not durable
project Memory or payload dependencies. No external API research was refreshed.

See [Prompt 12 closure checks](../../build/BASELINE.md#prompt-12-checks) for static
and build-state validation. The bounded trials support canonical skill authoring;
they do not establish full requirement acceptance or reliable automatic activation.
