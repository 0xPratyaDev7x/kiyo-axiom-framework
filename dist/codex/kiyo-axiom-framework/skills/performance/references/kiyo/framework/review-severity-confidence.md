# Review severity, confidence and classification

Use for candidate findings under the [Review procedure](../workflows/review.md)
(KIYO-REVIEW-001). These are Kiyo reporting conventions, not vendor permissions,
ISO levels, CVSS scores or numerical probabilities. Honor an established project
scale when applicable and explain any mapping; do not silently relabel it.

## Classification

| Category | Evidence needed | How to report |
| --- | --- | --- |
| Confirmed defect | Inspected behavior and a supported trigger conflict with a sourced requirement, contract or directly established invariant; relevant effective protections/exceptions examined. | State the causal path and impact within the inspected state. Static confirmation is possible; it does not mean reproduced at runtime or observed in production. |
| Plausible risk | A concrete suspicious path has a material unresolved condition, reachability question or unavailable protection/contract. | State the condition, missing evidence and what would confirm or dismiss it. Never present the hypothetical consequence as observed. |
| Improvement suggestion | A maintainability/design/coverage proposal without an established defect. | Explain the benefit/tradeoff and keep optional preference distinct from required repair. Do not manufacture a violation. |

Discard a candidate contradicted by effective evidence; a short explanation of
the checked protection can be useful, but it is not a defect. Missing requirements
may limit compliance assessment without invalidating a separate provable logic bug.
Do not force every uncertain concern into a finding when only an inspection
limitation is supportable.

## Severity: impact if the stated condition holds

| Severity | Contextual basis |
| --- | --- |
| CRITICAL | Supported path to catastrophic or broad compromise/loss; identify affected boundary, scale and assumptions. A security keyword alone does not justify this level. |
| HIGH | Major correctness, access-control, data-integrity or availability impact on an important affected path, with a concrete reason. |
| MEDIUM | Material but bounded incorrect behavior, compatibility failure or reliability impact; describe affected users/conditions. |
| LOW | Limited impact with narrow scope or an effective workaround; avoid minimizing sensitive exposure just because the diff is small. |
| INFO | Optional improvement without a demonstrated defect or material risk; not a pass/fail result. |

Severity rates finding impact, not the permission risk of performing the review,
not governance G1–G4 and not approval to fix. Qualify an uncertain blast radius
instead of assuming production exposure. For a Plausible risk, severity is
conditional on its stated trigger; indicate uncertainty separately.

## Confidence: strength of the finding's evidence

| Confidence | Required explanation |
| --- | --- |
| HIGH | Inspected sources support the bounded claim, relevant alternate explanations/protections checked, no material unresolved premise for that claim. |
| MEDIUM | Evidence supports a concrete concern but a named material premise or protection remains unresolved; commonly a Plausible risk. |
| LOW | Evidence is limited and conditional; identify the missing link and why the concern is still useful. Otherwise report only a limitation. |

Always pair the label with a short basis. Never invent percentages, imply a
calibrated probability or raise confidence because the code was AI-generated.
An unresolved premise essential to the defect means it is not Confirmed defect.
High confidence in the text of a Memory entry does not verify that entry's claim.
Confidence in a suggestion concerns the supported benefit, not user acceptance.

## Evidence and sensitive output

Use actually inspected file/line or range, view/revision, observed behavior,
impact, requirement/control reference, suggested fix and verification idea under
the [finding template](../templates/reports/review-finding.md). Preserve the
difference between observed static logic, externally supplied test output and
your own execution under the [Evidence Contract](evidence-contract.md).
A passing review-method check means the inspection was performed, not that the
application passed tests. Review-only build/tests are NOT_RUN, not N/A.

Sanitize secret/PII content and sensitive path segments under
[data handling](../governance/data-handling.md). Report a safe location and the
evidence limitation when full disclosure is not permitted; do not invent a
replacement path. Use synthetic markers/identities for proposed checks, never
copy credentials or run an exploit. Report self-review as such; no security,
independent-audit or tamper-proof assurance follows from a confidence label.
