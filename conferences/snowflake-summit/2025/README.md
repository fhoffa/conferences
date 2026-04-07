# Snowflake Summit 2025

Source catalog:
- https://reg.snowflake.com/flow/snowflake/summit25/sessions/page/catalog

## Status

Public catalog still exists and exposes a deeper public RainFocus sessions API behind the browser catalog.

This pass captures the paginated public catalog API results and normalizes them into a reviewable JSON dataset.

## Notes

- The public catalog page calls `https://events.summit.snowflake.com/api/sessions`.
- Pagination works through repeated requests with `from=<offset>`; the observed page size is 50.
- This capture produced 568 public catalog listings spanning 557 unique session IDs.
- A small number of session IDs appear more than once because the catalog can list multiple time slots separately.
- The dataset only includes fields exposed by the public catalog API; it does not claim attendee-only or admin-only access.

## Directories

- `normalized/` — normalized session records from the public catalog API
- `analysis/` — compact summary of what was captured
- `scripts/` — scraper used for the capture
- `docs/` — discovery notes and scrape proof
