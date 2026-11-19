# Workflows

## W1 — Meeting to Action
Trigger: authorized meeting notes or transcript. Extract decisions and assigned actions → validate → dedupe → approval → Asana creation → optional recap.

## W2 — Email to Task
Trigger: user-selected thread or scoped inbox triage. Classify requests → evidence-backed draft → reviewer chooses Create/Skip/Link existing → approved Asana task.

## W3 — Weekly Tasks intake
Trigger: authorized staff request. Map to verified Weekly Tasks project and appropriate section; prefer explicit assignee. Missing GIDs prevent publishing.

## W4 — Deadline reminders
Trigger: scheduled scan of approved Asana tasks. Suppress completed tasks and repeat notifications; generate draft for approved channel and cadence.

## W5 — Weekly performance report
Trigger: configured weekly reporting schedule. Read Asana tasks → aggregate by project/assignee/status → cite task permalinks → send only after report recipients verified.

## Failure paths
Unresolved identity, missing deadline, access forbidden, duplicate match, model confidence low, unauthorized request, API timeout: hold for manual review. Do not silently continue.
