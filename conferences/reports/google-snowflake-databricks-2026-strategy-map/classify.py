#!/usr/bin/env python3
"""
Topic classifier for the Snowflake vs Databricks 2026 strategy map.

Reads the pinned 2026-06-13 normalized snapshots:
  - Databricks Data + AI Summit 2026: 802 sessions
  - Snowflake Summit 2026: 537 sessions

Classifies every session against the 10 priority "mirrored chart" rows plus the
side callouts. The primary chart uses full title+abstract text and fractional
topic allocation: if one session matches k rows, each row receives 1/k session
credit. Binary topic prevalence and capped-text runs are emitted as audits.

Design notes (see NEXT_STEPS_TODO.md "Review/synthesis instructions"):
  - Primary rows are fractional topic allocations over full title+abstract text.
    Agenda share = fractional session credit / total sessions.
  - Binary prevalence is still reported separately: "what share of sessions
    touch this topic at all?"
  - Named-product prominence is kept distinct from broad conceptual coverage by
    splitting some rows into a "named" signal (taxonomy/product term) and a
    "broad" signal (concept keywords). See ROWS below.
"""
import json
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CONF = os.path.join(ROOT, "conferences")

SNAPSHOT = "2026-06-13.sessions.json"
DBX_PATH = os.path.join(CONF, "databricks-data-ai-summit", "2026", "normalized", "snapshots", SNAPSHOT)
SNOW_PATH = os.path.join(CONF, "snowflake-summit", "2026", "normalized", "snapshots", SNAPSHOT)


def load(path):
    with open(path) as f:
        return json.load(f)


def text_of(s):
    return f"{s.get('title', '')}\n{s.get('abstract', '')}".lower()


def kw(text, *terms):
    """Whole-ish word/phrase match on lowercased text."""
    for t in terms:
        t = t.lower()
        # word-boundary for short alpha tokens, substring for multiword/product names
        if re.search(r"(?<![a-z0-9])" + re.escape(t) + r"(?![a-z0-9])", text):
            return True
    return False


# ---- Databricks helpers -----------------------------------------------------

def dbx_tags(s):
    return set(t.lower() for t in (s.get("topic_tags") or []))


def dbx_track(s):
    return (s.get("track") or "").lower()


# ---- Snowflake helpers ------------------------------------------------------

def snow_attr(s, field):
    a = s.get("attributes") or {}
    return set(v.lower() for v in (a.get(field) or []))


def snow_tracks(s):
    return snow_attr(s, "Session Tracks")


def snow_topics(s):
    return snow_attr(s, "Covered Topics")


def snow_features(s):
    return snow_attr(s, "Covered Features")


def snow_code_prefix(s):
    m = re.match(r"[A-Za-z]+", s.get("code") or "")
    return m.group(0).upper() if m else ""


# ---------------------------------------------------------------------------
# Row matchers — FULL-TEXT FRACTIONAL, SYMMETRIC KEYWORDS.
#
# Fairness methodology (see AUDITS §0). Earlier drafts mixed each vendor's native
# taxonomy (Databricks topic_tags/track, Snowflake attributes) with keywords. Those
# taxonomies differ wildly in breadth — Snowflake's "AI Agents / Data Agents"
# covered-topic is auto-applied to 291 sessions; Databricks' "AI/BI" and "Unity
# Catalog" tags are similarly broad — so the mix silently inflated whichever side had
# the broader tag, in BOTH directions (it overstated Snowflake's GenAI/semantic leads
# AND Databricks' BI lead). This version removes that bias two ways:
#   1) the SAME keyword set is applied to BOTH vendors (concept terms + every vendor's
#      product names), so neither gets taxonomy credit the other lacks;
#   2) the primary chart uses full public title+abstract text, but divides each
#      session's credit across every row it matches. That preserves real agenda text
#      while reducing the "long abstracts match more rows" problem.
# Capped binary and capped fractional runs remain as sensitivity checks.
# ---------------------------------------------------------------------------

FULL_CAP = 10**9
SNOW_MEDIAN_CAP = 680
DBX_MEDIAN_CAP = 991
CAP = FULL_CAP


def text_capped(s):
    return text_of(s)[:CAP]


ROWS = []  # list of dicts: key, label, dbx_label, snow_label, dbx(fn), snow(fn)


def row(key, label, terms, dbx_label, snow_label):
    """Symmetric matcher: same keyword set on both vendors."""
    matcher = lambda s, t=tuple(terms): kw(text_capped(s), *t)
    ROWS.append(dict(key=key, label=label, dbx=matcher, snow=matcher,
                     dbx_label=dbx_label, snow_label=snow_label))


# 1. GenAI / agent app layer
row(
    "genai_app_layer", "Cortex / GenAI app layer",
    ["generative ai", "genai", "gen ai", "llm", "llms", "ai agent", "ai agents", "agentic",
     "copilot", "chatbot", "rag", "foundation model", "fine-tun", "mosaic ai", "agent bricks",
     "genie", "cortex", "cowork", "coco", "ai functions", "model serving"],
    dbx_label="Mosaic AI / Agent Bricks / Genie",
    snow_label="Cortex agents + CoWork",
)

# 2. Semantic context for agents (semantic layer/models feeding agents)
row(
    "semantic_context", "Semantic context for agents",
    ["semantic view", "semantic views", "semantic model", "semantic models", "semantic layer",
     "metric view", "metric views", "semantics", "ontology", "semantic studio", "cortex analyst"],
    dbx_label="Metric Views",
    snow_label="Semantic Views / Cortex Analyst",
)

# 3. Sharing / marketplace / clean rooms
row(
    "sharing_marketplace", "Sharing / marketplace / clean rooms",
    ["data sharing", "delta sharing", "secure data sharing", "marketplace", "data marketplace",
     "clean room", "clean rooms", "data exchange", "data clean room"],
    dbx_label="Delta Sharing + Marketplace",
    snow_label="Secure Sharing + Marketplace + Clean Rooms",
)

# 4. Open lakehouse / table formats (the open-format substrate; table/interop layer, NOT
#    governance). Counts Delta Lake AND Iceberg equally — both are open-source, openly governed
#    table formats — so Databricks' default (Delta) is not penalised for not being called
#    "Iceberg". Kept *keyword-symmetric* on both vendors on purpose: Databricks has no native
#    "table format" taxonomy tag, so crediting Snowflake's Iceberg/Polaris feature tags while
#    giving Databricks keyword-only would unfairly inflate Snowflake. See AUDITS §2.
row(
    "open_lakehouse", "Open lakehouse / table formats",
    ["delta lake", "delta table", "delta tables", "delta uniform", "uniform", "iceberg", "hudi",
     "parquet", "polaris", "open table format", "open table formats", "open lakehouse",
     "open format", "open formats", "interoperab", "interoperable", "interoperability"],
    dbx_label="Delta Lake + UniForm (+ Iceberg)",
    snow_label="Iceberg + Polaris",
)

# 5. Governance / control plane — as a CONCEPT, not a brand count.
#    NB: the earlier "Unity Catalog vs Horizon" row counted only the two product *names* —
#    but those are vendor-exclusive ("Unity Catalog" is Databricks-only, "Horizon" Snowflake-only),
#    so it measured brand repetition, not governance coverage. Bare "governance" is a dead tie
#    (DBX 21.2% / SNOW 21.4%). This row uses governance *concept* terms only (no product names),
#    which is the fair topic measure. The named-catalog brand prominence (Unity Catalog ~20% vs
#    Horizon ~5%) is reported separately as a side callout. See AUDITS §1.
row(
    "governance_control_plane", "Governance / control plane",
    ["governance", "data governance", "lineage", "access control", "rbac", "role-based access",
     "row-level security", "column-level", "data masking", "masking", "data quality", "compliance",
     "regulatory", "sovereignty", "data classification", "trust center", "catalog federation"],
    dbx_label="Governance / lineage / access",
    snow_label="Governance / lineage / access",
)

# 6. BI dashboards / metrics / AI-BI (dashboard/BI surface, not all "analytics" talk)
row(
    "bi_analytics", "BI dashboards / metrics / AI-BI",
    ["dashboard", "dashboards", "business intelligence", "ai/bi", "ai-bi", "bi tool",
     "self-service analytics", "snowsight"],
    dbx_label="AI/BI dashboards",
    snow_label="BI & Analytics / Snowsight",
)

# 7. App / operational database substrate (combined, vendor-specific labels)
row(
    "app_operational_db", "App / operational database substrate",
    ["lakebase", "databricks apps", "postgres", "oltp", "operational database",
     "transactional database", "unistore", "hybrid table", "hybrid tables", "native app",
     "native apps", "streamlit", "app development"],
    dbx_label="Lakebase / app database substrate",
    snow_label="Snowflake Postgres + Unistore / app-data bridge",
)

# 8. Evals / red teaming / AI quality (STRICT: eval/benchmark/red-team only)
row(
    "evals_strict", "Evals / red teaming / AI quality (strict)",
    ["eval", "evals", "evaluation", "evaluating", "benchmark", "benchmarks", "red team",
     "red-team", "red teaming", "llm judge", "llm-as-a-judge", "llm as a judge", "guardrail", "guardrails"],
    dbx_label="eval / benchmark / red-team",
    snow_label="eval / benchmark / red-team",
)

# 9. Lakeflow / Spark / streaming pipelines
row(
    "pipelines_streaming", "Lakeflow / Spark / streaming pipelines",
    ["lakeflow", "spark", "structured streaming", "streaming", "dlt", "delta live", "auto loader",
     "pipeline", "pipelines", "snowpipe", "dynamic table", "dynamic tables", "openflow",
     "snowpark", "nifi", "dbt", "ingestion"],
    dbx_label="Lakeflow / Spark / streaming",
    snow_label="Snowpipe + Openflow + Snowpark + dbt",
)

# 10. SQL warehouse / lakehouse modernization
row(
    "warehouse_modernization", "SQL warehouse / lakehouse modernization",
    ["data warehouse", "warehouse", "photon", "gen2 warehouse", "optima", "migration",
     "migrate", "modernization", "modernize"],
    dbx_label="Databricks SQL / Photon",
    snow_label="Gen2 warehouses + migrations",
)


# ---- Side callouts (reported separately, not in the mirrored chart) ----------

def nvidia(s):
    return kw(text_of(s), "nvidia", "gpu", "gpus", "cuda", "tensor core", "accelerated compute", "h100", "a100", "blackwell")


def norm_company(c):
    if not c:
        return ""
    c = c.strip().lower()
    c = re.sub(r"[,\.]", "", c)
    c = re.sub(r"\b(inc|llc|corp|corporation|ltd|limited|co|the|sa|ag|plc|gmbh)\b", "", c)
    return re.sub(r"\s+", " ", c).strip()


def speaker_companies(sessions):
    """Count of sessions each speaker-affiliation company appears in."""
    c = Counter()
    for s in sessions:
        seen = set()
        for sp in (s.get("speakers") or []):
            comp = norm_company(sp.get("company"))
            if comp and comp not in seen:
                c[comp] += 1
                seen.add(comp)
    return c


def session_matches(session, side):
    return [i for i, r in enumerate(ROWS) if r[side](session)]


def compute_rows(dbx, snow, cap, scoring="fractional"):
    """Compute row shares at a specific title+abstract cap.

    scoring="fractional" divides each matched session across all rows it matches.
    scoring="binary" gives every matched row one full session of prevalence credit.
    """
    global CAP
    old_cap = CAP
    CAP = cap
    try:
        nd, ns = len(dbx), len(snow)
        dbx_credit = [0.0] * len(ROWS)
        snow_credit = [0.0] * len(ROWS)
        dbx_touched = [0] * len(ROWS)
        snow_touched = [0] * len(ROWS)
        dbx_unmatched = 0
        snow_unmatched = 0
        dbx_multi = 0
        snow_multi = 0

        for session in dbx:
            matches = session_matches(session, "dbx")
            if not matches:
                dbx_unmatched += 1
                continue
            if len(matches) > 1:
                dbx_multi += 1
            weight = 1.0 if scoring == "binary" else 1.0 / len(matches)
            for i in matches:
                dbx_touched[i] += 1
                dbx_credit[i] += weight

        for session in snow:
            matches = session_matches(session, "snow")
            if not matches:
                snow_unmatched += 1
                continue
            if len(matches) > 1:
                snow_multi += 1
            weight = 1.0 if scoring == "binary" else 1.0 / len(matches)
            for i in matches:
                snow_touched[i] += 1
                snow_credit[i] += weight

        rows_out = []
        for i, r in enumerate(ROWS):
            dc = dbx_credit[i]
            sc = snow_credit[i]
            ds = 100.0 * dc / nd
            ss = 100.0 * sc / ns
            rows_out.append({
                "key": r["key"],
                "label": r["label"],
                "dbx_label": r["dbx_label"],
                "snow_label": r["snow_label"],
                "scoring": scoring,
                "dbx_session_credit": round(dc, 1),
                "snow_session_credit": round(sc, 1),
                "dbx_sessions": round(dc, 1) if scoring == "fractional" else int(dc),
                "snow_sessions": round(sc, 1) if scoring == "fractional" else int(sc),
                "dbx_touched_sessions": dbx_touched[i],
                "snow_touched_sessions": snow_touched[i],
                "dbx_share_pct": round(ds, 1),
                "snow_share_pct": round(ss, 1),
                "leader": "Databricks" if ds > ss else ("Snowflake" if ss > ds else "Tie"),
                "delta_pct_pts": round(abs(ds - ss), 1),
            })
        return {
            "scoring": scoring,
            "cap_chars": cap,
            "rows": rows_out,
            "matched_sessions": {
                "databricks": nd - dbx_unmatched,
                "snowflake": ns - snow_unmatched,
            },
            "multi_topic_sessions": {
                "databricks": dbx_multi,
                "snowflake": snow_multi,
            },
            "unmatched_sessions": {
                "databricks": dbx_unmatched,
                "snowflake": snow_unmatched,
            },
        }
    finally:
        CAP = old_cap


def main():
    dbx = load(DBX_PATH)
    snow = load(SNOW_PATH)
    nd, ns = len(dbx), len(snow)
    assert nd == 802, f"expected 802 DBX, got {nd}"
    assert ns == 537, f"expected 537 SNOW, got {ns}"

    primary = compute_rows(dbx, snow, FULL_CAP, scoring="fractional")
    rows_out = primary["rows"]
    binary_prevalence = compute_rows(dbx, snow, FULL_CAP, scoring="binary")
    sensitivity = {
        "fractional_full_text": primary,
        "fractional_cap_991_databricks_median": compute_rows(dbx, snow, DBX_MEDIAN_CAP, scoring="fractional"),
        "fractional_cap_680_snowflake_median": compute_rows(dbx, snow, SNOW_MEDIAN_CAP, scoring="fractional"),
        "binary_full_text": binary_prevalence,
        "binary_cap_991_databricks_median": compute_rows(dbx, snow, DBX_MEDIAN_CAP, scoring="binary"),
        "binary_cap_680_snowflake_median": compute_rows(dbx, snow, SNOW_MEDIAN_CAP, scoring="binary"),
    }

    # Side callouts -- NVIDIA / GPU / accelerated compute
    dbx_nv = [s["title"] for s in dbx if nvidia(s)]
    snow_nv = [s["title"] for s in snow if nvidia(s)]

    # Side callout -- named-catalog BRAND prominence (length-controlled). This is the
    # vendor-exclusive product naming that does NOT belong in the governance topic row (§5).
    uc = sum(1 for s in dbx if kw(text_capped(s), "unity catalog"))
    hz = sum(1 for s in snow if kw(text_capped(s), "horizon catalog", "horizon"))

    # Side callout -- shared speaker-affiliation companies (vendor self excluded)
    dc = speaker_companies(dbx)
    sc = speaker_companies(snow)
    for v in ("databricks", "snowflake"):
        dc.pop(v, None)
        sc.pop(v, None)
    shared = sorted(set(dc) & set(sc), key=lambda x: (-(dc[x] + sc[x]), x))
    shared_out = [{"company": x, "dbx_sessions": dc[x], "snow_sessions": sc[x]} for x in shared]

    out = {
        "denominators": {"databricks": nd, "snowflake": ns},
        "captured": "2026-06-13",
        "source_snapshots": {
            "databricks": "normalized/snapshots/2026-06-13.sessions.json",
            "snowflake": "normalized/snapshots/2026-06-13.sessions.json",
        },
        "method": {
            "primary_text": "full title+abstract",
            "primary_scoring": "fractional topic allocation",
            "note": "Primary rows use full public title+abstract text. Each session's one unit of agenda credit is divided across every row it matches; binary prevalence and capped-text runs are included as audits.",
        },
        "rows": rows_out,
        "primary_allocation": {
            "matched_sessions": primary["matched_sessions"],
            "multi_topic_sessions": primary["multi_topic_sessions"],
            "unmatched_sessions": primary["unmatched_sessions"],
        },
        "binary_prevalence": binary_prevalence,
        "sensitivity": sensitivity,
        "side_callouts": {
            "nvidia_gpu": {
                "databricks_sessions": len(dbx_nv), "snowflake_sessions": len(snow_nv),
                "databricks_share_pct": round(100.0 * len(dbx_nv) / nd, 1),
                "snowflake_share_pct": round(100.0 * len(snow_nv) / ns, 1),
                "databricks_titles": dbx_nv, "snowflake_titles": snow_nv,
            },
            "shared_companies": {
                "dbx_unique": len(dc), "snow_unique": len(sc), "shared_count": len(shared),
                "shared": shared_out,
            },
            "named_catalog_brand": {
                "note": "Brand-name prominence, NOT governance coverage (which is a tie — see row 5).",
                "unity_catalog_dbx_pct": round(100.0 * uc / nd, 1),
                "horizon_snow_pct": round(100.0 * hz / ns, 1),
            },
        },
    }

    with open(os.path.join(HERE, "chart_data.json"), "w") as f:
        json.dump(out, f, indent=2)

    # Reproducible CSV for the mirrored bar chart
    import csv
    with open(os.path.join(HERE, "databricks_snowflake_mirrored_bar_chart_data.csv"), "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["row_key", "row_label", "dbx_label", "snow_label",
                    "dbx_session_credit", "dbx_touched_sessions", "dbx_share_pct",
                    "snow_session_credit", "snow_touched_sessions", "snow_share_pct",
                    "leader", "delta_pct_pts"])
        for r in rows_out:
            w.writerow([r["key"], r["label"], r["dbx_label"], r["snow_label"],
                        r["dbx_session_credit"], r["dbx_touched_sessions"], r["dbx_share_pct"],
                        r["snow_session_credit"], r["snow_touched_sessions"], r["snow_share_pct"],
                        r["leader"], r["delta_pct_pts"]])

    # Console summary
    print(f"Denominators: DBX={nd}  SNOW={ns}\n")
    print("Primary scoring: full-text fractional session credit")
    print(f"Matched tracked rows: DBX={primary['matched_sessions']['databricks']}  "
          f"SNOW={primary['matched_sessions']['snowflake']}")
    print(f"Multi-topic sessions: DBX={primary['multi_topic_sessions']['databricks']}  "
          f"SNOW={primary['multi_topic_sessions']['snowflake']}\n")
    print(f"{'Row':<42}{'DBX cr':>8}{'DBX%':>7}{'SNOW cr':>9}{'SNOW%':>7}  {'Leader':<11}{'Δpp':>6}")
    print("-" * 98)
    for r in rows_out:
        print(f"{r['label']:<42}{r['dbx_session_credit']:>8}{r['dbx_share_pct']:>7}"
              f"{r['snow_session_credit']:>9}{r['snow_share_pct']:>7}  "
              f"{r['leader']:<11}{r['delta_pct_pts']:>6}")
    print("\nSide callout — NVIDIA/GPU/accelerated compute:")
    print(f"  DBX  {len(dbx_nv)} sessions ({round(100.0*len(dbx_nv)/nd,1)}%)")
    print(f"  SNOW {len(snow_nv)} sessions ({round(100.0*len(snow_nv)/ns,1)}%)")
    print(f"Side callout — shared speaker-companies: {len(shared)} "
          f"(DBX {len(dc)} unique, SNOW {len(sc)} unique)")


if __name__ == "__main__":
    main()
