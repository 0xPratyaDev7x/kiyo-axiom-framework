# Kiyo Compass — Content loading contract

Decision date: **2026-09-29**. Architecture, not observed execution. Inputs:
[ADR-001](decisions/ADR-001-static-canonical-packages.md), REQ-009–017/025–028/054
in [REQUIREMENTS](../build/REQUIREMENTS.md), and Prompt 02
[activation modes](../compatibility/activation-modes.md) / [invocation map](../compatibility/native-invocation-map.md).
Original native source checks are **2026-09-28, DOCUMENTED_ONLY**. Claude-only
Prompt 20 revalidation is **2026-09-29**, with [current limits](../compatibility/claude-package.md);
all six live loading results remain NOT_TESTED.

## Ordered instruction use

The logical workflow order is **bootstrap → selected skill procedure → relevant
references**. Host metadata discovery precedes this. A host may read the selected
SKILL.md before it can follow that file's bootstrap instruction; Kiyo cannot
change that native loading order with static Markdown.

```text
Host discovers name/description → user selection or host relevance matching
  → SKILL.md entry: read packaged KIYO.md before taking workflow actions
    → compact bootstrap: authority, scope, project-context pointers, loading budget
      → selected skill's mode and shared workflow
        → relevant core/policies/profile → selected template → authorized project output
```

Each authored skill has a short bootstrap reference and a short entry contract.
The long rules live once in shared Markdown. An already-read unchanged bootstrap
need not be reread repeatedly in the same task; after context loss or a changed
bundle identity, re-establish it rather than assuming retained context. A skill
cannot claim the bootstrap was read solely because the plugin was installed.

The bootstrap does not recursively read every file it links. It identifies the
baseline rules necessary to establish authority, honest evidence, scope and
safe context reads, then directs the selected task to the relevant procedure.
Memory First means consulting the established index/relevant memory within
permissions and checking material facts against current project evidence. It
does not mean loading every memory file or trusting poisoned/stale instructions.

Kiyo provides read instructions to the agent. Markdown links are locators, not
executable imports or an implicit native include guarantee. A denied/missing
reference is reported with its path and affected scope; stop dependent actions
or provide explicitly limited guidance. Never fetch a replacement core from the
network, guess omitted rules or run a generator to repair a consumer install.

## Context budget selected for authoring

These are **Kiyo design ceilings**, not native host limits or token measurements.
Prompt 04 adds line budgets and counts the complete mandatory bootstrap chain;
see [ADR-002](decisions/ADR-002-core-loading-budgets.md). Physical lines include
blanks/headings/frontmatter; words are whitespace-delimited.

| Layer | Budget and selection rule | Verification planned |
| --- | --- | --- |
| Project adapter | At most 250 whitespace-delimited words per Kiyo-owned block | Static count after rendering, excluding existing human instructions |
| Product bootstrap | `KIYO.md` plus mandatory `framework/bootstrap.md`, combined at most 120 lines and 600 words | Static count plus manual assessment of completeness; no hidden mandatory includes |
| Selected SKILL.md | At most 250 lines and 1,200 words including native frontmatter, entry and contract | Static count after rendering; move long reusable content to relevant references |
| Task references | Read named applicable sections only; record inspected scope and material omissions | Behavioral trace of actual reads; no claim that a fixed word count measures model tokens |

Do not evade these ceilings by hiding required initial text in an unbounded include.
If content exceeds a ceiling, split genuinely conditional references or record
the reason, measured size, impact and scoped exception in an ADR. No current
exception is authorized. The actual Core protocol is
[context-loading](../../src/kiyo/framework/context-loading.md).
Near a host context limit, produce the authorized handoff with task intent, known
facts, unresolved decisions, inspected paths, actual check results and next step.
Host truncation and model tokenization require later target tests.

## Activation modes and native project adapters

| Target | Project instruction adapter candidate from Prompt 02 | Architecture disposition / limitation |
| --- | --- | --- |
| Claude Code CLI | Existing `CLAUDE.md` or `.claude/CLAUDE.md` | Add a scoped project-relative locator only through authorized Init; plugin-root CLAUDE.md is not a core loader (C03/C07) |
| Claude Code VS Code | Same Claude project mechanism | Separate extension loading test; CLI behavior is not evidence (C05/C03/C07) |
| Codex CLI | Applicable `AGENTS.md` / `AGENTS.override.md` | Preserve actual instruction chain and its documented context cap; use explicit read text, not presumed link expansion (O03) |
| Codex IDE Extension | Native project guidance exists separately | Native plugin route remains UNSUPPORTED; no fallback package promised or generated (O03/O04/O05; DEC-004) |
| Copilot CLI | Applicable `.github/copilot-instructions.md` or `AGENTS.md` | Do not include cache paths through repository-restricted `@` includes; retain native precedence uncertainty (G04) |
| Copilot VS Code | Applicable `.github/copilot-instructions.md` or `AGENTS.md` | Respect selected harness/settings and test independently; do not assert always-on plugin rules (V03/V01) |

Source IDs resolve through [SOURCES](../research/SOURCES.md), checked 2026-09-28;
these rows are DOCUMENTED_ONLY design inputs, not an implementation or fresh
native API contract. Revalidate fields/commands when implementing overlays.

An explicit native invocation can select an installed skill without a project
bootstrap. Implicit selection can also use metadata without Init; it remains
model/configuration-dependent. Project-wide guidance uses an authorized native
project block or an already-authorized user/organization equivalent. None of
these establishes guaranteed automatic activation or compliance.

The project block contains only the Kiyo working identity, its adapter revision,
advisory nature, established project-relative state locators, and guidance to
select the appropriate **actually discovered** native skill. It does not copy
the core or hardcode a cache path. It must say what to do when Kiyo is unavailable:
report the unavailable skill, preserve project policy/memory and avoid claiming
a Kiyo workflow ran. Exact invocation presentation follows the native target;
unresolved plugin-qualified CLI spelling is not filled in from another host.

Init proposes the concrete insertion into an existing native file and preserves
unrelated instructions. The instruction to read project policy is ordinary
agent guidance unless that host's documented include behavior is deliberately
used and separately tested. No ninth bootstrap skill or runtime loader exists.

## Adapter ownership and lifecycle

An eventual project block uses identifiable begin/end comments and records
`adapter revision`, `last reviewed product version` (UNKNOWN if not established),
and `project state locations`. These are plain Markdown provenance labels, not
native permission or manifest keys. Project users own the resulting file.

Re-running Init compares the proposed block with current content before writing.
Human-modified blocks are preserved and reconciled with the user when necessary;
there is no automatic overwrite or background sync. Updating the plugin does
not update project files. A requested Init/Memory maintenance pass can report a
stale block and propose an authorized scoped change. It cannot claim continuous
drift detection or infer missing version information.

Uninstall leaves project policy/memory and the adapter intact. A separately
authorized project edit may remove only the identified Kiyo block after review;
it never deletes the containing native instruction file or user state. This is
manual agent work under host permissions, not an uninstall hook.

## Checks required later

Static checks must count budgets, resolve payload references and keep native
schema fields separate from advisory contracts. Behavioral scenarios must inspect
bootstrap-before-actions, irrelevant-reference avoidance, read-only modes,
missing/poisoned memory, unavailable skills and preserved human edits. Each of
the six live rows needs its own explicit/implicit/no-bootstrap/bootstrap,
relocation/update/uninstall evidence and observed environment. These are planned
checks; Prompt 03 checks only the architecture documents.

## Prompt 20 Claude adapter

The generated entry's conditional [Claude reference](../../platforms/claude/resources/activation.md)
uses the existing canonical Init managed-block shape plus a native selection
sentence. It is packaged inside every skill and does not copy a second Core.
A static sample block measured 114 words; rendering must still count actual
project locators/text. No project CLAUDE.md was created in this build.

Root/.claude CLAUDE.md and newer AGENTS selection are documented facilities with
version/context limits, not universal automatic Core loading. Preserve existing
instruction choice and human sections. Live selection/loading, authorized Init
behavior and update/uninstall preservation remain Prompt 26 tests, separately
for terminal and extension. Offline resource containment is not that evidence.
