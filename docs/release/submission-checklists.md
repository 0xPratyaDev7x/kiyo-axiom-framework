# Native submission readiness checklists

Checked **2026-09-29**. These are inactive review checklists, not submissions.
[Source register](../research/SOURCES.md#prompt-28-release-source-check) records
requested/returned URLs, status and limitations. All portal/curated behavior
below is DOCUMENTED_ONLY. No destination, publisher or account is selected.

## Common gates

- [ ] Owner confirms final name, actual release version/history, license,
  publisher/namespace, prepared source/ref and distribution destination.
- [ ] Required author/interface/catalog metadata uses real approved values;
  repository folder names and copyright do not prove publishing authority.
- [ ] Candidate digest/inventory, eight Skills, references, exclusions,
  permissions/activation claims and security-sensitive delta are reviewed.
- [ ] Required static, behavioral and independent CLI/IDE evidence is available;
  support wording lists remaining gaps honestly.
- [ ] Disclosure channel/owner, update/rollback/revocation process and any
  required signing mechanism have actual authorization and evidence.
- [ ] Exact candidate and destination have scoped human publication approval.

Unchecked gates remain unresolved. Version equality is not approval to assign it.
No release number/email/publisher/URL is filled to make a validator pass.
Signing is not universally claimed as a vendor requirement; its necessity is a
destination/organization decision. Current outputs are NOT_SIGNED/NOT_ATTESTED.

## Claude Code

- [ ] Choose explicitly between private/custom marketplace distribution and
  Anthropic directory review; obtain real source/catalog/owner values.
- [ ] Recheck current manifest/metadata requirements and the native validator.
  Retain P26 strict FAIL for missing version/author; do not hide it behind
  normal validation's exit 0 or change validation policy silently.
- [ ] Exercise marketplace installation, cache resources and lifecycle plus the
  intended Skills independently in CLI and the Claude VS Code panel.
- [ ] Revalidate chosen channel's submission process, account authority and
  applicable metadata; no portal/account operation happens in this rehearsal.

The current [Claude publishing guide](https://code.claude.com/docs/en/plugins/publish)
distinguishes custom catalogs, directory submission and the official marketplace;
directory approval is not an official-marketplace listing. Local validation is
not portal acceptance. No additional Claude surface enters Kiyo's launch scope.
Checked 2026-09-29; local lifecycle/behavior gaps remain in the
[live matrix](../compatibility/live-test-matrix.md).

## Codex

- [ ] Use the **Skills only** route for Kiyo; upload the tested self-contained
  candidate when separately authorized. Do not add MCP/app/server/domain-proof
  or demo credentials to imitate an unrelated submission track.
- [ ] Resolve missing version/author/interface.developerName from real owner
  evidence and review native/static contracts before regenerating. Retain the
  actual public ingestion FAIL despite P26 local install success.
- [ ] Establish verified publisher identity, actual submission-role authority,
  required scans and truthful policy attestations at the selected destination.
- [ ] Review exact listing requirements and optional versus required URLs for
  skills-only uploads; do not invent URLs/assets. Recheck evolving portal rules.
- [ ] Complete CLI Skill/activation/update evidence. Codex IDE native plugins
  remain UNSUPPORTED; no standalone fallback has been approved.
- [ ] Treat submission, review approval and publication as separate authorized
  actions; none is performed here.

[OpenAI submission](https://developers.openai.com/plugins/deploy/submission)
documents skills-only uploads and separate review/publication.
The [error reference](https://developers.openai.com/plugins/deploy/submission-errors)
distinguishes optional URLs for skills-only ZIPs and requirements for remote MCP.
Its precise track-specific rules refine the submission page's broad materials
table; do not require MCP test credentials for static Kiyo. Both checked
2026-09-29; portal scans/attestations/acceptance NOT_RUN.
[Earlier detailed owner gates](../compatibility/codex-submission.md) remain
historical; P26 local metadata does not satisfy them.

## GitHub Copilot CLI and VS Code

- [ ] Review each client's documented manifest/component support independently;
  keep one shared format only for supported fields and discovery.
- [ ] Provide a real prepared source or custom catalog with authorized identity.
  No GitHub App, VSIX service, cloud agent or consumer Actions runtime is needed.
- [ ] Verify CLI installation/selector/update/uninstall and VS Code
  source/Agent Plugins UI separately; CLI qualification remains UNKNOWN.
- [ ] Preserve user Memory/policy/human bootstrap on both targets. Do not alter
  broad settings to make a trial pass.
- [ ] If a curated repository/listing is desired, first select it and inspect its
  current contribution/review rules. No universal submission route or acceptance
  into all default sources is asserted.

[GitHub CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)
documents source/catalog mechanisms. [Microsoft agent plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins)
documents source install and configurable marketplaces, distinct from VSIX.
Checked 2026-09-29; Kiyo native tests for both targets remain NOT_TESTED.
Default source visibility or successful custom installation is not curated
publisher approval.

Use [draft marketplace copy](marketplace-copy.md) only as review material.
No checkbox is pre-approved by this document, a pipeline PASS or an AI agent.
