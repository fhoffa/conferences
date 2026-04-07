# Snowflake Summit 2025

Source catalog:
- https://reg.snowflake.com/flow/snowflake/summit25/sessions/page/catalog

## Status

Public catalog still exists and is scrapeable.

This pass captures the first rendered catalog page from the public RainFocus site and normalizes the visible session cards into a reviewable JSON dataset.

## Notes

- The catalog is client-rendered; plain `curl` is not enough.
- A headless Chromium DOM dump works reliably for the public page.
- This implementation intentionally stays practical: it captures the visible public card data without over-investing in deeper private/internal endpoints.

## Directories

- `normalized/` — normalized session-card records from the public catalog
- `analysis/` — compact summary of what was captured
- `scripts/` — scraper used for the capture
- `docs/` — discovery notes and scrape proof
