# Databricks scraper notes

## Working approach

Databricks exposes enough public structure to scrape without browser automation:

1. fetch agenda pages (`/dataaisummit/agenda?page=N`)
2. extract session detail slugs from agenda markup
3. fetch each session detail page
4. parse embedded `__NEXT_DATA__` JSON
5. normalize into a shared session shape

## Why this is good

- public and simple
- structured speaker records available
- speaker `job_title` is exposed when present in source
- no special auth or JS runtime needed for the current path

## Current limitation

Some schedule fields appear blank on certain session pages (`day`, `start_time`, `end_time`).
That likely means either:
- those records are not fully scheduled yet, or
- the richer agenda listing has fields not repeated on detail pages

If we want full timing completeness later, we should inspect whether another listing payload or endpoint carries the schedule fields more consistently.
