# Control ownership and target parity

Kiyo controls are advisory instructions. The categories below assign responsibility,
not evidence that a person accepted a role or that a native mechanism exists.

| Control owner | Responsibility | Cannot be inferred |
| --- | --- | --- |
| Kiyo Markdown guidance | State boundaries, inspect authorized evidence, report conflicts/gaps and stop dependent work | Hard enforcement, complete observation or reliable model compliance |
| Host-native security | Actual tool/file/network permissions, trusted loading/parsing, isolation and native denial | Enabled settings, cross-host parity or safe execution merely from documentation |
| Developer release process | Review exact source/dependencies/overlays, validate artifacts and record actual release checks | A signed/hashed artifact is safe, or review covers bytes it never inspected |
| Human organization process | Accept policy, appoint accountable owners, approve permitted scope, revoke and handle incidents | A generated record is authentic approval, or confirmation overrides host/policy denial |

## KIYO-SEC-006 — Establish required host controls or hold dependent execution

Before an action needing isolation, identify the actual required boundary:
files/write scope, process privileges, secrets, network/destination and relevant
data. Record requirement/policy source, responsible host/organization role,
observed host/version/configuration, evidence date/scope and any gaps. Product
claims or labels such as sandbox are insufficient evidence that the specific
action is contained.

If a required control cannot be verified, **HOLD the dependent execution or data
exposure**. Continue authorized static review or propose a separately permitted
synthetic environment. If evidence establishes the requirement is unsupported,
report UNSUPPORTED for that capability; mere absence of evidence is UNKNOWN.
An applicable denial remains DENY. Do not silently weaken the requirement,
change native settings, bypass a tool denial or ask for repeated confirmation
of a prohibited action. Use [approval policy](../governance/human-approval.md).

Kiyo has no sandbox, cannot block network traffic itself and does not verify
signatures at runtime. Documentation of a native feature is DOCUMENTED_ONLY;
live verification needs an actual scoped observation. Reading restricted data
can expose it even without execution. Host controls and data handling may apply
before Kiyo loads, which this guidance cannot retroactively protect.

## KIYO-SEC-008 — Keep accountable optional file records

Use a minimal inventory and accepted owner/approval/revocation/incident record
when required by actual organization policy or requested by the user. Discover
existing records first; preserve their location and human edits, and do not
create a competing inventory. Unknown owners/approvers remain UNKNOWN. An AI/PM
agent cannot approve its own use or impersonate a human decision.

Link artifact identity, reviewed scope, actual evidence and status. Record
revocation separately from confirmation that a native disable/uninstall occurred.
A revocation document is not a kill switch. Incident records distinguish suspected
and observed effects; authorized humans decide containment and notification.
Do not automatically contact others, destroy evidence or perform production action.

### Optional file records

| Template | Purpose |
| --- | --- |
| [Inventory](../templates/skill-governance/inventory.md) | Artifact/source, owner, scope, review and approval locators |
| [Approval](../templates/skill-governance/approval.md) | Concrete proposal and genuine human scope/validity evidence |
| [Revocation](../templates/skill-governance/revocation.md) | Decision scope plus separately observed native action |
| [Incident](../templates/skill-governance/incident.md) | Sanitized observations, uncertainty, authorized response and closure limits |

These are neutral files, optional to populate, not a database, live registry,
watcher or automatic enforcement. Populate only within write scope in an existing
user-selected project/organization location outside plugin cache; no mandatory new
.kiyo directory is implied. Keep secrets, PII, raw logs and private reasoning out.
Use non-sensitive role/evidence locators and [Memory rules](../framework/memory-specification.md)
if an actual memory entry is also needed. Read-only/no-delta means no writes.

## KIYO-SEC-009 — Verify each platform control independently

Compare canonical guidance and required native properties for every actual
target, artifact and host version. For each row record source/date, exact overlay
fields if any, actual behavior evidence, owner, status, limitation and required
resolution. Do not transplant unsupported permission fields or infer IDE parity
from a CLI result. Static content parity, native capability and observed behavior
are separate results; test installation/loading, referenced resources and update
scope independently before claiming compatibility.

Current **review baseline**, recorded 2026-09-29: canonical guidance is authored,
but no Kiyo native overlay/package or live control trial is implemented. U/T means
native control capability UNKNOWN for this assessment / live NOT_TESTED. I/T
means the same control result plus a prior native-plugin route gap. It is not a
claim that standalone IDE facilities lack all security controls.

| Control / required evidence | Claude Code CLI | Claude Code VS Code | Codex CLI | Codex IDE Extension | GitHub Copilot CLI | GitHub Copilot VS Code |
| --- | --- | --- | --- | --- | --- | --- |
| KIYO-SEC-001 trust/source matches loaded artifact | U/T | U/T | U/T | I/T | U/T | U/T |
| KIYO-SEC-002 metadata schema and honest loading | U/T | U/T | U/T | I/T | U/T | U/T |
| KIYO-PERM-001 least privilege and denial | U/T | U/T | U/T | I/T | U/T | U/T |
| KIYO-SEC-003 injection/authority behavior | U/T | U/T | U/T | I/T | U/T | U/T |
| KIYO-SEC-004 provenance of installed resources | U/T | U/T | U/T | I/T | U/T | U/T |
| KIYO-SEC-005 update scope and preserved user state | U/T | U/T | U/T | I/T | U/T | U/T |
| KIYO-SEC-006 required isolation/destination limits | U/T | U/T | U/T | I/T | U/T | U/T |
| KIYO-SEC-007 review/behavior observation completeness | U/T | U/T | U/T | I/T | U/T | U/T |
| KIYO-SEC-008 human approval/revocation versus native effects | U/T | U/T | U/T | I/T | U/T | U/T |
| KIYO-SEC-009 cross-target parity and missing controls | U/T | U/T | U/T | I/T | U/T | U/T |

I/T retains the 2026-09-28 documentation-only finding from the official
[Codex plugin reference](https://learn.chatgpt.com/docs/plugins): the IDE native-plugin
route was **UNSUPPORTED**. This claim was **NOT_REVALIDATED in this security step**;
recheck before implementation. No standalone fallback or scope reduction is
approved by this baseline. Other native schema/permission claims are not refreshed
here. The external link is optional provenance, not a runtime dependency.

Resolve each required gap through current native evidence and permitted trials.
If a target cannot satisfy a required control, hold dependent use on that target
and expose the unsupported gap. Do not hide it behind shared Markdown or copy a
successful result from another column.
