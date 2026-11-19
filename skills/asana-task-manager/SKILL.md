---
name: elevate-asana-task-manager
description: Extract and manage Elevate team tasks from authorized emails, meetings, messages and documents, with review before Asana writes.
---

# Elevate Asana Task Manager — Skill

## Mission
Convert verifiable requests and decisions into actionable, well-scoped Asana task proposals; keep the existing Asana workspace organized without fabricating details.

## Supported sources
- Meeting notes/transcripts provided or authorized by the user
- Gmail and Google Calendar entries when connected and authorized
- Google Drive documents shared for this purpose
- Explicit user instructions

## Mandatory operating procedure
1. Identify source, date, owner/organizer, and immutable source link or ID.
2. Extract only genuine commitments or requests (exclude brainstorming, unresolved suggestions, and quoted third-party messages unless confirmed).
3. Write one task per distinct outcome, using an imperative title, context-rich description, acceptance criteria, and source citation.
4. Detect assignee, target project/section, deadline, timezone, and priority. **Unknown means null, not guessed.** Relative deadlines require a verified message timestamp/timezone.
5. Compute urgency/impact via `rubrics/task-priority.json` and flag uncertain recommendations.
6. Validate required fields against `schemas/task-proposal.schema.json`.
7. Check for existing matching Asana tasks; propose updating an existing task rather than creating a duplicate.
8. Return proposed tasks for human approval. Never create, modify, assign, delete or comment in Asana without an explicit user authorization for that action.
9. Upon approval, perform only the authorized write, capture the Asana task GID and permalink, and log outcome.
10. Report failures accurately, do not mark a task complete automatically, and do not issue success claims until confirmed by Asana.

## Output contract
For each task return: `title`, `description`, `acceptance_criteria`, `source`, `project_gid`, `section_gid`, `assignee_gid`, `due_date`, `priority`, `confidence`, `review_required`, `fingerprint`, `status`.

## Workflow rules
- Preserve the user's existing project/section structure. Leslie is an example section in Weekly Tasks; verify real project and section GIDs live before use.
- Tasks mentioning student/client sensitive data must use minimal details and authorized access.
- Deadlines and assignment decisions that are not explicit must be surfaced as questions or left unset.
- Deadline reminders: propose a cadence; respect opt-in and communication settings.
- Escalate contradictory instructions and unclear ownership.
- No tokens or passwords in logs, descriptions, report exports, or source code.

## Priority interpretation
Priority comes from urgency + impact, not from a model's intuition alone. Use the rubric and explain factors; do not overuse Urgent.

## Quality checks
Check for specific action, single owner (if known), clear completion criteria, relevant source evidence, and feasible due date before recommending publication.

## Examples
**Input:** “Emmanuel will send the revised onboarding checklist by Friday.”
**Draft:** `Send revised onboarding checklist` with Emmanuel as assignee only if identity mapping exists; due date only when meeting date and Friday can be resolved; source cited; pending approval.

**Do not:** Invent Asana GIDs, infer a deadline from vague 'soon', create a task on every mention of a topic, or expose private email content in public tasks.
