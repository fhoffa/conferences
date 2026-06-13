# Evals / AI quality — Databricks vs Snowflake Summit 2026

Source basis: latest local normalized schedules as of 2026-06-02: Databricks 759 sessions; Snowflake 550 sessions.

## Bottom line

Databricks has the more explicit and mature **evals as production discipline** story. Snowflake has evals, but they appear more as part of the **Cortex agent optimization / trust / production-readiness** story.

- Strict eval/benchmark/red-team signals:
  - Databricks: 87 / 759 = 11.5%
  - Snowflake: 22 / 550 = 4.0%

- Broader AI/agent quality and trust signals:
  - Databricks: 212 / 759 = 27.9%
  - Snowflake: 110 / 550 = 20.0%

- Data quality signals:
  - Databricks: 51 / 759 = 6.7%
  - Snowflake: 20 / 550 = 3.6%

Interpretation: Databricks is putting evals closer to the center of the AI operating substrate: MLflow evals, traces, benchmarks, human-in-the-loop validation, Genie accuracy, agent judges, red teaming, security frameworks, and production feedback loops. Snowflake is putting evals inside Cortex/agent workflows: Cortex Agent Evaluations, benchmark/analyze/improve loops, trust signals, governance, and human review.

## Databricks: evals as AI operating discipline

Representative sessions:

- **Agent Evaluations**
  - Hands-on course on evaluating, governing, and securing agentic AI systems on Databricks.
  - Mentions MLflow evaluation metrics, online evaluation, synthetic evaluation, evaluation datasets from MLflow traces, Unity Catalog governance, access control, auditability, compliance, and the Databricks AI Security Framework.

- **Behind the Curtain: How We Do Eval in Genie**
  - Describes how Genie engineering evaluates at scale.
  - Covers offline benchmarks, human-in-the-loop validation, production feedback loops, and defining what “good” means when correctness is not binary.

- **Agent as a Judge: Scaling AI Evaluation for the Agentic Era**
  - Arize session on agent-as-judge and discovering failure modes from traces.
  - The concept is more advanced than simple LLM-as-judge scoring: evaluators discover recurring failure modes and turn them into targeted evals.

- **Building Higher Quality Genie Agents: How to Ensure Accuracy and Trust**
  - Focuses on metadata, semantics, evaluation, benchmarks, monitoring, and iterative optimization of Genie agents.

- **Three Steps to Red Team Your LLMs on Databricks**
  - Live walkthrough of red-teaming LLM endpoints using guardrails and attack probes.
  - Mentions Garak, PyRIT, CyberSecEval, jailbreaks, prompt injection, and system-prompt attacks.

Databricks counter-position: evals are not just a feature. They are part of the platform loop: build agent/model → trace → evaluate → benchmark → govern → red-team → monitor → improve.

## Snowflake: evals as Cortex agent optimization and trust

Representative sessions:

- **Eval-Driven Agent Optimization with Cortex Code CLI**
  - The clearest Snowflake eval session.
  - Uses Cortex Code's agent-optimization skill and native Snowflake Cortex Agent Evaluations.
  - Covers curating evaluation datasets from production logs, benchmarks, answer correctness, tool-selection accuracy, failure-pattern analysis, and benchmark → improve → validate loops.

- **Building Agents on the Data Your Business Trusts**
  - OpenAI session on agents grounded in Snowflake data.
  - Includes evaluation, governance, and human review as part of scaling enterprise agents.

- **Accelerating Trusted Enterprise AI: Operationalizing AI Agent Trust**
  - Bigeye session on visibility into active agents, touched data, ownership, cost, and whether interactions are trusted/governed/appropriate.
  - Focuses on trust signals like lineage, quality, classification, ownership, policy, usage, and cost.

- **Hex: Under the Hood of the World's Most Advanced AI Data Agent**
  - Discusses evaluation and governance for analytics agents, including why there is no simple unit test for analytical truth and why human feedback/context matter.

- **How to Evaluate Snowflake Gen2 Safely in Production and the Outcomes at Scale**
  - Not AI-agent evals; infrastructure evaluation.
  - Covers A/B validation, workload benchmarking, and production-risk mitigation.

Snowflake counter-position: evals are present, but framed more as making Cortex/agent workflows safe, measurable, governed, and production-ready — less as a cross-platform MLOps/evaluation discipline.

## Strategic difference

Databricks’ eval story is more technical and lifecycle-heavy:

- MLflow evaluations
- traces
- offline benchmarks
- human-in-the-loop validation
- production feedback loops
- Agent/LLM-as-judge
- red teaming
- AI security framework
- Genie accuracy/benchmarking
- model serving and MLOps adjacency

Snowflake’s eval story is more application/trust-layer oriented:

- Cortex Agent Evaluations
- Cortex Code optimization loops
- evaluation datasets from production logs
- answer correctness
- tool-selection accuracy
- human review
- governance and trust signals
- agent activity visibility
- production readiness for Snowflake Intelligence/Cortex agents

## Spicy but fair line

Databricks is treating evals like part of the AI production control plane. Snowflake is treating evals like part of making Cortex agents trustworthy enough for enterprise workflows.

## Caveats

- Some broad quality counts are noisy because “quality,” “trust,” and “monitoring” appear in data-quality, governance, observability, and security contexts.
- The strict eval count is more defensible for actual eval/benchmark/red-team emphasis.
- Snowflake’s strongest eval evidence is real but narrower: Cortex Agent Evaluations and Cortex Code optimization rather than a broad MLflow-style eval ecosystem.
- Absence from the catalog does not mean absence from the product roadmap or customer usage.
