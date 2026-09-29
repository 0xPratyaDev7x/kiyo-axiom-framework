# Standard concepts to Kiyo rules and evidence

Optional rationale, loaded for standards/traceability questions. These are
original Kiyo practices informed by public descriptions, not reproduced standards,
exact taxonomies, clause mappings, conformance tests or certification claims.
Links below are optional sources; following this checklist requires no network.

Public ISO catalogue pages were checked **2026-09-29**: DOCUMENTED_ONLY, not licensed
full-text assessments or behavioral results. The engineering rules are authored
guidance; applying them still needs task-specific evidence. Existing security
sources retain their own earlier check dates below.

| Standard concept / official source | Kiyo rule / procedure | Expected evidence | Status and limitation |
| --- | --- | --- | --- |
| Life-cycle processes — [ISO/IEC/IEEE 12207:2026, edition 2](https://www.iso.org/standard/90219.html) | [KIYO-ENG-002](requirements.md), [KIYO-ENG-005](testing.md), shared implementation flow | Linked behavior, scoped change, verification and completion records | DOCUMENTED_ONLY; checked 2026-09-29; public process scope, not a mandated Kiyo workflow or full standard implementation. |
| Requirements engineering — [ISO/IEC/IEEE 29148:2018, edition 2](https://www.iso.org/standard/72089.html) | [KIYO-ENG-002](requirements.md) | Sourced objective/rules, stable IDs, observable acceptance, decisions and unknowns | DOCUMENTED_ONLY; checked 2026-09-29; published edition with revision in progress, not the draft replacement or clause-level compliance. |
| Product quality model — [ISO/IEC 25010:2023, edition 2](https://www.iso.org/standard/78176.html) | [KIYO-ENG-006](quality.md) | Affected quality concern, project target and scoped evidence/gap | DOCUMENTED_ONLY; checked 2026-09-29; Kiyo grouping intentionally does not claim exact taxonomy equivalence. |
| Test concepts — [ISO/IEC/IEEE 29119-1:2022, edition 2](https://www.iso.org/standard/81291.html) | [KIYO-ENG-005](testing.md) | Rationale for applicable check types and distinction between expected and observed behavior | DOCUMENTED_ONLY; checked 2026-09-29; introductory public scope only, not full technique coverage. |
| Test processes — [ISO/IEC/IEEE 29119-2:2021, edition 2](https://www.iso.org/standard/79428.html) | [KIYO-ENG-005](testing.md), bounded failure recovery | Authorized baseline/execution, classified failures and repair limits | DOCUMENTED_ONLY; checked 2026-09-29; Kiyo's procedure is its own adaptation, not an ISO process claim. |
| Test documentation — [ISO/IEC/IEEE 29119-3:2021, edition 2](https://www.iso.org/standard/79429.html) | [KIYO-ENG-005](testing.md) | Scope, method/command, environment, result and sanitized evidence | DOCUMENTED_ONLY; checked 2026-09-29; no copyrighted test-document templates copied. |
| Test techniques — [ISO/IEC/IEEE 29119-4:2021, edition 2](https://www.iso.org/standard/79430.html) | [KIYO-ENG-002](requirements.md), [KIYO-ENG-005](testing.md) | Relevant boundary/error/regression examples and uncovered cases | DOCUMENTED_ONLY; checked 2026-09-29; examples are Kiyo choices, not claimed ISO technique-by-technique coverage. |
| Secure development — [NIST SSDF 1.1 / SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) | [KIYO-ENG-004](coding.md), dependency governance, application security | Scoped secure-code review, dependency rationale and actual verification | DOCUMENTED_ONLY; checked 2026-09-28 research baseline; final 1.1 baseline, not draft 1.2 adoption or an attestation. |
| Application security verification — [OWASP ASVS](https://owasp.org/projects/asvs) | [Application security](../../agent-security/application-security.md), [KIYO-ENG-004](coding.md) | Affected security boundary, finding/fix and scoped evidence | DOCUMENTED_ONLY; checked 2026-09-29 research baseline (5.0.0); topic adaptation, not ASVS control-level assessment or Agentic Skills AST. |

Architecture continuity (KIYO-ENG-003 / KIYO-ENG-001), minimal diff
(KIYO-ENG-007 / KIYO-CHG-001) and profile opt-in (KIYO-PROF-001) are Kiyo/project
rules. No ISO/NIST source is claimed to mandate a particular architecture,
library, stack, approval mode or test runner. For their evidence use the linked
[architecture](architecture.md), [scope](change-scope.md) and
[profile contract](../../profiles/extension-contract.md).

Management/AI-governance standards remain contextual references, not software
stack presets. Do not treat AI-assisted coding alone as development of an AI
system or automatically apply ISO/IEC 5338. No Kiyo checklist constitutes a
licensed standard, organizational audit or ISO/OWASP/NIST certification.
