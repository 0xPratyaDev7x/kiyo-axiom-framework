# Honest Kiyo self-check report

Use with the [self-check checklist](../../agent-security/security-submodes.md#self-check)
under one Security skill. Report in chat unless a separate destination is authorized.
The table is a neutral structure; never fill Unknown fields from plausible defaults.

- **Task/scope:** <requested Kiyo subject, selected host-exposed/supplied resources,
  actual target/version when known, inspection date and exclusions>
- **Actions/files changed:** <actual permitted metadata/resource reads and methods;
  no fixes/settings/Memory writes; any separately authorized artifact output>
- **Governance/risk rationale:** <actual read scope, data sensitivity, authority,
  independent G-level/risk basis, denied or held effects>
- **Verification/evidence:** <the fact table and nine-field check records, kept
  separate from capability/assurance labels; actual evidence location or Unknown>
- **Residual issues:** <capability/resource/identity gaps, incomplete inventory,
  undocumented/unverified activation and unperformed methods>
- **Memory impact:** <NONE / UPDATE_REQUIRED / CONFLICT / NOT_ASSESSED with scope
  and evidence; no implicit sync or verification-date refresh>
- **Status:** <DONE / PARTIALLY COMPLETE / BLOCKED / DECISION REQUIRED for the
  requested bounded inspection, never a security/compliance or installation verdict>
- **Next required action:** <specific missing evidence/decision or scoped proposal;
  no automatic installation, global scan, unsafe probe or remediation>

## Observed facts and capability evidence

| Property | Known observation or supplied claim | Exact source / inspected scope / date | Evidence status and limitation |
| --- | --- | --- | --- |
| Identity/version | <name, declared version and separately observed installed identity; Unknown where unavailable> | <actual metadata or exposed host evidence> | <reading a declaration does not authenticate publisher, installed bytes or version> |
| Readable resources | <specific files read/resolved, denied/missing/uninspected resources> | <actual scoped paths/read results> | <no inferred payload completeness or execution> |
| Skill/core availability | <metadata visibility, body read, Core read and inaccessible references separately> | <actual read/host observation> | <a locator or file existing is not proof it entered context> |
| Activation | <explicit selection, implicit selection, agent-directed Core read, automatic loading separately> | <applicable documentation source/check date or actual observed target/conditions> | <DOCUMENTED_ONLY / VERIFIED / UNKNOWN / NOT_TESTED / UNSUPPORTED; NOT_REVALIDATED where appropriate; never upgrade a document to a test> |
| Host capability gaps | <known exposed permissions, unknown required isolation/network properties and held dependencies> | <permitted actual observation or missing evidence> | <text/config claims alone do not verify enforcement> |
| Inspection scope/inventory | <supplied/visible subjects and exclusions; inventory incomplete if enumeration unavailable/partial> | <actual authorized listing or enumeration limit> | <no total/global completeness claim or global home/plugin scan> |
| Signature/integrity | <actual authorized verification evidence or unavailable> | <artifact/trust basis/method only if established> | <NOT_VERIFIED when unavailable; a local hash or Markdown claim is not cryptographic authenticity or safety> |

Use [activation meanings](../../framework/activation-contract.md) and
[Security assurance distinctions](../../workflows/security.md#findings-ownership-and-honest-status).
For actual checks preserve all nine [Evidence Contract](../../framework/evidence-contract.md)
fields: Name, Applicability, Command/method, Inspected scope, Execution status,
Observed result, Evidence location, Limitations and Baseline relation.
NOT_VERIFIED is an assurance label, not a sixth check status.

State relevant untested behavior explicitly. No cryptographic integrity, sandbox
isolation, network enforcement, complete inventory or 100% AST compliance can be
concluded from reading Markdown. No findings means none in inspected scope,
with limitations; LLM review is not proof of safety or independent audit.
