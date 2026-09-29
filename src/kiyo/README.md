# Kiyo canonical source — authoring scaffold

This directory is reserved for the single authored Kiyo product specification.
Prompt 03 created this non-runtime authoring note. Prompt 04 adds
[KIYO.md](KIYO.md), shared Core instructions, the control index and expected
response examples under framework/. At that step skills/native packages were not implemented;
Prompt 20 now adds the Claude development distribution; Core behavior on hosts remains untested. Prompt 05 adds the
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

Prompt 14 adds canonical [Review](skills/review/SKILL.md), logical ID kiyo.review,
its [shared procedure](workflows/review.md), severity/confidence guidance and a
bounded report template; the existing finding template now exposes every required
field. Current workspace/range scope, effective protections, static-versus-executed
evidence and read-only effects remain explicit. Sixteen developer scenarios and
separate trial evidence do not imply native verification. Four public skills and
native packages are still pending.

Prompt 15 adds canonical [Test](skills/test/SKILL.md), logical ID kiyo.test,
a [shared procedure](workflows/test.md), assess/run/write safety matrix and neutral
test plan/report templates. Mode boundaries preserve user intent; only actual
executions support outcomes/counts, and coverage requires measurement.
Eighteen developer scenarios and separate source trials do not establish native
acceptance. Three public skills and native packages remain pending.

Prompt 16 adds canonical [Security](skills/security/SKILL.md), logical ID
kiyo.security, its [shared procedure](workflows/security.md), four logical
submode checklists, security finding and honest self-check report. It reuses
AST/application/governance guidance with supplied-scope read-only boundaries,
unverified-signature/incomplete-inventory distinctions and no automatic remediation.
Eighteen developer scenarios and separate bounded source trials do not prove
native security or full compliance. Architecture and Memory skills remain pending.

Prompt 17 adds canonical [Architecture](skills/architecture/SKILL.md), logical ID
kiyo.architecture, its [shared procedure](workflows/architecture.md), observation
and impact templates and the extended shared drift report. It separates observed
structure, approved intent, proposals and deployment unknowns; assessments stay
read-only. Sixteen developer scenarios and bounded source trials do not establish
production topology or native acceptance. The public Memory entry remains pending.

Prompt 18 adds canonical [Memory](skills/memory/SKILL.md), logical ID kiyo.memory,
[mode definitions](framework/memory-modes.md) and diff/sync/repair reports using
the existing lifecycle. show/check stay read-only; scoped sync/repair preserves
provenance, human edits and decisions with no-delta no-op. Eighteen additional
Memory Skill scenarios and separate source trials do not prove whole-store
freshness or native behavior. All eight canonical public entries are now authored;
native catalogs/packages and complete acceptance remain pending.

Prompt 19 adds [configuration specification](framework/project-configuration.md),
[policy resolution](governance/policy-resolution.md), three optional
[presets](governance/presets.md) and neutral organization/project policy templates.
The established .kiyo/policy.md config equivalent is preserved; no second locator,
provider choice, permission grant or policy engine is introduced. Init can propose
drafts and Security governance can inspect completeness/conflicts. Sixteen
developer scenario specifications remain separate from bounded trial evidence.
Exactly eight public skills remain; real policy adoption is pending. Native packages
were still pending at the close of Prompt 19.

Prompt 20 generates a [Claude native development bundle](../../docs/compatibility/claude-package.md)
from this unchanged canonical product content and a small native overlay.
Eight complete resource snapshots preserve canonical bytes; the developer-only
packager is not installed. Live CLI/VS Code trials remain separately NOT_TESTED.
Prompt 21 also generates the [Codex development bundle](../../docs/compatibility/codex-package.md)
from these same canonical bytes with independent OpenAI metadata and AGENTS guidance.
Offline checks pass; ingestion validation fails absent owner release fields;
CLI live behavior remains NOT_TESTED and IDE plugins UNSUPPORTED. Copilot packaging,
publication identities and final release acceptance remain pending.

Follow [framework layout](../../docs/architecture/framework-layout.md),
[content loading](../../docs/architecture/content-loading.md) and
[packaging contract](../../docs/architecture/packaging-contract.md) as their
authorized implementation prompts arrive. The complete planned tree lives there;
do not create empty skill files or a second core tree to imitate completeness.

This README is developer-only and excluded from native payloads. Future product
instructions must not depend on it or on developer documentation. Keep populated
project policy/memory out of this directory. Kiyo Axiom Framework remains a working name;
no release version, publisher or license decision is introduced here.

## Prompt 22 Copilot output

The [Copilot overlay](../../platforms/copilot/README.md) generates a shared static
CLI/VS Code package from this same canonical content. Target-specific invocation,
instruction discovery and lifecycle remain separate in the adapter and evidence.
No source product file changes; no VSIX/consumer runtime or additional public skill.
All native results remain NOT_TESTED; working identity is not a published listing.
