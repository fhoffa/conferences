# Proof of scrape

We captured the public Snowflake Summit 2026 session catalog HTML and extracted five sample session records from the visible catalog markup.

Current status:
- proof of capture: yes
- proof of structured extraction: partial
- detail-page/API reverse engineering: still needed

Why partial:
- the RainFocus catalog clearly renders public session content, but the richer JSON/API path was not yet fully reverse engineered in this pass.
- this sample proves we can capture and parse visible session entries; a follow-up should extract stable IDs, speaker data, and richer metadata from the underlying event endpoints.
