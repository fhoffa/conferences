# Proof of scrape

We verified that the Snowflake Summit 2025 public session catalog is still available and can be scraped without login.

Current status:
- proof of public catalog availability: yes
- proof of rendered scrape: yes
- proof of structured extraction: yes
- deeper API reverse engineering: not done in this pass

Evidence collected:
- headless Chromium rendered the public catalog page successfully
- the rendered DOM contained 50 visible session tiles in the captured page state
- those visible tiles were normalized into `normalized/sessions.json`

Scope note:
- this is intentionally a practical, reviewable public capture of visible catalog cards
- it should be treated as a solid starting point, not a guaranteed full-fidelity export of every session and hidden field in RainFocus
