# Fairness audits — Snowflake vs Databricks 2026

All numbers recomputed from the **2026-06-13** catalogs (DBX 802 / SNOW 537) via
`classify.py`. These audits exist to keep the strategy map *spicy but fair*: where a
headline delta could be read as "vendor X has no story," this is where we check whether
the catalog actually shows a counter-story.

> **Capability floor:** the agenda counts below measure *what each vendor put on its summit
> agenda*, not *what it ships*. For every row, `VENDOR_POSITIONING_SOURCES.md` cites each
> vendor's own product pages / press releases so no delta can be misread as absence. Cited
> corrections are folded into §4 and §7 below.

---

## 1. Unity Catalog vs Horizon — named control plane (row 5)

| | Databricks | Snowflake |
|---|---|---|
| Named control-plane signal | Unity Catalog | Horizon Catalog |
| Sessions | 450 (56.1%) | 68 (12.7%) |

**Verdict: real but must be framed as *named-product prominence*, not "Snowflake has weak
governance."** Databricks attaches the **Unity Catalog** tag to 370 sessions and the term
appears in many more abstracts — UC is the gravitational center of the Databricks agenda
and is tagged onto sessions that are only adjacently about governance. Snowflake's
**Horizon Catalog** is a single named feature on 67 sessions.

**Fairness guard:** broad *governance* coverage is strong on **both** sides — Snowflake's
"Governance" covered-topic alone is on 167 sessions and its "Governance & Security" track
on 34. The 43pp gap measures **how dominant the *named* catalog brand is in the agenda**,
not the presence of governance capability. State it as: *Unity Catalog is the most
over-represented single product in either catalog; Horizon is a comparatively contained,
single-feature story.*

**Capability floor (cited):** **Horizon Catalog** is itself a full control plane —
cross-cloud RBAC, Trust Center, differential privacy, clean rooms, AI Agent Identity, and
AI security posture management — re-announced and expanded on 2026-06-02
([product page](https://www.snowflake.com/en/product/features/horizon/),
[press release](https://www.snowflake.com/en/news/press-releases/snowflake-advances-trusted-ai-with-snowflake-horizon-catalog-centralizing-governance-context-and-security-across-the-enterprise/)).
Unity Catalog's 56% reflects its role as the Databricks platform spine (it connects Lakebase,
Genie, Agent Bricks, Lakeflow), not a governance gap at Snowflake.

---

## 2. Iceberg / open-lakehouse interoperability (row 4)

| | Databricks | Snowflake |
|---|---|---|
| Sessions | 48 (6.0%) | 154 (28.7%) |
| Iceberg keyword only | 32 | 70 (feature tag) |

**Verdict: Snowflake decisively out-brands Databricks on *open-table-format /
interoperability* language — but this is partly a default-format artifact.** Databricks'
default table format is **Delta**, so most of its open-lakehouse work is implicit; it says
"Iceberg" (32) or "Uniform" (3) far less often than Snowflake foregrounds **Apache
Iceberg** (70), **Polaris** (26), and "Open Lakehouse"/"Interoperability" topics. Snowflake
has made Iceberg a marquee, externally-legible bet; Databricks treats open formats as
plumbing under Delta/Uniform.

**Fairness guard:** keep this row **separate from governance** (row 5). Iceberg is a
table/interoperability layer; do **not** claim Databricks is "closed" — Delta + Uniform +
Unity Catalog's external-engine access are a real openness story that simply isn't labeled
"Iceberg." Frame as: *Snowflake leads on named open-format prominence; Databricks' openness
is real but defaults to Delta and is less surfaced in session titles.*

**Capability floor (cited):** Databricks **open-sourced Unity Catalog (Apache 2.0)**, ships
**native Apache Iceberg managed tables**, and **Delta UniForm** exposes one copy as
Iceberg/Hudi to Trino, Dremio, DuckDB, and Snowflake
([Databricks PR](https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open),
[UC managed tables docs](https://docs.databricks.com/aws/en/tables/managed)). The 6-vs-28.7
gap is a labeling artifact, not closure.

---

## 3. App / operational database substrate — Lakebase vs Snowflake Postgres + Unistore (row 7)

| Signal | Databricks | Snowflake |
|---|---|---|
| Combined row | 206 (25.7%) | 92 (17.1%) |
| Lakebase (tag) | 109 | — |
| Databricks Apps (tag) | 108 | — |
| Snowflake Postgres (feature) | — | 12 |
| Hybrid Tables / Unistore | — | 13 / 3 |
| Native Apps (feature) | — | 36 |
| Streamlit in Snowflake (feature) | — | 35 |

**Verdict: Databricks leads in agenda concentration and product branding for the
operational-DB substrate — but Snowflake is NOT absent here.** Databricks gives **Lakebase**
its own track (33 sessions) plus a heavy **Databricks Apps** push; the Postgres-as-app-data
narrative is loud and named. Snowflake's directly comparable operational-DB pieces —
**Snowflake Postgres** (12) and **Hybrid Tables/Unistore** (13/3) — are quieter and still
preview-flavored. **But** Snowflake's app-development substrate is carried by **Native Apps
(36)** and **Streamlit (35)**, which is a substantial app-on-data story.

**Fairness guard (per TODO):** keep one combined row with vendor-specific labels —
`Lakebase / app database substrate` vs `Snowflake Postgres + Unistore / app-data bridge` —
and say Databricks leads on **branding/concentration**, not that Snowflake lacks an
operational-DB / app story.

---

## 4. NVIDIA / GPU / accelerated compute (side callout)

| | Databricks | Snowflake |
|---|---|---|
| Sessions matching GPU/NVIDIA/accelerated-compute | 12 (1.5%) | 3 (0.6%) |

**Verdict: the prior hypothesis holds — Databricks has meaningful GPU/accelerated-compute
presence; Snowflake's is incidental.** Databricks' 12 include genuinely accelerator-themed
sessions, at least one explicitly NVIDIA-partnered:

- *GPU-Accelerated Operations Research: Production-Grade Optimization with NVIDIA …*
- *AI Can't Wait: How to Overcome GPU Scarcity and Keep Workloads Running*
- *Coding with AI Agents to Supercharge Your Spark UDFs with GPU-Acceleration*
- *Train and Fine-Tune AI Models Without Managing GPUs*
- *Scaling Custom LLMs with vLLM and Databricks Model Serving*
- (also one **AMD**-sponsored CPU-efficiency talk)

Snowflake's 3 matches are incidental **model-serving** mentions (e.g. *Real-Time Lead
Prioritization with Snowflake Model Serving*), none NVIDIA-branded. Frame as: *Databricks
foregrounds raw accelerated compute and an explicit NVIDIA tie; Snowflake abstracts the GPU
away behind managed Cortex/serving.*

**Capability floor (do not over-claim):** Snowflake *does* have a real NVIDIA partnership —
NeMo Retriever, Triton, and NIM microservices run inside Cortex via Snowpark Container
Services, and Arctic is TensorRT-LLM-optimized ([Snowflake+NVIDIA PR](https://www.snowflake.com/en/news/press-releases/snowflake-and-nvidia-power-customized-ai-applications-for-customers-and-partners/)).
Databricks' is simply deeper on *raw compute* — H100 training, TensorRT-LLM serving, planned
native NVIDIA acceleration in Photon, serverless GPU jobs, Blackwell at GTC 2026
([deepen-collaboration PR](https://www.prnewswire.com/news-releases/databricks-and-nvidia-deepen-collaboration-to-accelerate-data-and-ai-workloads-with-the-data-intelligence-platform-302092139.html)).
So the 12-vs-3 gap is *agenda emphasis*, **not** "incidental bio mentions only."

---

## 5. Shared companies appearing in both catalogs (side callout)

**83 companies** field speakers at **both** summits (DBX 515 unique speaker-affiliations,
SNOW 416). These are the accounts/partners both vendors parade. Top of the overlap by
combined session presence:

| Company | DBX sessions | SNOW sessions |
|---|---:|---:|
| OpenAI | 6 | 9 |
| Accenture | 4 | 10 |
| Salesforce | 4 | 7 |
| Deloitte | 6 | 4 |
| EY | 2 | 6 |
| Workday | 5 | 3 |
| Anthropic | 5 | 2 |
| dbt Labs | 2 | 5 |
| Domo | 3 | 4 |
| Capital One | 1 | 5 |
| Morgan Stanley | 1 | 5 |
| Glean | 2 | 3 |
| Fivetran | 1 | 4 |
| Atlan | 1 | 4 |

**Read:** the overlap is dominated by (a) the **GenAI model labs** (OpenAI, Anthropic) —
both stages court the same foundation-model vendors; (b) the **GSI/consulting bench**
(Accenture, Deloitte, EY, Cognizant, Infosys); and (c) the **modern-data-stack tool
ecosystem** (dbt Labs, Fivetran, Atlan, Astronomer, Domo, Hex). **Fairness guard:** this is
*speaker affiliation* overlap, not a claim about who is a customer of whom — treat a company
appearing on one stage only as "absent from that catalog's speaker list," not as a
non-user.

---

## 6. Significant absences / asymmetries

Framed strictly as **absent from current catalog signals**, not absent as a
customer/partner:

- **Semantic layer (row 2):** Snowflake's **Semantic Views** (113 sessions, incl. 102
  feature-tagged) dwarf Databricks' **Metric Views / semantic models** (34, of which only 18
  say "metric view"). This is the clearest "named capability the other side barely surfaces"
  on the Snowflake side — semantic-context-for-agents is a Snowflake headline and a
  Databricks footnote *in the catalog*, even though UC Metric Views exist.
- **Named control plane (row 5):** mirror image — Unity Catalog saturates the Databricks
  agenda in a way Horizon does not for Snowflake.
- **BI/AI-BI (row 6):** Databricks' **AI/BI** (Genie/dashboards) is a much larger labeled
  presence (37.2%) than Snowflake's BI & Analytics track (14.7%).
- **Evals (row 8):** strict eval/benchmark/red-team/guardrail language is roughly **2.6×**
  more common on the Databricks agenda (11.2% vs 4.3%) — see audit 7.

---

## 7. Evals — strict vs broad (row 8)

The row counts **only** strict signals: `eval / evals / evaluation / benchmark / red team /
LLM-as-judge / guardrail`. Result: DBX 90 (11.2%), SNOW 23 (4.3%).

**Fairness guard:** do **not** conflate this with broad "trust / quality / responsible AI"
language, which is common on both sides (Snowflake's Governance/Compliance/Observability
covered-topics are large). The honest claim is narrow: *Databricks devotes materially more
agenda to explicit model **evaluation/red-teaming** mechanics; both vendors talk about trust
and quality broadly.*

**Capability floor (do not over-claim):** Snowflake *ships a productized eval stack* — it
acquired **TruEra/TruLens** (May 2024) and offers **AI Observability in Snowflake Cortex**
with LLM-as-a-judge, relevance, groundedness, and harmfulness metrics
([TruEra acquisition](https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/),
[Cortex AI Observability docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability)).
Databricks builds automated evaluation into **Agent Bricks** plus MLflow. So the 11.2-vs-4.3
gap is *how much each chose to put on the agenda*, **not** "Snowflake has no evals."
