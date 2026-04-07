# Snapshot policy

Databricks outputs should be stored as dated snapshots so future refreshes can be compared cleanly.

## Structure

- `normalized/snapshots/YYYY-MM-DD.sessions.json`
- `normalized/snapshots/YYYY-MM-DD.summary.json`
- `analysis/snapshots/YYYY-MM-DD.top_words.json`
- `analysis/snapshots/YYYY-MM-DD.top_words_by_track.json`

Optional convenience copies may live under:

- `normalized/current/`
- `analysis/current/`

These are for easy access only. The dated snapshots are the canonical history.

## Raw captures

`raw/` is gitignored by default.

Reason:
- raw HTML can be bulky and noisy
- normalized and analysis snapshots are what we most want to diff over time
- raw can still be generated locally when needed during debugging
