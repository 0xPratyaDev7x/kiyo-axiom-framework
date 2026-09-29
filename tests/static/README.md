# Static/contract tests

Developer-only Python standard library suite for Prompt 24. It reads canonical
files, existing overlays, the P23 inventory and **actual ZIP bytes**; no install,
native client, network, dependency download or consumer runtime. Synthetic
mutations are isolated in memory. Extraction and evidence writes are the only
test outputs; temporary directories are retained for inspection.

Run from the repository root, using a fresh evidence filename:

```powershell
python -B tests/static/test_contracts.py --report docs/evidence/static/test-results-new.json
```

An existing report is refused. Exit 0 means all selected assertions and required
rejections passed; exit 1 retains failures. JSON records command, exit code,
stdout/stderr, UTC times, Python/OS, Git base observation, consulted/source/tool/
fixture hashes, per-check scope/results and actual isolated subprocesses.
A Git revision identifies the base, not production or uncommitted content.

## Assertion map

[contracts.py](contracts.py) contains properties; [test_contracts.py](test_contracts.py)
loads actual artifacts, drives 16 groups and verifies each fixture's exact
expected error code plus diagnostic fragment. The six required negative IDs
cannot silently disappear. No product file is patched by the tests.

| Group | Meaningful asserted property | Boundary |
| --- | --- | --- |
| G01 | Exactly eight expected directories, unique frontmatter names, no extra nested SKILL.md; source plus three artifacts | Inventory, not host discovery |
| G02 | Closed name/description scalar frontmatter, unique fields, lowercase hyphenated name equals directory, length/scalar restrictions | Selected common subset, not general YAML/native parsing |
| G03 | 37 mandatory resources exist; all eight entry graphs reach Core, own shared procedure and required templates | Resource reachability does not prove reading order/agent use |
| G04 | Inline local links resolve with exact case and real anchors; no absolute/scheme/escaping path; installed references stay inside that Skill's subtree | HTTPS not fetched; rejects unsupported reference-link/HTML syntax; illustrative fenced content not resolved |
| G05 | Closed native property sets/types, documented selected schema value, Codex interface/compatibility equivalence, artifact/source manifest equality | Selected development fields; NOT FULL SCHEMA VALIDATION |
| G06 | 68 unique registered controls, used IDs equal registry, definitions contain their ID, logical IDs/names, all shared copies exact, 24 allowed entry transforms | Version/publisher remain unset per current owner decisions; no signature or release readiness claim |
| G07 | Pinned normative read-only/approval clauses and effect-table columns; Test assess/run, Memory show/check, Init preview, Requirement output boundary | Regression on authored contracts; not a natural-language authorization engine |
| G08 | Exact check/task/impact/readiness/G/risk/data enums, eight risk dimensions, 18 governance outcome records, nine-field EVID-01 and 20 labeled good/bad cases | Specifically tests example roles; bad illustrative PASS text is not execution evidence |
| G09 | AST01–10 titles, nine fields each, owners from four categories with responsibility, control/test refs, substantive limits and dated draft/AST-versus-ASI status | Mapping structure, not OWASP certification or mitigation effectiveness |
| G10 | Eight Memory templates: 13 fields, typed record/status placeholders, separate unknown modified/verified dates, evidence-only approval, drift boundary | Cannot establish actual human authority |
| G11 | 34 templates: neutral scoped fact fields and bounded private-key/credential-like/path/project-identity/sentinel patterns | Not comprehensive secret detection or proof all prose is neutral |
| G12 | Closed 112-input catalog; forbidden payload paths/extensions; exact output inventory and source/tool/ZIP/output hashes | Previously reviewed inputs; no arbitrary host behavior claim |
| G13 | Fresh actual extraction with spaces, regular/contained ZIP members, byte equality; copied standalone checker with denied external source reads | Cooperative Python audit guard, Windows only, no OS sandbox claim |
| G14 | Core <=120 lines/600 words; source/native SKILL <=250 lines/1,200 words; neutral managed block plus 40-word adapter reserve <=250 words | Kiyo budgets, not vendor limits; managed block reserve is design budget |
| G15 | All 105 product files substantial/non-TODO-only; required skill sections populated | Structural substance, not semantic completeness |
| G16 | Exactly REQ-001–080 once, six registry fields, one ten-column trace row each; full verification remains NOT_RUN at this phase | Registration/selected checks do not satisfy every acceptance clause |

G06 and G12 ensure the checked shared contracts/templates are the same bytes in
all three artifacts. G13 independently runs the standalone checker against
extracted content. Test source and fixtures never enter the allowlisted payload.

## Fixtures and expected reasons

All [JSON fixtures](fixtures/README.md) are synthetic mutation specifications.
They introduce no real credentials and execute no suspicious payload. Mandatory
cases: broken-resource, duplicate-skill, unsupported-manifest-field,
missing-approval-boundary, contradictory-fake-pass and private-package-file.
Additional cases cover case/escape, template contamination, control/requirement
duplicates, memory approval defaults, missing resources/AST owners and budgets.

Equivalent prose rewrites may require deliberate review of pinned normative
clauses. Change a contract assertion only against its source requirement; do not
remove an invariant or negative case to obtain green output. New release fields,
skill inventory, control counts, input catalog or acceptance phase require
explicit contract review. Reports preserve prior failures.

See [validation report](../../docs/evidence/static/validation-report.md) and
[coverage interpretation](../../docs/evidence/static/coverage-interpretation.md).
Static PASS does not prove an agent follows Markdown. Behavioral/live-host
evidence not run by this suite is **NOT_TESTED**; scenario execution remains
NOT_RUN. Prior source trials are separate bounded evidence.

