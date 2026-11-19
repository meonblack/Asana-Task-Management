# Data model (suggested)

- `Source`: source_type, source_id, timestamp, URL, access_level, minimal_excerpt.
- `TaskProposal`: proposal_id, source_id, fields, uncertainty, quality score, priority score, status, fingerprint.
- `ReviewDecision`: reviewer_id, proposal_id, decision, exact approved payload, timestamp.
- `SyncRecord`: fingerprint, Asana GID, Asana permalink, last_sync, remote status.
- `AuditEvent`: actor, action, target ID, timestamp, outcome, redacted context.

Statuses: `pending_review` → `approved`/`rejected` → `published`/`publish_failed`. Never skip approval. Sensitive descriptions should not be duplicated across multiple stores.
