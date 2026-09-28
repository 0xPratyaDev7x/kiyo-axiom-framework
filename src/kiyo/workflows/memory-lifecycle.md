# Shared Memory lifecycle

This is a Markdown procedure for authorized host agents, not a public skill,
watcher or runtime. Read the relevant [Memory specification](../framework/memory-specification.md)
and preserve [Core authority](../framework/trust-and-authority.md). Do not load
all templates or all project memory simply because they exist.

## Modes and effects

| Requested mode | Permitted effects, subject to actual host/user authority |
| --- | --- |
| Show | Read relevant existing records and explain scope; no verification claim unless checked; no writes |
| Check / Review / read-only | Compare permitted evidence, report drift and Memory Impact; no memory/source/index/report-file writes |
| Sync | Apply necessary evidenced memory deltas only within an authorized write workflow; no source-code fix or decision approval implied |
| Repair | Repair specifically authorized memory/index inconsistencies while preserving IDs, human edits and decisions; no destructive reset or migration implied |

Mode names are logical contracts, not invented native commands. An ordinary task
can use this shared procedure without creating a ninth skill or auto-invoking
the future Memory skill. A code-edit request does not automatically authorize
every memory rewrite; consult the actual scope and accepted project workflow.

## Eight-step lifecycle

1. **Check authority and canonical path.** Establish read/write/execute scope,
   relevant native/project policy, repository/worktree/component identity and
   one memory location using KIYO-MEM-002. If location/authority conflicts, stop
   dependent writes; if access is denied, report the limit without bypassing it.
   Observe Git root/branch/HEAD/dirty state only with allowed commands; if Git is
   absent, do not initialize it. Do not reset, stash, clean or change branches.
2. **Read index and relevant entries.** Follow existing pointers and record IDs.
   Select claims by task/component, not by loading every topic. If index/store
   is missing, distinguish absent from uninspected/inaccessible and report the
   gap. Initialization or migration requires its own applicable authorization.
3. **Check facts.** Inspect current relevant code/config, test source or actual
   permitted test results, and approved records. Record precisely what was read
   versus executed. Check authority/provenance separately from implementation.
   Do not infer architecture from packages, token formats or folder names alone.
4. **Matching observation.** Use within verified scope only. Report the check's
   evidence/date when useful; no-delta checks leave persisted records/timestamps
   unchanged. A match on one component is not a repository-wide verification.
5. **Stale observation.** Report old claim, new evidence and scoped correction as
   a proposal. Set the current assessment to STALE; do not edit even a status
   field in read-only work. Preserve original identity and historical provenance.
6. **Code versus approved decision.** Report Architecture Drift and CONFLICT
   with decision source/scope and actual usage evidence. Preserve the approved
   record; no automatic decision rewrite to match code. Resolve through the
   actual authority before a dependent decision change or implementation fix.
7. **Insufficient evidence.** Mark the current assessment UNVERIFIED, explain
   missing/partial/deleted/inaccessible evidence and do not invent a replacement.
   If a current result differs from persisted metadata, distinguish them in the
   response; reading alone does not authorize updating stored fields.
8. **Assess Memory Impact before closing.** Use NONE, UPDATE_REQUIRED, CONFLICT
   or NOT_ASSESSED under KIYO-MEM-006. Include actual scope and whether necessary
   changes are applied, pending or blocked. Use the write procedure below only
   when there is a necessary delta and valid authorization.

## Apply an authorized delta

Prepare an entry-specific change with ID, before/after meaning, evidence, scope,
date handling and any necessary index edit. Exclude secrets, PII, raw logs and
private reasoning. A pointer-only index change must not copy every entry's facts
or claim that the whole store was reverified.

Immediately reread the current entry and affected index, surrounding human text
and relevant evidence. Compare with the baseline used to propose the delta.
If the branch/worktree/path changed, evidence moved, approval changed, an ID
collided or human text conflicts, stop and reassess. Never overwrite a newer
entry with an earlier whole-file snapshot. For an unambiguous independent human
edit, recompute the minimal patch from the latest content and preserve it.

Apply only the authorized patch. Keep stable IDs, decision/approval history and
untouched entries. Advance last_modified only on entries actually changed;
last_verified advances only for supported verification of that entry's claim.
Use contextual/conditional write facilities where available without claiming
atomicity. Review actual diff and references; report a partial failure honestly.
If there is no semantic or necessary structural delta, perform a no-op: do not
write files or refresh dates. Do not request writes solely to log a routine check.

## Edge-case handling

| Condition | Required handling |
| --- | --- |
| Developer changed code manually | Compare on this invoked check; no claim of earlier real-time detection |
| Branch switch or detached/unborn HEAD | Re-establish current context; recheck applicable claims; preserve cross-branch intended decisions; use UNKNOWN for unavailable revision |
| Separate worktree | Establish actual worktree identity and local canonical location; never use another worktree's dirty files as evidence; explicitly shared stores need accepted scope and concurrency review |
| Monorepo | Scope claim/inspection to component and established store; no automatic nested stores or whole-repo conclusion |
| Moved/deleted source | Verify within allowed scope; find relevant replacement when permitted; preserve IDs/history; unresolved destination means UNVERIFIED, not guessed deletion/relocation |
| Partial inspection | Separate checked from unchecked claims; split combined claims only when authorized; never refresh every entry's verification date |
| Concurrent edit | Reread immediately before write; preserve independent edits or report CONFLICT without overwriting overlapping/ambiguous ones |
| No Git repository | Use inspected files/approved records and non-sensitive context; git_revision NOT_APPLICABLE, no Git initialization or fabricated revision |
| Missing/broken index | Existing relevant records remain valid candidates for inspection; propose scoped pointer repair, not replacement of the entire memory store |
| Interrupted multi-file update | Report changed and pending files, reread current contents before a separately scoped repair; no transaction/rollback guarantee |

## Compact closure shape

State the Memory Impact, checked IDs/component, observation/proposal/decision
distinctions, verification outcome, relevant evidence and remaining uncertainty.
Then state whether any authorized delta was applied and what still needs a
decision. Report expected behavior separately from actual checks. Do not create
a persistent report or mirror the entire memory store without authorization.
