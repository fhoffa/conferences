#!/usr/bin/env python3
"""Guest companies on stage: how many talks feature one, and split vendors vs customers.

Two questions:
  1. What share of talks put a non-host (guest) company on stage vs are host-only?
  2. Of the guest companies, which are VENDORS (partners/ISVs/tools/GSIs/clouds/model labs)
     and which are CUSTOMERS (end-user enterprises)?

Vendor detection combines three signals so the long tail of boutique SIs is caught:
  - a curated core vendor set (clouds, model labs, BI/data tools, big GSIs);
  - Databricks "Sponsored by: X |" titles — the named sponsor X is, by definition, a paying
    partner/vendor (this catches small SIs like Lovelytics, RearC, Advancing Analytics);
  - a conservative name heuristic (consulting/analytics/software/… markers).
A company is a CUSTOMER only if none of those fire. Writes guests_data.json.
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

_LEGAL = set("inc llc corp corporation ltd limited co sa ag plc gmbh llp lp pllc pvt ab se nv oyj kk bv".split())
_DESC = set("technologies technology software systems system solutions labs lab ai group global holdings "
            "holding ventures international services service digital media health financial bank company".split())
_ALIAS = {"amazon web": "amazon", "amazon web services": "amazon", "aws": "amazon", "google cloud": "google",
          "gcp": "google", "alphabet": "google", "ernst and young": "ey", "ernst young": "ey",
          "meta platforms": "meta", "facebook": "meta", "microsoft azure": "microsoft", "azure": "microsoft"}


def canon(c):
    if not c:
        return ""
    c = re.sub(r"\(.*?\)", "", c.lower().strip())
    c = re.sub(r"[^a-z0-9 &/]", " ", c).split("/")[0]
    base = " ".join(t for t in c.split() if t not in _LEGAL).strip()
    base = _ALIAS.get(base, base)
    while len(base.split()) > 1 and base.split()[-1] in _DESC:
        base = _ALIAS.get(" ".join(base.split()[:-1]), " ".join(base.split()[:-1]))
    return _ALIAS.get(base, base)


# Curated core vendors (canonical forms).
VENDOR_CORE = set("""
amazon google microsoft oracle ibm nvidia
openai anthropic mistral meta cohere
salesforce workday sap servicenow adobe zendesk domo
dbt fivetran glean crewai atlan astronomer monte carlo collibra coalesce starburst confluent dremio matillion alation
sigma sigma computing hex thoughtspot qlik omni mode looker tableau cube honeydew select star relationalai
dataiku informatica precisely acceldata neo4j snowplow prophecy reducto immuta onetrust lancedb puppygraph
langchain llamaindex replit lovable cursor vercel retool celonis chalk landingai ataccama human security
accenture deloitte ey pwc kpmg capgemini cognizant infosys wipro genpact tata consultancy services ntt data
slalom cdw quest software acxiom lseg trade desk amperity keebo aimpoint digital advancing analytics west monroe
thoughtworks archetype consulting resolve ai cyera blitzscaling ventures rearc minio superhuman kipiai phdata
lovelytics billigence coastal hakkoda exa bright data tealium boomi capital one software quest
""".split())

VENDOR_NAME = re.compile(r"\b(consult|consulting|consultancy|advisory|analytics|technologies|software|"
                         r"solutions|systems|labs|\.?ai|partners|digital|sciences|computing|ventures|"
                         r"datavolo|databricks|snowflake)\b", re.I)


def sponsors_from_titles(sessions):
    """Companies named after 'Sponsored by:' / 'Sponsored By:' — paying partners."""
    s = set()
    for x in sessions:
        m = re.search(r"sponsored by:\s*([^|]+)", x.get("title", ""), re.I)
        if m:
            s.add(canon(m.group(1)))
    return s


DBX_SPONSORS = sponsors_from_titles(dbx) | sponsors_from_titles(snow)


def is_vendor(name_canon, raw_name):
    if name_canon in VENDOR_CORE or name_canon in DBX_SPONSORS:
        return True
    if VENDOR_NAME.search(raw_name or ""):
        return True
    return False


def guest_breakdown(sessions, host):
    total = len(sessions)
    nospk = hostonly = hasguest = 0
    vendor_talks = customer_talks = 0
    vendor_companies, customer_companies = set(), set()
    for s in sessions:
        sps = s.get("speakers") or []
        raw = {(sp.get("company") or ""): canon(sp.get("company")) for sp in sps if sp.get("company")}
        guests = {rc: cc for rc, cc in raw.items() if cc and cc != host}
        if not sps:
            nospk += 1
            continue
        if not guests:
            hostonly += 1
            continue
        hasguest += 1
        sponsored = bool(re.search(r"sponsored", s.get("title", ""), re.I))
        snow_partner = "Snowflake Partners" in ((s.get("attributes") or {}).get("Covered Topics") or [])
        v = c = False
        for rc, cc in guests.items():
            if is_vendor(cc, rc):
                vendor_companies.add(cc)
                v = True
            else:
                customer_companies.add(cc)
                c = True
        # Talk label: vendor if explicitly sponsored/partner OR a vendor is the only guest type
        if sponsored or snow_partner or (v and not c):
            vendor_talks += 1
        else:
            customer_talks += 1
    return dict(total=total, nospk=nospk, hostonly=hostonly, hasguest=hasguest,
                vendor_talks=vendor_talks, customer_talks=customer_talks,
                vendor_companies=vendor_companies, customer_companies=customer_companies)


db = guest_breakdown(dbx, "databricks")
sb = guest_breakdown(snow, "snowflake")


def show(name, b):
    t = b["total"]
    print(f"\n{name}  ({t} talks)")
    print(f"  has a guest company : {b['hasguest']:>3}  ({100*b['hasguest']/t:.0f}%)")
    print(f"  host-only           : {b['hostonly']:>3}  ({100*b['hostonly']/t:.0f}%)")
    print(f"  no speakers listed  : {b['nospk']:>3}  ({100*b['nospk']/t:.0f}%)")
    g = b["hasguest"] or 1
    print(f"  --- of the {b['hasguest']} guest talks ---")
    print(f"  vendor / partner-led: {b['vendor_talks']:>3}  ({100*b['vendor_talks']/g:.0f}% of guest talks)")
    print(f"  customer-led        : {b['customer_talks']:>3}  ({100*b['customer_talks']/g:.0f}% of guest talks)")
    print(f"  distinct vendor companies   : {len(b['vendor_companies'])}")
    print(f"  distinct customer companies : {len(b['customer_companies'])}")


show("DATABRICKS", db)
show("SNOWFLAKE", sb)

# Union company split
allv = db["vendor_companies"] | sb["vendor_companies"]
allc = db["customer_companies"] | sb["customer_companies"]
allc -= allv  # a company classed vendor anywhere is a vendor
union = allv | allc
print("\n" + "=" * 60)
print("GUEST COMPANIES (union, canonicalized)")
print(f"  total {len(union)}  =  {len(allv)} vendors  +  {len(allc)} customers")
print(f"  vendors {100*len(allv)/len(union):.0f}%  /  customers {100*len(allc)/len(union):.0f}%")

out = {
    "databricks": {k: (v if not isinstance(v, set) else sorted(v)) for k, v in db.items()},
    "snowflake": {k: (v if not isinstance(v, set) else sorted(v)) for k, v in sb.items()},
    "union_companies": {"total": len(union), "vendors": len(allv), "customers": len(allc)},
}
json.dump(out, open(os.path.join(HERE, "guests_data.json"), "w"), indent=2)
print("\nwrote guests_data.json")
