# Mirrored-bar chart data — Snowflake vs Databricks 2026

**Source catalogs (fresh):** `normalized/current/sessions.json`, captured **2026-06-13**
**Denominators:** Databricks **802** sessions · Snowflake **537** sessions
**Reproduce:** `python3 classify.py` → writes `chart_data.json` + this CSV (`databricks_snowflake_mirrored_bar_chart_data.csv`)

**Method (length-controlled symmetric keywords).** Each row applies the **same** keyword set
(concept terms + every vendor's product names) to **both** vendors, over each session's
title+abstract **capped at 680 characters** (Databricks abstracts run ~1.45× longer, which
otherwise inflates its keyword hits). This replaces an earlier taxonomy-based method that
silently inflated margins in both directions — see `AUDITS.md §0`. Agenda share = matching
sessions ÷ that vendor's total. Rows overlap, so columns do **not** sum to 100%.

| # | Row | Databricks signal | DBX sessions | DBX share | Snowflake signal | SNOW sessions | SNOW share | Leader | Δ (pp) |
|---|-----|-------------------|-------------:|----------:|------------------|-------------:|-----------:|--------|-------:|
| 1 | Cortex / GenAI app layer | Mosaic AI / Agent Bricks / Genie | 334 | 41.6% | Cortex agents + CoWork | 249 | 46.4% | **Snowflake** | 4.7 |
| 2 | Semantic context for agents | Metric Views | 38 | 4.7% | Semantic Views / Cortex Analyst | 60 | 11.2% | **Snowflake** | 6.4 |
| 3 | Sharing / marketplace / clean rooms | Delta Sharing + Marketplace | 31 | 3.9% | Secure Sharing + Marketplace + Clean Rooms | 35 | 6.5% | Snowflake | 2.7 |
| 4 | Open lakehouse / table formats | Delta Lake + UniForm (+ Iceberg) | 84 | 10.5% | Iceberg + Polaris | 54 | 10.1% | tie | 0.4 |
| 5 | Unity Catalog vs Horizon control plane | Unity Catalog | 158 | 19.7% | Horizon Catalog | 25 | 4.7% | **Databricks** | 15.0 |
| 6 | BI dashboards / metrics / AI-BI | AI/BI dashboards | 87 | 10.8% | BI & Analytics / Snowsight | 38 | 7.1% | Databricks | 3.8 |
| 7 | App / operational database substrate | Lakebase / app database substrate | 105 | 13.1% | Snowflake Postgres + Unistore / app-data bridge | 26 | 4.8% | **Databricks** | 8.3 |
| 8 | Evals / red teaming / AI quality (strict) | eval / benchmark / red-team | 55 | 6.9% | eval / benchmark / red-team | 21 | 3.9% | Databricks | 2.9 |
| 9 | Lakeflow / Spark / streaming pipelines | Lakeflow / Spark / streaming | 213 | 26.6% | Snowpipe + Openflow + Snowpark + dbt | 135 | 25.1% | tie | 1.4 |
| 10 | SQL warehouse / lakehouse modernization | Databricks SQL / Photon | 80 | 10.0% | Gen2 warehouses + migrations | 53 | 9.9% | tie | 0.1 |

## Reading the split

- **Only one decisive gap:** Unity Catalog vs Horizon (**+15.0pp, Databricks**) — the named
  control plane is the single clearest divergence on the board.
- **Snowflake's real leads** are the **AI app layer** (+4.7) and the **semantic layer** (+6.4) —
  modest but consistent; this is the "legibility / meaning" half of the story.
- **Databricks' real leads** are the **named control plane** (+15.0) and the **operational-DB
  substrate** (+8.3); plus narrower edges on BI (+3.8) and evals (+2.9) — the "operability" half.
- **Genuine ties (<2pp):** open lakehouse/formats (0.4), pipelines (1.4), warehouse (0.1). Claim
  no leader.
- **Leans (2–4pp), not wins:** sharing/marketplace (SNOW +2.7), BI (DBX +3.8), evals (DBX +2.9).

Margins here are ~3× smaller than the earlier taxonomy-based draft, which overstated both
vendors' leads. The directional thesis survives; the dominance did not. See `AUDITS.md §0` for
the methodology change and §1–2 for the rows it most affected.
