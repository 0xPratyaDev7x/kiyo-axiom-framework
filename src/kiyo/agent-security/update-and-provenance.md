# Update and provenance review

## KIYO-SEC-004 — Bind source review to the actual artifact

For a requested release/adoption review, identify the observed source/revision,
publisher evidence, distribution channel, candidate artifact and included files.
Follow [dependency governance](../governance/dependency-governance.md) for direct
and relevant transitive inputs, fetched instructions, build/install scripts and
new external destinations. A same-named package or URL is not the same provenance.

In developer release work, record the actual canonical and overlay revisions,
allowed transformations, build inputs/tool versions, file inventory and computed
source/output digests. Compare generated shared bytes with their canonical source
and check contained resources. Bind every result to the actual reviewed artifact,
not merely a mutable tag or product name. No generated Kiyo package exists merely
because this procedure is present.

A hash computed from a candidate proves neither its origin nor that it matches an
independently trusted expected artifact. Record the digest method/value only if
actually run. A signature claim needs the real verification result, artifact,
trust basis and signer evidence from the authorized release/native mechanism.
Missing evidence stays UNKNOWN/NOT_RUN. Unsigned is not automatically malicious;
apply the accepted policy as described in [trust review](trust-review.md).

Kiyo supplies no runtime signature verifier, signing keys, transparency service
or end-user build step. Do not select publisher/license/version identities for
the owner or turn a provenance review into publication permission.

## KIYO-SEC-005 — Reassess changed content and scope before reuse

Use this shared update review before an authorized adoption/update and when
material drift is discovered; there is no watcher or background rescanning.

1. Establish installed/reviewed baseline and candidate identities from permitted
   evidence. A missing baseline is a review gap, not proof there is no delta.
   Inspect actual installed resources when authorized; do not assume the latest
   repository text equals cached content.
2. Compare instructions, metadata, source/publisher ownership, complete referenced
   resources, dependencies, destinations, loading/activation rules and requested
   permissions. Same version text with changed bytes is an integrity discrepancy.
3. Re-run relevant [Skill Audit](trust-review.md) checks for the delta and its
   dependencies. Review upstream fixes as well as new risks; do not prescribe
   indefinite pinning that ignores known required security updates.
4. Compare existing approval with the actual candidate/effects and
   [valid scope](../governance/human-approval.md). Reuse still-valid approval;
   expanded access or changed material prerequisites require reassessment and
   whatever new scope approval policy requires.
5. Use only documented native lifecycle/scope for the actual target when update
   execution is authorized. If verified pinning/update controls are required but
   unavailable or unverified, hold that dependent use; do not invent a host flag
   or claim Kiyo prevents automatic changes.
6. Record checks actually performed, remaining gaps and what identity is now
   observed. An update request is not proof it completed. Inspect rollback
   feasibility rather than promising it; rollback/disable/uninstall need their
   own authority and may not retract exposure or earlier effects.

Keep user-owned policy, approvals and canonical memory outside installed cache.
Do not replace them with new defaults or use an update to rewrite approved intent.
Preserve established state paths and concurrent human edits. No delta means no
timestamp touch; read-only review produces only a report in the authorized channel.
Record material findings through the [Memory lifecycle](../workflows/memory-lifecycle.md)
only when a real delta and write authority exist.
