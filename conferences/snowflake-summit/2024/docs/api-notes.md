# Snowflake Summit 2024 catalog API notes

- page: https://reg.snowflake.com/flow/snowflake/summit24/sessions/page/catalog
- main catalog API: POST https://events.summit.snowflake.com/api/sessions
- widget config API: POST https://events.summit.snowflake.com/api/widgetConfig
- secondary detail API: GET https://reg.snowflake.com/flow/common/sessions/bysessionids
- observed rfApiProfileId: jWSnSt8ustaXKDVcwqQQLUZm1wv0MJXQ
- observed rfWidgetId: 4aLWfToCldcgSpYjdX6h5k5NWghuMQ2Q
- observed workflowApiToken: snowflake.summit24.sessions

## Required browser-observed headers/tokens
- `rfApiProfileId`
- `rfWidgetId`
- `rfcsrf` (for `flow/common/sessions/bysessionids`)

## Main catalog request body
```
tab.sessioncatalogtab=1714168666431001NNiH&type=session&browserTimezone=America/Los_Angeles&catalogDisplay=grid
```

## Practical conclusion
- The public catalog is still deeply scrapable in 2024.
- The best practical path is: observe public browser headers/tokens, paginate `api/sessions`, then batch-enrich unique session ids through `flow/common/sessions/bysessionids`.
- Treat the detail endpoint as opportunistic public enrichment rather than a guaranteed stable contract.
