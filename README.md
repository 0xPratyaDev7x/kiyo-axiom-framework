# Kiyo Compass

Final build handoff: [Final Acceptance Report](docs/build/FINAL-ACCEPTANCE.md).
Static content is authored and local packages validated with stated limits;
full host acceptance and publication remain blocked. No public release exists.

**AI Engineering & Governance Framework for coding agents.**

Kiyo gives a coding agent a shared way to investigate a repository, choose the
right workflow, make bounded changes and report evidence. It addresses guessing
about the project, changing more than requested, claiming checks that never ran,
and turning a review into an implementation task.

Project Memory helps preserve context between tasks. It can be stale: current
code must be inspected, and an approved decision remains intended behavior even
when code differs. Kiyo's guidance distinguishes facts, assumptions, proposals,
approved decisions and unknowns.

**Development preview — working name, not a published release.** Kiyo is
Markdown-first, with static native metadata and no consumer runtime, MCP, hooks,
database or watcher. The host agent performs actions and controls permissions.
These instructions do not enforce a sandbox or guarantee agent compliance.

## Four pillars, eight Skills

| Pillar | What you use it for |
| --- | --- |
| Project Intelligence | Evidence-backed context, project-owned Memory and drift |
| Software Engineering | Requirements, minimal implementation, review and tests |
| AI Governance | Scope, risk, data handling and valid human approval |
| Agentic Skill Security | Trust, provenance, metadata and cross-host limits |

The eight public Skills are **Init, Requirement, Implement, Review, Test,
Security, Architecture and Memory**. Router, governance review and self-check
are shared procedures or submodes, not extra Skills.
[Choose a Skill](docs/user/skills.md).

## Support and evidence

Checked **2026-09-29**. VERIFIED applies only to the named observed property.
DOCUMENTED_ONLY means a vendor describes a facility; NOT_TESTED means Kiyo has
not exercised it. UNSUPPORTED identifies an explicit documented exclusion.
None of the six targets has a completed Kiyo agent-workflow or automatic Core
activation test. [Exact results and limitations](docs/compatibility/live-test-matrix.md).

| Target | Available evidence | Remaining boundary |
| --- | --- | --- |
| Claude Code CLI | VERIFIED: 2.1.220 normal validation and directory/ZIP discovery of eight Skills | Strict validation FAIL for missing version/author; persistent install and Skill behavior NOT_TESTED |
| Claude Code VS Code | DOCUMENTED_ONLY plugin route; extension metadata observed | Kiyo installation, invocation and activation NOT_TESTED |
| Codex CLI | VERIFIED: 0.158.0 disposable local catalog install, cache and uninstall | Skill behavior/update NOT_TESTED; public ingestion FAIL for unresolved release metadata |
| Codex IDE Extension | UNSUPPORTED native plugins per official documentation | Standalone Skills are a different route; no Kiyo fallback approved |
| GitHub Copilot CLI | DOCUMENTED_ONLY plugin route | Kiyo native checks NOT_TESTED; exact plugin-qualified Skill selector UNKNOWN |
| GitHub Copilot VS Code | DOCUMENTED_ONLY agent-plugin route | Kiyo installation, selection and activation NOT_TESTED |

The [evidence index](docs/evidence/live/README.md) records versions, commands,
failures and preservation checks. Local Windows results do not certify another
OS, account or IDE. Codex's observed fallback version 1.0.0 is not a Kiyo release.

## Quickstart

1. Choose a target from the table. Use its prepared
   [development package](docs/user/README.md#install-or-load-a-prepared-package)
   and native mechanism. There is no published Kiyo marketplace listing to install.
2. Confirm the Kiyo source and eight entries in that host. Select **Init**
   explicitly using the [native selection table](docs/user/README.md#select-a-skill).
3. Start with: “Preview onboarding for this repository; report evidence,
   unknowns and proposed Memory/config/bootstrap changes without writing files.”
   Then request only the local initialization changes you want.
4. For daily work, choose Requirement, Implement, Review, Test, Security,
   Architecture or Memory. State the target and allowed effects; review the
   evidence and limitations in the report.

This sequence is an **illustrative/synthetic user workflow, NOT_RUN** as a native
Kiyo walkthrough. It needs an authorized host session/account; installing metadata
alone does not load all Core rules on every task. No consumer generator is needed.

## Guides

- [User guide: install → Init → daily work → reports](docs/user/README.md)
- [Skill inputs, modes and scopes](docs/user/skills.md)
- [Governance and approval](docs/user/governance.md)
- [Memory and drift](docs/user/memory.md)
- [Application and agentic security](docs/user/security.md)
- [Troubleshooting](docs/user/troubleshooting.md)
- [Nine illustrative walkthroughs](docs/user/walkthroughs.md)
- [Maintainer guide](docs/developer/maintainer-guide.md)
- [Draft marketplace copy and owner inputs](docs/release/marketplace-copy.md)

Kiyo does not guarantee always-on loading, block all dangerous commands, certify
ISO/OWASP compliance or establish any provider's privacy terms. See
[Core](src/kiyo/KIYO.md), [build state](docs/build/PROGRESS.md) and
[open decisions](docs/build/DECISIONS.md). The existing [MIT LICENSE](LICENSE)
is preserved; final publication name, version, license confirmation, publisher
and destination remain owner decisions.
