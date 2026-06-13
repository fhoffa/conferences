#!/usr/bin/env python3
"""Apples-to-apples diff: run the SAME classifier (classify.ROWS) against the old
2026-06-02 snapshots (759/550) and the current 2026-06-13 catalogs (802/537), so
any change in a row's leader/delta reflects DATA drift, not method drift.

Flags rows whose leader flipped or whose delta moved materially (>= 5 pp).
"""
import json
import os

import classify as C

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(C.CONF, "{conf}", "2026", "normalized", "snapshots", "{date}.sessions.json")

OLD = {
    "dbx": SNAP.format(conf="databricks-data-ai-summit", date="2026-06-02"),
    "snow": SNAP.format(conf="snowflake-summit", date="2026-06-02"),
}


def shares(dbx, snow):
    nd, ns = len(dbx), len(snow)
    out = {}
    for r in C.ROWS:
        dc = sum(1 for s in dbx if r["dbx"](s))
        sc = sum(1 for s in snow if r["snow"](s))
        ds, ss = 100.0 * dc / nd, 100.0 * sc / ns
        out[r["key"]] = dict(
            label=r["label"], dbx_n=dc, snow_n=sc,
            dbx_share=round(ds, 1), snow_share=round(ss, 1),
            leader=("Databricks" if ds > ss else "Snowflake" if ss > ds else "Tie"),
            delta=round(ds - ss, 1),  # signed: + => Databricks ahead
        )
    return out, nd, ns


old_dbx = json.load(open(OLD["dbx"]))
old_snow = json.load(open(OLD["snow"]))
new_dbx = json.load(open(C.DBX_PATH))
new_snow = json.load(open(C.SNOW_PATH))

old, ond, ons = shares(old_dbx, old_snow)
new, nnd, nns = shares(new_dbx, new_snow)

print(f"OLD basis: DBX {ond} / SNOW {ons}  (2026-06-02)")
print(f"NEW basis: DBX {nnd} / SNOW {nns}  (2026-06-13)\n")
hdr = f"{'Row':<42}{'old Δ':>8}{'new Δ':>8}{'moved':>8}  flags"
print(hdr); print("-" * len(hdr) + "------------------")

material = []
for k in old:
    o, n = old[k], new[k]
    moved = round(n["delta"] - o["delta"], 1)
    flags = []
    if o["leader"] != n["leader"] and "Tie" not in (o["leader"], n["leader"]):
        flags.append(f"LEADER FLIP {o['leader']}→{n['leader']}")
    if abs(moved) >= 5:
        flags.append(f"delta moved {moved:+} pp")
    if flags:
        material.append((o["label"], flags))
    print(f"{o['label']:<42}{o['delta']:>+8}{n['delta']:>+8}{moved:>+8}  {'; '.join(flags)}")

print("\nMaterial changes (leader flip or |Δ move| >= 5 pp):")
if not material:
    print("  none -- every row keeps its leader and direction within 5 pp.")
for label, flags in material:
    print(f"  - {label}: {'; '.join(flags)}")
