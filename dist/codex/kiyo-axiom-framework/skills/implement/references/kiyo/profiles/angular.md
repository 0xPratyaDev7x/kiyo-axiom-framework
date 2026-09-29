# Angular profile

**First inspect actual versions, configuration, toolchain and architecture:**
package/lock metadata, workspace/project configuration (angular.json when used),
TypeScript/build/test configuration, package scripts, CI and affected application
boundaries. Separate configured versions from observed tool versions. Inspect
the actual component, routing, forms and state patterns; do not infer them from
an Angular package alone or from current vendor examples.

Apply [KIYO-PROF-001](extension-contract.md) and only relevant
[engineering checks](../framework/engineering/index.md).

- Preserve the project's module/standalone organization, change detection,
  forms/state approach and styling/component libraries. Do not force signals,
  zoneless, spartan, Tailwind or a forms/state architecture migration.
- Match APIs to the verified project version. Inspect existing input/output,
  lifecycle/subscription, dependency and template conventions before editing.
  Keep public component/route contracts compatible unless change is authorized.
- For UI behavior, check applicable validation and error/loading/empty states,
  keyboard/focus and labels; include relevant interaction/accessibility checks
  without inventing compliance results. For sensitive input or unsafe rendering
  apply the shared application-security checklist.
- Use existing builders/test tools and scoped commands after script/target
  inspection. A configured target can have side effects; do not run installs,
  migrations or deployment just because they appear in a test script.
- A small component/typo fix must not upgrade Angular/packages, reformat the
  workspace or replace state/forms. Flag insecure patterns with evidence and a
  scoped alternative instead of reproducing them.

Completion evidence: affected project/config versions and unknowns, preserved
architecture/contracts, selected checks with observed results and untested
browser/device/assistive contexts.

Optional provenance, **checked 2026-09-29, DOCUMENTED_ONLY**:
[Angular workspace configuration](https://angular.dev/reference/configs/workspace-config)
describes workspace/project settings and builder targets for Angular CLI.
This does not prove every Angular repository uses that layout, establish API
compatibility for its version, or validate its commands. No Angular fixture or
native-host profile execution is claimed; guidance is authored, not tested support.
