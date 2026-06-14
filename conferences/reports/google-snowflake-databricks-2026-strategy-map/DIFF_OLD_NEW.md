# Old-vs-new diff — does the refresh change any claim?

**Method:** the *same* primary classifier (full-text fractional symmetric keywords) run
against both the old **2026-06-02** snapshots (DBX 759 / SNOW 550) and the **2026-06-13**
snapshots (DBX 802 / SNOW 537). Because the method is held constant, any movement reflects **data
drift**, not classifier drift. Reproduce: `python3 diff_old_new.py`.

Δ is signed in **percentage points, Databricks − Snowflake** (positive = Databricks ahead).

| Row | old Δ | new Δ | moved | leader |
|---|---:|---:|---:|---|
| Cortex / GenAI app layer | −1.5 | −4.1 | −2.6 | Snowflake (stable) |
| Semantic context for agents | −2.1 | −2.1 | +0.0 | Snowflake (stable) |
| Sharing / marketplace / clean rooms | −1.2 | −1.2 | +0.0 | Snowflake (small lean, stable) |
| Open lakehouse / table formats | +1.1 | +1.0 | −0.1 | near-tie |
| Governance / control plane | +3.2 | +2.8 | −0.4 | Databricks (lean, stable) |
| BI / AI-BI | +1.7 | +1.8 | +0.1 | Databricks (lean, stable) |
| App / operational DB substrate | +4.9 | +5.6 | +0.7 | Databricks (stable) |
| Evals / red teaming (strict) | +2.3 | +2.9 | +0.6 | Databricks (lean, stable) |
| Lakeflow / Spark / streaming | +1.4 | +1.4 | +0.0 | near-tie |
| SQL warehouse / modernization | +0.9 | +0.7 | −0.2 | near-tie |

## Verdict

**No material change.** Across all 10 rows:
- **Zero leader flips.**
- **No delta moved ≥ 5 pp.** Largest move is GenAI (−2.6), widening slightly in Snowflake's
  favour but staying a modest lead.
- The largest gaps (operational DB +5.6, GenAI −4.1, evals +2.9, governance +2.8) are all stable
  to within ~3 pp. Only operational DB clears 5 pp.

**Implication:** the strategy narrative is robust to the 759→802 / 550→537 refresh. Every
published claim survives; none needs re-litigating on the new data. The watch items are the
**near-ties** — open formats (+1.0), pipelines (+1.4), warehouse (+0.7), and sharing (−1.2) —
which stay within noise on both bases and are correctly described as ties/leans, not wins.
