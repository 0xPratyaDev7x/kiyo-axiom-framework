# Kiyo Compass — Decisions

Observation date: 2026-09-28. “Owner” below is a role, not an invented person,
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

## Pending owner decisions

| ID | Decision | Current evidence / status | Who decides | Latest needed / effect | Resolution evidence |
| --- | --- | --- | --- | --- | --- |
| DEC-001 | Final publication name and native marketplace identifiers | OPEN. Kiyo Compass is only the working name; marketplace availability UNKNOWN | Repository/product owner | Before final release identities or marketplace registration/publication; does not block scope or research | None |
| DEC-002 | Confirm license intended for publication | OPEN. Existing root LICENSE is MIT and must remain intact; final owner confirmation is not supplied | Repository/product owner | Before release/legal metadata is finalized or the existing license is changed; does not block Prompt 01/02 | None |
| DEC-003 | Publisher identity, namespace and authorized publication destination | OPEN. No publisher/account evidence or approval supplied; do not infer from repository path or copyright | Repository/product owner | Before final publisher metadata, registration or publication; does not block Prompt 01/02 | None |
| DEC-004 | Treatment of Codex IDE native-plugin support gap | OPEN. Official [plugin documentation](https://learn.chatgpt.com/docs/plugins) excludes IDE plugins; [skills documentation](https://learn.chatgpt.com/docs/build-skills) supports standalone IDE skills. Checked 2026-09-28; DOCUMENTED_ONLY, live NOT_TESTED | Repository/product owner | Before promising six-target native installation or accepting a standalone fallback; does not block Prompt 03 design of documented surfaces | No fallback or scope reduction approved |

Ask only when an unresolved choice blocks the current authorized prompt. Existing
instructions authorize Prompt 02 research and build-state updates. Do not ask for
premature publication decisions to complete research. Publication metadata still
requiring confirmation is listed in [SOURCES](../research/SOURCES.md#publication-information-still-requiring-the-owner).

## Proposals and future technical decisions

Planned paths in REQUIREMENTS are provisional implementation areas, not an
approved architecture. Prompt 02 must establish capabilities, sources and gaps;
Prompt 03 can then define the canonical layout and overlay boundaries.
No native manifest syntax, version policy, signing identity or marketplace
availability was decided in Prompt 01. Prompt 02 now records documented formats
in [platform capabilities](../compatibility/platform-capabilities.md), but does
not choose/build overlays. Copilot plugin-rule semantics, exact Codex/Copilot CLI
plugin-skill selector details and custom lifecycle tests remain open.

When recording a future decision, separate observations and proposals from
approved decisions. Record the real authority, scope, evidence and date; preserve
prior decisions and human edits rather than rewriting approved intent to match
implementation drift.

