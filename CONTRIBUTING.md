# Contributing

1. Create an issue summarizing the change and any privacy implications.
2. Add tests for parsing/scoring/deduplication and make all external calls mockable.
3. Keep credentials, real contact data, transcripts and student/client records out of commits.
4. Maintain reviewer approval for all Asana writes; do not weaken the default dry-run mode.
5. Update relevant docs and example config before requesting review.

Run `python -m unittest discover -s tests -v` before committing.
