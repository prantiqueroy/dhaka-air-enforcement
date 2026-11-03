"""Recompute every number in the paper from data/ and save the inputs for the figures to figures/work/.
Applies the three Bangladesh Eid ul-Fitr date corrections (2016, 2018, 2024).

Run from the repository root:  python figures/code/compute_numbers.py
"""
import os
import pandas as pd, numpy as np, json
D = "data/"
os.makedirs("figures/work", exist_ok=True)
d  = pd.read_csv(D + "dhaka_daily_adjusted.csv", index_col=0, parse_dates=True)
tl = pd.read_csv(D + "enforcement_timeline.csv")
ne = pd.read_csv(D + "natural_experiments.csv")
tl["date"] = pd.to_datetime(tl["date"], dayfirst=True, format="mixed")
ne["start_date"] = pd.to_datetime(ne["start_date"], dayfirst=True, format="mixed")
for event, day in {"Eid ul-Fitr 2016": "2016-07-07", "Eid ul-Fitr 2018": "2018-06-16", "Eid ul-Fitr 2024": "2024-04-11"}.items():
    ne.loc[ne["event"] == event, "start_date"] = pd.Timestamp(day)
out = {}
out["days"] = len(d)
out["yearly"] = d.groupby(d.index.year)["adjusted_pct"].mean().round(1).to_dict()
lp, le = np.log(d["pm25"]), np.log(d["expected"])
out["r2_log"] = round(1 - ((lp-le)**2).sum()/((lp-lp.mean())**2).sum(), 3)

# ---- calibration (notebook 05 logic) ----
eids = ne[ne["event"].str.startswith("Eid") & (ne["start_date"] < "2025-02-22")].copy()
def eff5(day, during=(-1, 3), before=(-30, -8), after=(10, 30)):
    s = d["adjusted_pct"]
    w = lambda a, b: s.loc[day + pd.Timedelta(days=a): day + pd.Timedelta(days=b)]
    dur = w(*during); normal = pd.concat([w(*before), w(*after)])
    if len(dur) < 3 or len(normal) < 15: return np.nan
    return dur.mean() - normal.mean()
eids["effect"] = [round(eff5(x), 1) for x in eids["start_date"]]
tested = eids.dropna(subset=["effect"])
rng = np.random.default_rng(0)
eid_days = eids["start_date"].values
pool = [day for day in d.index[(d.index > "2016-05-01") & (d.index < "2025-02-01")]
        if np.abs((eid_days - np.datetime64(day)).astype("timedelta64[D]").astype(int)).min() > 40]
fake = []
for day in rng.choice(pool, 3000):
    e = eff5(pd.Timestamp(day))
    if not np.isnan(e): fake.append(e)
    if len(fake) == 1000: break
fake = np.array(fake); n = len(tested)
fake_avg5 = np.array([rng.choice(fake, n).mean() for _ in range(5000)])
out["eid"] = {"n": int(n), "avg": round(tested["effect"].mean(), 1), "rand_mean": round(fake.mean(), 1), "rand_sd": round(fake.std(), 1),
              "p": float((fake_avg5 <= tested["effect"].mean()).mean()), "min_detect": round(2*fake.std()/np.sqrt(12), 1)}
s = d["adjusted_pct"]
out["covid"] = round(s.loc["2020-03-26":"2020-05-30"].mean() - pd.concat([s.loc["2020-02-01":"2020-03-07"], s.loc["2020-06-15":"2020-07-15"]]).mean(), 1)
tested[["event", "start_date", "effect"]].to_csv("figures/work/eid_effects.csv", index=False)
np.save("figures/work/eid_fake_avg.npy", fake_avg5)

# ---- main test (notebook 06 logic) ----
eid_all = ne.loc[ne["event"].str.startswith("Eid"), "start_date"]
s2 = d["adjusted_pct"].copy()
for e in eid_all:
    s2.loc[e - pd.Timedelta(days=1): e + pd.Timedelta(days=3)] = np.nan
s2.loc["2020-03-26":"2020-05-30"] = np.nan
s2 = s2.dropna()
FROZEN = ["E01","E02","E03","E04","E08","E10","E11","E12","E14","E15","E24","E25"]
ev = tl[tl["event_id"].isin(FROZEN)].sort_values("date")[["event_id", "date", "tool"]]
ev["cluster"] = (ev["date"].diff().dt.days.fillna(999) >= 30).cumsum()
cl = ev.groupby("cluster").agg(date=("date", "first"), events=("event_id", "+".join), tool=("tool", "first"))
def eff6(day, before=(-30, -1), after=(1, 30)):
    b = s2.loc[day + pd.Timedelta(days=before[0]): day + pd.Timedelta(days=before[1])]
    a = s2.loc[day + pd.Timedelta(days=after[0]):  day + pd.Timedelta(days=after[1])]
    nb = min(15, (before[1] - before[0] + 1) // 2); na = min(15, (after[1] - after[0] + 1) // 2)
    if len(b) < nb or len(a) < na: return np.nan
    return a.mean() - b.mean()
cl["effect"] = [round(eff6(x), 1) for x in cl["date"]]
obs = cl["effect"].mean(); n6 = cl["effect"].notna().sum()
rng = np.random.default_rng(0)
avoid = pd.concat([tl["date"], eid_all, pd.Series(pd.date_range("2020-03-26", "2020-05-30"))])
cand = d.index[(d.index > "2016-05-01") & (d.index < "2025-02-01")]
dist = np.array([np.abs((avoid.values - np.datetime64(c)).astype("timedelta64[D]").astype(int)).min() for c in cand])
pool6 = cand[dist >= 40]
cache = {}
def pe(day):
    if day not in cache: cache[day] = eff6(day)
    return cache[day]
fk = []
while len(fk) < 1000:
    days = rng.choice(pool6, n6 * 2, replace=False)
    vals = [v for v in (pe(pd.Timestamp(x)) for x in days) if not np.isnan(v)][:n6]
    if len(vals) == n6: fk.append(np.mean(vals))
fk = np.array(fk)
out["main"] = {"avg": round(obs, 1), "rand_mean": round(fk.mean(), 1), "rand_sd": round(fk.std(), 1),
               "p_low": round((fk <= obs).mean(), 3), "p_high": round((fk >= obs).mean(), 3),
               "n_up": int((cl.effect > 0).sum()), "n_down": int((cl.effect < 0).sum())}
cl["early"] = [eff6(x, after=(1, 10)) for x in cl["date"]]
cl["late"] = [eff6(x, after=(21, 30)) for x in cl["date"]]
out["h2"] = [round(cl.early.mean(), 1), round(cl.late.mean(), 1)]
np.save("figures/work/main_fake_avg.npy", fk)
# before / after levels (notebook 07)
def mean_in(series, day, a, b, need=10):
    x = series.loc[day + pd.Timedelta(days=a): day + pd.Timedelta(days=b)]
    return x.mean() if len(x) >= need else np.nan
cl["before"] = [mean_in(s2, x, -30, -1) for x in cl["date"]]
cl["after"] = [mean_in(s2, x, 1, 30) for x in cl["date"]]
typ = np.nanmean([mean_in(s2, pd.Timestamp(x), -30, -1) for x in pool6])
out["levels"] = {"before": round(cl.before.mean(), 1), "after": round(cl.after.mean(), 1), "typical": round(typ, 1)}
cl.to_csv("figures/work/clusters.csv")
print(json.dumps(out, indent=1, default=str))
print(cl[["events","date","tool","effect","before","after"]].round(1).to_string())
print(tested.to_string())
