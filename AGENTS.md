# Kiyo Axiom Framework — Agent instructions

This file is read by Codex and GitHub Copilot. `CLAUDE.md` imports it for Claude Code,
and `.github/copilot-instructions.md` points here. Keep this the single source of rules.

## Rule 1 — Every feature ships on all three platforms

Any feature, skill, workflow, template, rule or behaviour change **must be delivered for all
three ecosystems: Claude Code, Codex and GitHub Copilot**. Never ship for one and leave the
others for later. If a platform genuinely cannot support it, record that as an explicit,
documented exception (in `docs/compatibility/`) instead of silently skipping it.

Checklist before calling a feature done:

1. **Canonical content** goes in `src/kiyo/` (shared, platform-neutral). Do not write
   platform-specific copies of the same content.
2. **Platform overlays** — update each of `platforms/claude/`, `platforms/codex/`,
   `platforms/copilot/` (and `platforms/codex-ide/` if affected): plugin metadata,
   `resources/activation.md`, README, marketplace templates.
3. **New source files** — register them in `tools/packaging-inputs.json` (sorted, unique)
   so the builders include them.
4. **Regenerate `dist/`** with the `tools/package_*.py` builders. Never hand-edit `dist/`.
   The builders refuse to overwrite changed output or inventories, and the default
   `docs/evidence/*/package-inventory.json` files are historical, so pass a fresh
   `--inventory` path (and remove the stale `dist/<target>` first) — see
   `docs/developer/maintainer-guide.md`.
5. **Marketplace manifests** — keep `.claude-plugin/marketplace.json`,
   `.github/plugin/marketplace.json` and `.agents/plugins/marketplace.json` consistent.
6. **Docs** — update `README.md` **and** `README.th.md` together, plus the relevant
   `docs/compatibility/*` pages (activation matrix, native invocation map, package docs).
7. **Tests** — add or update tests under `tests/` for all three platforms
   (`tests/integration/{claude,codex,copilot}`, `tests/packaging`, `tests/static`), then run
   `python -m pytest tests` (this also runs the static-contract and packaging scripts via
   `tests/test_script_suites.py`). For behavior changes, rerun the paid live harness
   `tests/live/e2e/run.py` on the hosts you can access.

## Naming

- Product / plugin name: **`kiyo-axiom-framework`** (marketplace name is the same).
  Do not reintroduce `kiyo-codejadee`.
- The GitHub repo URL and `kiyo-axiom.codejadee.com` docs domain still contain `codejadee`;
  that is intentional until they are renamed.

## Other rules

- `docs/evidence/`, `dist/releases/` and `docs/build/` are historical records with recorded
  hashes — do not bulk-rewrite them.
- Do not commit or push unless explicitly asked.
- The whole suite is expected to pass. `test_08_recorded_product_inputs_preserved` checks that
  the P29 record still names real allowlisted inputs, not that product bytes are frozen.
- Release identity (`version`, `author`) must stay identical across the three platform
  manifests; the `RELEASE_IDENTITY_PARITY` static contract enforces it.
