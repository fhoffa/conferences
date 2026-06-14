# Mirrored-bar chart data — Snowflake vs Databricks 2026

**Source catalogs:** pinned `normalized/snapshots/2026-06-13.sessions.json`, captured **2026-06-13**
**Denominators:** Databricks **802** sessions · Snowflake **537** sessions
**Reproduce:** `python3 classify.py` → writes `chart_data.json` + this CSV (`databricks_snowflake_mirrored_bar_chart_data.csv`)

**Primary method: full-text fractional agenda allocation.** Each row applies the **same**
keyword set (concept terms + every vendor's product names) to both vendors over the full public
title+abstract. A session receives one unit of agenda credit total; if it matches `k` tracked rows,
each row receives `1/k` credit. This preserves the full catalog descriptions while reducing the
long-abstract effect where one session touches many rows. Binary prevalence and capped-text runs
are kept in `chart_data.json` as audits.

Matched tracked rows: Databricks **716 / 802** sessions; Snowflake **432 / 537** sessions.
Multi-topic sessions: Databricks **509**; Snowflake **265**.

| # | Row | Databricks signal | DBX credit | DBX touched | DBX share | Snowflake signal | SNOW credit | SNOW touched | SNOW share | Leader | Δ (pp) |
|---|-----|-------------------|-----------:|------------:|----------:|------------------|------------:|-------------:|-----------:|--------|-------:|
| 1 | Cortex / GenAI app layer | Mosaic AI / Agent Bricks / Genie | 190.1 | 394 | 23.7% | Cortex agents + CoWork | 149.1 | 254 | 27.8% | **Snowflake** | 4.1 |
| 2 | Semantic context for agents | Metric Views | 18.3 | 47 | 2.3% | Semantic Views / Cortex Analyst | 23.3 | 60 | 4.3% | Snowflake | 2.1 |
| 3 | Sharing / marketplace / clean rooms | Delta Sharing + Marketplace | 18.8 | 44 | 2.4% | Secure Sharing + Marketplace + Clean Rooms | 19.0 | 37 | 3.5% | tie / lean SNOW | 1.2 |
| 4 | Open lakehouse / table formats | Delta Lake + UniForm (+ Iceberg) | 44.7 | 114 | 5.6% | Iceberg + Polaris | 24.6 | 54 | 4.6% | tie / lean DBX | 1.0 |
| 5 | Governance / control plane | Governance / lineage / access | 137.1 | 294 | 17.1% | Governance / lineage / access | 76.7 | 150 | 14.3% | Databricks | 2.8 |
| 6 | BI dashboards / metrics / AI-BI | AI/BI dashboards | 42.0 | 116 | 5.2% | BI & Analytics / Snowsight | 18.4 | 41 | 3.4% | Databricks | 1.8 |
| 7 | App / operational database substrate | Lakebase / app database substrate | 64.0 | 126 | 8.0% | Snowflake Postgres + Unistore / app-data bridge | 12.9 | 26 | 2.4% | **Databricks** | 5.6 |
| 8 | Evals / red teaming / AI quality (strict) | eval / benchmark / red-team | 37.8 | 90 | 4.7% | eval / benchmark / red-team | 9.8 | 23 | 1.8% | Databricks | 2.9 |
| 9 | Lakeflow / Spark / streaming pipelines | Lakeflow / Spark / streaming | 120.1 | 267 | 15.0% | Snowpipe + Openflow + Snowpark + dbt | 73.1 | 137 | 13.6% | tie / lean DBX | 1.4 |
| 10 | SQL warehouse / lakehouse modernization | Databricks SQL / Photon | 43.1 | 99 | 5.4% | Gen2 warehouses + migrations | 25.0 | 53 | 4.7% | tie | 0.7 |

## Reading The Split

- **No blowouts.** Full-text fractional allocation produces one clear row-level gap:
  operational DB substrate (Databricks +5.6pp). Everything else is a lean or near-tie.
- **Snowflake's primary leans** are the **AI app layer** (+4.1pp) and **semantic context**
  (+2.1pp). GenAI stays Snowflake-positive under fractional caps, even though binary full-text
  prevalence flips slightly toward Databricks.
- **Databricks' primary leans** are **operational DB** (+5.6pp), **evals** (+2.9pp), and
  **governance/control plane** (+2.8pp), with smaller leans in BI, pipelines, open formats, and
  warehouse modernization.
- **Binary prevalence is a different question:** it asks whether a session touches a topic at all.
  On full text, binary prevalence is much more Databricks-heavy because Databricks abstracts touch
  more rows per session. That is useful as reach/audit data, not the primary agenda-allocation
  chart.

## Sensitivity

Fractional allocation is stable across full text, Databricks-median cap, and Snowflake-median cap:

| Row | Full text fractional | 991-char fractional | 680-char fractional | Full text binary |
|---|---|---|---|---|
| GenAI app layer | SNOW +4.1 | SNOW +4.0 | SNOW +3.4 | DBX +1.8 |
| Semantic context | SNOW +2.1 | SNOW +2.0 | SNOW +2.2 | SNOW +5.3 |
| Sharing / marketplace | SNOW +1.2 | SNOW +1.2 | SNOW +1.2 | SNOW +1.4 |
| Open formats | DBX +1.0 | DBX +0.7 | DBX +0.4 | DBX +4.2 |
| Governance / control plane | DBX +2.8 | DBX +2.6 | DBX +0.6 | DBX +8.7 |
| BI / AI-BI | DBX +1.8 | DBX +1.8 | DBX +1.7 | DBX +6.8 |
| Operational DB substrate | DBX +5.6 | DBX +5.6 | DBX +5.2 | DBX +10.9 |
| Evals / red teaming | DBX +2.9 | DBX +2.8 | DBX +1.7 | DBX +6.9 |
| Pipelines / streaming | DBX +1.4 | DBX +1.3 | DBX +0.9 | DBX +7.8 |
| SQL modernization | DBX +0.7 | DBX +0.6 | DBX +0.5 | DBX +2.5 |

Use the primary chart for agenda allocation. Use binary prevalence to say “topic reach,” not
“share of agenda attention.”
