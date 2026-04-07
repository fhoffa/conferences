# Proof of scrape

We verified that the Snowflake Summit 2025 public session catalog is still available and can be scraped without login.

Current status:
- proof of public catalog availability: yes
- proof of deeper public API path: yes
- proof of structured paginated extraction: yes
- proof of first-page-only visible-card limitation being superseded: yes

Evidence collected:
- browser network inspection showed the catalog calling `POST https://events.summit.snowflake.com/api/sessions`
- the request paginates successfully with `from=<offset>`
- the public API yielded 568 catalog listings across 12 pages
- those listings normalized into `normalized/sessions.json`
- the dataset spans 557 unique session IDs, with 11 IDs repeated because some catalog listings represent separate time slots

Scope note:
- this is a public catalog API capture, not a private attendee or admin export
- it should be treated as a substantially better public dataset than the original visible-card scrape, while still respecting the limits of what the public API exposes
