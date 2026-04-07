# conferences

A growing repo for scraping and analyzing conference agendas, sessions, speakers, and trends.

This repo is organized so multiple conferences and multiple years can evolve side by side, while keeping each event self-contained enough to work on independently.

## Structure

```text
conferences/
  google-cloud-next/
    2025/
    2026/
  snowflake-summit/
    2026/
  databricks-data-ai-summit/
    2026/
shared/
  schemas/
  lib/
  docs/
```

## Per-event layout

Each conference/year can grow into a self-contained work area with common buckets like:

- `raw/` — captured source payloads, HTML, API responses, exports
- `normalized/` — cleaned session/speaker/company datasets
- `analysis/` — notebooks, summaries, derived outputs
- `site/` — generated pages, charts, or presentation assets
- `scripts/` — event-specific scrapers and transforms
- `docs/` — notes, runbooks, assumptions, quirks

This keeps conferences separate while leaving room for shared helpers later.

## Current focus

- Google Cloud Next 2025 and 2026 imported from the original source project
- Snowflake Summit 2026 now has a working browser-backed catalog capture and normalized session export
- Databricks Data + AI Summit 2026 scaffolded for upcoming scraping work

## Working style

The repo is intentionally starting simple:
- keep conference/year work isolated
- add shared abstractions only after patterns become real
- preserve upstream/source provenance where imports happen
