# GitHub submission import

Source: [neetcode-submissions](https://github.com/yuni-wyx/neetcode-submissions), now the combined repository. NeetCode owns the submission folder; tracker metadata and Markdown live separately.

- `data/submissions.json` is generated snapshot metadata.
- Count distinct existing submission files, never maximum suffix plus one or total commits.
- Sync timestamps are GitHub author dates, not original solve times (especially bulk sync).
- Source may sync accepted-only or all statuses; acceptance cannot be inferred. Removed/unsynced submissions are not counted.
- `data/attempts.json` is separate, manually evidenced practice sessions; repeated submissions/debugging in one session are not necessarily additional attempts.
- Familiarity stays unknown until assessed. Catalog mapping and review UI follow in later phases.

Snapshot: 61 unique slugs, 102 files at 9205db658196c2552fb531207b83edb8bb22b3b6.
