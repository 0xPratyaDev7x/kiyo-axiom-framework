# Skill revocation record template

Separate an authorized human revocation decision from a proposed response and from any native disable/uninstall. Preserve history; never imply that a file can terminate running sessions.

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
# Skill revocation record

Record ID: <stable project-local ID>
Record type/status: <proposal/pending or evidenced decision/status>
Affected skill/artifact/host/scope: <exact target; UNKNOWN where uninspected>
Reason and finding evidence: <sanitized source/impact>
Approval or use scope being revoked: <existing record/reference>
Decision authority/evidence/date: <actual non-PII authorized human role and trusted source, or UNKNOWN>
Effective conditions and limits: <actual scope/time; no invented dates>
Proposed native response: <disable/uninstall/restrict/review as applicable, not executed by this record>
Action authorization: <separate valid scope or UNKNOWN>
Native action observed: <NOT_RUN unless actual evidence exists>
Residual exposure and active-session uncertainty: <known effects/gaps; no retraction guarantee>
Follow-up owner/evidence: <actual role acceptance or UNKNOWN>
Last modified: <actual edit date>
Last verified date and scope: <actual verification or NOT_RUN>
```
