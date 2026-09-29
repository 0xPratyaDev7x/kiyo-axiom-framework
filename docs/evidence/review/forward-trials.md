# Review bounded source-guided evidence

Checked: **2026-09-29** (Asia/Bangkok). Developer-only evidence; excluded from
installed resources. Prompt 14 authoring status is separate from full requirement,
scenario-suite and native-host verification.

## Method and source

An independent evaluating agent received the actual
[Review entry](../../../src/kiyo/skills/review/SKILL.md), relevant packaged
references and three isolated synthetic current-file review requests. It was not
given scenario expectations, suspected defects, proposed fixes or author conclusions.
Accepted fixture contracts were supplied as task requirements. All source,
Memory, reports, tests and Git mutation/execution were outside the evaluator's
scope; safe file inspection and chat delivery were allowed.

These were source-guided reviews, not native skill invocation or an independent
security audit. The author created temporary fixtures outside the repository,
captured thirteen exact file hashes/mtime values and five directory names before
evaluation, then compared the same sets after it. Resource-copy validation used
a separate temporary root; it was not in the evaluator's allowed fixture scope.

Actual source SHA-256 values used:

| Source relative to src/kiyo | SHA-256 |
| --- | --- |
| skills/review/SKILL.md | 0afc737082e6865988c1e698e32af063f0e76d789c60e74c0e2822b22af3d244 |
| workflows/review.md | 08bb940ef5d1c01ab21f43a22134c149295b6d4511309b22aa1fb09d4a111179 |
| framework/review-severity-confidence.md | 92a7e13e59c7fb191d4a6b13e4762151e2ad251429bd7b990dcadcdc648aa8b3 |
| templates/reports/review-finding.md | 203ef1d10ce93eba5f988936b3b2b114fad575f6c4ab6a98b63a7f20142dd425 |
| templates/reports/review-report.md | f8302dd2e0ba3d8f698569edcfe6dccffc832b7cd49dd6e9e39287d81d5b8324 |

## Raw fixture intent and bounded observations

- **alpha:** contract R-EXPORT-1 says only invoice-tenant members may read the
  total and dispatch is the sole public entry. dispatch rejects only a null
  user, calls export_total, and that helper returns the selected invoice total
  without checking tenant membership. Test notes supply a same-tenant example,
  explicitly no execution results.
- **beta:** the same tenant rule applies. dispatch first loads the invoice,
  calls require_tenant with its tenant, then calls export_total. The guard rejects
  a null user or a mismatched tenant. The accepted contract identifies dispatch
  as the sole public entry and the helper as called only there. Test notes supply
  no executed results. This fixture distinguishes effective protection from a
  policy file merely being present.
- **gamma:** R-PAGE-1 requires size zero to return an empty list. paging.py
  returns items[:1] for size zero; routes.py registers first_page at /v2/items.
  The accepted contract names .kiyo/memory as its canonical store. The index points
  to observation MEM-ROUTE-001, whose recorded route is /v1/items, with historical
  dates and a human note to preserve its text. No approved architecture decision
  or executed tests were supplied.

The evaluator returned A-1 as Confirmed defect, HIGH severity/HIGH confidence,
citing alpha/app.py lines 2, 4 and 8 and contract line 1. It explained the
cross-tenant condition, gave a proposed guard and synthetic negative checks,
and explicitly distinguished static causality from runtime/production evidence.

For beta it reported no findings in the inspected scope after tracing app.py
lines 5 onward through policy.py line 2, rather than declaring the helper unsafe
because it lacks a duplicate check. It retained missing error-contract and test
execution limits; negative cases remained proposed.

For gamma it returned G-1, Confirmed defect, MEDIUM severity/HIGH confidence,
citing paging.py line 2 onward, routes.py line 3 and contract line 1. It separately
classified MEM-ROUTE-001 as a stale observation with UPDATE_REQUIRED and a proposed
correction, not an approved-decision conflict or proven route bug. Memory text,
status and verification dates remained untouched.

Each review was DONE only for its supplied current-file inspection. Findings
remained unfixed; no comparison or regression attribution was invented. The
evaluator used G1 Observe and LOW action risk for bounded synthetic local reads,
separate from defect severity. It covered all ten dimensions proportionately,
kept all build/tests NOT_RUN, and supplied the shared report/evidence fields.
Its static contract checks recorded FAIL for alpha/gamma, PASS for beta and FAIL
for gamma's stale observation; these are actual review outcomes, not failing
executed application tests. The author did not import or execute fixture code.

## Actual check records

| Name | Applicability | Command/method | Inspected scope | Execution status | Observed result | Evidence location | Limitations | Baseline relation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REV-FWD-01 Tenant boundary | Bounded variant of REV-01/04/10 | Independent agent follows source skill; line-numbered file inspection and static contract comparison | alpha/app.py, accepted contract and test notes | PASS | Identified supported A-1 with all finding semantics, no repair or fabricated execution; application contract inspection itself FAIL | Evaluator final response summarized above, actual fixture hashes below | No exploit/runtime/production, actual diff or full scenario execution | Deliberately seeded fixture defect; no earlier revision, regression attribution Unknown |
| REV-FWD-02 Effective policy | Bounded variant of REV-02/10 | Same source-guided inspection, trace registered public call through guard | beta/app.py, policy.py, accepted contract and notes | PASS | Rejected local-check false positive; bounded no-findings conclusion and NOT_RUN tests; static tenant contract inspection PASS | Evaluator response and fixture evidence below | Single declared public entry, no hidden caller/runtime/native result | Controlled contrasting fixture, not an application before/after comparison |
| REV-FWD-03 Bug and Memory | Bounded variant of REV-03/04/10/14 | Source-guided static inspection; read canonical index then relevant observation and compare registry | gamma paging/route/contract/notes and two Memory files | PASS | Identified zero-size defect and stale observation separately; UPDATE_REQUIRED proposal, no code/Memory edits or execution; no invented Git state | Evaluator response, snapshot comparison and hashes below | No Git/range/branch/PR behavior evaluated; approved-decision conflict not exercised | Source versus deliberately stale observation; defect introduction Unknown |
| REV-SNAPSHOT-01 Read-only artifacts | Required preservation evidence for all three trials | Author inline Python SHA-256, exact mtime_ns, file/directory-set equality | All thirteen fixture files and five directories before/after | PASS | Exact bytes/timestamps/sets unchanged; no added/deleted report, test or Memory file | Actual comparison output and hashes below | Snapshot equality cannot prove absence of transient effects or all access; tool-method claims rely on evaluator report | Author-captured original fixture snapshots, unchanged after evaluation |
| REV-RESOURCE-01 Relocated resources | Canonical packaging design validation | Inline Python copies shared resources byte-for-byte, transforms entry links, resolves contained references | Init, Requirement, Implement and Review temporary source copies; 77 shared files each | PASS | Entry/local link counts: Init 10/431, Requirement 10/431, Implement 14/435, Review 11/432; all targets contained and present | Actual resource-check stdout; Review rendered entry SHA-256 5b2a5dee74ae309850e4cce9a993ef03957773f61c1a3711533b95b6c134de6d | Not native package/cache installation, host activation or lifecycle; developer-only temporary transform | Existing entries checked with the new shared resource snapshot |

Reported inspection methods: PowerShell Get-Content -LiteralPath with line numbers;
rg --files --hidden excluding .git/node_modules within each explicit fixture;
Get-ChildItem -LiteralPath -Force for names, modes and link information. No
project import, build, test, network, install or Git operation was reported.
One aggregated shared-reference output was truncated; the evaluator reread the
affected Memory lifecycle reference completely. This is a disclosed context
limitation, not evidence of exhaustive reads. The author reviewed the delivered
responses and compared fixtures; no claim of complete independent tool telemetry.

## Immutable fixture inventory

Paths below are relative to the isolated fixture root, not repository product
content. Temporary fixtures may not persist across environments; these hashes
and concise input descriptions identify the observed variants, not a committed
executable test harness. All thirteen before/after hashes and mtime_ns values
matched exactly; mtime equality was compared as integer strings, not rounded values.

| File | Observed SHA-256, unchanged |
| --- | --- |
| alpha/app.py | cb5dd40096ca3da33e7e5d5829b54667141fca2626fadd448ae00e2677803202 |
| alpha/contract.md | 35c3bc80fd7ff6626dc299024e98fa4b1f455402157c37ba03e05f2b28f4e53a |
| alpha/tests_notes.md | 14be95d0ca152a45130862ae9f93b797b9ffefe841f46c59af7718bd7c82b8ff |
| beta/app.py | c9853be41fb423b3ab30500a5e9c0aca3fe3d2995e270e7541cd250320188aeb |
| beta/contract.md | 109453c0b5ac7aa2a76c4ed9d24c91cb9ccd10d1842438dff531f5f8f59ba048 |
| beta/policy.py | bb5714b0aa1af2efead4feea30ab8df579f63f1e5880bb19c1c64dcdf330f98b |
| beta/tests_notes.md | 14be95d0ca152a45130862ae9f93b797b9ffefe841f46c59af7718bd7c82b8ff |
| gamma/contract.md | 02ed3c8ed77e23c9fbd8779ce94753370adb6ade67fead6b74700ead84505d7f |
| gamma/paging.py | af4d5e6e18aea1118970baa804692f649d8c9d1865729dcbfef8eb337d646cdd |
| gamma/routes.py | ffa567c455acf4e0b75d433f5ece10faf101fedc350f9ebd679ef021c2114c41 |
| gamma/tests_notes.md | 4af8310e63aa6d523eb6a57c1ee2858fe35a4963746b349fa417ef234be54223 |
| gamma/.kiyo/memory/index.md | 3baea0a1c62a985480f159ee44dec1a4f7c22ae1f7399ea68ff90d7b63736931 |
| gamma/.kiyo/memory/project.md | 44b7de218b6c2fa52310ca51c8eebc5fe944ffe43cb7855a6825443a675fadcc |

## Remaining evidence boundary

The complete sixteen-case [Review matrix](../../../tests/behavioral/review/scenarios.md)
is NOT_RUN. These variants do not establish staged/index behavior, zero-diff
handling, unavailable refs, actual PR access, concurrent human edits, all redaction/
injection cases or an explicitly authorized execution/output transition.
All six native targets remain NOT_TESTED. No application runtime, build, test,
network, native package or production check was performed by these trials.
Developer-source evaluation is not a security/certification guarantee.
