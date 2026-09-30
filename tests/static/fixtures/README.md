# Synthetic negative fixtures

Checked: 2026-09-29. These 23 JSON records describe in-memory mutations of the
reviewed product snapshot; they are not shipped examples or executable attacks.
No real secrets are used. Each must raise its expected code and include the
specified diagnostic fragment. A precondition failure or unrelated error FAILs
the test; it cannot count as successful rejection.

| Fixture | Group | Required rejection | Diagnostic fragment |
| --- | --- | --- | --- |
| [absolute-developer-path](absolute-developer-path.json) | G11 | TEMPLATE_SENSITIVE_CONTENT | templates/memory/project.md |
| [approved-memory-default](approved-memory-default.json) | G10 | MEMORY_APPROVAL_DEFAULT | decisions.md |
| [bootstrap-budget](bootstrap-budget.json) | G14 | CONTEXT_BUDGET | bootstrap |
| [broken-resource](broken-resource.json) | G04 | RESOURCE_MISSING | SYNTHETIC-missing.md |
| [case-mismatched-link](case-mismatched-link.json) | G04 | RESOURCE_CASE | kiyo.md |
| [contradictory-fake-pass](contradictory-fake-pass.json) | G08 | EVIDENCE_CONTRADICTION | EVID-01 |
| [duplicate-requirement](duplicate-requirement.json) | G16 | REQUIREMENT_DUPLICATE | registry |
| [duplicate-skill](duplicate-skill.json) | G01 | DUPLICATE_SKILL | duplicate |
| [escaping-link](escaping-link.json) | G04 | RESOURCE_ESCAPE | SYNTHETIC-outside |
| [fake-project-fact](fake-project-fact.json) | G11 | TEMPLATE_PROJECT_FACT | observed_date |
| [invalid-release-version](invalid-release-version.json) | G05 | MANIFEST_PROPERTIES | Invalid manifest version |
| [invalid-frontmatter](invalid-frontmatter.json) | G02 | FRONTMATTER_FIELDS | review |
| [mismatched-release-version](mismatched-release-version.json) | G05 | RELEASE_IDENTITY_PARITY | copilot |
| [missing-approval-boundary](missing-approval-boundary.json) | G07 | APPROVAL_BOUNDARY_MISSING | KIYO-AUTH-003 |
| [missing-ast-owner](missing-ast-owner.json) | G09 | AST_FIELDS | AST01 |
| [missing-procedure](missing-procedure.json) | G03 | REQUIRED_FILE | workflows/review.md |
| [private-package-file](private-package-file.json) | G12 | PAYLOAD_ALLOWLIST | private/ |
| [read-only-write-grant](read-only-write-grant.json) | G07 | UNREQUESTED_WRITE | review |
| [sensitive-template](sensitive-template.json) | G11 | TEMPLATE_SENSITIVE_CONTENT | templates/memory/project.md |
| [todo-only-procedure](todo-only-procedure.json) | G15 | TODO_ONLY | workflows/review.md |
| [unknown-control](unknown-control.json) | G06 | CONTROL_REFERENCE | undefined |
| [unreviewed-product-file](unreviewed-product-file.json) | G12 | INPUT_ALLOWLIST | unreviewed |
| [unsupported-manifest-field](unsupported-manifest-field.json) | G05 | MANIFEST_FIELDS | copilot |

Operations: replace requires exactly one matching region; copy uses path as
source and value as fresh destination; package-add uses path as target name and
match as new relative payload path. Append/set/delete/json-field operate only on
isolated byte dictionaries. Every test gets a fresh copy; the next test and
actual source/archive files are unaffected. The six user-required negative IDs
are checked by the runner independently of fixture count.

The absolute-path canary specifically guards the narrowed path pattern after
the initial false positive on ordinary prose. Good/bad example roles remain
separate; no fake PASS execution record is emitted as successful evidence.

See [test contract](../README.md) and
[actual results](../../../docs/evidence/static/test-results-final.json).

