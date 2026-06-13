# Mirrored-bar chart data — Snowflake vs Databricks 2026

**Source catalogs (fresh):** `normalized/current/sessions.json`, captured **2026-06-13**
**Denominators:** Databricks **802** sessions · Snowflake **537** sessions
**Reproduce:** `python3 classify.py` → writes `chart_data.json` + this CSV (`databricks_snowflake_mirrored_bar_chart_data.csv`)

Agenda share = sessions matching the row ÷ that vendor's total sessions. Rows are
independent topic prevalences (a session can match several rows), so columns do
**not** sum to 100%. Counts are whole sessions — no fractional crediting is applied.

| # | Row | Databricks signal | DBX sessions | DBX share | Snowflake signal | SNOW sessions | SNOW share | Leader | Δ (pp) |
|---|-----|-------------------|-------------:|----------:|------------------|-------------:|-----------:|--------|-------:|
| 1 | Cortex / GenAI app layer | Mosaic AI / Agent Bricks / Genie | 414 | 51.6% | Cortex agents + AI functions | 370 | 68.9% | **Snowflake** | 17.3 |
| 2 | Semantic context for agents | Metric Views / semantic models | 34 | 4.2% | Semantic Views | 113 | 21.0% | **Snowflake** | 16.8 |
| 3 | Sharing / marketplace / clean rooms | Delta Sharing + Marketplace | 110 | 13.7% | Secure Sharing + Marketplace + Clean Rooms | 97 | 18.1% | **Snowflake** | 4.3 |
| 4 | Iceberg / open-lakehouse interoperability | Iceberg / Uniform / open formats | 48 | 6.0% | Iceberg + Polaris + interoperability | 154 | 28.7% | **Snowflake** | 22.7 |
| 5 | Unity Catalog vs Horizon control plane | Unity Catalog | 450 | 56.1% | Horizon Catalog | 68 | 12.7% | **Databricks** | 43.4 |
| 6 | BI dashboards / metrics / AI-BI | AI/BI dashboards | 298 | 37.2% | BI & Analytics | 79 | 14.7% | **Databricks** | 22.4 |
| 7 | App / operational database substrate | Lakebase / app database substrate | 206 | 25.7% | Snowflake Postgres + Unistore / app-data bridge | 92 | 17.1% | **Databricks** | 8.6 |
| 8 | Evals / red teaming / AI quality (strict) | eval/benchmark/red-team/guardrail | 90 | 11.2% | eval/benchmark/red-team/guardrail | 23 | 4.3% | **Databricks** | 6.9 |
| 9 | Lakeflow / Spark / streaming pipelines | Lakeflow / Spark / streaming | 279 | 34.8% | Snowpipe + Openflow + Snowpark + dbt | 194 | 36.1% | **Snowflake** | 1.3 |
| 10 | SQL warehouse / lakehouse modernization | Databricks SQL / DW modernization | 347 | 43.3% | Gen2 warehouses + migrations | 200 | 37.2% | **Databricks** | 6.0 |

## Reading the split

- **Snowflake leads (5 rows):** GenAI app layer, semantic context, sharing/marketplace,
  Iceberg/open-lakehouse, and pipelines (by a hair).
- **Databricks leads (5 rows):** named control plane, BI/AI-BI, operational-DB substrate,
  evals, and warehouse/modernization.
- **Decisive deltas (>20pp):** Unity Catalog vs Horizon (43.4pp, DBX), Iceberg/open
  (22.7pp, SNOW), BI/AI-BI (22.4pp, DBX).
- **Near-ties (<5pp):** pipelines (1.3pp), sharing/marketplace (4.3pp) — claim no clear
  leader here.

See `AUDITS.md` for the fairness caveats that qualify several of these deltas (especially
rows 4, 5, and 7).
