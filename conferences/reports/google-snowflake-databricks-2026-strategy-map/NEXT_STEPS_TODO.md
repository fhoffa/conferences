# Snowflake vs Databricks 2026 strategy map — next steps TODO

## Current state

Fresh public session catalogs were downloaded on **2026-06-13**.

Latest normalized counts:

- **Databricks Data + AI Summit 2026:** 802 sessions
  - Previous working snapshot: 759 sessions
  - Net change: +43 sessions
  - Added: 61
  - Removed: 18
- **Snowflake Summit 2026:** 537 sessions
  - Previous working snapshot: 550 sessions
  - Net change: -13 sessions
  - Added: 2
  - Removed: 15

Current normalized files:

- `conferences/databricks-data-ai-summit/2026/normalized/sessions.json`
- `conferences/databricks-data-ai-summit/2026/normalized/summary.json`
- `conferences/databricks-data-ai-summit/2026/normalized/current/sessions.json`
- `conferences/databricks-data-ai-summit/2026/normalized/current/summary.json`
- `conferences/snowflake-summit/2026/normalized/sessions.json`
- `conferences/snowflake-summit/2026/normalized/summary.json`
- `conferences/snowflake-summit/2026/normalized/current/sessions.json`
- `conferences/snowflake-summit/2026/normalized/current/summary.json`

Dated snapshots:

- `conferences/databricks-data-ai-summit/2026/normalized/snapshots/2026-06-13.sessions.json`
- `conferences/databricks-data-ai-summit/2026/normalized/snapshots/2026-06-13.summary.json`
- `conferences/snowflake-summit/2026/normalized/snapshots/2026-06-13.sessions.json`
- `conferences/snowflake-summit/2026/normalized/snapshots/2026-06-13.summary.json`

## What changed in the latest catalogs

### Databricks

Added examples to review:

- `FanDuel Presents: Operating Databricks at Scale`
- `Supporting Fine-Grained Access Control with Server-Side Scan Planning`
- `We Killed ETL: Unstructured.io Foundation`
- `AI Governance with Matei`
- `Building RAG Agents with Agent Bricks`
- `Proliferation of Agent Harnesses and Tools, AI Dev Kit`
- `Women in Data & AI: Hear how not to do AI from Robin, Maria & Holly`
- `Building Search for Agents with Lakebase`

Removed examples to inspect for impact:

- `Sponsored by: Cognizant | An AI Data Foundation for Decision Intelligence for Medtronic, in Partnership with Cognizant`
- `From Transactions to Analytics: How Lakebase Works with Lakehouse`
- `High Stakes, High Trust: Scaling Reliable Data + Agents at FanDuel`
- `Beyond Batch: Engineering Self-Evolving Ingestion with Databricks Auto Loader`
- `Deploying and Monitoring Agents on Databricks`
- `Streaming to Lakehouse: How Launchmetrics Simplified Pipelines, Built Data Trust and Adopted Genie`
- `Sponsored By: Fractal | From Questions to Action: Conversational AI for Occasion‑Based Marketing`
- `Building Semantic Models with UC Metric views`

### Snowflake

Added sessions:

- `BI232B — Turning Data into Decisions: How to Stop Paying the Reporting Tax`
- `IN108 — Building the Digital Backbone for Team USA`

Removed sessions include several PCZ roadmap/user-research sessions; inspect whether these removals change the app/operational DB, Cortex Code, native app, or sovereign/hybrid side notes:

- `What's Next for Unistore: Help Shape the Roadmap for Hybrid Workloads`
- `Help Shape Cortex Code's Roadmap: Use Cases, Workflows and Tradeoffs`
- `Native Apps for Providers: Agents, MCP and What's Next`
- `Running Regulated and Sovereign Workloads`
- `Accelerating Data Sharing Workflows with Cortex Code`
- `AI-Powered Data Engineering with DCM: Deploying Changes Fast and Safely`

## Analysis that must be recalculated from the fresh catalogs

Recompute all rows currently based on the older **759 / 550** working snapshot. The new denominators are **802 / 537**.

Priority rows for the mirrored chart:

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

Also re-audit side callouts:

- NVIDIA / GPU / accelerated compute
- Shared companies appearing in both catalogs
- Significant absences from one side
- Snowflake Postgres + Unistore vs Databricks Lakebase story
- Horizon vs Unity Catalog fairness framing

## Review/synthesis instructions

When recomputing, keep the story spicy but fair:

- Do not claim a vendor lacks a capability when the catalog shows a counter-story.
- Distinguish named-product prominence from broader conceptual coverage.
- Keep counts as session counts unless a row explicitly uses fractional agenda share.
- For fractional rows, label counts as fractional session credits, not sessions.
- Separate speaker/company affiliation from title mentions for company overlap.
- Treat “missing” as absent from current catalog signals, not absent as a customer/partner/user.

Specific fairness checks:

- **App / operational database substrate:** keep one combined row with vendor-specific labels:
  - Databricks: `Lakebase / app database substrate`
  - Snowflake: `Snowflake Postgres + Unistore / app-data bridge`
  - Say Databricks leads in agenda concentration/product branding, not that Snowflake lacks operational DB/app story.
- **Unity Catalog vs Horizon:** compare named catalog/control-plane prominence, not broad governance. Broad governance is strong on both sides.
- **Iceberg / open-lakehouse:** keep separate from governance/control-plane. Iceberg is a table/interoperability layer; Horizon is the closer Snowflake counterpart to Unity Catalog.
- **Evals:** distinguish strict eval/benchmark/red-team from broader trust/quality language.
- **NVIDIA:** verify whether Snowflake still has only incidental bio mentions and whether Databricks still has meaningful NVIDIA/GPU session presence.

## Implementation tasks

1. Re-run the topic classifiers against `normalized/current/sessions.json` for both conferences.
2. Write updated mirrored-chart data with the new **802 / 537** denominators.
3. Diff old vs new chart rows and flag any claim whose leader/delta changes materially.
4. Rebuild the visualization using the mirrored bar design:
   - Snowflake blue extends left.
   - Databricks red extends right.
   - Bar length is actual agenda share.
   - Center label shows leader and delta.
5. Update the strategy narrative with only claims that survive the new data.
6. Add an appendix explaining methodology, denominators, raw-vs-fractional rows, and caveats.
7. Run a final fairness audit before publishing.

## Existing draft artifacts to reconcile

Older scratch/report artifacts may still use the prior 759 / 550 snapshot. Review and update before quoting numbers:

- `/root/conference_backup/google-cloud-next/2026/graphify-out/databricks_snowflake_mirrored_bar_chart_data.csv`
- `/root/conference_backup/google-cloud-next/2026/graphify-out/databricks_snowflake_mirrored_bar_chart_data.md`
- `/root/conference_backup/google-cloud-next/2026/graphify-out/databricks_snowflake_visualization_staging_notes.md`
- `/root/conference_backup/google-cloud-next/2026/graphify-out/databricks_snowflake_evals_chapter.md`
- `/root/conference_backup/google-cloud-next/2026/graphify-out/nvidia_presence_audit.md`
- `/root/conference_backup/google-cloud-next/2026/graphify-out/snowflake_postgres_story_audit.md`
- `/root/conference_backup/google-cloud-next/2026/graphify-out/category_fairness_audit_lakebase_iceberg_unity_horizon.md`
