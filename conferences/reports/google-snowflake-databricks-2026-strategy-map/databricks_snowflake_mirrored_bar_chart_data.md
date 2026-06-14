# Mirrored-bar chart data — Snowflake vs Databricks 2026

**Source catalogs:** pinned `normalized/snapshots/2026-06-13.sessions.json`, captured **2026-06-13**
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
| 5 | Governance / control plane | Governance / lineage / access | 214 | 26.7% | Governance / lineage / access | 148 | 27.6% | tie | 0.9 |
| 6 | BI dashboards / metrics / AI-BI | AI/BI dashboards | 87 | 10.8% | BI & Analytics / Snowsight | 38 | 7.1% | Databricks | 3.8 |
| 7 | App / operational database substrate | Lakebase / app database substrate | 105 | 13.1% | Snowflake Postgres + Unistore / app-data bridge | 26 | 4.8% | **Databricks** | 8.3 |
| 8 | Evals / red teaming / AI quality (strict) | eval / benchmark / red-team | 55 | 6.9% | eval / benchmark / red-team | 21 | 3.9% | Databricks | 2.9 |
| 9 | Lakeflow / Spark / streaming pipelines | Lakeflow / Spark / streaming | 213 | 26.6% | Snowpipe + Openflow + Snowpark + dbt | 135 | 25.1% | tie | 1.4 |
| 10 | SQL warehouse / lakehouse modernization | Databricks SQL / Photon | 80 | 10.0% | Gen2 warehouses + migrations | 53 | 9.9% | tie | 0.1 |

## Reading the split

- **No decisive gaps under the 680-char chart.** The agendas are remarkably close — **no topic gap
  exceeds ~8pp.** The biggest is the **operational-DB substrate** (+8.3, Databricks). These are
  cap-sensitive topic-emphasis reads; see sensitivity below.
- **Snowflake's 680-char leads** are the **AI app layer** (+4.7 under the primary cap) and the
  **semantic layer** (+6.4). Semantic is stable across caps; GenAI should be phrased as
  cap-dependent because it flips to a small Databricks lean when the cap is relaxed.
- **Databricks' real leads** are the **operational-DB substrate** (+8.3); plus narrower edges on
  BI (+3.8) and evals (+2.9) — the "governed system" half (selling the build).
- **Genuine ties (<2pp):** governance/control plane (0.9), open lakehouse/formats (0.4), pipelines
  (1.4), warehouse (0.1). Claim no leader.
- **Leans (2–4pp), not wins:** sharing/marketplace (SNOW +2.7), BI (DBX +3.8), evals (DBX +2.9).
- **Brand-name caveat (row 5):** governance *coverage* is a tie, but Databricks **names** its
  catalog far more — "Unity Catalog" appears in 19.6% of its sessions vs "Horizon" in 4.7% of
  Snowflake's. That's brand prominence, not governance volume (`AUDITS.md §1`).

Margins here are ~3× smaller than the earlier taxonomy-based draft, which overstated both
vendors' leads. The directional thesis survives; the dominance did not. See `AUDITS.md §0` for
the methodology change and §1–2 for the rows it most affected.

## Cap sensitivity

Same symmetric keyword matcher, changing only the title+abstract cap:

| Row | 680-char primary | 991-char sensitivity | Full-text sensitivity |
|---|---|---|---|
| GenAI app layer | SNOW +4.7 | DBX +0.5 | DBX +1.8 |
| Semantic context | SNOW +6.4 | SNOW +5.3 | SNOW +5.3 |
| Sharing / marketplace | SNOW +2.7 | SNOW +1.5 | SNOW +1.4 |
| Open formats | DBX +0.4 | DBX +3.4 | DBX +4.2 |
| Governance / control plane | SNOW +0.9 | DBX +7.5 | DBX +8.7 |
| BI / AI-BI | DBX +3.8 | DBX +6.5 | DBX +6.8 |
| Operational DB substrate | DBX +8.3 | DBX +10.7 | DBX +10.9 |
| Evals / red teaming | DBX +2.9 | DBX +6.3 | DBX +6.9 |
| Pipelines / streaming | DBX +1.4 | DBX +6.8 | DBX +7.8 |
| SQL modernization | DBX +0.1 | DBX +1.9 | DBX +2.5 |

Use the primary chart for the fair length-controlled visualization, but qualify cap-dependent
claims (especially GenAI and governance) as "under the 680-char method."
