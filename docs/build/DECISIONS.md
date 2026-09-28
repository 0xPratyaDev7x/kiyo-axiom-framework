# Kiyo Compass — Decisions

Snapshot date: 2026-09-29. “Owner” below is a role, not an invented person,
publisher or approver. No approval date is assigned to unresolved decisions.

## Confirmed task constraints

The user supplied these instructions in Prompt 01; they are recorded in
[BUILD-CONTRACT.md](BUILD-CONTRACT.md), not inferred product approvals:

- Use Kiyo Compass as a working name containing Kiyo.
- Build a file-based, Markdown-first, vendor-neutral framework with no runtime.
- Use the four pillars, exactly eight public skills and four shared procedures/
  submodes described in the contract.
- Maintain one canonical specification and necessary native overlays.
- Treat the six targets independently and Kiyo controls as advisory.
- Execute Prompt 01 only, create eight build records and stop after its summary.

Prompt 02 was subsequently authorized on 2026-09-28: research official native
documentation and standards, create five research/compatibility files, update
build state and stop before Prompt 03. This adds no publication authorization.

Prompt 03 was subsequently authorized: design canonical architecture, create the
four architecture contracts and ADR, add only necessary scaffold, check/update
build state and stop before Prompt 04. The selected technical design is recorded
on 2026-09-29 in [ADR-001](../architecture/decisions/ADR-001-static-canonical-packages.md).
This authorizes architecture choices, not publication identities or later prompts.

Prompt 04 was subsequently authorized on 2026-09-29: implement compact shared
Core and expected responses, check/update build state and stop before Prompt 05.
[ADR-002](../architecture/decisions/ADR-002-core-loading-budgets.md) records the
requested line ceilings and retains existing word budgets over the complete
mandatory bootstrap. No publication authority or host enforcement is added.

## Pending owner decisions

| ID | Decision | Current evidence / status | Who decides | Latest needed / effect | Resolution evidence |
| --- | --- | --- | --- | --- | --- |
| DEC-001 | Final publication name and native marketplace identifiers | OPEN. Kiyo Compass is only the working name; marketplace availability UNKNOWN | Repository/product owner | Before final release identities or marketplace registration/publication; does not block scope or research | None |
| DEC-002 | Confirm license intended for publication | OPEN. Existing root LICENSE is MIT and must remain intact; final owner confirmation is not supplied | Repository/product owner | Before release/legal metadata is finalized or the existing license is changed; does not block Prompt 01/02 | None |
| DEC-003 | Publisher identity, namespace and authorized publication destination | OPEN. No publisher/account evidence or approval supplied; do not infer from repository path or copyright | Repository/product owner | Before final publisher metadata, registration or publication; does not block Prompt 01/02 | None |
| DEC-004 | Treatment of Codex IDE native-plugin support gap | OPEN. Official [plugin documentation](https://learn.chatgpt.com/docs/plugins) excludes IDE plugins; [skills documentation](https://learn.chatgpt.com/docs/build-skills) supports standalone IDE skills. Checked 2026-09-28; DOCUMENTED_ONLY, live NOT_TESTED | Repository/product owner | Before promising six-target native installation or accepting a standalone fallback; does not block Prompt 03 design of documented surfaces | No fallback or scope reduction approved |

Ask only when an unresolved choice blocks the current authorized prompt. Existing
instructions authorize Prompt 04 Core and build-state updates. Do not ask for
premature publication decisions to complete that scope. Publication metadata still
requiring confirmation is listed in [SOURCES](../research/SOURCES.md#publication-information-still-requiring-the-owner).

## Proposals and future technical decisions

Planned paths in REQUIREMENTS are historical provisional implementation areas.
Prompt 03 selects [the canonical layout](../architecture/framework-layout.md)
and overlay boundaries; this refines future paths without rewriting requirements.
No native manifest syntax, version policy, signing identity or marketplace
availability was decided in Prompt 01. Prompt 02 now records documented formats
in [platform capabilities](../compatibility/platform-capabilities.md), but does
not choose/build overlays. Copilot plugin-rule semantics, exact Codex/Copilot CLI
plugin-skill selector details and custom lifecycle tests remain open.

ADR-001 is accepted for build design within the user's Prompt 03 scope: one
authored specification, generated shared resources inside each skill, compact
bootstrap and project-owned state. It is not an owner release approval, completed
Core implementation or verified host behavior. Future version values remain
unset; preserve any established history found when release work begins.

When recording a future decision, separate observations and proposals from
approved decisions. Record the real authority, scope, evidence and date; preserve
prior decisions and human edits rather than rewriting approved intent to match
implementation drift.

