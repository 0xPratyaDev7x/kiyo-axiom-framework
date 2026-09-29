# Project policy supplement template

Use only for a requested project policy draft or accepted supplement at its
established location. Existing rules may already be in .kiyo/policy.md; preserve
their human sections rather than add a competing file. The
[config template](../init/project-context.md) holds locators/preferences, while
this artifact describes scoped rules and their authority. Neither is a native
manifest. Follow [resolution](../../governance/policy-resolution.md) for adoption.

Copy only the fenced body when writing is authorized. Replace prompts with
actual safe evidence or explicit Unknowns; remove unused optional rows. Do not
invent an organization, approver, date, domain, provider or permission. All new
rules remain proposals until their actual acceptance is established.

## Artifact body

```markdown
# Project AI policy supplement

- Policy ID / revision: <existing identity or explicitly proposed new ID>
- Project/component/environment scope: <actual affected scope, exclusions and source>
- Owner / source: <actual responsible role and record, or UNKNOWN>
- Status: DRAFT — not adopted
- Review date / scope: <actual reviewed sections/date, or NOT_REVIEWED>
- Last modified: <actual edit date; not approval or verification>
- Acceptance source / authorized approver: <evidenced source and scope, or NOT_ESTABLISHED>
- Parent policies: <actual records/sections, applicability and acceptance evidence, or UNKNOWN>
- Existing config / canonical Memory locator: <established relative references; no second store>
- Selected governance preference: <optional preset/refinements, source/status/scope, or NONE selected>

## Local uses, profiles and constraints
<Allowed/proposed AI uses and relevant evidence-backed component profiles.
Preserve project tools/architecture; do not install libraries or select providers.>

## Data, provider and resource expectations
<Applicable parent data/provider/account/model rules; known limits and Unknowns.
Specify scoped file/tool/network expectations and prohibited operations.
Content governs classification; an output path or preset grants no permissions.>

## Dependencies and sensitive actions
<Applicable review/approval rules and local scoped refinements. Identify actual
human authority; distinguish drafting, policy editing/adoption and execution.>

## Overrides or exceptions
| ID / parent rule | Proposed difference and reason | Exact project/action/environment/data scope | Source and authorized acceptance | Validity / expiry / revocation |
| --- | --- | --- | --- | --- |
| <actual ID/rule or proposed ID> | <proposal or evidenced accepted difference> | <bounded scope> | <actual evidence or NOT_ESTABLISHED> | <actual conditions or UNKNOWN> |

Remove the example row when no override is needed. A project statement cannot
relax organization policy without the parent's valid exception authority.
Expired/unverified exceptions grant no operational permission.

## Memory and reporting
<Existing canonical path; minimized allowed content, audience and actual handling/
retention rules. Chat default; optional evidence destination needs independent
write scope. Preserve human sections and decision history.>

## Conflicts, unresolved decisions and history
<Both source sections and material disagreement; actual authorized decision needed.
No code/Memory self-escalation. Preserve accepted intent until valid revision;
record real changes without fabricating review or approval dates.>
```
