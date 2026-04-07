# Snowflake Summit 2025 discovery notes

## Entry point
- https://reg.snowflake.com/flow/snowflake/summit25/sessions/page/catalog

## What worked
- The public catalog page is still live.
- Browser network inspection shows the page calling a public RainFocus sessions API:
  - `POST https://events.summit.snowflake.com/api/sessions`
  - headers include public page-observed `rfApiProfileId` and `rfWidgetId`
  - body includes `tab.sessioncatalogtab=1714168666431001NNiH&type=session&catalogDisplay=grid`
- Pagination works by repeating the same request with `from=<offset>`.
- The first request returns a section-wrapped payload; subsequent `from>0` requests return a flatter payload with the same `items` structure.
- The API response includes materially richer public data than the visible-card DOM scrape, including:
  - `sessionID` and `sessionTimeID`
  - clean title and session code
  - HTML abstract
  - times, rooms, UTC timestamps, and duration
  - participant/speaker records with company, title, bio, photo, and social links when present
  - attribute/value groupings such as track, level, day, covered topics, and delivery method

## What did not work cleanly
- Plain HTML fetches mostly reveal the shell plus large translation/config payloads.
- `size=100` did not increase the observed page size beyond 50, so full capture still requires paginated requests.
- The public API appears to return catalog listings, not a perfectly deduplicated session master table; 11 session IDs appeared twice across 568 listings.

## Practical conclusion
A much better public scrape is possible in 2025 than the original visible-card pass. The low-friction path is:
1. call the public catalog sessions API the page already uses
2. paginate with `from=<offset>` until all results are collected
3. normalize the public API fields into a reviewable dataset
4. document clearly that this is a public catalog export, not private/internal data
