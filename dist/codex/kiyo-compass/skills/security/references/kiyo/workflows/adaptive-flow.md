# Adaptive flow depth

## KIYO-FLOW-001 — Reduce ceremony without skipping controls

Choose Tiny, Normal or High-impact from the actual action, uncertainty and effects,
not line count alone. These are Kiyo procedure depths, not native modes, ISO/NIST
levels or risk ratings. Governance G1–G4 and LOW/MEDIUM/HIGH/CRITICAL remain
separate under [risk assessment](../governance/risk-assessment.md).
A one-line auth/policy change can require High-impact handling.

| Depth | When appropriate | Visible working shape |
| --- | --- | --- |
| Tiny | Bounded, understood, low-impact change or narrow analysis with adequate scope/evidence | Compact scope/risk check; for an authorized change, small edit, applicable checks, memory impact and result; no elaborate plan/artifact |
| Normal | Several related steps or meaningful behavior requiring focused investigation | Short plan naming affected behavior/areas and checks; follow the relevant flow and report actual outcomes |
| High-impact | Sensitive effects, broad impact, difficult recovery or material uncertainty | Explicit scope/impact assessment, required human decision/approval and stronger boundary/effect evidence; hold unresolved dependent actions |

Tiny change sequence:
**compact scope/risk check → small edit → applicable checks → memory impact → result**.
For a read-only Tiny task, substitute focused inspection/analysis for small edit;
no write, implementation or memory sync occurs. Tiny does not waive accepted
policy, mandatory checks or required approval, nor does it require a question
when the existing explicit request already authorizes the bounded action.

The [implementation flow](implement-flow.md) gives the logical obligations;
Tiny may combine their presentation. Memory orientation remains authorized and
relevant; missing/no relevant memory does not justify initializing a store or
reading every template. The short scope statement can carry the plan for a typo.
Normal uses a short explicit plan. High-impact names the target/environment,
all material risk dimensions, affected users/data, reversibility and evidence gaps.

Preserve these obligations at every depth:

- Actual authority and read-only intent; valid scope is required before effects.
- Authorized relevant evidence and memory validation before asserting facts.
- Applicable human decision/approval, with reuse rather than repeat ceremony.
- Command/target/side-effect inspection before execution and honest check results.
- Minimum necessary change, human-edit preservation, scoped review and Memory Impact.

If scope, API/schema/architecture, data destination, target, approved intent or
required native control changes, pause the dependent step and replan/reassess.
Increase depth when new evidence warrants it; do not use the initial Tiny label
to keep a risky action compressed. Safe independent work can continue.

[Governance Review](../governance/ai-usage.md) and relevant
[security review](../agent-security/trust-review.md) remain shared checklists, not
extra agents. No automatic approval or orchestration is introduced.
