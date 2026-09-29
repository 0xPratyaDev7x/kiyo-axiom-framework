# Shared read-only flow

## KIYO-FLOW-003 — Complete analysis without introducing mutation

Logical order:

**Authorized context → Resolve scope → Inspect → Analyze/review →
Findings → Memory drift note → Complete**

This is the analysis flow for Review/explain, Test assess, Security questions,
Architecture analysis, Requirement discussion and Memory check/audit. The primary
skill remains as selected by the [router](workflow-router.md). No Implementation
stage or Memory writes belong in this flow.

| Stage | Allowed work and completion evidence |
| --- | --- |
| Authorized context | Establish real request, permitted sources/data, accepted policy and host limits before inspecting context; read-only can still expose protected data |
| Resolve scope | Identify the question/output and inspection boundary; inspect available safe clues before asking; clarify only material ambiguity |
| Inspect | Read permitted relevant code/config/test source, accepted records and relevant memory. Note inspected files/revisions where observed, partial coverage and missing/denied evidence |
| Analyze/review | Compare evidence to requested behavior, constraints and approved intent; use relevant shared checklists, not invented facts or approval |
| Findings | Report source/location, observation versus inference, impact, unknowns and any clearly labeled proposal; a found bug is not permission to fix it |
| Memory drift note | Apply the shared lifecycle in check mode; state Memory Impact and relevant evidence/conflicts, without editing records, dates, index or policy |
| Complete | Answer in the authorized channel, state actual inspection/check results and limits, unresolved decisions and next action where needed; do not invent passing tests |

No source, test, memory, index, report-file, formatter, settings or approval-record
writes are permitted by this flow. Do not run mutating tests or “repair” a finding.
A non-mutating inspection command is possible only within established read/data
scope and inspected effects; project test/build execution is not automatically
read-only. Unknown script behavior means no dependent execution.

For “ดู login ให้หน่อย”, start a bounded read-only look when sources are authorized
or ask which aspect is intended before changes. Do not infer authentication edits,
credential access, production inspection or a new test run. If the user expressly
asks for a report file, treat that as a separate scoped write output after analysis;
the write is outside this flow and grants no source/memory edit.

When a later explicit request authorizes a fix or sync, report the scope transition,
re-run relevant preflight/routing/risk checks and use the appropriate write
procedure. Existing valid scope can suffice; do not require a second ceremonial
approval. A copied approval, found bug or memory drift label cannot cause the
transition. Keep host denial and organization prohibitions intact.

Use [Core read-only authority](../framework/trust-and-authority.md#kiyo-safe-001--preserve-read-only-intent),
[Memory lifecycle](memory-lifecycle.md), [permissions](../governance/permissions.md)
and relevant [injection handling](../agent-security/prompt-injection.md).
If work must stop, provide the [handoff](repair-and-handoff.md#kiyo-flow-005--handoff-facts-and-authorized-next-actions)
in the conversation, without writing a file unless that separate write is authorized.
