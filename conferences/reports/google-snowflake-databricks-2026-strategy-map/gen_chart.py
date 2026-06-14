#!/usr/bin/env python3
"""Generate the mirrored-bar SVG from chart_data.json.

Layout: Snowflake (blue) extends LEFT, Databricks (red) extends RIGHT from a
center column that carries each row's leader + delta. Bar length = agenda share.
Run after classify.py. Emits chart.svg.
"""
import json
import os


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


HERE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(HERE, "chart_data.json")))
rows = data["rows"]
nd = data["denominators"]["databricks"]
ns = data["denominators"]["snowflake"]

# Geometry
W = 700
CX0, CX1 = 300, 400          # center column (leader+delta) x-bounds
LEFT_EDGE, RIGHT_EDGE = 24, 676
AXIS_MAX = 50.0              # pct points mapping to the full half-width
left_span = CX0 - LEFT_EDGE  # px available for snowflake bars
right_span = RIGHT_EDGE - CX1
ROW_H = 46
TOP = 96
BAR_H = 15
H = TOP + ROW_H * len(rows) + 36

BLUE = "#185FA5"   # c-blue 600  (Snowflake)
BLUE_T = "#85B7EB"
RED = "#A32D2D"    # c-red 600   (Databricks)
RED_T = "#F09595"

def lx(pct):  # left bar start x for a given share
    return CX0 - (pct / AXIS_MAX) * left_span

def rx(pct):  # right bar end x
    return CX1 + (pct / AXIS_MAX) * right_span

parts = []
parts.append(
    f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
    f'aria-labelledby="ttl desc">'
)
parts.append('<title id="ttl">Snowflake vs Databricks 2026 — fractional agenda share by strategy row</title>')
parts.append(
    '<desc id="desc">Mirrored bar chart. Snowflake share in blue extends left, '
    'Databricks share in red extends right, from a center column showing the leader '
    'and delta in percentage points for each of ten strategy rows. Each session is '
    'fractionally allocated across every row it matches.</desc>'
)

# Header
parts.append(f'<text x="{CX0-8}" y="34" text-anchor="end" class="th" font-size="15" fill="{BLUE}">Snowflake</text>')
parts.append(f'<text x="{(CX0+CX1)/2}" y="34" text-anchor="middle" class="t" font-size="12" fill="var(--color-text-tertiary)">leader · Δpp</text>')
parts.append(f'<text x="{CX1+8}" y="34" text-anchor="start" class="th" font-size="15" fill="{RED}">Databricks</text>')
parts.append(f'<text x="{CX0-8}" y="52" text-anchor="end" class="t" font-size="11" fill="var(--color-text-tertiary)">{ns} sessions</text>')
parts.append(f'<text x="{CX1+8}" y="52" text-anchor="start" class="t" font-size="11" fill="var(--color-text-tertiary)">{nd} sessions</text>')
parts.append(f'<text x="{W/2}" y="74" text-anchor="middle" class="t" font-size="11" fill="var(--color-text-secondary)">fractional agenda share (% of each catalog) · captured {data["captured"]}</text>')

# Center divider
parts.append(f'<line x1="{(CX0+CX1)/2}" y1="84" x2="{(CX0+CX1)/2}" y2="{H-30}" stroke="var(--color-border-tertiary)" stroke-width="1"/>')

for i, r in enumerate(rows):
    y = TOP + i * ROW_H
    sp, dp = r["snow_share_pct"], r["dbx_share_pct"]
    # Row label centered above the bars
    parts.append(
        f'<text x="{W/2}" y="{y-6}" text-anchor="middle" font-size="12.5" '
        f'fill="var(--color-text-primary)">{i+1}. {esc(r["label"])}</text>'
    )
    by = y + 4
    # Snowflake bar (left)
    sx = lx(sp)
    parts.append(f'<rect x="{sx:.1f}" y="{by}" width="{CX0-sx:.1f}" height="{BAR_H}" rx="2" fill="{BLUE}"/>')
    parts.append(f'<text x="{sx-5:.1f}" y="{by+BAR_H-3}" text-anchor="end" font-size="11" fill="{BLUE}">{sp}%</text>')
    # Databricks bar (right)
    dx = rx(dp)
    parts.append(f'<rect x="{CX1}" y="{by}" width="{dx-CX1:.1f}" height="{BAR_H}" rx="2" fill="{RED}"/>')
    parts.append(f'<text x="{dx+5:.1f}" y="{by+BAR_H-3}" text-anchor="start" font-size="11" fill="{RED}">{dp}%</text>')
    # Center leader + delta
    lead = "SNOW" if r["leader"] == "Snowflake" else ("DBX" if r["leader"] == "Databricks" else "tie")
    lead_color = BLUE if r["leader"] == "Snowflake" else (RED if r["leader"] == "Databricks" else "var(--color-text-tertiary)")
    parts.append(
        f'<text x="{(CX0+CX1)/2}" y="{by+BAR_H-3}" text-anchor="middle" font-size="10.5" '
        f'font-weight="500" fill="{lead_color}">{lead} +{r["delta_pct_pts"]}</text>'
    )

parts.append('</svg>')
svg = "\n".join(p for p in parts if p)

with open(os.path.join(HERE, "chart.svg"), "w") as f:
    f.write(svg)
print(f"wrote chart.svg ({len(svg)} bytes, {len(rows)} rows)")
