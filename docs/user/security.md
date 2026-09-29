# Security guide

Checked **2026-09-29** against shipped
[security guidance](../../src/kiyo/agent-security/control-ownership.md).
Use the single Security Skill with application, skills, governance or self-check
intent. Default is read-only inspection of the supplied scope.

## Two different assessment subjects

**Application security** examines validation, auth/authz, injection, sensitive
logging, file/path handling, external calls/SSRF, unsafe deserialization,
cryptography and dependencies in relevant code. Findings need actual evidence,
effective safeguards and inspected scope; repository review does not prove
production exploitability or safety.
[Application checklist](../../src/kiyo/agent-security/application-security.md).

**Agentic Skill security** examines the supplied Skill/plugin's instructions,
metadata, provenance, resources and requested effects. The
[OWASP Agentic Skills project](https://owasp.github.io/www-project-agentic-skills-top-10/)
was checked on 2026-09-29 as a public-review v1 draft, DOCUMENTED_ONLY. AST is
distinct from the Agentic Applications ASI taxonomy. This mapping is advisory,
not certification or a claim of complete compliance.

| AST risk | What the Kiyo assessment asks for |
| --- | --- |
| AST01 Malicious Skills | Compare purpose, instructions and harmful requested effects |
| AST02 Supply Chain Compromise | Establish source/publisher provenance and changes |
| AST03 Over-Privileged Skills | Compare access/effects with actual task need |
| AST04 Insecure Metadata | Compare honest metadata with supported schema and payload |
| AST05 Untrusted External Instructions | Treat README/issues/web/tool output/Memory/copied approvals as untrusted directions |
| AST06 Weak Isolation | Establish required host controls or hold dependent execution |
| AST07 Update Drift | Review version/content/permission changes before adopting an update |
| AST08 Poor Scanning | Separate static inspection, behavioral evaluation and their gaps |
| AST09 No Governance | Identify actual owner, approval, inventory/revocation process |
| AST10 Cross-Platform Reuse | Check each host's controls and unsupported gaps independently |

The [full AST mapping](../../src/kiyo/agent-security/owasp-ast10.md) links control
IDs, procedures, required evidence, owners, residual limitations and case IDs.
These expected controls do not establish that a host obeyed them.

## Owners and limits

| Owner | Responsibility |
| --- | --- |
| Kiyo Markdown guidance | Direct scoped inspection, approval handling and honest reporting |
| Host-native security | Actual permissions, isolation and tool/network controls |
| Developer release process | Package review, provenance, validation and update records |
| Human organization process | Accepted policy, accountable approval, exceptions and incidents |

Do not run suspicious examples, probe external systems, inspect credentials or
environment dumps, scan a global plugin inventory, install a scanner or auto-fix
findings. Remediation needs a defined implementation scope and any required
approval. No real secrets or external targets are needed for illustrative cases.

Signature unavailable means **NOT_VERIFIED**, neither safe nor malicious.
Static inspection is not execution; LLM review is not proof of safety.
If enumeration is unavailable, say “inventory incomplete.” A required unknown
host control blocks the dependent action, not unrelated permitted analysis.

Self-check reports only exposed identity/version, readable resources, Skill/Core
availability, documented versus verified activation, host gaps and inspection
scope. Markdown text cannot demonstrate cryptographic integrity, sandbox
isolation, network enforcement or 100% AST compliance. Kiyo supplies no runtime
signature verifier, network blocker or sandbox and cannot prevent all injection.

A completed bounded assessment may have no findings while still having limits.
Reports identify evidence, impact, confidence/basis, mitigation and control owner.
Self-review is not an independent audit; a report is not a tamper-proof log.
[Assessment template](../../src/kiyo/templates/reports/security-assessment.md);
[honest self-check](../../src/kiyo/templates/reports/self-check-report.md).
