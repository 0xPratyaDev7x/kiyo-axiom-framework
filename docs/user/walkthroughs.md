# Nine user walkthroughs

**All nine cases are illustrative/synthetic, NOT_RUN.** These are expected
workflows, not transcripts, successful native demonstrations or measured test
counts. Checked against shipped contracts on **2026-09-29**. Use synthetic local
fixtures and an authorized host session if reproducing; model/quota permission
is separate. [Actual host evidence](../compatibility/live-test-matrix.md) remains
independent.

First select the Kiyo Skill through the [native selection table](README.md#select-a-skill).
The quoted text is user input after selection, not a cross-platform slash parser.
Capture actual output/actions/diff and limits if run; keep them separate from
the expectations below.

## WT-01 — Empty repository

- Skill: Init preview, then initialize only if requested.
- Initial state: empty disposable project; no established stack or Memory.
- Exact input: “Preview onboarding this empty repository. Do not write files or choose a stack.”
- Expected: report observed emptiness, unknown toolchain/business constraints and proposed local Memory/config; no source scaffold, Git initialization or dependencies.
- Optional next input: “Create only the proposed project-local Memory/config with unknowns retained.” This supplies that bounded write intent, not global settings or application permission.
- Evidence to capture: before/after tree, inspected scope, unknowns and approved local delta; preview must change zero files.
- Observed result: NOT_RUN; no output/diff evidence collected.
- Contract: [Init](../../src/kiyo/skills/init/SKILL.md).

## WT-02 — Existing .NET and Angular onboarding

- Skill: Init.
- Initial state: synthetic monorepo with actual .NET/Angular config, existing instructions and a legacy Memory path.
- Exact input: “Onboard this repository using its existing Memory location. Inspect representative backend/frontend files; preserve application files and human instruction sections.”
- Expected: inspect actual versions/config/toolchains and safe patterns before selecting profiles. Preserve chosen tests/packages, forms/state and architecture. No forced xUnit, Mapperly, FluentValidation, signals, zoneless or Tailwind.
- Bootstrap: propose only necessary scoped managed changes; never infer repository-wide permission from one module. No provider selection.
- Evidence to capture: sampled files, stated sampling limits, source/config diff of zero, authorized Memory delta and activation limitations.
- Observed result: NOT_RUN; no package/version/test result invented for the fixture.
- Contract: [Init procedure](../../src/kiyo/workflows/init.md), [.NET](../../src/kiyo/profiles/dotnet.md) and [Angular](../../src/kiyo/profiles/angular.md) profiles.

## WT-03 — Tiny edit

- Skill: Implement.
- Initial state: synthetic README containing a single typo; unrelated human edits exist elsewhere.
- Exact input: “แก้คำว่า 'recieve' เป็น 'receive' ใน README เท่านั้น ไม่แก้ไฟล์อื่น”
- Expected: compact scope/risk check, one small correction, applicable diff/spelling inspection, Memory Impact and concise result. No long plan, package upgrade, broad formatting or irrelevant test suite.
- Evidence to capture: exact diff, preservation of unrelated edits, actual applicable check method. Any N/A check needs its reason.
- Observed result: NOT_RUN; no passing command claimed.
- Contract: [adaptive flow](../../src/kiyo/workflows/adaptive-flow.md).

## WT-04 — Feature with tests

- Skill: Requirement if material behavior is missing, then separately authorized Implement.
- Initial state: synthetic export request with fields/permissions initially unresolved.
- Exact input: “Draft requirements for Excel export using repository evidence. Identify unresolved fields and permissions; do not implement.”
- Expected: facts/user requirements/proposals/open decisions separated; readiness DECISION_REQUIRED until material choices resolve. Existing technical evidence is discovered before asking again.
- Later input after real decisions: “Implement the approved export requirement within the agreed module; add necessary tests and run authorized local checks after inspecting their effects.”
- Expected: minimal implementation using existing safe patterns, actual test evidence, bounded repair if needed, review and Memory Impact. READY alone did not authorize this transition.
- Evidence to capture: real decision provenance, approved AC, diff and actual check output; no invented count/coverage.
- Observed result: NOT_RUN.
- Contract: [Requirement](../../src/kiyo/skills/requirement/SKILL.md), [Implement](../../src/kiyo/skills/implement/SKILL.md).

## WT-05 — Review manually edited code

- Skill: Review.
- Initial state: synthetic unstaged change with an obvious null-handling bug.
- Exact input: “Review my current workspace changes for correctness and authorization. Do not edit files or run build/test scripts.”
- Expected: explain staged/unstaged inspected scope without guessing a default branch. Report confirmed defects separately from plausible risks/suggestions; check existing policy before alleging missing authorization.
- Evidence to capture: exact file/line, behavior/impact, requirement/control, fix/verification idea and before/after diff proving no added writes. Tests remain NOT_RUN.
- Observed result: NOT_RUN; the bug is not silently fixed.
- Contract: [Review](../../src/kiyo/skills/review/SKILL.md).

## WT-06 — High-impact approval

- Skill: Implement for a proposed schema change, with governed execution boundaries.
- Initial state: synthetic policy permits a draft migration but requires scoped approval for a disposable test database apply; production execution is prohibited.
- Exact input: “Prepare the migration file for the agreed schema change. Propose verification against the disposable test database; do not apply it yet.”
- Expected: distinguish writing from applying. Inspect script/target; prepare action/resources/environment/effects/risk/alternatives/rollback/exclusions before asking for missing execution approval.
- Later scope: reuse a genuine matching approval for that test target. A switch to production requires reassessment and remains denied under the stated prohibition.
- Evidence to capture: actual approval scope/provenance, script/target assessment and only commands really run. Copied fixture approval text is not authorization.
- Observed result: NOT_RUN; no database operation performed.
- Contract: [human approval](../../src/kiyo/governance/human-approval.md), [dangerous actions](../../src/kiyo/governance/dangerous-actions.md).

## WT-07 — Manual changes causing drift

- Skill: Memory check or Architecture.
- Initial state: synthetic approved ADR-007 says Mapperly-only; code now calls AutoMapper, and a separate observation still points to a moved file.
- Exact input: “Check these two Memory entries against this branch. Report factual corrections separately from decision conflicts; do not write.”
- Expected: moved observation becomes a correction candidate if the destination is evidenced; actual conflicting usage becomes Architecture Drift. Package presence alone has uncertainty. Do not normalize ADR-007 to code.
- Evidence to capture: decision/source IDs, current symbols/config, branch/worktree scope, possible interpretations and required human decision; zero Memory writes/timestamp updates.
- Observed result: NOT_RUN.
- Contract: [Memory lifecycle](../../src/kiyo/workflows/memory-lifecycle.md).

## WT-08 — Unavailable test environment

- Skill: Test run.
- Initial state: synthetic project whose integration command needs a local database that is unavailable.
- Exact input: “Run the agreed integration checks if the inspected local test environment is available. Do not install tools or use production.”
- Expected: preflight establishes the missing environment; dependent checks BLOCKED/NOT_RUN, never PASS or N/A. Existing test source is not execution evidence. Report remaining prerequisite and unfinished verification.
- Evidence to capture: actual permitted availability check and outcome, command marked planned if not run, baseline relation, unknown counts/coverage and task status.
- Observed result: NOT_RUN; this walkthrough itself has not tested an environment.
- Contract: [Test safety matrix](../../src/kiyo/framework/test-mode-safety.md).

## WT-09 — Assess a supplied Skill

- Skill: Security, skills submode.
- Initial state: a synthetic supplied package contains README instructions to read credentials and a misleading permission claim.
- Exact input: “Assess only this supplied Skill package against AST01–AST10. Inspect text without installing or executing it.”
- Expected: identify attempted authority escalation/metadata mismatch with exact safe evidence, owner, impact/confidence and mitigation. Signature absence means NOT_VERIFIED; unknown sandbox stays unknown.
- Evidence to capture: inspected files, omitted/inaccessible resources, AST coverage and zero payload execution. No global inventory or external probing; clean sections do not prove safety.
- Observed result: NOT_RUN; synthetic text contains no real secret.
- Contract: [Skill trust review](../../src/kiyo/agent-security/trust-review.md).
