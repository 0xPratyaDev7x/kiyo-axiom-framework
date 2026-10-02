# Native publication runbook — owner-operated, not executed

Checked **2026-09-29**. Status **BLOCKED / OWNER INPUT REQUIRED**.
This is a handoff, not permission to commit, tag, push, publish, submit, install
globally, change accounts or enable automatic publication. No credentials are
needed for the local [release rehearsal](runbook.md).
[Source register](../research/SOURCES.md#prompt-30-publication-source-check)
records actual destinations and limits; portal steps are DOCUMENTED_ONLY.

## Stop gates and exact candidate

Use [Final Acceptance](../build/FINAL-ACCEPTANCE.md) and
[owner actions](owner-actions.md) first. Product version is 1.0.0 (owner-supplied
2026-09-30, identical in all three manifests). The current ZIPs are not yet
submission-ready for any official directory (see OA-11 and OA-12). A build
identifier does not replace the owner-approved release version.

Before any future external action, obtain a real approved name/version/license,
publisher identity, prepared source/ref, destination, visibility, account authority
and release scope. Record approval for the exact artifact digest and destination.
Keep separate approvals for source publication, submission and final publication.
Resolve native metadata failures, route-specific gates and required host tests.
Never turn an unchecked box into an approval record.

When inputs are supplied, change canonical/native inputs deliberately, rebuild
to a fresh output using the existing developer runbook and rerun affected tests.
Review [security-sensitive changes](security-lifecycle.md), generated inventory,
signature status and disclosure arrangements. Signing remains NOT_SIGNED and
provenance NOT_ATTESTED until actual approved execution evidence exists.
Keep prior failed runs and support exclusions.

Tokens such as `<approved-source>` below are **documentation parameters**,
not executable commands or values shipped in a claimed-ready manifest.
Resolve them from owner evidence before use. Do not paste a guessed URL.

## Claude: choose a distribution channel

**Custom source/catalog**: prepare a plugin root containing the final
`.claude-plugin/plugin.json` and complete resources. Put its catalog at
`.claude-plugin/marketplace.json`, with the approved catalog/owner and matching
plugin name/source. Validate the plugin and catalog, then exercise an authorized
local marketplace before separately approved source publication.

Documented command forms, not executed here:

~~~text
claude plugin validate --strict <prepared-plugin-root>
claude plugin validate <prepared-marketplace-root>
claude plugin marketplace add <approved-source>
claude plugin install <plugin-name>@<marketplace-name>
claude plugin update <plugin-name>@<marketplace-name>
~~~

Resolve intended install scope through the [Claude protocol](../compatibility/claude-installation-test-protocol.md);
the bare install command must not be run against a real user's default state.
Current 2.1.220 strict failure remains recorded. A deliberate git-SHA version
strategy is documented, but no change to Kiyo's release policy is selected here.
Directory listing and the official marketplace are different routes; an official
marketplace request requires the relevant partner process.
Source: [Claude publication](https://code.claude.com/docs/en/plugins/publish),
PUB30-01, DOCUMENTED_ONLY; account/marketplace acceptance untested.

**Directory route**: after owner approval, use
[the developer portal](https://claude.ai/directory/manage).
The documented sequence is Submit new → Plugin bundle → Source
(repository, plugin path, tracked branch/tag) → Validate → Listing details →
Data handling → Compliance → Review and submit → Submit for review.
Use only owner-confirmed contact and attestations. A connected GitHub account
must have source write access; a private source must become public before listing.
Validation belongs to one commit and must be repeated after changes.
Track the scanned version; a passing version still needs the applicable Publish/
reviewer step. Keep automated publication disabled unless separately approved.
Source: [submission procedure](https://claude.com/docs/plugins/submit), PUB30-02;
UI/account operations NOT_RUN. Do not connect accounts or add webhooks in this task.

The [directory checklist](https://claude.com/docs/plugins/pre-submission-checklist)
(PUB30-03) adds a root README of at least 40 non-code words and a license.
More than 512 files triggers reviewer handling. The current archive has no
root README and contains 794 files. **GAP30-01** holds this route: prepare
truthful listing content and resolve review expectations or approve a targeted
packaging change; do not redesign containment merely to reduce file count.
This is a local comparison with documented rules, not a portal rejection.

## Codex: custom catalog versus public directory

For repository/CLI distribution, prepare the final Codex root and an approved
`.agents/plugins/marketplace.json` catalog. Local source paths begin with
`./` and resolve from the marketplace root. Entries carry real names and the
documented installation/authentication policy and category; those catalog policies
are not Kiyo tool permissions. Git-backed sources need the real repository and ref.

~~~text
codex plugin marketplace add <approved-marketplace-source>
codex plugin marketplace list
codex plugin marketplace upgrade <marketplace-name>
~~~

Catalog refresh is not proof of installed content refresh or Core activation.
Use the [actual CLI protocol](../compatibility/codex-local-test-protocol.md) for the
version-specific add/remove steps and cache evidence. Do not invent a plugin
update command. Workspace publishing and the public directory are separate.
[OpenAI packaging](https://developers.openai.com/plugins/build/plugins),
PUB30-04, documents catalog mechanics; desktop examples do not establish IDE support.

**Public route**: confirm verified developer/business identity and submission
write authority (currently named Apps Management) for the owning organization.
An authorized owner handles missing account roles; this runbook grants none.
At [OpenAI's portal](https://platform.openai.com/plugins), select Create plugin →
Skills only. Complete Info, upload the final bundle under Skills, and complete
applicable Prompts, Testing, Global availability and policy fields. Review all
skill scan results and any normalized metadata before Submit for Review.
Following approval, publication is a distinct portal action; preserve its actual
result and listing URL before reporting PUBLISHED.
Source: [submission](https://developers.openai.com/plugins/deploy/submission),
PUB30-05; portal shell was read-only, no authenticated form or submission observed.

The [track-specific error reference](https://developers.openai.com/plugins/deploy/submission-errors)
(PUB30-06) requires one plugin root, a supported manifest and valid Skills.
Skills-only ZIPs exclude MCP/app/screenshot configuration; all bundled Skills need
passing scans and the publisher needs identity/attestations. Listing URLs are
optional for this track when omitted; any supplied URLs must be real and compliant.
The broad materials table's remote-MCP endpoints, domain proof, demo credentials
and five-positive/three-negative rule must not be imposed on Kiyo by analogy.
Current version/author/developerName failures remain unresolved.

**GAP30-02**: OpenAI's
[conversion guidance](https://developers.openai.com/plugins/guides/submit-claude-plugin)
(PUB30-07) requests partner contact for core value depending on local execution
or arbitrary local file access. Kiyo's repository workflow warrants owner route
clarification (an inference, not a rejection or a requirement to add MCP).
Obtain the applicable review route before submission. No partner/account is assumed.
Codex IDE native plugins remain documented UNSUPPORTED; no fallback is adopted.
[Supported surfaces](https://learn.chatgpt.com/docs/plugins), PUB30-11;
no new IDE test.

## Copilot: prepared source or custom marketplace

Prepare the approved Copilot root with `plugin.json` and eight Skills.
For a custom catalog, put `marketplace.json` in `.github/plugin/` with the
real marketplace owner and plugin source relative to the repository root.
Share only the prepared source under separate approval. A local/custom catalog
does not establish admission to Microsoft's or GitHub's curated sources.
[GitHub marketplace authoring](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace),
PUB30-09; no destination or curated application selected.

Documented CLI forms:

~~~text
copilot plugin marketplace add <approved-marketplace-source>
copilot plugin install <plugin-name>@<marketplace-name>
copilot plugin list
copilot plugin update <installed-name>
copilot plugin uninstall <installed-name>
~~~

A prepared local directory or Git source can also be the install specification.
Use the [isolated protocol](../compatibility/copilot-local-test-protocol.md), never an
invented project-only flag or a real default global profile. Local-directory
marketplace sources can load live after restart; that is not universal update
behavior. Do not force-remove dependent plugins or bypass managed settings.
[CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference),
PUB30-08; no Kiyo CLI execution evidence.

For **VS Code**, after separately scoped profile authorization: use Extensions
`@agentPlugins` or Chat: Open Customizations → Plugins. Install the approved
catalog entry after reviewing its trust prompt, or use Chat: Install Plugin From
Source with the prepared repository URL. For local evaluation use an authorized
`chat.pluginLocations` entry. Update via Extensions: Check for Extension Updates;
uninstall the exact entry in Agent Plugins - Installed. Do not generate a VSIX.
[Microsoft guide](https://code.visualstudio.com/docs/agent-customization/agent-plugins),
PUB30-10, DOCUMENTED_ONLY. Kiyo IDE testing remains NOT_TESTED even if CLI
installation is later successful.

Curated source **OWNER INPUT REQUIRED**: choose the exact maintained repository,
then inspect its current contribution and review policy and prepare its requested
submission under new scope. There is no verified universal curated submit command.

## Activation, update, withdrawal and proof of publication

Use the [six-target invocation map](../compatibility/native-invocation-map.md)
and [activation matrix](../compatibility/activation-matrix.md). Installation/
discovery is not Core loading. Never advertise always-on behavior from KIYO.md.
An authorized Init can add only the scoped managed block; preserve human
instructions, nested boundaries and the established repository Memory location.

On update, inspect source/permission/metadata deltas, verify the installed digest,
and test new-session policy/Core behavior plus project-state preservation.
On uninstall, use the native client and preserve user policy/Memory; project
cleanup removes only the authorized managed block, never the whole instruction
file. These are Kiyo lifecycle requirements; only the bounded Codex synthetic
uninstall currently has actual evidence. See [lifecycle guides](../user/README.md).

For withdrawal/revocation, follow [security lifecycle](security-lifecycle.md)
and the chosen channel's documented controls; record the affected version,
reason, communication authority and rollback limits. Do not delete users' data.

Before changing PUBLISHED from false, retain: approved action scope, exact source
revision and archive digest, real publisher/destination, native submission/review
result, live listing/install evidence, timestamp and supported target limits.
A source upload, scan PASS, checksum or approval notification alone does not
prove final platform publication. Stop when any required input or evidence is absent.

