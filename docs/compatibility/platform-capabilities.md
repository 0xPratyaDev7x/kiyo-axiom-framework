# Kiyo Axiom Framework — Platform capabilities

Original research: **2026-09-28**; Claude, Codex and Copilot refreshed **2026-09-29**.
Copilot's [Prompt 22 field map](copilot-package.md) / CP22-01–16 supersedes its
historical tables below. Claude/Codex refreshes are in
[Prompt 20 field map](claude-package.md) / CL20-01–CL20-13 and
[Prompt 21 field map](codex-package.md) / CX21-01–CX21-12. Sources: [source register](../research/SOURCES.md).
C/O/G/V/A IDs below identify its exact official source rows. Every capability is
DOCUMENTED_ONLY unless explicitly marked otherwise. The [Prompt 26 live matrix](live-test-matrix.md) supersedes the blanket
NOT_TESTED baseline for bounded native management/discovery checks only. All model
behavior and activation remain NOT_TESTED. Prompt 20 observes only Claude CLI --version and named extension
metadata. Prompt 21 observes Codex version/help and named extension metadata;
active IDE/account contexts remain unknown. Prompt 22's bounded lookup did not resolve
copilot on PATH or matching extension metadata in the inspected standard directory;
alternative/active environments remain UNKNOWN. Offline checks are separate.

## Target summary

| Target | Native plugin capability | Observed version | Live state | Principal gap / sources (refreshed 2026-09-29) |
| --- | --- | --- | --- | --- |
| Claude Code CLI | DOCUMENTED_ONLY plus bounded native observations | CLI 2.1.220 (2026-09-29) | VERIFIED subset; behavior NOT_TESTED | [P26 evidence](../evidence/live/claude-cli.json): normal validation warns, strict FAIL; directory/ZIP inventory finds eight Skills; marketplace/agent loading pending |
| Claude Code VS Code | DOCUMENTED_ONLY; shared development bundle | Extension manifests 2.1.283 / 2.1.284; active version UNKNOWN (2026-09-29) | NOT_TESTED | CL20-04; independent extension loading/engine/cache/lifecycle pending |
| Codex CLI | DOCUMENTED_ONLY plus bounded native observations | codex-cli 0.158.0 (2026-09-29) | VERIFIED local install/cache/uninstall subset; behavior NOT_TESTED | [P26 evidence](../evidence/live/codex-cli.json): temporary local catalog/cache/removal observed; ingestion FAIL still open; exact skill selector/update/activation pending |
| Codex IDE Extension | UNSUPPORTED for native plugins | Extension metadata 26.917.62051; active version UNKNOWN (2026-09-29) | NOT_TESTED | CX21-04/06/07; standalone mechanism separate and not adopted as fallback, DEC-004 |
| GitHub Copilot CLI | DOCUMENTED_ONLY; static bundle prepared | UNKNOWN; not resolved on inspected PATH | NOT_TESTED | CP22-01–16; exact plugin selector/collision and rule loading remain UNKNOWN; no native parser/install |
| GitHub Copilot VS Code | DOCUMENTED_ONLY; shared static bundle | UNKNOWN; scoped extension metadata lookup had no matches | NOT_TESTED | CP22-07/08/09; official source fallback read; independent UI/harness/loading/lifecycle untested |

P26 [environment](../evidence/live/environment.json) also observes editor 1.139.1
and the same named Claude/Codex extension metadata; active IDEs remain UNKNOWN.
The Copilot lookups are still bounded negative observations, not proof of absence.

## Shared schema boundary

Agent Plugins **1.0.0** uses root `plugin.json` with required `$schema` equal to
`https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` and required `name`.
Optional keys are `version`, `description`, `author`, `homepage`, `repository`,
`license`, `keywords`, `extensions`. The JSON schema is closed
(`additionalProperties: false`); name is 1–64 characters, lowercase alphanumeric,
hyphen or period, with alphanumeric ends and no consecutive hyphens/periods.
It does not define portable `rules`, `skills` path overrides or a `core` field.
Host documentation may describe ignoring unknown fields; that is not schema
validity. OpenAI and both Copilot targets document this format; Claude's own
reference documents its separate manifest. No universal Claude support is inferred.
**Sources A01, O01, G01, V01; checked 2026-09-28; limitation:** schema inspected,
not executed against a package.

Static-only feasibility means a native manifest plus eight Markdown skills and
packaged references/templates. Omit MCP, hooks, scripts, agents, automations,
network services and dependency declarations. Having those optional capabilities
in a host does not make them necessary for Kiyo. This is a **design inference**
from C01/C07/O01/O02/G02/V01, constrained by the Build Contract; implementation
is deferred. A native plugin is currently unavailable for the Codex IDE target.

## Claude Code CLI

The table below retains Prompt 02 findings. Prompt 20's current schema/layout,
actual development bundle, native invocation and local observations are in
[Claude package](claude-package.md), checked 2026-09-29. Historical “no package”
statements below are superseded for static artifacts only; live tests stay pending.

| # | Topic | Documented capability / finding | Evidence and limitation |
| --- | --- | --- | --- |
| 1 | Manifest schema / file | `.claude-plugin/plugin.json`; manifest optional with conventional layout. If present, `name` is required; metadata and `skills` path string/array are available. Unknown top-level keys are stripped with validator warnings. | C04; 2026-09-28; do not add a fictitious `core` or `rules` key. Native validation NOT_RUN. |
| 2 | Installation / marketplace | `claude plugin marketplace add <source>`, then `claude plugin install <plugin>@<marketplace>`; interactive `/plugin`. Marketplace catalog convention is `.claude-plugin/marketplace.json`. GitHub, Git, local and hosted catalogs documented. | C06; 2026-09-28; discovery is not official listing acceptance. |
| 3 | Skill directory / frontmatter | `skills/<name>/SKILL.md`; YAML at file start. Claude currently makes fields optional, recommends `description`, and can derive `name`. Kiyo can explicitly supply both for portability. | C02/C07; 2026-09-28; host extensions must not be copied to other targets unchecked. |
| 4 | Explicit invocation | `/<plugin>:<skill>`; standalone skills use `/<skill>`. | C01/C07; 2026-09-28; Kiyo identifiers not yet finalized or tested. |
| 5 | Automatic selection | Description-based selection; default exposes description and loads body on invocation. `disable-model-invocation: true` disables model activation; `user-invocable: false` hides direct invocation. | C02; 2026-09-28; selection is conditional, not a promise that all work runs through Kiyo. |
| 6 | Project instructions / core | Project `CLAUDE.md` or `.claude/CLAUDE.md`, user guidance and applicable `.claude/rules` are separate discovery channels. **UNSUPPORTED:** automatically loading a plugin-root `CLAUDE.md` as project context. | C03/C07 explicitly document this exclusion; 2026-09-28; install alone does not load arbitrary core files. |
| 7 | Actual plugin rules | No plugin `rules` component is defined in C04/C07's complete field/component reference. The native project/user rules mechanism is C03. Proposed plugin `rules` field: **UNSUPPORTED** under that schema; any undocumented folder auto-loader: **UNKNOWN**. | C03/C04/C07; 2026-09-28; skills are advisory instructions, not host permission rules. |
| 8 | Relative resources | Manifest paths start `./`, resolve inside plugin root and must exist. Skill content supports `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_SKILL_DIR}`; root can change with versioned cache. | C02/C04/C07; 2026-09-28; use packaged resources, never author checkout paths; relocation NOT_TESTED. |
| 9 | Install/update/uninstall scope | User, project, local; managed settings can restrict changes. Shell install defaults to user; maintain with `claude plugin update/uninstall` and explicit scope. Project enablement alone does not download collaborators' copies. | C06; 2026-09-28; inspect actual scope before later mutation; no lifecycle operation run. |
| 10 | Version / OS / account | C08 lists macOS 13+, Windows 10 1809+/Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+, x64/ARM64 and 4 GB RAM. Authentication/provider setup required. Plugin minimum supported version for Kiyo: **UNKNOWN**. | C08/C06; 2026-09-28; feature gates such as one-command marketplace install v2.1.275 are not a universal minimum; owner/test matrix pending. |
| 11 | Evidence / limits | DOCUMENTED_ONLY; live **NOT_TESTED**. No package, validator result, metadata/core loading trace or cache test exists. | C01–C08; 2026-09-28; future CLI evidence cannot stand in for IDE evidence. |

## Claude Code VS Code

The table below retains Prompt 02 findings. Prompt 20's current schema/layout,
actual development bundle, native invocation and local observations are in
[Claude package](claude-package.md), checked 2026-09-29. Historical “no package”
statements below are superseded for static artifacts only; live tests stay pending.

| # | Topic | Documented capability / finding | Evidence and limitation |
| --- | --- | --- | --- |
| 1 | Manifest schema / file | Extension manages the Claude plugin system: `.claude-plugin/plugin.json` and C04's fields. | C05 explicitly says plugin management uses CLI commands/settings; C04; 2026-09-28; documentary linkage, no inferred live parity. |
| 2 | Installation / marketplace | Type `/plugins` in the Claude panel; use Plugins and Marketplaces tabs to install/add sources. | C05; 2026-09-28; not VS Code's Copilot `@agentPlugins` UI. |
| 3 | Skill directory / frontmatter | Claude plugin `skills/<name>/SKILL.md`, with C02 frontmatter. | C05/C02/C07; 2026-09-28; bundled CLI version may differ from terminal CLI. |
| 4 | Explicit invocation | Claude panel's slash commands expose plugin skills as `/<plugin>:<skill>`. | C05's prompt-box integration, C06 confirmation workflow; 2026-09-28; exact Kiyo menu entry NOT_TESTED. |
| 5 | Automatic selection | Claude description-based skill selection in the extension's Claude session. | C05/C02; 2026-09-28; no IDE activation trace or guarantee of selection. |
| 6 | Project instructions / core | Native Claude project guidance remains separate from installed skill metadata; plugin-root `CLAUDE.md` is **UNSUPPORTED** as automatic project context. | C05/C03/C07; 2026-09-28; project discovery must be tested in the actual extension workspace/remote environment. |
| 7 | Actual plugin rules | Same documented plugin components; no supported plugin `rules` field. Project `.claude/rules` is a different mechanism. | C04/C05/C07; 2026-09-28; do not interpret Copilot rules support as Claude extension support. |
| 8 | Relative resources | Claude plugin/skill-root substitution and contained relative package paths apply to the documented shared plugin engine. | C05/C02/C04; 2026-09-28; remote extension paths and cache relocation NOT_TESTED. |
| 9 | Install/update/uninstall scope | UI offers user, project and local scope; CLI and extension share settings on a computer. Changes apply to open sessions, with reload/restart recovery if needed; maintenance uses shared plugin management. | C05/C06; 2026-09-28; uninstall effects across scopes must be checked separately. |
| 10 | Version / OS / account | VS Code 1.94.0+; paid Claude plan (Pro/Max/Team/Enterprise) or Console account; provider alternatives documented. Extension bundles its CLI; terminal CLI is separate. | C05/C08; 2026-09-28; platform binary availability matters; exact Kiyo extension floor and actual version UNKNOWN. |
| 11 | Evidence / limits | DOCUMENTED_ONLY; live **NOT_TESTED** independently of CLI. | C05; 2026-09-28; no extension installed or launched for this task. |

## Codex CLI

Prompt 21 [current field map](codex-package.md) and [protocol](codex-local-test-protocol.md)
supersede old no-package/version observations below for Codex. Twelve sources were
rechecked on 2026-09-29. The detailed table retains the historical Prompt 02 baseline;
CLI live state is NOT_TESTED and IDE native plugins remain UNSUPPORTED/NOT_TESTED.

| # | Topic | Documented capability / finding | Evidence and limitation |
| --- | --- | --- | --- |
| 1 | Manifest schema / file | Portable root `plugin.json` per A01; OpenAI extension data under `extensions.com.openai`. Legacy `.codex-plugin/plugin.json` remains a fallback; its `skills: "./skills/"` is for legacy packaging, not a portable path override. | O01/A01; 2026-09-28; do not combine portable and legacy semantics. |
| 2 | Installation / marketplace | `/plugins` opens CLI browser for configured marketplaces. `codex plugin marketplace add/list/upgrade/remove` manages sources. Repo/personal catalog convention: `.agents/plugins/marketplace.json`. | O04/O01; 2026-09-28; O01 emphasizes desktop local testing; custom CLI lifecycle needs a trial. |
| 3 | Skill directory / frontmatter | Plugin `skills/<name>/SKILL.md`; YAML `name`, `description` required. Standalone repo/user discovery uses `.agents/skills`; `agents/openai.yaml` is optional. | O01/O05; 2026-09-28; not the same as installing a plugin. |
| 4 | Explicit invocation | `/skills` selector or `$<skill>` mention. | O05; 2026-09-28; exact plugin-qualified Kiyo selector spelling remains UNKNOWN until observed; do not invent `/kiyo:...` for Codex. |
| 5 | Automatic selection | Model can match description; initial metadata includes name, description and path; full body is read on use. Invocation policy can be configured via optional OpenAI metadata. | O02/O05; 2026-09-28; initial catalog can truncate descriptions or omit skills when budget is exceeded. |
| 6 | Project instructions / core | `AGENTS.override.md` / `AGENTS.md` chain: global then project root to current directory, once per run; default combined cap 32 KiB. No documented plugin-install core injection. | O03; 2026-09-28; a Markdown link is not evidence of automatic import. |
| 7 | Actual plugin rules | Portable schema has no rules component; O01 does not document a plugin-wide instruction-rule loader. **UNKNOWN** for such extension behavior; proposed top-level `rules/core` is **UNSUPPORTED** in A01. | O01/A01; 2026-09-28; host command-policy rules are not Kiyo project guidance. |
| 8 | Relative resources | O01 paths are plugin-root relative with `./`; A02 resources resolve from skill root. Package all references with skills. O01's explicit cache path describes desktop local installs. | O01/A02; 2026-09-28; exact CLI cache layout/substitutions UNKNOWN; no `${CLAUDE_PLUGIN_ROOT}` assumption. |
| 9 | Install/update/uninstall scope | Browser installs/uninstalls environment bundles and toggles installed entries. Bundled skills available in new session. Marketplace `upgrade` refreshes sources; it is not proof of installed payload replacement. | O04/O01; 2026-09-28; repo/personal catalogs and enablement settings are distinct from install scope; exact CLI update persistence UNKNOWN. |
| 10 | Version / OS / account | CLI page exposes macOS/Linux and Windows installation routes and ChatGPT/available sign-in methods. O04 permits supported curated plugins with API-key login, with OAuth-dependent exclusions. | O07/O04; 2026-09-28; pictured v0.117.0-alpha.15 is an example, not a minimum; OS floors and Kiyo host floor UNKNOWN. |
| 11 | Evidence / limits | DOCUMENTED_ONLY; live **NOT_TESTED**. | O01–O07; 2026-09-28; current assistant tools are not a native Kiyo CLI test. |

## Codex IDE Extension

Prompt 21 [current field map](codex-package.md) and [protocol](codex-local-test-protocol.md)
supersede old no-package/version observations below for Codex. Twelve sources were
rechecked on 2026-09-29. The detailed table retains the historical Prompt 02 baseline;
CLI live state is NOT_TESTED and IDE native plugins remain UNSUPPORTED/NOT_TESTED.

| # | Topic | Documented capability / finding | Evidence and limitation |
| --- | --- | --- | --- |
| 1 | Manifest schema / file | Native plugin manifest loading **UNSUPPORTED** in this target. O01's schema describes supported plugin surfaces, not this extension. | O04; 2026-09-28; no IDE plugin manifest should be generated. |
| 2 | Installation / marketplace | Native plugin browser/install **UNSUPPORTED**; official guidance redirects users to desktop or CLI. Standalone skills are separately supported. | O04/O05; 2026-09-28; file-copy skills do not satisfy REQ-004 native plugin installation. |
| 3 | Skill directory / frontmatter | Standalone `.agents/skills/<name>/SKILL.md` in repository/user scope; required `name`, `description`; optional `agents/openai.yaml`. | O05 explicitly includes IDE; 2026-09-28; fallback is informational, not an approved change to product scope. |
| 4 | Explicit invocation | Standalone `/skills` or `$<skill>`. Plugin invocation **UNSUPPORTED**. | O05/O04; 2026-09-28; fallback invocation NOT_TESTED. |
| 5 | Automatic selection | Description matching for standalone skills is DOCUMENTED_ONLY. Plugin skill activation **UNSUPPORTED**. | O05/O04; 2026-09-28; do not transfer CLI plugin activation results. |
| 6 | Project instructions / core | Codex project instruction chain uses `AGENTS.md`; persistent core guidance requires that separate setup. | O03/O06; 2026-09-28; working directory/remote extension behavior NOT_TESTED. |
| 7 | Actual plugin rules | **UNSUPPORTED** because plugins are unavailable; native project instructions remain distinct. | O04; 2026-09-28; no plugin policy parity claim. |
| 8 | Relative resources | Standalone skill resources can be packaged beneath the skill root (A02). Plugin-cache resolution is **UNSUPPORTED / not applicable** here. | O05/A02/O04; 2026-09-28; no cache path invented. |
| 9 | Install/update/uninstall scope | Native plugin lifecycle **UNSUPPORTED**. Standalone skills have repository/user discovery and local enablement configuration, a different lifecycle. | O04/O05; 2026-09-28; do not offer a central Kiyo installer. |
| 10 | Version / OS / account | O06 requires extension installation/enablement and sign-in; lists VS Code and compatible editors. Inspected page does not establish exact OS/editor minimums or a plugin-enabled version. | O06/O04; 2026-09-28; versions/account availability UNKNOWN; upgrading is not an evidenced fix. |
| 11 | Evidence / limits | Plugin capability **UNSUPPORTED** by current docs; live **NOT_TESTED**. Standalone skills DOCUMENTED_ONLY. | O04/O05; 2026-09-28; six-target native release blocked until scope/capability changes, architecture research can proceed. |

## GitHub Copilot CLI

The following table preserves the Prompt 02 baseline. [Prompt 22](copilot-package.md)
revalidates this target on 2026-09-29 and prepares a shared static artifact with
independent evidence columns. Historical no-package observations are superseded;
native results remain NOT_TESTED and rule-loader semantics remain UNKNOWN.

| # | Topic | Documented capability / finding | Evidence and limitation |
| --- | --- | --- | --- |
| 1 | Manifest schema / file | Agent Plugins 1.0 root `plugin.json` per A01. Legacy `name` required; optional metadata/component paths. Legacy lookup: `.plugin/plugin.json`, root `plugin.json`, `.github/plugin/plugin.json`, `.claude-plugin/plugin.json`. | G01/A01; 2026-09-28; exact schema opt-in changes semantics; unknown keys are reported/ignored by host. |
| 2 | Installation / marketplace | `copilot plugin install <spec>` supports registered `plugin@marketplace`, repo/subdir, Git URL, local directory. Marketplace add/browse commands available; catalog lookup includes root, `.plugin`, `.github/plugin`, `.claude-plugin`. | G01/G02; 2026-09-28; catalog refresh differs from installed-plugin update. |
| 3 | Skill directory / frontmatter | Portable `skills/<name>/SKILL.md` fixed; legacy path configurable. Required YAML `name`, `description`; optional license. Standalone repo `.github/.claude/.agents` skill locations; personal `.copilot/.agents`. | G01/G03; 2026-09-28; host accepts more fields, but permission preapproval is not portable. |
| 4 | Explicit invocation | Include `/<skill-name>` in prompt; inspect `/skills list` and `/skills info`. | G03; 2026-09-28; retrieved example does not establish plugin-prefix collision syntax; that exact spelling is UNKNOWN. |
| 5 | Automatic selection | Prompt/description matching then SKILL.md injection. Project/personal duplicate skill names can shadow plugin skills (first found wins). | G03/G01; 2026-09-28; installed does not mean selected or even winning discovery. |
| 6 | Project instructions / core | Repository `.github/copilot-instructions.md`, `AGENTS.md` and other documented files; user instructions; path-specific `*.instructions.md` with `applyTo`. Relative `@file` includes only in supported instruction files and within allowed root. | G04; 2026-09-28; multiple files combined without general precedence; external cache imports cannot be assumed. |
| 7 | Actual plugin rules | Portable client-specific `com.github.copilot/rules/` is documented. Portable top-level `rules` field is **UNSUPPORTED**. | G01/G02; 2026-09-28; complete rule frontmatter, trigger timing and always-on precedence remain **UNKNOWN** in retrieved pages; do not choose as core-loader contract yet. |
| 8 | Relative resources | G03 discovers supporting files in the skill directory; A02 uses skill-root references. Installed paths under `~/.copilot/installed-plugins/` differ for marketplace/direct sources. | G01/G03/A02; 2026-09-28; `PLUGIN_ROOT` MCP/LSP substitution is not evidence of substitution in Markdown; relocation NOT_TESTED. |
| 9 | Install/update/uninstall scope | User-home plugin storage; `copilot plugin update NAME`, `uninstall NAME`, enable/disable. Organization/MDM or repository enablement can control activation. Local-directory marketplace path sources can load in place after restart. | G01; 2026-09-28; do not invent Claude-style `--scope project`; uninstall effects on bootstrap files need separate tests. |
| 10 | Version / OS / account | All Copilot plans; organization-provided access requires CLI policy enabled. Quickstart offers Windows and macOS/Linux installation; the npm route requires Node.js 22+. | G05; 2026-09-28; Node is a host-installation-route prerequisite, not a Kiyo payload dependency. Plugin minimum, OS floors and installed version UNKNOWN. |
| 11 | Evidence / limits | DOCUMENTED_ONLY; live **NOT_TESTED**. Rule semantics and exact plugin-skill selector need follow-up. | G01–G05; 2026-09-28; GitHub CLI `gh skill` is standalone-skill tooling, not proof of plugin installation. |

## GitHub Copilot VS Code

The following table preserves the Prompt 02 baseline. [Prompt 22](copilot-package.md)
revalidates this target on 2026-09-29 and prepares a shared static artifact with
independent evidence columns. Historical no-package observations are superseded;
native results remain NOT_TESTED and rule-loader semantics remain UNKNOWN.

| # | Topic | Documented capability / finding | Evidence and limitation |
| --- | --- | --- | --- |
| 1 | Manifest schema / file | Root `plugin.json` with Agent Plugins schema; root legacy Copilot, `.claude-plugin/plugin.json` Claude, `.plugin/plugin.json` legacy OpenPlugin also recognized. | V01/A01; 2026-09-28; format recognition does not equal every other host's behavior. |
| 2 | Installation / marketplace | Extensions filter `@agentPlugins`, Customizations Plugins tab, or `Chat: Install Plugin From Source`. Custom sources via `chat.plugins.marketplaces`; local registration via `chat.pluginLocations`. | V01; 2026-09-28; agent plugin is not a VSIX requiring a Kiyo extension/runtime. |
| 3 | Skill directory / frontmatter | Portable `skills/<name>/SKILL.md`. YAML requires `name` (matching directory; max 64, lowercase/digits/hyphens), `description` (max 1024). `user-invocable`, `disable-model-invocation` supported. | V02/V01; 2026-09-28; colons/slashes in name cause loading failure; namespace is supplied by host. |
| 4 | Explicit invocation | Plugin `/<plugin>:<skill>`; standalone `/<skill>`; `/skills` opens configuration. | V02; 2026-09-28; not copied to Copilot CLI without evidence. |
| 5 | Automatic selection | Metadata discovery, relevant SKILL.md loading, then optional resources. Manual-only and hidden-menu controls differ. | V02; 2026-09-28; matching/settings/harness affect activation; not every-turn core loading. |
| 6 | Project instructions / core | Copilot harness recommends `.github/copilot-instructions.md` or `AGENTS.md`; targeted `.github/instructions/**/*.instructions.md`. Local harness has separate settings/compatibility formats. | V03; 2026-09-28; no effect on inline suggestions; record selected harness in live evidence. |
| 7 | Actual plugin rules | `com.github.copilot/rules/` in Agent Plugins is a documented client extension; other clients may ignore it. | V01; 2026-09-28; rule parsing/trigger semantics and installation-time core loading **UNKNOWN**; no universal rule overlay yet. |
| 8 | Relative resources | Markdown or `#file:` references relative to SKILL.md. Plugin-root tokens are documented for hooks/MCP, not blanket Markdown substitution. | V02/V01; 2026-09-28; package resources under skill root; cache relocation NOT_TESTED. |
| 9 | Install/update/uninstall scope | UI enables/disables globally or per workspace; discovers CLI-installed plugins separately. Update check command or 24-hour checks when auto-update enabled. External-source uninstall removes disk copy; marketplace-inline plugins can remain on disk inactive. | V01; 2026-09-28; shared bootstrap cleanup and remote/profile effects not tested. |
| 10 | Version / OS / account | GitHub account with Copilot access; eligible accounts can use Free, organization policies apply. `chat.plugins.enabled` must be true. | V04/V01; 2026-09-28; exact plugin editor/extension minimum and OS floors absent from inspected pages: UNKNOWN, not guessed from Claude's requirement. |
| 11 | Evidence / limits | DOCUMENTED_ONLY; live **NOT_TESTED** independently from Copilot CLI. | V01–V04; 2026-09-28; harness, extension and workspace must be captured in later tests. |

## Decisions this evidence permits

Prompt 03 may design a static, self-contained canonical content model with
host-specific loading boundaries. It must preserve the Codex IDE plugin gap and
avoid committing to undocumented Copilot rule semantics, Codex plugin-qualified
selector syntax or cache paths. See [activation modes](activation-modes.md) and
[invocation map](native-invocation-map.md). No native payload was created here.

## Prompt 22 Copilot boundary

The independently documented intersection is Agent Plugins 1.0.0 with root
plugin.json and eight skills. CLI documentation also accepts 1.1.0; this does
not establish VS Code 1.1.0 support. No optional rules or component override is
used. [Current delta](copilot-package.md) separates schema, naming, source
lifecycle, account/version limits and instruction discovery for both clients.
The original shared-schema/decision tables above are historical design inputs;
the three native prompts now have scoped artifact evidence, not live acceptance.

