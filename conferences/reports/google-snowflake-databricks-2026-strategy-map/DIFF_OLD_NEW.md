# Old-vs-new diff — does the refresh change any claim?

**Method:** the *same* classifier (`classify.ROWS`) run against both the old
**2026-06-02** snapshots (DBX 759 / SNOW 550) and the current **2026-06-13** catalogs
(DBX 802 / SNOW 537). Because the method is held constant, any movement reflects **data
drift**, not classifier drift. Reproduce: `python3 diff_old_new.py`.

Δ is signed in **percentage points, Databricks − Snowflake** (positive = Databricks ahead).

| Row | old Δ | new Δ | moved | leader |
|---|---:|---:|---:|---|
| Cortex / GenAI app layer | −17.4 | −17.3 | +0.1 | Snowflake (stable) |
| Semantic context for agents | −16.3 | −16.8 | −0.5 | Snowflake (stable) |
| Sharing / marketplace / clean rooms | −4.1 | −4.3 | −0.2 | Snowflake (lean, stable) |
| Iceberg / open-lakehouse | −22.6 | −22.7 | −0.1 | Snowflake (stable) |
| Unity Catalog vs Horizon | +46.8 | +43.4 | −3.4 | Databricks (stable) |
| BI / AI-BI | +25.6 | +22.4 | −3.2 | Databricks (stable) |
| App / operational DB substrate | +9.6 | +8.6 | −1.0 | Databricks (stable) |
| Evals / red teaming (strict) | +5.6 | +6.9 | +1.3 | Databricks (stable) |
| Lakeflow / Spark / streaming | −0.1 | −1.3 | −1.2 | tie → slight Snowflake |
| SQL warehouse / modernization | +8.4 | +6.0 | −2.4 | Databricks (stable) |

## Verdict

**No material change.** Across all 10 rows:
- **Zero leader flips.**
- **No delta moved ≥ 5 pp.** Largest moves are Unity Catalog (−3.4) and BI (−3.2), both
  *narrowing* slightly while staying decisive Databricks leads.
- The two largest gaps on the board (Unity Catalog +43–47, Iceberg −22 to −23) are stable
  to within ~3 pp.

**Implication:** the strategy narrative in `STRATEGY_MAP.md` is robust to the 759→802 /
550→537 refresh. Every published claim survives; none needs re-litigating on the new data.
The only watch item is the **pipelines** row, which was a dead-heat tie on the old basis
(−0.1) and is now a hair toward Snowflake (−1.3) — still correctly described as a tie.
