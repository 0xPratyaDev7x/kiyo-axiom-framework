# Optional governance presets

These are **unadopted examples**, not organization policy, business classifications
or native permission settings. Do not pick one from an industry, company name,
account tier or repository layout. An authorized user may select a preference
for the actual scope; accepted higher-authority restrictions still apply.
Record selection/source/status in the existing
[project configuration](../framework/project-configuration.md). NONE selected is valid.

| Preset | Proposed treatment when selected within authority | Boundaries |
| --- | --- | --- |
| Balanced engineering | Use ordinary requested bounded code/docs/tests changes with applicable checks; reuse existing scoped authorization. Apply policy-defined sensitive-action approvals and restricted-operation rules. | No extra approval ceremony for a tiny authorized fix; no automatic commit/push/deploy, provider selection or dependency installation beyond scope. |
| Stricter approval | In addition to baseline controls, propose an explicit scoped approval checkpoint before new dependency adoption/install, public API/schema behavior changes or changes to data destinations. Prepare a reviewable delta first; reuse an already matching approval. | Exact classes/exceptions must be accepted for the project. Existing sensitive/prohibited operations stay controlled. Not every read, formatting correction or test source edit automatically requires another approval. |
| Observe/read-only | Limit the task to authorized relevant inspection and chat findings. No source/config/Memory/report writes, installation or execution of project test/build scripts. | Native metadata/file reads still need authority and data handling. Read-only can expose protected data. A later requested mode transition requires reassessment and applicable scope approval. |

The Stricter example distinguishes drafting a migration file from executing a
database operation. Review proposed schema behavior in the draft; live execution
requires a separate actual target/effects assessment. No preset permits production
resources to make checks pass or overrides an organization prohibition.

## Three separate decisions

| Concept | Question | Evidence |
| --- | --- | --- |
| Preset | Which optional continuing preferences were actually selected for this project/component? | Existing config plus source, accepted scope/status and relevant refinements |
| G1–G4 | What advisory action mode/control treatment fits this particular task? | [Governance levels](governance-levels.md), intent, actual effects and policy |
| Risk | What are the concrete consequences and uncertainties? | [Eight risk dimensions](risk-assessment.md), LOW/MEDIUM/HIGH/CRITICAL or unassigned Unknown |

No automatic mapping exists. Under Balanced, an authorized small edit can be G2
with LOW risk, while reading confidential material can be G1 with HIGH risk or
DENY. Observe selection does not make a sensitive read safe. A G4 operation
remains restricted even if someone selects Balanced and types “approved”.

Select only after discovering existing accepted policy and current intent.
Changing a preset cannot bypass the [policy change process](policy-resolution.md#policy-changes-and-exceptions).
A config selection does not enable native tools/network, adopt a company's rules,
authorize all future tasks or change an account/model. No preset is chosen by
Kiyo automatically and no preset selection is mandatory before routine work.
