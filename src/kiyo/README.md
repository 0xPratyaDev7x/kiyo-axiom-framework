# Kiyo canonical source — authoring scaffold

This directory is reserved for the single authored Kiyo product specification.
Prompt 03 created this non-runtime authoring note. Prompt 04 adds
[KIYO.md](KIYO.md), shared Core instructions, the control index and expected
response examples under framework/. At that step skills/native packages were not implemented;
native packages remain unimplemented and Core behavior on hosts remains untested. Prompt 05 adds the
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
Prompt 08 adds the shared [Workflow Router](workflows/workflow-router.md),
adaptive/implementation/read-only flows and bounded repair/handoff guidance.
Thirty routing rows and nine recovery/flow specifications are developer-only
expected behavior, NOT_RUN; no executable router or public skill is created.

Prompt 09 adds [six engineering standards](framework/engineering/index.md),
a dated concept-to-rule/evidence mapping, four optional stack profiles and the
[extension contract](profiles/extension-contract.md). React/Java/company examples
are bounded outlines, not full supported recipes. Sixteen developer-only scenario
specifications remain NOT_RUN; no stack/runtime/package is installed.

Prompt 10 adds the shared [Evidence Contract](framework/evidence-contract.md),
[Definition of Done](framework/definition-of-done.md), [reporting contract](framework/reporting-contract.md)
and seven neutral report templates, with 20 synthetic good/bad scenario
specifications kept developer-only and NOT_RUN. Chat remains the default;
no reporting engine, automatic log, public skill or evidence archive is added.

Prompt 11 authors the first canonical [Init skill](skills/init/SKILL.md),
logical ID kiyo.init, with a complete [procedure](workflows/init.md), bounded
discovery, conditional managed-bootstrap guidance, output examples and a neutral
project-context template. Sixteen Init scenario specifications are developer-only;
actual forward-trial evidence is recorded separately from the specifications.
The entry has name/description only. Remaining seven skills and native overlays/
prepared packages are still pending; source-directed use is not native installation.

Prompt 12 adds the canonical [Requirement skill](skills/requirement/SKILL.md),
logical ID kiyo.requirement, its [shared procedure](workflows/requirement.md),
neutral requirement template and readiness checklist. It uses authorized evidence,
returns chat by default and permits only explicitly scoped specification output.
Readiness never starts implementation or authorizes Memory/source/test/config edits.
Twelve scenario specifications and separate bounded evidence remain developer-only;
six public skills and native packages are still pending.

Prompt 13 adds canonical [Implement](skills/implement/SKILL.md), logical ID
kiyo.implement, and a neutral [short plan](templates/short-plan.md). It reuses the
existing implementation/repair/handoff and engineering-report contracts, adds
explicit daily engineering boundaries and requires actual authorized checks.
Developer scenarios/trials remain outside the payload. Five public skills and
native packages are pending; no runtime or automatic commit/PR/deployment is added.

Follow [framework layout](../../docs/architecture/framework-layout.md),
[content loading](../../docs/architecture/content-loading.md) and
[packaging contract](../../docs/architecture/packaging-contract.md) as their
authorized implementation prompts arrive. The complete planned tree lives there;
do not create empty skill files or a second core tree to imitate completeness.

This README is developer-only and excluded from native payloads. Future product
instructions must not depend on it or on developer documentation. Keep populated
project policy/memory out of this directory. Kiyo Compass remains a working name;
no release version, publisher or license decision is introduced here.
