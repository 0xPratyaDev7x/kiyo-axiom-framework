# Change scope checklist

Use for an authorized edit or when reviewing a proposed diff. This operationalizes
the Core minimum-change rule; it does not create write permission.

## KIYO-ENG-007 — Preserve human work and keep the diff necessary

1. Establish affected behavior/files, allowed mutation and known exclusions.
   Inspect working tree, staged changes and relevant current content if Git is
   available; without Git inspect the relevant files and report that limitation.
   Existing changes are not disposable.
2. Identify the smallest coherent change that satisfies the request and safety
   requirements. Retain naming, formatting and public contracts unless the task
   requires changing them.
3. Re-read the affected content before writing. Use focused edits; preserve
   concurrent human work and reconcile or stop on overlapping changes. Do not
   reset, clean, stash, overwrite or silently revert another person's edits.
4. Do not broadly format, rename, relocate architecture, upgrade packages or
   remove adjacent code because a tool suggests it. Inspect formatter/generator
   side effects before running them. A required dependency/contract change needs
   explicit justification and reassessment, not concealment in a tiny fix.
5. Review the actual final diff, including new/untracked files. Identify
   unintended changes and correct only changes demonstrably made by this task;
   preserve uncertain/user edits and surface conflicts.
6. Run applicable checks and assess
   [Memory Impact](../memory-specification.md#kiyo-mem-006--memory-impact-at-closure).
   No memory delta means no timestamp touch.

An insecure existing pattern should be reported with evidence and a scoped safe
alternative, not copied to minimize lines. If resolving it expands scope, use
[replanning and recovery](../../workflows/repair-and-handoff.md) and
[approval scope](../../governance/human-approval.md); retain independent authorized
work where safe. Read-only findings never authorize applying the proposed diff.

Completion evidence: affected files, why the diff is needed, preserved/pre-existing
changes, actual checks, deferred findings and memory impact. No unrelated
refactor, dependency upgrade or project-memory initialization is implied.
