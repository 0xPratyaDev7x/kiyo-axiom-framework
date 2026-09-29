# Prompt 24 — Coverage interpretation

Checked: 2026-09-29. Source: [test definitions](../../../tests/static/README.md),
[actual final execution](test-results-final.json) and
[canonical contracts](../../../src/kiyo/framework/evidence-contract.md).
This is selected-property **static** validation, not FULL SCHEMA VALIDATION.

## Coverage and requirement relation

| Groups | Partial requirement coverage | What remains outside that assertion |
| --- | --- | --- |
| G01–03 | REQ-026/027 | Native discovery, procedure execution and user outcomes |
| G04/12/13 | REQ-002/003/006 | Six independent installation/cache/update lifecycles; actual host sandbox |
| G05/06 | REQ-061/064/067/079 | Owner-approved release identity, ingestion and semantic portability |
| G07 | REQ-011/027/049/069/071–075 | Host enforcement, real authority and behavioral adherence |
| G08 | REQ-023/040/044/045/047/048/050 | Correct risk judgments and truthful agent responses in novel situations |
| G09 | REQ-058–067 | Security effectiveness, complete inventories or AST compliance |
| G10 | REQ-019/020/022 | Real Memory sync/concurrency/approval behavior |
| G11 | REQ-046 | Complete secret/PII detection or universal prose-fact classification |
| G14 | REQ-009 | Actual automatic activation or host context consumption |
| G15 | REQ-027 | No TODO-only sections; not proof of semantic completeness |
| G16 | REQ-043/080 | Full requirement acceptance |
| Suite/report | REQ-077/078 | Behavioral/live suites and final product acceptance |

Exactly 40 trace rows receive a P24 partial static-evidence reference.
All 80 original IDs remain present and unique; **79 PARTIALLY_IMPLEMENTED /
1 NOT_IMPLEMENTED**, all full requirement verifications **NOT_RUN**. These
counts deliberately do not promote selected assertions to full acceptance.

## Selected schema properties, not a schema engine

The manifest checks delegate to the existing independent native builders,
following the [P20 Claude](../claude/package-checks.md),
[P21 Codex](../codex/package-checks.md) and
[P22 Copilot](../copilot/package-checks.md) records. Their source/revalidation dates
remain 2026-09-29; P24 does not claim another online revalidation.

- Claude: exact name/description keys, kiyo-compass working identity, nonempty
  description, existing selected payload/frontmatter checks.
- Copilot: exact $schema/name/description keys, recorded Agent Plugins 1.0.0
  schema URL, native name pattern/length, nonempty description.
- Codex: exact portable fields and OpenAI interface nesting; nonempty presentation
  strings, displayName/shortDescription <=30, Productivity category, empty
  capabilities, 1–3 single-line prompts <=128 characters; generated compatibility
  manifest equals the selected portable fields and skills path.
- Entries: exactly name/description, simple unquoted scalar syntax, no duplicate
  fields, lowercase-hyphen names <=64, directory/name equality, description
  1–1,024 characters and rejected unsupported scalar syntax. This intentionally
  narrow authoring subset does not parse every valid YAML/native option.

No formal JSON Schema/YAML validator, current host parser or remote schema fetch
runs here. Unknown/unsupported extra fields fail the closed development subset;
that does not mean all fields outside the subset are invalid in every host.
Missing Codex version/author/developerName still causes the separately recorded
ingestion **FAIL**. Static subset PASS does not erase that result.
The eight names are a canonical inventory, not proof of a universal slash command.

## Interpretation and residual gaps

Normative-clause checks and effect tables catch concrete regressions, including
a removed approval wait and an added write grant. They cannot parse all English
contradictions or make an AI comply. G08 distinguishes a deliberately bad example
from its good counterpart; only mutating the good evidence record to fake PASS
causes the expected EVIDENCE_CONTRADICTION.

Template scanning checks explicit neutral fields and bounded suspicious patterns,
plus synthetic sentinels. It is not DLP, universal secret detection or a claim
that every possible private fact can be recognized. No real secret is used.
AST ownership is drawn from Kiyo Markdown guidance, host-native security,
developer release process and human organization process; no runtime security
control was added or certified.

G13 tests actual Windows extraction and exact-case string resolution. The
source-denying Python audit hook is test-only, cooperative isolation, never a
consumer sandbox. No native POSIX OS test was run. P23's additional real
filesystem symlink probe remains **BLOCKED** (Windows 1314); regular ZIP
membership/symlink rejection already has separate evidence and is not waived.

Content parity is not behavioral parity. No fresh behavioral evaluation,
native installation, activation, cache update/uninstall or publication was
performed. Unrun behavioral/live-host evidence remains **NOT_TESTED**; source
scenario execution stays NOT_RUN. Codex IDE native plugins remain
**UNSUPPORTED**, independently of CLI content. All six target records remain
separate in the [activation matrix](../../compatibility/activation-matrix.md).

Owner DEC-001–004 (name, release license, publisher/destination, IDE gap) remain
open. LICENSE and existing version/history are preserved. No project Memory,
bootstrap, credentials, global permissions, consumer runtime, MCP or hooks were
created. Stop at Prompt 24; Prompt 25 requires its own user request.

