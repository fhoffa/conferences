# conferences

A growing repo for scraping and analyzing conference agendas, sessions, speakers, and trends.

This repo starts by importing the existing Google Cloud Next work and reorganizing it into a structure that can grow across:

- multiple conferences
- multiple years per conference
- separate scrapers and analysis pipelines per event/year when needed

## Structure

```text
conferences/
  google-cloud-next/
    2025/
    2026/
```

## Current contents

### `conferences/google-cloud-next/2026/`
Imported from the original `google-cloud-next-2026-unofficial-scrape` project.
Contains the current Google Cloud Next 2026 scraping, enrichment, analysis, website, and media artifacts.

### `conferences/google-cloud-next/2025/`
Contains the existing Google Cloud Next 2025 data and scripts that previously lived under `next2025/` in the original repo.

## Direction

The idea is to keep each conference/year self-contained enough that future work can add:

- `google-cloud-next/2027`
- other events like `kubecon/2026`, `ces/2027`, etc.
- event-specific scrapers where sites differ significantly
- shared tooling later, once patterns become clear

For now, this is intentionally simple: preserve the existing work, separate it by year, and make room for expansion.
