# Shared Performance procedure

This is a procedure for the single public Performance skill. Analysis is
[read-only](read-only-flow.md); measurement is an EXECUTE action under actual
[permissions](../governance/permissions.md). Neither findings nor this procedure
grant implementation, installation or production access.

## Measure → Localize → Hypothesize → Validate → Recommend → Verify

1. **Measure:** define the operation, symptom, relevant metric and comparison
   question. Inspect existing authorized telemetry/results first. Record source,
   revision/build when known, timestamp, environment/hardware/runtime, workload,
   dataset/size, concurrency, method/command, units, sample count/duration and
   warm-up/cache state at useful depth. Unknown fields remain unknown. Supplied
   measurements are attributed, not claimed as independently executed. Without
   measurements, report NOT_MEASURED and propose the smallest useful check.
2. **Localize:** separate end-to-end time from component cost, CPU work from
   waiting, and individual latency from throughput. Use relevant spans, profiles,
   query plans or counters to locate where measured cost accumulates. Correlation
   alone does not establish causation; a slow dependency or expensive-looking
   loop is a suspected bottleneck until relevant evidence supports attribution.
3. **Hypothesize:** state a small number of explanations tied to inspected
   evidence, their alternatives and what observation would disconfirm each.
   Keep static observations separate from inferred impact and hypotheses.
4. **Validate:** choose the smallest discriminating experiment using available
   tools. Before any execution, inspect command/scripts, target, isolation, data,
   network/write effects, overhead, resource limits, stop conditions and cleanup.
   Obtain only missing authority and respect host restrictions. Do not silently
   install a profiler, run project code, hit production or widen test traffic.
   Profiling overhead and noisy/shared environments limit conclusions. An
   EXPLAIN ANALYZE or equivalent may execute the query and produce side effects;
   do not treat its name as read-only permission.
5. **Recommend:** rank proposals by supported impact and cost, with functional
   constraints and latency/throughput/CPU/memory/consistency/maintainability
   trade-offs. Preserve response/output, errors, ordering, transaction and
   consistency contracts. A finding is a proposal, not authority to optimize
   source, schema/indexes, infrastructure or production configuration.
6. **Verify:** only after a separately authorized change or supplied comparison,
   compare equivalent workload/data, environment, tooling, concurrency,
   warm-up/cache and measurement boundaries. Repeat enough to expose variability;
   report sample size/distribution and errors, not only the best run. Distinguish
   cache-cold/warm results and profiler overhead. State remaining confounders.
   Confirm functional behavior with relevant authorized checks. Missing or
   incomparable baseline means no proven improvement; report what is still needed.

## Choose evidence for the symptom

Use only relevant rows; these are measurement options, not commands to execute
automatically or a demand to collect every metric.

| Area | Useful evidence and localization questions |
| --- | --- |
| API / throughput / latency | End-to-end and span timings, latency distribution such as p50/p95/p99 when sampled, request rate, concurrency, saturation and error rate; distinguish service time from queue/wait time. |
| Database / query / N+1 | Query count per operation and timings, actual plans/row counts where authorized, scans, locks/waits and round trips; a loop issuing queries is an OBSERVED N+1 risk until runtime evidence establishes repeated cost. |
| CPU / memory / allocation / GC | CPU samples, hot paths, allocation rate, retained/live heap, GC frequency/pause time; separate transient allocations from retained growth and CPU work from waiting. |
| I/O / network / external API | Bytes, calls, disk/network waits, dependency spans, retries, connection pools and timeout behavior; separate remote time from local overhead. |
| Concurrency / blocking | Queue length, contention/lock wait, thread or event-loop blocking, pool saturation, scheduling and concurrency level; avoid assuming that more parallelism improves throughput. |
| Frontend | Actual user/device/browser conditions, navigation/render timings, main-thread tasks, network waterfall, bundle/asset sizes and interaction evidence; separate lab measurements from field data. |

Use the evidence statuses defined in the Performance entry. Numeric deltas require cited, comparable
measurements and units; missing data never becomes an estimated benchmark.
Return the [compact report](../templates/reports/performance-report.md), including
limitations, check execution status and next action. Assess Memory Impact without
writes; completing analysis does not prove improved application performance.
