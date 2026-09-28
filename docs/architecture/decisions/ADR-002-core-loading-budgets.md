# ADR-002 — Bound the complete mandatory Core bootstrap

- Date: **2026-09-29** (Asia/Bangkok).
- Status: **ACCEPTED FOR BUILD DESIGN** under the user's Prompt 04 instructions.
- Scope: refines the loading-budget portion of
  [ADR-001](ADR-001-static-canonical-packages.md); all other boundaries remain.
- No owner release approval, vendor limit or tested activation is implied.

## Context and decision

Prompt 03 selected a 600-word KIYO.md budget, 1,200-word SKILL.md budget and
250-word project-adapter budget. Prompt 04 explicitly requests a short bootstrap,
shared bootstrap.md and initial ceilings of 120 bootstrap lines / 250 skill lines.

Keep both metrics: **KIYO.md plus framework/bootstrap.md combined must fit 120
physical lines and 600 whitespace-delimited words**. Selected SKILL.md must fit
250 lines and 1,200 words, including rendered native frontmatter. The project
adapter retains its 250-word ceiling. Blank lines/headings count as lines.
No token equivalence or host limit is claimed.

The entry reads the short shared baseline before workflow actions. Other Core
files are conditionally consulted references, not unbounded mandatory includes.
The control index provides stable canonical locators; examples are expected
responses rather than test results. If a ceiling is exceeded, split genuinely
conditional material or document the measured size, reason, impact and scoped
exception before accepting it. No exception is granted by this ADR.

## Consequences and validation

This closes the possibility of apparently meeting the entry budget while hiding
the same mandatory text in another file. Static counts check authored/rendered
files; behavioral and target tests must separately inspect actual context reads.
No skills exist yet, so the skill ceiling is a contract with NOT_RUN measurement,
not a vacuously passing eight-skill check.

Product protocol: [Core context loading](../../../src/kiyo/framework/context-loading.md).
Developer contract: [content loading](../content-loading.md).
Actual counts/checks: [Prompt 04 evidence](../../build/BASELINE.md#prompt-04-checks).
