# Application Security review boundary

## KIYO-SEC-010 — Review application behavior separately from agent skills

Agentic Security reviews the agent's instructions, skill provenance, authority,
tool use and operating boundaries. Application Security reviews the software the
user is building. A clean skill review does not establish application security,
and a secure application does not establish safe agent behavior.

Use this shared application-review checklist in an authorized Security/Review
task, starting from actual changed behavior, data flow and inspected code/config.
Do not infer the framework, routes, schema or production deployment. Record
applicability with reasons and inspect relevant evidence rather than forcing every
item onto a Markdown-only change. Review remains read-only by default.

| Concern | Concrete review and evidence to seek when applicable |
| --- | --- |
| Validation | Trust-boundary inputs, domain constraints and failure behavior; inspect validators and negative/boundary test results |
| Authentication and authorization | Identity/session assumptions, server-side role/object/tenant access checks and denied cases; use synthetic identities, never real credentials |
| Injection | Untrusted data reaching queries, commands or rendered output; inspect parameterization/context handling and bounded negative cases |
| Sensitive logs | Logging/error paths and redaction/access rules; use synthetic sensitive markers, not copied production logs |
| File/path handling | User-controlled paths, containment, traversal, symlink/archive behavior and allowed resources; inspect code and safe fixtures |
| External calls / SSRF | Destination selection, redirects, address resolution and network boundary assumptions; use approved mocks/local synthetic cases, no cloud-metadata or external probing |
| Unsafe deserialization | Formats, type/tag handling, parser configuration and untrusted object construction; inspect without executing hostile input |
| Cryptography | Established library use, key-management boundaries and evidenced algorithm/configuration requirements; no invented guarantees or custom cryptography |
| Dependencies | Exact declared/resolved inputs, provenance and current relevant advisories; follow dependency governance and report scans not run |

For each finding cite inspected location, expected/observed behavior, evidence,
risk/reason, remediation proposal, owner and limitations. Select permitted tests
for the affected boundary; a source finding is not proof of exploitability or
production state. No fix, scan install, exploit or deployment is implied by review.
Use [governance scope](../governance/ai-usage.md) for any requested transition and
[separate check layers](trust-review.md#kiyo-sec-007--keep-review-layers-and-blind-spots-explicit).

Optional provenance: [OWASP ASVS official project](https://owasp.org/projects/asvs),
checked 2026-09-29, DOCUMENTED_ONLY. Main text identifies stable 5.0.0; sidebar
also uses bleeding-edge wording. This is an original Kiyo topic checklist from
the task scope, not a clause-by-clause ASVS assessment, a full application audit
or OWASP/ISO certification. Pin and inspect the actual applicable standard before
making requirement-level mappings; do not invent clause IDs.
