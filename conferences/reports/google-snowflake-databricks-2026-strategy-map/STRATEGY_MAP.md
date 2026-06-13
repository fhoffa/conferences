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
around it** (Unity Catalog, Lakebase, BI, evals). Under the fair method (length-controlled
symmetric keywords; `AUDITS.md §0`) Databricks leads 7 of 10 rows by emphasis, but only **one**
gap is decisive — Unity Catalog (+15pp). Snowflake's real leads are the GenAI app layer (+4.7)
and the semantic layer (+6.4); everything else is a modest lean or a tie.

---

## Where Snowflake's agenda leans in

- **Semantic context for agents (11.2% vs 4.7%, +6.4).** Snowflake's clearest real lead.
  **Semantic Views / Cortex Analyst** are a Snowflake headline (its own Summit domain); Databricks'
  Metric Views language is a footnote. If agents-need-a-semantic-layer is the thesis, Snowflake is
  selling it harder *on the agenda* — though the gap is ~6pp, not the ~17pp the taxonomy draft
  showed.
- **GenAI / agent app layer (46.4% vs 41.6%, +4.7).** Snowflake edges it — but both conferences
  are heavily agent-focused, so this is a slim *prominence* lean, not the rout (69% vs 52%) the
  taxonomy draft implied. The earlier gap was a Snowflake-covered-topic artifact.
- **Sharing / marketplace / clean rooms (6.5% vs 3.9%, +2.7) — a lean, not a lead.**

## Where Databricks' agenda leans in

- **Unity Catalog vs Horizon (19.7% vs 4.7%, +15.0).** The **only decisive gap on the board.**
  Unity Catalog is named in ~1 in 5 Databricks sessions; Horizon in ~5% of Snowflake's. **Frame
  as named-control-plane prominence** — broad governance is strong on both sides (`AUDITS.md §1`).
- **App / operational DB substrate (13.1% vs 4.8%, +8.3).** Databricks leads on **branding and
  concentration** — Lakebase gets its own track plus a heavy Databricks Apps push. Snowflake is
  **not absent**: Native Apps + Streamlit + Snowflake Postgres carry a real app-on-data story
  (`AUDITS.md §3`).
- **BI / AI-BI (10.8% vs 7.1%, +3.8) — a lean.** First-party AI/BI (Genie + dashboards) beats
  Snowflake's dashboard presence, but by ~4pp, not the 22pp the taxonomy draft showed (AI/BI-tag
  artifact). Snowflake cedes dashboards to Streamlit/partners by design.
- **Evals / red teaming (6.9% vs 3.9%, ~1.8×) — narrow.** Both ship it (Snowflake via
  TruEra/TruLens); only Databricks foregrounds the mechanics (`AUDITS.md §7`).

## Where it's effectively a tie

- **Open lakehouse / table formats (10.5% vs 10.1%).** Equal airtime — Databricks on Delta,
  Snowflake on Iceberg (`AUDITS.md §2`).
- **Pipelines / streaming (26.6% vs 25.1%).** Lakeflow/Spark vs Snowpipe/Openflow/Snowpark/dbt.
- **SQL warehouse / modernization (~10% each, +0.1).** Both deep; dead heat.

## Side callouts

- **NVIDIA changed tables.** Jensen Huang keynoted Snowflake Summit 2024; in 2026 NVIDIA has
  **0** speaking sessions at Snowflake and **2** at Databricks, and Snowflake's marquee AI
  fireside went to **Anthropic** instead. **Both still have real NVIDIA partnerships** (H100 +
  Photon at Databricks; NeMo/NIM in Cortex at Snowflake) — so this is about *stage billing*, not
  the partnership: Snowflake's headline AI guest moved from the chip vendor to the model lab,
  while NVIDIA presents at the platform that sells raw compute (`AUDITS.md §4`).
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

**Classification method — length-controlled symmetric keywords (`AUDITS.md §0`).** The **same**
keyword set (concept terms + every vendor's product names) is applied to **both** vendors, over
each session's title+abstract **capped at 680 characters**. This replaces an earlier draft that
mixed each vendor's native taxonomy (Databricks `topic_tags`/`track`, Snowflake `attributes`)
with keywords — those taxonomies differ in breadth and silently inflated whichever side had the
broader tag, in both directions. The cap neutralises Databricks' ~1.45× longer abstracts (median
991 vs 680 chars), which otherwise over-credit it on raw keyword counts. Net effect: margins are
~3× smaller than the taxonomy draft and four rows are ties; the directional thesis survives.

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
