# Engineering requirement template

Use the [Requirement procedure](../workflows/requirement.md) and
[readiness checklist](../framework/requirement-readiness.md). This is a neutral
field checklist, not a mandated new project format or approved specification.
Chat is default; a disk artifact requires the actual requested/approved path.
Preserve existing IDs, layout and human sections. For a tiny task, compact fields
may share a line if all their meanings remain explicit.

Copy only the fenced artifact body when needed. Fill it from permitted evidence;
remove instructional placeholders. Do not copy this template's package-relative
links. Declare the source-path base in the artifact so references remain usable
after plugin uninstall. No developer-project facts belong in the template.

## Artifact body

```markdown
# <requirement title>

- Requirement ID: <existing ID; otherwise response-local provisional draft label, or evidenced durable allocation>
- Objective: <requested user outcome and source>
- Current problem: <inspected current behavior or attributed reported symptom; evidence and limits>
- Expected behavior: <observable requested behavior; distinguish unaccepted alternatives>
- Scope: <included behavior, actors, component and boundaries>
- Out of scope: <specific excluded changes/effects>
- Business rules: <sourced requirements/accepted constraints, or explicit unresolved choice>
- Acceptance criteria: <stable criterion IDs; observable inputs/preconditions and outcomes; planned check method>
- Validation/error behavior: <relevant valid/invalid/denied/failure cases from evidence or pending decision; do not invent status codes>
- Dependencies: <actual prerequisites/integrations and availability gaps, or non-applicability with reason>
- Security/data impact: <affected access/data/export/retention boundaries and sourced constraints; unknowns visible>
- Technical constraints: <observed versions/contracts/architecture boundaries and scope, or Unknown>
- Open decisions: <blocking choices/gaps, options/tradeoffs and next question/evidence step; or none with basis>
- Evidence references: <actual source locators/sections, inspected scope/date/revision when observed, limitations>

## Origin of statements

- Existing facts: <IDs or field references to inspected observations and separately identified approved intent>
- User requirements: <IDs or field references to actual requests/accepted inputs and their source>
- AI proposals: <unaccepted suggestions/assumptions and impact, or none>
- Unresolved decisions: <references to open choices/missing evidence; avoid duplicating the full text>

## Assessment and delivery

- Evidence path base: <actual repository/component or artifact-relative base; no author-machine/cache path>
- Implementation readiness: <READY_FOR_IMPLEMENTATION / DECISION_REQUIRED / INSUFFICIENT_EVIDENCE; scope, reasons and remaining blockers>
- Task status: <DONE / PARTIALLY COMPLETE / BLOCKED / DECISION REQUIRED; agreed draft/ready-spec/file-delivery scope>
- Actions/files changed: <actual authorized spec path/delta, or none; no implementation>
- Governance/risk rationale: <read/spec-write authority, affected data and applicable policy; no fabricated approval>
- Verification/evidence: <actual check records or locators with scope/status/limits; proposed behavior tests remain NOT_RUN>
- Residual issues: <unresolved scope/evidence/decision limitations>
- Memory Impact: <NONE / UPDATE_REQUIRED / CONFLICT / NOT_ASSESSED; scope and proposed delta; no writes>
- Implementation authorization: <actual separate request/approval scope if present, otherwise not established; never inferred from readiness>
- Next required action: <blocking decision/evidence/path request, or none within this requirement task; stop before implementation>
```

Use [Evidence Contract](../framework/evidence-contract.md) for actual checks, and
the smallest [shared report](../framework/reporting-contract.md) for closure.
A referenced approved record establishes only its real scope; this template does
not create approval, business authority, executed test evidence or a tamper-proof log.
