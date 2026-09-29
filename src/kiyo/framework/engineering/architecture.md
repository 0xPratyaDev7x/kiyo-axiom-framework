# Architecture checklist

Load when a change affects dependencies, public interfaces, deployment boundaries
or an architectural decision. Do not turn every edit into architecture work.

## KIYO-ENG-003 — Preserve safe boundaries and explicit design intent

1. Inspect the affected implementation and nearby safe examples, configuration,
   dependencies, tests and accepted decisions. Identify the actual architecture;
   a folder or package name alone is insufficient evidence.
2. Trace the relevant dependency direction and data/control flow. Respect the
   project's established boundaries and ownership. Do not introduce a new layer,
   ORM, CQRS, service split or framework merely because it is a preferred pattern.
3. Check public contract consumers: signatures, API behavior, events, schemas,
   persisted formats and supported versions where applicable. State intended
   compatibility and evidence; do not invent an endpoint or claim production
   consumers are known from local source alone.
4. Prefer the smallest safe change that fits those boundaries. If an existing
   pattern is insecure, report the concrete issue and propose a scoped safer
   alternative; do not reproduce it for consistency or rewrite adjacent systems.
5. When a material tradeoff, boundary or approved decision must change, prepare
   an ADR proposal using the project's convention: context/evidence, options,
   proposed decision, consequences, compatibility and verification. Preserve
   existing ADR IDs/history and label the new decision Proposed until real approval.
6. Apply [risk and governance](../../governance/risk-assessment.md) and scoped
   approval where required. A requested bug fix is not a modernization mandate.

An approved Mapperly decision plus observed AutoMapper usage is Architecture
Drift: cite both, report the conflict and seek the needed decision. Do not edit
the approved record to match the code or migrate libraries silently.

Completion evidence: the affected boundary and consumers inspected, the chosen
minimal approach, relevant contract checks, any proposed ADR and unresolved
decisions. State partial inspection and untested consumers. For read-only
architecture work, return analysis/proposals without implementation or memory
writes. Follow [Change scope](change-scope.md) for authorized edits and the
[Memory lifecycle](../../workflows/memory-lifecycle.md) for drift handling.
