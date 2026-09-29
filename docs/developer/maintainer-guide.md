# Maintainer guide

Checked **2026-09-29**. This describes existing developer tooling and evidence,
not a published release process. Consumers use prepared native packages and do
not run Python, a generator or a Kiyo executable.

## One source, generated distributions

Author rules in [src/kiyo](../../src/kiyo/README.md): Core/framework, governance,
agent-security, workflows, profiles, templates and exactly eight Skills.
Platform manifests/activation metadata live in platforms/claude, platforms/codex
and platforms/copilot. Generated distributions live in dist/. Do not fix a rule
by editing one generated copy.

[Packaging contract](../architecture/packaging-contract.md) and
[distribution build](../architecture/distribution-build.md) define allowed
transformations: entry relative paths/native adapter suffixes, line endings and
target-specific static metadata. Shared content remains mechanically comparable.
Operational references must be inside the payload. Developer docs, tests,
fixtures, logs and tooling remain outside it.

Public docs describe authored contracts and dated evidence. When a behavior
changes, review affected guides/examples and source/overlay parity. Do not add
unsupported native permission fields or turn a submode into a ninth Skill.

## Build and check a candidate

Use the existing Python standard-library toolchain from repository root.
Python 3.11.9 was exercised; this is not a declared minimum version. The following
are **command templates**, not new execution records. Replace placeholders with
fresh developer output paths; do not overwrite historical inventories/results.

```text
python -B tools/package_distributions.py --output <fresh-archive-directory> --inventory <fresh-inventory.json>
python -B tests/packaging/test_distributions.py --report <fresh-packaging-results.json>
python -B tests/static/test_contracts.py --report <fresh-static-results.json>
python -B tests/behavioral/evaluation/test_suite.py --report <fresh-offline-helper-results.json>
```

The closed [input allowlist](../../tools/packaging-inputs.json) excludes .git,
credentials/.env, actual project Memory, private notes, logs, fixtures,
node_modules and developer scripts. Review additions intentionally. Build twice
from identical bytes and compare inventories/archives. Extract to fresh paths,
including spaces, then verify contained exact-case resources and all eight Skills.
Do not treat a cooperative path checker as an OS sandbox.

Existing builders refuse changed pre-existing outputs/inventories. Choose a fresh
destination, inspect any interrupted output, and preserve prior evidence.
Default inventories include historical Git context; later commits should use
fresh paths even if product bytes are unchanged.

Keep the [three evidence layers](../evidence/static/coverage-interpretation.md)
separate:

- P24 static selected properties/negative fixtures: 37 PASS, not full schema or behavior.
- P25 offline behavioral-helper checks: 13 PASS; all 48 host cases NOT_RUN.
- P26 native subsets: Claude metadata/discovery and Codex disposable lifecycle;
  model/activation and most target acceptance remain untested.

These are historical results, not checks run by this guide. Follow the
[behavioral protocol](../../tests/behavioral/evaluation/protocol.md) and
[native reproduction guide](../compatibility/live-reproduction-guide.md) only
with the actual target/account/quota authority. P26 check_records.py audits a
pinned historical build state; do not rewrite its assumptions or old evidence
to make it serve as a later-step acceptance gate.

## Update, uninstall and migration

1. Identify the actual installed source, version/digest and scope. Product version
   is currently unset; a host fallback is not a release. Review upstream changes,
   metadata, references and policy effects before adopting them.
2. Use the chosen host's documented update/reinstall mechanism. Catalog refresh,
   installed-payload update and new-session activation are distinct. See
   [activation/lifecycle matrix](../compatibility/activation-matrix.md) and
   [target protocols](../compatibility/live-owner-required-tests.md).
3. Preserve project-owned Memory, policy and human instructions. A managed block
   carries scope/revision and an actual version reference when known; current
   block revision is init-locator-1, not a product release version.
4. Update a managed block only in an authorized scope, after rereading current
   text and resolving concurrent edits. Avoid duplicate blocks and copying the
   whole Core into instructions each task. Preserve nested AGENTS.md, CLAUDE.md
   and Copilot path-specific boundaries.
5. For uninstall, remove the exact native candidate through its real install
   route. Session-only Claude loading ends when not supplied in a later session.
   Do not delete guessed cache directories, the whole instruction file or user
   Memory/policy. A requested project cleanup removes only the identified managed
   block; without such a request, report residual instructions.
6. Migration is an explicit scoped proposal when a real format/path/version
   change requires it. Preserve existing canonical Memory location and decision
   history; do not initialize a second store or regenerate all records. Missing
   or outdated Core must be reported before dependent Kiyo actions.

Only the bounded Codex uninstall preservation case is fully observed in P26.
Cross-target update, managed-block migration and new-session policy behavior
remain NOT_TESTED. No automatic migration or cleanup runtime exists.

## Release boundary

[Draft marketplace copy](../release/marketplace-copy.md) is review material only.
Obtain real owner decisions for identity/version/license/publisher/destination,
revalidate selected native requirements, and keep signature absence explicit.
Local acceptance is not curated approval. Critical unsafe behavior, secret
exposure or fabricated check results block release; missing required evidence
cannot be relabeled optional.

Prompt 28 release tooling, Prompt 29 gap audit and Prompt 30 final acceptance
are subsequent work, not implemented by this guide. No command here commits,
tags, pushes, submits or publishes. Keep [build state](../build/PROGRESS.md),
traceability and honest limitations current.
