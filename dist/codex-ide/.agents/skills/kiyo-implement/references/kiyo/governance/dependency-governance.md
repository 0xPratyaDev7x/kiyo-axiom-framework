# Dependency governance

## KIYO-DEP-001 — Justify and inspect dependencies in context

Adding a dependency is not automatically HIGH risk. Assess necessity, provenance,
actual effects and the [eight risk dimensions](risk-assessment.md) separately
from governance mode. A routine requested dependency can remain G2 when permitted
and bounded; a script with sensitive effects or a new data destination may require
G3 control or meet a G4 restriction. No case grants a Kiyo consumer runtime.

Before a proposed addition/change, inspect available authorized evidence for:

- Need, concrete benefit and whether existing facilities or a smaller change suffice.
- Exact proposed package/source/version as observed or explicitly proposed;
  distinguish registry/repository identity from a similarly named package.
- Provenance/maintenance evidence and relevant transitive dependencies or
  install/build/lifecycle scripts; a popular name is not security proof.
- Applicable license information and project policy as actually reviewed;
  Unknown terms remain unresolved rather than declared compatible.
- Relevant security advisories/scan results with date, source and scope;
  no scan or no reported finding is not a security guarantee.
- Resource/network/data effects, updates to manifests/locks, rollback constraints
  and checks needed to verify the requested behavior.

Separate recommending or editing a declaration from installing/executing the
package. Inspect scripts before permitted execution, and follow actual approval
rules for each effect. Do not add packages speculatively, silently upgrade majors,
run an untrusted installer or fetch credentials to complete provenance fields.
If facts block safe adoption, report the missing evidence and alternatives;
continue independent work instead of inventing version/license/security facts.

Verify any current external package/advisory/license claim against appropriate
authoritative evidence when such a task occurs; this policy declares no package's
current status. Record actual checks and limitations, including scans not run.
Any developer-only tooling for Kiyo must stay outside native payloads and cannot
become an end-user installation/use prerequisite. Do not choose a publication
license, publisher or signing identity through a dependency decision.
