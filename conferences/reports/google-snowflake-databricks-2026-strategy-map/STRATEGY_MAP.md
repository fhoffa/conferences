# Snowflake vs Databricks 2026 — strategy map

**Catalogs:** Snowflake Summit 2026 (537 sessions) vs Databricks Data + AI Summit 2026
(802 sessions), public agendas captured **2026-06-13**.
**Companion files:** `chart.svg` (mirrored bar), `databricks_snowflake_mirrored_bar_chart_data.md`
(data table), `AUDITS.md` (fairness audits), `VENDOR_POSITIONING_SOURCES.md` (cited vendor
self-positioning per row), `DIFF_OLD_NEW.md` (old-vs-new stability check),
`classify.py` / `gen_chart.py` (reproducible).

Every number below is recomputed against the fresh **802 / 537** denominators — the prior
working draft used **759 / 550** and must not be quoted. Only claims that survive the new
data are stated here.

> **The one principle that keeps this fair:** every number measures **session-agenda
> emphasis** — what each vendor chose to schedule — **not shipped capability**. A big delta
> means one vendor *talks about* something more, not that the other *can't do* it.
> `VENDOR_POSITIONING_SOURCES.md` cites each vendor's own product pages so no row is misread
> as absence. The corrections that matter most: **NVIDIA** (Snowflake has a real Cortex+NVIDIA
> partnership), **open table formats** (count Delta Lake — it's open-source too — and Databricks
> actually leads; Snowflake only leads the *Iceberg* word), **BI** (Snowflake cedes dashboards to
> Streamlit/partners *by design*), and **evals** (Snowflake ships TruEra/TruLens AI Observability).

---

## The one-line story

Both vendors now run the *same* play — an AI/agent layer on top of a governed lakehouse —
but they foreground different halves of it. **Snowflake's agenda is louder on the AI app
surface and the meaning layer** (Cortex, Semantic Views, the neutral Iceberg format).
**Databricks' agenda is louder on the governed substrate and the analyst/operational tooling
around it** (Unity Catalog, AI/BI, Lakebase, evals). Databricks leads 6 of 10 rows by emphasis
(four of them narrowly), but the *decisive* gaps are balanced 2–2: Unity Catalog and AI/BI for
Databricks; the GenAI app layer and the semantic layer for Snowflake.

---

## Where Snowflake's agenda leans in

- **GenAI app layer (68.9% vs 51.6%).** Cortex agents + AI functions + CoWork/CoCo
  saturate the Snowflake agenda; more than two of every three sessions touch the GenAI app
  layer. Databricks' Mosaic AI / Agent Bricks / Genie story is large too (over half the
  agenda) — this is a *prominence* gap, not a capability gap.
- **Semantic context for agents (21.0% vs 4.2%).** The single sharpest asymmetry in
  Snowflake's favor. **Semantic Views** are a headline (113 sessions); Databricks' Metric
  Views / semantic-model language is a footnote (34, only 18 saying "metric view"). If
  agents-need-a-semantic-layer is the thesis, Snowflake is selling it far harder *on the
  agenda*.
- **The neutral Iceberg format (8.4% vs 4.0%) — but not open formats overall.** Snowflake
  brands Apache Iceberg + Polaris ~2× more — its bet on the *industry-neutral* table format.
  **But count Delta (also open-source) and the gap inverts:** open table formats touch 14.2%
  of Databricks' agenda vs 10.1% of Snowflake's, because Delta Lake (11.6% vs 0.4%) is
  everywhere on the Databricks stage. So row 4 actually *leans Databricks* — this is a
  which-format difference (house vs neutral), **not** open-vs-closed. (See `AUDITS.md §2`.)
- **Sharing / marketplace / clean rooms (18.1% vs 13.7%) — narrow, <5pp.** Call it a lean,
  not a lead.

## Where Databricks' agenda leans in

- **Unity Catalog vs Horizon (56.1% vs 12.7%).** The largest delta on the board (43.4pp).
  Unity Catalog is the gravitational center of the Databricks agenda; Horizon is a contained
  single feature. **Frame as named-control-plane prominence** — broad governance is strong
  on both sides (`AUDITS.md §1`).
- **BI / AI-BI (37.2% vs 14.7%).** AI/BI (Genie + dashboards) is a much larger labeled
  presence than Snowflake's BI & Analytics track. (Tightened to exclude the bare "analytics"
  keyword and the Databricks SQL tag, which belong to the warehouse row.)
- **App / operational DB substrate (25.7% vs 17.1%).** Databricks leads on **branding and
  concentration** — Lakebase gets its own track plus a heavy Databricks Apps push. Snowflake
  is **not absent**: Native Apps (36) + Streamlit (35) + Snowflake Postgres/Hybrid Tables
  preview carry a real app-on-data story (`AUDITS.md §3`).
- **Evals / red teaming (11.2% vs 4.3%).** Strict eval/benchmark/red-team/guardrail language
  is ~2.6× more common on Databricks' agenda. Narrow claim only — broad trust/quality talk
  is common on both sides (`AUDITS.md §7`).
- **SQL warehouse / modernization (43.3% vs 37.2%) — modest, 6pp.** Both are deep here;
  Databricks edges it.

## Where it's effectively a tie

- **Pipelines / streaming (34.8% vs 36.1%, 1.3pp).** Lakeflow/Spark vs
  Snowpipe/Openflow/Snowpark/dbt — dead heat. Do not claim a leader.

## Side callouts

- **NVIDIA / accelerated compute:** Databricks 12 sessions (incl. an NVIDIA-partnered talk)
  vs Snowflake 3 incidental model-serving mentions. **Both have real NVIDIA partnerships** —
  Databricks foregrounds raw GPU compute (H100, Photon, serverless GPUs), Snowflake abstracts
  it behind managed Cortex inference (NeMo/NIM/Triton). The gap is emphasis, not absence
  (`AUDITS.md §4`).
- **Shared companies:** ~85 companies speak at both summits — dominated by the model labs
  (OpenAI, Anthropic), the GSI bench (Accenture, Deloitte, EY), and the modern-data-stack
  ecosystem (dbt Labs, Fivetran, Atlan) (`AUDITS.md §5`).

---

## Appendix — methodology

**Denominators.** Databricks 802, Snowflake 537 — the `session_count` from each catalog's
`normalized/current/summary.json`, captured 2026-06-13. These replace the prior draft's
759 / 550.

**Timing asymmetry.** The catalogs are at different lifecycle stages: **Snowflake Summit 2026**
already ran (June 1–4) so its agenda is final and its ~26 announcements are public;
**Databricks DAIS 2026** is upcoming (June 15–18, two days after capture) so its 802-session
agenda is forward-looking and not all announcements have dropped. Both are published agendas,
so the comparison holds — but read Databricks' as a forward agenda and Snowflake's as settled.

**What a "row" measures.** Each of the 10 rows is a binary topic membership test applied to
every session. **Agenda share = matching sessions ÷ that vendor's total sessions.** Rows are
**independent overlapping prevalences, not a partition** — a session can match several rows
(e.g., a Cortex-agent-over-Iceberg talk counts in rows 1 and 4). Columns therefore do **not**
sum to 100%.

**Raw vs fractional.** All rows are reported as **whole session counts**. No fractional
session crediting is applied anywhere in this build, so there are no "fractional session
credit" rows to label. (The TODO permits fractional only when a row *explicitly* uses
fractional agenda share; none here do.)

**Classification method.** Vendor-native taxonomy first, keyword backstop second:
- *Databricks:* `track`, `topic_tags` (Unity Catalog, AI/BI, Databricks Agents, Databricks
  SQL, Lakeflow, Lakebase, Databricks Apps, Genie, Delta Sharing, Data Marketplace), then
  title+abstract keywords.
- *Snowflake:* `attributes` → Session Tracks, Covered Topics, Covered Features (Cortex
  Agents, Semantic Views, Apache Iceberg, Horizon Catalog, Secure Data Sharing, Snowflake
  Postgres, Native Apps, Streamlit, Snowpipe/Dynamic Tables, etc.), then title+abstract
  keywords.

This is reproducible: `python3 classify.py` regenerates `chart_data.json` and the CSV;
`python3 gen_chart.py` regenerates `chart.svg`.

**Caveats and fairness guards (full detail in `AUDITS.md`).**
1. *Named-product prominence ≠ conceptual coverage.* Big deltas on rows 5 (Unity Catalog)
   and 2 (Semantic Views) reflect how dominant a *named brand* is in the agenda, not the
   presence/absence of the underlying capability.
2. *Open table formats (row 4) count Delta and Iceberg equally* — both are open-source — and
   the row is kept separate from the governance control plane (row 5). Databricks leads open
   formats overall (Delta); Snowflake leads the neutral Iceberg format. Not open-vs-closed.
3. *"Missing" means absent from current catalog signals* — not absent as a customer,
   partner, or user. Company overlap is speaker affiliation only.
4. *Evals (row 8) is strict* — eval/benchmark/red-team/guardrail only, deliberately
   excluding broad trust/quality language.
5. *BI (row 6) excludes the bare "analytics" keyword* (which over-matched 121 Snowflake
   sessions) and the Databricks SQL tag (counted under warehouse, row 10), keeping the two
   sides symmetric.

**Final fairness check (pre-publication).** Re-read before quoting: no row claims a vendor
*lacks* a capability where the catalog shows a counter-story; near-ties (rows 3, 9) are
labeled as leans/ties, not wins; the operational-DB row stays combined with vendor-specific
labels per the TODO's explicit instruction.
