# Behavioral evaluation suite

Prompt 25, checked 2026-09-29. **48 host cases: 32 Skill cases (four each) and
16 cross-cutting cases. All 48 are NOT_RUN.** The user explicitly selected
offline suite/protocol work; no host/model, paid API or external quota was used.

- [Case index](CATALOG.md) and [canonical case data](catalog.json): exact user
  inputs, requirement/control IDs, activation, fixture, allowed/forbidden
  effects, operator-only expected criteria and evidence/limitation references.
- [Synthetic fixture bundles](fixtures.json): common accepted-policy envelope
  plus one selected bundle; no real secrets, PII, endpoints or organizations.
- [Manual protocol](protocol.md), [metrics/grading](metrics-and-grading.md) and
  [blank observation form](observation-template.json).
- [Observed-result ledger](../../../docs/evidence/behavioral/observations.json):
  separate from expected criteria, with unknown host/model/settings and no
  fabricated outputs/actions/diffs.
- [Actual offline evidence](../../../docs/evidence/behavioral/validation-report.md)
  and [defect/gate register](../../../docs/evidence/behavioral/defects.md).

[runner.py](runner.py) is a developer-only fixture/snapshot helper, not a Kiyo
initializer, agent launcher, policy engine or consumer dependency. It creates
fresh directories outside the repository and copies all 105 canonical files
with their relative structure. It never installs packages, starts a model,
executes fixture scripts, initializes Git, deletes or cleans directories.

## Offline validation

```powershell
python -B tests/behavioral/evaluation/test_suite.py --report docs/evidence/behavioral/harness-results-new.json
```

Choose a fresh filename. [test_suite.py](test_suite.py) validates the 48-case
inventory and real control/requirement IDs, materializes all 48 fixtures, checks
snapshot stability, parses fixture Python without executing it, rejects unsafe
paths/overwrites, detects byte/timestamp/framework changes, retains captures,
exercises the actual helper CLI, and ensures results/metrics remain unmeasured.
The test includes intentionally planted **harness** mutations, not agent actions.

Passing these developer tests proves only the helper's checked properties.
It is not routing accuracy, behavior compliance, secret protection or live-host
acceptance. The P24 static results and earlier bounded source trials remain
historical independent evidence; none is relabeled as one of these 48 host runs.

## Activation boundary

Most cases explicitly select a source entry. Cases marked automatic test
**skill selection after explicitly supplied Core**, not native automatic Core
loading. The fixture envelope does not name the expected Skill for those cases.
Record actual selection and resource reads if a later host runs. No universal
slash syntax, installed-plugin availability or always-on behavior is asserted.

The source-guided protocol can be used in an authorized real coding host later.
Its results must identify actual host/model/settings and loading evidence.
Native installation, namespace, cached resources and automatic loading need
separate Prompt 26 evidence; this suite does not resolve the Codex IDE plugin gap.

