---
name: review
description: Review existing human or AI changes without editing them. Inspect staged or unstaged diffs, specified files, a supplied commit range, or accessible PR context; report evidence-based defects, risks and suggestions with severity, confidence and limitations. Review alone does not authorize fixes or build/test execution.
---

# Review

Logical ID: **kiyo.review**. Canonical name: review. This logical ID is not
universal native invocation syntax; platform-only metadata belongs in overlays.

Read [KIYO.md](./references/kiyo/KIYO.md) and its bootstrap before workflow actions unless
already read and unchanged. Follow the [shared review procedure](./references/kiyo/workflows/review.md)
within the [read-only flow](./references/kiyo/workflows/read-only-flow.md).
Resolve references from this file's installed location, not a guessed checkout.
Missing required resources hold dependent conclusions; do not invent their content.

## Input and authority

Accept staged/unstaged changes, specified files, an explicit commit range, or PR
context available through actual authorized tools. Establish root, permitted
content and current state. Without a supplied range, inspect the current workspace
and explain staged, unstaged and relevant untracked coverage; never guess a
default branch or include unrelated history. No diff means report no changes,
not fabricated findings. Explicit file review can still inspect unchanged files.

This skill authorizes analysis and chat output only. Do not edit source, tests,
config or Memory; create report files by default; install packages; or commit,
push, stash, reset or otherwise clean up the workspace. Preserve all existing
human/AI edits; authorship does not change the evidence standard.

Do not automatically run build, test, formatter, scanner, project script or
application code: they can write artifacts, use network or affect data. Safe
non-mutating inspection is distinct from running project code. If execution is
needed, describe the proposed check and obtain missing execution scope or use
explicitly requested Test run after effect/target preflight. Reuse real matching
authorization; the Review selection alone adds none. Do not invent a native Test
command or continue execution under the read-only label.

## Procedure

1. Resolve the requested comparison and actual accessible files/revisions using
   the shared procedure. State excluded/unavailable scope; do not fetch a missing
   base or replace it with a guessed ref. Separate index, working-tree and
   supplied revision evidence, including deleted-file locations.
2. Read authorized relevant Memory through the
   [shared lifecycle](./references/kiyo/workflows/memory-lifecycle.md) in check mode. Verify
   material claims against inspected code/config/test source and accepted records.
   Missing/stale Memory is not implementation truth or permission to sync.
3. Inspect changed behavior and enough callers, guards, contracts and tests to
   establish impact. Use the ten dimensions in the shared procedure; load only
   applicable [engineering references](./references/kiyo/framework/engineering/index.md),
   [application security](./references/kiyo/agent-security/application-security.md) or
   [dependency guidance](./references/kiyo/governance/dependency-governance.md).
4. Validate each candidate against existing protections and sourced requirements.
   Classify Confirmed defect, Plausible risk or Improvement suggestion using the
   [severity/confidence guide](./references/kiyo/framework/review-severity-confidence.md).
   Cite an actual file/line or inspected range and state whether evidence is
   static, supplied or executed. Never invent a requirement, line or test result.
5. Return prioritized findings using the
   [finding template](./references/kiyo/templates/reports/review-finding.md) and the smallest
   suitable [review report](./references/kiyo/templates/reports/review-report.md).
   Include scope, governance/risk rationale, check evidence, limitations and
   Memory Impact. Redact sensitive content; a suggested fix is not an applied fix.
6. Close under the Review row of
   [Definition of Done](./references/kiyo/framework/definition-of-done.md). No findings means
   only none identified within the inspected scope. Tests not run stay NOT_RUN.
   DONE means the agreed review is delivered, not that defects are fixed, tests
   pass or the application is ready for production.

A required missing base, file or assessment prevents full completion; report
PARTIALLY COMPLETE, BLOCKED or DECISION REQUIRED as appropriate. A bounded review
can be DONE with findings and pending Memory corrections when the agreed
inspection is complete. Leave source, records and timestamps untouched.

## Claude native guidance

For Claude invocation or an authorized project bootstrap, read the conditional
[Claude activation reference](./references/claude/activation.md).
