# Kiyo Compass — Native invocation map

Original baseline: **2026-09-28**; Claude rechecked **2026-09-29** under CL20-01–13; Codex under CX21-01–12. Source IDs: [SOURCES](../research/SOURCES.md).
Syntax below is **DOCUMENTED_ONLY**, not execution evidence.
All six targets are **NOT_TESTED**. Angle-bracket tokens are metavariables,
not runnable Kiyo release identifiers. No publication name or namespace is finalized. Prompt 20 uses the development
working namespace kiyo-compass with the eight canonical skill slugs.

## Six separate invocation surfaces

| Target | Discover / manage | Explicit skill selection | Automatic selection | Limitation / source / checked |
| --- | --- | --- | --- | --- |
| Claude Code CLI | `/plugin`; shell `claude plugin list` | Plugin `/<plugin>:<skill>`; standalone `/<skill>` | Description match unless disabled | CL20-01/02/05/09, 2026-09-29; working package /kiyo-compass:<skill>, actual selection untested; no action approval implied. |
| Claude Code VS Code | Claude panel `/plugins` | Claude panel `/<plugin>:<skill>` | Claude description match | CL20-02/04/09, 2026-09-29; /kiyo-compass:<skill> documented convention, independent Claude panel entry untested. |
| Codex CLI | /plugins; /skills or $ mention picker | Select actual Kiyo source entry | Description match; not guaranteed | CX21-04/06, 2026-09-29; exact plugin-qualified spelling UNKNOWN. Local 0.158.0 help separately exposes plugin add/remove; no invocation tested. |
| Codex IDE Extension | /skills or $ for standalone skills only | Plugin invocation **UNSUPPORTED** | Standalone description match only | CX21-04/06, 2026-09-29; no native Kiyo plugin route or approved standalone fallback. |
| GitHub Copilot CLI | `/skills list`, `/skills info`; shell `copilot plugin list` | `/<skill-name>` in prompt | Prompt/description match | G01/G03, 2026-09-28; exact plugin namespace/collision spelling UNKNOWN; do not copy VS Code spelling. |
| GitHub Copilot VS Code | `/skills`; Extensions `@agentPlugins` | Plugin `/<plugin>:<skill>`; standalone `/<skill>` | Relevance match unless disabled | V01/V02, 2026-09-28; plugin prefix is host-added, not part of frontmatter name. |

These are three different acts: managing a plugin, explicitly selecting a skill,
and asking naturally for a task. Natural language such as “review this change”
may select a skill, but does not count as proof that the user explicitly invoked
a native command. A skill can also be discovered without being selected.
Sources C02/O05/G03/V02; checked 2026-09-28; limitation: matching is model- and
configuration-dependent.

## Installation and maintenance vocabulary

| Target | Native route documented | Scope / update distinction | Source / checked / limit |
| --- | --- | --- | --- |
| Claude Code CLI | `claude plugin marketplace add <source>`; `claude plugin install <plugin>@<marketplace> --scope <user-or-project-or-local>` | `claude plugin update` / `uninstall` target actual installed scope; catalog update is separate | C06, 2026-09-28; placeholders only, no commands executed. |
| Claude Code VS Code | Claude `/plugins` UI, select marketplace/plugin/scope | User/project/local choices; shared settings with CLI, but independent UI test required | C05/C06, 2026-09-28; no scope mutation performed. |
| Codex CLI | `codex plugin marketplace add <source>`, then `/plugins` | `marketplace upgrade` refreshes sources; browser install/uninstall/toggle; start new session | O01/O04, 2026-09-28; exact custom-source payload update lifecycle UNKNOWN. |
| Codex IDE Extension | **UNSUPPORTED** native plugin route | Standalone skill authoring/discovery is not plugin installation | O04/O05, 2026-09-28; retain REQ-004/005 gap. |
| GitHub Copilot CLI | `copilot plugin marketplace add <source>`; `copilot plugin install <spec>` | `copilot plugin update <name>` / `uninstall <name>`; user-home storage and policy/repo activation controls | G01, 2026-09-28; no invented `--scope project` flag. |
| GitHub Copilot VS Code | Extensions/Customizations install or `Chat: Install Plugin From Source` | Global/workspace enablement; update checking and uninstall in UI | V01, 2026-09-28; CLI-discovered and locally registered sources require lifecycle testing separately. |

## Curated listing versus custom source

| Ecosystem | Curated/public listing | Custom source | Limitation / source / checked |
| --- | --- | --- | --- |
| Claude | Anthropic official marketplace is distinct from other marketplaces | Add a Git/local/hosted catalog explicitly | C06, 2026-09-28; adding a catalog does not submit or approve a plugin for the official listing. |
| OpenAI | Shared universal public directory, publication/review path | Repo/personal catalogs and configured Git/local sources | O01/O04, 2026-09-28; local catalog may call itself “curated”, but that is not OpenAI curation or surface-wide availability. |
| Copilot CLI | Marketplace discovery depends on registered sources | Direct local/repo/Git install and custom catalogs | G01/G02, 2026-09-28; a successful direct install would not establish publisher verification. |
| Copilot VS Code | Default discovery sources include copilot-plugins and awesome-copilot | Additional `chat.plugins.marketplaces`, direct source or local path | V01, 2026-09-28; marketplace trust prompt is not certification/security proof. |

Publication requires [owner decisions](../build/DECISIONS.md). This prompt has
not checked/reserved name availability or submitted to any directory.

## Required later invocation evidence

For each target independently, capture host/extension version, OS, harness,
account/policy conditions without secrets, package/source revision, install scope,
discovered skill identity and exact prompt. Compare explicit selection, intended
implicit selection, unrelated prompt, manual-only/hidden behavior where supported,
name collisions and disabled plugin. Record the actual loaded instruction/resource
paths and any permission prompts. These are **planned checks**, not test results.

The eight public skills remain Init, Requirement, Implement, Review, Test,
Security, Architecture and Memory. Router, Governance Review, Skill Audit and
Self-check stay shared procedures. Prompt 03 will map these logical identities
to native names within supported surfaces; this research creates no commands.


## Prompt 20 concrete Claude mapping

The [native reference](../../platforms/claude/resources/activation.md) lists all
eight /kiyo-compass:<skill> selectors for the prepared development manifest.
Name/description frontmatter stays canonical. Logical modes are request text,
not extra commands; /kiyo-init is not supplied. These are DOCUMENTED_ONLY names,
not VERIFIED invocations. Source/date/limitations and CLI/VS Code observations:
[Claude field map](claude-package.md), checked 2026-09-29.
Both live targets remain NOT_TESTED. The current
[disposable protocol](claude-installation-test-protocol.md) supersedes historical
Claude lifecycle examples for future testing; nothing was installed or published.

## Prompt 21 Codex mapping

The [shipped adapter](../../platforms/codex/resources/activation.md) maps all eight
logical IDs to their actual canonical names and intent. Choose the discovered
Kiyo entry via native /skills/$ UI; do not guess a plugin-qualified alias from
the manifest ID or copy the Claude selector. Mode words remain logical UX.
Version/help observation is not a successful Kiyo invocation.

The [current guide](codex-package.md), [protocol](codex-local-test-protocol.md) and
[submission gates](codex-submission.md) separate selected fields, actual offline
checks, stricter ingestion failure and untested host behavior. Both native target
results remain NOT_TESTED; IDE plugin capability remains UNSUPPORTED.

