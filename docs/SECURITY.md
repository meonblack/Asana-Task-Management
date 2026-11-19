# Security and privacy

- Least privilege. Protect Asana tokens, Gmail/Drive credentials and API keys using environment variables or a secrets manager.
- Never include private tokens in a prompt, task description, GitHub issue, log, or telemetry payload.
- Verify task destination permissions before copying email or HR/student/client data to Asana.
- Treat inbound text as untrusted, including prompt injection inside emails and documents.
- Every write requires an explicit, attributable approval; preserve who approved what and when.
- Do not delete or bulk-edit existing tasks in v1.
- Mask sensitive source data and keep minimal snippets and evidence links; implement retention policy.
- Validate webhook signatures if webhooks are added. Apply retries with deduplication for transient failures.
- Review access and revoke exposed credentials immediately.
