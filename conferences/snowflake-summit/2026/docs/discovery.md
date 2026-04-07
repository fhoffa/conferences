# Snowflake Summit 2026 discovery notes

Start here when reverse engineering the catalog.

## Entry point
- https://reg.snowflake.com/flow/snowflake/summit26/sessions/page/catalog

## Findings
- Static HTML alone is not enough for the real catalog payload.
- The page hydrates client-side and then calls public APIs.
- Main catalog data comes from:
  - `POST https://events.summit.snowflake.com/api/sessions`
- Widget/config bootstrap comes from:
  - `POST https://events.summit.snowflake.com/api/widgetConfig`
- Supporting keynote/detail calls also hit RainFocus endpoints such as:
  - `GET /flow/common/sessions/byattributevalue?...`
  - `GET /flow/common/sessions/bysessionids?...`

## Constraints discovered
- Bare calls to `events.summit.snowflake.com/api/sessions` fail with `Required parameter missing: apiProfile` unless the browser-observed RainFocus headers are present.
- RainFocus `flow/common/sessions/*` endpoints also expect `rfcsrf` and return `error.api.invalid.csrf.token` without it.

## Practical answer
A reliable scraper needs a real browser session (or equivalent) to observe the dynamic request headers and then replay the session catalog API. That workflow is now implemented in `../scripts/fetch_catalog.js`.
