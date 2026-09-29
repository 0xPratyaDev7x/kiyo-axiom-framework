# Governance levels

## KIYO-GOV-002 — Keep Kiyo modes separate from risk and permissions

**G1–G4 are Kiyo's advisory governance model.** They are not ISO/NIST levels,
native permission settings, certifications or a linear risk score. They describe
the allowed workflow under applicable authority; the host still controls access.
Use [risk assessment](risk-assessment.md) independently for each concrete action.

| Mode | Intended scope | Boundary |
| --- | --- | --- |
| G1 Observe | Read/analyze information already authorized for the task | No file changes, including memory/index/report files. A read may expose sensitive information and still be forbidden. |
| G2 Assist | Make ordinary requested code/docs/tests changes and perform permitted verification | Remain within the actual request and inspected side effects; a test command is not automatically safe. Do not add unnecessary approval questions for ordinary scoped work. |
| G3 Controlled | Handle policy-defined sensitive changes with scoped human approval | Establish actual applicable policy and valid approval before dependent action; reuse approval if it already covers the work. |
| G4 Restricted | Production, destructive or security-critical execution | Do not execute by default. Confirmation alone is insufficient; an organization prohibition or host denial can forbid execution despite confirmation. |

Select the applicable mode from accepted policy and requested effects; do not
silently promote a review into edits or downgrade a required restriction to make
execution possible. If no mode was explicitly named, explain the applicable
Kiyo default briefly when it matters; do not claim the user selected it. A
material scope transition needs the authority required for its new effects,
not necessarily another question when that authority was already explicit.

Within G4, preparatory analysis or a draft can be separately allowed at its own
scope. Execution remains held unless the applicable policy expressly permits
an exception/process, the authorized human's scoped approval and required
operational safeguards are evidenced, the target is verified, and native access
allows it. A valid prohibition remains a denial until changed through its real
authority; do not treat “approved” as that policy change.

An existing G1 restriction does not become G2 when a bug is discovered. A G2
task can encounter a G3-sensitive source change or a G4 execution step; stop
only that step and reassess. Drafting a migration is distinct from applying it.
Changing an auth handler is distinct from executing a live security-control change.

Examples of independence: an authorized public-source read can be G1/LOW;
attempting to disclose credentials can be G1/CRITICAL and denied. A bounded,
isolated non-destructive test migration may be G3/MEDIUM under an accepted policy.
No mapping such as G1=LOW or G4=CRITICAL is automatic. The
[examples](decision-examples.md) state their synthetic conditions explicitly.
