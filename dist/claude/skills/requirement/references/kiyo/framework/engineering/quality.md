# Contextual quality review

Load only quality concerns materially affected by the requested behavior.
This table is Kiyo's practical grouping, **not an exact ISO/IEC 25010 taxonomy**,
a clause checklist or a certification assessment. Optional provenance is in
[the concept mapping](standards-mapping.md).

## KIYO-ENG-006 — Evaluate affected quality with proportionate evidence

| Concern | Ask / act | Expected evidence when relevant |
| --- | --- | --- |
| Correctness | Does behavior satisfy sourced requirements, edge cases and invariants? | Acceptance examples and actual checks or explicit gaps. |
| Maintainability | Can a maintainer understand the change within existing boundaries without unnecessary complexity? | Focused review of naming, cohesion and dependencies. |
| Performance | Is a material latency/resource/volume concern introduced? Avoid speculative optimization or invented budgets. | Relevant query/profile/measurement with workload and environment, or NOT_RUN. |
| Reliability | What happens under failure, timeout, retry, concurrency or partial completion? Avoid duplicate effects and silent data loss. | Failure/concurrency checks appropriate to the changed path. |
| Compatibility | Which public consumers, persisted formats and supported versions could be affected? | Contract/version evidence and migration/compatibility plan when necessary. |
| Accessibility / interaction | Can affected users complete the journey, including keyboard/focus, labels, error feedback and relevant assistive use? | Scoped UI review and actual interaction checks; mark untested devices/assistive tools. |
| Operational concerns | Where applicable, examine deploy/rollback, configuration, observability, capacity and recovery effects. | Authorized environment evidence, sanitized diagnostics and limits on untested operation. |

Use observed project quality targets; ask about a material missing target rather
than inventing performance budgets, uptime promises or accessibility compliance.
Security concerns use the separate
[application checklist](../../agent-security/application-security.md) and actual
policy. A quality objective does not authorize access to production or user data.

For a concern not applicable to this change, a short reason is enough; do not
generate a full quality report for a tiny edit. Record tradeoffs as proposals,
link approved decisions only when evidenced and report remaining uncertainty.
A local measurement, review or tool score has a stated scope and is not a blanket
quality guarantee. Follow [Testing](testing.md) for result reporting.
