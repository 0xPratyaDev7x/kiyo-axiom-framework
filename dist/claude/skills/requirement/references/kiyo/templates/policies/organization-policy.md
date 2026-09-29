# Organization policy template

Optional neutral artifact for an authorized draft. Follow
[policy resolution](../../governance/policy-resolution.md) and
[data/provider handling](../../governance/provider-policy.md). Copy only the
fenced body into the consumer's established policy location when writing is
authorized. Fill from actual evidence; retain UNKNOWN or a proposed decision
where needed, remove prompts/unused optional sections and never invent approval.
This template is not accepted organization policy and does not enforce access.
Use non-sensitive role/record references; no credentials, PII, raw logs or
private reasoning. Do not populate company facts in the distributed template.

## Artifact body

```markdown
# Organization AI policy

- Policy ID / revision: <existing stable record identity; proposed ID if new>
- Organization / applicable scope: <evidenced organization and projects/components, or UNKNOWN>
- Owner: <actual responsible role/source, or UNKNOWN>
- Source: <actual policy origin/record and section references, or UNKNOWN>
- Status: DRAFT — not adopted
- Review date / scope: <actual completed review date and sections, or NOT_REVIEWED>
- Next review due: <only if established; otherwise UNKNOWN>
- Acceptance source / authorized approver: <only evidenced record/role and scope, or NOT_ESTABLISHED>
- Effective / expiry conditions: <actual terms, or UNKNOWN; no implied indefinite grant>
- Last modified: <actual edit date only; not evidence of review/approval>

## Allowed AI uses
<Allowed purposes, actors, affected projects/environments and exclusions.
Distinguish proposed uses from accepted uses; unknown allowance is not approval.>

## Approved provider, account and model
<Actually evidenced permitted combinations, data/use scope and policy source,
or UNKNOWN. Separate desired configuration from observed host/account facts.
No credentials/account secrets; an Enterprise label alone is insufficient.>

## Data classifications and handling
<Apply actual content/policy to Public / Internal / Confidential / Restricted,
or map the organization's established classes explicitly. Record permitted
audience/destinations, minimization and unknown handling; do not classify by extension.>

## File, tool and network expectations
<Scoped read/write/execute expectations, resources, destinations and evidence
needed from native controls. Policy text itself grants no access or enforcement.>

## Dependencies
<Need/provenance/license/change review and permitted adoption/install scope.
Separate adding a declaration from executing install/lifecycle scripts.>

## Sensitive action approvals
<Actual action classes, authorized human decision process, approval evidence,
resource/environment/data limits and reassessment triggers. Reuse valid scope.
Policy revision/adoption approval does not itself approve operational execution.>

## Prohibited operations
<Accepted prohibitions and scope with source, or proposed restrictions clearly
marked. Native denial cannot be overridden. Do not invent organization bans.>

## Memory and reports
<Canonical state locator/reference; permitted minimized contents, audience,
storage and actual retention/deletion policy or UNKNOWN. Chat is default;
an output path does not authorize a write. No secrets/PII/raw logs/private reasoning.>

## Exceptions and expiry
<For each real exception: stable ID, parent rule, reason, source/authorized human
acceptance, exact scope/conditions, validity/expiry and renewal/revocation process.
If none established, say so. Do not create an approved exception from this prompt.>

## Conflicts, changes and history
<Authorized resolution process and historical record references. Surface material
conflicts, preserve previous decisions and do not silently weaken rules.
Review due dates and last modified do not automatically expire accepted policy.>
```
