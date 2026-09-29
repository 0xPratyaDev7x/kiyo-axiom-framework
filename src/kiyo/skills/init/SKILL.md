---
name: init
description: Onboard Kiyo to a repository, perform initial project analysis, create or incrementally update Project Memory, and inspect setup readiness when the user requests initialization or a setup preview. Do not use merely because a user adds a feature or fixes a bug.
---

# Init

Logical ID: **kiyo.init**. Canonical name: init. This ID is not a universal native
command; host invocation/metadata belongs to the applicable overlay.

Before workflow actions read [KIYO.md](../../KIYO.md) and its bootstrap, unless
already read and unchanged. Then use the [Init procedure](../../workflows/init.md).
Resolve these links from this file, not the shell directory. If a required
resource is missing, report the affected limitation and hold dependent actions.

## Intent and inputs

Use for requested Kiyo onboarding, initial repository analysis, Project Memory
creation/update or setup-readiness inspection. A feature request, ordinary bug
fix or absent memory alone does not authorize Init. Report an explicit
skill/request mismatch; do not silently turn a feature into onboarding.

Inputs: the project root (or an unambiguous observed workspace root), the user's
initialize/preview intent, and optional profile/governance preferences.
Discover available facts before asking for a material missing root, scope or
authority decision. Preferences are not evidence of the actual stack or accepted
organization policy.

## Mode and access contract

| Mode / access | Bound |
| --- | --- |
| Preview / readiness / initial analysis | Authorized inspection and chat output only; no source, memory, config, bootstrap or report-file writes. |
| Initialize / incremental update | Write only necessary project-local Memory/config and a needed managed bootstrap within the actual request/approval. An explicit initialize request can already cover the bounded ordinary state writes; do not ask again without a material gap. |
| Read | Applicable instructions, existing Kiyo state and a bounded sample of manifests/docs/representative source/test text; respect data permissions and the discovery budget. |
| Execute | Only inspected non-mutating metadata/file/Git checks within authority. Do not run application build/test/install/migration/deploy scripts to initialize Kiyo. |
| Forbidden writes | Application source, dependencies/manifests/lockfiles, tests, global settings and credentials. No Git initialization, reset/clean/stash, source scaffolding, tool/package installation or runtime component. |

Project config here means Kiyo's local context/preferences, not application
configuration. Init never repairs a discovered application defect. A later
request for such changes is a separate task, not permission to expand this one.

## Procedure and conditional references

Follow [the twelve-step procedure](../../workflows/init.md) for baseline,
existing-state discovery, incremental/no-op decisions, sampling, evidence,
preferences, scoped approvals, state writes, bootstrap and final checks.
Reuse [Memory lifecycle](../../workflows/memory-lifecycle.md) and its record
specification instead of copying long Core rules into this skill.

- For sampling or partial/empty/monorepo discovery, read
  [Init discovery](../../framework/init-discovery.md).
- For bootstrap proposals or activation readiness, read
  [Init activation](../../framework/init-activation.md).
- When local context config is needed, use only the artifact body of the
  [project-context template](../../templates/init/project-context.md).
- For reporting distinctions, consult
  [output examples](../../framework/init-output-examples.md) only when useful.
  They are expected behavior, not actual check results.

## Completion and output

Report an evidence-backed project summary, Unknowns, separate proposals/confirmed
constraints, actual Memory/config/bootstrap changes or no-op, activation readiness
and limitations. Include inspected scope, checks, risk/authority rationale,
Memory Impact, task status and next required action under the shared
[reporting contract](../../framework/reporting-contract.md) and
[Init Definition of Done](../../framework/definition-of-done.md).

Preview completion proves only the bounded assessment. Applied state does not
prove automatic Core loading, native install or production state. If requested
mandatory setup cannot be completed, report partial/blocked/decision-required
scope honestly; do not call a smaller delivered subset the full requested task.
