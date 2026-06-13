#!/usr/bin/env python3
"""Company-lens analysis: same logos, different talks — and who's missing.

Two questions an analyst reading both agendas would ask:
  1. For companies that present at BOTH summits, do they talk about the SAME thing?
     (track/topic divergence per shared company)
  2. Who shows up at one but not the other? (notable presences/absences by segment)

Reproducible. Run after classify.py is importable. Writes companies_data.json.
"""
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)  # so `python3 companies.py` finds classify.py
import classify as C
dbx = json.load(open(C.DBX_PATH))
snow = json.load(open(C.SNOW_PATH))


def norm(c):
    return C.norm_company(c)


def dbx_topic(s):
    """Best single topic label for a Databricks session."""
    t = (s.get("track") or "").strip()
    if t and t.lower() != "none":
        return t
    tags = s.get("topic_tags") or []
    return tags[0] if tags else "(untracked)"


def snow_topic(s):
    a = s.get("attributes") or {}
    tr = a.get("Session Tracks") or []
    if tr:
        return tr[0]
    ct = a.get("Covered Topics") or []
    return ct[0] if ct else "(untracked)"


def company_sessions(sessions, topic_fn):
    """company -> list of (title, topic)."""
    d = defaultdict(list)
    for s in sessions:
        seen = set()
        for sp in (s.get("speakers") or []):
            c = norm(sp.get("company"))
            if c and c not in seen:
                d[c].append((s.get("title", ""), topic_fn(s)))
                seen.add(c)
    return d


dbx_c = company_sessions(dbx, dbx_topic)
snow_c = company_sessions(snow, snow_topic)
for v in ("databricks", "snowflake"):
    dbx_c.pop(v, None)
    snow_c.pop(v, None)

shared = sorted(set(dbx_c) & set(snow_c), key=lambda x: -(len(dbx_c[x]) + len(snow_c[x])))
only_dbx = sorted(set(dbx_c) - set(snow_c), key=lambda x: -len(dbx_c[x]))
only_snow = sorted(set(snow_c) - set(dbx_c), key=lambda x: -len(snow_c[x]))


def top_topics(pairs):
    return Counter(t for _, t in pairs).most_common()


print("=" * 78)
print("SHARED COMPANIES — same logo, what topic at each?")
print("=" * 78)
divergent = []
for c in shared[:28]:
    dt = top_topics(dbx_c[c])
    st = top_topics(snow_c[c])
    dlab = dt[0][0] if dt else "?"
    slab = st[0][0] if st else "?"
    flag = "  <-- different" if dlab != slab else ""
    print(f"\n{c.upper()}  (DBX {len(dbx_c[c])} / SNOW {len(snow_c[c])}){flag}")
    print(f"   DBX : {', '.join(f'{t}×{n}' for t,n in dt)}")
    print(f"   SNOW: {', '.join(f'{t}×{n}' for t,n in st)}")
    if dlab != slab:
        divergent.append((c, dlab, slab))

print("\n" + "=" * 78)
print(f"PRESENT AT DATABRICKS, ABSENT AT SNOWFLAKE  ({len(only_dbx)} total) — top 30")
print("=" * 78)
for c in only_dbx[:30]:
    print(f"  {len(dbx_c[c]):>2}  {c}")

print("\n" + "=" * 78)
print(f"PRESENT AT SNOWFLAKE, ABSENT AT DATABRICKS  ({len(only_snow)} total) — top 30")
print("=" * 78)
for c in only_snow[:30]:
    print(f"  {len(snow_c[c]):>2}  {c}")

# Segment probes -- where do notable named players show up?
SEGMENTS = {
    "Hyperscalers": ["amazon web services", "aws", "microsoft", "azure", "google", "google cloud", "oracle"],
    "Model labs": ["openai", "anthropic", "mistral", "mistral ai", "cohere", "meta", "hugging face", "google deepmind"],
    "BI / viz": ["tableau", "thoughtspot", "sigma", "sigma computing", "hex", "looker", "power bi", "qlik", "mode", "omni"],
    "Data tools": ["dbt labs", "fivetran", "confluent", "atlan", "astronomer", "collibra", "monte carlo", "alation", "starburst", "dremio"],
    "GSIs": ["accenture", "deloitte", "ey", "pwc", "kpmg", "cognizant", "infosys", "capgemini", "tata consultancy services", "slalom"],
    "AI app / agent": ["glean", "crewai", "langchain", "llamaindex", "writer", "sierra", "cursor", "replit", "perplexity", "cognition", "lovable"],
}


def where(name):
    n = norm(name)
    return (len(dbx_c.get(n, [])), len(snow_c.get(n, [])))


print("\n" + "=" * 78)
print("SEGMENT PROBE — sessions at (DBX / SNOW)")
print("=" * 78)
for seg, names in SEGMENTS.items():
    print(f"\n{seg}:")
    for nm in names:
        d, s = where(nm)
        if d or s:
            print(f"   {nm:<28} DBX {d} / SNOW {s}")

out = {
    "shared_count": len(shared),
    "only_dbx_count": len(only_dbx),
    "only_snow_count": len(only_snow),
    "divergent": [{"company": c, "dbx_topic": d, "snow_topic": s} for c, d, s in divergent],
    "only_dbx_top": [{"company": c, "sessions": len(dbx_c[c])} for c in only_dbx[:40]],
    "only_snow_top": [{"company": c, "sessions": len(snow_c[c])} for c in only_snow[:40]],
}
json.dump(out, open(os.path.join(HERE, "companies_data.json"), "w"), indent=2)
print(f"\nwrote companies_data.json — {len(divergent)} divergent shared companies")
