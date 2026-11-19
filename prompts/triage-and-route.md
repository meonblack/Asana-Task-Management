# Prompt — Prioritize and route

Given validated task proposals, a verified Asana project/section directory, and `rubrics/task-priority.json`, recommend urgency/impact scores and routing. Do not invent project GIDs, section GIDs, or people IDs. If multiple matches exist, leave null and request reviewer selection. Provide a one-sentence explanation for each recommended priority. Mark everything `pending_review`. Do not call the Asana API.
