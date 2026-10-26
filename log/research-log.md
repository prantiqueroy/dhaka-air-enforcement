   # Research log

   ## 13 Oct 2026
   - Set up GitHub repository and wrote README
   - Read the project plan
   - Next: create Colab, OSF and Zenodo accounts; start pandas basics
## 13 Oct 2026 (evening)
- Created accounts on Google Colab, OSF and Zenodo
- Made my first Colab notebook (01_weather_download.ipynb)
- Downloaded hourly Dhaka weather from Open-Meteo, 2016–2025: 87,672 hours of data
- Made a chart of average temperature by month
- Noticed: June was the hottest month (about 29°C) and January the coolest (about 18°C).
  April to September are almost the same, all around 28–29°C.
- Noticed: the cool months (Nov–Feb) are the same months Dhaka's air is worst.
  Need to check later whether temperature itself affects PM2.5.
- Confused about: nothing yet
- Next: get OpenAQ API key, read Sarwar et al. paper
## 13 Oct 2026 (night): PM2.5 download
- Got OpenAQ API key, stored it in Colab Secrets (not on GitHub)
- Found the US consulate monitor is split into two OpenAQ records:
  sensor 4680 (11 Mar–9 Nov 2016, StateAir) and sensor 24434 (10 Nov 2016–24 Mar 2025, AirNow)
- First attempt used only sensor 4680: just 5,656 hours, winter missing, chart looked wrong
- Second attempt combined both but year counts were suspiciously round (6,000 / 7,000);
  the download was silently skipping pages when the server rate-limited it
- Fixed by downloading month by month with automatic retries
- Final dataset: 72,035 hourly readings, 11 Mar 2016 to 24 Mar 2025 (about 91% of all hours)
- First look: January is worst (~200 µg/m³), July cleanest (~35)
- Also found two low-cost AirGradient sensors in Baridhara with 2026 data (15462183, 15677432),
  possible second check for the Savar kiln test
- Next: read Sarwar et al. paper, start cleaning the data
- Saved both datasets to the data folder and wrote a data README describing sources, dates and columns
## 25 Oct 2026
- Read Sarwar et al. (2023) and wrote summary (notes/01_sarwar_2023_summary.md)
- Key takeaway: about half of Dhaka's PM2.5 may come from outside Bangladesh,
  so any crackdown effect will be small and needs careful comparison
- Read Sarkar & Khan (2021) and wrote summary (notes/02_sarkar_khan_2021_summary.md)
- Key takeaway: even the full COVID lockdown only cut PM2.5 ~11% and it was not
  statistically clear, so crackdown effects will be small and weather control is essential
- Wrote one-page proposal (notes/00_proposal.md) and made a PDF version for mentor emails
- Cleaned the PM2.5 data (notebooks/03_clean_and_merge.ipynb)
- Found Sep 2018 monthly average near 1,000 µg/m³ (impossible). Top raw values were
  exactly 985, the monitor's error code. Removed 43 such hours.
- Added a spike rule (>500 and >3x the 24-hour median): removed 25 hours, all in
  winter/spring. Final: 71,967 of 72,035 hours kept.
- Check against Sarwar et al. (2023): my days above 65 for 2019–2021 (171, 147, 172)
  match their range of 144–188. Winter night PM2.5 is about twice the afternoon
  level, matching their finding.
- 2016–2018 show fewer days above 65 than the paper, probably because of missing
  winter data (to confirm with the coverage check)
- Coverage check: 2016–2018 show fewer days above 65 because of missing winter data
  (Jan–Feb 2016 no data; Nov 2017 – Mar 2018 almost no data). Not a cleaning error.
- Events between Nov 2017 and Mar 2018 cannot be tested (no before/after data).
- Sep–Oct 2018 data exists in my file although Sarwar et al. reported it missing;
  same period as the 985 error codes, so treat with caution.
  ## 26 Oct 2026
- Built enforcement timeline: 28 events (2019–2025), 14 verified with two
  independent news sources; sources and dates compiled with AI assistance (Claude)
- Corrected Nov 2019 kiln order date to 26 Nov (same-day Financial Express report)
- Found that Daily Star print stories' "yesterday" means the same day as the online date
- Added natural experiments list (COVID holiday, Eids 2016–2025) for calibration
- Weak spots: only 2 verified physical drives; no events found for 2016–2018
