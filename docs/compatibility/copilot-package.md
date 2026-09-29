# Copilot package and independent target capabilities

Checked **2026-09-29**. Source IDs CP22-01–16 resolve through the
[source register](../research/SOURCES.md#prompt-22-copilot-revalidation).
Every native capability in this document is DOCUMENTED_ONLY; each row inherits
this checked date. Both Kiyo live targets are NOT_TESTED. Offline checks are
[separate evidence](../evidence/copilot/package-checks.md).

## Four different products

| Surface | Meaning for this task | Source / limitation |
| --- | --- | --- |
| Copilot CLI plugin | Terminal-host bundle with native component discovery/lifecycle | CP22-01/02/05; no terminal installation tested |
| VS Code agent plugin | Static customization bundle managed by agent-plugin facilities | CP22-07/08; shared format does not establish same behavior |
| VSIX extension | Separate VS Code extension packaging/publication mechanism | CP22-14; no Kiyo VSIX, extension activation code or package.json is needed |
| GitHub App-based Copilot Extension/service | Distinct server integration; GitHub's notice schedules its sunset for 2025-11-10 | CP22-15; announcement, not an operational account test; no App/service or MCP replacement is in Kiyo scope |

GitHub Apps, cloud agents, OpenCode, other harnesses/ecosystems and Actions
execution are outside this launch scope. A source page describing them does not
authorize adding them.

## Selected native format and field justification

Use one root **plugin.json** at dist/copilot/kiyo-axiom-framework. CLI and VS Code
independently document Agent Plugins 1.0.0; the CLI also documents 1.1.0, but
VS Code support for that newer marker was not established here. Selecting 1.0.0
is the evidenced intersection, not a claim that every client extension is portable.
CP22-01/02/07/10/11; no native parser run.

| Shipped field / file | Meaning and basis | Limit |
| --- | --- | --- |
| $schema | Exact Agent Plugins 1.0.0 schema URL; required, CP22-10 | Format identity, not product release version |
| name: kiyo-axiom-framework | Required package ID derived from existing working name; lowercase valid form, CP22-10 | No publication reservation or owner-final identity |
| description | Optional string describing actual static content, CP22-10 | Does not grant permissions |
| `skills/<name>/SKILL.md` | Immediate native skill directories, CP22-02/07 | No component-path override field or root SKILL.md fallback |
| YAML name / description | Existing canonical names and matching directories, CP22-03/08 | Eight plain slugs; no manual namespace in frontmatter |
| references/kiyo and references/copilot | Relative linked Markdown resources, CP22-03/08 plus packaging design | Files are installed; actual host reads still untested |
| LICENSE | Byte copy of existing repository legal file | Final publication-license confirmation still required |

The inspected JSON schema requires only $schema/name and excludes unknown
top-level properties. Description is a string; name is 1–64 characters with
documented character and boundary restrictions. The local packager checks the
three selected fields, with no schema download at consumer time.
Native acceptance and optional-field/full operational conformance are not implied.

No version, author, repository URL, publisher ID, marketplace ID or signature is
invented. No compatibility manifest is necessary for this selected shared format.
No extensions.com.github.copilot metadata, allowed-tools, visibility fields,
agents/openai.yaml, rule folder, permissions or safety flags are needed.

## CLI versus VS Code delta

| Topic | Copilot CLI | Copilot VS Code | Sources / limitation |
| --- | --- | --- | --- |
| Manifest/discovery | Root recognized 1.0.0 marker; fixed skills directory | Same 1.0.0 root format and skills discovery | CP22-01/02/07; older installed versions need their own test |
| Native source | Local directory, repo/subdir, Git URL or registered catalog | Source Git URL, catalog UI or explicit local plugin location | CP22-01/05/07; source registration can write native state |
| Skill metadata | name/description plus optional native fields | Matching name/directory, <=64 name and <=1024 description | CP22-03/08; Kiyo ships only common name/description |
| Explicit use | /skills list/info; generic `/<skill-name>` documented, exact plugin qualification UNKNOWN | Slash menu /kiyo-axiom-framework:<skill>; /skills configuration | CP22-03/08; CLI built-in/name collisions require observation |
| Inferred use | Prompt/description match followed by entry injection | Metadata, selected body, then relevant referenced resources | CP22-03/08; neither promises selection on every request |
| Project guidance | Applicable .github/copilot-instructions.md and path-specific applyTo; instruction files combined | Copilot Agent Host or Local session instructions; selected harness/settings matter | CP22-04/09; preserve conflicts/scope, no universal precedence |
| Plugin rules | com.github.copilot/rules component location documented | Same namespace listed | CP22-01/07; exact rule trigger/frontmatter/always-on semantics UNKNOWN; omitted |
| Resources/cache | Direct local installs cached; reinstall after source edits; local-directory marketplace path sources can load in place after restart | Relative skill references; native stores/source types differ | CP22-02/01/08; do not substitute MCP/hook PLUGIN_ROOT expansion for Markdown resolution |
| Lifecycle | Named update/disable/enable/uninstall; separate catalog refresh | UI workspace/global enablement, update check, source-dependent uninstall | CP22-01/05/07; independent preservation trials required |
| Version/OS/account | All Copilot plans; organization CLI policy; Windows PowerShell >=6; npm route Node >=22 | GitHub account/Copilot access, eligible Free and organization policy; plugins enabled | CP22-12/13/07; exact Kiyo plugin minimum/editor/OS floors UNKNOWN |
| Local observation | copilot not resolved by scoped PATH lookup | No matching github.copilot* metadata in inspected standard extension directory | Local check only; alternative installations/remote/bundled harness and active versions UNKNOWN |

A CLI install may be discovered by VS Code (CP22-07); that is an additional
interaction to test, not evidence for the IDE row. It is not approval to install
globally. Native managed restrictions still apply; Markdown cannot weaken them.

## Core and project adapter

Use the [shipped adapter](../../platforms/copilot/resources/activation.md) for
eight logical mappings, preservation and module-scope rules. Core loading after
skill selection differs from metadata discovery and persistent project guidance.
An explicit or relevant implicit selection need not depend on Init; it still
needs readable packaged Core before actions. Installation itself performs no Init.

Approved Init may render the existing short init-locator-1 block into an actual
applicable project instruction file. No full Core copy, external cache import,
automatic hook or every-turn loading guarantee is supplied. A module-only
request cannot authorize a repository-wide block or widened applyTo pattern.
Existing project policy/Memory paths and human text stay user-owned.

## Canonical-to-package transform

[Developer packaging](../../tools/package_copilot.py) copies the 97 shared Markdown
resources into each skill, remaps only canonical entry destinations and appends
one conditional native-reference link. All long instructions remain authored
once. Native metadata is independently justified above; no Claude/Codex manifest
is consumed. Common file/hash helpers are reused without changing prior tools.

The generated artifact has eight public entries and no consumer executable,
MCP, Actions workflow, LSP, hooks, runtime dependencies or populated project state.
Inventory/source hashes are outside the payload. Consumers receive prepared files.
No directory publication or successful native invocation is inferred from building.

See [installation](copilot-installation.md), [protocol](copilot-local-test-protocol.md)
and [expected integration cases](../../tests/integration/copilot/scenarios.md).
