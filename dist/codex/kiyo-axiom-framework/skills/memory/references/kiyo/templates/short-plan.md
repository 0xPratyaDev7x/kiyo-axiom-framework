# Short implementation plan

Use with [implementation flow](../workflows/implement-flow.md) and
[adaptive depth](../workflows/adaptive-flow.md). This is a neutral thinking/output
aid, not an approval artifact, new workflow or required disk file. Chat is default;
file persistence needs actual authorized path/scope. Preserve existing project
planning conventions and user choices.

Tiny work may compress the fields into one scope/risk/check sentence. Normal work
uses a few concrete steps. High-impact work needs the actual dimensions and any
missing decision under [Governance Review](../governance/ai-usage.md); do not enlarge
a plan merely to appear thorough.

Copy only the artifact body if needed; fill observed values or explicit unknowns.
Keep references relative to a declared project/component or output path, never
the plugin cache. No developer-project facts, guessed IDs or test results belong here.

## Artifact body

```markdown
- Intent / acceptance / scope: <actual requested behavior, criteria and excluded effects>
- Baseline / evidence: <observed root/worktree/branch/revision/dirty state where available; human edits, relevant Memory and current evidence; limitations>
- Minimal change: <necessary files/areas and short ordered actions using existing safe patterns; no speculative abstraction or package>
- Impact / authority: <dependencies/schema/API/security/data/tool effects, target/environment, risk and applicable policy; valid existing scope or concrete missing approval>
- Verification: <applicable checks and why, commands/methods to inspect before execution, baseline comparison and environment prerequisites; planned, not passed>
- Memory / completion: <anticipated assessment/sync boundary, required DoD evidence and report; no assumption that writes are authorized>
- Replan / recovery: <material scope/target/effect changes that require reassessment; known reversibility limits and bounded repair/handoff>
```

A plan is neither a human approval nor permission to run a command. Reuse current
matching authorization; ask only a blocking choice/approval after permitted
discovery. State concrete effects and alternatives using the existing
[approval template](reports/approval-request.md) only when approval is missing.

Before execution, resolve actual targets and relevant script effects; an unverified
test DB is not an alternative to a missing environment. Do not use production to
obtain a green check. Safe baseline collection is useful, not a reason to disturb
human changes or install tools without authority.

Use [repair/handoff](../workflows/repair-and-handoff.md) for failure attribution,
the default two unsuccessful-cycle bound and resume facts. Report actual results
through the existing [engineering](reports/engineering-report.md) or
[compact](reports/compact-task-report.md) template. Do not duplicate execution
results or private reasoning in a planning record.
