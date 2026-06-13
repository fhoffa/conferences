# Snowflake vs. Databricks: two theories of the AI data stack

> **External-review draft.** This is a narrative/fairness draft, not a final publication draft. The Databricks and Snowflake catalogs were refreshed on 2026-06-13, so the denominators below are current, but the fractional pillar percentages and visual data still need to be recomputed before publication. See `EXTERNAL_REVIEW_TODO.md`.

_Subtitle: I treated public conference agendas as strategy documents to compare how Snowflake Summit and Databricks Data + AI Summit are positioning enterprise AI — with Google Cloud Next as a reference case._

Everyone in enterprise data now says the same words.

Agents. Governance. Apps. Lakehouse. Real time. Open formats. Security. Industry solutions. RAG. Semantic layers. Evals.

That is why most AI conference recaps blur together. If you only ask whether a vendor mentioned AI, everyone looks like they are telling the same story.

But Snowflake Summit and Databricks Data + AI Summit are not telling the same story.

They are the two conferences that feel most directly comparable: two data-platform companies, two large enterprise audiences, two aggressive AI narratives, and two competing claims on what the modern data stack becomes next.

So I treated the conference agenda as the strategy document.

Current public catalog basis:

- Databricks Data + AI Summit 2026: **802 sessions**
- Snowflake Summit 2026: **537 sessions**
- Google Cloud Next 2026: **1,160 sessions**, used as a cloud/AI platform reference point

That is **2,499 sessions** total.

The result is not a measurement of product quality. It does not prove who has the better warehouse, lakehouse, model serving layer, agent framework, semantic layer, or app substrate.

It shows what each vendor chooses to emphasize when it has a conference-sized stage.

And the Snowflake vs. Databricks split is sharper than the shared AI vocabulary suggests.

The short version:

- **Databricks is betting on the messy middle where AI demos become production systems.** Its agenda points toward governance, pipelines, analytics, streaming, orchestration, evals, Lakebase, apps, and AI operating together.
- **Snowflake is betting that governed enterprise data becomes a business application layer.** Its agenda points toward Cortex, Snowflake Intelligence, semantic/business-facing AI, apps, marketplaces, sharing, connectors, and governed workflows.
- **Google is the useful reference case.** It shows what an AI-native cloud/platform conference looks like when the center of gravity is models, agents, protocols, infrastructure, security, and ecosystem.

The spicy version:

> Google sells possibility. Databricks sells the build. Snowflake sells the outcome.

(Databricks fills its stage with the people and products that *construct* the system; Snowflake fills its with the people and products that *report the result*. More on that below — it shows up in the topics, the partners, and even the job titles on stage.)

For Snowflake vs. Databricks, that means the real fight is not “who has AI?”

They both do.

The real fight is: **does enterprise AI attach to the governed lakehouse operating system, or does it attach to the governed business data cloud?**

## How I counted it (and the traps I had to climb out of)

Counting conference topics fairly is harder than it looks, and the first few methods I tried were quietly unfair. The honest method has one rule: **measure both vendors the exact same way.**

Concretely, for each topic (agents, governance, semantic layer, open formats, operational DB, evals, …) I apply the **same keyword set to both catalogs** — concept terms plus *every* vendor's product names — and count a session if its title+abstract matches. A row's "agenda share" is just matching sessions ÷ that vendor's total.

Two non-obvious biases nearly fooled me, and both inflate one side without you noticing:

1. **Don't trust the vendors' own taxonomies.** Each catalog ships topic tags, but they're applied with wildly different breadth (Snowflake auto-tags "AI Agents" onto ~290 sessions; Databricks tags "Unity Catalog" onto hundreds). Mixing those tags into the count inflated whichever vendor had the broader tag — in *both* directions.
2. **Control for abstract length.** Databricks' session abstracts run ~1.45× longer than Snowflake's (median 991 vs 680 characters). Longer text → more keyword hits → Databricks looks bigger on everything. I cap every abstract at 680 characters before matching, so each session gets equal airtime.
3. **Beware brand-vs-brand rows.** Two comparisons looked like blowouts but were just one vendor repeating its own product name: "Delta vs Iceberg" and "Unity Catalog vs Horizon." Counted as *concepts* (open table formats; governance) instead of brand names, both are ties.

Net effect: the margins are about **3× smaller** than my first (taxonomy-based) draft, and several "obvious" gaps vanish. That's not a weaker story — it's a truer one. The differences that survive are about *emphasis and audience*, not capability.

(Denominators: Databricks **802**, Snowflake **537**, Google **1,160**, captured 2026-06-13. The full per-row table, the classifier, and a stability check against an older snapshot are in the companion files.)

## The headline: Databricks owns the production loop; Snowflake owns the business translation layer

At the pillar level, Databricks and Snowflake look closer to each other than either looks to Google. Both are talking about AI, governance, data movement, analytics, apps, open data, and business use cases.

But the shape is different.

Databricks is more balanced. Its agenda feels like an operating loop:

Data comes in. It is governed. It moves through pipelines. It is queried and modeled. It becomes BI, apps, agents, and production workflows. Then it is monitored, evaluated, and governed again.

Snowflake is more directional. Its agenda pushes governed data toward business-facing surfaces:

Cortex, Cortex Agents, Snowflake Intelligence, Cortex Analyst, Streamlit, Native Apps, Marketplace, Horizon Catalog, Dynamic Tables, Snowpark, Snowflake Postgres, Unistore, and industry solutions.

That leads to a simple distinction:

> Databricks sells the build; Snowflake sells the outcome.

One caveat to keep this honest (it's the whole point of the analysis): measured fairly — the *same* keyword set applied to both vendors, over abstracts capped to the same length so Databricks' longer write-ups don't over-count — **the two agendas are remarkably close. No single topic gap exceeds ~8 points.** The tilts are real but modest: Snowflake leans to the AI app surface and the semantic layer; Databricks leans to the operational-database substrate. Several rows people *assume* are blowouts — governance, open formats, pipelines — are statistical ties.

## Databricks: where AI demos go to become production systems

Databricks' advantage is not that it says “agents” more loudly than everyone else.

Its advantage is that it lives in the unglamorous middle where AI systems have to become repeatable, governed, tested, fresh, and useful.

The strongest evidence to review is the production-discipline cluster:

- Unity Catalog / governance / lineage
- Lakeflow / streaming / real-time pipelines
- Databricks SQL / AI/BI / Genie / Metric Views
- MLflow / evals / traces / Agent-as-Judge / red teaming
- Databricks Apps and production application surfaces
- Lakebase and app/operational database substrate signals

That is the Databricks thesis hiding inside the agenda.

Not just AI. AI with consequences.

Who owns the pipeline? Who owns the catalog? Who owns the evals? Who owns the dashboard? Who owns the operational database? Who owns the agent when it breaks?

Databricks wants the answer to be: the same governed data/AI operating system.

This is why the conference is best for:

- data engineers
- ML engineers
- analytics engineers
- lakehouse/platform owners
- AI platform teams
- governance and data quality teams
- teams responsible for production pipelines, streaming, lineage, evals, and operational data systems

The core attendee question is:

> How do we make AI/data systems actually work in production?

More specifically:

- How do we make AI work on top of governed enterprise data?
- How do we connect data engineering, analytics, ML, and agents into one operating loop?
- How do we evaluate AI outputs before they affect customers or business processes?
- How do we stream fresh data into AI and analytics systems?
- How do we govern access, lineage, data quality, and model behavior together?
- How do Unity Catalog, Lakeflow, MLflow, Mosaic AI, Databricks SQL, AI/BI Genie, Apps, and Lakebase fit into one platform?

The hidden anxiety behind the Databricks attendee is:

> We can build AI demos. But can we operate them safely, repeatedly, and at enterprise scale?

That is why Databricks' “boring middle” may be its strongest strategic position.

Google has the biggest AI halo. Snowflake has the cleanest business-app translation. Databricks sits in governance, SQL, pipelines, BI, streaming, evals, orchestration, ML lifecycle, and app data systems.

That is not as glamorous as a model keynote.

It may be more durable.

## Snowflake: governed data becomes business-facing AI

Snowflake's agenda is AI-heavy, but its more interesting signal is not raw AI volume.

It is where the AI points.

Snowflake's differentiator is the semantic/business-facing layer:

- Cortex and Snowflake Intelligence as enterprise AI interfaces
- Cortex Analyst and semantic context for agentic analytics
- Streamlit and Native Apps as application surfaces
- Marketplace, sharing, and clean rooms as distribution patterns
- Horizon Catalog as governance/context around the AI Data Cloud
- Snowflake Postgres, Unistore, Hybrid Tables, streaming, and Dynamic Tables as operational/app-data bridges
- industry solutions as the business packaging layer

That makes the Snowflake story less like “we have an AI engineering platform” and more like:

> Governed enterprise data is becoming an app surface.

That is the connective tissue between Cortex, Snowflake Intelligence, Cortex Analyst, Streamlit, Native Apps, Marketplace, Horizon Catalog, Dynamic Tables, Snowpark, Snowflake Postgres, Unistore, and industry solutions.

Snowflake is not just selling infrastructure for builders. It is trying to package AI in ways that business teams can understand: departments, workflows, governed data products, industry contexts, analytics experiences, and applications.

This is why Snowflake Summit is best for:

- data leaders
- analytics and BI leaders
- business application builders
- enterprise workflow owners
- CIO/CDO/VP Data types
- teams trying to turn governed data assets into apps, decisions, and business processes
- operations, finance, marketing, risk, supply chain, healthcare, retail, financial services, and other domain leaders

The core attendee question is:

> How do we turn governed data into apps, decisions, and business workflows?

More specifically:

- How do we let business users ask questions without giving them raw access to everything?
- How do Cortex, Snowflake Intelligence, Cortex Analyst, Streamlit, and Native Apps become an enterprise app layer?
- How do we package data products for departments, customers, partners, or industries?
- How do we monetize or exchange governed data?
- How do we build apps where the data already lives?
- How do Snowflake Postgres and Unistore connect operational/app patterns to the AI Data Cloud?
- How do we make AI legible to executives and business teams?

The hidden anxiety behind the Snowflake attendee is:

> We have data. We have governance. How do we turn it into something the business actually uses?

That is the Snowflake wedge.

Snowflake is the conference for people who do not want to explain the AI stack. They want the AI stack to disappear into governed business workflows.

## The fairness trap: do not compare features by unfair names

The most important review issue is not the top-line thesis. It is category fairness.

If the chart says “Lakebase,” Snowflake readers will reasonably object: Snowflake has Postgres, Unistore, Hybrid Tables, CDC/streaming, Streamlit, SPCS, Native Apps, and app-data patterns.

If the chart says “Postgres/OLTP,” Databricks readers will reasonably object: Lakebase is a named app/operational database substrate and is much more central to Databricks’ agenda.

The fair row is:

**App / operational database substrate**

Vendor labels:

- **Databricks:** Lakebase / app database substrate
- **Snowflake:** Snowflake Postgres + Unistore / app-data bridge

The claim should be:

> Databricks leads in agenda concentration and product branding around the app/operational database substrate. Snowflake has comparable operational pieces, but tells the story as Postgres + Unistore + Hybrid Tables woven into the AI Data Cloud.

Similarly, Unity Catalog vs Horizon should not become “Databricks has governance; Snowflake does not.” This one is worth dwelling on, because it's the trap I fell into first. If you count the *product names*, Databricks wins 4 to 1 — "Unity Catalog" shows up in ~20% of its sessions, "Horizon" in ~5% of Snowflake's. But "Unity Catalog" is Databricks-only and "Horizon" is Snowflake-only, so that's just measuring which brand gets repeated. Count **governance as a concept** instead — lineage, access control, RBAC, masking, compliance, classification — and it's a **dead tie** (~27% of each agenda). Databricks simply names its catalog more, because Unity Catalog is the spine that wires its whole platform together. So:

- **Governance coverage:** a tie. Both conferences take it seriously.
- **Named-catalog prominence:** Databricks by 4×. That's branding, not coverage — don't let it masquerade as a governance gap.

And open table formats are the same story: counted as a concept (Delta *and* Iceberg, both open-source), it's another tie — Databricks talks Delta, Snowflake talks Iceberg, equal airtime. "Snowflake leads openness" was a counting artifact of looking only for the word "Iceberg."

## The most important non-difference: RAG is table stakes

RAG is no longer a clean differentiator. Everyone has the vocabulary. Everyone has the product surface. Everyone can tell a story about retrieval, vector search, and grounding models in enterprise data.

The real competition is the system around RAG.

For Databricks, RAG attaches to governance, pipelines, evals, streaming, MLflow, Unity Catalog, Mosaic AI, Lakeflow, Databricks SQL, AI/BI Genie, and production data apps.

For Snowflake, RAG attaches to governed data, Cortex, Snowflake Intelligence, Cortex Analyst, Streamlit, Native Apps, Marketplace, Dynamic Tables, industry solutions, and business workflows.

For Google, the reference case, RAG attaches to Gemini, Vertex AI, agent protocols, cloud runtime, security, and infrastructure.

Same primitive. Different operating system.

The spicy way to say it:

> RAG has gone from differentiator to plumbing. The real battle is who owns the operating system around it.

## The Snowflake surprise: semantics are a sharper edge than generic AI

Snowflake's AI story is not just “we have agents.” Its sharper edge is semantic and business-facing.

Instead of starting with models and asking how to connect them to data, Snowflake starts with governed enterprise data and asks how to turn it into decisions, workflows, and apps.

Spicy but fair:

> Snowflake's AI strategy makes the most sense when you stop treating it as an AI platform story and start treating it as an enterprise app-platform story.

## The Databricks surprise: conversational analytics and BI are part of the production loop

One useful review question is whether conversational analytics should be framed as a Databricks strength, a Snowflake strength, or a different kind of strength on each side.

For Databricks, AI/BI Genie and related analytics sessions support the broader operational-loop story: BI, SQL, governance, semantic context, and AI experiences live inside the same platform motion.

For Snowflake, Snowflake Intelligence and Cortex Analyst support a different business-facing story: governed data becomes a queryable, explainable, executive-legible interface.

Both are important. The final chart needs fresh counts to avoid overclaiming.

## Open formats are not the whole openness story

Open table formats are visible in both Databricks and Snowflake.

Databricks has the historical Delta/lakehouse position and a convergence story around Delta + Iceberg + Unity Catalog + Delta Sharing.

Snowflake has a strong Iceberg/open-lakehouse interoperability story: Iceberg Tables, Open Catalog, catalog federation, zero-copy access, and bringing Snowflake governance/performance/AI to open-table architectures.

But “open” is no longer one argument.

A better reading is:

- Databricks says open tables and governed lakehouse interoperability.
- Snowflake says open business integration, connectors, marketplace, and governed exchange.
- Google says open agent protocols and cloud integration.

Spicy version:

> The open data stack is splitting into three religions: open tables, open agents, and open apps.

## Google as the reference case: what a cloud AI platform agenda looks like

Google is not the main comparison here, but it is useful because it clarifies what Snowflake and Databricks are not.

Google Cloud Next is the most AI-heavy of the three agendas. It is trying to make agents feel like a cloud platform layer: Gemini, Vertex AI, protocols, runtime, security, infrastructure, developer tools, and ecosystem.

That is why Google Cloud Next is best for people asking:

> What will the AI-native cloud platform look like?

Databricks and Snowflake are asking more data-platform-specific questions.

Databricks asks:

> How do we make AI operational inside the governed data/AI stack?

Snowflake asks:

> How do we turn governed enterprise data into business-facing AI experiences?

Google is the reference because it shows the third path: AI as the new cloud substrate.

## Who should attend which conference?

If your problem is **building and running it**, go to Databricks.

You are probably asking:

- How do we make AI/data systems actually work in production?
- How do we govern data, models, pipelines, lineage, and access together?
- How do we evaluate AI outputs?
- How do we connect streaming, BI, ML, apps, and agents into one platform?
- How do we stop building separate stacks for analytics, ML, AI, governance, and orchestration?

If your problem is **the business outcome**, go to Snowflake.

You are probably asking:

- How do we turn governed data into business apps and workflows?
- How do we let business users ask questions safely?
- How do we package AI for departments, industries, customers, and partners?
- How do we make the semantic layer and governed data products useful to non-engineers?
- How do we make AI show up as decisions, applications, and business value?

If your problem is **what's even possible**, go to Google.

You are probably asking:

- What does the AI-native cloud platform look like?
- How do agents connect to tools, APIs, workflows, and enterprise systems?
- Will MCP, A2A, and related agent protocols matter?
- How do Gemini, Vertex AI, runtime, security, and infrastructure fit together?
- Should we build more of our AI estate around Google Cloud?

The conferences are not interchangeable because the implied attendee is different.

Google Cloud Next is for the platform buyer asking whether agents are becoming the new cloud control plane.

Databricks Data + AI Summit is for the operator asking how to turn AI from a demo into a governed, evaluated, real-time production system.

Snowflake Summit is for the business-data buyer asking how governed enterprise data becomes applications, workflows, and decisions.

Put differently:

> If you're asking what's *possible*, go to Google. If you're asking how to *build and run it*, go to Databricks. If you're asking what it *produces for the business*, go to Snowflake.

## What I would watch at Snowflake and Databricks

The next round of announcements will probably all contain agents.

That will not be the interesting part.

For Databricks, I would watch whether the company keeps the operational loop coherent as it pushes further into apps and agents:

- Do evals become more central?
- Does AI/BI become a governed production interface or just another copilot?
- Does Lakeflow make real-time data and orchestration feel native to AI workflows?
- Does Unity Catalog remain the control plane for the expanding AI surface?
- Do Databricks Apps and Lakebase become part of the operating system or just adjacent product surfaces?

For Snowflake, I would watch whether the company turns business-facing AI into a durable application and operations platform:

- Does Snowflake Intelligence become the default interface for governed data?
- Does Cortex Analyst make the semantic layer feel real to business teams?
- Do Streamlit and Native Apps become a serious enterprise app surface?
- Does Horizon Catalog become an AI governance control plane or mainly a data governance story?
- Do Snowflake Postgres, Unistore, and Hybrid Tables make app-data workloads feel native to the AI Data Cloud?
- Does Snowflake connect industry solutions to reusable app/workflow patterns?

And for both companies, I would watch the same hard question:

> When the agent is wrong, stale, unauthorized, expensive, or operationally broken, which layer is responsible?

The answer to that question will tell us more than another agent demo.

## Closing

Snowflake and Databricks are not fighting over whether enterprise AI matters.

They are fighting over what enterprise AI attaches to.

Databricks wants AI to attach to the governed lakehouse operating loop: catalog, pipelines, SQL, streaming, ML lifecycle, evals, data quality, app databases, and production apps.

Snowflake wants AI to attach to governed enterprise data becoming a business application layer: semantics, Cortex, Snowflake Intelligence, Streamlit, Native Apps, Marketplace, Postgres/Unistore app-data bridges, industry solutions, and workflows.

Google, as the reference point, wants AI to attach to the cloud platform itself: models, agents, protocols, runtime, security, and infrastructure.

That is the real split.

Everyone says agents now.

The question is what the agents attach to.

## Review requests

External reviewers should focus on:

1. Is the Snowflake-vs-Databricks framing fair to both sides?
2. Are the spicy labels — possibility (Google), the build (Databricks), the outcome (Snowflake) — useful, or still too cute?
3. Does the Lakebase vs Snowflake Postgres/Unistore category avoid unfair feature framing?
4. Does Unity Catalog vs Horizon avoid implying Snowflake lacks governance?
5. Does the Google reference case clarify the comparison or distract from it?
6. Which claims require stronger session evidence before publication?

## Publication blockers

The Snowflake-vs-Databricks analysis has been rebuilt with the fair (length-controlled symmetric) method and the mirrored chart now reflects it (`databricks_snowflake_mirrored_bar_chart_data.md`, `chart.svg`). Still open before publishing:

- **Weave in the new findings this draft doesn't yet have:** who's actually on stage (Snowflake is a VP/customer conference, Databricks a practitioner one — 44% of Snowflake customer talks feature a VP+ vs 33% at Databricks); the Novo Nordisk "one company, two stages" anecdote; the twin talks / Open Semantic Interchange convergence; and **NVIDIA changing tables** (Jensen keynoted Snowflake in 2024; in 2026 NVIDIA has 0 Snowflake sessions, 2 at Databricks, and Snowflake's AI fireside went to Anthropic). See `CONFERENCE_CONTRAST.md`.
- Reconcile the **Google** numbers (still on the older fractional basis) with the fair method, or scope the post to Snowflake-vs-Databricks and treat Google as a qualitative reference only.
- Decide whether the three-way "possibility / build / outcome" framing earns its keep with Google in the mix (review request #2).
