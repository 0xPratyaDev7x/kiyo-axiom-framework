# Skill inventory record template

One record per actually observed skill/artifact and host scope. Link existing approval/review records rather than asserting that inventory presence authorizes use.

Usage: discover the existing user-owned record location; populate only when
requested or required by accepted policy and writing is authorized. Re-read before
editing and preserve concurrent human changes. Do not create a second inventory,
initialize project memory by default, or write into plugin cache. No delta means
no timestamp touch. Leave unavailable facts UNKNOWN and unrun checks NOT_RUN.
Use [record ownership](../../agent-security/control-ownership.md#kiyo-sec-008--keep-accountable-optional-file-records)
and [human scope](../../governance/human-approval.md). No secrets, PII, raw logs,
private reasoning, developer-repository facts or invented approval belong here.

Copy only the artifact below; replace placeholders from authorized evidence.
Evidence locators must remain meaningful outside an installed package.

```markdown
# Skill inventory record

Record ID: <stable project-local ID>
Record type: observation
Skill identity and stated purpose: <observed identity/purpose or UNKNOWN>
Source and claimed publisher: <permitted source locator; claim is not verified identity>
Publisher/provenance evidence: <inspected evidence or UNKNOWN>
Artifact revision/digest: <actual observation/method or UNKNOWN; never a sample hash>
Host/version and install scope: <observed context or UNKNOWN>
Owner role and acceptance evidence: <non-sensitive role/evidence locator or UNKNOWN>
Allowed purpose/resources/data: <accepted scope or UNKNOWN>
Review evidence and limitations: <record locator/scope or NOT_RUN>
Approval status/scope/evidence: <UNKNOWN, pending, approved, denied, expired or revoked; evidence required>
Revocation/incident references: <existing record locators or none observed within stated scope>
Observed date: <actual observation date or UNKNOWN>
Last verified date and scope: <actual verification or NOT_RUN; not whole-file freshness>
Last modified: <actual edit date when populated>
Uncertainty and next review trigger: <gaps/material changes requiring review>
```
