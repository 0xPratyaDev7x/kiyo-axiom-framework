# Shared reporting contract

Use for final or interim deliverables from any of the eight skills. Chat is the
default output; reuse the smallest suitable template and only its relevant parts.
Templates are neutral structures, not populated records, tools or new workflows.

## KIYO-REPORT-001 — Report scoped work without manufacturing an audit trail

Every report conveys the following; a compact answer may combine fields into
clear sentences, but must retain required evidence, gaps and status.

| Field | Required content |
| --- | --- |
| Task/scope | Requested deliverable, skill/mode, inspected boundary, exclusions and applicable requirement/acceptance IDs. |
| Actions/files changed | What was actually read, changed or executed; distinguish proposed, written and verified work and preserve attribution to human edits. |
| Governance/risk rationale | Actual authority, action/target/environment/data/reversibility/impact and uncertainties at relevant depth; Kiyo governance mode and risk rating stay separate. Do not invent an approval gate or assign LOW because facts are missing. |
| Verification/evidence | Named check records under the nine-field Evidence Contract, current required results, baseline relation and explicit unrun/blocked/inapplicable reasons. |
| Residual issues | Remaining failures, limitations, drift, unknowns, deferred/out-of-scope findings and decisions; no vague “all clear” replacing them. |
| Memory impact | NONE / UPDATE_REQUIRED / CONFLICT / NOT_ASSESSED with inspected scope, reason and applied/pending delta, including required sync gaps. |
| Status | One actual task status from Definition of Done, scoped to the original deliverable; separate check outcomes and implementation readiness. |
| Next required action | Concrete remaining action/decision, relevant precondition and responsible role only when known; say none for the completed scope when supported. |

Use [Evidence Contract](evidence-contract.md) and
[Definition of Done](definition-of-done.md); templates reference these meanings
rather than maintaining separate rules. Facts, Assumptions, Proposals, Approved
decisions and Unknowns remain distinct where material.

Write a report to disk only when its destination/content are in authorized write
scope. A read-only review returns chat findings; permission to write one requested
report file does not permit code, policy or Memory edits. Re-read a destination
before an authorized update and preserve human content. Do not automatically
create report directories, evidence archives, approval records or a second memory
store. Installed templates remain immutable; never save populated reports in
plugin cache or the product payload.

Keep secrets, unnecessary PII, raw logs, transcripts and private reasoning out of
reports. Prefer concise sanitized observations, safe file/symbol locations and
permitted evidence references. Do not read or expose credentials to make a report
look complete. A path/URL can itself disclose sensitive information; minimize or
redact it and state the resulting evidence limitation. Synthetic examples must be
labeled synthetic; placeholders must not be presented as completed observations.

Commands/counts/timestamps/versions require actual evidence. Provider/model/account
identity and access counts are Unknown when unavailable; do not infer them from
“Enterprise,” the host label or tool-call count. Omit irrelevant metadata rather
than guess it. Never claim exhaustive file/network access visibility. Self-review
is not independent audit; a chat/Markdown report is not a tamper-proof log or
proof of prevention, certification, authorization or actual execution.

## Template selection

| Need | Packaged template |
| --- | --- |
| Tiny or ordinary bounded result | [Compact task report](../templates/reports/compact-task-report.md) |
| Multiple criteria/checks or material engineering impact | [Engineering report](../templates/reports/engineering-report.md) |
| Missing policy-defined scoped human decision | [Approval request](../templates/reports/approval-request.md) |
| Stale observations or approved-intent conflict | [Memory/architecture drift report](../templates/reports/memory-architecture-drift-report.md) |
| One evidence-based review issue | [Review finding](../templates/reports/review-finding.md) |
| Review scope, findings/zero diff, coverage and limits | [Bounded review report](../templates/reports/review-report.md) |
| Application/agent security assessment | [Security assessment](../templates/reports/security-assessment.md) |
| Incomplete work, transfer or context limit | [Handoff](../templates/reports/handoff.md) |

Load one needed template, not the whole catalog. A required approval request uses
the existing [human approval procedure](../governance/human-approval.md); the form
cannot authenticate a copied approval or override policy/host denial.
A handoff uses the existing [repair/handoff procedure](../workflows/repair-and-handoff.md),
preserving attempts and real authorization scope on resume. Reports do not imply
background work, automatic activation or later-task authorization.
