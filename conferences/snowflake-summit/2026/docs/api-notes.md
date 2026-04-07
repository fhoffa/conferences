# Snowflake Summit 2026 catalog API notes

- page: https://reg.snowflake.com/flow/snowflake/summit26/sessions/page/catalog
- main catalog API: POST https://events.summit.snowflake.com/api/sessions
- widget config API: POST https://events.summit.snowflake.com/api/widgetConfig
- observed rfApiProfileId: ghKgUWZvlHrGVucBmFxaVccUkK8g0AuF
- observed rfWidgetId: Vh7SEIGH0Gsepgj327Z71LzPA2mggVoZ

## Required headers
- `rfApiProfileId`
- `rfWidgetId`
- browser-like `referer` / `user-agent`

## Main catalog request body
```
type=session&browserTimezone=America/Los_Angeles&catalogDisplay=grid
```

## Notes
- Static HTML is not enough; the real catalog is hydrated client-side.
- The public catalog returned 319 sessions during this capture.
- A raw `requests.post()` without the observed RainFocus headers returns `Required parameter missing: apiProfile`.
- Some RainFocus `flow/common/sessions/*` endpoints also expect CSRF (`rfcsrf`) and are better treated as secondary/detail endpoints.
