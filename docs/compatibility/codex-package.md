# Codex native development distribution

P26 follow-up: [native results](../evidence/live/codex-cli.json) establish
local disposable install/cache/uninstall. Public ingestion failure is unchanged;
installer fallback 1.0.0 is not an approved Kiyo release. No Skill/agent/IDE result.
The P21 statements below remain historical except for that bounded lifecycle.

Checked **2026-09-29**; [CX21-01–12](../research/SOURCES.md#prompt-21-codex-revalidation)
record actual official URLs, redirects and limits. Host capabilities here are
DOCUMENTED_ONLY unless a bounded local observation is explicitly identified.
CLI and IDE live Kiyo results are independently NOT_TESTED.

## Package choice and field map

[OpenAI packaging](https://developers.openai.com/plugins/build/plugins), CX21-01,
describes a portable root manifest and a supported compatibility layout.
Kiyo authors one [portable input](../../platforms/codex/plugin.json) and derives
the compatibility manifest from it. This is an OpenAI-specific packaging decision,
not a renamed Claude manifest. Output: dist/codex/kiyo-axiom-framework.

| Selected surface | Treatment / justification | Source and limitation |
| --- | --- | --- |
| root plugin.json | Agent Plugins 1.0.0 schema URL, working name and truthful description | CX21-01; current portable format; selected-field checks, not live host acceptance |
| extensions.com.openai.interface | displayName, shortDescription, longDescription, category, capabilities and defaultPrompt | CX21-01; presentation only, no tool grants; empty capabilities makes no catalog capability claim |
| .codex-plugin/plugin.json | Generated matching name/version/description/author/interface and skills: ./skills/ | CX21-01; supported compatibility path; portable inline interface wins, no merge |
| skills/<name>/SKILL.md | Eight unchanged canonical names/descriptions; remapped contained references | [Codex skills](https://learn.chatgpt.com/docs/build-skills), CX21-04; no universal host-mode parser |
| agents/openai.yaml | Omitted as optional and unnecessary for current CLI package | CX21-04; desktop appearance/dependency examples are not universal CLI/IDE obligations |
| version / author | 1.0.0 / 0xPratyaDev7x, owner-supplied 2026-09-30; Codex installs the cached plugin as version 1.0.0 | CX21-01 |
| interface.developerName | Omitted until owner supplies a real value | [Submission errors](https://developers.openai.com/plugins/deploy/submission-errors), CX21-10; required for ingestion/publication, so readiness is BLOCKED |
| apps / MCP / hooks / permissions / core / rules | No runtime components or invented enforcement fields | [Plugin architecture](https://developers.openai.com/plugins/concepts/plugins), CX21-02; skill-only is documented; absence of a general rule loader claim is not sandboxing |

All rows checked 2026-09-29. Root portable metadata may omit release version
under CX21-01; CX21-10's ingestion checks are stricter. The local bundled validator
actually returned FAIL for version, author and interface.developerName on
2026-09-29; version and author were supplied on 2026-09-30, so only
interface.developerName remains open (not re-validated with the bundled validator).
This is an unresolved ingestion/release gate, not a successful validation or proof
a native reader rejects all development use. Host acceptance remains NOT_TESTED.
See [checks](../evidence/codex/package-checks.md) and [publication gates](codex-submission.md).

The 105 canonical product files are unchanged. Every entry includes all 97 shared
resources inside references/kiyo and one Codex native reference. Copies are
generated; users never run the developer packager. Inventory identifies actual
source/output bytes. No reference requires this source checkout, a developer
path, a symlink outside payload or the original working directory.

## Native invocation guide

[CX21-04](https://learn.chatgpt.com/docs/build-skills) documents /skills and the
$ mention picker for Codex; relevance matching uses descriptions.
Use the [eight-entry map shipped with each skill](../../platforms/codex/resources/activation.md).
Pick the actual Kiyo source entry. Bare names such as init/review may collide
with other installed skills. Exact plugin-qualified spelling remains UNKNOWN:
this prompt did not open a native skill menu, and the inspected docs do not
establish a Kiyo-qualified spelling. No /kiyo-init or Claude selector is supplied.
A logical submode is natural-language intent, not an invented CLI argument.

Initial metadata is distinct from reading the selected body and Core. Implicit
selection can be possible without project bootstrap, but is not guaranteed.
Neither installation nor KIYO.md makes Core always-on. See
[activation adapter](../../platforms/codex/resources/activation.md) for authorized,
minimal AGENTS guidance and an explicit unavailable-skill response.

## CLI and IDE are separate targets

| Target | Capability / local observation | Remaining limits |
| --- | --- | --- |
| Codex CLI | Plugin browser documented by [CX21-06](https://learn.chatgpt.com/docs/plugins). Actual npm binary returned codex-cli 0.158.0; help exposes plugin add/remove and marketplace management | Version/help VERIFIED only in that command scope; Kiyo install/discovery/invocation/cache/update NOT_TESTED |
| Codex IDE Extension | CX21-06 explicitly excludes native plugins; CX21-04 separately documents standalone skills. Named extension metadata reports 26.917.62051 and vscode ^1.96.2 | Native plugin UNSUPPORTED; active extension/engine/editor version UNKNOWN; standalone Kiyo fallback not approved or generated; live NOT_TESTED |

[CLI setup](https://learn.chatgpt.com/docs/codex/cli), CX21-08, exposes
macOS/Linux/Windows setup and sign-in. [IDE setup](https://learn.chatgpt.com/docs/codex/ide),
CX21-07, identifies supported editor integrations and sign-in steps.
Exact Kiyo-tested OS/host minimums remain UNKNOWN. Local OS reports
Windows 10.0.26200; developer Python 3.11.9 is not a consumer requirement.
Account entitlement/provider/model/authentication were not inspected. CX21-06's
API-key support statement concerns supported curated plugins; it does not prove
this custom catalog works with the current account.

## Instructions, scope and lifecycle

[AGENTS discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
CX21-05, describes a per-run root-to-current-directory chain, override precedence
and a default combined 32 KiB limit. That native cap is distinct from Kiyo's
250-word managed-block and compact-Core budgets. A file at the wrong scope or
shadowed by existing instructions may not load. No AGENTS.override.md/global
settings edits or permission widening are part of Init.

The [packaged adapter](../../platforms/codex/resources/activation.md) preserves
human/nested instructions and uses actual instruction-file-relative Memory/config
locators. Module intent stays module-scoped. Successful insertion is only file
evidence; instruction loading and Core reads need separate observation.

Local catalogs, repo enablement and installed caches are distinct. The documented
desktop cache convention does not establish this CLI's exact cache layout.
Actual 0.158.0 help says marketplace upgrade refreshes Git snapshots; that alone
does not prove installed skill replacement. No generic Codex update or --scope
flag is invented. Use the [disposable protocol](codex-local-test-protocol.md)
to establish actual lifecycle and preserve project state before compatibility claims.
