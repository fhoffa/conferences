# Session record draft schema

A lightweight cross-conference target shape for normalized session data.

## Core fields

- `conference`
- `year`
- `session_id`
- `title`
- `abstract`
- `track`
- `format`
- `level`
- `speakers[]`
- `companies[]`
- `tags[]`
- `start_time`
- `end_time`
- `timezone`
- `location`
- `source_url`
- `source_type`
- `raw_ref`

## Notes

This is intentionally loose for now.
Different conferences may not expose all fields, and some fields may need mapping later.
The goal is just to give Snowflake and Databricks a common landing shape once we start normalizing.
