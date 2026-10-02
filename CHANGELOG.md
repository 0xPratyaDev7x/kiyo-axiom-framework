# Changelog

All notable changes to Kiyo Axiom Framework are recorded here. Dates are `YYYY-MM-DD`.

## 1.0.0 — 2026-10-02

First stable release, through this repository's marketplace. Not yet listed in any official
plugin directory.

### Support status

| Host | Status | Basis |
| --- | --- | --- |
| Claude Code (CLI) | Stable | Live E2E 2026-09-30 on Claude Code 2.1.220, all eight Skills passed |
| Codex CLI | Stable | Live E2E 2026-09-30 on codex-cli 0.158.0, all eight Skills passed |
| GitHub Copilot (CLI / VS Code) | Beta | Marketplace add, install and Skill discovery verified on Copilot CLI; model-run behavior not yet verified; VS Code not tested |
| Codex IDE Extension | Experimental | Standalone-Skill route (`dist/codex-ide`), discovery documented, Kiyo use not tested |

### Included

- Eight Skills: `init`, `requirement`, `implement`, `review`, `test`, `security`, `architecture`, `memory`.
- Shared Core, workflows, 68 controls and templates, authored once in `src/kiyo/` and generated into
  the Claude Code, Codex, Copilot and Codex IDE packages.
- Advisory governance levels G1–G4 and stack profiles for .NET, Angular, PostgreSQL and Python.
- Project Memory with drift checks, and OWASP AST01–AST10 coverage for agentic Skill security.
- Marketplace manifests for Claude Code (`.claude-plugin/`), Copilot (`.github/plugin/`) and
  Codex (`.agents/plugins/`).
- Replies follow the language of the user's latest message (KIYO-REPORT-001).
- English and Thai READMEs.
- Live E2E harness (`tests/live/e2e/`) that runs real agent sessions on synthetic repositories.

### Known limitations

- Kiyo guides the agent. Permissions and command execution remain the host's job; it is not a
  sandbox and does not guarantee agent compliance or certify ISO/OWASP compliance.
- The 2026-09-30 live E2E results do not record the commit they ran against. Rerun the harness after
  changing any Skill or shared content.
- A Copilot E2E run on 2026-10-02 was inconclusive: the host also loaded unrelated `kiyo-*` Skills
  from the operator's personal `~/.agents/skills`, so its results are not used as evidence.
- Copilot VS Code and the Codex IDE Extension have no Kiyo test results.
- Historical records under `docs/build/` and `docs/evidence/` (2026-09-29) predate the 1.0.0
  identity and still show the product version as `UNSET`.
