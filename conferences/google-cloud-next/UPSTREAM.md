# Google Cloud Next upstream tracking

This directory was bootstrapped from the original repo:

- Upstream repository: `https://github.com/fhoffa/google-cloud-next-2026-unofficial-scrape`
- Imported on: `2026-04-07`
- Upstream commit at import: `2e92b36e1711ff1607baaf970c1879205a41d199`

## Import mapping

- Upstream repo root → `conferences/google-cloud-next/2026/`
- Upstream `next2025/` → `conferences/google-cloud-next/2025/`

## Sync notes

When the upstream repo changes, use this file to compare against the recorded commit and decide what to bring over.

Suggested refresh flow:

1. Fetch the latest upstream repo state.
2. Compare upstream changes since `2e92b36e1711ff1607baaf970c1879205a41d199`.
3. Copy relevant updates into the matching year folder.
4. If upstream adds cross-year/shared logic, decide whether it belongs in:
   - `conferences/google-cloud-next/<year>/`, or
   - a future shared utilities area.
5. Update this file with the new imported commit after each sync.

## Why this exists

The original Google Cloud Next work may keep evolving in its source repo. This file makes that relationship explicit so the `conferences` repo can stay in sync intentionally instead of relying on memory.
