# Kiyo Compass — Naming and versioning

Decision date: **2026-09-29**. Design under
[ADR-001](decisions/ADR-001-static-canonical-packages.md) and
[REQ-001/006/017/026/054/076/079/080](../build/REQUIREMENTS.md).
Repository observations and limits are in
[Prompt 03 baseline](../build/BASELINE.md#prompt-03-repository-observation).

## Preserve observed identity and history

Kiyo Compass remains a working name. Preserve the existing repository name,
root MIT LICENSE, requirement IDs, build history and research files. No product
version file, native manifest or Git tag was found in the inspected baseline;
this does not authorize inventing an initial release number, publisher or account.
No files are renamed to manufacture a new product history.

Internal directory slugs are `init`, `requirement`, `implement`, `review`, `test`,
`security`, `architecture`, `memory`; display labels remain the eight names in
the Build Contract. Canonical `name` matches its skill directory, and
`description` states intent and boundaries without host-specific commands.
These are internal authoring identities, not a reservation of marketplace names.
No extra public router/governance/audit/self-check skills are introduced.

Prompt 11 authors canonical name/directory init with the user-specified logical
ID **kiyo.init** in Markdown. That logical ID is not a native command or a new
frontmatter field; overlays later derive actual target metadata/selector names.
Prompt 12 adds name/directory requirement and logical ID **kiyo.requirement**
under the same boundary. Prompt 13 adds name/directory implement with logical ID
**kiyo.implement**. Prompt 14 adds name/directory review and logical ID
**kiyo.review**. Prompt 15 adds name/directory test and logical ID **kiyo.test**.
Prompt 16 adds name/directory security and logical ID **kiyo.security**.
Prompt 17 adds name/directory architecture and logical ID **kiyo.architecture**.
Prompt 18 adds name/directory memory and logical ID **kiyo.memory**.
All eight canonical entries are authored; no extra router/governance/self-check
entry exists. Native catalogs and per-target acceptance remain pending.
assess/run/write and Security application/skills/governance/self-check are logical
submodes under their existing public skills, not universal native command arguments.
Memory show/check/sync/repair likewise describe logical effects, not native permissions.

Native plugin IDs and host-added prefixes belong to overlays. Use the actual
discovered identity when invoking a host; do not prepend a universal `kiyo-`
or bake `plugin:skill` into canonical names. The
[invocation map](../compatibility/native-invocation-map.md), checked 2026-09-28,
remains DOCUMENTED_ONLY and retains the unknown CLI qualification details and
unsupported Codex IDE plugin route. Revalidate before implementing aliases.

## Stable controls independent of standards

Core control IDs use `KIYO-<DOMAIN>-<NNN>`, with uppercase domain and a stable
three-digit number, for example **KIYO-FACT-001**. Prompt 04 introduces the initial
16-control vocabulary and canonical definitions through
[control-index](../../src/kiyo/framework/control-index.md). ACTIVE means authored
instruction, not behavioral verification; the original design example is now
the evidence/knowledge-class control. Prompt 05 adds KIYO-MEM-002 through
KIYO-MEM-007 without renumbering the original controls. Prompt 06 adds nine
governance controls. Prompt 07 adds KIYO-SEC-001 through KIYO-SEC-010;
Prompt 08 adds KIYO-ROUTE-001 and KIYO-FLOW-001 through KIYO-FLOW-005;
Prompt 09 adds KIYO-ENG-002 through KIYO-ENG-007 and KIYO-PROF-001;
Prompt 10 adds KIYO-VERIFY-001/002, KIYO-DONE-001 and KIYO-REPORT-001;
Prompt 11 adds KIYO-INIT-001 for bounded, repeatable initialization;
Prompt 12 adds KIYO-REQ-001 for evidenced requirements and bounded delivery;
Prompt 13 adds KIYO-IMPL-001 for intent, baseline and checked engineering scope;
Prompt 14 adds KIYO-REVIEW-001 for bounded evidence-based read-only review;
Prompt 15 adds KIYO-TEST-001 for separate test effects and observed results;
Prompt 16 adds KIYO-SEC-011 for bounded Security submodes and assurance;
Prompt 17 adds KIYO-ARCH-001 for evidence-scoped architecture and approved intent;
Prompt 18 adds KIYO-MEM-008 for explicit Memory modes and preserved history;
Prompt 19 adds KIYO-CONFIG-001 and KIYO-POLICY-001 for static project configuration
and sourced policy resolution, bringing the index to 68 IDs. AST taxonomy labels remain external mapping IDs,
not Kiyo control numbers or ASI identifiers. G1–G4 are advisory Kiyo modes,
not standards identifiers or native permission settings.

Each registered control records its title, normative Markdown location, related
REQ IDs, status and replacement/deprecation link when relevant. One ID has one
canonical definition. Skills cite IDs and shared files; overlays do not redefine
them. Do not renumber after moving a file, reuse retired IDs or change an ID's
meaning silently. Add a new ID for a different obligation and retain a migration
record for the old one. Correcting prose without changing meaning keeps the ID.

ISO/NIST/OWASP research is recorded in developer documentation. Prompt 09 adds an
optional packaged [concept mapping](../../src/kiyo/framework/engineering/standards-mapping.md)
for engineering rationale; neither mapping is a control-number namespace, runtime
dependency or claimed certification.
Use the [standards baseline](../research/standards-baseline.md), original source check
2026-09-28 and scoped Prompt 07/09 refreshes, with their edition, draft and lawful-public-metadata limits. Do not
invent clause numbers or copy protected standards text. Supporting references
and the conditional ISO 5338 scope remain as recorded there.

## One release identity, derived native metadata

When release work is authorized, first inspect existing version history again.
If a version already exists, preserve that established convention. If still
absent, obtain the owner's initial release identity/number instead of assuming
`0.1.0`, `1.0.0` or a date-based version. No VERSION file is needed now.

The selected policy for a future new numeric version stream is major/minor/patch:
major for incompatible public skill/contract or project-state changes; minor for
compatible capabilities; patch for compatible corrections. This is a Kiyo design
policy, not evidence of an existing release or a promise about native host caches.
Native restrictions must be revalidated before final version representation.

One approved release value is an input to developer packaging. Derive every
native version field and release inventory from it; do not edit three separate
versions by hand. Bind the value to the exact canonical/overlay revision and
actual digests. Rebuilding identical inputs should produce identical artifacts;
the two-build proof belongs to later packaging checks, not this architecture.
Changing shipped canonical content or native metadata requires a new recorded
release identity. Do not reuse the same release label for different bytes.

Project adapter revisions track the small adapter's format independently from
the product release it was last reviewed against. They are provenance text in
user-owned project files, not a second product release line. Prompt 11's neutral managed-block shape uses internal adapter text revision
init-locator-1, not a product/host release number; preserve any actual established
adapter history instead of forcing this format. Missing product version
information stays UNKNOWN; no automatic updater, forced policy migration or
memory migration is introduced.

## Maintenance and publication gates

Use native install/update/uninstall at the observed host scope. Catalog refresh
and installed-bundle update are distinct where the native documentation says so;
do not substitute one for the other. Never hardcode cache versions/locations.
Installed resources are immutable; user memory and policy retain their established
project-local paths across version changes and uninstall. Review adapter drift
only when requested, as defined in [content-loading](content-loading.md).

The following remain unresolved in [DECISIONS](../build/DECISIONS.md): final
publication name/identifiers (DEC-001), intended publication license (DEC-002),
publisher/namespace/destination (DEC-003), and whether any alternative for the
unsupported Codex IDE plugin route is accepted (DEC-004). Marketplace availability,
curated listing, signatures, account authority and publication approvals need
actual evidence. None is inferred from a local folder, copyright name or
custom-source install. These gates do not prevent Prompt 04 Core authoring.
