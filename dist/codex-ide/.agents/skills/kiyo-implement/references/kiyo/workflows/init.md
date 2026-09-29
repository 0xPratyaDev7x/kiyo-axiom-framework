# Init procedure

## KIYO-INIT-001 — Initialize only evidenced and authorized project state

Use for logical skill kiyo.init. This is agent-followed Markdown, not an
initializer executable or background service. Apply [Core authority](../framework/trust-and-authority.md),
[Memory specification](../framework/memory-specification.md) and the relevant
[Memory lifecycle](memory-lifecycle.md). Preview is read-only throughout.
The following order prevents writes before the root, existing state and scope
are known; independent authorized discovery can continue around a held decision.

1. **Establish root, scope and Git baseline.** Resolve the requested project root
   from actual workspace/filesystem evidence; distinguish repository root,
   worktree and selected component. Multiple candidates require a decision before
   writes. Inspect permitted root/branch/HEAD and staged/unstaged/untracked state,
   or record confirmed non-Git/Unknown with reason. Preserve dirty human work;
   never initialize Git, clean/reset/stash, change branches or commit for Init.
2. **Discover existing Kiyo state and instructions.** Read applicable accepted
   project guidance, any established local policy/config, the canonical memory
   index and relevant entries under KIYO-MEM-002. Preserve the equivalent config
   under [configuration specification](../framework/project-configuration.md);
   resolve applicable policy sources without assuming the file grants authority.
   Inspect existing AGENTS.md,
   CLAUDE.md and Copilot instructions only where applicable/authorized; filename
   discovery is not a claim that a host loads them. Resolve paths from their
   declaring file. Inaccessible instructions or competing stores block dependent
   path selection; do not mistake denied access for an unconfigured repository.
3. **Choose incremental update or no-op.** Compare actual existing content and
   the requested scope. Preserve established memory/config paths, IDs, index
   names and human sections. For unchanged state use no-op, without rewriting,
   reformatting, touching dates or adding duplicate entries. Missing/broken index
   needs an authorized pointer repair, not regeneration of an entire store.
4. **Sample relevant evidence.** Apply [discovery budget](../framework/init-discovery.md):
   manifests, pertinent docs and representative source/test text within a bounded
   component scope. Inspect script text only; do not run the application's tests
   or setup hooks. Record read scope/omissions and distinguish declared versions
   from observed tool/runtime state. An empty repository remains stack Unknown;
   do not scaffold an application.
5. **Prepare evidence-backed observations.** Use the existing Memory envelope
   and [selected topic templates](../framework/memory-specification.md#template-catalog).
   Each durable claim gets a stable collision-checked ID, source, real dates,
   verification scope and uncertainty. Source inspection verifies only that
   observation, not executed behavior/production. No approved ADR/decision may
   be created from a folder/package name or preferred architecture.
6. **Separate knowledge and constraints.** Distinguish observations, Unknowns,
   assumptions/proposals and confirmed constraints with their actual source and
   acceptance scope. Preserve approved intent when code differs; report drift
   rather than rewriting a decision. Do not store credentials, PII, raw logs,
   copied instructions/approvals or private reasoning in Memory.
7. **Select relevant profiles/preferences.** Inspect actual version/config/
   toolchain/architecture before selecting a [profile](../framework/engineering/index.md).
   Optional user preferences remain proposals unless accepted for the actual
   scope; they cannot override native/organization policy. No profile installs
   packages, upgrades frameworks, assigns an owner or invents provider identity.
   Offer [optional presets](../governance/presets.md) or neutral policy templates
   when relevant; do not adopt them by industry or enable native permissions.
   Missing policies/fields need a decision only where they block the scoped work.
8. **Resolve only missing authority.** Build a concrete destination/delta plan:
   selected root/store/config, entries affected, optional instruction block,
   effects, unknowns and exclusions. Match actual request/policy/approval using
   [human approval](../governance/human-approval.md). Reuse valid scope; ask only
   for uncovered sensitive effects, conflicting paths or material decisions.
   Preview stops at the proposal/report and never crosses into writes.
9. **Apply scoped state changes.** For a new unconfigured project use
   .kiyo/memory with index.md and only useful topic files; create no empty topic
   set. A minimal index plus project.md can record the inspected empty scope and
   explicit unknowns when initialization was requested. If a locator/preference
   file is needed, use [.kiyo/policy.md context shape](../templates/init/project-context.md)
   unless an established accepted config already provides it. Reuse existing
   config rather than add a second truth source. Immediately reread target
   entries/index/config and relevant input, recheck root/branch/IDs/permissions,
   and apply only necessary deltas. Newly appeared/overlapping human content
   means reconcile or hold; never overwrite an earlier whole-file snapshot.
10. **Add bootstrap only if needed and authorized.** Follow the
    [activation procedure](../framework/init-activation.md). Equivalent existing
    guidance means no new block. Require the exact target's evidenced native
    facility, appropriate write authority and known project-relative locators.
    Unknown/unsupported automatic loading is a reported limitation, not a reason
    to add hooks, copy Core, invent a command or guess a cache path.
11. **Preserve human/native instructions.** Read the latest instruction file
    again before any scoped edit. Insert one bounded managed locator block or
    update a provably unchanged owned block; preserve all surrounding human
    sections and instruction priority. Human-modified/ambiguous blocks require
    reconciliation. Never replace an entire AGENTS.md/CLAUDE.md/Copilot file,
    change global settings, or delete a file to “clean up” duplicates.
12. **Verify and report actual readiness.** Review only Init-owned diffs and
    preserved user changes. Resolve canonical store/index/evidence/locator paths
    against their declared bases; check unique IDs, entry-specific dates, actual
    references and no payload/cache dependency in project output. Perform
    authorized non-mutating file checks under [Evidence Contract](../framework/evidence-contract.md).
    Separate installed/discovered skill, agent-directed Core read, project
    guidance and actual auto-load evidence. Report the outputs below and apply
    [Definition of Done](../framework/definition-of-done.md); no unrun native test
    becomes PASS because files were created.

## Output and closure

Use the smallest [report](../framework/reporting-contract.md) in chat:
evidence-backed summary of inspected component/current state; unknowns and
uninspected areas; proposals versus sourced constraints; selected profiles;
exact Memory/config/bootstrap delta or no-op; separate activation readiness and
limits; check records; Memory Impact and status/next action.

After creating/updating necessary Memory retain UPDATE_REQUIRED with “applied”
and remaining gaps; a no-delta assessed rerun is NONE. Conflicts are CONFLICT;
inaccessible/insufficient assessment is NOT_ASSESSED as appropriate. Mandatory
requested setup still missing prevents full DONE. Optional native guidance can
remain unverified without misrepresenting successful bounded Memory setup.

Do not create a durable report merely for closure, an endpoint/method inventory,
an adopted organization policy, a release version or publisher. Requested neutral
policy drafts remain proposals; adoption and operational actions need their own
applicable authority under [policy resolution](../governance/policy-resolution.md). Application fixes,
test execution and dependency installation are separate tasks. Init does not
subscribe to future file changes or automatically run on every feature request.
