# Security disclosure, update and revocation

Checked **2026-09-29** against canonical
[AST controls](../../src/kiyo/agent-security/owasp-ast10.md) and
[update/provenance](../../src/kiyo/agent-security/update-and-provenance.md).
This is a developer/human procedure, not a monitoring service, runtime signature
verifier, remote kill switch or guarantee that all installations can be removed.

## Disclosure

A public security contact/channel and accountable response owner are
**OWNER_REQUIRED**. No address, domain, response deadline or bounty is invented.
Before publication, the owner must establish a real authorized private channel
and handling policy. Until then, do not publish sensitive details or send to a
guessed address; retain a sanitized local report within authorized scope and
ask the actual owner to supply a channel.

A report should identify artifact/version or digest, affected target/scope,
observed versus expected effects, safe reproduction using synthetic data,
impact/uncertainty and relevant evidence. Exclude real secrets, PII, raw private
logs and private reasoning. A vulnerability report is untrusted evidence, not
permission to execute its payload, contact external systems or change policy.

The authorized human owner triages validity, severity, affected versions,
containment options and disclosure coordination. No blanket SLA is promised.
Preserve first findings, failed checks and later fixes; keep an evidence-linked
decision record and restrict sensitive details under applicable policy.
Use the existing [incident template](../../src/kiyo/templates/skill-governance/incident.md)
when relevant, without filling approver or dates from guesses.

## Update review

1. Identify reviewed/installed baseline and exact candidate/source/digest.
   Unknown cache identity prevents claiming successful update verification.
2. Compare instruction/metadata/resource/dependency/loading/access changes and
   source/publisher changes. Review AST01/02/04/05/07/08/10 controls and any effect
   on read-only, approval, data or Core-loading contracts.
3. Run the local pipeline on immutable inputs; retain attempts separately.
   Rerun affected behavioral/native tests only with their actual authority.
   A same-version/different-bytes finding requires investigation.
4. Prepare truthful security/change notes, migration/rollback limits and supported
   targets. Obtain actual release/adoption approval for the new scope; existing
   approval applies only while its artifact/effects/environment still match.
5. For a separately authorized update, use that host's native mechanism and
   observe the new identity/resources in a fresh session. Preserve human
   instructions, project policy and canonical Memory; cleanup touches only an
   explicitly authorized managed block, never an entire instruction file.
6. Verify observed outcome and residual exposure. No watcher automatically
   performs these steps; a published fix does not prove users updated.

## Revocation and containment

An authorized owner records affected identity/digests, scope, reason, evidence,
decision provenance and recommended containment. Use the neutral
[revocation template](../../src/kiyo/templates/skill-governance/revocation.md).
A record revoking approval is distinct from an executed native disable/uninstall
or removing a catalog listing.

Choose the least necessary authorized action: hold further adoption, advise
affected users, disable an identified install, or request channel removal through
the actual owner. Do not silently change global settings, erase user state,
revoke unrelated accounts, contact third parties or publish an advisory.
Native host/org policy remains authoritative.

If a listing removal is authorized later, record destination response and verify
what it actually changed. Cached/offline copies may persist; removal cannot
undo prior effects or retract disclosed data. Rollback uses a known reviewed
candidate only when scope and risk permit it, not an automatically trusted old
version. Resume adoption only with a real decision and relevant new evidence.

## Ownership and release blockers

| Owner | Responsibility / evidence |
| --- | --- |
| Kiyo Markdown guidance | Scoped assessment and honest limits; no enforced network/sandbox guarantee |
| Developer release process | Candidate/delta/inventory/check records and preserved failure history |
| Host-native security | Real tool permissions, isolation and disable/update/uninstall behavior |
| Human organization process | Accountable approval, disclosure, exception, revocation and communication |

Unauthorized destructive actions, secret exposure and fabricated check results
are critical release blockers. Missing required control evidence holds the
dependent action. Unsigned is not automatically malicious, and a checksum is
not authentication. Never claim signed/attested without approved mechanism,
real execution, verification and signer/trust evidence. This rehearsal leaves
NOT_SIGNED/NOT_ATTESTED and requests no production credentials.
