# Snowflake Summit 2025 discovery notes

## Entry point
- https://reg.snowflake.com/flow/snowflake/summit25/sessions/page/catalog

## What worked
- The public catalog page is still live.
- Rendering the page with headless Chromium exposes session-card markup in the dumped DOM.
- The rendered DOM includes enough public fields to build a useful normalized capture:
  - session tile id
  - title
  - apparent session code (when present in title)
  - abstract
  - speaker names from avatar `aria-label`s
  - banner image URL

## What did not work cleanly
- Plain HTML fetches mostly reveal the shell plus large translation/config payloads.
- I did not fully reverse engineer a richer bulk API in this pass.

## Practical conclusion
A useful public scrape is still possible in 2025, but the low-friction path is:
1. render the page in headless Chromium
2. parse the visible card markup
3. document the limitation that this is a visible-page capture, not a complete internal export
