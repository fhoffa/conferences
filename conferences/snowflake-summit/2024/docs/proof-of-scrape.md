# Proof of scrape

We verified that the Snowflake Summit 2024 public session catalog is still available and can be captured without login.

Current status:
- proof of public catalog availability: yes
- proof of deeper public API path: yes
- proof of secondary public detail enrichment: yes
- proof of structured repeatable extraction: yes

Evidence committed in this tree:
- `raw/catalog.html`
- `raw/widget_config.json`
- `raw/sessions_api.json`
- `raw/session_details.json`
- `normalized/sessions.json`
- `analysis/summary.md`

Scope note:
- this is a public catalog + public detail capture from unauthenticated browser traffic
- it does not claim attendee-only or admin-only access
- the detail endpoint still depends on browser-observed public tokens, so the scripted approach keeps that browser step explicit
