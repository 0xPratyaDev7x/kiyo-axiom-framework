# Test plan template

Use the [Test procedure](../workflows/test.md) and [mode/safety matrix](../framework/test-mode-safety.md).
A compact chat plan is enough for a small task. Writing this template to a file
needs an authorized destination; it neither grants execution nor installs tooling.

- **Task / mode / scope:** <assess/run/write or explicit phases, requested output,
  root/component, permitted reads/writes/artifacts and exclusions>
- **Requirements / evidence:** <actual requirement/AC or named criterion, relevant
  code/test/Memory observations, known facts versus proposals/open decisions>
- **Strategy / cases:** <selected unit/integration/API/E2E/regression layers and
  reasons; applicable happy/error/boundary/authz/validation inputs and expected results>
- **Project capability / environment:** <observed framework/tool/config version
  when relevant, actual non-production target/data, missing prerequisites>
- **Commands / effects / authority:** <observed command or explicitly proposed
  unrun method, working context, selected scope, script/setup/teardown effects,
  artifact paths, current approval scope or specific missing authority; no secrets>
- **Baseline / required evidence:** <comparable observed baseline or Unknown,
  mandatory checks, real counts/skips/blockers/coverage to capture if available;
  no predicted PASS or made-up percentage>
- **Completion / Memory / next action:** <mode-specific deliverable, actual
  checks required for DONE, scoped Memory Impact, unresolved decision/held action>

| Criterion / source | Existing test evidence or gap | Proposed case / layer | Expected behavior source | Planned method / scope | Authorization or environment gap |
| --- | --- | --- | --- | --- | --- |
| <actual ID or named requirement> | <source inspected, not proof it ran> | <inputs/boundary and test type> | <accepted rule or unresolved choice> | <observed command or proposed method, NOT_RUN> | <specific prerequisite or none within established scope> |

Do not create a new requirement merely to fill a test row. An unsupported E2E
capability is a reported limit; select proportionate other layers without claiming
they satisfy an explicitly mandatory E2E check. Plans and expected outcomes are
not results; record execution separately using the
[Test report](reports/test-report.md).
