# .NET profile

**First inspect actual versions, configuration, toolchain and architecture:**
relevant project/solution files, target frameworks, global.json if present,
package/central version files, build props/targets, lock/restore settings and CI.
Distinguish configured SDK selection, target framework and observed SDK/runtime;
do not invent one from another. Inspect references, affected layers/modules and
nearby tests before describing architecture or picking a command.

Apply [KIYO-PROF-001](extension-contract.md) and only the relevant
[engineering checks](../framework/engineering/index.md).

- Preserve project-selected test framework, adapter/runner and packages. Inspect
  actual test configuration/scripts and side effects before choosing verification;
  a familiar command or package name does not prove which runner/version is used.
- Follow existing safe dependency boundaries, DI/lifetime patterns, nullability,
  validation/error contracts and async/cancellation conventions where applicable.
  Inspect serialization/persistence/public contracts when the changed path uses them.
- Reuse safe mapping/validation/error handling already established. **xUnit,
  Mapperly, FluentValidation and ProblemDetails are recommendations or opt-in
  preset choices only**, never mandatory dependencies or automatic installations.
  Verify version-specific APIs before proposing their use; preserve another
  suitable project choice.
- An approved Mapperly decision conflicting with AutoMapper usage is drift:
  report both sources and the needed decision. Do not rewrite the decision,
  silently replace a mapper or introduce a new one.
- Do not impose Clean Architecture, CQRS, MediatR, EF Core, a new layer or a
  framework upgrade on a legacy project. Flag unsafe existing patterns with a
  scoped alternative rather than copying them or modernizing adjacent code.

Completion evidence: observed/configured versions with provenance and any
Unknowns, affected boundary/contracts, minimal diff or read-only findings,
selected existing checks with actual results/NOT_RUN and unresolved decisions.

Optional provenance, **checked 2026-09-29, DOCUMENTED_ONLY**:
[Microsoft global.json documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json)
describes SDK selection separately from target runtime;
[Microsoft .NET testing overview](https://learn.microsoft.com/en-us/dotnet/core/testing/)
distinguishes platform and framework. Neither establishes this project's versions,
package choices or safe command. No .NET fixture or native-host profile execution
is claimed; these are authored review instructions.
