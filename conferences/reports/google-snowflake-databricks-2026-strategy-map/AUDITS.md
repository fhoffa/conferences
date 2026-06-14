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

## 0. Methodology — why the margins are smaller than the first draft

The mirrored chart uses **length-controlled symmetric keywords**: the same keyword set
(concept terms + every vendor's product names) is applied to **both** vendors, over each
session's title+abstract **capped at 680 characters** for the primary chart. Because that cap is a methodological choice, §0a below shows the sensitivity at Databricks' median length (991 chars) and at full text.

This corrects two biases in the earlier taxonomy-based draft:
1. **Taxonomy breadth.** Mixing each vendor's native tags (Databricks `topic_tags`/`track`,
   Snowflake `attributes`) credited whichever side had the broader tag. Snowflake's
   "AI Agents / Data Agents" covered-topic is auto-applied to 291 sessions; Databricks' "AI/BI"
   and "Unity Catalog" tags are similarly broad. This inflated margins in **both** directions —
   it overstated Snowflake's GenAI (+17→+5) and semantic (+17→+6) leads *and* Databricks' BI
   (+22→+4) lead.
2. **Abstract length.** Databricks abstracts run ~1.45× longer than Snowflake's (median 991 vs
   680 chars), so plain keyword counts over-credit Databricks. Capping both at 680 neutralises it.
3. **Brand-vs-brand rows.** Two rows compared a Databricks-only product name against a
   Snowflake-only one — Delta vs Iceberg (§2) and Unity Catalog vs Horizon (§1). Counting only the
   brands made each look lopsided; measured as *concepts* (open formats; governance) both are ties.

**Net effect at the 680-char cap:** margins shrink ~3× and the two agendas are strikingly close — **no topic gap
exceeds ~8pp** (the largest is operational DB, +8.3). These are cap-sensitive agenda-emphasis
findings, not absolute topic-volume facts: Snowflake leads the GenAI app layer only under the
680-char length-control, while governance/pipelines/BI/evals swing more Databricks-heavy as the
cap is relaxed. The robust read is modest tilts, not dominance. Governance and open formats are
ties under the primary fair chart.

*(Speaker/company findings — VP-vs-practitioner, who-heads-talks, twin talks, guest split,
roster overlap — are unaffected: they key on titles and affiliations, not abstract keywords.)*

### 0a. Cap sensitivity — which claims are stable?

The primary chart caps both catalogs at **680 characters** (Snowflake median title+abstract length).
That is a fair length-control choice, but some claims are sensitive to it. Re-running the same
symmetric keyword matcher at **991 characters** (Databricks median) and with **full text** gives:

| Row | 680-char primary | 991-char sensitivity | Full-text sensitivity |
|---|---|---|---|
| GenAI app layer | SNOW +4.7 | DBX +0.5 | DBX +1.8 |
| Semantic context | SNOW +6.4 | SNOW +5.3 | SNOW +5.3 |
| Sharing / marketplace | SNOW +2.7 | SNOW +1.5 | SNOW +1.4 |
| Open formats | DBX +0.4 | DBX +3.4 | DBX +4.2 |
| Governance / control plane | SNOW +0.9 | DBX +7.5 | DBX +8.7 |
| BI / AI-BI | DBX +3.8 | DBX +6.5 | DBX +6.8 |
| Operational DB substrate | DBX +8.3 | DBX +10.7 | DBX +10.9 |
| Evals / red teaming | DBX +2.9 | DBX +6.3 | DBX +6.9 |
| Pipelines / streaming | DBX +1.4 | DBX +6.8 | DBX +7.8 |
| SQL modernization | DBX +0.1 | DBX +1.9 | DBX +2.5 |

**What survives:** semantic context stays Snowflake's clearest topic lead; operational DB stays
Databricks' clearest lead; sharing stays a small Snowflake lean; BI/evals/pipelines stay
Databricks leans. **What must be qualified:** GenAI flips from Snowflake +4.7 at the 680-char cap
to Databricks +0.5/+1.8 when more Databricks abstract text is admitted; governance shifts from a
680-char near-tie to a Databricks lead under longer text. So write "under the 680-char
length-controlled method" for cap-dependent claims, not universal truths.

---

## 1. Governance / control plane (row 5) — count the topic, not the brand

**Governance coverage is a tie; the brand naming is not.** The earlier "Unity Catalog vs Horizon"
row counted only the two **product names** — but those are vendor-exclusive ("Unity Catalog" is
Databricks-only, "Horizon" Snowflake-only), so it measured *which brand gets repeated*, not who
covers governance. That's the same brand-vs-brand trap as the Iceberg row (§2). Measured fairly:

| Signal (length-controlled) | Databricks | Snowflake |
|---|---|---|
| **Governance as a concept** (governance, lineage, access control, RBAC, masking, compliance…) | **26.7%** | **27.6%** → **tie (SNOW +0.9)** |
| Bare "governance" | 21.2% | 21.4% |
| **Brand: "Unity Catalog" vs "Horizon"** | **19.6%** | **4.7%** |

**Verdict:** governance *coverage* is even under the 680-char chart — both conferences put it on
~27% of the agenda. What looks like a 4-to-1 Databricks blowout is **brand repetition**:
Unity Catalog is the Databricks platform *spine* (it wires Lakebase, Genie, Agent Bricks,
Lakeflow together), so it is named in ~20% of sessions; Snowflake's Horizon is named far more
sparingly. Report the two things separately: **governance topic = near-tie under the primary
cap**; **named-catalog brand prominence = Databricks by 4×.** Do not let the second masquerade
as the first.

**Capability floor (cited):** **Horizon Catalog** is itself a full control plane —
cross-cloud RBAC, Trust Center, differential privacy, clean rooms, AI Agent Identity, and
AI security posture management — re-announced and expanded on 2026-06-02
([product page](https://www.snowflake.com/en/product/features/horizon/),
[press release](https://www.snowflake.com/en/news/press-releases/snowflake-advances-trusted-ai-with-snowflake-horizon-catalog-centralizing-governance-context-and-security-across-the-enterprise/)).
Unity Catalog's naming prominence reflects its role as the Databricks platform spine, not a
governance gap at Snowflake.


---

## 2. Open lakehouse / table formats (row 4) — count Delta *and* Iceberg

**Delta Lake is an open-source table format too** (Linux Foundation / Apache 2.0), so a fair
"open formats" row must count it alongside Iceberg. The earlier draft counted only "Iceberg"
*and* gave Snowflake credit from its native feature/track tags while Databricks got
keyword-only — that double-penalised Databricks and produced a misleading 6%-vs-28.7% gap. The
corrected row uses the **same keyword set on both vendors** (delta lake, uniform, iceberg, hudi,
parquet, polaris, "open table/lakehouse", interoperability):

| Signal | Databricks | Snowflake |
|---|---|---|
| **Open lakehouse / formats (row 4, length-controlled)** | **84 (10.5%)** | **54 (10.1%)** → **tie** |
| "Delta Lake" (raw mention rate) | 11.6% | 0.4% |
| "Iceberg" (raw mention rate) | 4.0% | 8.4% |

**Verdict: it's a tie — both conferences run on open table formats, they just use different
ones.** Under the fair method (count Delta, control for length) the row is **DBX 10.5% vs SNOW
10.1%** — dead even. The composition differs: Databricks' open formats are **Delta Lake**
(11.6% of its agenda), Snowflake's are **Iceberg** (8.4%). Snowflake bet on the
**industry-neutral** format; Databricks emphasizes its own (open) Delta and bridges to Iceberg
via UniForm.

**Fairness guard:** keep this row **separate from governance** (row 5). Do **not** say Snowflake
"leads openness" or that Databricks is "closed" — open-format airtime is **equal**. The real
difference is *which* open format: neutral (Iceberg) vs house (Delta). The earlier "6% vs 28.7%
Snowflake-leads-openness" gap was an artifact of counting only "Iceberg" and giving Snowflake
taxonomy credit.

**Capability floor (cited):** Databricks **open-sourced Unity Catalog (Apache 2.0)**, ships
**native Apache Iceberg managed tables**, and **Delta UniForm** exposes one copy as
Iceberg/Hudi to Trino, Dremio, DuckDB, and Snowflake
([Databricks PR](https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open),
[UC managed tables docs](https://docs.databricks.com/aws/en/tables/managed)). Snowflake reads/writes
Iceberg and donated Polaris to Apache. **Both are genuinely open** at the table-format layer.

---

## 3. App / operational database substrate — Lakebase vs Snowflake Postgres + Unistore (row 7)

| Signal | Databricks | Snowflake |
|---|---|---|
| Combined row | 105 (13.1%) | 26 (4.8%) |
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

| NVIDIA-the-company breakout sessions (catalog) | Databricks | Snowflake |
|---|---|---|
| 2024 | — | **0** |
| 2025 | — | **0** |
| 2026 | **2** | **0** |
| GPU/accelerated-compute keyword sessions (2026) | 12 (1.5%) | 3 (0.6%) |

**The precise read — Snowflake's marquee AI guest changed from NVIDIA to Anthropic, while
NVIDIA's breakout-session signal is absent from the normalized Snowflake speaker-company field.**
The normalized `company` field shows 0 NVIDIA-affiliated Snowflake breakout speakers in 2024,
2025, and 2026, but that field is incomplete in 2024: `AI241` names Bryan Catanzaro from Nvidia
in the abstract, `K1` includes Jensen Huang / NVIDIA in the keynote, and several 2024 sessions
mention BioNeMo, NVIDIA accelerated infrastructure, or NeMo Retriever. So do **not** write
"NVIDIA was never in the Snowflake catalog." The safer claim is narrower: in 2026, NVIDIA is
absent from Snowflake breakout speaker/company signals while Anthropic gets the marquee AI slot;
Databricks, meanwhile, has two 2026 NVIDIA working sessions. Read it as Snowflake's headline AI
guest shifting *up the stack*, from the **chip vendor** (compute) to the **model lab** (agents) —
the "abstract the GPU, sell the agent" posture the rest of this map shows. **Fairness guard:**
this is about catalog/keynote emphasis, not the partnership — which is alive in both products
(capability floor below). Don't write "NVIDIA dumped Snowflake"; write "Snowflake's headline AI
guest moved from the chip vendor to the model lab."

**Databricks' 12 GPU/accelerator sessions** include genuinely accelerator-themed talks, at least
one explicitly NVIDIA-partnered (and NVIDIA staff present two of them):

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

About **85 companies** field speakers at **both** summits — out of ~790 distinct organizations
across the two events (after merging regional/legal name variants like "AWS"/"Amazon Web
Services"; raw un-normalized affiliations number ~515 DBX / ~416 SNOW). These are the
accounts/partners both vendors parade. Top of the overlap by combined session presence:

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

- **Semantic layer (row 2):** Snowflake's **Semantic Views / Cortex Analyst** (11.2%) lead
  Databricks' **Metric Views** (4.7%) — Snowflake's clearest real lead after the AI app layer.
  Semantic-context-for-agents is a Snowflake headline and a Databricks footnote *in the catalog*,
  even though UC Metric Views exist.
- **Named-catalog branding (not governance):** Unity Catalog is named in ~20% of Databricks
  sessions vs Horizon's ~5% — but governance *coverage* is a tie (~27% each, §1). Brand
  prominence, not a topic gap.
- **BI/AI-BI (row 6):** Databricks' **AI/BI** (Genie/dashboards) is a *lean*, not a rout —
  10.8% vs 7.1% once length-controlled (the taxonomy draft's 37% vs 15% was an AI/BI-tag
  artifact).
- **Evals (row 8):** strict eval/benchmark/red-team/guardrail language is roughly **1.8×**
  more common on the Databricks agenda (6.9% vs 3.9%) — see audit 7.

---

## 7. Evals — strict vs broad (row 8)

The row counts **only** strict signals: `eval / evals / evaluation / benchmark / red team /
LLM-as-judge / guardrail` (length-controlled). Result: DBX 55 (6.9%), SNOW 21 (3.9%).

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
Databricks builds automated evaluation into **Agent Bricks** plus MLflow. So the 6.9-vs-3.9
gap is *how much each chose to put on the agenda under the 680-char chart*, **not** "Snowflake
has no evals."
