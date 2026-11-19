# Architecture

```text
Gmail / Calendar / Drive / Meeting notes / User text
                |
     Authorized ingestion (read-only)
                |
     AI extraction (untrusted JSON)
                |
 Schema validation + source evidence
                |
 Priority scoring + routing + deduplication
                |
       Human approval queue
                |
       Asana API write adapter
                |
  Task GID + audit trail + progress polling
                |
    Reports / opt-in notifications
```

## Components
- Ingestion adapters normalize provenance and access level; initially manual JSON import.
- AI engine proposes action items without making API mutations.
- Rules engine validates, scores, flags ambiguity, computes duplicate fingerprints.
- Review interface (to build) accepts explicit approve/reject/edit decisions.
- Asana adapter publishes only approved requests; credential stored server-side.
- Reporting reads Asana with scoped permissions and transparent last-synced timestamps.

## Persistence (proposed)
`source_records`, `task_proposals`, `approval_decisions`, `asana_sync`, `audit_events`.
Use immutable IDs, timestamps, project/assignee mappings and an idempotency key. Store only necessary excerpts; define retention and deletion policies.

## Non-goals for v1
Fully autonomous task creation, unrestricted email scraping, automatic completion, deleting existing tasks, and auto-reassigning people.
