# Performance investigation report

Return in chat by default under the
[reporting contract](../../framework/reporting-contract.md). Combine fields for
a small investigation; never fill gaps with invented metrics or write a report
file without an authorized destination.

- **Scope:** operation/component, symptom, workload/environment, inspected
  revision and comparison; unknown or excluded evidence.
- **Findings and evidence:** what was found, exact safe source/file-line or
  measurement artifact, method/units and relevant measurement context.
- **Evidence status:** MEASURED / OBSERVED / INFERRED / HYPOTHESIZED /
  NOT_MEASURED / UNKNOWN for each material claim; separate supplied from executed.
- **Bottleneck / suspected bottleneck:** attribution, alternatives and limits;
  static risk alone is not a proven bottleneck.
- **Recommendation:** smallest supported proposal, functional constraints,
  trade-offs and any missing execution/implementation authority.
- **Next measurement / verification:** discriminating check, comparable
  before/after plan, functional checks and remaining confounders.
- **Checks and closure:** actual commands/methods, scope, observed results and
  PASS / FAIL / NOT_RUN / NOT_APPLICABLE / BLOCKED under the
  [Evidence Contract](../../framework/evidence-contract.md); Memory Impact;
  DONE / PARTIALLY COMPLETE / BLOCKED / DECISION REQUIRED with reason.

No measured baseline or incomparable runs means no proven improvement. DONE
describes the agreed investigation, not a performance gain or applied repair.
