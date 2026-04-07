# Proof of scrape

We now have a repeatable browser-backed capture for the public Snowflake Summit 2026 session catalog.

Current status:
- proof of capture: yes
- proof of structured extraction: yes
- detail-page/API reverse engineering: enough for main catalog; secondary RainFocus detail endpoints are optional follow-up

Evidence committed in this tree:
- `raw/catalog.html`
- `raw/widget_config.json`
- `raw/sessions_api.json`
- `normalized/sessions.json`
- `analysis/summary.md`

What changed versus the earlier partial state:
- the richer JSON/API path is now identified and used
- the main catalog payload currently returns 319 sessions
- normalized output now includes stable ids, session codes, titles, abstracts, speakers, times, rooms, and attribute buckets

Remaining nice-to-haves:
- dedicated normalized filter taxonomy output
- deeper per-session enrichment if Snowflake later exposes more detail via secondary endpoints
