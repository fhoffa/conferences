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

## Spicy takes — how the two conferences differ

The nine differences, each grounded in the data below. Spicy, not mean: every one is about
*emphasis and audience*, not a vendor's competence.

1. **Snowflake Summit is a VP conference; Databricks is a practitioner conference.** 44% of
   Snowflake's customer talks put a VP-or-above on stage (vs 33% at Databricks) — and Databricks
   is the only one of the two where hands-on practitioners (35%) outnumber the execs.

2. **Databricks sells the build; Snowflake sells the outcome.** Databricks fills its stage with the
   people who construct the system — practitioners and architects, the governed substrate (Unity
   Catalog), the operational database. Snowflake fills its stage with the people who report the
   results — VPs and customers, the AI app surface, the semantic layer. You can read the whole
   split off one company: Novo Nordisk sent platform architects + Lakebase to Databricks and a VP
   of AI + CoWork to Snowflake — same company, same month, opposite half of the story.

3. **Customers tailor their story to each host.** It isn't just Novo Nordisk — across the ~85
   companies that present at both, the same logo routinely brings each conference the half of its
   program that fits the host's pitch (Fivetran is "pipelines" at Snowflake, "AI/BI" at
   Databricks; Capital One is "secure sharing" at Databricks, "Iceberg interoperability" at
   Snowflake).

4. **They barely share a guest list.** Of the ~790 distinct companies that took a speaking slot,
   only about 1 in 9 (~85) appeared at both. Two nearly separate universes of customers.

5. **Snowflake's BI story is a guest list; Databricks' is a product.** Third-party BI vendors take
   16 Snowflake slots to Databricks' 5; the modern-data-stack ecosystem, 23 to 7. Snowflake leans
   on partner ecosystems for those layers; Databricks brings more of them in-house.

6. **The only talks that play in both rooms are about not having to pick a room.** The near-verbatim
   repeat talks — Astronomer, ServiceNow, Tableau's Open Semantic Interchange — are all the
   semantic/context layer, engineered to be platform-neutral, so the slides port unchanged.

7. **Open table formats are a dead tie — they just use different ones.** Open formats touch ~10%
   of each agenda (Databricks on its open house format **Delta Lake**, Snowflake on **Iceberg**,
   the neutral standard it bet on). Equal airtime, different format — neither is "closed," and the
   "Snowflake leads openness" story was a counting artifact.

8. **Even the no-shows tilt.** Databricks-only logos skew tech and consumer (Mastercard, Adobe,
   Nubank, PepsiCo); Snowflake-only skew regulated and industrial (Toyota, Roche, BlackRock,
   Sanofi). Different rooms attract different rosters.

9. **Snowflake's marquee AI guest changed from NVIDIA to Anthropic.** The normalized Snowflake
   speaker-company field shows 0 NVIDIA breakout affiliations in 2024–2026, but the 2024 catalog
   still contains NVIDIA evidence (Bryan Catanzaro in `AI241`, Jensen Huang in keynote `K1`, plus
   BioNeMo / NeMo Retriever / accelerated-infrastructure mentions). So the safe read is narrower:
   in 2026, NVIDIA disappears from Snowflake breakout speaker/company signals while **Anthropic's
   Daniela Amodei** gets the marquee AI slot — and NVIDIA presents working sessions at
   **Databricks** (2 in 2026). The partnership lives on in both products (NeMo/NIM in Cortex;
   H100/TensorRT at Databricks), but Snowflake's headline AI guest shifted from chip vendor to
   model lab, from compute to agents.

*Full evidence, fairness caveats, and citations in the sections below.*

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
frames it as the build** (architects, Lakebase, 30× throughput, the semantic plumbing) and
**Snowflake frames it as the outcome** (an AI VP, CoWork, commercial impact). Even the
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

Reading the topic mix (share of each catalog, length-controlled symmetric keywords — see
`AUDITS.md §0`; rows overlap, so they don't sum to 100). **The 680-char chart tilts are modest** —
zero gaps clear 10pp — and some topic leaders change when the cap is relaxed, so treat these as
length-controlled agenda-emphasis reads:

- **Snowflake leans into the AI app surface and "meaning."** It edges Databricks on the GenAI /
  agent layer (**46% vs 42%**) and leads the **semantic layer** more clearly — Semantic Views /
  Cortex Analyst appear on **11%** of sessions vs **5%** for Databricks' Metric Views. Snowflake
  gave semantics its own Summit domain (Semantic Studio, Cortex Sense). The message: *the value
  is in making your data legible to agents.*
- **Databricks owns more of the operational-DB substrate** (**13% vs 5%** — the board's largest
  gap). Both tell the same "agents need an OLTP database" story (Lakebase vs Snowflake Postgres +
  Unistore); Databricks gives it more agenda real estate and its own track.
- **Governance is a dead tie — but the branding isn't.** Governance *coverage* is even (~27%
  each). What looks lopsided is the **product name**: "Unity Catalog" appears in ~20% of Databricks
  sessions vs "Horizon" in ~5% of Snowflake's. Unity Catalog is the connective tissue wiring
  Lakebase, Genie, Agent Bricks and Lakeflow together, so it is named in ~20% of Databricks sessions;
  Snowflake's governance rides on Horizon, named far more sparingly. Brand prominence, not a
  governance gap.
- **Smaller Databricks leans:** first-party AI/BI dashboards (**10.8% vs 7.1%** — a lean, not the
  rout the first draft implied) and explicit evals (**6.9% vs 3.9%**, ~1.8×; both ship it —
  Snowflake via TruEra/TruLens — only one headlines it).
- **Genuine ties:** open table formats (**10.5% vs 10.1%** — Databricks on Delta, Snowflake on
  Iceberg, equal airtime; `AUDITS.md §2`), data pipelines/streaming (**26.6% vs 25.1%**), and
  warehouse/modernization (**~10% each**). Claim no leader on these.

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

**First: is anyone outside the host even on stage?** Not always. Splitting every session by who
heads it (of talks with a named speaker):

- **Databricks — 37% host-led · 29% partner-led · 34% customer-led**
- **Snowflake — 20% host-led · 33% partner-led · 47% customer-led**

So no, it isn't "almost every talk has a guest." **Databricks keeps over a third of its agenda
in-house** — its own engineers presenting product depth — while **Snowflake fronts an outside
company in 4 of 5 sessions and a *customer* in nearly half of them.** Snowflake's stage runs on
customer proof points; Databricks' runs more on its own product team. The two lean on partners
about equally (~30%). And of the guest companies, roughly **3 in 4 are end customers**; about
**1 in 4 are vendors / partners / SIs** (a heuristic split: curated vendor list + the companies
named in "Sponsored by" titles + name markers, so the long tail of boutique SIs is caught).

**The rosters barely overlap.** Of ~**790** distinct companies that took a speaking slot across
the two events — names normalized to merge regional/legal variants (e.g. "AWS" = "Amazon Web
Services", "EY New Zealand" = "EY") — only **~85, about 1 in 9,** appeared at both. (The raw,
un-normalized speaker affiliations number ~850; the variant cleanup is why the count is
approximate.) Each conference is mostly its own universe of references.

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

## Part 5 — who they send (the org chart on stage)

> **The spiciest read of the two agendas: Snowflake Summit is pitched at the VP; Databricks is
> pitched at the practitioner — just look at who each lets on stage.** Among customer talks,
> **44% at Snowflake feature a VP-or-above, but only 28% put a hands-on practitioner up there.**
> At Databricks it flips: **35% feature a practitioner, 33% a VP+.** Snowflake's customer stage
> runs executives-to-builders **1.5 : 1**; Databricks runs **1.1 : 1** — essentially even.

Novo Nordisk sent architects to Databricks and an AI VP to Snowflake — and it wasn't a fluke.
Classifying the **job title of every customer speaker** (enterprises only — hosts, vendors, GSIs,
and field roles removed; DBX 607 / SNOW 516 speakers) confirms the tilt across the whole stage:

| Seniority tier | Databricks | Snowflake |
|---|---:|---:|
| C-suite | 17.8% | 20.0% |
| VP | 10.9% | 13.6% |
| Director / Head | 27.8% | 28.7% |
| Manager | 10.7% | 11.0% |
| Senior IC (principal/staff/lead) | 11.9% | 10.5% |
| IC / practitioner (engineer/architect/scientist) | 14.3% | 11.4% |

**First, the honest part: both stages are senior.** "Director / Head" is the single largest tier
at *both* events (~28%), and C-suite is ~1 in 5 at each. Neither conference is an engineering
meetup — these are decision-maker rooms.

**But the tilt is real and it points the way Novo Nordisk predicted.** The cleanest way to see it
is a **builder-to-buyer ratio** — practitioners (IC + senior IC) divided by executives (VP +
C-suite):

- **Databricks — 0.91 builders per buyer** (159 practitioners, 174 executives): nearly balanced.
- **Snowflake — 0.65 builders per buyer** (113 practitioners, 173 executives): execs outnumber
  builders about 3 to 2.

Databricks puts ~40% more builders per executive on stage. Snowflake is the more
executive-heavy room (C-suite + VP = 33.6% vs 28.7%).

**And even the executives are titled differently** — build vs outcome shows up in the C-suite too:

- **Databricks execs lean architecture/data-platform:** Chief Data & AI Officer, **Chief
  Architect**, VP of Data + AI Architecture, VP of Digital, Data & AI Foundation.
- **Snowflake execs lean strategy/innovation/product:** **Chief Innovation Officer**, SVP –
  Digital Strategy & Operations, VP of AI and Head of Product, VP of AI and Data Innovation.

So the people each conference attracts match the story it tells: Databricks fills the room with
the people who **architect and build**; Snowflake fills it with the people who **own the strategy
and report the outcome**. (Caveat: a tilt, not a chasm — and DAIS is still upcoming, so its
speaker list may shift.)

## The thesis (what survives all the receipts)

> **Databricks sells the build; Snowflake sells the outcome.**

Databricks spends its stage time on the *system* — its operational-DB substrate (Lakebase, the
board's biggest gap), its own analytics surface, evaluation on the main stage, the Unity Catalog
spine it names much more often than Snowflake names Horizon, and the engineers and architects who wire it together. Snowflake spends its stage
time on the *result* — the AI app surface, the semantic layer that makes data legible to agents, a
partner bench that handles BI and data movement, and the VPs and customers who report business
outcomes. Same destination, opposite half of the stack. Neither picture is the *whole* company —
it's the half each one chose to show.

It even shows in the seats (Part 5): Snowflake's stage is pitched at the **VP who buys the
outcome**; Databricks' at the **practitioner who builds it**. The story each sells and the
audience each courts are the same choice, made twice.

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
- Near-ties stay ties/leans: pipelines (1.4pp), sharing (2.7pp), and open formats (0.4pp).
- Use the 802/537 (2026-06-13) basis; `DIFF_OLD_NEW.md` shows no leader flipped vs the older
  759/550 data, so the contrasts are stable.
