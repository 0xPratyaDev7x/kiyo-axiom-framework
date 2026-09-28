# Kiyo canonical source — authoring scaffold

This directory is reserved for the single authored Kiyo product specification.
Prompt 03 created this non-runtime authoring note. Prompt 04 adds
[KIYO.md](KIYO.md), shared Core instructions, the control index and expected
response examples under framework/. Skills/native packages are not implemented
or installable yet; Core behavior on hosts remains untested. Prompt 05 adds the
[Memory specification](framework/memory-specification.md),
[shared lifecycle](workflows/memory-lifecycle.md) and eight neutral topic templates
under templates/memory/. These are product instructions, not this developer
project's populated memory. Behavioral scenarios remain specifications only.
Prompt 06 adds [Markdown governance policies](governance/ai-usage.md) and
[expected decision examples](governance/decision-examples.md), without a policy
engine or native permission configuration.
Prompt 07 adds [AST controls and review procedures](agent-security/owasp-ast10.md),
a separate application checklist and four optional neutral governance templates.
The six-target control matrix records gaps; 19 developer scenario specifications
remain NOT_RUN. No public Security skill or security runtime is introduced.

Follow [framework layout](../../docs/architecture/framework-layout.md),
[content loading](../../docs/architecture/content-loading.md) and
[packaging contract](../../docs/architecture/packaging-contract.md) as their
authorized implementation prompts arrive. The complete planned tree lives there;
do not create empty skill files or a second core tree to imitate completeness.

This README is developer-only and excluded from native payloads. Future product
instructions must not depend on it or on developer documentation. Keep populated
project policy/memory out of this directory. Kiyo Compass remains a working name;
no release version, publisher or license decision is introduced here.
