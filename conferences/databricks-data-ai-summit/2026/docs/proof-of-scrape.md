# Proof of scrape

We captured the public Databricks Data + AI Summit 2026 agenda and extracted five sample session records into normalized JSON.

Current status:
- proof of capture: yes
- proof of structured extraction: yes
- speaker job titles captured: yes, when available in source

Method:
- discover session links from the public agenda page
- fetch individual session pages
- parse embedded `__NEXT_DATA__` JSON
- map fields into the draft normalized session shape
