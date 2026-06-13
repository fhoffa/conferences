# Spicy takes — grounded edition

Sharp claims for the blog post. Each take is paired with **the number** (from `classify.py`,
2026-06-13 catalogs: DBX 802 / SNOW 537) and **the receipt** (vendor's own materials in
`VENDOR_POSITIONING_SOURCES.md`), plus the caveat that keeps it honest. Rule: a take can be
spicy about *emphasis and strategy*; it may **not** claim a vendor lacks a capability the
catalog or the vendor contradicts.

---

### 1. "Snowflake won the AI-agenda war; Databricks won the platform-spine war."
**Number:** Snowflake leads the GenAI app layer (68.9% vs 51.6%), semantic context (21.0% vs
4.2%), and Iceberg/open (28.7% vs 6.0%). Databricks leads Unity Catalog (56.1% vs 12.7%),
AI/BI (37.2% vs 14.7%), and evals (11.2% vs 4.3%).
**Why it's fair:** the split is real and symmetric — 5 rows each. Snowflake foregrounds the AI
*surface*; Databricks foregrounds the governed *substrate*.

### 2. "Unity Catalog is the most over-marketed product in the data industry."
**Number:** it's tagged on **56% of all Databricks sessions** — the single most over-represented
product in either catalog.
**Caveat that saves it:** this is because UC is the platform spine wiring Lakebase, Genie,
Agent Bricks, and Lakeflow together — not because Snowflake lacks governance. Horizon Catalog
is a full control plane (RBAC, Trust Center, differential privacy, AI Agent Identity), expanded
2026-06-02. Spicy framing: *"Databricks turned its catalog into a religion; Snowflake treats
governance as plumbing."* Both ship the plumbing.

### 3. "Snowflake's BI strategy is to not have a BI tool — and that's deliberate."
**Number:** Databricks talks dashboards 2.5× more (37.2% vs 14.7%).
**Receipt:** Snowsight is officially "basic reporting… not intended to replace BI software";
Snowflake is **retiring its legacy Dashboards UI (2026-06-22)** and steering users to Streamlit
or Power BI/Tableau. Its BI investment goes into **Semantic Views** (the row-2 lead), not a
dashboard product. ([Snowsight scope](https://coefficient.io/snowflake/what-is-snowsight),
[Snowflake+Power BI](https://www.snowflake.com/en/developers/guides/end-to-end-analytics-with-snowflake-and-power-bi/))
**Spicy + true:** *"Snowflake doesn't want to be your dashboard. It wants to be the semantic
layer underneath everyone else's."*

### 4. "Both panic-bought a Postgres company in June 2025 — Databricks paid 4× more."
**Receipt:** Databricks acquired **Neon (~$1B)** → Lakebase; Snowflake acquired **Crunchy Data
(~$250M, announced June 2, 2025)** → Snowflake Postgres. Same week, same thesis: an OLTP
database for AI agents. ([Lakebase](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakebase-new-class-operational-database-ai-apps),
[Crunchy](https://www.constellationr.com/insights/news/snowflake-makes-its-postgres-move-acquires-crunchy-data))
**Number:** Databricks brands it 1.5× louder on the agenda (25.7% vs 17.1%) and gives Lakebase
its own track. **Caveat:** Snowflake is *not* absent — Native Apps (36) + Streamlit (35) +
Snowflake Postgres carry the app-on-data story.

### 5. "Snowflake shouts 'open'; Databricks quietly open-sourced its catalog."
**Number:** Snowflake brands Iceberg/open 4.8× more on the agenda (28.7% vs 6.0%).
**The twist:** Databricks **open-sourced Unity Catalog under Apache 2.0**, ships **native Iceberg
managed tables**, and **Delta UniForm** lets one copy be read as Iceberg by Trino, Dremio, and
even Snowflake. ([Databricks PR](https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open),
[UC managed tables](https://docs.databricks.com/aws/en/tables/managed))
**Spicy + fair:** *"Iceberg is Snowflake's billboard and Databricks' default setting."* Both are
genuinely open — only the marketing volume differs.

### 6. "Everyone says 'eval' — only some ship one. Both do; one hides it."
**Number:** Databricks devotes 2.6× more agenda to strict eval/red-team/guardrail (11.2% vs 4.3%).
**Receipt:** Databricks builds automated evaluation into **Agent Bricks** + MLflow. Snowflake
**acquired TruEra/TruLens in 2024** and ships **AI Observability in Cortex** (LLM-as-judge,
groundedness) — it just barely mentions it on stage. ([Snowflake TruEra](https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/))
**Spicy:** *"Snowflake bought an evals company and forgot to put it on the agenda."*

### 7. "The real 2026 battleground isn't agents — it's the semantic layer feeding them."
**Number:** the sharpest single asymmetry after Unity Catalog: Snowflake **Semantic Views** at
21.0% vs Databricks **Metric Views** at 4.2%.
**Receipt:** Snowflake made semantics a named Summit domain (Semantic Studio, Cortex Sense,
Horizon Context). Whoever owns the semantic layer owns how every agent grounds its answers.
([native semantic views](https://www.snowflake.com/en/blog/engineering/native-semantic-views-ai-bi/))
**Fair:** Databricks has the capability (UC Metric Views) — it just isn't selling it as the
headline yet.

### 8. "Neither is really fighting NVIDIA's battle — they're on opposite sides of the GPU."
**Number:** Databricks 12 NVIDIA/GPU sessions vs Snowflake 3.
**Receipt:** both have real NVIDIA partnerships — Databricks on **raw compute** (H100, Photon,
serverless GPUs, Blackwell at GTC 2026), Snowflake on **managed inference** (NeMo, NIM, Triton
in Cortex). ([Databricks+NVIDIA](https://www.prnewswire.com/news-releases/databricks-and-nvidia-deepen-collaboration-to-accelerate-data-and-ai-workloads-with-the-data-intelligence-platform-302092139.html),
[Snowflake+NVIDIA](https://www.snowflake.com/en/news/press-releases/snowflake-and-nvidia-power-customized-ai-applications-for-customers-and-partners/))
**Spicy + fair:** *"Databricks wants to sell you the GPU; Snowflake wants you to forget it
exists."*

---

## The one-liner thesis (survives all the receipts)

> **Google sells possibility. Databricks sells operability. Snowflake sells legibility.**

Mapped to this data: Databricks' agenda is governed-substrate-and-tooling heavy (Unity Catalog,
AI/BI, Lakebase, evals = *operability*); Snowflake's is AI-surface-and-meaning heavy (Cortex,
Semantic Views, Iceberg branding = *legibility*). The split is **emphasis, not capability** —
which is exactly why the takes land without lying.

## What you may NOT say (the guardrails)
- ❌ "Snowflake has no evals / no operational DB / no NVIDIA story / is closed." All false —
  see receipts.
- ❌ "Databricks isn't open." It open-sourced its catalog.
- ❌ Treat near-ties as wins: pipelines (1.3pp) and sharing (4.3pp) are **ties/leans**.
- ❌ Quote the old 759/550 numbers. Use 802/537; the diff (`DIFF_OLD_NEW.md`) shows no leader
  flipped, so every take is stable to the refresh.
