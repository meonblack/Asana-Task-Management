# Asana setup checklist

1. Confirm the Asana workspace/org and the desired projects with an administrator.
2. Read live project GIDs and their sections; do not guess from names.
3. Read users' Asana GIDs and verify email-to-user matching explicitly.
4. Populate `config/project-map.example.json` in a private environment with **verified** IDs.
5. Create a least-privilege access token or OAuth app. Never commit credentials.
6. Test read-only endpoint access and confirm project/section visibility.
7. Test one synthetic task in a designated test project with explicit approval.
8. Test duplicate detection, incorrect assignee, missing due date, and failed API responses.
9. Enable production writes only after review UI/audit trail is complete.

## Known project context
Elevate uses a **Weekly Tasks** Asana project and has used a section named **Leslie**. This repository does not contain or assume a verified Asana GID for either; identify them through the authorized Asana integration.

## Useful API calls
`GET /api/1.0/projects/{project_gid}/sections` and `GET /api/1.0/projects/{project_gid}/tasks` for discovery; `POST /api/1.0/tasks` for approved writes. Follow current Asana API documentation for required fields, rate limits and OAuth/PAT policies.
