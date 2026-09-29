# Coding checklist

Load the affected rows for code implementation or review. Apply the discovered
language/version, project conventions and accepted policy; no preset installs
libraries or authorizes a refactor.

## KIYO-ENG-004 — Keep changed code clear, bounded and safe

| Concern | Action | Expected evidence |
| --- | --- | --- |
| Readability / naming / cohesion | Follow meaningful local naming; keep one understandable responsibility and explicit behavior. Use comments for intent that code cannot convey. | Focused diff and a nearby safe convention, or a justified local departure. |
| Validation / nulls | Validate at relevant trust boundaries and preserve domain invariants. Handle missing/invalid values using the project's actual type/null conventions. | Boundary and invalid-input cases; no invented business rule or redundant validation framework. |
| Errors | Preserve error contracts and useful failure context; handle expected failures without swallowing defects or catching everything as success. | Error-path checks and compatibility evidence. |
| Sensitive logging | Minimize logged data; avoid credentials, tokens, sensitive payloads and unnecessary PII. Inspect changed log arguments and error output. | Redacted/synthetic diagnostic example and relevant data classification, not copied secrets. |
| Duplication / complexity | Reuse a safe local helper when it fits. Prefer a simple local change over speculative abstraction; consolidate only the duplication relevant to this task. | Justified scope and readable paths, not an arbitrary complexity score alone. |
| Dependencies | Use existing suitable capabilities. Explain need, alternatives, compatibility and side effects before an addition or upgrade. | Actual manifest/lock diff and proportionate provenance/verification evidence when authorized. |

Inspect existing patterns critically: unsafe string-built SQL, broad exception
suppression or sensitive logs must be flagged rather than copied. Distinguish a
necessary local correction from deferred unrelated findings. A tiny typo does
not justify package upgrades, formatter churn or a library replacement.

Use [dependency governance](../../governance/dependency-governance.md) for
dependency changes, [data handling](../../governance/data-handling.md) for
sensitive content and the relevant [application security checklist](../../agent-security/application-security.md)
for affected validation, auth, injection or other security boundaries.
No static/LLM review proves the absence of vulnerabilities.

Complete with scoped change/review findings, relevant actual checks and remaining
limitations. A Review task reports suggestions without editing code. Follow
[Testing](testing.md) and [Change scope](change-scope.md) as applicable.
