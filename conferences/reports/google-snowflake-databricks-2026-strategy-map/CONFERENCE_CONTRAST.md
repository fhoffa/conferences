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

## Part 2 — same logos, different talks

83 companies presented at *both* summits. The interesting part isn't the overlap — it's that
the **same company often gets framed differently at each event**, because each vendor slots the
partner into its own story.

| Company | At Snowflake, it's about… | At Databricks, it's about… |
|---|---|---|
| **Fivetran** | Data engineering & pipelines (×4) | AI/BI (×1) |
| **dbt Labs** | Data engineering + cost/performance | AI & agents / AI-BI |
| **Microsoft** | Architectures & interoperability (×3) | Delta Sharing / interop (×1) |
| **Capital One Software** | Performance/cost + governance (×4) | Unity Catalog (×1) |
| **Anthropic** | Generative AI & agents (×2) | AI & agents **+ cybersecurity** (×5) |
| **OpenAI** | Spread across GenAI, industry, BI, data eng (×9) | AI & agents (×6) |

The pattern: at **Snowflake**, ecosystem partners are cast as **data-movement and
cost/governance** players; at **Databricks**, the same partners are recast as **AI/agent**
players. Microsoft is the neutral guest at both — invited specifically to say "interoperability."
And the model labs hedge across both stages, but with different intensity: **Anthropic leans
Databricks** (5 sessions to 2, including security talks), **OpenAI is courted slightly harder by
Snowflake** (9 to 6).

---

## Part 3 — who's in the room, and who isn't

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

---

## Guardrails (so "eye-opening" never tips into "wrong")
- Agenda emphasis ≠ capability. Don't say Snowflake "has no" evals/operational-DB/NVIDIA story,
  or that Databricks "isn't open." Each is contradicted by the vendor's own product
  (`VENDOR_POSITIONING_SOURCES.md`).
- A company's absence = no speaker this year, not a non-customer. Don't infer churn or rejection.
- Near-ties stay ties: pipelines (1.3pp) and sharing (4.3pp).
- Use the 802/537 (2026-06-13) basis; `DIFF_OLD_NEW.md` shows no leader flipped vs the older
  759/550 data, so the contrasts are stable.
