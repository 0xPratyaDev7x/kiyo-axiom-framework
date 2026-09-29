# Requirement readiness checklist

Use after scoped discovery/drafting and again after a material answer or changed
source. This is an advisory assessment for the requirement's actual scope, not
a native permission setting, approval engine or certification. Apply
[KIYO-REQ-001](../workflows/requirement.md#kiyo-req-001--define-evidenced-requirements-without-authorizing-implementation)
and the [requirements standard](engineering/requirements.md).

## Required assessment

- The fourteen [template fields](../templates/requirement.md) are addressed.
  Unknowns and inapplicable aspects have reasons; mandatory gaps are not hidden
  in “N/A.” Keep effort proportional to the requested change.
- Existing facts and accepted constraints have authorized current evidence;
  stale Memory, uninspected repository portions and reported-only symptoms are
  explicit. No production conclusion is inferred from code.
- User requirements are sourced; material AI proposals/assumptions are visibly
  unaccepted or have actual acceptance evidence. No fabricated approvals.
- Acceptance criteria are observable and cover relevant success, invalid/denied,
  failure and boundary behavior. Planned verification is distinguishable from
  checks actually run; a specification needs no invented test PASS.
- Relevant dependencies, compatibility, security/data impact and validation/error
  behavior are bounded. Exact HTTP, permission and retention semantics require
  evidence or a decision; common patterns cannot supply business intent.
- Material conflicts/open choices and missing evidence have a next action.
  Do not ask again about complete supplied facts, or block a tiny change on
  irrelevant frameworks, provider identity or optional design preferences.
- The artifact, if requested, uses the authorized path and preserves human edits.
  Delivery completeness, requirement acceptance and permission to implement are
  separately reported; scope does not expand from a readiness label.
- Memory Impact is assessed within scope without writes. Use the relevant
  [DoD](definition-of-done.md) and [report contract](reporting-contract.md).

## Exact readiness values

Choose one value for the stated scope; list every material blocker, even when
more than one category applies.

| Value | Use when | Next action |
| --- | --- | --- |
| READY_FOR_IMPLEMENTATION | Enough current evidence and sourced/accepted behavior make the scoped requirement actionable; no unresolved material decision/evidence conflict prevents implementation planning. Permissible low-level implementation choices may remain open. | Deliver the assessment and stop. A separate authorized implementation task must establish its own preflight, checks and policy approvals. |
| DECISION_REQUIRED | A material behavior, business permission, scope, accepted-intent conflict or policy choice needs an authorized decision. Prefer this value if both a known decision and missing technical evidence block progress; list the evidence gaps too. | State known facts, alternatives/tradeoffs and the specific blocking question; continue independent authorized drafting only. |
| INSUFFICIENT_EVIDENCE | Necessary technical/current-state evidence is missing, inaccessible or unverified, and no specific unresolved material choice is yet established. | Name the smallest missing evidence and safe acquisition step or needed access; never invent facts or treat denied access as absence. |

Readiness is not a check status or one of the four task statuses. Task
**DECISION REQUIRED** (with a space) and readiness **DECISION_REQUIRED** (underscore)
belong to separate fields. Do not replace an unperformed mandatory check with
a readiness value.

## Delivery versus readiness

| Agreed deliverable | Example closure |
| --- | --- |
| Bounded draft/brainstorm with open choices | Task DONE can accompany readiness DECISION_REQUIRED or INSUFFICIENT_EVIDENCE when the requested draft and honest assessment are complete. |
| Implementation-ready requirement | Material choice blocks it: task DECISION REQUIRED; missing mandatory evidence may mean BLOCKED or PARTIALLY COMPLETE, according to actual progress. Do not call only the delivered draft the entire completed task. |
| Complete requirement in chat | Task DONE and readiness READY_FOR_IMPLEMENTATION can coexist with no file writes and no implementation authorization. |
| Requested specification file not written | Report partial/blocked scope and actual reason even if its content would otherwise be ready; chat delivery is not silently substituted for the requested file. |

“Ready” never authorizes code, test, config or Memory changes. A user may already
have supplied valid authorization, but Requirement still stops after its bounded
deliverable; report any route/scope transition through the shared workflow rather
than silently launching Implement. No automatic handoff execution exists.
