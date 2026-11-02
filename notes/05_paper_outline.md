# Paper outline: Do Crackdowns Clear the Air?
Draft structure, 2 Nov 2026. Target length about 3,000–3,500 words (excluding references).
Section order follows the Journal of Emerging Investigators (JEI) format: Abstract, Introduction, Results, Discussion, Materials and Methods, References. Check the JEI author guide before submitting.

**How to use this:** each section lists the points and numbers to include. Write the sentences yourself, in plain English. Send each section to Claude for feedback when it's done.

**Working title:** Do enforcement actions lower fine particulate pollution in Dhaka? A pre-registered event study, 2016–2025

---

## Abstract (about 250 words) · write this LAST
- One sentence: Dhaka's PM2.5 problem (annual mean 5–6 times the national standard).
- The gap: courts and the DoE have issued many orders, but no study has tested whether air is cleaner afterwards.
- What you did: 9 years of hourly data, weather model, 10 enforcement clusters, pre-registered.
- The check: method detects Eid (−43.5%) and COVID (−19.7%).
- The answer: no cleaning effect (+7.3%, p = 0.97); air returned to normal levels after actions.
- One-sentence meaning: enforcement as practised left no detectable trace; reasons and what would need to change.

## 1. Introduction (about 600 words)
**Para 1: the problem**
- Dhaka among the world's most polluted cities. Winter about 165–175 µg/m³, monsoon about 30–35 (Sarwar et al., 2023).
- Annual mean 5–6 times the Bangladesh standard of 15 µg/m³; about half of days above the daily standard of 65.

**Para 2: the policy response**
- HRPB writ petition (Jan 2019), High Court nine-point directive (13 Jan 2020), repeated orders through 2025.
- DoE mobile courts and brick kiln demolition drives.

**Para 3: the gap**
- Earlier studies describe patterns (Sarwar et al., 2023) or measure lockdowns (Sarkar & Khan, 2021; Salam et al., 2021).
- Sarkar & Khan did not remove the effect of weather, and their result was not statistically clear.
- No study has tested whether enforcement actions are followed by cleaner air.

**Para 4: this study**
- Research question, in one sentence.
- Approach in one sentence: weather-adjusted PM2.5, before vs after, compared with random dates.
- Hypothesis H1 (pre-registered at https://osf.io/6bsek).

## 2. Results (about 900 words)
**2.1 Data and the weather model**
- 66,679 valid hours, 2,478 days (March 2016 – March 2025).
- Model explains about 80% of day-to-day variation, tested on unseen years (R² = 0.80).
- Figure 1: actual vs expected PM2.5 (notebook 04, Cell 4).

**2.2 Calibration: can the method see a real drop?**
- 13 Eids: average −43.5%; 0 of 5,000 random sets came close.
- COVID holiday: −19.7% (vs −11% in Sarkar & Khan, without weather adjustment).
- Smallest detectable average effect across 10–12 events: about 13%.
- Figure 2: Eid bars and the placebo histogram (notebook 05, Cell 4).

**2.3 Main test (pre-registered)**
- 12 verified events, 10 clusters (table of events in Materials and Methods).
- Average change: +7.3%; H1 not supported (p = 0.97).
- Figure 3: effect for each cluster, and the placebo histogram with the red line (notebook 06, Cells 4–5).

**2.4 Robustness (pre-registered)**
- Table 1: main +7.3%; without summonses +6.5%; E11 on 4 Jan +8.2%; 15-day +10.5%; 60-day +9.3%.
- H2: first 10 days +8.0%, days 21–30 +1.5%.

**2.5 Exploratory checks (not pre-registered; say so clearly)**
- No pre-trend: +2.0% vs +1.6% on random dates.
- Before actions: +2.8%; after: +10.1%; typical: +9.5%. The rise looks like a return to normal.
- Season does not explain it (month-matched random dates: −2.1%).
- Raw PM2.5 before actions was not unusually high, so courts did not act during bad-air spikes.
- Figure 4: before vs after levels with the typical line (notebook 07).

## 3. Discussion (about 800 words) · the most important section, mostly your own thinking
**Para 1: main finding in plain words**
- No detectable cleaning effect after court orders or drives. Method can see real drops, so this is a meaningful null.

**Para 2: why? (from notes/04_why_evidence.md)**
- Your main explanation: about half of PM2.5 comes from outside Bangladesh.
- Second: enforcement focused on brick kilns, not vehicles, road dust and other sources.
- Supporting evidence: court repeatedly said orders were ignored; stay orders on kilns; DoE vacancies and one magistrate in Dhaka (2019); judges' comment on officials "managed by" kiln owners.
- The Eid tension: Eid shows local sources matter (−44%), so outside pollution limits the effect but does not fully explain no effect. Non-enforcement is the other half.

**Para 3: comparison with earlier work**
- Fits HRPB's own view that pollution fell only when directives were implemented and rose with lax enforcement.
- COVID: weather adjustment gives a larger drop than Sarkar & Khan reported.

**Para 4: limitations**
- One monitor; 10 clusters; official dates may not match real enforcement; overlapping windows; only 2 verified physical drives, so H3 untested; deviation from the plan for short windows (minimum data scaled to half the window).

**Para 5: what would need to change**
- Your four points: sustained enforcement, public tracking, more DoE capacity, regional cooperation.
- Next step for research: test physical drives properly (more events, Bangla news sources), and Savar kiln ban with low-cost sensors.

## 4. Materials and Methods (about 700 words)
- **Data:** OpenAQ sensors 4680 and 24434; Open-Meteo ERA5 weather; cleaning rules (985 error code, spike rule, 18-hour rule, blank hours).
- **Weather model:** gradient boosting; features listed; leave-one-year-out testing; outcome = % above or below expected.
- **Enforcement timeline:** search method, two independent sources, date rules (Daily Star "yesterday" rule, late-day orders), 28 events, 14 verified. Table 2: the 12 events used.
- **Calibration:** Eid window −1 to +3; normal days −30 to −8 and +10 to +30.
- **Main test:** as pre-registered; placebo with 1,000 random sets; p-value definition.
- **Deviations from the pre-registration:** minimum data for short windows.
- **Use of AI:** code, candidate event search and date checks with Claude; all decisions reviewed by the author. Data and code: GitHub link.

## 5. Acknowledgements
- Mentor or teacher (once confirmed), anyone who gave feedback.

## References
Sarwar et al. (2023); Sarkar & Khan (2021); Salam et al. (2021); news sources for key events; OpenAQ; Open-Meteo / ERA5.

---

## Figures and tables checklist
| Item | Source |
|---|---|
| Figure 1: actual vs expected | notebook 04, Cell 4 |
| Figure 2: Eid calibration | notebook 05, Cell 4 |
| Figure 3: main result + placebo | notebook 06, Cells 4–5 |
| Figure 4: before vs after levels | notebook 07 |
| Table 1: robustness | notebook 06, Cell 8 |
| Table 2: the 12 events | enforcement_timeline.csv |

## Writing plan (3–20 Nov)
| Days | Section |
|---|---|
| 3–5 Nov | Materials and Methods (easiest: describe what you did) |
| 6–8 Nov | Results |
| 9–12 Nov | Discussion |
| 13–14 Nov | Introduction |
| 15 Nov | Abstract, title |
| 16–20 Nov | Mentor feedback and revision |
