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
> is effectively tied; Snowflake only leads the *Iceberg* word), **BI** (Snowflake cedes dashboards to
> Streamlit/partners *by design*), and **evals** (Snowflake ships TruEra/TruLens AI Observability).

---

## The one-line story

Both vendors now run the *same* play — an AI/agent layer on top of a governed lakehouse — and the
full-text fractional agenda view says the contrast is real but not a blowout. Snowflake leans
toward the **AI app surface** (+4.1pp) and **semantic context** (+2.1pp). Databricks leans toward
the **operational-DB substrate** (Lakebase, +5.6pp, the board's biggest), with smaller edges in
evals (+2.9pp) and governance/control plane (+2.8pp). Binary topic reach is more Databricks-heavy,
but the fractional chart is the better read of agenda attention because each session gets one
unit of credit split across all rows it touches.

---

## Where Snowflake's agenda leans in

- **GenAI / agent app layer (27.8% vs 23.7%, +4.1pp fractional agenda credit).** Snowflake puts
  slightly more of its tracked agenda attention into the AI app surface. Binary full-text
  prevalence flips narrowly toward Databricks, so the honest wording is a Snowflake
  *allocation* lean, not a universal GenAI lead.
- **Semantic context for agents (4.3% vs 2.3%, +2.1pp fractional agenda credit).** Snowflake's
  meaning-layer lean is smaller under fractional allocation than under binary prevalence, but it
  survives every sensitivity check.
  **Semantic Views / Cortex Analyst** are a Snowflake headline (its own Summit domain); Databricks'
  Metric Views language is a footnote. If agents-need-a-semantic-layer is the thesis, Snowflake is
  selling it harder *on the agenda* — though the gap is modest, not the ~17pp the taxonomy draft
  showed.
- **Sharing / marketplace / clean rooms (3.5% vs 2.4%, +1.2pp) — a small lean, not a lead.**

## Where Databricks' agenda leans in

- **App / operational DB substrate (8.0% vs 2.4%, +5.6pp) — the board's largest gap.** Databricks
  leads on **branding and concentration** — Lakebase gets its own track plus a heavy Databricks
  Apps push. Snowflake is **not absent**: Native Apps + Streamlit + Snowflake Postgres carry a
  real app-on-data story (`AUDITS.md §3`).
- **Evals / red teaming (4.7% vs 1.8%, +2.9pp) — a narrow but real mechanics lean.** Both ship it
  (Snowflake via TruEra/TruLens); Databricks foregrounds it more (`AUDITS.md §7`).
- **Governance / control plane (17.1% vs 14.3%, +2.8pp).** Fractional allocation gives Databricks
  a modest topic-attention lean, while the eye-catching "Unity Catalog vs Horizon" gap (20% vs
  5%) remains **brand naming**, not governance absence at Snowflake (`AUDITS.md §1`).
- **BI / AI-BI (5.2% vs 3.4%, +1.8pp) — a small lean.** First-party AI/BI (Genie + dashboards)
  beats Snowflake's dashboard presence, but by far less than the 22pp taxonomy draft showed (AI/BI-tag
  artifact). Snowflake cedes dashboards to Streamlit/partners by design.

## Where it's effectively a tie

- **Open lakehouse / table formats (5.6% vs 4.6%, +1.0pp Databricks).** Effectively equal airtime
  — Databricks on Delta,
  Snowflake on Iceberg (`AUDITS.md §2`).
- **Pipelines / streaming (15.0% vs 13.6%, +1.4pp Databricks).** Lakeflow/Spark vs
  Snowpipe/Openflow/Snowpark/dbt.
- **SQL warehouse / modernization (5.4% vs 4.7%, +0.7pp Databricks).** Both deep; dead heat.

## Side callouts

- **Snowflake's marquee AI guest changed from NVIDIA to Anthropic.** The normalized Snowflake
  speaker-company field shows 0 NVIDIA breakout affiliations in 2024-2026, but the 2024 catalog
  still contains NVIDIA evidence (Bryan Catanzaro in `AI241`, Jensen Huang in keynote `K1`, plus
  BioNeMo / NeMo Retriever / accelerated-infrastructure mentions). So the safe read is narrower:
  in 2026, NVIDIA disappears from Snowflake breakout speaker/company signals while Anthropic gets
  the marquee AI slot — and NVIDIA presents working sessions at Databricks. Both still have real
  NVIDIA partnerships (`AUDITS.md §4`).
- **Shared companies:** ~85 companies speak at both summits — dominated by the model labs
  (OpenAI, Anthropic), the GSI bench (Accenture, Deloitte, EY), and the modern-data-stack
  ecosystem (dbt Labs, Fivetran, Atlan) (`AUDITS.md §5`).

---

## Appendix — methodology

**Denominators.** Databricks 802, Snowflake 537 — loaded from the pinned
`normalized/snapshots/2026-06-13.sessions.json` files. These replace the prior draft's
759 / 550.

**Timing asymmetry.** The catalogs are at different lifecycle stages: **Snowflake Summit 2026**
already ran (June 1–4) so its agenda is final and its ~26 announcements are public;
**Databricks DAIS 2026** is upcoming (June 15–18, two days after capture) so its 802-session
agenda is forward-looking and not all announcements have dropped. Both are published agendas,
so the comparison holds — but read Databricks' as a forward agenda and Snowflake's as settled.

**What a "row" measures.** Each of the 10 rows is a topic matcher applied to the full public
title+abstract. A session can match several rows. For the primary chart, each session receives
one unit of agenda credit total; if it matches `k` tracked rows, each row receives `1/k` credit.
**Agenda share = fractional session credit ÷ that vendor's total sessions.** Unmatched sessions
stay outside the 10 tracked rows rather than being forced into a topic bucket.

**Binary prevalence vs fractional allocation.** `chart_data.json` keeps binary prevalence as an
audit: "what share of sessions touch this topic at all?" Binary full-text prevalence is more
Databricks-heavy because Databricks abstracts touch more rows per session. Fractional allocation
answers the better primary question here: "how much of the agenda's tracked topic attention goes
to this row?"

**Classification method — full-text fractional symmetric keywords (`AUDITS.md §0`).** The
**same** keyword set (concept terms + every vendor's product names) is applied to **both**
vendors over full title+abstract text. This replaces an earlier draft that mixed each vendor's
native taxonomy (Databricks `topic_tags`/`track`, Snowflake `attributes`) with keywords — those
taxonomies differ in breadth and silently inflated whichever side had the broader tag, in both
directions. Capped 680-char and 991-char versions remain as sensitivity checks, but they are no
longer the primary chart.

This is reproducible: `python3 classify.py` regenerates `chart_data.json` and the CSV;
`python3 gen_chart.py` regenerates `chart.svg`.

**Caveats and fairness guards (full detail in `AUDITS.md`).**
1. *Named-product prominence ≠ conceptual coverage.* Big deltas on rows 5 (Unity Catalog)
   and 2 (Semantic Views) reflect how dominant a *named brand* is in the agenda, not the
   presence/absence of the underlying capability.
2. *Open table formats (row 4) count Delta and Iceberg equally* — both are open-source — and
   the row is kept separate from the governance control plane (row 5). Open-format airtime is
   effectively tied overall; Databricks skews Delta, Snowflake skews neutral Iceberg. Not open-vs-closed.
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
