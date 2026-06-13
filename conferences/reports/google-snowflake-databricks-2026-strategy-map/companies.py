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
import re
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

shared = sorted(set(dbx_c) & set(snow_c), key=lambda x: (-(len(dbx_c[x]) + len(snow_c[x])), x))
only_dbx = sorted(set(dbx_c) - set(snow_c), key=lambda x: (-len(dbx_c[x]), x))
only_snow = sorted(set(snow_c) - set(dbx_c), key=lambda x: (-len(snow_c[x]), x))


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

# Curated set of genuine END-CUSTOMERS (enterprises whose business is NOT selling data
# software) that present at BOTH summits. Hand-maintained because there's no reliable
# company-type field; vendors/tools/GSIs/model-labs are deliberately excluded.
CUSTOMERS = [
    "morgan stanley", "capital one", "goldman sachs", "barclays", "northern trust",
    "nasdaq", "coinbase", "block",
    "gsk", "novo nordisk", "johnson & johnson", "centene",
    "walt disney company", "nbcuniversal", "warner music group", "directv", "comcast",
    "at&t", "nokia", "siemens", "cummins", "8451",
]


def best_title(pairs, topic):
    for t, tp in pairs:
        if tp == topic:
            return t
    return pairs[0][0] if pairs else ""


print("\n" + "=" * 78)
print("SHARED END-CUSTOMERS — different chapter of their story at each venue")
print("=" * 78)
customers_out = []
for c in CUSTOMERS:
    if c not in dbx_c or c not in snow_c:
        continue
    dt = top_topics(dbx_c[c])[0][0]
    st = top_topics(snow_c[c])[0][0]
    rec = {
        "company": c,
        "dbx_topic": dt, "dbx_sessions": len(dbx_c[c]), "dbx_title": best_title(dbx_c[c], dt),
        "snow_topic": st, "snow_sessions": len(snow_c[c]), "snow_title": best_title(snow_c[c], st),
    }
    customers_out.append(rec)
    print(f"\n{c.upper()}  (DBX {rec['dbx_sessions']} / SNOW {rec['snow_sessions']})")
    print(f"   DBX  [{dt}]  {rec['dbx_title'][:72]}")
    print(f"   SNOW [{st}]  {rec['snow_title'][:72]}")

# Twin talks: same company giving a near-identical talk at BOTH summits (the slides
# port unchanged). Jaccard similarity over title tokens, minus boilerplate words.
TWIN_STOP = set(
    "the a an of to with and for in on how is your you are from at by using use as into "
    "more not get built building build why fix data ai databricks snowflake sponsored".split()
)


def _toks(t):
    import re as _re
    t = _re.sub(r"[^a-z0-9 ]", " ", t.lower())
    return {w for w in t.split() if w not in TWIN_STOP and len(w) > 2}


twins = []
for c in shared:
    best, pair = 0.0, None
    for dt, _ in dbx_c[c]:
        for st, _ in snow_c[c]:
            A, B = _toks(dt), _toks(st)
            if not A or not B:
                continue
            j = len(A & B) / len(A | B)
            if j > best:
                best, pair = j, (dt, st)
    if best >= 0.40:
        twins.append({"company": c, "jaccard": round(best, 2),
                      "dbx_title": pair[0], "snow_title": pair[1]})
twins.sort(key=lambda x: -x["jaccard"])

print("\n" + "=" * 78)
print("TWIN TALKS — same company, near-identical talk at both (Jaccard >= .40)")
print("=" * 78)
for t in twins:
    print(f"\n[{t['jaccard']}] {t['company'].upper()}")
    print(f"   DBX : {t['dbx_title']}")
    print(f"   SNOW: {t['snow_title']}")

# ---- Guest-list count -------------------------------------------------------
# How many DISTINCT companies spoke, and how many at both? norm_company() above is
# light (it keeps regional/legal variants like "EY New Zealand" or "AWS" vs "Amazon
# Web Services" separate), which over-counts distinct orgs and hides cross-event
# overlap. canon() collapses those to the parent org so the headcount is honest.
_LEGAL = set("inc llc corp corporation ltd limited co sa ag plc gmbh llp lp pllc pvt ab se nv oyj kk bv".split())
_DESC = set("technologies technology software systems system solutions labs lab ai group global "
            "holdings holding ventures international services service digital media health financial "
            "bank company".split())
_ALIAS = {"amazon web": "amazon", "amazon web services": "amazon", "aws": "amazon",
          "google cloud": "google", "gcp": "google", "alphabet": "google",
          "ernst and young": "ey", "ernst young": "ey", "meta platforms": "meta", "facebook": "meta",
          "microsoft azure": "microsoft", "azure": "microsoft",
          "jp morgan": "jpmorgan", "jpmorganchase": "jpmorgan", "jpmorgan chase": "jpmorgan"}


def canon(c):
    if not c:
        return ""
    c = re.sub(r"\(.*?\)", "", c.lower().strip())
    c = re.sub(r"[^a-z0-9 &/]", " ", c).split("/")[0]
    base = _ALIAS.get(" ".join(t for t in c.split() if t not in _LEGAL).strip(), None) \
        or " ".join(t for t in c.split() if t not in _LEGAL).strip()
    while len(base.split()) > 1 and base.split()[-1] in _DESC:
        base = _ALIAS.get(" ".join(base.split()[:-1]), " ".join(base.split()[:-1]))
    return _ALIAS.get(base, base)


def _orgs(sessions, host):
    s = set()
    for x in sessions:
        for sp in (x.get("speakers") or []):
            n = canon(sp.get("company"))
            if n and n != host:
                s.add(n)
    return s


def _collapse(names):
    """Merge 'a b c' into 'a b' when 'a b' also appears (≥2-token prefix = same parent)."""
    names = set(names)
    return {(" ".join(n.split()[:2]) if len(n.split()) > 2 and " ".join(n.split()[:2]) in names else n)
            for n in names}


g_dbx = _collapse(_orgs(dbx, "databricks"))
g_snow = _collapse(_orgs(snow, "snowflake"))
g_union = _collapse(_orgs(dbx, "databricks") | _orgs(snow, "snowflake"))
g_shared = g_dbx & g_snow
g_overlap = round(100.0 * len(g_shared) / len(g_union), 1)
print("\n" + "=" * 78)
print("GUEST LIST (org-level canonicalization)")
print("=" * 78)
print(f"  distinct companies:  DBX {len(g_dbx)}  |  SNOW {len(g_snow)}  |  union {len(g_union)}")
print(f"  at both: {len(g_shared)}  ({g_overlap}% of union  ≈ 1 in {round(len(g_union)/len(g_shared))})")

out = {
    "shared_count": len(shared),
    "only_dbx_count": len(only_dbx),
    "only_snow_count": len(only_snow),
    "divergent": [{"company": c, "dbx_topic": d, "snow_topic": s} for c, d, s in divergent],
    "shared_customers": customers_out,
    "twin_talks": twins,
    "guest_list": {"dbx_distinct": len(g_dbx), "snow_distinct": len(g_snow),
                   "union": len(g_union), "shared": len(g_shared), "overlap_pct": g_overlap},
    "only_dbx_top": [{"company": c, "sessions": len(dbx_c[c])} for c in only_dbx[:40]],
    "only_snow_top": [{"company": c, "sessions": len(snow_c[c])} for c in only_snow[:40]],
}
json.dump(out, open(os.path.join(HERE, "companies_data.json"), "w"), indent=2)
print(f"\nwrote companies_data.json — {len(divergent)} divergent shared companies")
