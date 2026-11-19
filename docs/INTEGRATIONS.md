# Integration contracts

## Gmail
Consent and read scopes first. Normalize: message/thread IDs, timestamp, author, subject, excerpt and link. Avoid full message storage and skip newsletters unless explicitly configured.

## Google Calendar
Normalize event ID, organizer, local start/end, timezone, attendees and link. Calendar events alone are not evidence of task assignment; use notes or agreed decisions.

## Google Drive
Use scoped access and document IDs; respect folder permissions and link restrictions. Extract action items from documents only if asked.

## Meetings
Accept user-supplied transcript/notes; preserve speaker and timestamps where possible; distinguish proposed action from confirmed ownership.

## Asana
Read projects/sections/users and tasks; write only with approval. Record response GID/permalink and server timestamp. Handle 401/403/429/5xx without duplicate posting.

## GoHighLevel (optional)
CRM lead/contact references may be linked to Asana tasks by opaque IDs. Do not mirror private CRM contact details into broadly accessible tasks.
