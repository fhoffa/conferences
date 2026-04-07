# Session record draft schema

A lightweight cross-conference target shape for normalized session data.

The point is not to force every source into a rigid model immediately.
The point is to define the fields we want to preserve when available, so we do not accidentally lose useful information during scraping and normalization.

## Top-level session fields

- `conference` — canonical conference slug, for example `google-cloud-next`
- `year` — event year
- `session_id` — stable source identifier when available
- `title`
- `abstract`
- `description_raw` — optional original long-form description before cleanup
- `track`
- `subtrack`
- `format` — breakout, keynote, workshop, lab, etc.
- `level` — beginner/intermediate/advanced when exposed
- `topic_tags[]`
- `keywords[]`
- `language`
- `audience`
- `session_code` — human-facing code like BRK123 when present
- `registration_required` — boolean if separately tracked
- `capacity_limited` — boolean if exposed
- `catalog_url` — listing page URL
- `session_url` — detail page URL when present
- `source_url` — canonical source used for the record
- `source_type` — html, json, api, embedded-state, etc.
- `raw_ref` — path or id pointing to stored raw source payload

## Schedule/location fields

- `start_time`
- `end_time`
- `timezone`
- `day`
- `date`
- `duration_minutes`
- `venue`
- `building`
- `room`
- `location_text` — keep original human-readable location too
- `is_virtual`
- `on_demand_available`

## Entity fields

- `speakers[]`
- `companies[]`
- `sponsors[]`

## Speaker object fields

Each speaker entry should preserve as much source detail as possible.

- `speaker_id`
- `name`
- `first_name`
- `last_name`
- `job_title` ← important: we missed this before and want to keep it when available
- `role`
- `company`
- `company_id`
- `bio`
- `profile_url`
- `linkedin_url`
- `twitter_url`
- `image_url`
- `is_employee` — optional inferred/explicit boolean for conference host company
- `source_url`
- `raw_ref`

## Company object fields

- `company_id`
- `name`
- `normalized_name`
- `domain`
- `industry`
- `source_url`
- `raw_ref`

## Optional quality/processing fields

- `scraped_at`
- `normalized_at`
- `parser_version`
- `completeness_score`
- `warnings[]`

## Minimal viable normalized record

If a source is messy, we still want at least:

- `conference`
- `year`
- `session_id` or another stable key
- `title`
- `abstract` or `description_raw`
- `speakers[]` with `name` and `job_title` when available
- `company`/`companies[]` when available
- `start_time` / `end_time` when available
- `source_url`
- `raw_ref`

## Notes

- Preserve source richness first; simplify later.
- Prefer explicit null/missing fields over dropping information silently.
- Keep speaker job title whenever available, even if the rest of the speaker profile is incomplete.
