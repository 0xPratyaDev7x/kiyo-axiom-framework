# Troubleshooting

Checked **2026-09-29**. Use the current
[live matrix](../compatibility/live-test-matrix.md) before interpreting an older
package-build report. Earlier NOT_TESTED snapshots are historical; newer native
metadata results still do not establish Skill behavior.

| Symptom | Inspect within authorized scope | Next action and limit |
| --- | --- | --- |
| Skill does not appear | Actual host/surface, enabled candidate/source, manifest location and eight skills/<slug>/SKILL.md files | Use the [selection guide](README.md#select-a-skill); confirm Kiyo source, not a built-in command. Do not invent aliases or enable broad/global permissions |
| Resources missing after install | Actual installed entry and its relative references/kiyo tree; package identity and complete extraction | Use the complete prepared payload. Report the missing file; stop dependent Kiyo actions. Do not fetch a guessed replacement or require a consumer generator |
| Core not loaded | Whether the Skill was actually selected and its bootstrap/readable Core established | Explicit selection and automatic Core are separate. Report unavailable/unverified activation; propose a managed project block only if needed and authorized |
| Wrong workflow | User intent, selected Skill and allowed mutation | Review/explain remains read-only; fixes need Implement intent. “ดู login ให้หน่อย” is not write permission. Report explicit-selection mismatch before transitioning |
| Memory is stale | Current canonical index, record type, scope, evidence and last_verified | Use check; sync only authorized observation deltas. Code conflicting with approved intent is drift, not permission to revise a decision |
| Version unsupported or unknown | Actual version/help/extension metadata and the dated capability page | Minimum Kiyo compatibility is not established by one observed version. Keep NOT_TESTED/UNKNOWN; do not force an upgrade or claim CLI success proves IDE support |
| Codex IDE cannot install Kiyo | Official native-plugin support | UNSUPPORTED, not a transient install failure. No standalone fallback has been approved |
| Validation warns or fails | Exact diagnostic and candidate bytes | Claude strict check fails for missing version/author; Codex public ingestion lacks version/author/developerName. Owner inputs are required; do not fill fake values |
| Host reports version 1.0.0 | Manifest version versus host-derived metadata | P26 Codex fallback is not a Kiyo release; record both without inventing history |
| Tests cannot run | Inspected command, environment and target | BLOCKED/NOT_RUN with reason; missing environment is not NOT_APPLICABLE or PASS. Do not use production or install tools implicitly |
| Policy/host denies an action | Actual authority, scope and prohibition | Preserve the denial; request an authorized decision where applicable. Do not change policy or native settings to pass the task |

For Claude native validation/discovery use the exact
[no-quota reproduction commands](../compatibility/live-reproduction-guide.md).
For documented Copilot source/UI lifecycle, see
[installation guide](../compatibility/copilot-installation.md).
Restart/new-session checks and managed-block update behavior remain untested.

A useful issue report contains the target, observed host/plugin version or
Unknown, candidate/source, install method/scope, sanitized exact error, selected
Skill, expected versus observed behavior and inspected resource paths. Include
actual evidence only; redact sensitive values and do not attach credentials,
environment dumps or raw private logs. Creating a report file requires authorized
write scope. Do not delete an entire cache or instruction file as a generic fix.
