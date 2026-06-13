# Databricks vs Snowflake: how their conferences differ

*An analyst's read of two 2026 agendas — Databricks Data + AI Summit (802 sessions) and
Snowflake Summit (537 sessions), captured 2026-06-13. We're not grading the companies; we're
reading what each agenda is **trying to say**. A session catalog is a curated message: the
topics a vendor schedules, and the partners it puts on stage, are the story it wants you to
walk away with. Every number traces to `classify.py` / `companies.py`; capability claims are
cited in `VENDOR_POSITIONING_SOURCES.md`.*

> **One rule keeps this honest:** the counts measure **agenda emphasis**, not capability. When
> one conference talks about something more, that's a choice about messaging — not proof the
> other vendor can't do it. We flag the capability floor wherever a gap could be misread.

---

## One company, two stages

The whole story compresses into a single customer. **Novo Nordisk** — one pharma company, one
data organization — presented at *both* summits within the same month. What it chose to talk
about at each, and *who it sent*, is a near-perfect read of what each vendor wants to be known for.

**At Databricks, Novo Nordisk sent its architects.** Two talks, both showcasing Databricks'
flagship 2026 launches, both *build* stories:
- *Modernizing Clinical Data Integration at Novo Nordisk With Lakebase* — replacing "fragmented,
  self-hosted Postgres silos" with **Lakebase** (Databricks' new operational database) for "30×
  faster" data availability. Speakers: platform & domain architects.
- *Empowering Non-Technical Users in Pharma With Dashboards and Chatbots* — **Genie + Agent
  Bricks** over a Unity Catalog semantic layer. Speaker: Principal IT Solution Architect.

**At Snowflake, Novo Nordisk sent its AI VP.** One talk, showcasing Snowflake's flagship 2026
launch, a *business-outcome* story:
- *Move Beyond Prototypes to High-Velocity AI Products Using Snowflake CoWork* — **CoWork**
  (Snowflake's flagship agent) with Cortex Analyst & Search, framed around a "NovoMind" operating
  model and "commercial AI products that directly impact our field." Speakers: VP – AI Foundation;
  Associate Director.

Same company, same underlying reality — governed AI on regulated pharma data. But **Databricks
frames it as operability** (architects, Lakebase, 30× throughput, the semantic plumbing) and
**Snowflake frames it as legibility and outcomes** (an AI VP, CoWork, commercial impact). Even the
*speakers* each vendor recruited carry the message: Databricks gets the people who **build** the
platform; Snowflake gets the people who **report results** to the business. One customer, two
stages, and you can read each company's entire positioning off which Novo Nordisk talk you walk
into.

---

## The headline

Stand both agendas side by side and they're selling different halves of the same idea — an AI
layer on a governed lakehouse. **Snowflake's agenda foregrounds the AI surface and the meaning
layer.** **Databricks' agenda foregrounds the governed substrate and the tooling around it.**
You can see it in the topics, in how the same companies are framed, and in who's invited.

---

## Part 1 — what each conference puts in the spotlight

Reading the topic mix (share of each catalog; rows overlap, so they don't sum to 100):

- **Snowflake leans into the AI app surface and "meaning."** Cortex/agents touch **68.9%** of
  its agenda vs Databricks' 51.6%. The sharper signal is the **semantic layer**: Snowflake's
  Semantic Views appear on **21%** of sessions vs **4%** for Databricks' Metric Views. Snowflake
  gave semantics its own Summit domain (Semantic Studio, Cortex Sense). The message: *the value
  is in making your data legible to agents.*
- **Snowflake also brands "open" the loudest.** Iceberg / open-lakehouse shows up on **28.7%**
  of its agenda vs **6%** for Databricks. Worth stating plainly so the gap isn't misread:
  Databricks is *not* closed — it open-sourced Unity Catalog (Apache 2.0) and ships Delta
  UniForm so one copy reads as Iceberg. Iceberg is simply Snowflake's billboard and Databricks'
  default setting. (`VENDOR_POSITIONING_SOURCES.md §4`)
- **Databricks leans into the governed substrate.** Unity Catalog appears on **56%** of its
  sessions — the most omnipresent single product at either event. That's because it's the
  connective tissue: it's how Lakebase, Genie, Agent Bricks, and Lakeflow are wired together.
  Snowflake has no single product playing that narrative role; its governance is carried by
  Horizon, a full control plane that simply isn't repeated on every slide.
- **Databricks brings its own analytics surface.** First-party AI/BI (Genie + Dashboards) is on
  **37%** of its agenda vs **15%** for Snowflake — because Snowflake, by design, leaves the
  dashboard to partners (more on that below) and invests in the semantic layer underneath.
- **Both arrived at the same operational-database conclusion.** Databricks' Lakebase and
  Snowflake's Postgres + Unistore tell the same "agents need an OLTP database" story; Databricks
  simply gives it more agenda real estate (25.7% vs 17.1%) and its own track.
- **Evals: on the main stage vs inside the product.** Databricks puts evaluation/red-teaming on
  the agenda 2.6× more (11.2% vs 4.3%). Snowflake keeps it productized (Cortex AI Observability,
  the TruEra/TruLens lineage) rather than foregrounded. Both ship it; only one headlines it.
- **A genuine tie:** data pipelines/streaming — 34.8% vs 36.1%, within noise.

---

## Part 2 — same customer, different chapter of their story

The most revealing slice isn't the vendors — it's the **end-customers** who present at *both*
summits. These are enterprises with one data program, yet they walk on stage and tell a
**different chapter** depending on whose conference it is. The talk title they pick is a tell:
it's the part of their story that fits the host's narrative.

| Customer | On the Databricks stage | On the Snowflake stage |
|---|---|---|
| **Capital One** | Secure data collaboration | Multi-catalog **Iceberg interoperability** |
| **Coinbase** | Real-time **fraud feature serving** | **Growth-marketing** BI |
| **Barclays** | Equities-platform **migration** | Enterprise **observability** |
| **GSK** | Scaling **Genie 10×** (conversational analytics) | Clinical supply-chain innovation |
| **Novo Nordisk** | Dashboards + **Lakebase** clinical data | Agents via **Snowflake CoWork** |
| **Johnson & Johnson** | "Molecule to market" life-sci AI | Open-source **Native Apps** for drug discovery |
| **Disney** | Real-time **streaming** architecture (DATOS) | Audience-flow app |
| **NBCUniversal** | AI ad/content alignment | **Synthetic data** + privacy |
| **AT&T** | *(industry-forum panel)* | **Iceberg** journey + **agentic** telecom (×3) |
| **Morgan Stanley** | *(industry-forum panel)* | **FinOps** at scale + resilience (×5) |

**The pattern mirrors Part 1 exactly — from the customer's mouth.** When these companies bring a
talk to **Databricks**, it skews engineering-deep: streaming (Disney, Coinbase, 8451),
Genie/AI-BI (GSK, Comcast, Centene), Lakebase (Warner Music, Novo Nordisk), migrations (Barclays).
When the *same* companies bring a talk to **Snowflake**, it skews openness-and-meaning:
Iceberg/interoperability (Capital One, AT&T, Goldman Sachs), Cortex/CoWork agents (Novo Nordisk,
Cummins, AT&T), data sharing/marketplace (Goldman, J&J, Nokia), and FinOps/cost (Morgan Stanley,
Northern Trust, 8451). The customers self-select into each platform's flagship story.

**The honest counterpoint:** a few customers tell the *same* story everywhere. **Goldman Sachs**
brings an "open, interoperable Iceberg lakehouse" talk to both; **Block** brings "build a data MCP
for analytics agents" to both. Some enterprises have a platform-agnostic thesis (open lakehouse,
MCP) they'll repeat regardless of host — and that's worth showing too.

**One fairness caveat on counts:** Snowflake Summit already happened (final agenda); Databricks
DAIS is still upcoming (June 15–18), so customers currently shown only on a Databricks
industry-forum panel (Morgan Stanley, AT&T, DirecTV) may yet add dedicated talks. Read the
**topic divergence** as the durable signal, not the session tally.

*(The ecosystem vendors diverge the same way: Fivetran is a "pipelines" story at Snowflake but
"AI/BI" at Databricks; dbt is "data engineering" at Snowflake, "AI & agents" at Databricks;
Microsoft is the neutral "interoperability" guest at both. Anthropic leans Databricks 5-to-2;
OpenAI leans Snowflake 9-to-6.)*

---

## Part 3 — the talks that play in both rooms

Flip the question around. Instead of who tells a *different* story at each event, who tells the
**exact same one** — sometimes the same slides? A near-duplicate-title check across the shared
companies surfaces a small, revealing club:

| Company | The talk (near-identical at both) | Similarity |
|---|---|---|
| **Astronomer** | "Your AI Strategy Has a Context Problem. Orchestration Solves It." | 0.86 |
| **ServiceNow** | "The Patchwork Enterprise Is Holding Your AI Agents Back" | 0.83 |
| **Salesforce / Tableau** | "Demystifying the Open Semantic Interchange (OSI)" — swap only the host name | 0.71 |
| **IBM** | "…Real-time Context for AI…" | 0.57 |
| **Atlan** | "The Enterprise Context Layer… Demystified and Demoed" | 0.56 |
| **Capital One Software** | "Using Context and AI for Cost Optimization and Security" | 0.88 |

**Look at what they're all selling: context.** Astronomer ("context problem"), Atlan ("enterprise
context layer"), IBM ("real-time context"), Capital One Software ("context and AI"),
Salesforce/Tableau (the semantic interchange), ServiceNow (stitching the "patchwork enterprise"
so agents can use it). Every twin talk is about the **semantic / context / governance layer that
feeds AI agents** — the layer that sits *above* whichever lakehouse you bought. And that's exactly
why the talk ports unchanged: if your product's whole job is to make the platform underneath
interchangeable, your pitch doesn't change when the logo on the lanyard does.

**There's even a standard for it.** Several of these names — Salesforce/Tableau, Atlan, plus
Sigma, Hex, ThoughtSpot, Omni, Alation from Part 4 — are founding members of the **Open Semantic
Interchange (OSI)**, a vendor-neutral semantic-model spec launched September 2025 by Snowflake,
Salesforce, dbt Labs, and BlackRock so one definition of "revenue" works across any BI or AI tool.
([Snowflake announcement](https://www.snowflake.com/en/news/press-releases/snowflake-salesforce-dbt-labs-and-more-revolutionize-data-readiness-for-ai-with-open-semantic-interchange-initiative/),
[dbt on the OSI spec](https://www.getdbt.com/blog/the-osi-spec-updates)) OSI is the literal
embodiment of the pattern: a layer engineered to be platform-agnostic, presented identically to
both platforms' audiences.

**And the customers echo it one layer down.** The enterprises that *don't* change their story
(Part 2) are doing the same thing at the storage and access layers: **Goldman Sachs** brings "open,
interoperable Iceberg lakehouse" to both; **Workday** brings "governed agentic AI on Iceberg +
context/semantics" to both; **Block** brings "build a data MCP for analytics agents" to both. Open
table format (storage), semantic layer (meaning), MCP (agent access) — three portable layers,
three repeatable talks.

**The takeaway:** where the two conferences *disagree* is the platform itself. Where they
*converge* is everything built to sit above it — Iceberg, the semantic/context layer, and MCP. The
companies that can give one talk to both rooms are precisely the ones whose business is making the
room you're in not matter.

## Part 4 — who's in the room, and who isn't

**The rosters barely overlap.** Of ~**848** distinct companies that took a speaking slot across
the two events, only **83 (under 10%)** appeared at both. Each conference is mostly its own
universe of references.

**The partner mix quietly confirms the strategy split:**

- **Third-party BI/viz vendors cluster at Snowflake** — Sigma, Hex, ThoughtSpot, Qlik, Omni
  total **~16 sessions at Snowflake vs ~5 at Databricks**. This is the partner-side mirror of the
  BI topic gap: Snowflake's dashboard story *is* its partner ecosystem, so those logos fill the
  stage. Databricks brings AI/BI in-house, so it needs fewer of them.
- **The "modern data stack" is a Snowflake gathering** — Fivetran, dbt, Atlan, Monte Carlo,
  Alation, Coalesce total **~23 sessions at Snowflake vs ~7 at Databricks**. Databricks
  internalizes ingestion, transformation, and catalog (Lakeflow, Unity Catalog), so the
  independent tools have less to plug into.
- **Databricks courts the AI-app builders more** — Replit, LangChain, LlamaIndex, Lovable,
  CrewAI, Glean total **11 sessions at Databricks vs 7 at Snowflake**. The builder/developer
  crowd skews to the Databricks stage; Cursor is a Snowflake guest.
- **The clouds show up at their aligned house** — Google Cloud appears at Databricks (not
  Snowflake); AWS appears at Snowflake (not Databricks); Microsoft plays neutral interop guest
  at both.

**And who's simply absent** (read gently — a missing logo means "no speaker this year," not
"not a customer"): the customer rosters have different texture. Databricks-only names skew
tech/platform and consumer (Mastercard, Adobe, Atlassian, Nubank, PepsiCo, Adidas); Snowflake-only
names skew regulated-enterprise and industrial (Toyota, Roche, BlackRock, Sanofi, Medtronic,
Truist, Booking.com). It's a soft tilt, not a hard line — but it's the kind of thing that shows
up when you read the room rather than the press release.

---

## The thesis (what survives all the receipts)

> **Snowflake's conference sells legibility; Databricks' conference sells operability.**

Snowflake spends its stage time making data *legible* — to agents (semantics), to the open
ecosystem (Iceberg), and through a partner bench that handles BI and data movement. Databricks
spends its stage time making AI *operable* — one governed control plane (Unity Catalog), its own
analytics and operational-DB surfaces, and evaluation on the main stage. Same destination,
opposite emphasis. Neither picture is the *whole* company — it's the half each one chose to show.

And the kicker (Part 3): the two stages disagree about the platform but quietly **agree about the
layers above it** — open table formats, the semantic/context layer, and agent access. The handful
of companies that give the identical talk in both rooms are the ones building that neutral layer.
The platform war is loud; the layer above it is already being standardized in public.

---

## Guardrails (so "eye-opening" never tips into "wrong")
- Agenda emphasis ≠ capability. Don't say Snowflake "has no" evals/operational-DB/NVIDIA story,
  or that Databricks "isn't open." Each is contradicted by the vendor's own product
  (`VENDOR_POSITIONING_SOURCES.md`).
- A company's absence = no speaker this year, not a non-customer. Don't infer churn or rejection.
- Near-ties stay ties: pipelines (1.3pp) and sharing (4.3pp).
- Use the 802/537 (2026-06-13) basis; `DIFF_OLD_NEW.md` shows no leader flipped vs the older
  759/550 data, so the contrasts are stable.
