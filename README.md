# Kiyo Axiom Framework
**English** | [ภาษาไทย](README.th.md)

**Make your AI coding agent work like a professional engineer: read the real project first, change only what was asked, and report only what it can prove.**

📖 **Full documentation: [https://kiyo-axiom.codejadee.com](https://kiyo-axiom.codejadee.com/)**

Kiyo is a set of Markdown Skills for Claude Code, Codex and GitHub Copilot.
Install it and start working. There is no runtime, MCP server, hook, database or watcher to maintain.

---

## Why Kiyo

If your AI agent has ever done any of these, Kiyo helps:

| Common problem | How Kiyo helps |
| --- | --- |
| 🤔 **Guesses** your stack and conventions | Reads the real code, docs and tests first, and keeps *facts / assumptions / proposals / unknowns* clearly apart |
| ✂️ **Changes more than asked**, e.g. refactors a whole file to fix one bug | Keeps the change scoped to the task and leaves your unrelated edits alone |
| ✅ **Claims tests passed** when they never ran | Reports honestly: `PASS` / `FAIL` / `NOT_RUN` / `BLOCKED`, with evidence |
| 🔧 **Starts editing when you only asked for a review** | Review, Security and Architecture are read-only: they inspect and report, never touch code |
| 🧠 **Forgets context** every new session | Project Memory stores project context in your repo and can check drift against current code |
| ⚠️ **Takes risky actions** like push, deploy or touching a production DB | Governance and human approval rules apply: no commit, push or deploy unless you ask |

**In short:** your agent becomes more predictable, easier to verify and safer for your team's codebase.

### Four pillars

| Pillar | What it covers |
| --- | --- |
| **Project Intelligence** | Evidence-based project understanding, Project Memory, drift checks |
| **Software Engineering** | Requirements, minimal implementation, review, tests |
| **AI Governance** | Task scope, risk, data handling, human approval |
| **Agentic Skill Security** | Skill trust and provenance, prompt-injection defense |

---

## 🚀 Get started in 3 steps

### 1. Install

This repository is already a custom marketplace. Pick the commands for your host.

**Claude Code** (CLI / VS Code)
```text
/plugin marketplace add 0xPratyaDev7x/kiyo-codejadee-framework
/plugin install kiyo-axiom-framework@kiyo-axiom-framework
```

**Codex (CLI / VS Code)**
```text
codex plugin marketplace add 0xPratyaDev7x/kiyo-codejadee-framework
codex plugin add kiyo-axiom-framework@kiyo-axiom-framework
```

**GitHub Copilot** (CLI / VS Code)
```text
copilot plugin marketplace add 0xPratyaDev7x/kiyo-codejadee-framework
copilot plugin install kiyo-axiom-framework@kiyo-axiom-framework
```

**Codex IDE Extension (VS Code)** cannot load plugins. Copy all eight `kiyo-*`
folders from `dist/codex-ide/.agents/skills/` into your repository's `.agents/skills/`
(or `$HOME/.agents/skills/` for every project), then open a new chat
([detailed steps](platforms/codex-ide/README.md)).

> Other options, such as a ZIP for a single-session trial, are in the
> [install guide](docs/user/README.md#install-or-load-a-prepared-package).

### 2. Run Init so Kiyo learns your project

Invoke the **Init** Skill (see the per-host syntax under "Invoking a Skill" below) and start with a preview:

```text
Preview onboarding for this repository; report evidence, unknowns and proposed
Memory/config/bootstrap changes without writing files.
```

If you are happy with the preview, continue:

```text
Create the proposed local Memory/config; preserve existing instructions.
```

By default Kiyo creates Memory in `.kiyo/memory` and config in `.kiyo/policy.md`,
without touching your source code, tests or dependencies.

### 3. Daily work

Pick the Skill that fits the task, state the goal and the allowed scope, then read the report.
Kiyo replies in the language you write in.

---

## 📋 Cheatsheet: the 8 Skills

| Skill | Use it when | Example prompt | Writes files? |
| --- | --- | --- | --- |
| **Init** | Onboarding a project, or asking Kiyo to analyze it | “Preview onboarding only.” | preview: ❌ / initialize: Memory/config only |
| **Requirement** | Turning a raw request or issue into an implementation-ready requirement | “Add Excel export; identify missing fields and permissions first.” | ❌ chat only (writes only a spec path you request) |
| **Implement** | Adding a feature, fixing a bug, or an explicitly scoped refactor | “Fix the boundary error and add its regression test.” | ✅ code/tests/docs within scope |
| **Review** | Reviewing a diff, files, a commit range or a PR | “Review my unstaged changes; do not edit.” | ❌ read-only |
| **Test** | Finding test gaps, running tests, or writing tests | “Assess authorization test gaps in this module.” | Depends on mode (see below) |
| **Security** | Assessing risk in code, a Skill package or a policy | “Assess this handler for validation and authorization risks.” | ❌ read-only |
| **Architecture** | Design questions, impact analysis, drift from an ADR | “Compare ADR-007 with this module; report deviations only.” | ❌ read-only |
| **Memory** | Showing, checking, syncing or repairing Project Memory | “Compare these Memory observations with this branch.” | show/check: ❌ / sync/repair: authorized entries only |

### Modes worth knowing

| Skill | Mode | What it does |
| --- | --- | --- |
| Init | `preview` | Read-only; reports findings and what it would propose |
| Init | `initialize` | Creates/updates authorized Memory, config and bootstrap |
| Test | `assess` | Reads tests and finds gaps; no writes, no execution |
| Test | `run` | Runs an existing suite after inspecting its script and environment; no source/test edits |
| Test | `write` | Writes tests for agreed cases (writing does not authorize running them) |
| Security | `application` / `skills` / `governance` / `self-check` | App code / Skill package against AST01–AST10 / policy / Kiyo itself |
| Memory | `show` / `check` | Summarize entries / compare Memory with current code for drift (no writes) |
| Memory | `sync` / `repair` | Apply evidence-backed observation fixes / repair moved-file links (decisions and history preserved) |

### Invoking a Skill

The eight slugs are `init`, `requirement`, `implement`, `review`, `test`, `security`, `architecture`, `memory`.

| Host | How to invoke (example: `init`) |
| --- | --- |
| Claude Code CLI / VS Code | `/kiyo-axiom-framework:init` |
| Codex CLI | Open `/skills` or the `$` picker and choose the Kiyo entry |
| Codex IDE Extension | `$kiyo-init`, or choose it from `/skills` |
| GitHub Copilot CLI | `/skills list` or `/skills info` to find Kiyo's selector |
| GitHub Copilot VS Code | `/kiyo-axiom-framework:init`, or choose it in Configure Skills |

> Don't confuse these with host built-ins such as `/init` or `/review`.

### Reading a report

| Label | Meaning |
| --- | --- |
| `PASS` / `FAIL` | The check actually ran and passed / failed |
| `NOT_RUN` | The check did not run (this is not a pass) |
| `NOT_APPLICABLE` | Not relevant to this task |
| `BLOCKED` | Could not proceed, e.g. missing environment or permission |
| `DONE` / `PARTIALLY COMPLETE` / `DECISION REQUIRED` | Task status: finished / partly finished / needs your decision |

Requirement has its own readiness labels: `READY_FOR_IMPLEMENTATION`, `DECISION_REQUIRED`,
`INSUFFICIENT_EVIDENCE`. READY does not mean coding starts on its own; invoke Implement next.

### Tips

- **Always state the goal and the scope**, e.g. “only these files” or “do not edit”.
- **Ambiguous requests start read-only.** “Take a look at login” makes Kiyo inspect or ask first, not edit.
- **Invoking the Skill explicitly** is the most reliable route. Init adds routing hints so the host can pick a Skill on its own, but that is not guaranteed.
- **Want another language?** Say “answer in Thai” (or any language). Code, commands and paths stay unchanged.

---

## 📚 Documentation

**Full documentation: [https://kiyo-axiom.codejadee.com/](https://kiyo-axiom.codejadee.com/)**

Guides in this repository:

- [User guide: install → Init → daily work → reports](docs/user/README.md)
- [Skill inputs, modes and scopes](docs/user/skills.md)
- [Governance and approval](docs/user/governance.md)
- [Memory and drift](docs/user/memory.md)
- [Application and agentic security](docs/user/security.md)
- [Troubleshooting](docs/user/troubleshooting.md)
- [Nine illustrative walkthroughs](docs/user/walkthroughs.md)
- [Maintainer guide](docs/developer/maintainer-guide.md)

---

## Project status

Kiyo is a **development preview** (working name, no public release yet).
You can install it from this repository's marketplace, but full agent-workflow testing on every host is not finished.

- Kiyo guides the agent; permissions and command execution remain the host's job.
  Kiyo does not provide a sandbox or guarantee agent compliance.
- It does not certify ISO/OWASP compliance or any provider's privacy terms.
- Per-host test results: [compatibility matrix](docs/compatibility/live-test-matrix.md)
  and [Final Acceptance Report](docs/build/FINAL-ACCEPTANCE.md).

## License

[MIT](LICENSE)
