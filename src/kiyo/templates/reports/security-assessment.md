# Security assessment template

Use with the [reporting contract](../../framework/reporting-contract.md). Default
output is chat. Report only the authorized bounded assessment, with no implicit
exploit execution, credential access, production probe or remediation.

- **Task/scope:** <application security, agentic skill security or both; actual components/trust boundaries, mode and exclusions>
- **Actions/files changed:** <actual inspected files/configuration/methods and authorized changes, if any>
- **Governance/risk rationale:** <authority, target/environment, data, effects, risk/uncertainty and still-valid approval where required>
- **Verification/evidence:** <nine-field check records; static/behavioral/live layers kept separate>
- **Residual issues:** <findings, unverified required controls, method limits, untested attack paths and residual risk>
- **Memory impact:** <value, scoped findings and authorized applied/pending delta>
- **Status:** <bounded assessment status under DoD; unfinished mandatory method prevents DONE>
- **Next required action:** <scoped treatment/decision/check, real responsible role when known, and preconditions>

| Finding / boundary | Observation and safe evidence | Impact / uncertainty | Control owner and proposed next action |
| --- | --- | --- | --- |
| <actual finding, or explicit bounded no-findings statement> | <sanitized evidence/reference> | <supported consequence and gaps> | <Kiyo guidance / host security / developer release / human organization as applicable> |

**Assessment limits:** <inspected versus untested scope; unavailable controls;
tool/review limits and actual review independence>.
Use [application security](../../agent-security/application-security.md) separately
from [agentic AST controls](../../agent-security/owasp-ast10.md) when relevant.
Self-review, regex/scanner output or LLM review is not independent audit or proof
of safety. Completion never means secure/certified or guaranteed injection defense.
No secrets, raw logs, private reasoning or unsupported access/provider counts belong here.
