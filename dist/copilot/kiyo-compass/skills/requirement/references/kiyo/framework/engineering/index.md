# Engineering reference selection

Use after the [Core loading procedure](../context-loading.md), within the
selected skill's authorized mode. These are shared Markdown checklists, not a
router engine, compiler, automatic upgrade policy or extra public skills.
A checklist cannot turn Review into Implement or authorize command execution.

| Task evidence / question | Load only the relevant reference |
| --- | --- |
| Behavior, scope or acceptance is unclear; Requirement task | [Requirements](requirements.md) |
| Boundary, public contract or architectural decision is affected | [Architecture](architecture.md) |
| Code is being written or inspected | Relevant rows of [Coding](coding.md) |
| Choosing or reporting verification; Test assess or execute | [Testing](testing.md) |
| A material quality attribute is affected | Relevant rows of [Quality](quality.md) |
| A proposed diff may exceed scope or overlap human edits | [Change scope](change-scope.md) |
| Evidence establishes the affected .NET component | [.NET](../../profiles/dotnet.md) |
| Evidence establishes the affected Angular component | [Angular](../../profiles/angular.md) |
| Evidence establishes the affected Python component | [Python](../../profiles/python.md) |
| Evidence establishes PostgreSQL persistence work | [PostgreSQL](../../profiles/postgresql.md) |
| A different stack or accepted company supplement is needed | [Profile extension contract](../../profiles/extension-contract.md) |
| Asked why a standard concept informs a rule | [Concept-to-evidence mapping](standards-mapping.md) |

Load the smallest relevant set, per component in a mixed repository. Do not load
four profiles from folder names, package names or user-agent/model identity.
Missing configuration means Unknown, not a default stack. A documentation typo
normally needs only the compact scope/evidence checks already in Core.

Read-only analysis selects checks but does not run mutating tests or write
requirements, ADRs, code or memory. For writes, use the existing
[implementation flow](../../workflows/implement-flow.md); for analysis use
[read-only flow](../../workflows/read-only-flow.md). Consult
[application security](../../agent-security/application-security.md) only for
affected security concerns; it remains distinct from skill/agent security.

All operational references resolve relative to this installed file and are part
of the same payload snapshot. External citations in the mapping/profiles are
optional provenance, not mandatory online loads. No consumer generator or
developer checkout is needed. Native packages and live profile behavior still
require their own evidence; authored guidance does not prove host enforcement.
