# Project configuration

## KIYO-CONFIG-001 — Reuse one evidenced project configuration

Configuration is static agent-followed Markdown. Fields describe context and
instructions, not native permissions, a parser API or automatic host loading.
Follow [policy resolution](../governance/policy-resolution.md) for authority and
[activation](activation-contract.md) for actual loading limits.

## Location and compatibility

Discover the established accepted locator/config from authorized project guidance.
Retain its path, human sections and field names when they convey the meanings below.
The existing Kiyo default is **.kiyo/policy.md**, the equivalent of .kiyo/config.md.
For a new project an explicitly selected .kiyo/config.md is also possible; create
only one locator/config, never both merely to satisfy these names. No automatic
rename or migration is required. Policy rules may already coexist in that file;
preserve them. Referenced organization/project policies are scoped source records,
not competing config or Memory stores.

Use the [project-context template](../templates/init/project-context.md) only
within authorized Init/config work. Installation, missing fields or a normal
feature task alone do not authorize creation. Missing config is a scoped Unknown,
not a universal block on authorized work. A field needed for a sensitive action
must be resolved before that action. Do not scan global home, credentials or all
organizational repositories to discover a policy.

## Logical fields

These are content expectations, not vendor schema keys. Existing equivalent
labels remain valid; do not rewrite an otherwise adequate record to match wording.

| Field | Meaning, evidence and unresolved handling |
| --- | --- |
| Framework version reference | Intended Kiyo release/revision and its actual source, or UNKNOWN. Keep an observed installed version separate when exposed by an authorized host. A target reference does not prove installation/currentness; never invent a release or infer it from a cache path. |
| Canonical Memory location | Preserve the existing Canonical Memory index locator; the containing store is derived from that single pointer. Resolve relative to the config file, not shell/cache. New default under .kiyo/policy.md is memory/index.md. Respect legacy locations, worktree/component scope and actual access; competing locations need resolution before writes. |
| Selected technology profiles | Existing Selected profiles and Profile evidence: relevant component, inspected config/version/toolchain/architecture and selection source. NONE selected or UNKNOWN is valid. Profile names do not install packages, infer the stack or mandate modernization. |
| Governance profile | Existing Governance preferences may record an optional preset, local refinements, acceptance status/source and scope. NONE selected is valid. A proposal is not adopted policy. Keep task-specific G1–G4 and risk separate. |
| Approved policy references | Actual policy path/record, applicable section/scope and acceptance evidence. A bare link or APPROVED label alone is insufficient. Record unaccepted candidates separately as PROPOSED/UNVERIFIED; use none established in inspected scope when appropriate. |
| Reporting language | Actual user/project preference with source, or UNKNOWN. Absent preference, follow current user/native instructions; do not infer language from organization/domain or permanently rewrite config every task. |
| Optional evidence output location | Optional established project-relative destination with scope/handling reference, or not configured. Resolve from config. A destination is not write approval: chat stays default and read-only tasks save nothing. Respect actual report/data/retention rules; never use plugin cache. |

Framework references are review inputs, not forced upgrades. Profiles and policy
references may be component-specific in a monorepo; do not apply one component's
exception to siblings. An existing config outside the new default requires known
authority and readable locators, not a duplicate .kiyo store. A moved/broken
reference is unresolved; do not silently fetch a replacement or choose by date.

## Reuse and updates

Read only applicable config/policy sections alongside authorized Memory. Reuse
unchanged context already available in the current task. Recheck material inputs
after branch/worktree/component switches, changed config/policy, revoked/expired
authority or context loss. No watcher or automatic freshness guarantee exists;
users do not need to author a new config before every task.

Before an authorized update, reread the latest target and referenced authority,
compare a necessary delta and preserve concurrent human edits. No delta means no
write or date refresh. Changing preferences is distinct from changing accepted
policy; [policy adoption/edit approval](../governance/policy-resolution.md#policy-changes-and-exceptions)
does not authorize the operational action afterward. Never weaken policy to let
the current task pass. Keep mutable config, Memory and reports in the consumer
project; shipped templates remain generic and installed resources immutable.

Init may propose neutral [organization](../templates/policies/organization-policy.md)
and [project](../templates/policies/project-policy.md) templates when relevant.
Creating a requested draft does not adopt it, assign an owner, choose a provider
or enable host permissions. Security governance review can inspect selected
configuration for completeness/conflicts; a completed review proves neither
enforcement nor organization-wide compliance.
