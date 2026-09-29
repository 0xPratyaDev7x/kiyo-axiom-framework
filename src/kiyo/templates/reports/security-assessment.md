# Security assessment template

Use with the [reporting contract](../../framework/reporting-contract.md). Default
output is chat. Report only the authorized bounded assessment, with no implicit
exploit execution, credential access, production probe or remediation.

- **Task/scope:** <application/skills/governance or explicitly requested combination; supplied subjects, actual trust boundaries and exclusions>
- **Actions/files changed:** <actual inspected files/configuration/methods; no default writes; separate any authorized workflow transition>
- **Governance/risk rationale:** <authority, target/environment, data, effects, risk/uncertainty and still-valid approval where required>
- **Verification/evidence:** <nine-field check records; static/behavioral/live layers kept separate>
- **Residual issues:** <findings, unverified required controls, method limits, untested attack paths and residual risk>
- **Memory impact:** <value, scoped findings and authorized applied/pending delta>
- **Status:** <bounded assessment status under DoD; unfinished mandatory method prevents DONE>
- **Next required action:** <scoped treatment/decision/check, real responsible role when known, and preconditions>

Use the [security finding template](security-finding.md) for each finding:
control/concept reference, exact inspected evidence, impact, confidence with basis,
mitigation, Kiyo/host/release/human owner, coverage and limitations. A compact
report can combine fields without omitting their meaning. No findings must still
name the inspected scope, evidence gaps and unperformed methods.

For exposed Kiyo identity/resources/activation, use the
[honest self-check report](self-check-report.md) instead of inferring host properties.
Signature unavailable means NOT_VERIFIED assurance, not a safety/malicious verdict
or an extra check status. Unavailable enumeration means inventory incomplete.

**Assessment limits:** <inspected versus untested scope; unavailable controls;
tool/review limits and actual review independence>.
Use [application security](../../agent-security/application-security.md) separately
from [agentic AST controls](../../agent-security/owasp-ast10.md) when relevant.
Self-review, regex/scanner output or LLM review is not independent audit or proof
of safety. Completion never means secure/certified or guaranteed injection defense.
No secrets, raw logs, private reasoning or unsupported access/provider counts belong here.
