# Visualization staging notes — Databricks vs Snowflake Summit 2026

Source basis: latest local normalized schedules as of 2026-06-02: Databricks 759 sessions; Snowflake 550 sessions.

Goal: stage the data for a visual that explains the strategic contrast without overclaiming category labels.

## Best visual thesis

Snowflake and Databricks are not simply competing on the same agenda. They are emphasizing different layers of the enterprise AI stack.

- Snowflake: enterprise AI data interface — Cortex, agents, semantic context, sharing, native apps, Iceberg interoperability.
- Databricks: governed production substrate — Unity Catalog, SQL/lakehouse modernization, Lakeflow/Spark pipelines, AI/BI, Lakebase, Delta/Iceberg convergence, evals/MLOps.

## Recommended visualization: divergence map, not exhaustive category chart

Use 8–10 high-contrast topics, each with:

- Databricks agenda share
- Snowflake agenda share
- delta in percentage points
- one-line strategic meaning
- 1–2 representative session examples available via tooltip / appendix

Avoid plotting every topic. Ties and noisy broad categories will weaken the story.

## Strongest visual topics

### 1. Cortex / GenAI / LLM application infrastructure

- Snowflake strict GenAI/LLM excluding Cortex-only: 258 / 550 = 46.9%
- Databricks comparable strict/broad LLM: 223 / 759 = 29.4%
- Snowflake advantage: +17.5 pp

Meaning: Snowflake is foregrounding Cortex, Snowflake Intelligence, Cortex Agents, Cortex Code, OpenAI-style agent workflows, and LLM access to enterprise data.

Use in visual as Snowflake-leading.

### 2. Unity Catalog / governance control plane

- Databricks governance/control-plane signal: 519 / 759 = 68.4%
- Snowflake governance/control-plane signal: 277 / 550 = 50.4%
- Databricks advantage: +18.0 pp

Meaning: Databricks makes Unity Catalog the operating control plane for data, AI, apps, tools, and external engines. Snowflake has governance too, but Databricks over-indexes on governance as architecture.

Use in visual as Databricks-leading.

### 3. Iceberg / open-lakehouse interoperability

- Snowflake Iceberg/open-lakehouse strict: 85 / 550 = 15.5%
- Databricks Iceberg/open-lakehouse strict: 38 / 759 = 5.0%
- Snowflake advantage: +10.5 pp

Meaning: Snowflake over-indexes on Iceberg as its interoperability answer. This is not the same as “open table formats” generally.

Use in visual as Snowflake-leading.

### 4. Delta + Iceberg / open-table convergence

- Databricks open-table total including Delta: 90 / 759 = 11.9%
- Snowflake open-table total: 85 / 550 = 15.5%
- But Delta-specific:
  - Databricks Delta: 61 / 759 = 8.0%
  - Snowflake Delta: 0 / 550 = 0.0%

Meaning: Databricks owns the Delta + Iceberg convergence story; Snowflake owns the Iceberg-forward interoperability story. Visual should split these into two adjacent bars, not one generic “open table formats” bar.

Use as paired visual: Snowflake = Iceberg interoperability; Databricks = Delta/Iceberg convergence.

### 5. Lakeflow / Spark / streaming / declarative pipelines

- Databricks data engineering/streaming fractional share: 61.4 / 759 = 8.1%
- Snowflake data engineering/streaming fractional share: 31.1 / 550 = 5.7%
- Databricks advantage: +2.4 pp

Meaning: Databricks has more visible agenda share around Spark, Lakeflow, streaming, CDC, ETL, and pipeline mechanics.

Use in visual as Databricks-leading.

### 6. Databricks SQL / lakehouse warehouse modernization

- Databricks warehouse/lakehouse SQL fractional share: 64.1 / 759 = 8.4%
- Snowflake warehouse/lakehouse SQL fractional share: 26.9 / 550 = 4.9%
- Databricks advantage: +3.5 pp

Meaning: Databricks is actively reframing warehouse modernization as lakehouse SQL. Snowflake is obviously a warehouse company, but Databricks spends more agenda share on the warehouse-as-lakehouse modernization story.

Use in visual as Databricks-leading.

### 7. Semantic context vs BI/dashboarding split

Semantic context for agents:
- Snowflake: 135 / 550 = 24.5%
- Databricks: 58 / 759 = 7.6%
- Snowflake advantage: +16.9 pp

BI/dashboards/reporting:
- Databricks: 324 / 759 = 42.7%
- Snowflake: 108 / 550 = 19.6%
- Databricks advantage: +23.1 pp

Meaning: This should be a split visual, not one semantic/BI category. Snowflake emphasizes semantic context for agents/Cortex Analyst. Databricks emphasizes BI modernization, AI/BI dashboards, Metric Views, and open semantics.

Use as one of the most important visual contrasts.

### 8. App/operational database substrate: Lakebase vs Snowflake Postgres + Unistore

Audited caution: do not chart this as “Databricks has operational DB, Snowflake does not.” Snowflake has Postgres, Hybrid Tables, Unistore, streaming/CDC, and app-stack content.

Use one fair category with vendor-specific labels:

- Databricks label: **Lakebase / app database substrate**
- Snowflake label: **Snowflake Postgres + Unistore / app-data bridge**

Comparable category scan excluding generic CDC/streaming noise:

- Databricks: 99 / 759 = 13.0%
- Snowflake: 21 / 550 = 3.8%
- Databricks advantage: +9.2 pp

Important sub-counts:
- Lakebase strict:
  - Databricks: 82 / 759 = 10.8%
  - Snowflake: 0 / 550 = 0.0%
- Postgres / OLTP strict:
  - Databricks: 17 / 759 = 2.2%
  - Snowflake: 15 / 550 = 2.7%
- Broader operational DB / transactional / database branching / Unistore / Hybrid Tables:
  - Databricks: 21 / 759 = 2.8%
  - Snowflake: 14 / 550 = 2.5%

Meaning: Both companies have operational/app database stories. Databricks makes it a named Lakebase pillar. Snowflake tells it as an integration story across Snowflake Postgres, Unistore, Hybrid Tables, streaming/CDC, SPCS/Streamlit, Cortex, and Iceberg.

Use in visual as Databricks-leading on agenda concentration, while explicitly showing Snowflake’s product counter-label.

### 9. Evals / red teaming / AI quality

Strict eval / benchmark / red-team:
- Databricks: 87 / 759 = 11.5%
- Snowflake: 22 / 550 = 4.0%
- Databricks advantage: +7.5 pp

Broader AI/agent quality/trust:
- Databricks: 212 / 759 = 27.9%
- Snowflake: 110 / 550 = 20.0%
- Databricks advantage: +7.9 pp

Meaning: Databricks treats evals like AI production infrastructure. Snowflake treats evals more as Cortex-agent optimization and production-readiness.

Use in visual as Databricks-leading.

### 10. NVIDIA / GPU / accelerated compute

Snowflake audit:
- meaningful NVIDIA session company/title/abstract presence: 0
- incidental NVIDIA bio mentions only: 7
- GPU mentions: 3

Databricks audit:
- NVIDIA sessions: 4
- GPU sessions: 11
- RAPIDS: 2
- cuOpt: 1

Meaning: Small count, high narrative value. Snowflake is surprisingly quiet on NVIDIA/accelerated compute; Databricks has visible NVIDIA/GPU production-AI infrastructure signals.

Use as a callout, not a main bar, because absolute counts are small.

### 11. Sharing / marketplace / clean rooms / native-app distribution

- Snowflake: 275 / 550 = 50.0%
- Databricks: 280 / 759 = 36.9%
- Snowflake advantage: +13.1 pp

Meaning: Snowflake makes governed collaboration, clean rooms, marketplace, secure sharing, and native-app distribution more central. Databricks has Delta Sharing, but the strategic weight differs.

Use in visual as Snowflake-leading.

### 12. Hard MLOps / model lifecycle

Broad ML including Cortex makes Snowflake look stronger:
- Snowflake broad ML including Cortex AI: 193 / 550 = 35.1%
- Databricks broad ML: 149 / 759 = 19.6%

But strict model lifecycle tells the opposite story:
- Databricks hard model lifecycle terms: 68 / 759 = 9.0%
- Snowflake hard model lifecycle terms: 6 / 550 = 1.1%

Meaning: Do not use a generic “ML platform” bar. Split into:
- Snowflake: Cortex AI platform surface
- Databricks: hard MLOps / model lifecycle mechanics

Use if the visualization can support nuanced paired contrasts; otherwise leave out to avoid confusion.

## Topics to avoid or down-rank

### Sovereign / hybrid / private

- Snowflake sovereign strict: 6 / 550 = 1.1%
- Databricks sovereign strict: 5 / 759 = 0.7%
- Snowflake hybrid operational: 18 / 550 = 3.3%
- Databricks hybrid operational: 11 / 759 = 1.4%
- Regulated/compliance is actually close or Databricks-leaning depending rules.

Use only as a minor annotation, not a main visual pillar.

### Generic governance

Governance is important, but generic governance keywords can be noisy. For the visual, label it specifically as Unity Catalog / governance control plane vs Horizon/data governance, not just “governance.”

### Generic AI

Both conferences are AI-heavy. Generic AI counts are boring. The useful split is:
- Snowflake: Cortex / agents / semantic context
- Databricks: evals / model lifecycle / AI-BI / governed production substrate

## Recommended chart structure

### Option A: mirrored two-sided agenda-share bars — recommended

Rows: the strongest divergence topics above, sorted by absolute difference or grouped by vendor-leading side.

Geometry:
- zero line in the center
- Snowflake extends left in Snowflake blue
- Databricks extends right in Databricks red
- bar length = each conference's agenda share for that topic, not just the delta
- labels on each side show percentage and raw count, e.g. `24.5% / 135 sessions`
- optional small center annotation shows the delta, e.g. `Snowflake +16.9 pp`

Why this is better than a simple +/- bar:
- it preserves total volume on both sides
- it still makes asymmetry obvious
- it avoids making a 2% vs 0% gap look visually comparable to a 47% vs 29% gap
- it makes “both are doing this, but one emphasizes it more” clear

Design defaults:
- Snowflake left: blue, e.g. `#29B5E8` or a darker accessible Snowflake blue
- Databricks right: red, e.g. `#FF3621` or a darker accessible Databricks red
- use a common x-axis scale on both sides
- cap main chart to 10 rows; put NVIDIA/GPU and open-table-format split as callouts
- keep count labels visible because Databricks has 759 sessions and Snowflake has 550

Best for a report/post because it gives both magnitude and contrast.

### Option B: simple delta-only divergence chart

Rows: topics above.

Bar = percentage-point advantage only.

Use only if space is extremely tight. It is punchy, but hides total volume and can overemphasize small categories.

### Option C: Two-column stack map

Left: Snowflake-led layers.
Right: Databricks-led layers.

Each block has:
- topic
- percentage
- representative session titles

This is better for storytelling than a raw chart.

### Option C: Quadrant / layer diagram

Vertical axis: interface layer → infrastructure/substrate layer.
Horizontal axis: business/application → technical/platform.

Plot topics:
- Snowflake upper/interface/business: Cortex, semantic context, sharing/native apps, Iceberg interoperability.
- Databricks lower/substrate/platform: Unity Catalog, Lakeflow/Spark, SQL/lakehouse, Lakebase, evals/MLOps, GPU/NVIDIA.

Use actual percentages as labels; not as dot sizes unless we want a more complex visual.

## First visualization cut

Use these 10 rows:

1. Cortex / GenAI app layer — Snowflake +17.5 pp
2. Semantic context for agents — Snowflake +16.9 pp
3. Sharing / marketplace / clean rooms — Snowflake +13.1 pp
4. Iceberg / open-lakehouse interoperability — Snowflake +10.5 pp
5. Unity Catalog / governance control plane — Databricks +18.0 pp
6. BI dashboards / metrics / AI-BI — Databricks +23.1 pp
7. Lakebase / Postgres-like operational DB — Databricks +14.6 pp
8. Evals / red teaming / AI quality — Databricks +7.5 pp strict
9. Lakeflow / Spark / streaming pipelines — Databricks +2.4 pp fractional
10. Databricks SQL / lakehouse warehouse modernization — Databricks +3.5 pp fractional

Then add two callouts:

- NVIDIA/GPU: Databricks visible; Snowflake catalog effectively silent aside from bio artifacts.
- Open table formats need split treatment: Snowflake = Iceberg interoperability; Databricks = Delta/Iceberg convergence.
