# Shared Definition of Done

Use the selected skill's actual task/output and authorized action mode, not a
generic “code works” claim. These are Kiyo completion rules, not ISO levels,
native enforcement or automatic gates. Read only the relevant workflow row and
shared closure rules; do not load every report/profile.

## KIYO-DONE-001 — Close the agreed workflow against current required evidence

Before work and again at closure, identify agreed deliverables/acceptance,
required checks, actual approval scope and any mandatory Memory sync from the
accepted workflow/policy. Use the [Evidence Contract](evidence-contract.md).
Do not retroactively weaken a mandatory check to obtain DONE.

| Workflow / mode | Completion criterion | Boundary of the conclusion |
| --- | --- | --- |
| Implement | Agreed behavior and acceptance criteria are met; required approvals still match action/resources/environment/effects; required verification actually passes for the final affected state; scope, security and governance review completed; Memory Impact assessed and any mandatory sync completed under valid write authority. | Local checks cover their actual scope, not production or all consumers. A required failed/unrun/blocked check or pending mandatory sync prevents DONE. |
| Review / explain | Agreed inspection scope examined; findings, evidence and limitations delivered; Memory drift/impact reported without writes. | DONE means the bounded review is complete, not that the application is bug-free or tests pass. If required inspection is unavailable, report incomplete scope. |
| Requirement | Agreed requirement deliverable includes the applicable objective/problem/behavior, scope/exclusions, rules, acceptance, constraints/dependencies and separated facts/assumptions/proposals/approved decisions/unknowns, with stable IDs where appropriate. | Report document delivery status separately from implementation readiness. A requested proposal may be DONE with clearly recorded open decisions; a request for a ready-to-implement specification cannot be DONE while required decisions/criteria remain unresolved. |
| Memory check / audit / show | Requested entries/component inspected or shown within permission; checked versus merely displayed claims, drift, uncertainty and Memory Impact stated. | A check of selected entries does not certify all project memory. Check/show never implies sync, freshness-date writes or code fixes. |
| Security | Agreed bounded assessment and required review/check methods completed; findings, affected boundaries, limitations, residual risk and necessary next actions delivered. | Completion is not “secure,” certified, vulnerability-free or an independent audit by default. Mandatory unperformed methods prevent DONE for that assessment. |
| Test assess / execute | Assess: requested coverage/gap analysis delivered with proposed checks labeled unrun. Execute: requested check scope actually evaluated and evidence/failures reported, with any required repairs/acceptance handled as agreed. | A test-results report can be delivered with FAIL results when that is its agreed objective; it does not make an implementation with required failed verification DONE. |
| Architecture analyze / propose | Agreed boundaries/contracts/tradeoffs inspected; evidence, conflicts and proposal/ADR status delivered with limitations. | A proposal is not approval, implementation, migration or production validation. Apply Implement criteria as well if actual changes were authorized. |
| Init or authorized Memory writes | Agreed setup or necessary record delta applied under actual authority; existing canonical paths, human edits and approved decisions preserved; required scoped checks and Memory Impact completed. | No installation, automatic activation or whole-project verification claim follows from file creation. Actual public-skill specifics remain defined by their own scope. |

### Shared closure procedure

1. Compare final deliverables to each agreed criterion. Separate inspection,
   authored artifact, executed behavior and remaining work. For requirements,
   state **Implementation readiness: READY / NOT_READY / UNKNOWN** with evidence
   and open decisions; these are readiness labels, not additional task statuses.
2. Review the final affected scope against requirements, architecture/quality,
   security and governance; explain actual non-applicability. Confirm approval
   validity under [human approval](../governance/human-approval.md); do not ask
   again when it still matches. Label review performed by the author as self-review,
   not an independent audit. A template cannot grant approval or waive denial.
3. Reconcile required check records with the final state using KIYO-VERIFY-002.
   Preserve every failure and unrun gap. Missing environment is not N/A.
   Record partial/blocked work honestly; a repair limit is not completion evidence.
4. Assess [Memory Impact](memory-specification.md#kiyo-mem-006--memory-impact-at-closure):
   NONE, UPDATE_REQUIRED, CONFLICT or NOT_ASSESSED, with scope and applied/pending
   deltas. NONE means no necessary delta, not “we lacked permission to check.”
   If assessment required for closure is missing, NOT_ASSESSED prevents DONE.
5. When applicable policy/workflow requires sync, verify the necessary delta was
   actually completed before Implement DONE. Without write authority, hold the
   sync and report incomplete/blocked completion; never write just to satisfy DoD.
   A read-only review may finish with UPDATE_REQUIRED or CONFLICT as a finding
   when its agreed assessment is complete. No delta means no memory touch.
6. Report the appropriate task status, remaining issues and next required action
   using [shared reporting](reporting-contract.md). A file is optional and needs
   actual write scope. No commit, PR, release, deployment or memory initialization
   is implied by completion.

### Exact task statuses

| Task status | When to use it |
| --- | --- |
| DONE | The explicitly named deliverable/workflow scope and all its applicable mandatory completion criteria are satisfied with current evidence. |
| PARTIALLY COMPLETE | Useful scoped work is delivered but requested work or mandatory evidence remains unfinished; show completed and remaining portions and any concrete blockers. |
| BLOCKED | A concrete missing prerequisite prevents required progress on the named scope; identify the held action and safe next step. Partial artifacts, if any, remain visible. |
| DECISION REQUIRED | An unresolved material business/scope/authority choice prevents the next dependent action; state the concrete decision and existing evidence. |

Choose one status for the reported task scope and show subtask/check results
separately. A blocked check can accompany a PARTIALLY COMPLETE task; use BLOCKED
when the task cannot make required progress. If progress specifically depends on
a choice, use DECISION REQUIRED, without hiding missing mandatory evidence.
Do not label only the finished subset as the entire original task. Redefining the
requested deliverable from working behavior to “a patch was written” needs a real
scope decision. Report status does not prove behavior or authorize further work.
