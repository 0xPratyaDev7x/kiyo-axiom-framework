# Init project-context template

Use only when an authorized Init needs a local Kiyo locator/preferences record
and no existing accepted configuration already provides it. The default for a
new unconfigured project is .kiyo/policy.md; preserve an established path.
This is advisory Markdown, not native plugin metadata or a policy engine.

Follow [Init procedure](../../workflows/init.md) and
[policy authority](../../framework/trust-and-authority.md#kiyo-auth-002--policy-provenance-and-acceptance).
Use only the fenced body; replace prompts from actual evidence, remove unused
optional lines and all template instructions. Keep project-specific information
in the consumer project, never this shipped template or plugin cache.
Path values are relative to the containing config file; for the default new
.kiyo/policy.md, memory/index.md points to .kiyo/memory/index.md. Do not use that
default when an accepted legacy store/index already exists.

## Artifact body

```markdown
# Kiyo project context

This record describes project-local Kiyo context. It does not override native
instructions, accepted organization policy or the user's actual authorization.

- Project/component scope: <actual root/component description; no developer-machine path>
- Canonical Memory index: <actual config-file-relative existing/new index path>
- Setup authority/source: <actual initialize request or accepted project record; no invented approver>
- Selected profiles: <evidence-supported profile names and relevant component, or NONE selected>
- Profile evidence: <actual project-relative config/source references, or UNKNOWN>
- Governance preferences: <actual requested preference and source/scope; PROPOSED if unaccepted, or none requested>
- Confirmed constraints: <sourced accepted constraint, or none established in inspected scope>
- Unknowns/limitations: <uninspected scope, unresolved versions/authority/activation>

```

Record durable claims with the full Memory envelope in appropriate topic entries;
this config holds locators/preferences, not a competing architecture inventory.
An existing accepted policy's constraints/owner/history are preserved; this
minimal record does not create an organization policy pack or grant permissions.
