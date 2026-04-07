# Snowflake Summit 2024 discovery notes

## Entry point
- https://reg.snowflake.com/flow/snowflake/summit24/sessions/page/catalog

## What worked
- The public catalog page is still live and accessible without login.
- Browser network inspection shows the page calling a public RainFocus sessions API at `POST https://events.summit.snowflake.com/api/sessions`.
- That API paginates with `from=<offset>` and exposes the full public catalog, including times, rooms, speaker records, and attribute buckets.
- The same live page also calls `GET /flow/common/sessions/bysessionids` with a valid `rfcsrf` token, and that endpoint can be replayed to enrich deduplicated session ids.

## What did not work cleanly
- Static HTML alone does not expose the RainFocus request headers used by the public JSON APIs.
- The detail endpoint depends on a live `rfcsrf` token from the browser session, so bare replay without a prior browser step is brittle.

## Practical conclusion
The deepest practical public path for Snowflake Summit 2024 is browser-backed: observe headers/tokens from the public catalog, paginate the public catalog API, then optionally enrich the deduplicated session ids via `bysessionids` from the same page session. That is implemented in `../scripts/fetch_catalog.js`.
