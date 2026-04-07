# AI term comparison across GCP Next, Databricks, and Snowflake (2026)

This view uses **percentage of sessions mentioning each term**, not raw counts, so conference size differences do not dominate the chart.

## Method note
- Snowflake and Databricks percentages are computed directly from cleaned session title/description text.
- GCP percentages are derived from the repo's own processed `topWords.all` / `sessionCount` pipeline in `media/insights-summary.json`, because the imported raw `sessions/sessions.json` is empty in this repo snapshot.
- So GCP is using the conference's documented internal word-stats path rather than ad-hoc re-parsing.

## Percent of sessions mentioning each term
### GCP Next 2026
- AI: 71.7% (757 / 1056)
- Agents: 44.7% (472 / 1056)
- MCP: 0.0% (0 / 1056)
- Models: 0.0% (0 / 1056)
- LLMs: 0.0% (0 / 1056)
- GenAI: 0.0% (0 / 1056)

### Databricks 2026
- AI: 58.9% (93 / 158)
- Agents: 29.7% (47 / 158)
- MCP: 4.4% (7 / 158)
- Models: 30.4% (48 / 158)
- LLMs: 8.2% (13 / 158)
- GenAI: 10.1% (16 / 158)

### Snowflake 2026
- AI: 66.5% (212 / 319)
- Agents: 32.9% (105 / 319)
- MCP: 2.8% (9 / 319)
- Models: 21.3% (68 / 319)
- LLMs: 2.5% (8 / 319)
- GenAI: 4.4% (14 / 319)

