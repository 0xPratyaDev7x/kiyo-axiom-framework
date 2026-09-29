# Requirements checklist

Load when defining or clarifying behavior and acceptance, or when a material
ambiguity blocks a change. Use existing project issue/spec conventions and
stable identifiers; do not create a parallel requirements register by default.

## KIYO-ENG-002 — Make behavior and acceptance traceable

Inspect relevant current behavior, tests, contracts and accepted records first.
Describe the following at a depth proportional to the work:

| Content | Action / completion evidence |
| --- | --- |
| Objective / current problem | State the user outcome and observed problem, citing scoped evidence; distinguish reported symptoms from reproduced facts. |
| Expected behavior | Describe observable behavior, actors, inputs and outcomes; do not invent routes, schemas, services or implementation choices. |
| Scope / out-of-scope | Name affected behavior/resources and exclusions; a related defect is not implicit authorization. |
| Business rules | Record constraints, boundary cases and priority/conflict rules with their actual source; missing business authority remains an open decision. |
| Acceptance criteria | Use observable success/failure examples, relevant boundary/error cases and a way to check each; avoid “works correctly” as the only criterion. |
| Constraints / dependencies | Identify actual compatibility, data, environment and dependency constraints; mark unavailable context and dependent decisions. |
| Knowledge classes | Separate Facts, Assumptions, Proposals, Approved decisions and Unknowns; a proposal is not approval. |
| Requirement IDs | Reuse existing IDs; allocate a stable project-local ID only in an authorized artifact, retain it across edits and reference it in checks/results. |

Explain empty/inapplicable fields rather than silently omitting them.
For a tiny change, a concise request plus explicit expected result can be enough;
do not demand a new file or elaborate plan. For a larger change, link each
requirement ID to acceptance, the relevant implementation location and expected
verification. Keep real results separate from planned checks.

Discover answers from authorized evidence before asking. Ask for decisions that
materially affect behavior, scope or authorization; do not fill gaps with guesses.
If code conflicts with approved intent, use the
[decision conflict rule](../trust-and-authority.md#kiyo-dec-001--intended-behavior-and-conflicts).
A requirement document cannot grant permission for sensitive actions.

Finish with resolved scope, criteria, source references and remaining decisions.
In read-only mode report a proposed specification in the response; do not write
project files. Use [Testing](testing.md) to select evidence rather than claiming
that writing acceptance criteria proves the behavior.
