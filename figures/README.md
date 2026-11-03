# Figures

Figures for the paper *Do Enforcement Actions Lower Fine Particulate Pollution in Dhaka? A Pre-registered Event Study, 2016–2025*.

| File | What it shows |
|---|---|
| `fig1_design.png` (`.svg`) | Study design: data, weather model, weather-adjusted PM2.5, calibration and main test |
| `fig2_data_model.png` | (A) Daily PM2.5, 2016–2025, with the 10 enforcement clusters. (B) Observed vs weather-expected PM2.5 |
| `fig3_calibration.png` | (A) Change during each of the 13 Eids. (B) Eid average vs 5,000 random sets of dates |
| `fig4_main_result.png` | (A) Change after each enforcement cluster. (B) Average vs 1,000 random sets of dates |
| `fig5_before_after.png` | Levels in the 30 days before and after each cluster vs the typical level (exploratory) |

## Remaking the figures

Run these from the repository root:

```
python figures/code/compute_numbers.py   # recomputes the numbers in the paper from data/, writes figures/work/
python figures/code/make_figures.py      # draws Figures 2–5
python figures/code/make_fig1.py         # draws Figure 1 (needs Playwright and Chromium)
```

- The random date sets use fixed seeds, so the numbers come out the same as in the paper.
- `compute_numbers.py` applies the three Bangladesh Eid ul-Fitr date corrections (7 July 2016, 16 June 2018, 11 April 2024).
- The figures use the Inter font. If it is not installed, Matplotlib uses its default font. The numbers don't change.
- Colours: blue = PM2.5, green = Eid/calibration, orange = enforcement actions, grey = random dates.
