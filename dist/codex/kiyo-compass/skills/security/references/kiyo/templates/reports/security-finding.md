# Security finding template

Use under the [Security procedure](../../workflows/security.md) with the
[assessment report](security-assessment.md), in chat by default.
For multiple findings put shared task/report fields once in that report.
This is a neutral template, not a scanner result or approval.

- **Finding ID/title and classification:** <actual or response-local ID; Confirmed
  defect / Plausible risk / Improvement suggestion as supported; no fabricated issue>
- **Control/concept reference:** <actual Kiyo ID, AST topic, secure-coding concept
  or sourced accepted requirement; no invented standards clause or equivalence to ASI>
- **Exact evidence:** <actually inspected safe file:line/range/symbol, view/revision
  when observed, method and concise observation; redact protected values/path
  details and explain the resulting limit instead of inventing a location>
- **Impact:** <affected boundary/behavior/data and supported consequence; separate
  observed effect from conditional risk and unavailable reachability>
- **Confidence:** <HIGH/MEDIUM/LOW with concrete evidence basis and unresolved
  premises under the shared guide; not a probability, intent verdict or test result>
- **Mitigation:** <bounded proposed treatment, verification idea marked unrun,
  required scope/approval/control evidence before any remediation or execution>
- **Control owner:** <Kiyo / host / release / human responsibilities and actual
  accepted owner evidence when available; category is not a named approver>
- **Coverage and limitations:** <inspected versus unread/denied/untested content,
  static/behavioral/native distinction, relevant snapshot/freshness/baseline limits>

Use the [confidence guide](../../framework/review-severity-confidence.md) and
[ownership mapping](../../agent-security/control-ownership.md). Add severity only
when useful/supported; it is independent of confidence and review-action risk.

For unavailable signatures report **Signature assurance: NOT_VERIFIED**, with
the gap and any actual policy dependency; do not label unsigned safe or malicious.
That assurance label does not replace the five
[check statuses](../../framework/evidence-contract.md#exact-check-statuses).
For inaccessible enumeration state inventory incomplete. No finding, LLM review,
static syntax result or template completion establishes safety/certification.
