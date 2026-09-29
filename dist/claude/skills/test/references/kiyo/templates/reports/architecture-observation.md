# Architecture observation template

Use with the [Architecture procedure](../../workflows/architecture.md).
Neutral chat structure, not Project Memory or an approved ADR. Keep all five
categories distinct; combine shared report context once when using impact/drift
sections. Do not fill unknowns from folder names or typical architecture patterns.

- **Task/scope:** <actual question, component/worktree, inspected snapshot and exclusions>
- **Actions/files changed:** <actual read/search methods; no project/Memory/policy writes>
- **Governance/risk rationale:** <permitted context, sensitivity, actual read effects and constraints>
- **Verification/evidence:** <five categories below and nine-field check records>
- **Residual issues:** <findings, unresolved decisions, unknown consumers and coverage gaps>
- **Memory impact:** <NONE / UPDATE_REQUIRED / CONFLICT / NOT_ASSESSED; inspected IDs/scope and reason; no sync>
- **Status:** <DONE / PARTIALLY COMPLETE / BLOCKED / DECISION REQUIRED for the actual assessment>
- **Next required action:** <specific needed evidence/decision or bounded proposal, no implicit implementation>

## Current observed structure

<Actually inspected modules, dependencies, ownership, contracts and conventions.
For each substantive assertion/finding give exact safe file:line/symbol/view,
inspected boundary, direct observation versus inference, potential impact,
confidence with evidence basis and relevant requirement/control. No runtime claim
from test source, dependency name or configuration alone.>

## Approved intended structure

<Applicable existing decision IDs and actual approval provenance/scope, known
constraints and conflicts. If unavailable, state which records were inspected
and what remains unestablished; do not declare absence beyond scope.>

## Proposals

<Optional alternatives or corrective directions, assumptions, tradeoffs and
required human choices. An observed pattern is not an approved mandate.
No proposed ADR adoption, architecture migration or library installation implied.>

## Unknown deployment behavior

<Actual runtime topology, active providers/wiring, external consumers and
environment-dependent behavior not established by permitted evidence.>

## Inspection limitations

<Files/symbols/components inspected, searches and exclusions, unavailable sources,
snapshot/concurrent-edit limits and unperformed checks. No unsupported score.>

Reuse the [Evidence Contract](../../framework/evidence-contract.md) and
[confidence guide](../../framework/review-severity-confidence.md).
For decision comparison use the [drift report](memory-architecture-drift-report.md);
for prospective effects use the [impact report](architecture-impact-report.md).
Report delivery is not production verification or approval to change the project.

