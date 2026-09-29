# Activation contract

## KIYO-ACT-001 — Distinguish activation capabilities and their evidence

Kiyo supplies static instructions. The native host discovers files and decides
which instructions enter context. No hook, runtime, MCP component or background
service may be added to simulate always-on Core loading.

| Capability | What establishes it | What it does not establish |
| --- | --- | --- |
| Explicit skill invocation | User selects an actually available native skill entry using that host's evidenced syntax | Automatic Core loading, successful execution or approval of every action |
| Implicit skill selection | Observed host selection for a particular prompt/configuration | Explicit user invocation or reliable selection for all future prompts |
| Automatic Core loading | Target-specific evidence that a native facility loaded the Core under stated conditions | That all sessions/targets load it or that the agent obeyed every control |
| Agent-directed Core read | Actual read of the packaged bootstrap after selection or authorized request | Native automatic loading or permanent installation |

Use only native facilities established for the exact target, version and scope.
Documentation can support a candidate mechanism; it does not prove a Kiyo run.
Before claiming automatic activation, require actual target-specific loading
evidence. Keep CLI and IDE observations separate, even within one ecosystem.
Never invent commands, manifest fields, include behavior or plugin rules to
close an evidence gap. Permission is not created by successful discovery.

For an activation question, identify the capability, target, environment/version
where known, evidence source/check date and limitation. Use:

- **DOCUMENTED_ONLY:** supported by checked native documentation, not a Kiyo test.
- **NOT_TESTED:** no live test of that capability on the stated target.
- **UNKNOWN:** insufficient/conflicting evidence; do not infer unsupported status.
- **UNSUPPORTED:** an applicable source or observation explicitly establishes the limit.
- **VERIFIED:** an actual recorded observation, limited to the conditions tested.
- **NOT_REVALIDATED:** a freshness/access qualifier for a source not rechecked.

If the host does not load Core automatically, report that limitation plainly.
If loading was not observed, report UNKNOWN/NOT_TESTED rather than asserting
that it failed. A verified native explicit invocation or an authorized direct
read can be offered when available; otherwise state the missing prerequisite.
Do not promise a universal command or silently install project instructions.

Project guidance may be supplied through an authorized, evidenced native facility.
Preserve existing instructions, use project-relative state locators and do not
link to a guessed cache location. Such guidance is separate from metadata-driven
selection. Installation alone is not evidence of per-task Core reads. Removing
a bundle must not be treated as authority to remove user policy or memory.

This file defines a reporting contract, not a support matrix or a live result.
It adds no host-specific schema, invocation or automatic activation claim.
