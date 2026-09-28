# ADR-001 — One canonical static specification with contained skill resources

- Date: **2026-09-29** (Asia/Bangkok).
- Status: **ACCEPTED FOR BUILD DESIGN**, not product/live verification.
- Authority: user's Prompt 03 authorizes repository architecture and minimal
  scaffold under the [Build Contract](../../build/BUILD-CONTRACT.md). The chosen
  technical design is recorded by the implementing agent; no owner publication
  decision or independent review is implied.
- Scope: content ownership, progressive loading, resource packaging, state and
  identity boundaries. Implementation follows separately authorized prompts.

## Context

The repository has build/research/compatibility documents and an existing LICENSE,
but no product implementation or release version. Requirements call for static
native installation, eight skills and one specification with no consumer runtime.
Prompt 02 [activation research](../../compatibility/activation-modes.md) shows
metadata discovery is different from core loading, and resource conventions vary.
Its official-source checks are dated 2026-09-28, DOCUMENTED_ONLY, all targets
NOT_TESTED; Codex IDE native plugins are UNSUPPORTED and some native details
remain UNKNOWN. This design preserves those limitations.

## Decision

1. Author product content in `src/kiyo/`, with `KIYO.md`, `framework/`,
   `governance/`, `agent-security/`, `workflows/`, `profiles/`, `templates/` and
   exactly eight `skills/<name>/SKILL.md` entries. Stable Kiyo control IDs are
   independent of standards clause numbering.
2. Keep canonical frontmatter to name/description. Put justified host metadata
   in three ecosystem overlays, retaining six distinct target evidence records.
   Express access/approval contracts in Markdown, not unsupported native keys.
3. Have each skill read the compact bootstrap before workflow actions, then its
   shared procedure and relevant references. A small authorized native project
   adapter supplies persistent project context without copying the full core.
4. At developer build time, copy the complete shared Markdown subtree into each
   installed skill's `references/kiyo/`, preserving its structure and bytes.
   Rewrite entry reference paths and merge allowlisted overlay metadata. End
   users install the prepared static bundle without a generator/interpreter.
5. Keep mutable policy/memory in the consumer project, defaulting new projects
   to `.kiyo/policy.md` and `.kiyo/memory/`, preserving established paths. No
   user state, external symlink, checkout path or cache locator enters payloads.
6. Keep tools, tests, research and evidence developer-only; put derived bundles
   in `dist/`. Preserve existing identity/license/history and pending owner gates.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Hand-maintained host-specific core/skills | Creates competing specifications and silent parity drift |
| One shared plugin-root resource tree for all hosts | Smaller payload, but relies on inconsistent or untested cross-skill/root resolution contracts |
| Long rules copied into every authored SKILL.md | Loses single-definition maintenance and progressive loading |
| Symlink to checkout or dynamic runtime fetch/resolver | Breaks self-containment, cache portability and the no-runtime boundary |
| Copy complete core into native project instructions | Bloats initial context and creates stale user-project copies after update |
| Implement generator/core/eight placeholder skills now | Exceeds Prompt 03 and mistakes scaffold for features |

## Consequences and validation

Generated bundles contain repeated shared resource bytes, but those copies are
not editable authorities. Deterministic copy/parity/reference checks must prevent
drift. Initial file budgets and progressive selection keep instruction reads
bounded independently of installed size. This is advisory loading, not host
enforcement or guaranteed activation.

The unsupported IDE route remains an explicit gap, with no approved fallback.
Schema-specific outputs, relocation behavior, update scopes and six native
surfaces need later revalidation and live evidence. Project adapters survive
uninstall and need authorized maintenance; no background process manages them.

Detailed contracts: [layout](../framework-layout.md),
[loading](../content-loading.md), [packaging](../packaging-contract.md),
[identity/versioning](../naming-and-versioning.md). Changes to these boundaries
require a superseding ADR with reason and migration/verification impact;
do not erase this decision to match later implementation drift.
