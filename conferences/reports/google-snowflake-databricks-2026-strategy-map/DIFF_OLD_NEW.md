# Old-vs-new diff — does the refresh change any claim?

**Method:** the *same* classifier (`classify.ROWS`, length-controlled symmetric keywords) run
against both the old **2026-06-02** snapshots (DBX 759 / SNOW 550) and the **2026-06-13**
snapshots (DBX 802 / SNOW 537). Because the method is held constant, any movement reflects **data
drift**, not classifier drift. Reproduce: `python3 diff_old_new.py`.

Δ is signed in **percentage points, Databricks − Snowflake** (positive = Databricks ahead).

| Row | old Δ | new Δ | moved | leader |
|---|---:|---:|---:|---|
| Cortex / GenAI app layer | −1.3 | −4.7 | −3.4 | Snowflake (stable) |
| Semantic context for agents | −6.6 | −6.4 | +0.2 | Snowflake (stable) |
| Sharing / marketplace / clean rooms | −2.5 | −2.7 | −0.2 | Snowflake (lean, stable) |
| Open lakehouse / table formats | +0.5 | +0.4 | −0.1 | tie |
| Governance / control plane | −0.6 | −0.9 | −0.3 | tie |
| BI / AI-BI | +4.2 | +3.8 | −0.4 | Databricks (lean, stable) |
| App / operational DB substrate | +7.5 | +8.3 | +0.8 | Databricks (stable) |
| Evals / red teaming (strict) | +1.7 | +2.9 | +1.2 | Databricks (lean, stable) |
| Lakeflow / Spark / streaming | +1.9 | +1.4 | −0.5 | tie |
| SQL warehouse / modernization | +0.4 | +0.1 | −0.3 | tie |

## Verdict

**No material change.** Across all 10 rows:
- **Zero leader flips.**
- **No delta moved ≥ 5 pp.** Largest move is GenAI (−3.4), widening slightly in Snowflake's
  favour but staying a modest lead.
- The largest gaps (operational DB +8.3, semantic −6.4, GenAI −4.7) are all stable to within
  ~3 pp. No gap on the board exceeds ~8 pp.

**Implication:** the strategy narrative is robust to the 759→802 / 550→537 refresh. Every
published claim survives; none needs re-litigating on the new data. The watch items are the
**ties** — open formats (+0.4), pipelines (+1.4), warehouse (+0.1) — which stay within noise on
both bases and are correctly described as ties, not wins.
