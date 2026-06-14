# External review TODO — Snowflake vs Databricks strategy-map blog

This TODO supports `blog-post-external-review.md`. The goal is to send a narrative/fairness draft to external reviewers while making the data-refresh blockers explicit.

## Current review artifact

- Draft for review: `conferences/reports/google-snowflake-databricks-2026-strategy-map/blog-post-external-review.md`
- Fresh-catalog process note: `conferences/reports/google-snowflake-databricks-2026-strategy-map/NEXT_STEPS_TODO.md`

## Current source catalogs

Merged in PR #14 on 2026-06-13:

- Databricks Data + AI Summit 2026: **802 sessions**
- Snowflake Summit 2026: **537 sessions**
- Google Cloud Next 2026: **1,160 sessions**
- Total comparison basis if Google remains included: **2,499 sessions**

Older scratch/blog artifacts used one of these stale bases and must not be quoted without recalculation:

- **714 / 517 / 1,160** in early Google-vs-Databricks-vs-Snowflake drafts
- **759 / 550** in later Snowflake-vs-Databricks audit artifacts

## What is new in the draft

Compared with `blog-post-v3.md`, the external-review draft:

- updates the public catalog basis to **802 / 537 / 1,160**;
- removes most stale fractional percentages from the prose;
- keeps the strongest narrative line: **Google sells possibility; Databricks sells operability; Snowflake sells legibility**;
- adds the fairness framing for **App / operational database substrate**:
  - Databricks: `Lakebase / app database substrate`
  - Snowflake: `Snowflake Postgres + Unistore / app-data bridge`
- explicitly says the draft is not publishable until numeric rows and visuals are recomputed;
- adds external-review prompts at the end.

## What reviewers should evaluate

Ask reviewers to focus on narrative/fairness first, not decimal-point precision.

### 1. Core thesis

Review claim:

> Google sells possibility. Databricks sells operability. Snowflake sells legibility.

Questions:

- Is this memorable and fair?
- Does “legibility” capture Snowflake’s business-facing/semantic/app story, or should it be “adoption,” “business translation,” or another word?
- Does “operability” capture Databricks’ production-loop story without underselling its AI/app ambitions?
- Does the Google reference case clarify the Snowflake-vs-Databricks comparison, or distract from it?

### 2. Snowflake framing

Review whether the draft fairly represents Snowflake as:

- Cortex / Snowflake Intelligence / Cortex Analyst;
- semantic context for business-facing AI;
- Streamlit / Native Apps / Marketplace / clean rooms;
- Horizon Catalog and governance/context;
- Snowflake Postgres + Unistore + Hybrid Tables as app-data/operational bridges;
- Iceberg/open-lakehouse interoperability.

Avoid implying:

- Snowflake lacks governance;
- Snowflake lacks an operational/app database story;
- Snowflake is only “business users” and not technical builders.

### 3. Databricks framing

Review whether the draft fairly represents Databricks as:

- Unity Catalog as governance/control-plane center;
- Lakeflow / Spark / streaming / pipelines;
- Databricks SQL / AI/BI / Genie / Metric Views;
- MLflow / evals / traces / Agent-as-Judge;
- Lakebase / Databricks Apps / Mosaic AI as app/agent substrate;
- Delta + Iceberg / Unity Catalog interoperability.

Avoid implying:

- Databricks lacks business-facing AI;
- Databricks is only infrastructure and not applications;
- Databricks’ AI/BI/conversational analytics story is secondary unless the fresh numbers support that.

### 4. Category fairness

The main rows needing skeptical review:

- **App / operational database substrate**
  - Databricks: `Lakebase / app database substrate`
  - Snowflake: `Snowflake Postgres + Unistore / app-data bridge`
  - Claim: Databricks leads in agenda concentration/product branding, not capability existence.

- **Unity Catalog vs Horizon governance control plane**
  - compare named catalog/control-plane prominence, not broad governance.
  - broad governance is strong on both sides.

- **Iceberg / open-lakehouse interoperability**
  - keep separate from Unity/Horizon governance.
  - Iceberg is table/interoperability layer; Horizon is closer Snowflake counterpart to Unity Catalog.

- **Semantic context vs BI/AI-BI**
  - Snowflake may lead semantic context for agentic analytics.
  - Databricks may lead BI/dashboard/AI-BI agenda share.
  - Keep the distinction explicit.

- **Evals / AI quality**
  - distinguish strict eval/benchmark/red-team signals from broader trust/security/quality language.


## Uploaded context for external reviewer

This PR also includes the Tier 1/Tier 2 context requested by the external-review agent:

### Tier 1 — old raw snapshots for apples-to-apples reruns

- `conferences/databricks-data-ai-summit/2026/normalized/snapshots/2026-06-02.sessions.json` — **759** Databricks sessions, matching the prior Snowflake-vs-Databricks draft basis.
- `conferences/snowflake-summit/2026/normalized/snapshots/2026-06-02.sessions.json` — **550** Snowflake sessions, matching the prior Snowflake-vs-Databricks draft basis.

These are preferred over comparing against the old mirrored-bar CSV because the reviewer can run the same classifier on both old and current snapshots, isolating **data drift** from **method drift**.

### Tier 2 — editorial intent and prior framing

- `conferences/reports/google-snowflake-databricks-2026-strategy-map/prior-analysis/2026-06-02/databricks_snowflake_visualization_staging_notes.md` — prior mirrored-bar staging/design decisions.
- `conferences/reports/google-snowflake-databricks-2026-strategy-map/prior-analysis/2026-06-02/databricks_snowflake_evals_chapter.md` — prior evals narrative/framing voice.

### Explicitly not included

The old mirrored-bar CSV/MD is not included because the raw 759/550 snapshots are available. The three prior audits are also not included because the reviewer already rebuilt those from fresh data in `AUDITS.md`; they can be added later only if needed as a methodology cross-check.

## Data work required before publication

Recompute from dated 2026-06-13 snapshot files:

- `conferences/databricks-data-ai-summit/2026/normalized/snapshots/2026-06-13.sessions.json`
- `conferences/snowflake-summit/2026/normalized/snapshots/2026-06-13.sessions.json`
- Google source catalog used by the original strategy map, if Google remains in the post.

Rows to recompute:

1. Cortex / GenAI app layer
2. Semantic context for agents
3. Sharing / marketplace / clean rooms
4. Iceberg / open-lakehouse interoperability
5. Unity Catalog vs Horizon governance control plane
6. BI dashboards / metrics / AI-BI
7. App / operational database substrate
8. Evals / red teaming / AI quality
9. Lakeflow / Spark / streaming pipelines
10. SQL warehouse / lakehouse modernization

Side callouts to re-audit:

- NVIDIA / GPU / accelerated compute
- shared companies appearing in both catalogs
- significant absences from one side
- Snowflake Postgres + Unistore vs Databricks Lakebase story
- Horizon vs Unity Catalog fairness framing
- Iceberg/open-lakehouse interoperability

## Visual work required before publication

Rebuild or update:

- mirrored Snowflake-vs-Databricks bar chart using **802 / 537** denominators;
- any three-vendor Google/Databricks/Snowflake strategy map if keeping Google in the blog;
- validation/evidence browser if it will be referenced in final copy.

Visual rules:

- label raw counts vs fractional session-equivalents explicitly;
- do not mix raw session counts and fractional credits without marking them;
- use vendor-specific labels inside fair categories;
- include a methodology/caveat note: agenda emphasis, not product quality or market share.

## Suggested external-review note

When sending this PR for review, ask reviewers:

> This is a narrative/fairness review draft. Please focus on whether the strategic framing is fair to Snowflake, Databricks, and Google; whether the category labels avoid vendor-specific traps; and which claims need stronger evidence. The fresh catalogs are 802 Databricks sessions and 537 Snowflake sessions, but final percentages/visuals still need recalculation before publication.

## Done criteria before final publication

- [ ] All stale denominators removed or replaced.
- [ ] Fractional rows recomputed against current catalogs.
- [ ] Mirrored chart rebuilt.
- [ ] Any Google numbers verified if Google remains in the post.
- [ ] Lakebase/Postgres/Unistore row fairness-reviewed.
- [ ] Unity/Horizon row fairness-reviewed.
- [ ] Iceberg/open-lakehouse row fairness-reviewed.
- [ ] Evals row strict-vs-broad definitions reviewed.
- [ ] Reviewer feedback synthesized into final copy.
- [ ] Final artifact references point to files that exist in repo, not private scratch paths.
