# Kiyo Compass — Research sources

Checked: **2026-09-28**, Asia/Bangkok. Prompt 02 only.

## Evidence rules

- **VERIFIED**: a named, actually executed observation/check with reproducible evidence and a narrow scope. In this prompt it applies to repository/document checks, never to Kiyo host behavior.
- **DOCUMENTED_ONLY**: the retrieved authoritative source describes the capability or publication. It has not been demonstrated with a Kiyo package.
- **NOT_TESTED**: no live Kiyo test was run on that specific target. This can coexist with DOCUMENTED_ONLY or UNSUPPORTED.
- **UNSUPPORTED**: the source explicitly excludes the capability, or its documented closed format excludes the proposed field. Absence of a mention alone is not enough.
- **UNKNOWN**: inspected sources do not establish the fact, conflict, or leave relevant semantics unspecified.
- **NOT_REVALIDATED**: freshness/access qualifier when the relevant page cannot be retrieved. It is not a synonym for UNSUPPORTED.

Every source row below has source-check status **DOCUMENTED_ONLY** and checked date
**2026-09-28**. Source IDs are stable locators, not test IDs. Capability tables inherit
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
| S01 | [ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html) | Same | 2026-09-28 | Public catalog/abstract; full copyrighted text not reviewed. |
| S02 | [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) | Same | 2026-09-28 | Published edition with DIS replacement in development; not the draft as baseline. |
| S03 | [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | Same | 2026-09-28 | Public product-quality abstract; no clause-level mapping. |
| S04 | [ISO/IEC/IEEE 29119-1:2022](https://www.iso.org/standard/81291.html) | Same | 2026-09-28 | Part 1 only; do not call all of 29119 a single edition. |
| S05 | [ISO/IEC/IEEE 29119-2:2021](https://www.iso.org/standard/79428.html) | Same | 2026-09-28 | Test-process catalog/abstract only. |
| S06 | [ISO/IEC/IEEE 29119-3:2021](https://www.iso.org/standard/79429.html) | Same | 2026-09-28 | Test-documentation catalog/abstract only; no copied templates. |
| S07 | [ISO/IEC/IEEE 29119-4:2021](https://www.iso.org/standard/79430.html) | Same | 2026-09-28 | Test-technique catalog/abstract only. |
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
| W01 | [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | [Final page](https://owasp.org/projects/asvs) | 2026-09-28 | Main text names stable 5.0.0; sidebar also says Bleeding Edge, so avoid equating moving repository head with stable. |
| W02 | [OWASP Agentic Skills Top 10](https://owasp.github.io/www-project-agentic-skills-top-10/) | Same | 2026-09-28 | Public review v1 draft; status section says new proposal/1.0 (2026 Edition). Proposed universal schema is not a host contract. |
| W03 | [OWASP SAMM model](https://owaspsamm.org/model/) | Same | 2026-09-28 | Model describes version 2.0; latest patch/tool version not established. |
| W04 | [OWASP SAMM v2 release notes](https://owaspsamm.org/release-notes-v2/) | Same | 2026-09-28 | Reached via model page link; incremental guidance updates are not automatically a new model edition. |

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

