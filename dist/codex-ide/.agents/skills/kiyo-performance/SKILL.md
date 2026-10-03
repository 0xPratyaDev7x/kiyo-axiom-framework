---
name: kiyo-performance
description: Investigate software performance with measured evidence or clearly labeled static risks. Use for slow APIs or queries, N+1, CPU, memory/allocation/GC, I/O, network/external APIs, concurrency/blocking, throughput/latency, frontend performance or before/after comparisons. Analysis does not authorize benchmarks, load tests, tool installation or production code changes.
---

# Performance

Logical ID: **kiyo.performance**. Canonical name: performance. Benchmarking,
profiling, database, API and frontend investigation belong to this one public
skill, not separate skills. Platform-only metadata belongs in overlays.

Read [KIYO.md](./references/kiyo/KIYO.md) and its bootstrap before workflow actions unless
already read and unchanged. Follow the
[shared Performance procedure](./references/kiyo/workflows/performance.md). Use
[read-only flow](./references/kiyo/workflows/read-only-flow.md) for inspection; explicitly
authorized measurement is a separate EXECUTE action. Resolve references from
this installed file's actual location; missing resources hold dependent work.

## Scope and authority

Establish the affected operation/component, symptom, workload, environment,
available evidence and requested comparison. Inspect relevant authorized code,
traces, metrics or supplied results before asking about material gaps. Do not
assume a stack, deployment, traffic pattern, target latency or available tooling.
Requests such as “why is it slow?”, “find the bottleneck”, “check this query” or
“compare performance before/after” begin with bounded analysis.

Analysis returns chat findings; no implicit source, test, config, Memory or
report-file writes. Finding a bottleneck does not authorize changing production
code. Optimization requires separately established implementation scope,
preserves functional behavior and uses the project's existing patterns.

Benchmark, profiling and load-test commands are **EXECUTE** actions, even when
described as diagnostic. Inspect the actual target/environment and effects,
including data writes, network calls, resource pressure, sensitive trace data
and cleanup. Reuse valid matching authorization; obtain only missing execution
scope before running. Never implicitly load test production or install tooling
without authorization. Unknown isolation or host denial holds dependent execution.

## Evidence and investigation

**Measure → Localize → Hypothesize → Validate → Recommend → Verify**

No measurement = no proven performance claim. Static inspection can identify
risks or observations, never prove a performance bottleneck. Do not invent
benchmark results, latency, throughput, memory usage or any other metric.

Label each material claim, independently of check/task completion status:

| Evidence status | Meaning |
| --- | --- |
| MEASURED | Actual measurement supports this claim within its recorded workload/environment; cite the result and provenance. |
| OBSERVED | Directly inspected code, configuration or event; its performance impact is not established by inspection alone. |
| INFERRED | Reasoned conclusion from cited evidence; state assumptions and missing causal proof. |
| HYPOTHESIZED | Candidate explanation requiring a discriminating measurement. |
| NOT_MEASURED | The needed metric or comparable baseline was not collected. |
| UNKNOWN | Evidence is absent, inaccessible, conflicting or insufficient to decide. |

Use the shared procedure to choose the smallest relevant measurement, localize
cost and test competing explanations. If execution is unavailable, deliver
static observations, hypotheses and a measurement plan with explicit limits;
do not manufacture a completed measurement cycle.

Recommend the smallest supported change with verification criteria and trade-offs
across latency, throughput, CPU, memory, consistency and maintainability. Never
claim an improvement without comparable before/after evidence. A faster result
with changed output, errors or consistency does not establish a valid optimization.

## Report and complete

Use the [Performance report](./references/kiyo/templates/reports/performance-report.md) in
chat at proportional depth: findings, supporting evidence, evidence status,
bottleneck or suspected bottleneck, recommendation, and next measurement or
verification. Distinguish supplied results from commands actually executed.
Keep raw sensitive traces out of the response.

Record checks under the [Evidence Contract](./references/kiyo/framework/evidence-contract.md),
assess Memory Impact without implicit writes and close under
[Definition of Done](./references/kiyo/framework/definition-of-done.md). DONE means the
agreed investigation was delivered, not that performance improved or source
was repaired. Missing mandatory measurement/comparison remains partial or blocked.

## Codex native guidance

For Codex invocation or an authorized project bootstrap, read the conditional
[Codex activation reference](./references/codex/activation.md).
