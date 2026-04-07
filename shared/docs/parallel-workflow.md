# Parallel conference workflow

This repo is set up so conferences can be developed in parallel without stepping on each other.

## Principle

Keep each conference/year mostly self-contained while discovery is still messy.

That means separate:
- source captures
- parsing scripts
- normalized outputs
- documentation of site quirks

## Suggested branch strategy

Examples:
- `snowflake-summit/initial-scraper`
- `snowflake-summit/catalog-capture`
- `databricks-data-ai-summit/agenda-capture`
- `databricks-data-ai-summit/session-normalization`

## Concurrency rules

1. Prefer editing only one conference subtree per branch when possible.
2. Put cross-conference utilities under `shared/` only when at least two conferences need them.
3. Keep raw captures inside the relevant event/year folder.
4. Document oddities and blockers in the event's `docs/` folder.

## Why this matters

Snowflake and Databricks will almost certainly expose different site structures and data-loading patterns. The best early move is to keep them parallel but decoupled.
