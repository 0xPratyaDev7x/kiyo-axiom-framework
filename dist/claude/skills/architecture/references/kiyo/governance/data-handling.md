# Data handling

## KIYO-DATA-001 — Classify content and minimize exposure

Apply actual accepted organization/project policy using content, provenance,
authorized audience and consequences of disclosure. File extension, folder/name,
an “internal” label or an “Enterprise” account is not sufficient classification.
Do not read forbidden content merely to classify it; use permitted context and
record uncertainty. An unknown class is not automatically Public.

| Class | Meaning and handling expectation |
| --- | --- |
| Public | Evidence establishes authorized public disclosure; use only relevant content and respect remaining task/policy constraints |
| Internal | Intended for an authorized internal audience; verify permitted tools/destinations before further exposure |
| Confidential | Sensitive organizational, contractual or personal content with limited authorized access; minimize and use only evidenced approved handling paths |
| Restricted | Highly sensitive or explicitly tightly controlled material, such as credentials or critical secrets; avoid raw access/disclosure unless independently authorized and expressly permitted by applicable policy/host |

These Kiyo categories do not invent an organization's classification or legal
determination. An accepted policy can impose stricter handling. Mixed content
must be handled at the most restrictive applicable class for the part being
processed until safe separation is established. Explain the content/policy basis
and limits; do not infer it solely from a path or downgrade it to use a tool.

Consider reading, model context, tool output, logs, attachments, network requests,
memory, reports and generated artifacts as possible exposure points. Read-only
can still disclose data. Before requesting additional sensitive content, establish
necessity, actual access and allowed destination through
[permissions](permissions.md) and [provider policy](provider-policy.md).
Prefer redacted excerpts, synthetic fixtures, schema/metadata or a local
authorized validation whose output avoids protected values when sufficient.

Never persist secrets, PII, raw logs or private reasoning in project memory.
Use concise safe summaries and non-sensitive evidence/role references under
[Memory minimization](../framework/memory-specification.md#kiyo-mem-007--durable-minimized-content).
Do not reproduce sensitive material in approval requests or drift reports.
If accidental sensitive content appears, avoid repeating or forwarding it,
identify the issue without the value and follow the actual authorized handling
process. Do not claim that deleting a local copy retracts an earlier transmission.

Kiyo is not DLP or an egress filter. It cannot guarantee that data has not already
been transmitted to a provider before this policy was loaded, nor that native
software follows it. This limitation does not authorize further disclosure.
Use observed controls and report unknown exposure instead of inventing assurance.
