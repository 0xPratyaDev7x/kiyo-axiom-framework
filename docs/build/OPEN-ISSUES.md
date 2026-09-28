# Kiyo Compass — Open Issues

Snapshot: Prompt 02, 2026-09-28. Research is recorded; remaining capability gaps
do not block architecture of documented surfaces. Open means unresolved, not approved.

| ID | Gap / evidence | Related requirements / decision | Required action and responsibility | Blocking point / state |
| --- | --- | --- | --- | --- |
| ISS-001 | Final publication name and marketplace availability unknown | REQ-001, REQ-004, REQ-079; DEC-001 | Owner selects final identity; research checks availability without claiming it is reserved | OPEN; final naming/registration/publication |
| ISS-002 | Root MIT LICENSE exists, but intended release-license confirmation was not supplied | REQ-001, REQ-053, REQ-079; DEC-002 | Owner confirms intended publication license; preserve current LICENSE meanwhile | OPEN; license change or release finalization |
| ISS-003 | Publisher/namespace/account authority unknown | REQ-001, REQ-059, REQ-079; DEC-003 | Owner supplies approved publisher identity and destination before publication-related work | OPEN; final publisher metadata/registration/publication |
| ISS-004 | Six-target research now documented in [capabilities](../compatibility/platform-capabilities.md). Codex IDE plugins UNSUPPORTED; Copilot rule semantics, exact CLI plugin-skill selector spellings and Codex custom lifecycle/cache behavior not established | REQ-004–007, REQ-009–011, REQ-061, REQ-067; DEC-004 | Prompt 03 preserves gaps; later native prompts revalidate dependent contracts and test each target. No guessed manifest or universal core-loader | OPEN; only dependent packaging/activation/compatibility claims gated |
| ISS-005 | Official editions and AST labels documented in [standards baseline](../research/standards-baseline.md); ISO full texts not reviewed; AST v1 remains public-review draft; latest SAMM incremental version UNKNOWN | REQ-056–067 | Use concept mappings with edition/status limits; recheck evolving references before release. Lawful full-text review needed before clause-level mappings | OPEN for detailed mappings/release revalidation; Prompt 02 public-source baseline complete |
| ISS-006 | No Kiyo live target tests performed; CLI/IDE/account availability not inspected | REQ-005, REQ-067, REQ-076–078 | Later inspect authorized environments; test each target in Prompt 26 and retain NOT_TESTED with concrete missing prerequisites where necessary | OPEN; compatibility acceptance |
| ISS-007 | Canonical layout, public skills, core procedures, overlays, tests and release artifacts not implemented | REQ-001–080; see per-row traceability | Execute only subsequently requested roadmap steps; use planned areas as proposals, not existing files | OPEN; product acceptance in Prompt 30 |
| ISS-008 | Final gap audit and final acceptance have not occurred | REQ-043, REQ-077, REQ-079, REQ-080 | Reconcile all criteria, implementation and real evidence in Prompts 29–30 | OPEN; final completion claims |
| ISS-009 | Native plugin installation exposes skill metadata, not evidence of always-loaded core. Bootstrap/reference/version ownership and residual project files after uninstall not designed | REQ-006, REQ-009, REQ-076; [activation modes](../compatibility/activation-modes.md) | Prompt 03 designs compact native bootstrap and self-contained resource policy; later tests verify explicit/implicit loading and lifecycle | OPEN; persistent-core/automatic-activation guarantees prohibited |

No missing prerequisite has been replaced by invented data. Missing live evidence
does not establish that a particular executable, extension or account is absent.
Prompt 01 and Prompt 02 checks and their limitations are recorded in
[BASELINE.md](BASELINE.md). Update these issue rows as evidence
arrives instead of duplicating them on reruns.

