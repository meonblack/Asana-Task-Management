# Elevate Asana Task Management — AI-Assisted Starter

A review-first system for turning meeting notes, emails, messages and Google Drive documents into organized Asana tasks. It extracts action items, recommends assignees and due dates, checks duplicates, and generates progress reports.

> **Status:** starter repository. No live connectors or unattended automations are configured. By default, commands are dry-run and require explicit approval before any task is written to Asana.

## Core workflow
1. Ingest authorized content from Gmail, Calendar, Drive or meeting notes.
2. AI drafts structured action items with **source evidence**.
3. Validate each draft, assign priority according to `rubrics/task-priority.json`, and flag uncertainties.
4. Human reviewer confirms project, assignee, deadline and content.
5. Publish approved tasks to Asana; avoid duplicates using deterministic fingerprints.
6. Monitor changes and prepare reminders/reports within approved access boundaries.

## Repository map
- `skills/asana-task-manager/SKILL.md`: AI operating procedures.
- `rubrics/`: priority and task-quality scoring rules (not academic grading).
- `prompts/`: extraction, triage and reporting instructions.
- `schemas/`: data contracts for proposed tasks and approvals.
- `docs/`: architecture, setup, permissions, safety, workflow designs, deployment roadmap.
- `config/`: configuration templates; replace placeholders using verified Asana IDs.
- `src/`: small dependency-free reference library and CLI (dry-run by default).
- `tests/`: standard library unit tests.

## Quick start
```bash
python -m unittest discover -s tests -v
python -m src.cli examples/sample-input.json
```
To enable Asana API publishing later, copy `.env.example` into your local secrets manager, configure valid IDs, and implement a reviewed action gate. **Never commit an access token**.

## Required integrations (planned)
- Asana API: target projects/sections, members, task creation, status.
- Google Workspace: Gmail/Calendar/Drive with minimal read scopes.
- Optional GoHighLevel: CRM-linked task references; not required to launch.
- AI model: extraction and summaries; treat model output as untrusted drafts.

## Definition of done for first deployment
Tests pass; permissions and task routing verified; sample tasks reviewed manually; duplicate prevention tested; audit records retained; no automatic writes without approval.
