"""Figure 1: study design diagram. SVG drawn here, rendered to PNG with Playwright.

Run from the repository root:  python figures/code/make_fig1.py  (needs: pip install playwright; playwright install chromium)

Text sizes are set relative to the canvas width so that, printed at the paper's
column width, they match the Matplotlib figures (about 8-9 pt).
"""
import math
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path("figures")
W = 1040
TEXT, TEXT2, MUTED, GRID = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
ORANGE = "#eb6834"
# accent: (bar colour, fill tint, border tint)
ACC = {
    "blue":   ("#2a78d6", "#eef4fc", "#c4d9f3"),
    "orange": ("#eb6834", "#fdf3ef", "#f6d3c4"),
    "aqua":   ("#1baf7a", "#edf9f4", "#bfe6d7"),
    "grey":   ("#b4b3ab", "#f7f6f2", "#e0dfd8"),
}
PAD_L, PAD_R = 22, 12

parts, defs = [], []
n_clip = 0


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, cls, limit=None, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    lim = f' data-limit="{limit}"' if limit else ""
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{a}{lim}>{esc(s)}</text>')


def box(x, y, w, h, title, lines, acc="grey", eyebrow=None):
    """Rounded box with a coloured left bar. Returns y of the title's mid-height."""
    global n_clip
    bar, fill, border = ACC[acc]
    n_clip += 1
    cid = f"clip{n_clip}"
    defs.append(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/></clipPath>')
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}"/>')
    parts.append(f'<rect x="{x+.5}" y="{y+.5}" width="{w-1}" height="{h-1}" rx="7.5" fill="none" stroke="{border}"/>')
    parts.append(f'<rect x="{x}" y="{y}" width="5" height="{h}" fill="{bar}" clip-path="url(#{cid})"/>')
    tx, lim = x + PAD_L, x + w - PAD_R
    ty = y + 32
    if eyebrow:
        text(tx, y + 25, eyebrow, "e", lim)
        ty = y + 48
    text(tx, ty, title, "t", lim)
    for i, ln in enumerate(lines):
        text(tx, ty + 25 + i * 22, ln, "b", lim)
    return ty - 6.5


def path(points, r=9):
    """Orthogonal polyline with rounded corners."""
    d = f"M{points[0][0]},{points[0][1]}"
    for i in range(1, len(points) - 1):
        (x0, y0), (x1, y1), (x2, y2) = points[i - 1], points[i], points[i + 1]
        l1, l2 = math.hypot(x1 - x0, y1 - y0), math.hypot(x2 - x1, y2 - y1)
        rr = min(r, l1 / 2, l2 / 2)
        ax, ay = x1 - (x1 - x0) / l1 * rr, y1 - (y1 - y0) / l1 * rr
        bx, by = x1 + (x2 - x1) / l2 * rr, y1 + (y2 - y1) / l2 * rr
        d += f" L{ax:.1f},{ay:.1f} Q{x1},{y1} {bx:.1f},{by:.1f}"
    d += f" L{points[-1][0]},{points[-1][1]}"
    return d


def arrow(points):
    parts.append(f'<path d="{path(points)}" fill="none" stroke="{MUTED}" stroke-width="1.5" marker-end="url(#ah)"/>')


# ---- columns -------------------------------------------------------------
C1x, C1w = 16, 312
C2x, C2w = C1x + C1w + 50, 272
C3x, C3w = C2x + C2w + 60, 314
assert C3x + C3w + 16 == W, C3x + C3w + 16
for x, w, label in [(C1x, C1w, "DATA"), (C2x, C2w, "MEASURE"), (C3x, C3w, "TESTS")]:
    text(x, 22, label, "h")
    parts.append(f'<line x1="{x}" y1="34.5" x2="{x+w}" y2="34.5" stroke="{GRID}"/>')

BH = 96
A_y, B_y = 50, 162
M_y = (A_y + B_y) // 2                 # model centred between the two data boxes
J_y = 250
K_y, K_h = M_y, 106
S_h = 188

# column 1 (air and weather)
box(C1x, A_y, C1w, BH, "Hourly PM2.5",
    ["U.S. Embassy monitor, Dhaka", "2016–2025 · 66,679 valid hours"], "blue")
box(C1x, B_y, C1w, BH, "Hourly weather",
    ["ERA5 reanalysis via Open-Meteo", "Temperature, humidity, rain, wind"], "grey")

# column 2
box(C2x, M_y, C2w, BH, "Weather model",
    ["Predicts PM2.5 from weather", "R² = 0.80 on unseen years"], "grey")
box(C2x, J_y, C2w, BH, "Weather-adjusted PM2.5",
    ["% above or below the level", "expected from the weather"], "blue")
j_c = J_y + BH / 2

# column 3: main-test title sits level with the arrow from the adjusted box
S_y = round(j_c - (48 - 6.5))
k_mid = box(C3x, K_y, C3w, K_h, "Calibration",
            ["13 Eids and the COVID-19 holiday", "Can the method see a known fall?"], "aqua", eyebrow="STEP 1")
s_mid = box(C3x, S_y, C3w, S_h, "Main test",
            ["30 days after vs 30 days before", "Compared with 1,000 random sets"], "orange",
            eyebrow="STEP 2 · PRE-REGISTERED")
assert abs(s_mid - j_c) < 0.6, (s_mid, j_c)

# mini window schematic inside the main-test box
bx0, bx1 = C3x + PAD_L, C3x + C3w - 18
mid = (bx0 + bx1) / 2
bar_c = S_y + 131
by, bh = bar_c - 14, 28
parts.append(f'<rect x="{bx0}" y="{by}" width="{mid-bx0-2}" height="{bh}" rx="4" fill="#e7e6e0"/>')
parts.append(f'<rect x="{mid+2}" y="{by}" width="{bx1-mid-2}" height="{bh}" rx="4" fill="#f8d5c6"/>')
text((bx0 + mid) / 2, by + 19, "30 days before", "s", anchor="middle")
text((mid + bx1) / 2, by + 19, "30 days after", "s", anchor="middle")
parts.append(f'<line x1="{mid}" y1="{by-8}" x2="{mid}" y2="{by+bh+8}" stroke="{ORANGE}" stroke-width="2.5" stroke-linecap="round"/>')
text(mid, by + bh + 27, "action (day 0)", "s", anchor="middle")

# column 1 (enforcement), centred on the schematic so the arrow lines up with it
T_y = round(bar_c - BH / 2)
box(C1x, T_y, C1w, BH, "Enforcement timeline",
    ["28 actions found in news reports", "12 verified, in 10 clusters"], "orange")

H = max(S_y + S_h, T_y + BH) + 18

# ---- arrows --------------------------------------------------------------
gx1 = (C1x + C1w + C2x) / 2
gx2 = (C2x + C2w + C3x) / 2
m_c = M_y + BH / 2
arrow([(C1x + C1w, A_y + BH / 2), (gx1, A_y + BH / 2), (gx1, m_c), (C2x, m_c)])
arrow([(C1x + C1w, B_y + BH / 2), (gx1, B_y + BH / 2), (gx1, m_c), (C2x, m_c)])
c2mid = C2x + C2w / 2
arrow([(c2mid, M_y + BH), (c2mid, J_y)])
arrow([(C2x + C2w, j_c), (C3x, j_c)])
arrow([(gx2, j_c), (gx2, k_mid), (C3x, k_mid)])
parts.append(f'<circle cx="{gx2}" cy="{j_c}" r="3.2" fill="{MUTED}"/>')
arrow([(C1x + C1w, bar_c), (C3x, bar_c)])
text((C1x + C1w + C3x) / 2, bar_c - 10, "enforcement dates", "l", anchor="middle")

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9.5" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">
<path d="M0,0.8 L9.5,5 L0,9.2 z" fill="{MUTED}"/></marker>
{''.join(defs)}
<style>
text {{ font-family: Inter, sans-serif; }}
.t {{ font-size: 18px; font-weight: 600; fill: {TEXT}; }}
.b {{ font-size: 15px; font-weight: 400; fill: {TEXT2}; }}
.s {{ font-size: 13.5px; font-weight: 500; fill: {TEXT2}; }}
.h {{ font-size: 13px; font-weight: 600; letter-spacing: 1.6px; fill: {MUTED}; }}
.e {{ font-size: 11.5px; font-weight: 600; letter-spacing: 1.3px; fill: {MUTED}; }}
.l {{ font-size: 14px; font-weight: 400; fill: {MUTED}; font-style: italic; }}
</style>
</defs>
<rect width="{W}" height="{H}" fill="#ffffff"/>
{''.join(parts)}
</svg>"""

(OUT / "fig1_design.svg").write_text(svg, encoding="utf-8")
html = f"<!doctype html><html><head><meta charset='utf-8'><style>html,body{{margin:0;background:#fff}}</style></head><body>{svg}</body></html>"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2.5)
    pg.set_content(html)
    pg.wait_for_timeout(300)
    pg.locator("svg").screenshot(path=str(OUT / "fig1_design.png"))
    over = pg.evaluate("""() => [...document.querySelectorAll('text[data-limit]')].map(t => {
        const b = t.getBBox(); return [t.textContent, Math.round(b.x + b.width), +t.dataset.limit]; })
        .filter(([s, r, lim]) => r > lim)""")
    fam = pg.evaluate("() => document.fonts.check('15px Inter')")
    b.close()
print("size", W, H, "| Inter available:", fam)
for t, r, lim in over:
    print("OVERFLOW:", t, r, ">", lim)
print("ok")
