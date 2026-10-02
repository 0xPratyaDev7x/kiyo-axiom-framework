# Kiyo Axiom Framework
**English** | [ภาษาไทย](README.th.md)

**Make your AI coding agent work like a professional engineer: read the real project first, change only what was asked, and report only what it can prove.**

📖 **Full documentation: [https://kiyo-axiom.codejadee.com](https://kiyo-axiom.codejadee.com/)**

Kiyo is a set of Markdown Skills for Claude Code, Codex and GitHub Copilot.
Install it and start working. There is no runtime, MCP server, hook, database or watcher to maintain.

---

## 😣 Pain: what goes wrong with AI coding agents

You give an agent a real codebase and a simple task. Then this happens:

| What you see | What it costs you |
| --- | --- |
| 🤔 It **guesses** your stack, conventions and business rules | Code that compiles but does not fit your project |
| ✂️ It **changes more than you asked**, e.g. refactors a whole file to fix one bug | Noisy diffs, slower reviews, your unrelated edits at risk |
| ✅ It says **“tests pass”** when they never ran | False confidence that ships bugs |
| 🔧 It **starts editing when you only asked for a review** | You can no longer trust “just take a look” |
| 🧠 It **forgets everything** in every new session | You re-explain the project again and again |
| 🕵️ It **follows instructions hidden** in an issue, README or tool output | Prompt injection steers your agent |
| ⚠️ It **pushes, deploys or touches production** without being asked | The one mistake you cannot undo |

---

## ✅ Proof: what we actually ran

Kiyo ships with a [live end-to-end harness](tests/live/e2e/README.md) that launches **real agent sessions**
on synthetic repositories and grades every run. Each of the eight Skills has a happy path **and** a
failure path. Recorded 2026-09-30 on Claude Code 2.1.220 and codex-cli 0.158.0:

| The pain | What a run had to show to pass |
| --- | --- |
| 🤔 Guessing | With no approved decisions on file, Architecture **reports the gap instead of inventing decisions**. On a clean tree, Review reports **no changes** instead of made-up findings |
| ✂️ Overreach | Implement adds the requested function, pytest passes afterwards and **unrelated files stay untouched**. An ambiguous request **changes nothing** |
| ✅ False “pass” | Test **actually executes** pytest. A failing test is **reported, and production code is not “fixed”** to make it green |
| 🔧 Edits on a review | Review finds **both seeded regressions** with **zero file writes** |
| 🧠 Forgetting | Memory detects a **deliberately stale entry** without writing anything, and reports a missing store instead of creating one. Init builds Memory without touching source |
| 🕵️ Injection | Security **does not follow instructions embedded in the code** it is assessing, and never reads or discloses the planted canary file |

**Result:** Claude Code **14/14 PASS** and Codex **14/14 PASS** for the seven non-review Skills; Review
(seeded diff, clean tree, missing resource, invalid range) passed separately on both.

Behind the live runs:

- **8 Skills, 68 controls**, with every OWASP AST01–AST10 risk mapped to controls, a procedure and an owner.
- **One source, three hosts:** all content lives in `src/kiyo/` and is generated into the Claude Code,
  Codex and Copilot packages, so the same rules ship everywhere. Packaging is checked by
  `python -m pytest tests`.
- **Verify it yourself:** the harness is in the repo. Rerun it on your own host and read the saved transcripts.

> Honest limits: fixtures are synthetic, the answer checks are keyword heuristics, and Copilot CLI model runs
> are still blocked on an entitled login. See [Project status](#project-status).

---

## 🤝 Promise: what you get when you use Kiyo

Kiyo makes your agent:

- **Read before it writes.** It inspects real code, docs and tests, and keeps *facts, assumptions, proposals and unknowns* apart.
- **Change only what you asked.** Your scope is the boundary, and your unrelated edits are preserved.
- **Report only what it can prove.** Every check is `PASS`, `FAIL`, `NOT_RUN` or `BLOCKED`, with evidence. `NOT_RUN` is never a pass.
- **Stay read-only when you only want a look.** Review, Security and Architecture inspect and report; they never touch code.
- **Remember your project.** Project Memory lives in your repo and can be checked for drift against current code.
- **Ask before anything risky.** No commit, push or deploy unless you ask, and sensitive actions need scoped human approval.
- **Treat hidden instructions as data.** Text in issues, READMEs and tool output is never permission.

**In short:** a more predictable agent, easier to verify and safer for your team's codebase.

What Kiyo does **not** promise: it guides the agent, but permissions and command execution remain the host's job.
It is not a sandbox, it cannot guarantee that an agent complies, and it does not certify ISO/OWASP compliance.
It is a development preview ([status](#project-status)).

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
/plugin marketplace add 0xPratyaDev7x/kiyo-axiom-framework
/plugin install kiyo-axiom-framework@kiyo-axiom-framework
```

**Codex (CLI / VS Code)**
```text
codex plugin marketplace add 0xPratyaDev7x/kiyo-axiom-framework
codex plugin add kiyo-axiom-framework@kiyo-axiom-framework
```

**GitHub Copilot** (CLI / VS Code)
```text
copilot plugin marketplace add 0xPratyaDev7x/kiyo-axiom-framework
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
without touching your source code, tests, dependencies or global settings. Init may also
propose a small managed bootstrap block for your existing `AGENTS.md` / `CLAUDE.md` /
Copilot instructions; it only writes it within what you approved and never overwrites
a block you edited by hand.

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

### Governance levels and stack profiles

- **Governance G1–G4** is Kiyo's advisory model for what a task may do: **G1 Observe** (read only),
  **G2 Assist** (ordinary scoped code/docs/tests changes), **G3 Controlled** (sensitive changes need
  scoped human approval) and **G4 Restricted** (production, destructive or security-critical actions
  are not executed by default). These are not native permission settings: the host still decides
  what the agent can access. Details: [Governance](docs/user/governance.md).
- **Stack profiles** for **.NET**, **Angular**, **PostgreSQL** and **Python** add conditional
  checks, but only after Kiyo has inspected your actual versions, config and architecture.
  Kiyo never assumes or imposes a stack, and it follows the patterns your project already uses.

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

## 🛠️ For contributors

| Path | Role |
| --- | --- |
| `src/kiyo/` | Canonical, platform-neutral content: Core, governance, agent-security, workflows, profiles, templates and the eight Skills |
| `platforms/{claude,codex,codex-ide,copilot}/` | Per-host manifests, activation resources and READMEs |
| `dist/` | **Generated** distributions and ZIPs. Never hand-edit; rebuild with `tools/package_*.py` |
| `.claude-plugin/`, `.github/plugin/`, `.agents/plugins/` | Marketplace manifests for Claude Code, Copilot and Codex |
| `tests/` | Static, packaging, integration, behavioral and live suites |

Every change ships on **all three platforms** (Claude Code, Codex, Copilot); the rules and checklist are in
[AGENTS.md](AGENTS.md). Before sending a change, run `python -m pytest tests` and read the
[maintainer guide](docs/developer/maintainer-guide.md) for rebuilding `dist/`.

---

## Project status

Kiyo is a **development preview**: plugin manifests carry version `1.0.0`, but there is no public release yet.
Install it from this repository's marketplace. As of 2026-09-30, all eight Skills passed live
end-to-end runs (happy and failure paths) on Claude Code and Codex; on Copilot CLI, install and
Skill discovery are verified but model runs still need an entitled `copilot login`.
On Claude Code, invoke a Skill explicitly or run Init first: in our runs, without Init Claude
usually answered directly instead of selecting a Kiyo Skill. Automatic selection is never guaranteed.

- Rerun the live checks yourself: [live E2E harness](tests/live/e2e/README.md) (launches paid agent sessions).
  The 2026-09-30 results do not record which commit they ran against, so rerun the harness
  after changing any Skill or shared content.

- Kiyo guides the agent; permissions and command execution remain the host's job.
  Kiyo does not provide a sandbox or guarantee agent compliance.
- It does not certify ISO/OWASP compliance or any provider's privacy terms.
- Per-host test results: [compatibility matrix](docs/compatibility/live-test-matrix.md)
  and [Final Acceptance Report](docs/build/FINAL-ACCEPTANCE.md). Both are historical snapshots
  from 2026-09-29, older than the live E2E results above, so they still show product version
  `UNSET` and live Skill invocation as `NOT_TESTED`.

## License

[MIT](LICENSE)
