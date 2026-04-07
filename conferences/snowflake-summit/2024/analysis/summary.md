# Snowflake Summit 2024 catalog snapshot

- source catalog: https://reg.snowflake.com/flow/snowflake/summit24/sessions/page/catalog
- source sessions API: https://events.summit.snowflake.com/api/sessions
- source detail API: https://reg.snowflake.com/flow/common/sessions/bysessionids
- captured catalog listings: 541
- unique session IDs captured: 527
- duplicate session IDs across catalog listings: 14
- sessions API page count: 11
- sessions API page size observed: 50
- detail batches fetched: 14
- detail records fetched: 527
- normalized sessions written: 527
- sessions with speaker links: 524
- total speaker links: 1050
- sessions with public files/images: 5
- observed rfApiProfileId: jWSnSt8ustaXKDVcwqQQLUZm1wv0MJXQ
- observed rfWidgetId: 4aLWfToCldcgSpYjdX6h5k5NWghuMQ2Q

## What this capture is

This is a public browser-backed RainFocus capture for Snowflake Summit 2024. It uses the same unauthenticated catalog API the public page calls, then enriches deduplicated session IDs through the public `flow/common/sessions/bysessionids` endpoint observed from the same page context.

## Why this is the practical depth limit

- The main catalog API is enough to enumerate the full public catalog and speaker/time metadata.
- The `bysessionids` endpoint adds useful public fields like session files/images and slightly richer detail records, but it requires a live `rfcsrf` token from a browser session.
- Beyond that, secondary RainFocus endpoints are better treated as optional follow-up rather than a stable deeper export path.

## Sessions by type
- Breakout Session: 270
- Theater Session: 198
- Hands-On Lab: 25
- Activity: 24
- Dev Day Luminary Talk: 6
- Keynote: 4
