# Python profile

**First inspect actual versions, configuration, toolchain and architecture:**
project metadata/configuration (pyproject.toml when present, or existing legacy
packaging files), declared Python constraints, dependency/lock/environment files,
scripts, test/lint/type configuration and CI. Distinguish declared compatibility
from the authorized observed interpreter/environment. Inspect the affected
module, framework if any, boundaries and safe local patterns before selecting tools.

Apply [KIYO-PROF-001](extension-contract.md) and only relevant
[engineering checks](../framework/engineering/index.md).

- Retain the existing package manager, environment/build backend, framework and
  test tools. Do not introduce a new manager or lock format, force FastAPI, or
  replace unittest/pytest/another chosen tool merely as a preferred preset.
- Preserve supported interpreter syntax and public interfaces. Follow the
  project's applicable typing, validation, exception and sync/async conventions;
  inspect resource cleanup and error paths where affected.
- Check changed file/path handling, serialization, process calls and external
  input against the shared application-security guidance. A local unsafe pattern
  is a finding, not permission to copy it.
- Inspect the actual script/test startup, imports and setup side effects before
  execution. Keep dependency additions/upgrades justified and scoped; do not
  silently install a formatter, create environments or change global tools.
- Use focused checks with existing tools; a typo or narrow bug fix does not
  justify packaging conversion, module reorganization or framework modernization.

Completion evidence: declared and observed versions with their sources, relevant
architecture/configuration, minimal change/findings, actual check results or
NOT_RUN and unresolved environment/dependency constraints.

Optional provenance, **checked 2026-09-29, DOCUMENTED_ONLY**:
[PyPA pyproject.toml guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
describes project metadata, Python constraints and build configuration. Its sample
backend/framework dependencies are examples, not Kiyo defaults or proof of local
setup. Legacy configuration remains valid input to discovery. No Python fixture
or native-host profile execution is claimed.
