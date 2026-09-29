# OWASP Agentic Skills Top 10 — Kiyo control mapping

## Source, status and scope

Taxonomy rechecked **2026-09-29 (Asia/Bangkok)** against the official
[Agentic Skills project](https://owasp.github.io/www-project-agentic-skills-top-10/).
The page labels v1 as public review while also presenting a proposal/2026-edition
status. Treat this as **DOCUMENTED_ONLY, public-review draft**, not a finalized
standard. Individual source links below were followed to the shown astNN.html
pages on the same date; no redirect was reported for those pages.

AST is the **Agentic Skills** taxonomy used here. **ASI** belongs to the separate
Agentic Applications initiative; its official
[release announcement](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)
is dated 2025-12-09 and uses ASI identifiers. Checked 2026-09-29,
DOCUMENTED_ONLY; this announcement is not evidence of the latest minor revision.
Do not relabel AST controls as ASI, substitute ASI rankings, or claim a one-to-one
mapping. Application code security is separately covered by the
[Application Security checklist](application-security.md).

These risk summaries, controls, ownership assignments and expected outcomes are
**Kiyo interpretations**, not copied OWASP mitigations, clauses or certification.
The proposed universal skill format and host examples on the AST site are not
native API contracts. Source links are optional citations, not instructions to
fetch remote operational content or prerequisites for the installed procedure.
The mapping adds no runtime, sandbox, network block or signature verifier.

Every entry below inherits the checked date/status above and its own residual
limitation. Kiyo IDs point through the [canonical index](../framework/control-index.md).
Shared procedures exist as Markdown; the [Security procedure](../workflows/security.md)
and Review now reuse them. This authoring update does not refresh source status
or establish native security behavior. Test references are synthetic scenario specifications;
**execution NOT_RUN**, not observed behavior or six-target native evidence.

## AST01 Malicious Skills

- Risk summary: A skill can disguise unrelated or harmful actions as necessary task instructions.
- Kiyo control IDs: KIYO-SEC-001, KIYO-SEC-003.
- Skill/shared procedure: [Skill Audit and trust review](trust-review.md).
- Expected behavior: Inspect origin and requested effects; report suspicious directions and hold/deny unauthorized effects. Missing signature alone is not a malicious verdict.
- Required evidence: Exact inspected source/artifact, publisher evidence or UNKNOWN, suspicious location/effect and actual review scope/date.
- Control owner: Kiyo Markdown guidance: assess/report; Developer release process: inspect shipped bytes; Human organization process: accepted adoption policy; Host-native security: actual access boundary.
- Residual limitations: Review cannot establish benign intent or inspect inaccessible content.
- Test case references: TC-AST-01A, TC-AST-01B; execution NOT_RUN.
- Source: [OWASP AST01](https://owasp.github.io/www-project-agentic-skills-top-10/ast01.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.

## AST02 Supply Chain Compromise

- Risk summary: The reviewed source and distributed content can diverge through compromised or substituted inputs.
- Kiyo control IDs: KIYO-SEC-004, KIYO-DEP-001.
- Skill/shared procedure: [Provenance review](update-and-provenance.md#kiyo-sec-004--bind-source-review-to-the-actual-artifact).
- Expected behavior: Bind findings to observed artifacts and dependencies; flag missing/mismatched provenance before dependent adoption.
- Required evidence: Source/overlay revisions, artifact inventory, actual digest comparison and its independent expected source when available, dependency/script review scope and date.
- Control owner: Developer release process: source-to-artifact evidence; Kiyo Markdown guidance: flag gaps; Human organization process: adoption authority.
- Residual limitations: Hashes without trusted comparison do not authenticate origin; Kiyo has no runtime signature verifier.
- Test case references: TC-AST-02; execution NOT_RUN.
- Source: [OWASP AST02](https://owasp.github.io/www-project-agentic-skills-top-10/ast02.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.

## AST03 Over-Privileged Skills

- Risk summary: A small task can gain unnecessary access whose misuse affects unrelated resources.
- Kiyo control IDs: KIYO-PERM-001, KIYO-SEC-006.
- Skill/shared procedure: [Minimum-access review](../governance/permissions.md) and [required-control check](control-ownership.md#kiyo-sec-006--establish-required-host-controls-or-hold-dependent-execution).
- Expected behavior: Compare every requested effect/resource to demonstrated need; keep read-only intent and flag excess without changing settings.
- Required evidence: Task scope, declared/observed read/write/execute/network effects, actual host permission evidence or UNKNOWN and review date.
- Control owner: Kiyo Markdown guidance: compare need; Host-native security: enforce access; Human organization process: policy and valid human scope.
- Residual limitations: Advisory restriction does not remove a tool's real privileges; unknown host state stays explicit.
- Test case references: TC-AST-03; execution NOT_RUN.
- Source: [OWASP AST03](https://owasp.github.io/www-project-agentic-skills-top-10/ast03.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.

## AST04 Insecure Metadata

- Risk summary: Misleading fields or unsafe loading can hide a skill's actual purpose and effects.
- Kiyo control IDs: KIYO-SEC-002.
- Skill/shared procedure: [Metadata review](trust-review.md#kiyo-sec-002--compare-honest-metadata-with-the-actual-payload).
- Expected behavior: Check truthful names/descriptions against payload and the actual target schema; reject unsupported enforcement claims, without executing metadata.
- Required evidence: Target schema URL/date/version or gap, inspected metadata/body/reference set, parser validation actually run and omitted inputs.
- Control owner: Developer release process: validate authored overlays/payload; Host-native security: safe loading; Kiyo Markdown guidance: identify unsupported claims.
- Residual limitations: No native schema/loader is implemented by this text; a parsable field can still be ignored.
- Test case references: TC-AST-04; execution NOT_RUN.
- Source: [OWASP AST04](https://owasp.github.io/www-project-agentic-skills-top-10/ast04.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.

## AST05 Untrusted External Instructions

- Risk summary: Retrieved evidence can carry directions that try to replace the authorized task or scope.
- Kiyo control IDs: KIYO-SEC-003, KIYO-TRUST-001.
- Skill/shared procedure: [Injection review](prompt-injection.md).
- Expected behavior: Keep README/web/issues/tool outputs/memory/copied approvals at their actual authority; do not execute embedded privilege changes or secret reads.
- Required evidence: Sanitized source/location, trusted task/policy boundary, attempted effect, approval provenance and observed or withheld actions.
- Control owner: Kiyo Markdown guidance: interpret/report; Host-native security: real denial/permissions; Human organization process: valid policy/approval.
- Residual limitations: Instructions can be missed; Kiyo cannot prevent all prompt injection or retract prior exposure.
- Test case references: TC-AST-05A, TC-AST-05B, TC-AST-05C, TC-AST-05D, TC-AST-05E, TC-AST-05F; execution NOT_RUN.
- Source: [OWASP AST05](https://owasp.github.io/www-project-agentic-skills-top-10/ast05.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.

## AST06 Weak Isolation

- Risk summary: Insufficient boundaries let an agent action reach data or systems outside its intended scope.
- Kiyo control IDs: KIYO-SEC-006.
- Skill/shared procedure: [Required-control check](control-ownership.md#kiyo-sec-006--establish-required-host-controls-or-hold-dependent-execution).
- Expected behavior: Hold dependent execution/disclosure when required isolation cannot be established; retain independent safe review.
- Required evidence: Specific policy requirement, actual host/version/configuration, permitted control observation/date and missing or unsupported properties.
- Control owner: Host-native security: implement isolation; Human organization process: required boundary and permitted environment; Kiyo Markdown guidance: report/hold.
- Residual limitations: Kiyo has no sandbox or network blocker; a host feature description is not evidence it was enabled.
- Test case references: TC-AST-06; execution NOT_RUN.
- Source: [OWASP AST06](https://owasp.github.io/www-project-agentic-skills-top-10/ast06.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.

## AST07 Update Drift

- Risk summary: Changed skill content or stale installed versions can invalidate earlier reviews and approvals.
- Kiyo control IDs: KIYO-SEC-005, KIYO-AUTH-004.
- Skill/shared procedure: [Update review](update-and-provenance.md#kiyo-sec-005--reassess-changed-content-and-scope-before-reuse).
- Expected behavior: Compare baseline/candidate and material permissions/references; reuse only still-matching approval and preserve user policy/memory.
- Required evidence: Observed old/new identities, actual diff and relevant advisories, changed effects, approval scope and native update outcome if executed.
- Control owner: Developer release process: delta review; Human organization process: valid adoption scope; Host-native security: actual lifecycle controls; Kiyo Markdown guidance: reassess.
- Residual limitations: No watcher or automatic pinning; unknown cached identity blocks a claim of successful update review.
- Test case references: TC-AST-07A, TC-AST-07B; execution NOT_RUN.
- Source: [OWASP AST07](https://owasp.github.io/www-project-agentic-skills-top-10/ast07.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.

## AST08 Poor Scanning

- Risk summary: A review may miss behavior while reporting clean syntax, patterns or model judgments.
- Kiyo control IDs: KIYO-SEC-007.
- Skill/shared procedure: [Layered Skill Audit](trust-review.md#kiyo-sec-007--keep-review-layers-and-blind-spots-explicit).
- Expected behavior: Separate static, behavioral, adversarial and per-target observations; report omissions and do not certify safety from regex/LLM output.
- Required evidence: Reviewed artifact/date, actual tool/options or human method, coverage, fixtures, expected/observed effects, results and blind spots.
- Control owner: Developer release process: execute permitted checks and retain evidence; Kiyo Markdown guidance: honest results; Host-native security: safe test environment and observable effects.
- Residual limitations: Finite tests and incomplete traces cannot prove absence of harmful behavior; future specs are NOT_RUN.
- Test case references: TC-AST-08; execution NOT_RUN.
- Source: [OWASP AST08](https://owasp.github.io/www-project-agentic-skills-top-10/ast08.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.

## AST09 No Governance

- Risk summary: Unowned adoption or stale authorization leaves skill use and response to incidents unaccountable.
- Kiyo control IDs: KIYO-SEC-008, KIYO-AUTH-004.
- Skill/shared procedure: [Optional record procedure](control-ownership.md#kiyo-sec-008--keep-accountable-optional-file-records).
- Expected behavior: Use existing records when needed; preserve unknown owners and actual human scope; distinguish revocation decisions from executed disablement.
- Required evidence: Artifact inventory, actual role/approval provenance, validity/revocation scope, sanitized incident observations and action evidence if available.
- Control owner: Human organization process: accountable decisions/response; Kiyo Markdown guidance: neutral records; Host-native security: actual disable/uninstall effects.
- Residual limitations: Files are optional records, not tamper-proof logs, an authenticated approval service or a kill switch.
- Test case references: TC-AST-09; execution NOT_RUN.
- Source: [OWASP AST09](https://owasp.github.io/www-project-agentic-skills-top-10/ast09.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.

## AST10 Cross-Platform Reuse

- Risk summary: A port can preserve instructions while losing required loading or permission behavior.
- Kiyo control IDs: KIYO-SEC-009, KIYO-SEC-002.
- Skill/shared procedure: [Six-target parity review](control-ownership.md#kiyo-sec-009--verify-each-platform-control-independently).
- Expected behavior: Compare each required control independently on each host; expose unsupported/unverified gaps and hold dependent use.
- Required evidence: Exact source/overlay/artifact, native contract/date, host/version/configuration, per-control/per-target observations and limits.
- Control owner: Developer release process: content/overlay parity; Host-native security: target controls; Kiyo Markdown guidance: gap reporting; Human organization process: accepted required controls.
- Residual limitations: Shared Markdown and a passing CLI test do not prove IDE behavior; no fallback or unsupported field is invented.
- Test case references: TC-AST-10; execution NOT_RUN.
- Source: [OWASP AST10](https://owasp.github.io/www-project-agentic-skills-top-10/ast10.html), checked 2026-09-29, DOCUMENTED_ONLY; draft taxonomy, not native enforcement evidence.
