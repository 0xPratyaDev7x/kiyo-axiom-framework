# Kiyo Compass — Research sources

Original baseline: **2026-09-28**, Asia/Bangkok (Prompt 02).
Prompt 07 rechecked W01/W02 and added W05–W15 on **2026-09-29**.
Prompt 09 rechecked S01–S07 and added E01–E06 on **2026-09-29**.

Prompt 20 adds CL20-01–CL20-13 on **2026-09-29** for Claude packaging.
Prompt 21 adds CX21-01–CX21-12 on **2026-09-29** for Codex packaging.

## Evidence rules

- **VERIFIED**: a named, actually executed observation/check with reproducible evidence and a narrow scope. In this prompt it applies to repository/document checks, never to Kiyo host behavior.
- **DOCUMENTED_ONLY**: the retrieved authoritative source describes the capability or publication. It has not been demonstrated with a Kiyo package.
- **NOT_TESTED**: no live Kiyo test was run on that specific target. This can coexist with DOCUMENTED_ONLY or UNSUPPORTED.
- **UNSUPPORTED**: the source explicitly excludes the capability, or its documented closed format excludes the proposed field. Absence of a mention alone is not enough.
- **UNKNOWN**: inspected sources do not establish the fact, conflict, or leave relevant semantics unspecified.
- **NOT_REVALIDATED**: freshness/access qualifier when the relevant page cannot be retrieved. It is not a synonym for UNSUPPORTED.

Every source row below has source-check status **DOCUMENTED_ONLY**; use each row's
checked date. Unchanged Prompt 02 sources remain checked **2026-09-28**. Source IDs are stable locators, not test IDs. Capability tables inherit
that date and link here; their limitation cells apply in addition to the source limits.
All six live targets remain NOT_TESTED. No plugin, skill, account, cache relocation,
automatic selection or permission behavior was exercised.

## Retrieval and redirect method

Used web search for discovery and opened official pages for evidence. Followed the
web tool's reported redirects; the destination column is the observed final URL.
“Same” means no redirect was reported by the tool, not an independently captured
HTTP redirect chain. No HTTP status codes, intermediate hops, archive timestamps
or response hashes are invented. Search crawl dates are not host versions.
Pages may change between requests; revalidate before packaging and release.
Only public documentation URLs were sent to the web tool.

## Source register

| ID | Official source / requested URL | Observed destination | Checked | Limitation |
| --- | --- | --- | --- | --- |
| C01 | [Claude plugins overview](https://code.claude.com/docs/en/plugins) | Same | 2026-09-28 | Plugin component overview; not a live installation. |
| C02 | [Claude skills](https://code.claude.com/docs/en/skills) | Same | 2026-09-28 | Frontmatter, invocation, disclosure and substitutions; host version gates vary. |
| C03 | [Claude project memory](https://code.claude.com/docs/en/memory) | Same | 2026-09-28 | Project instructions/rules, not plugin-root core auto-loading. |
| C04 | [Claude manifest reference](https://code.claude.com/docs/en/plugins-reference) | Same | 2026-09-28 | Field/path reference; no manifest validator executed. |
| C05 | [Claude VS Code](https://code.claude.com/docs/en/vs-code) | Same | 2026-09-28 | Independent IDE documentation; no extension session tested. |
| C06 | [Claude installation and management](https://code.claude.com/docs/en/discover-plugins) | Same | 2026-09-28 | Scope, marketplace and maintenance documentation only. |
| C07 | [Claude plugin components](https://code.claude.com/docs/en/plugins/components) | Same | 2026-09-28 | Reached from C04's components link; explicit plugin-root CLAUDE.md limitation. |
| C08 | [Claude system requirements](https://code.claude.com/docs/en/setup) | Same | 2026-09-28 | Host prerequisites, not a Kiyo minimum supported version. |
| O01 | [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins) | Same | 2026-09-28 | Portable and compatibility formats; some local testing guidance specifically targets desktop. |
| O02 | [OpenAI plugin skills concepts](https://developers.openai.com/plugins/concepts/skills) | Same | 2026-09-28 | Metadata/on-demand loading, not always-on core. |
| O03 | [Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) | [Final page](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 2026-09-28 | Redirect observed; project guidance is separate from plugin installation. |
| O04 | [Codex plugin surfaces](https://learn.chatgpt.com/codex/plugins) | [Final page](https://learn.chatgpt.com/docs/plugins) | 2026-09-28 | Explicit CLI support and IDE plugin exclusion; no Kiyo trial. |
| O05 | [Codex skills](https://developers.openai.com/codex/skills) | [Final page](https://learn.chatgpt.com/docs/build-skills) | 2026-09-28 | Standalone IDE skills do not imply IDE plugin support. |
| O06 | [Codex IDE](https://developers.openai.com/codex/ide) | [Final page](https://learn.chatgpt.com/docs/codex/ide) | 2026-09-28 | Extension overview; exact minimum plugin version cannot be inferred. |
| O07 | [Codex CLI](https://developers.openai.com/codex/cli) | [Final page](https://learn.chatgpt.com/docs/codex/cli) | 2026-09-28 | Installation/sign-in overview; no observed local executable version. |
| G01 | [Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) | Same | 2026-09-28 | Portable/legacy fields and commands; page changed from 435 to 486 rendered lines during research, so use named sections, not line numbers. |
| G02 | [Copilot CLI plugin creation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating) | Same | 2026-09-28 | Skills-only packaging documented; no package built. |
| G03 | [Copilot CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-skills) | [Final page](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | 2026-09-28 | Slash skill selection documented; plugin skill namespace spelling not established by the example. |
| G04 | [Copilot CLI instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) | Same | 2026-09-28 | Repository/user discovery and relative includes; no general instruction-file precedence. |
| G05 | [Copilot CLI quickstart](https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-getting-started) | [Final page](https://docs.github.com/en/copilot/get-started/cli-quickstart) | 2026-09-28 | All Copilot plans and organization-policy condition; exact OS floors not established. |
| V01 | [VS Code agent plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins) | Same | 2026-09-28 | Copilot/Local harness details must not be applied to a separate vendor IDE extension. |
| V02 | [VS Code agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) | Same | 2026-09-28 | Plugin-prefixed invocation and relative resources; fork context experimental. |
| V03 | [VS Code custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) | [Final page](https://code.visualstudio.com/docs/agent-customization/custom-instructions) | 2026-09-28 | Harness-dependent behavior; inline suggestions excluded. |
| V04 | [VS Code Copilot setup](https://code.visualstudio.com/docs/copilot/setup) | [Final page](https://code.visualstudio.com/docs/setup/copilot) | 2026-09-28 | Account/plan access; not proof of this machine's entitlement. |
| A01 | [Agent Plugins JSON Schema 1.0.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json) | Same | 2026-09-28 | Schema fetched; semantic requirements also exist; host support still needs independent evidence. |
| A02 | [Agent Skills specification](https://agentskills.io/specification) | Same | 2026-09-28 | Portable conventions; host extensions and enforcement differ. |
| S01 | [ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html) | Same | 2026-09-29 | Public catalog/abstract; full copyrighted text not reviewed. |
| S02 | [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) | Same | 2026-09-29 | Published edition with DIS replacement in development; not the draft as baseline. |
| S03 | [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | Same | 2026-09-29 | Public product-quality abstract; no clause-level mapping. |
| S04 | [ISO/IEC/IEEE 29119-1:2022](https://www.iso.org/standard/81291.html) | Same | 2026-09-29 | Part 1 only; do not call all of 29119 a single edition. |
| S05 | [ISO/IEC/IEEE 29119-2:2021](https://www.iso.org/standard/79428.html) | Same | 2026-09-29 | Test-process catalog/abstract only. |
| S06 | [ISO/IEC/IEEE 29119-3:2021](https://www.iso.org/standard/79429.html) | Same | 2026-09-29 | Test-documentation catalog/abstract only; no copied templates. |
| S07 | [ISO/IEC/IEEE 29119-4:2021](https://www.iso.org/standard/79430.html) | Same | 2026-09-29 | Test-technique catalog/abstract only. |
| S08 | [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) | Same | 2026-09-28 | Management-system reference, not product certification. |
| S09 | [ISO/IEC 27001:2022/Amd 1:2024](https://www.iso.org/standard/88435.html) | Same | 2026-09-28 | Amendment identified separately; no clause reproduction. |
| S10 | [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) | Same | 2026-09-28 | Management-system reference; no organizational conformity assessment. |
| S11 | [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html) | Same | 2026-09-28 | AI risk guidance; not evidence that Kiyo enforces risk controls. |
| S12 | [ISO/IEC 38507:2022](https://www.iso.org/standard/56641.html) | Same | 2026-09-28 | Supporting governance reference only. |
| S13 | [ISO/IEC 27034-1:2011](https://www.iso.org/standard/44378.html) | Same | 2026-09-28 | Supporting part 1 only; other parts not baseline-validated. |
| S14 | [ISO/IEC 5338:2023](https://www.iso.org/standard/81118.html) | Same | 2026-09-28 | Conditional on actual AI-system development, not ordinary agent-assisted coding. |
| N01 | [NIST SSDF 1.1 final](https://csrc.nist.gov/pubs/sp/800/218/final) | Same | 2026-09-28 | Final publication, distinct from revision draft. |
| N02 | [NIST SSDF 1.2 initial public draft](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd) | Same | 2026-09-28 | Draft dated 2025-12-17; comment closure does not make it final. |
| N03 | [NIST SSDF project](https://csrc.nist.gov/projects/ssdf) | Same | 2026-09-28 | Practice groups and supplementary AI profile; project page alone is not revision status. |
| N04 | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | Same | 2026-09-28 | 1.0 released; revision in progress; no assumed successor edition. |
| W01 | [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | [Final page](https://owasp.org/projects/asvs) | 2026-09-29 | Main text names stable 5.0.0; sidebar also says Bleeding Edge, so avoid equating moving repository head with stable. |
| W02 | [OWASP Agentic Skills Top 10](https://owasp.github.io/www-project-agentic-skills-top-10/) | Same | 2026-09-29 | Public review v1 draft; status section says new proposal/1.0 (2026 Edition). Proposed universal schema is not a host contract. |
| W03 | [OWASP SAMM model](https://owaspsamm.org/model/) | Same | 2026-09-28 | Model describes version 2.0; latest patch/tool version not established. |
| W04 | [OWASP SAMM v2 release notes](https://owaspsamm.org/release-notes-v2/) | Same | 2026-09-28 | Reached via model page link; incremental guidance updates are not automatically a new model edition. |
| W05 | [OWASP Agentic Applications release announcement](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) | Same | 2026-09-29 | Announcement dated 2025-12-09 uses ASI identifiers; separate from AST. Not evidence of latest minor revision or Kiyo behavior. |
| W06 | [AST01: Malicious Skills](https://owasp.github.io/www-project-agentic-skills-top-10/ast01.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |
| W07 | [AST02: Supply Chain Compromise](https://owasp.github.io/www-project-agentic-skills-top-10/ast02.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |
| W08 | [AST03: Over-Privileged Skills](https://owasp.github.io/www-project-agentic-skills-top-10/ast03.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |
| W09 | [AST04: Insecure Metadata](https://owasp.github.io/www-project-agentic-skills-top-10/ast04.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |
| W10 | [AST05: Untrusted External Instructions](https://owasp.github.io/www-project-agentic-skills-top-10/ast05.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |
| W11 | [AST06: Weak Isolation](https://owasp.github.io/www-project-agentic-skills-top-10/ast06.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |
| W12 | [AST07: Update Drift](https://owasp.github.io/www-project-agentic-skills-top-10/ast07.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |
| W13 | [AST08: Poor Scanning](https://owasp.github.io/www-project-agentic-skills-top-10/ast08.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |
| W14 | [AST09: No Governance](https://owasp.github.io/www-project-agentic-skills-top-10/ast09.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |
| W15 | [AST10: Cross-Platform Reuse](https://owasp.github.io/www-project-agentic-skills-top-10/ast10.html) | Same; reached from W02 summary link | 2026-09-29 | Draft taxonomy detail; original Kiyo interpretation only, no native schema/enforcement or incident validation claim. |

## Prompt 07 OWASP revalidation

Opened W02's recorded URL and followed its ten category links to W06–W15;
no redirect was reported for the landing/detail pages. W01 again redirected from
the original project URL to https://owasp.org/projects/asvs. W05 was discovered
through official-source search and opened at its shown URL without a reported
redirect. Browser text retrieval establishes source content, not Kiyo behavior.
No hostile example, scanner integration or external attack was executed.

W02 still presents public-review v1 together with proposal/2026-edition wording.
Retain draft maturity and do not infer a finalized release. W05 establishes a
separate ASI taxonomy and announcement, not interchangeability with AST. W01 main
text identifies stable 5.0.0 while the sidebar retains bleeding-edge wording.
Other standards, vendor schemas, host settings and the linked v1 Google Doc were
not revalidated in Prompt 07. No clause text or OWASP schema is imported.

The [Kiyo AST controls](../../src/kiyo/agent-security/owasp-ast10.md) and
[scenario specifications](../../tests/behavioral/agent-security/scenarios.md)
are authored interpretations/expected behavior. Execution remains NOT_RUN;
native targets remain NOT_TESTED. See [P07 checks](../build/BASELINE.md#prompt-07-checks).

## Prompt 09 engineering and profile sources

S01–S07 were retrieved again on **2026-09-29**. Their requested ISO URLs remained
the final displayed URLs; published editions remain 12207:2026, 29148:2018,
25010:2023, 29119-1:2022 and 29119-2/3/4:2021 (each edition 2). The 29148 DIS
remains in development. Public catalogue metadata/abstracts only were inspected;
no full-text or clause-level review is claimed. Other source dates are unchanged.

| ID | Requested official URL | Final URL / redirect | Checked | Limit / use |
| --- | --- | --- | --- | --- |
| E01 | [Microsoft .NET SDK selection](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json) | Same; no redirect reported | 2026-09-29 | SDK selection is distinct from target framework/runtime; no local SDK/version established. |
| E02 | [Microsoft .NET testing overview](https://learn.microsoft.com/en-us/dotnet/core/testing/) | Same; no redirect reported | 2026-09-29 | Test platform and framework are separate; no project runner/framework choice or safe command established. |
| E03 | [Angular workspace configuration](https://angular.dev/reference/configs/workspace-config) | Same; no redirect reported | 2026-09-29 | Angular CLI workspace/project/build-target scope; not evidence that all repositories use this layout or current APIs. |
| E04 | [PyPA pyproject.toml guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) | Same; no redirect reported | 2026-09-29 | Metadata, build configuration and Python constraints; examples do not select a backend, package manager or framework. |
| E05 | [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html) | Same; no redirect reported | 2026-09-29 | Current alias rendered documentation 18; not target-version evidence or a guarantee every migration is reversible. |
| E06 | [PostgreSQL libpq execution](https://www.postgresql.org/docs/current/libpq-exec.html) | Same; no redirect reported | 2026-09-29 | Current alias rendered documentation 18; separate value parameters documented for libpq, not every driver's API. |

All six profile sources are DOCUMENTED_ONLY. Read the relevant source body, not
just search snippets. Microsoft's SDK page displayed an authorization banner
alongside readable public article text; the public body supplied the observation,
without sign-in or privileged access. PostgreSQL's current aliases are moving
URLs even when no redirect occurs; recheck against an actually observed target
version before using version-specific APIs.

These sources support discovery guidance in the
[packaged engineering/profile selection](../../src/kiyo/framework/engineering/index.md).
They do not prove stack support, command safety or native-host behavior. The
[concept mapping](../../src/kiyo/framework/engineering/standards-mapping.md)
retains N01's 2026-09-28 and W01's Prompt 07 2026-09-29 dates; neither was
revalidated by Prompt 09. No dependencies were installed or database contacted.

## Retrieval failures and recovery

| Requested URL | Actual result on 2026-09-28 | Recovery / effect |
| --- | --- | --- |
| `https://code.claude.com/docs/en/plugin-components` | Tool reported inaccessible; NOT_REVALIDATED at this URL | Followed C04's component link to C07; no guessed schema used. |
| `https://csrc.nist.gov/pubs/sp/800/218/r1/iprd` | Tool reported inaccessible; NOT_REVALIDATED at this URL | Official search found N02 with `ipd`; opened it and confirmed draft status. |
| `https://owaspsamm.org/release-notes/` | Tool reported inaccessible; NOT_REVALIDATED at this URL | Followed W03's release-notes link to W04. |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-getting-started/installing-copilot-cli` | Tool reported inaccessible; NOT_REVALIDATED at this URL | G05 establishes plan and platform installation routes; exact OS/version floors remain UNKNOWN. |

Research access succeeded overall. The failed URLs above are retained as a retrieval
record, not cited as substantive evidence. An unresolved schema-dependent detail
stays deferred even though other pages are reachable.

## Authority and conflicts

Native vendor references determine native packaging. A01/A02 explain portable
formats only where the target itself documents support. W02 is a security taxonomy
and proposal: its illustrative `skill.json`, `manifest.json`, permissions and signing
examples cannot override C04/O01/G01/V01. The local plugin-creator skill or this
chat's installed skill list is not an API contract.

O04 explicitly excludes plugins in the Codex IDE extension. O05 independently
documents standalone IDE skills. These statements are compatible; neither
authorizes advertising a six-target native plugin release.

O01's local marketplace examples emphasize desktop testing, while O04 documents
the CLI marketplace browser. Keep custom CLI install/update behavior pending a
target-specific trial instead of silently promoting the desktop instructions.

## Publication information still requiring the owner

Link to [DEC-001–003](../build/DECISIONS.md): final name/identifiers and availability,
release license, publisher/account/namespace and authorized destination.
Before publication also confirm repository/homepage/support contact, release
version, public versus private distribution, intended supported host versions/OS,
truthful capabilities, asset rights and any required privacy/terms URLs. No
identity, account entitlement, signature, review acceptance or marketplace
reservation is established by this research. No submission was made.


## Prompt 20 Claude revalidation

All rows in this section are **DOCUMENTED_ONLY**, checked **2026-09-29**.
The observed destination is the requested URL: the web tool reported no redirect
for these successful opens. This is not an independently captured HTTP chain.
The legacy /docs/en/discover-plugins URL was also opened; it returned the
installation page without a reported redirect. Current overview links led to
/docs/en/plugins/create and /docs/en/plugins/install; those exact destinations
were followed and used below. No guessed HTTP status/intermediate hop is recorded.

| ID | Requested official URL / observed destination | Checked | Limitation |
| --- | --- | --- | --- |
| CL20-01 | [Plugin manifest](https://code.claude.com/docs/en/plugins-reference) — same reported URL | 2026-09-29 | name/description/default skills path; authoritative native validator deferred |
| CL20-02 | [Skills/frontmatter](https://code.claude.com/docs/en/skills) — same reported URL | 2026-09-29 | Namespaced selection/metadata and optional controls; no observed Kiyo invocation |
| CL20-03 | [Project instruction loading](https://code.claude.com/docs/en/memory) — same reported URL | 2026-09-29 | CLAUDE.md and version-dependent AGENTS selection; no target loading trace |
| CL20-04 | [Claude VS Code](https://code.claude.com/docs/en/vs-code) — same reported URL | 2026-09-29 | Panel management, prerequisites and scope; active extension not established |
| CL20-05 | [Create plugin](https://code.claude.com/docs/en/plugins/create) — same reported URL | 2026-09-29 | Skill-only layout and session --plugin-dir; no session run |
| CL20-06 | [Plugin components](https://code.claude.com/docs/en/plugins/components) — same reported URL | 2026-09-29 | Plugin-root CLAUDE.md excluded from project context; no runtime added |
| CL20-07 | [Create marketplace](https://code.claude.com/docs/en/plugin-marketplaces) — same reported URL | 2026-09-29 | Required catalog structure and relative source base; template is inactive |
| CL20-08 | [Marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference) — same reported URL | 2026-09-29 | Root/entry fields; owner/name unresolved, no catalog registration |
| CL20-09 | [Install and manage](https://code.claude.com/docs/en/plugins/install) — same reported URL | 2026-09-29 | Scope and maintenance forms; no installation/update/uninstall |
| CL20-10 | [Plugin loading](https://code.claude.com/docs/en/plugins/loading) — same reported URL | 2026-09-29 | Local-directory in-place versus copied cache; native relocation untested |
| CL20-11 | [Host setup](https://code.claude.com/docs/en/setup) — same reported URL | 2026-09-29 | OS/hardware prerequisites, not a tested Kiyo minimum |
| CL20-12 | [Claude directory](https://code.claude.com/docs/en/claude-directory) — same reported URL | 2026-09-29 | Configuration-root relocation documentation, not proven isolation |
| CL20-13 | [Environment variables](https://code.claude.com/docs/en/env-vars) — same reported URL | 2026-09-29 | CLAUDE_CONFIG_DIR for future isolated protocol; no process setting changed |

The original C01–C08 rows preserve Prompt 02's dated baseline. For Prompt 20
Claude decisions use [the current field map](../compatibility/claude-package.md)
and [test protocol](../compatibility/claude-installation-test-protocol.md).
No OpenAI/Copilot/standards source was refreshed by this Claude-only pass.

Observed locally, separately from public documentation: terminal --version
returned 2.1.220 (Claude Code); scoped on-disk VS Code extension manifests declare
2.1.283 and 2.1.284 with engine ^1.94.0. The active extension, running VS Code
version, account and provider/model remain UNKNOWN. See
[actual check evidence](../evidence/claude/package-checks.md).
Both native targets remain NOT_TESTED; no install/activation/cache/lifecycle claim
follows from the observations or offline generated-package checks.

## Prompt 21 Codex revalidation

All rows below are **DOCUMENTED_ONLY**, checked **2026-09-29**.
Requested legacy Codex URLs were opened or followed from official links;
reported redirects are recorded explicitly. "Same" means no redirect reported,
not an independent HTTP-chain capture. No guessed status code or hop is used.

| ID | Requested official source | Observed destination | Checked | Limitation |
| --- | --- | --- | --- | --- |
| CX21-01 | [OpenAI package/schema/interface/catalog](https://developers.openai.com/plugins/build/plugins) | Same | 2026-09-29 | Portable and compatibility precedence; selected fields documented, ingestion/live acceptance separate. |
| CX21-02 | [Plugin architecture](https://developers.openai.com/plugins/concepts/plugins) | Same | 2026-09-29 | Skills-only supported; optional MCP/runtime examples do not require those components. |
| CX21-03 | [Plugin skill authoring](https://developers.openai.com/plugins/build/skills) | Same | 2026-09-29 | Instruction-only workflow documented; ChatGPT and Codex invocation differ. |
| CX21-04 | [Codex skills/frontmatter/metadata](https://developers.openai.com/codex/skills/) | [Final page](https://learn.chatgpt.com/docs/build-skills) | 2026-09-29 | Name/description, progressive loading, /skills/$ and optional agents/openai.yaml; exact plugin-qualified Kiyo selector unknown. |
| CX21-05 | [Project instructions](https://developers.openai.com/codex/guides/agents-md/) | [Final page](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 2026-09-29 | Per-run AGENTS chain/scope/precedence; no automatic Kiyo Core guarantee. |
| CX21-06 | [Supported plugin surfaces](https://learn.chatgpt.com/docs/plugins) | Same | 2026-09-29 | CLI plugin browser; IDE plugins explicitly excluded; no account access or compatibility demonstrated. |
| CX21-07 | [Codex IDE setup](https://developers.openai.com/codex/ide) | [Final page](https://learn.chatgpt.com/docs/codex/ide) | 2026-09-29 | Editor/setup guidance does not grant plugin support or identify active local extension. |
| CX21-08 | [Codex CLI setup](https://developers.openai.com/codex/cli) | [Final page](https://learn.chatgpt.com/docs/codex/cli) | 2026-09-29 | OS setup/sign-in routes, not tested Kiyo minimum versions or entitlement. |
| CX21-09 | [Submission flow](https://developers.openai.com/plugins/deploy/submission) | Same | 2026-09-29 | Skills-only track, verified identity, role/review/publication; no portal used. |
| CX21-10 | [Submission error/field requirements](https://developers.openai.com/plugins/deploy/submission-errors) | Same | 2026-09-29 | Stricter version/publisher/scan/listing requirements; remote-MCP requirements kept separate. |
| CX21-11 | [Config precedence](https://developers.openai.com/codex/config-file/config-basic) | [Final page](https://learn.chatgpt.com/docs/config-file/config-basic) | 2026-09-29 | Trusted project config and native constraints; no config written or trust changed. |
| CX21-12 | [State/environment locations](https://developers.openai.com/codex/config-file/environment-variables) | [Final page](https://learn.chatgpt.com/docs/config-file/environment-variables) | 2026-09-29 | CODEX_HOME documents state root, not complete OS/credential/marketplace isolation. |

Direct .md variants for submission/error pages returned unsupported-content-type
errors in the web tool; their HTML pages were successfully retrieved above.
This does not make the established HTML evidence NOT_REVALIDATED. Original O01–O07
remain the dated Prompt 02 baseline; use CX21 rows for current Codex decisions.
Claude/Copilot/standards sources were not refreshed in this Codex-only step.

[Current field map](../compatibility/codex-package.md) distinguishes portable
packaging from stricter ingestion/publication. The local plugin-creator validator
actually fails absent version, author and interface.developerName; official
submission rules corroborate those gates. No missing identity was invented.
Local skill-creator/plugin scaffolding defaults are not a native schema authority.

Actual local observations: codex-cli 0.158.0 from --version; bounded plugin
--help output exposes add/remove and marketplace add/upgrade. Only version/help
was executed, not those actions. Named IDE extension metadata declares
26.917.62051, vscode ^1.96.2; active extension/editor/engine UNKNOWN.
See [offline evidence](../evidence/codex/package-checks.md).
All six Kiyo live targets remain NOT_TESTED; IDE plugin support remains
documented UNSUPPORTED, without a silently approved standalone fallback.

