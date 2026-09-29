# Risk assessment

## KIYO-RISK-001 — Assess the concrete action and uncertainty

Risk is **LOW / MEDIUM / HIGH / CRITICAL**, separately recorded from G1–G4,
data class, authorization and the final decision. Use evidence and a concise
reason, not a keyword, ungrounded numerical formula or automatic mode mapping.

| Dimension | Questions/evidence needed |
| --- | --- |
| Action | Read, draft, generate, modify, install, execute, publish or delete? Which command/sub-actions actually occur? |
| Target | Which exact files/resources, branch, service, database or destination are affected? Is that identity established? |
| Environment | Local, isolated test, shared non-production or production? Verify configuration/context; do not infer from a label alone. |
| Data sensitivity | Applicable content-based class, authorized audience and any protected records/credentials; missing classification remains Unknown. |
| Reversibility | Can the actual effects be reversed, by whom, with what evidence? Is restoration merely proposed or tested? |
| Blast radius | What systems, data, repositories and downstream consumers could be affected, including hidden script effects? |
| Affected users | Who is affected, how many/which groups if evidenced, and is there a shared/operational impact? Avoid unnecessary personal identifiers. |
| Uncertainty | Which assumptions, inaccessible inputs, unreviewed scripts or unverified targets could change the conclusion? |

| Level | Evidence-based guidance, not automatic thresholds |
| --- | --- |
| LOW | Bounded, understood effects; little sensitive exposure and straightforward recovery within the known scope |
| MEDIUM | Meaningful but contained impact, dependency/contract effects or recovery effort with adequate target evidence |
| HIGH | Substantial sensitive exposure, security/availability impact, broad shared effects or difficult recovery |
| CRITICAL | Credible severe/widespread irreversible loss, major protected-data disclosure or critical security/production impact |

State all eight dimensions for sensitive/ambiguous actions. A small task may
summarize them in a sentence when clear; do not create eight empty sections or
request approval merely to complete a form. Explain which facts drive the level.
Risk can remain **Unknown (not assigned)** when evidence is insufficient; this
is the absence of a rating, not a fifth risk level or permission to proceed.
Hold dependent actions when an unknown target/environment/data exposure prevents
a safe decision. Do not label every uncertainty CRITICAL or silently rate it LOW.

Reassess changes to action, files/resources, environment, data class/destination,
reversibility, blast radius, affected users, scripts or uncertainty. A mitigation
only lowers assessed risk when supported by evidence. A backup filename is not
proof that rollback works, and a passing local test is not production assurance.

Do not assume read-only work is always safe, tests are always safe, dependencies
are always HIGH, or generating a migration equals applying it to production.
Use [dangerous actions](dangerous-actions.md) and
[approval scope](human-approval.md) for the resulting decision. LOW risk cannot
override an explicit prohibition; HIGH risk alone does not manufacture one.
