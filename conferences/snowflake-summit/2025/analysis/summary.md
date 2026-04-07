# Snowflake Summit 2025 catalog API summary

- source catalog: https://reg.snowflake.com/flow/snowflake/summit25/sessions/page/catalog
- source sessions API: https://events.summit.snowflake.com/api/sessions
- paginated catalog listings captured: 568
- unique session IDs captured: 557
- duplicate session IDs across multiple catalog listings: 11
- pages fetched: 12
- API page size observed: 50
- sessions with at least one speaker: 549
- average speakers per listing: 1.87

## What this capture is

This is a deeper public RainFocus API capture of the Snowflake Summit 2025 catalog, using the same unauthenticated session API that the public catalog page calls in the browser. It is materially more complete than a first-page DOM scrape.

## Remaining limits

- The public API returns catalog listings, which means a small number of session IDs appear more than once when the catalog lists multiple time slots separately.
- This pass only captures fields present on the public catalog API response. It does not claim access to private attendee-only or admin-only fields.
- The API headers (`rfApiProfileId`, `rfWidgetId`) were observed from public browser traffic and could rotate in the future.

## Most common attribute groups

- Session Type: present on 568 listings
- Hide From Catalog: present on 568 listings
- Day: present on 568 listings
- Session Catalog Tab: present on 568 listings
- Time: present on 568 listings
- Session Start Time: present on 566 listings
- Covered Topics: present on 527 listings
- Recommendations (Rule Based): present on 527 listings
- Technical Level: present on 521 listings
- Session Tracks: present on 519 listings

## First five titles

- Advanced Training: Fresh Snow, ACT103
- Beginner Training: Snowflake Foundations, ACT102
- Data for Good Hackathon, OS203
- GROUP BY US - Central, M01
- “Show Me The Money” - How To Measure The Business Impact of AI Investments
, EC02
