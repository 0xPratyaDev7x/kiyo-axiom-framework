# Kiyo Compass — Standards baseline

Checked: **2026-09-28**. Official source IDs resolve in
[SOURCES.md](SOURCES.md). This is a concept-level research baseline for
REQ-056–067, not a conformity assessment, certification, legal opinion, complete
control mapping or evidence that product controls exist.

All edition/status findings below are **DOCUMENTED_ONLY**: public official
catalogs/project pages were retrieved. Full licensed ISO texts were not reviewed
or copied. No clause numbers are supplied. “Published”, “draft” and “confirmed”
are source publication states, not Kiyo verification results.

## Primary engineering references

| Reference | Edition / status observed | Proposed Kiyo concept alignment | Source / checked | Limitation |
| --- | --- | --- | --- | --- |
| ISO/IEC/IEEE 12207 | **2026, edition 2**, published April 2026; replaces withdrawn 2017 edition | Lifecycle-aware Requirement, Implement, Review, Test and release/handoff evidence | [S01](https://www.iso.org/standard/90219.html), 2026-09-28 | Catalog/abstract only; do not retain 2017 as “latest” or claim lifecycle compliance. |
| ISO/IEC/IEEE 29148 | **2018, edition 2**, published; confirmed 2024, now revision in development (DIS 29148) | Requirement provenance, measurable acceptance criteria and traceability | [S02](https://www.iso.org/standard/72089.html), 2026-09-28 | A DIS is not a published replacement; recheck before detailed mapping. |
| ISO/IEC 25010 | **2023, edition 2**, published; product quality model, supersedes 2011 | Quality-attribute questions and measurable quality criteria in Architecture/Review/Test | [S03](https://www.iso.org/standard/78176.html), 2026-09-28 | Do not treat old quality-in-use coverage as unchanged or reproduce the model's full normative text. |
| ISO/IEC/IEEE 29119-1 | **2022, edition 2**, published | Testing vocabulary and separation of test intent from evidence | [S04](https://www.iso.org/standard/81291.html), 2026-09-28 | Part 1, not an edition for the whole series. |
| ISO/IEC/IEEE 29119-2 | **2021, edition 2**, published | Test planning, execution, reporting and completion decisions | [S05](https://www.iso.org/standard/79428.html), 2026-09-28 | Process alignment proposal; no process-conformity claim. |
| ISO/IEC/IEEE 29119-3 | **2021, edition 2**, published | Kiyo-authored test/evidence templates and trace records | [S06](https://www.iso.org/standard/79429.html), 2026-09-28 | Do not copy copyrighted standard templates. |
| ISO/IEC/IEEE 29119-4 | **2021, edition 2**, published | Risk-relevant test-design technique selection | [S07](https://www.iso.org/standard/79430.html), 2026-09-28 | Detailed technique/clause correspondence not assessed; other series parts outside this baseline. |

## Primary governance and security references

| Reference | Edition / status observed | Proposed Kiyo concept alignment | Source / checked | Limitation |
| --- | --- | --- | --- | --- |
| ISO/IEC 27001 | **2022, edition 3**, published; **Amendment 1:2024** (climate action changes) published separately | Information-security risk ownership, evidence, access responsibility and review | [S08](https://www.iso.org/standard/27001), [S09](https://www.iso.org/standard/88435.html), 2026-09-28 | An ISMS standard; installing Kiyo is not implementing or certifying an ISMS. |
| ISO/IEC 42001 | **2023, edition 1**, published | AI use accountability, governance decisions, review and records | [S10](https://www.iso.org/standard/42001), 2026-09-28 | Organization management-system obligations need organization evidence, not Markdown alone. |
| ISO/IEC 23894 | **2023, edition 1**, published | Context, identification, assessment, treatment and review of AI-related risks | [S11](https://www.iso.org/standard/77304.html), 2026-09-28 | Guidance used at concept level; actual risk decisions remain owned by users/organizations. |
| NIST SSDF | **SP 800-218, version 1.1**, final, 2022-02-03. **SP 800-218 Rev. 1, version 1.2** remains initial public draft, 2025-12-17 | Preparation, software protection, secure production and vulnerability response inform Security/Review/release procedures | [N01](https://csrc.nist.gov/pubs/sp/800/218/final), [N02](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd), [N03](https://csrc.nist.gov/projects/ssdf), 2026-09-28 | Use 1.1 final as baseline; track 1.2 separately. Closed comment period does not establish final status. |
| NIST AI RMF | **1.0**, released 2023-01-26; official site says revision in progress | Governance and context/risk review, assessment evidence, treatment follow-up | [N04](https://www.nist.gov/itl/ai-risk-management-framework), 2026-09-28 | Voluntary framework; no guessed successor number. Generative-AI profile is supplemental, not replacement. |
| OWASP ASVS | Official project main text identifies **5.0.0** as stable | Application-specific technical security acceptance criteria in Security/Review/Test | [W01](https://owasp.org/projects/asvs), 2026-09-28 | Apply only relevant application controls; not a plugin packaging schema or universal checklist for every artifact. Moving/bleeding-edge content must be pinned before requirement-level mapping. |
| OWASP Agentic Skills Top 10 | **v1 public-review draft**; same page also labels active new-project proposal / “1.0 (2026 Edition)” | Skill Audit taxonomy in the following table | [W02](https://owasp.github.io/www-project-agentic-skills-top-10/), 2026-09-28 | Mixed maturity wording; no evidence of a finalized release. Platform examples and proposed universal format are not native API contracts. |

## Supporting and conditional references

| Reference | Edition / status observed | Use decision | Source / checked | Limitation |
| --- | --- | --- | --- | --- |
| ISO/IEC 38507 | **2022, edition 1**, published | Supporting: governance implications of organizational AI use | [S12](https://www.iso.org/standard/56641.html), 2026-09-28 | Inform owner/accountability questions, not an additional certification claim. |
| ISO/IEC 27034 | **Part 1:2011, edition 1**, published; confirmed 2022 | Supporting: application-security concepts and lifecycle context | [S13](https://www.iso.org/standard/44378.html), 2026-09-28 | Only part 1 reviewed; do not label the entire multipart family “2011” or assert other parts' status. |
| OWASP SAMM | **Version 2 / 2.0 model** described by model and release-notes pages | Supporting: improvement planning and security-practice maturity questions | [W03](https://owaspsamm.org/model/), [W04](https://owaspsamm.org/release-notes-v2/), 2026-09-28 | Latest incremental content/tool release UNKNOWN; no maturity score or completed assessment claimed. |
| ISO/IEC 5338 | **2023, edition 1**, published | **Conditional only:** use when a project develops/acquires an actual AI system | [S14](https://www.iso.org/standard/81118.html), 2026-09-28 | Not activated merely because an AI coding agent helps build ordinary software. Kiyo's current static framework scope does not itself establish an AI-system lifecycle project. |

## AST taxonomy provenance and mapping

The retrieved W02 summary names the same ten categories as REQ-058–067.
The abbreviated labels below preserve the registered IDs. All proposed actions
were Prompt 02 design interpretations, **not implemented controls at that step**.
Prompt 07 now authors [advisory controls and procedures](../../src/kiyo/agent-security/owasp-ast10.md);
this does not establish runtime enforcement or behavioral success.

Source for every row: [W02](https://owasp.github.io/www-project-agentic-skills-top-10/),
checked **2026-09-28**, DOCUMENTED_ONLY, public-review maturity limit.

| Category | Requirement | Proposed advisory check | Limit / native boundary |
| --- | --- | --- | --- |
| AST01 Malicious Skills | REQ-058 | Origin, suspicious instructions and claimed authority | Review cannot prove absence of malicious intent. |
| AST02 Supply Chain Compromise | REQ-059 | Source-to-artifact provenance and release integrity evidence | No invented hashes, signatures, publisher trust or scanner result. |
| AST03 Over-Privileged Skills | REQ-060 | Compare requested access to task need | Host, not Kiyo, grants/enforces permissions. |
| AST04 Insecure Metadata | REQ-061 | Validate actual host fields and honest capability metadata | Unknown fields can be dropped or ignored; no cross-host enforcement inference. |
| AST05 Untrusted External Instructions | REQ-062 | Treat retrieved text as data and inspect authority conflicts | A source claiming authority cannot promote itself to host/system instruction. |
| AST06 Weak Isolation | REQ-063 | Record actual host isolation and residual exposure | No Kiyo sandbox, network boundary or runtime isolation is supplied. |
| AST07 Update Drift | REQ-064 | Re-review changed package/source/version and activation behavior | Native auto-update semantics vary; a version pin needs real verification. |
| AST08 Poor Scanning | REQ-065 | Separate static, behavioral and adversarial checks | A clean static result is not proof of safe behavior. |
| AST09 No Governance | REQ-066 | Static inventory, owner, scoped approval and revocation records | No central registry/service or fabricated approver. |
| AST10 Cross-Platform Reuse | REQ-067 | Per-target capability and control gaps | Shared Markdown and manifest parsing do not prove control parity. |

W02's universal format proposes permission/signature fields. They are **not**
adopted as native manifest/frontmatter fields. Its runtime mitigations remain host
or organization responsibilities. This research neither adds runtime components
nor imports third-party scanning dependencies.

## Prompt 07 revalidation and implemented guidance

Checked 2026-09-29: [W02](https://owasp.github.io/www-project-agentic-skills-top-10/)
and its ten linked detail pages retain AST01–AST10 above. Source state remains
DOCUMENTED_ONLY, public-review draft with mixed proposal/edition wording; no
finalized AST release is inferred. [W05](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)
announces the separate Agentic Applications initiative using ASI identifiers.
Its 2025-12-09 announcement is not a latest-minor-version determination.
AST and ASI IDs are not interchangeable; no exhaustive crosswalk is claimed.

[W01](https://owasp.org/projects/asvs) was rechecked after its original URL
redirect: main text still calls 5.0.0 stable, with conflicting sidebar wording
retained as a limitation. Kiyo's separate
[application checklist](../../src/kiyo/agent-security/application-security.md)
covers the user-requested topics; it is not a full ASVS clause mapping.
The table above preserves Prompt 02's original check dates; other standards were
not refreshed. Detailed URL/dates and retrieval limits are in
[SOURCES](SOURCES.md#prompt-07-owasp-revalidation).

Ten new Kiyo security controls, scoped Skill Audit/update/injection procedures,
four optional neutral record templates and a six-target control-gap matrix are
authored Markdown. Nineteen developer scenario specifications are NOT_RUN.
No scanner, runtime isolation, signature verification or certification is supplied.

## Mapping and revalidation boundary

The architecture and authored governance/security guidance use these concepts
with explicit responsibility, evidence scope and residual gaps. Later packaging,
skill and verification prompts must connect them to actual artifacts and outcomes.
A clause-level mapping requires lawful
access to the selected edition and review of the exact text first.

Recheck editions, amendments, draft/final state and AST labels before release.
If a required official page becomes inaccessible, record NOT_REVALIDATED for that
claim, preserve the last checked edition and defer only the dependent mapping or
schema decision. Do not “upgrade” a baseline from memory.

