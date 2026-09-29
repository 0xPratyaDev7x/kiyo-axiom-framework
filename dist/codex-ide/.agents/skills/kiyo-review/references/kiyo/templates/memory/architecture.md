# Architecture context — template

Authoring guidance: follow the [shared Memory specification](../../framework/memory-specification.md)
and [authorized lifecycle](../../workflows/memory-lifecycle.md). Keep observed implementation separate from approved intended design. A package/folder name is a clue, not architecture evidence; link actual usage and decision records.

Use only the fenced artifact body in the consumer project, preserving existing
paths/IDs. Replace prompts from evidence, omit unused records, and remove guidance
comments. UNKNOWN is honest missing information; it is not a completed entry.
Dates belong to the individual claim. No whole-file last_verified stamp.

## Artifact body

```markdown
# Architecture context

## <stable-id> — <short title>

- id: <existing ID or checked unused MEM-TOPIC-NNNN>
- record_type: <observation | proposal | decision>
- status: <status valid for record_type>
- statement: <one observed structural fact or one evidenced design decision>
- source: <kind; repository-relative path; symbol/section/line, or UNKNOWN>
- observed_date: UNKNOWN
- last_modified: UNKNOWN
- last_verified: UNKNOWN
- verification_status: UNVERIFIED
- verification_scope: <claim and evidence checked; limits and uninspected areas>
- uncertainty: <specific missing, partial or conflicting evidence>
- repository_context: <repository/worktree key; component; branch and dirty state, or UNKNOWN>
- git_revision: <actual observed revision with scope; UNKNOWN; or confirmed non-Git NOT_APPLICABLE>

<!-- Add approval_source, approver (non-PII role/record reference), approval_scope
and approval_date only where actual evidence exists. No assumed approver/approval.
Optional related_ids/supersedes must refer to actual records. Remove unused prompts. -->

### Evidence notes

<Concise supporting evidence and limitations; no secrets, PII, raw logs or private reasoning.>

```

