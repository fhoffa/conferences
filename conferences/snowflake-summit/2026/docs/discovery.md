# Snowflake Summit 2026 discovery notes

Start here when reverse engineering the catalog.

## Entry point
- https://reg.snowflake.com/flow/snowflake/summit26/sessions/page/catalog

## Questions to answer
- Is session data embedded in HTML, JSON script tags, or fetched after load?
- Is there a public JSON/XHR endpoint behind filters/search?
- Are speakers/session details fetched separately?
- Are pagination and filters server-side or client-side?
- Are there anti-bot/rate-limit constraints to respect?
