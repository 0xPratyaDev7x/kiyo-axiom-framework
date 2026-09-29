# Native integration protocols

Developer/operator material only; never packaged. [cases.json](cases.json)
defines twelve independent checks for each of six targets. Expected behavior
lives here; actual observations live under
[docs/evidence/live](../../docs/evidence/live/README.md).

Use [reproduction](../../docs/compatibility/live-reproduction-guide.md) for
disposable prerequisites, command provenance and fixture preparation.
Use [matrix](../../docs/compatibility/live-test-matrix.md) for actual statuses.
No test here launches a paid agent automatically. The user selected no-quota
native checks for Prompt 26; later model cases require fresh scoped authority.

Audit evidence records without launching any native host:

```powershell
python -B tests/live/check_records.py --report docs/evidence/live/record-audit-new.json
```

Use a fresh output filename. This P26 baseline-specific audit checks recorded
outcomes, links, unchanged package hashes and build-state consistency. It does
not rerun integration or establish that an agent follows the instructions.

P25 fixture IDs resolve in [catalog](../behavioral/evaluation/catalog.json);
reuse only their synthetic workspace data and exact case inputs. The P25
source-guided invocation envelope supplies Core and is **not** a native
activation test. Operator expectations/baselines stay outside agent context.
