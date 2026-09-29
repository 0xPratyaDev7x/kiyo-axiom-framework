# Owner-required remaining integration work

Snapshot **2026-09-29**; no model-call permission is pending: the user selected
native checks without quota. These are remaining tests for a later authorized
run, not requests to spend quota or publish now. Source:
[actual matrix](live-test-matrix.md) and [P26 register](../research/SOURCES.md#prompt-26-native-revalidation).

| Gate / responsible role | Targets / cases | Concrete prerequisite and next test | What remains unclaimed |
| --- | --- | --- | --- |
| Account/quota authority — human owner | Supported five targets, LT-02–10 | Approve exact host/account, synthetic data scope, turn/spend ceiling and model; use actual sign-in without copying credentials | All Skill behaviors, Core/automatic activation and sensitive approval handling |
| Disposable IDE session — operator | Claude VS Code, Copilot VS Code, LT-01–12 | Native UI access, observed active extension/engine, isolated host state and permitted account; use target's own plugin UI | No CLI result substitutes for IDE |
| Copilot host — operator | Copilot CLI, LT-01–12 | Identify an existing authorized executable or separately approve host installation in an isolated environment; inspect help/version first | PATH lookup does not prove universal absence |
| Native plugin gap — owner DEC-004 | Codex IDE, LT-01–12 | Recheck official support; decide any standalone fallback as a distinct contract before building/testing it | Six-target native support; no fallback selected |
| Claude catalog — owner/operator | Claude CLI marketplace LT-01/11/12; IDE independently | Supply real authorized local catalog owner/name if testing that route; keep release metadata unknown until confirmed | Session --plugin-dir discovery is not persistent install/uninstall |
| Release identity — owner DEC-001–003 | All publication/release metadata; Claude strict validation | Confirm name, version/history, publisher/destination and license; rerun relevant native and ingestion checks | Claude strict PASS, Codex ingestion PASS, listing, signature or release readiness |
| Two-candidate update — owner/operator | All supported LT-11 | Two real reviewed candidate digests/identities and the target's documented replacement method, then state-preservation diff/new session | No native update, downgrade, rollback or human managed-block survival claim |
| Cache/read/activation — operator | Supported LT-08–10 | Agent trace from native cache with source unavailable; explicit separate fresh sessions with/without authorized managed bootstrap | Static containment or metadata cost cannot prove Core loading |
| Stronger environment coverage — operator | All later runs | Real host policies/restrictions, agreed OS/editor versions and nested/module/legacy state variants | One Windows metadata/lifecycle subset is not broad parity or minimum-version support |

Keep immutable attempt IDs and original failures. Update the per-target records
by adding a new run, not rewriting NOT_RUN history as a pass. Critical unauthorized
effects, disclosure or fabricated test results block release. No such behavioral
assessment was run here; absence of an observed failure is not proof of safety.

Prompt 27 documentation may proceed using these limits. Compatibility/release
acceptance must retain the unresolved rows.
