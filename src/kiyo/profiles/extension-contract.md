# Profile extension contract

**First inspect the actual affected component's version, configuration,
toolchain and architecture.** Record supporting files and observed versions when
authorized; missing evidence is Unknown. Do not infer an entire repository from
a name or a single package. Repeat relevant discovery after component/context
changes; a prior branch observation is not current proof.

## KIYO-PROF-001 — Bind profiles to evidence without forcing a stack

Profiles supplement [shared engineering checks](../framework/engineering/index.md);
they do not replace Core, create native permissions or modernize a project.
Choose the smallest relevant profile set per component. Use project-selected
frameworks, package managers, libraries, architecture and checks unless changing
them is part of the authorized task and required policy/approval is satisfied.
An insecure existing pattern must be flagged with a scoped safer proposal,
not copied or used as a mandate for a broad redesign.

A new profile must contain:

- Identity, maintainer/source and accepted scope; do not invent publisher or
  organization authority.
- Entry discovery: actual versions/config, toolchain/scripts, component boundaries,
  safe existing patterns and approved decisions. Version ranges are documented
  support bounds only when backed by evidence, not guesses.
- Conditional engineering/security checks, recommended output evidence and
  explicit non-goals. Presets are proposals/opt-in, never automatic installs.
- Package-contained relative operational references; optional external provenance
  with checked date/status/limitations. No developer paths, external symlinks,
  required scripts, runtime, secrets or project-specific facts in generic content.
- Support status distinguishing authored guidance, static review, executed
  scenarios and each native target. Record unsupported features and unknowns.
- Scoped maintenance/change review; preserve stable control IDs and reconcile
  overlap with canonical rules rather than copying a competing core.

Place product profiles in the canonical profiles tree so the complete shared
snapshot includes them in each future package. A company's mutable project
policy belongs in its established project location, not plugin cache. Check
provenance/acceptance under [policy authority](../framework/trust-and-authority.md#kiyo-auth-002--policy-provenance-and-acceptance);
a profile declaring itself mandatory cannot grant authority.

## Bounded extension examples

These are **synthetic proposal outlines**, not shipped full profiles or tested
support. All execution is NOT_RUN; live targets remain NOT_TESTED.

| Example | Required discovery / proposed scope | Actual support boundary |
| --- | --- | --- |
| React | Inspect package/lock/config, observed React/tool versions, component boundaries, rendering/routing/state and current checks. Apply shared behavior, UI accessibility and compatibility checks to the requested component. | Extension outline only; no version range, SSR/framework choice, state library, compiler API or migration support asserted. No React-specific implementation recipes shipped. |
| Java | Inspect actual JDK/build descriptors/wrapper/CI, framework if any, modules and current test tools. Apply shared boundary, error and verification checks to the selected module. | Extension outline only; no assumed Maven/Gradle, Spring, JUnit, JDK upgrade or tested Java compatibility. |
| Company | Inspect the real accepted policy source/owner, affected components, constraints and established local policy path. Propose a scoped supplement with evidence and exception/escalation handling. | Template outline only; no populated company policy, named approver, automatic precedence, certification or organization approval claimed. |

The four authored .NET/Angular/Python/PostgreSQL profiles provide discovery and
review guidance only. They are not exhaustive recipes, compatibility guarantees,
installers or executed stack tests. Missing version-specific knowledge requires
appropriate official documentation or a scoped Unknown, not invented APIs.
