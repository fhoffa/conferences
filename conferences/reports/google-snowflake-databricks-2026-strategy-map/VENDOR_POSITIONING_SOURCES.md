# Vendor self-positioning — sources & fairness grounding

The strategy map measures **session-agenda emphasis** (what each vendor chose to put on its
summit agenda). That is *not* the same as **shipped capability** or **official positioning**.
This document grounds every row in what Databricks and Snowflake say about *themselves* —
press releases, product pages, summit keynotes — so no row can be read as "vendor X lacks
capability Y" when the vendor in fact ships and markets it.

**Read this with `AUDITS.md`.** Where a row's agenda delta could imply absence, the rule is:
*agenda emphasis ≠ capability.* Citations below establish the capability floor.

## Timing asymmetry (read first)

The two catalogs are at different lifecycle stages, which inflates nothing but is worth stating:

- **Snowflake Summit 2026** ran **June 1–4, 2026** — it has *already happened*; its agenda is
  final and its ~26 announcements are public. ([keynote](https://www.snowflake.com/en/summit/keynote/),
  [recap](https://atlan.com/know/snowflake/summit-2026-announcements/))
- **Databricks Data + AI Summit 2026** runs **June 15–18, 2026** — it is *upcoming* (2 days
  after the 2026-06-13 capture). Its 802-session agenda is pre-event and its announcements
  have not all dropped. ([event page](https://www.databricks.com/dataaisummit),
  [builder preview](https://chatforest.com/builders-log/databricks-data-ai-summit-2026-builder-preview-lakebase-mlflow-june/))

Both are *published agendas*, so the comparison is fair, but treat the Databricks numbers as a
forward-looking agenda and Snowflake's as a settled one.

---

## Row-by-row grounding

### 1. Cortex / GenAI app layer
- **Snowflake** (post-Summit): theme "Making AI Real for Business"; two headline agents —
  **CoWork** (rebranded from Snowflake Intelligence, personal agent for knowledge workers) and
  **CoCo / Cortex Code** (Snowflake-native coding agent, incl. a Claude Code plugin). 26+
  capabilities across six domains. ([diginomica](https://diginomica.com/snowflake-summit-2026-how-snowflake-making-strategic-shift-towards-agentic-ai),
  [Atlan recap](https://atlan.com/know/snowflake/summit-2026-announcements/))
- **Databricks**: **Agent Bricks** — unified platform to build/deploy/govern production agents
  with Lakehouse context, identity-first UC governance, and automated evaluation; GA Document
  Intelligence + Custom Agents. ([letsdatascience](https://letsdatascience.com/news/databricks-launches-agent-bricks-enterprise-agent-platform-6d7b19ad))
- **Fair read:** both lead with an agentic-enterprise thesis. Agenda gap (SNOW 68.9% vs DBX
  51.6%) is emphasis, not a capability gap — both ship a full GenAI/agent app layer.

### 2. Semantic context for agents — *Snowflake leads, and confirms it*
- **Snowflake** made **context & semantics a named domain**: **Semantic Studio**, **Cortex
  Sense**, **Horizon Context**; **Semantic Views** carry BI metadata *and* AI metadata
  (synonyms, sample values, verified queries) for "AI-powered BI." ([native semantic views blog](https://www.snowflake.com/en/blog/engineering/native-semantic-views-ai-bi/))
- **Databricks** has the analogous capability in **Unity Catalog Metric Views** — real, but a
  much smaller agenda presence (18 sessions say "metric view").
- **Fair read:** Snowflake's row-2 lead (21.0% vs 4.2%) matches its own positioning — semantics
  is a strategic pillar for Snowflake, a feature for Databricks. Capability exists on both sides.

### 3. Sharing / marketplace / clean rooms
- Both ship the full stack: Snowflake **Secure Data Sharing + Marketplace + Data Clean Rooms**
  ([Horizon governance](https://www.snowflake.com/en/product/features/horizon/)); Databricks
  **Delta Sharing (open protocol) + Marketplace + Clean Rooms**. Near-tie (4.3pp) — call it a
  lean, not a win.

### 4. Open table formats — *count Delta, not just Iceberg*
- **Delta Lake is open** (Linux Foundation / Apache 2.0), so a fair "open formats" row counts it
  alongside Iceberg. Doing so (keyword-symmetric) gives **Databricks 14.2% vs Snowflake 10.1%** —
  Databricks leads, because Delta (11.6% vs 0.4%) is its open house format and is everywhere on
  its agenda. Snowflake leads only the **Iceberg word** (8.4% vs 4.0%).
- **Snowflake** bet on the **industry-neutral** format: **Apache Iceberg v3**, **Apache Polaris /
  Open Catalog**, reads/writes Iceberg as its interop play.
  ([Atlan recap](https://atlan.com/know/snowflake/summit-2026-announcements/))
- **Databricks** leads with its own open format and bridges out: it **open-sourced Unity Catalog
  (Apache 2.0)**, added **native Apache Iceberg managed tables**, and ships **Delta UniForm** (one
  copy readable as Iceberg/Hudi by Trino, Dremio, DuckDB, Snowflake).
  ([Databricks PR](https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open),
  [UC managed tables docs](https://docs.databricks.com/aws/en/tables/managed),
  [VentureBeat](https://venturebeat.com/data-infrastructure/databricks-open-sources-unity-catalog-challenging-snowflake-on-interoperability-for-data-workloads))
- **Fair read:** this is **house format vs neutral format**, not open vs closed. The earlier
  "6% vs 28.7%" gap was an artifact of counting only "Iceberg" and giving Snowflake taxonomy
  credit while Databricks got keyword-only. Both have first-class open-table-format stories.

### 5. Unity Catalog vs Horizon — named control plane
- **Snowflake Horizon Catalog** is a *full* control plane: governance + discovery + RBAC across
  clouds + Trust Center + privacy (differential privacy, clean rooms) + AI security (Agent
  Identity, AI-SPM, prompt-injection defense). Upgraded and re-announced **2026-06-02**.
  ([product page](https://www.snowflake.com/en/product/features/horizon/),
  [press release](https://www.snowflake.com/en/news/press-releases/snowflake-advances-trusted-ai-with-snowflake-horizon-catalog-centralizing-governance-context-and-security-across-the-enterprise/))
- **Databricks Unity Catalog** is the platform spine connecting Lakebase, Genie, Agent Bricks,
  Lakeflow, Lakehouse — which is *why* it's tagged on 56% of sessions.
- **Fair read:** the 43pp gap is **named-brand prominence**, not a governance-capability gap.
  Broad governance is strong on both sides (Snowflake "Governance" topic = 167 sessions).

### 6. BI dashboards / AI-BI — *Databricks leads by design choice, not Snowflake weakness*
- **Databricks** ships first-party **AI/BI** (Dashboards + Genie) as a product.
- **Snowflake deliberately cedes the dashboard surface**: Snowsight is "basic reporting… not
  intended to replace BI software," and Snowflake is **removing its legacy Dashboards UI on
  2026-06-22**, steering users to **Streamlit** or third-party BI (Power BI, Tableau). Its BI
  investment goes into the *semantic layer* (row 2), not a dashboard product.
  ([Snowsight guide](https://coefficient.io/snowflake/what-is-snowsight),
  [Snowflake+Power BI guide](https://www.snowflake.com/en/developers/guides/end-to-end-analytics-with-snowflake-and-power-bi/))
- **Fair read:** the 37.2% vs 14.7% gap reflects a **strategic split** — Databricks owns the
  dashboard surface; Snowflake owns the semantic layer and partners for dashboards. Neither
  "lacks BI."

### 7. App / operational DB substrate — both made a June-2025 Postgres bet
- **Databricks Lakebase**: serverless Postgres OLTP on object storage, via the **~$1B Neon**
  acquisition; launched June 2025, **GA early 2026**. Has its own track + Databricks Apps push.
  ([launch PR](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakebase-new-class-operational-database-ai-apps),
  [Neon docs](https://neon.com/docs/introduction/neon-and-lakebase))
- **Snowflake**: **Snowflake Postgres** via the **~$250M Crunchy Data** acquisition (announced
  June 2, 2025), complementing **Unistore / Hybrid Tables**; plus **Native Apps** (36 sessions)
  and **Streamlit** (35) for app-on-data.
  ([Snowflake Postgres blog](https://www.snowflake.com/en/blog/snowflake-postgres-enterprise-ai-database/),
  [Constellation](https://www.constellationr.com/insights/news/snowflake-makes-its-postgres-move-acquires-crunchy-data))
- **Fair read:** Databricks leads on **branding/agenda concentration** (and paid ~4×). Snowflake
  is **not absent** — same Postgres-OLTP-for-agents thesis, surfaced more quietly. Keep the row
  combined with vendor-specific labels (per `NEXT_STEPS_TODO.md`).

### 8. Evals / red teaming — *Snowflake ships a real eval product too*
- **Databricks**: automated evaluation built into **Agent Bricks**; **MLflow** LLM evaluation —
  heavy agenda presence.
- **Snowflake**: acquired **TruEra / TruLens** (May 2024) and ships **AI Observability in
  Snowflake Cortex** — LLM-as-a-judge with relevance, groundedness, harmfulness metrics.
  ([TruEra acquisition](https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/),
  [AI Observability docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability))
- **Fair read:** the 11.2% vs 4.3% gap is **agenda emphasis**. Databricks talks eval mechanics
  more; both vendors ship productized evaluation. Do not claim Snowflake "has no evals."

### 9. Lakeflow / Spark / streaming pipelines — near tie
- **Databricks**: Lakeflow (Connect, Declarative Pipelines, Jobs), Spark, Structured Streaming.
- **Snowflake**: Openflow (ex-Datavolo), Snowpipe Streaming, Dynamic Tables, Snowpark, dbt.
- 1.3pp — dead heat. Both are deep here; claim no leader.

### 10. SQL warehouse / lakehouse modernization
- **Databricks**: Databricks SQL + Photon (with planned native NVIDIA acceleration).
- **Snowflake**: virtual warehouses, **Gen2 Warehouses**, **Adaptive Compute**, **Optima**.
- Modest 6pp Databricks edge; both are core-competent.

---

## Side callout — NVIDIA / accelerated compute (both have real partnerships)
- **Databricks + NVIDIA**: H100 for Mosaic AI training, TensorRT-LLM in Model Serving, planned
  **native NVIDIA acceleration in Photon**, serverless GPU notebooks/jobs, Blackwell (RTX PRO
  4500) at GTC 2026. ([deepen collaboration PR](https://www.prnewswire.com/news-releases/databricks-and-nvidia-deepen-collaboration-to-accelerate-data-and-ai-workloads-with-the-data-intelligence-platform-302092139.html),
  [AI Runtime serverless GPUs](https://www.databricks.com/blog/introducing-ai-runtime-scalable-serverless-nvidia-gpus-databricks-training-and-finetuning))
- **Snowflake + NVIDIA**: NeMo Retriever, Triton, and **NIM microservices** inside Cortex via
  Snowpark Container Services; Arctic LLM optimized with TensorRT-LLM. ([Snowflake+NVIDIA PR](https://www.snowflake.com/en/news/press-releases/snowflake-and-nvidia-power-customized-ai-applications-for-customers-and-partners/))
- **Fair read:** Databricks foregrounds **raw accelerated compute** (training, Photon); Snowflake
  abstracts the GPU behind **managed Cortex inference**. The catalog gap (12 vs 3 sessions) is
  emphasis — Snowflake has a genuine NVIDIA partnership, not "incidental bio mentions."

---

## Sources
- Snowflake + NVIDIA — https://www.snowflake.com/en/news/press-releases/snowflake-and-nvidia-power-customized-ai-applications-for-customers-and-partners/
- Databricks + NVIDIA (deepen collaboration) — https://www.prnewswire.com/news-releases/databricks-and-nvidia-deepen-collaboration-to-accelerate-data-and-ai-workloads-with-the-data-intelligence-platform-302092139.html
- Databricks AI Runtime (serverless NVIDIA GPUs) — https://www.databricks.com/blog/introducing-ai-runtime-scalable-serverless-nvidia-gpus-databricks-training-and-finetuning
- Snowsight BI scope — https://coefficient.io/snowflake/what-is-snowsight
- Snowflake native Semantic Views / AI-BI — https://www.snowflake.com/en/blog/engineering/native-semantic-views-ai-bi/
- Snowflake + Power BI guide — https://www.snowflake.com/en/developers/guides/end-to-end-analytics-with-snowflake-and-power-bi/
- Databricks open-sources Unity Catalog — https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open
- Databricks UC managed tables (Delta + Iceberg) — https://docs.databricks.com/aws/en/tables/managed
- VentureBeat (UC open source / interoperability) — https://venturebeat.com/data-infrastructure/databricks-open-sources-unity-catalog-challenging-snowflake-on-interoperability-for-data-workloads
- Snowflake Horizon Catalog (product) — https://www.snowflake.com/en/product/features/horizon/
- Snowflake Horizon Catalog (2026-06-02 press release) — https://www.snowflake.com/en/news/press-releases/snowflake-advances-trusted-ai-with-snowflake-horizon-catalog-centralizing-governance-context-and-security-across-the-enterprise/
- Databricks Lakebase launch — https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakebase-new-class-operational-database-ai-apps
- Neon + Lakebase — https://neon.com/docs/introduction/neon-and-lakebase
- Snowflake Postgres (Crunchy) blog — https://www.snowflake.com/en/blog/snowflake-postgres-enterprise-ai-database/
- Constellation (Crunchy acquisition) — https://www.constellationr.com/insights/news/snowflake-makes-its-postgres-move-acquires-crunchy-data
- Snowflake acquires TruEra (AI observability/evals) — https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/
- Snowflake Cortex AI Observability docs — https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability
- Databricks Agent Bricks (eval built in) — https://letsdatascience.com/news/databricks-launches-agent-bricks-enterprise-agent-platform-6d7b19ad
- Snowflake Summit 2026 keynote — https://www.snowflake.com/en/summit/keynote/
- Snowflake Summit 2026 recap (Atlan) — https://atlan.com/know/snowflake/summit-2026-announcements/
- Snowflake Summit 2026 (diginomica) — https://diginomica.com/snowflake-summit-2026-how-snowflake-making-strategic-shift-towards-agentic-ai
- Databricks DAIS 2026 (event page) — https://www.databricks.com/dataaisummit
- Open Semantic Interchange (OSI) launch — https://www.snowflake.com/en/news/press-releases/snowflake-salesforce-dbt-labs-and-more-revolutionize-data-readiness-for-ai-with-open-semantic-interchange-initiative/
- OSI spec (dbt Labs) — https://www.getdbt.com/blog/the-osi-spec-updates
