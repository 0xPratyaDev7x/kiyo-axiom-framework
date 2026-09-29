# Local release readiness

Generated developer evidence; not a release or publication.

- Package: **PACKAGE_VALIDATED_WITH_LIMITATIONS**
- Host: **NOT_HOST_VERIFIED** (six statuses in pipeline.json)
- Publication: **NOT_PUBLISHED / BLOCKED**
- Signature: **NOT_SIGNED**; provenance attestation: **NOT_ATTESTED**
- Pipeline exit: 0
- Checksums identify bytes, not publisher identity.
- Read pipeline.json for commands, results, failures and blocked checks.
- Read artifact-inventory.json for per-file hashes and canonical provenance.
- Read dependency-inventory.json / attribution-inventory.json; neither is a formal SBOM.

Publication blockers:
- Owner name/version/license/publisher/source/destination/approval unresolved
- Native metadata/ingestion release failures retained
- Independent host/behavior/activation/update acceptance incomplete
- Signing/attestation mechanism and authority not approved
- Human security/license review and disclosure contact not established
