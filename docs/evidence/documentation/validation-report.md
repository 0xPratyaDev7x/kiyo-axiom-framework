# Prompt 27 documentation validation

Checked **2026-09-29**; documentation scope only. Task status: DONE.
The [first actual audit](audit-01.json) ran via a PowerShell single-quoted
here-string piped to `python -B -`: exit **0**, six checks PASS, no failure.
It recorded its start/end times, command argv, document hashes and actual output.
The [final build-state closure](audit-02.json) also exits **0**, six checks PASS,
including eight new trace mappings and next28. It checks 2,575 Markdown files and
18,707 local links before this final result-link edit. Its JSON retains the audit
source for reproduction; the first record is preserved. No native/model call ran.

## What was checked

| ID | Actual method / scope | Result and limitation |
| --- | --- | --- |
| P27-A01 | Match guide Skill links with canonical and all three shipped eight-entry inventories; inspect nine exact-input/expected/evidence/observed sections | PASS: ten guide/draft documents; nine walkthroughs explicitly NOT_RUN. No behavioral execution |
| P27-A02 | Compare six README target rows and underlying native/behavioral JSON states | PASS: no result promotion; 72 live records retain two PASS/70 NOT_RUN; 48 behavioral cases NOT_RUN |
| P27-A03 | Compare draft descriptions/interface/identity to actual overlay JSON | PASS: values match; version unset; owner gates explicit, no listing |
| P27-A04 | SHA-256 comparisons to P23 inventory plus Git product/tool/test diff and original LICENSE blob | PASS: 112 inputs, tooling and three ZIPs unchanged |
| P27-A05 | Inspect local inline Markdown links/heading anchors, containment and exact-case directory names; platform adapters resolved in their shipped context | PASS: first run 2,574 Markdown files and 18,642 links. External URLs are handled by the separate source check, not this script |
| P27-A06 | Registry/trace identity and status assertions; Git index/HEAD/branch, absent local project state and diff --check | PASS: 80 full statuses remain NOT_RUN, no product Memory/bootstrap; closure rerun also checks next28 and scoped trace additions |

Seven official pages were retrieved for current native wording:
[UG27 source/date/destination record](../../research/SOURCES.md#prompt-27-documentation-source-check).
No redirect was reported for these returned URLs. They document native facilities,
not observed Kiyo activation.

## Content review

The author compared the guides with the shipped eight SKILL.md entries, Core,
Memory/config/governance contracts, native adapters, manifest metadata and P26
results. Reviewed boundaries include Requirement readiness versus coding authority;
Test assess/run/write effects; read-only Review/Architecture/Security; Memory
correction versus approved-intent drift; contextual risk/scoped approvals;
project-owned state and managed-block-only cleanup; static versus host enforcement.

A draft walkthrough link to a nonexistent profiles index was corrected to the
actual .NET/Angular files before the first audit. No test invariant was removed,
no product behavior was changed, and no failed host result was concealed.
This is self-review, not independent audit, usability study or proof that every
possible documentation interpretation is correct.

## Coverage and retained gaps

Primary documentation requirement: REQ-078. Supporting documentation coverage:
REQ-004, REQ-005, REQ-010, REQ-076, REQ-077, REQ-079, REQ-080.
All remain PARTIALLY_IMPLEMENTED with full verification NOT_RUN; documentation
existence/static checks do not satisfy their unexecuted native clauses.
The nine [walkthroughs](../../user/walkthroughs.md) are illustrative/synthetic
expected behavior, not simulated evidence or new host results.

No native installation, agent/model call, account operation, paid quota,
publication, global setting, product rebuild or consumer runtime was introduced.
Source/overlay/tool/test/package bytes, historical results, user work and LICENSE
are preserved. Developer-project Memory Impact: NONE.

DEC-001–004 remain open: publication identity, license confirmation,
publisher/destination and Codex IDE treatment. Product version is unset; Claude
strict metadata failure and Codex public ingestion failure remain. No universal
support/always-on/security/privacy/certification claim is made. Safe to continue
with requested Prompt 28 release tooling while preserving those gates.
