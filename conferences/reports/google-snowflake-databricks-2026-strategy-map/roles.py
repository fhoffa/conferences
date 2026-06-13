#!/usr/bin/env python3
"""Speaker-role analysis: what kind of person do CUSTOMER companies put on each stage?

Isolates enterprise/customer speakers (drops the host, vendors, tools, GSIs, model labs,
and vendor field roles), then classifies each by seniority tier. Tests the Novo Nordisk
hypothesis: does Databricks skew toward builders (engineers/architects) and Snowflake
toward buyers (VPs/executives)? Writes roles_data.json.
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import classify as C

dbx = C.load(C.DBX_PATH)
snow = C.load(C.SNOW_PATH)

# Companies that are NOT customers (hosts, vendors, tools, GSIs, model labs, clouds).
NON_CUSTOMER = set("""
databricks snowflake
openai anthropic mistral ai meta google deepmind hugging face cohere
salesforce workday domo dbt labs fivetran glean crewai microsoft ibm sap servicenow zendesk adobe hp
quest software aimpoint digital cognizant astronomer atlan cdw acxiom ntt data slalom infosys
accenture deloitte ey pwc kpmg capgemini tata consultancy services wipro genpact tealium boomi
sigma sigma computing hex thoughtspot qlik omni mode looker tableau monte carlo monte carlo data alation collibra coalesce starburst confluent dremio
dataiku informatica precisely acceldata neo4j snowplow prophecy reducto immuta onetrust lancedb
langchain llamaindex replit lovable cursor matillion phdata kipiai advancing analytics west monroe thoughtworks
archetype consulting resolve ai cyera blitzscaling ventures rearc minio superhuman capital one software
amazon web services aws google cloud oracle lseg nvidia trade desk amperity keebo chalk landingai ataccama billigence
""".split())

# Vendor field-role markers in the TITLE that betray a non-customer even if company slips through.
FIELD_ROLE = re.compile(
    r"\b(developer advocate|developer relations|devrel|sales engineer|solutions engineer|"
    r"solution engineer|presales|pre-sales|field cto|technical evangelist|evangelist|"
    r"customer success|practice lead|practice director|practice head|global practice|"
    r"snowflake|databricks|data superhero)\b", re.I)


def seniority(title):
    t = " " + title.lower() + " "
    if re.search(r"\bvice president\b|\bvp\b|\bsvp\b|\bevp\b|\bavp\b", t):
        return "VP"
    if re.search(r"\bchief\b|\bc[edimft]o\b|\bciso\b|\bcaio\b|\bfounder\b|\bco-founder\b|\bpresident\b|\bowner\b", t):
        return "C-suite"
    if re.search(r"\bdirector\b|\bhead\b|\bmanaging director\b|\bmd\b", t):
        return "Director / Head"
    if re.search(r"\bmanager\b|\bmgr\b", t):
        return "Manager"
    if re.search(r"\bprincipal\b|\bstaff\b|\bdistinguished\b|\bfellow\b|\blead\b", t):
        return "Senior IC"
    if re.search(r"\b(engineer|architect|scientist|analyst|developer|consultant|specialist|"
                 r"administrator|programmer|researcher|sre|practitioner|technologist|member of technical staff)\b", t):
        return "IC / practitioner"
    return "Other"


SENIORITY_ORDER = ["C-suite", "VP", "Director / Head", "Manager", "Senior IC", "IC / practitioner", "Other"]


def enterprise_speakers(sessions, host):
    out = []
    for s in sessions:
        for sp in (s.get("speakers") or []):
            comp = C.norm_company(sp.get("company"))
            title = (sp.get("job_title") or "").strip()
            name = sp.get("name") or sp.get("full_name") or ""
            if not comp or not title:
                continue
            if comp in NON_CUSTOMER or comp == host:
                continue
            if FIELD_ROLE.search(title):
                continue
            out.append((comp, title, name))
    return out


dE = enterprise_speakers(dbx, "databricks")
sE = enterprise_speakers(snow, "snowflake")


def dist(speakers):
    c = Counter(seniority(t) for _, t, _ in speakers)
    n = sum(c.values())
    return c, n


dc, dn = dist(dE)
sc, sn = dist(sE)


def pct(c, n, k):
    return round(100.0 * c.get(k, 0) / n, 1) if n else 0.0


def exec_titles(speakers):
    """Verbatim VP/C-suite titles -> 'VP of what'."""
    ex = [t for _, t, _ in speakers if seniority(t) in ("VP", "C-suite")]
    return Counter(ex).most_common(), len(ex)


d_exec, d_execn = exec_titles(dE)
s_exec, s_execn = exec_titles(sE)


def builder_buyer(c):
    builders = c.get("Senior IC", 0) + c.get("IC / practitioner", 0)
    buyers = c.get("C-suite", 0) + c.get("VP", 0)
    return builders, buyers, (round(builders / buyers, 2) if buyers else None)


print(f"Enterprise (customer) speakers w/ title:  DBX {dn}  |  SNOW {sn}\n")
print(f"{'Seniority tier':<22}{'DBX %':>9}{'SNOW %':>9}   (count DBX / SNOW)")
print("-" * 64)
for k in SENIORITY_ORDER:
    print(f"{k:<22}{pct(dc,dn,k):>8}%{pct(sc,sn,k):>8}%     {dc.get(k,0):>4} / {sc.get(k,0)}")

db, dbuy, dr = builder_buyer(dc)
sb, sbuy, sr = builder_buyer(sc)
print(f"\nBuilders (IC+Senior IC) vs buyers (VP+C-suite):")
print(f"  DBX : {db} builders / {dbuy} buyers  = {dr}:1 builder-to-buyer")
print(f"  SNOW: {sb} builders / {sbuy} buyers  = {sr}:1 builder-to-buyer")


def talk_level(sessions, host):
    """Among customer-involving talks, share that feature a VP+ vs a practitioner on stage."""
    talks = with_exec = with_prac = 0
    for s in sessions:
        ranks = []
        for sp in (s.get("speakers") or []):
            comp = C.norm_company(sp.get("company"))
            title = (sp.get("job_title") or "").strip()
            if not comp or not title or comp in NON_CUSTOMER or comp == host or FIELD_ROLE.search(title):
                continue
            ranks.append(seniority(title))
        if not ranks:
            continue
        talks += 1
        if any(r in ("C-suite", "VP") for r in ranks):
            with_exec += 1
        if any(r in ("IC / practitioner", "Senior IC") for r in ranks):
            with_prac += 1
    return talks, with_exec, with_prac


dt_t, dt_e, dt_p = talk_level(dbx, "databricks")
st_t, st_e, st_p = talk_level(snow, "snowflake")
print(f"\nTalk-level — share of customer talks featuring...")
print(f"  DBX ({dt_t} talks):  a VP+ {100*dt_e/dt_t:.0f}%   a practitioner {100*dt_p/dt_t:.0f}%")
print(f"  SNOW ({st_t} talks): a VP+ {100*st_e/st_t:.0f}%   a practitioner {100*st_p/st_t:.0f}%")

print("\n=== 'VP / C-suite of WHAT' — DBX top ===")
for t, n in d_exec[:18]:
    print(f"  {n:>2}  {t}")
print("\n=== 'VP / C-suite of WHAT' — SNOW top ===")
for t, n in s_exec[:18]:
    print(f"  {n:>2}  {t}")

out = {
    "dbx_total": dn, "snow_total": sn,
    "seniority": {k: {"dbx_pct": pct(dc, dn, k), "snow_pct": pct(sc, sn, k),
                      "dbx_n": dc.get(k, 0), "snow_n": sc.get(k, 0)} for k in SENIORITY_ORDER},
    "builder_buyer": {"dbx": {"builders": db, "buyers": dbuy, "ratio": dr},
                      "snow": {"builders": sb, "buyers": sbuy, "ratio": sr}},
    "talk_level": {
        "dbx": {"talks": dt_t, "with_vp_plus_pct": round(100 * dt_e / dt_t, 1),
                "with_practitioner_pct": round(100 * dt_p / dt_t, 1)},
        "snow": {"talks": st_t, "with_vp_plus_pct": round(100 * st_e / st_t, 1),
                 "with_practitioner_pct": round(100 * st_p / st_t, 1)},
    },
    "exec_titles_dbx": [{"title": t, "n": n} for t, n in d_exec[:30]],
    "exec_titles_snow": [{"title": t, "n": n} for t, n in s_exec[:30]],
}
json.dump(out, open(os.path.join(HERE, "roles_data.json"), "w"), indent=2)
print("\nwrote roles_data.json")
