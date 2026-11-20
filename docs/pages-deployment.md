# Phase 7 — GitHub Pages

One-time setup: repository Settings > Pages > Build and deployment > Source > GitHub Actions. Then run Deploy dashboard to GitHub Pages from Actions. Expected URL: https://yuni-wyx.github.io/neetcode-submissions/ .

Deployment runs on relevant main changes and successful Refresh submission tracker completion (including bot-generated data updates, which do not trigger ordinary push workflows). It checks out latest main, tests, builds and uploads dashboard/dist. No database or secrets required. Local browser records do not leave the device. Site remains public; repository history is already public.

Verify six views, search/filter, log persistence after reload, JSON export/import, and mobile layout. Deployment and browser QA must be confirmed before release sign-off.
