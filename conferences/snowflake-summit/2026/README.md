# Snowflake Summit 2026

Source catalog:
- https://reg.snowflake.com/flow/snowflake/summit26/sessions/page/catalog

## Status

Working public-catalog capture in place.

What exists now:
- browser-backed scraper: `scripts/fetch_catalog.js`
- raw captures: `raw/catalog.html`, `raw/widget_config.json`, `raw/sessions_api.json`
- normalized dataset: `normalized/sessions.json`
- quick summary: `analysis/summary.md`
- reverse-engineering notes: `docs/discovery.md`, `docs/proof-of-scrape.md`, `docs/api-notes.md`

## How to refresh

From the repo root:

```bash
node conferences/snowflake-summit/2026/scripts/fetch_catalog.js
```

Notes:
- The Snowflake catalog is hydrated client-side, so this script uses Playwright/Chromium instead of scraping static HTML only.
- The main catalog currently comes from `POST https://events.summit.snowflake.com/api/sessions` after extracting dynamic RainFocus headers from a live page load.

## Directory guide

- `raw/` — captured HTML/API responses from the Snowflake catalog
- `normalized/` — normalized session records
- `analysis/` — derived summaries and slices
- `site/` — visualizations or generated pages
- `scripts/` — Snowflake-specific scraping/parsing code
- `docs/` — notes about site behavior, endpoints, and reverse engineering
