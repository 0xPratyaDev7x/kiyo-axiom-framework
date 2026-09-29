# Engineering report template

Neutral structure for a material change/analysis; use the
[reporting contract](../../framework/reporting-contract.md) in chat by default.
The tables express relationships, not pre-populated test results or audit logs.

- **Task/scope:** <requested behavior/output, skill/mode, criteria, exclusions>
- **Actions/files changed:** <actual inspected/edited paths and purpose; human edits preserved>
- **Governance/risk rationale:** <authority, separate G-mode/risk and material factors; approval scope/source/validity or gap>
- **Verification/evidence:** <current nine-field check records per Evidence Contract; summarize trace below>
- **Residual issues:** <baseline/new/environment/unknown failures, uncovered risk and decisions>
- **Memory impact:** <value, assessed entries/component, required sync and actual applied/pending delta>
- **Status:** <task status with unmet mandatory criteria visible>
- **Next required action:** <specific step/decision and preconditions, or none within scope>

| Requirement / acceptance ID or named criterion | Actual implementation / inspected files | Planned or existing test/check ID | Actual evidence reference / gap |
| --- | --- | --- | --- |
| <existing criterion> | <real location or missing> | <ID and planned/executed distinction> | <safe observed result reference or unavailable> |

Use the [nine-field check record](../../framework/evidence-contract.md) for each
check; the trace table is not a substitute. Identify the checked state and any
later changes requiring recheck. Report requirement-document delivery separately
from **Implementation readiness:** <READY_FOR_IMPLEMENTATION / DECISION_REQUIRED /
INSUFFICIENT_EVIDENCE, basis> when relevant; use the
[Requirement readiness checklist](../../framework/requirement-readiness.md).

**Self-review:** <requirements, architecture, quality, security, governance;
evidence/findings or reason not applicable per dimension>. Label actual independent
review only if its separate reviewer/process is evidenced. Do not infer it from
self-review, a scanner or this report.

Sensitive details stay out; concise redacted observations and safe references
replace raw logs. No PR/commit is required to provide traceability.
