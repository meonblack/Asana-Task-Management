# Development roadmap

**Phase 1 — Repository and validation**: skill, prompts, rubrics, JSON schemas, dry-run CLI and tests (included).

**Phase 2 — Asana discovery**: authenticated read-only project, sections, users and task lookup; configure verified mappings.

**Phase 3 — AI extraction**: plug in a model; validate structured responses; source evidence and duplicate search.

**Phase 4 — Human approval**: queue, edit/approve/reject UI, immutable audit log, explicit Asana write service.

**Phase 5 — Monitoring**: scoped reads, weekly reporting, opted-in reminders, rate limits and retry handling.

**Phase 6 — Integrations**: Gmail, Calendar, Drive, optional GoHighLevel, with permission review and production test suite.

### Acceptance checks
No guessed IDs, no silent writes, no duplicate task creation on retries, no task created without confirmed approval, and clear failure/status reporting.
