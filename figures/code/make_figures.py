"""Draw Figures 2-5 of the paper (Matplotlib, Inter font if installed).
Run compute_numbers.py first.

Run from the repository root:  python figures/code/make_figures.py
"""
import pandas as pd, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

D = "data/"
F = "figures/"          # finished figures
W = "figures/work/"     # inputs written by compute_numbers.py
TEXT, TEXT2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, AXIS = "#e1e0d9", "#c3c2b7"
BLUE, ORANGE, AQUA, GREYBAR = "#2a78d6", "#eb6834", "#1baf7a", "#cfcdc6"

plt.rcParams.update({
    "font.family": "Inter", "font.size": 8.5, "text.color": TEXT,
    "axes.edgecolor": AXIS, "axes.linewidth": 0.8, "axes.labelcolor": TEXT2, "axes.labelsize": 8.5,
    "xtick.color": TEXT2, "ytick.color": TEXT2, "xtick.labelsize": 8, "ytick.labelsize": 8,
    "xtick.major.size": 0, "ytick.major.size": 0, "xtick.major.pad": 4, "ytick.major.pad": 4,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
    "legend.frameon": False, "legend.fontsize": 8,
    "figure.dpi": 100, "savefig.dpi": 300, "savefig.facecolor": "white",
})

def panel(ax, letter, title):
    ax.set_title(f"$\\bf{{{letter}}}$   {title}", loc="left", fontsize=9, color=TEXT, pad=10)

def pct(x, sign=True):
    return f"{x:+.1f}%".replace("-", "−") if sign else f"{x:.1f}%"

def tk(t):
    return "0" if t == 0 else f"{t:+.0f}%".replace("-", "−")

d = pd.read_csv(D + "dhaka_daily_adjusted.csv", index_col=0, parse_dates=True)
cl = pd.read_csv(W + "clusters.csv", parse_dates=["date"])
eid = pd.read_csv(W + "eid_effects.csv", parse_dates=["start_date"])
eid_fake = np.load(W + "eid_fake_avg.npy")
main_fake = np.load(W + "main_fake_avg.npy")

# ---------------- Figure 2: data and model ----------------
fig, (a, b) = plt.subplots(1, 2, figsize=(7.2, 3.0), gridspec_kw={"width_ratios": [2.35, 1], "wspace": 0.28})
full = d["pm25"].reindex(pd.date_range(d.index.min(), d.index.max()))
a.plot(full.index, full.values, color=BLUE, lw=0.6, solid_joinstyle="round")
a.axhline(65, color=MUTED, lw=0.8)
a.scatter(cl["date"], [392] * len(cl), marker="v", s=26, color=ORANGE, zorder=5, clip_on=False, linewidths=0)
a.set_ylim(0, 400); a.set_yticks([0, 100, 200, 300, 400])
a.set_xlim(pd.Timestamp("2016-03-01"), pd.Timestamp("2025-04-01"))
a.set_ylabel("Daily mean PM2.5 (µg/m³)")
a.grid(axis="x", visible=False)
a.legend(handles=[Line2D([], [], color=BLUE, lw=1.2, label="Daily PM2.5"),
                  Line2D([], [], color=MUTED, lw=1.0, label="Daily standard, 65 \u00b5g/m\u00b3"),
                  Line2D([], [], marker="v", ls="", color=ORANGE, ms=5, label="Enforcement cluster (10)")],
         loc="lower left", bbox_to_anchor=(0.0, 1.0), ncol=3, handlelength=1.4, columnspacing=1.1, fontsize=7.4, borderaxespad=0.2)
a.set_title("$\\bf{A}$   PM2.5 peaks every winter; most actions came in the dry season", loc="left", fontsize=9, color=TEXT, pad=22)
b.scatter(d["expected"], d["pm25"], s=3, color=BLUE, alpha=0.28, linewidths=0, rasterized=True)
b.plot([5, 450], [5, 450], color=TEXT2, lw=0.9)
b.set_xscale("log"); b.set_yscale("log")
ticks = [10, 30, 100, 300]
b.set_xticks(ticks); b.set_yticks(ticks)
b.set_xticklabels([str(t) for t in ticks]); b.set_yticklabels([str(t) for t in ticks])
b.minorticks_off()
b.set_xlim(6, 450); b.set_ylim(6, 450)
b.set_xlabel("Expected from weather (µg/m³)"); b.set_ylabel("Observed (µg/m³)")
b.text(0.05, 0.95, "R² = 0.80\nunseen years", transform=b.transAxes, va="top", fontsize=8, color=TEXT)
b.text(11, 8.2, "1:1 line", fontsize=7.2, color=TEXT2, ha="left", va="center")
b.set_title("$\\bf{B}$   Weather explains 80%", loc="left", fontsize=9, color=TEXT, pad=22)
fig.savefig(F + "fig2_data_model.png", bbox_inches="tight", pad_inches=0.08)
plt.close(fig)

# ---------------- Figure 3: calibration ----------------
fig, (a, b) = plt.subplots(1, 2, figsize=(7.2, 3.4), gridspec_kw={"width_ratios": [1.15, 1], "wspace": 0.42})
e = eid.sort_values("start_date", ascending=False).reset_index(drop=True)
y = np.arange(len(e))
a.barh(y, e["effect"], height=0.62, color=AQUA, linewidth=0)
for yi, v in zip(y, e["effect"]):
    a.text(v - 1.2, yi, pct(v, sign=True), va="center", ha="right", fontsize=7, color=TEXT2)
a.set_yticks(y); a.set_yticklabels(e["event"].str.replace("Eid ul-", "", regex=False))
a.axvline(0, color=TEXT2, lw=0.9)
a.set_xlim(-93, 3); a.set_xticks([-80, -60, -40, -20, 0])
a.set_xticklabels([tk(t) for t in [-80, -60, -40, -20, 0]])
a.grid(axis="y", visible=False)
a.set_xlabel("Change vs nearby normal days")
panel(a, "A", "Every Eid lowered PM2.5")
b.hist(eid_fake, bins=np.arange(-50, 30, 1.5), color=GREYBAR, edgecolor="white", linewidth=0.4)
avg = eid["effect"].mean()
b.axvline(avg, color=AQUA, lw=2)
b.text(avg + 1.5, b.get_ylim()[1] * 0.92, f"13 real Eids\n{pct(avg)}", fontsize=8, color=TEXT, va="top")
b.text(13, b.get_ylim()[1] * 0.70, "5,000 sets of\n13 random dates", fontsize=7.4, color=TEXT2, va="top")
b.axvline(0, color=TEXT2, lw=0.6)
b.set_xlim(-50, 28); b.set_xticks([-40, -20, 0, 20]); b.set_xticklabels([tk(t) for t in [-40, -20, 0, 20]])
b.set_yticks([]); b.grid(False); b.spines["left"].set_visible(False)
b.set_xlabel("Average change across 13 dates")
panel(b, "B", "None of 5,000 random sets came close")
fig.savefig(F + "fig3_calibration.png", bbox_inches="tight", pad_inches=0.08)
plt.close(fig)

# ---------------- Figure 4: main result ----------------
fig, (a, b) = plt.subplots(1, 2, figsize=(7.2, 3.3), gridspec_kw={"width_ratios": [1.6, 1], "wspace": 0.26})
lab = [f"{dd:%b}\n{dd:%Y}" for dd in cl["date"]]
x = np.arange(len(cl))
a.bar(x, cl["effect"], width=0.62, color=ORANGE, linewidth=0)
for xi, v in zip(x, cl["effect"]):
    a.text(xi, v + (1.2 if v > 0 else -1.2), f"{v:+.0f}".replace("-", "−"), ha="center", va="bottom" if v > 0 else "top", fontsize=7, color=TEXT2, zorder=5, bbox=dict(fc="white", ec="none", pad=0.4))
a.axhline(0, color=TEXT2, lw=0.9)
m = cl["effect"].mean()
a.hlines(m, -0.45, 9.45, color=TEXT, lw=0.9, zorder=3)
a.text(9.62, m, f"Average\n{pct(m)}", ha="left", va="center", fontsize=7.4, color=TEXT)
a.set_xlim(-0.6, 10.75)
a.set_xticks(x); a.set_xticklabels(lab, fontsize=7)
a.set_ylim(-25, 40); a.set_yticks([-20, -10, 0, 10, 20, 30, 40])
a.set_yticklabels([tk(t) for t in [-20, -10, 0, 10, 20, 30, 40]])
a.grid(axis="x", visible=False)
a.set_ylabel("Change, 30 days after vs before")
a.text(-0.55, 37.5, "Dirtier after ↑", fontsize=7.2, color=TEXT2, va="top")
a.text(-0.55, -24, "Cleaner after ↓", fontsize=7.2, color=TEXT2, va="bottom")
panel(a, "A", "PM2.5 rose after 6 of 10 clusters")
b.axvspan(-20, 0, color="#f0efec", zorder=0, linewidth=0)
b.hist(main_fake, bins=np.arange(-18, 18, 0.9), color=GREYBAR, edgecolor="white", linewidth=0.4, zorder=2)
b.axvline(m, color=ORANGE, lw=2, zorder=3)
top = b.get_ylim()[1]
b.text(m + 0.6, top * 0.95, f"10 real\nclusters\n{pct(m)}", fontsize=8, color=TEXT, va="top", zorder=4)
b.text(-17.2, top * 0.95, "Predicted (H1):\na fall, left of 0", fontsize=7.4, color=TEXT2, va="top", zorder=4)
b.text(-17.2, top * 0.62, "1,000 sets of\n10 random dates", fontsize=7.4, color=TEXT2, va="top", zorder=4)
b.set_xlim(-18, 16); b.set_xticks([-15, -10, -5, 0, 5, 10, 15])
b.set_xticklabels([tk(t).replace("%", "") for t in [-15, -10, -5, 0, 5, 10, 15]], fontsize=7.8)
b.set_yticks([]); b.grid(False); b.spines["left"].set_visible(False)
b.set_xlabel("Average change across 10 dates (%)")
panel(b, "B", "97% of random sets were lower (p = 0.97)")
fig.savefig(F + "fig4_main_result.png", bbox_inches="tight", pad_inches=0.08)
plt.close(fig)

# ---------------- Figure 5: before / after ----------------
fig, ax = plt.subplots(figsize=(7.2, 3.6))
c = cl.copy().reset_index(drop=True)
rows = [f"{dd:%b %Y}" for dd in c["date"]] + ["Average"]
before = list(c["before"]) + [c["before"].mean()]
after = list(c["after"]) + [c["after"].mean()]
yy = np.arange(len(rows))[::-1].astype(float)
yy[-1] -= 0.45   # small gap before the average row
typ = 9.5
ax.axvline(typ, color=MUTED, lw=1.0, zorder=1)
ax.text(typ + 0.6, yy[0] + 0.75, "Typical level (+9.5%)", fontsize=7.4, color=TEXT2, va="bottom")
ax.axvline(0, color=TEXT2, lw=0.6, zorder=1)
for yi, bv, av, r in zip(yy, before, after, rows):
    bold = r == "Average"
    ax.annotate("", xy=(av, yi), xytext=(bv, yi),
                arrowprops=dict(arrowstyle="-|>", color=TEXT2 if not bold else TEXT, lw=1.0 if not bold else 1.4,
                                shrinkA=4.5, shrinkB=4.5, mutation_scale=7), zorder=2)
    ax.scatter([bv], [yi], s=34 if not bold else 46, facecolor="white", edgecolor=MUTED, linewidth=1.3, zorder=3)
    ax.scatter([av], [yi], s=34 if not bold else 46, color=ORANGE, linewidth=0, zorder=4)
ax.set_yticks(yy); ax.set_yticklabels(rows)
for t in ax.get_yticklabels():
    if t.get_text() == "Average": t.set_fontweight("bold"); t.set_color(TEXT)
ax.set_xlim(-22, 46); ax.set_xticks([-20, -10, 0, 10, 20, 30, 40])
ax.set_xticklabels([tk(t) for t in [-20, -10, 0, 10, 20, 30, 40]])
ax.set_ylim(yy[-1] - 0.7, yy[0] + 1.5)
ax.grid(axis="y", visible=False)
ax.set_xlabel("Weather-adjusted PM2.5 (% above or below the level expected from weather)")
ax.legend(handles=[Line2D([], [], marker="o", ls="", mfc="white", mec=MUTED, mew=1.3, ms=6, label="30 days before"),
                   Line2D([], [], marker="o", ls="", color=ORANGE, ms=6, label="30 days after")],
          loc="lower right", ncol=2, handletextpad=0.3, columnspacing=1.2)
ax.set_title("Actions followed cleaner-than-usual months; afterwards PM2.5 returned to its typical level",
             loc="left", fontsize=9, color=TEXT, pad=10)
fig.savefig(F + "fig5_before_after.png", bbox_inches="tight", pad_inches=0.08)
plt.close(fig)
print("ok")
