# Snowflake Summit 2024

Source catalog:
- https://reg.snowflake.com/flow/snowflake/summit24/sessions/page/catalog

## Status

Working public-catalog capture in place.

What exists now:
- browser-backed scraper: `scripts/fetch_catalog.js`
- raw captures: `raw/catalog.html`, `raw/widget_config.json`, `raw/sessions_api.json`, `raw/session_details.json`
- normalized dataset: `normalized/sessions.json`
- quick summary: `analysis/summary.md`
- reverse-engineering notes: `docs/discovery.md`, `docs/proof-of-scrape.md`, `docs/api-notes.md`

## How to refresh

From the repo root:

```bash
node conferences/snowflake-summit/2024/scripts/fetch_catalog.js
```

Notes:
- The public page is browser-hydrated, so the script uses Playwright/Chromium instead of relying on static HTML alone.
- The main catalog comes from `POST https://events.summit.snowflake.com/api/sessions`.
- The deepest practical public enrichment found here is `GET /flow/common/sessions/bysessionids`, replayed with a browser-observed `rfcsrf` token from the same page session.

## Directory guide

- `raw/` — captured HTML/API responses from the public catalog
- `normalized/` — normalized session records
- `analysis/` — derived summaries and slices
- `scripts/` — Snowflake-specific scraping/parsing code
- `docs/` — notes about site behavior, endpoints, and reverse engineering
