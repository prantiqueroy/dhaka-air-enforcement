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
- Cleaning check: found monthly average near 1,000 µg/m³ in Sep 2018 (impossible).
  Likely instrument error codes (985+) in the raw data. Added a rule to remove them.
