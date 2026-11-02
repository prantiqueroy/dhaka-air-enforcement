# Results (draft)

## Data and the weather model
After cleaning, the record contained 66,679 valid hours between March 2016 and March 2025, and 2,478 days with at least 18 valid hours. Weather and season explained most of the day-to-day variation in PM2.5: the model, tested on years it had not seen, explained 80% of the variation in daily log PM2.5 (R² = 0.80), and its predictions followed the observed series closely through each winter (Figure 1). Averaged by year, weather-adjusted PM2.5 was lowest in 2020 (10.1% below the level expected from weather) and highest in 2023 (24.3% above), with 2021 to 2023 all above expected levels.

**Figure 1.** Observed and weather-expected daily PM2.5. (A) Winter 2022–23. (B) All days, 2016–2025; the line shows perfect agreement.

## Calibration: the method detects known drops
PM2.5 fell sharply during every Eid holiday with enough data (Figure 2A). Across 13 Eids, weather-adjusted PM2.5 was on average 43.5% lower during the holiday than on normal days nearby; individual Eids ranged from −1.9% (Eid ul-Fitr 2024) to −68.3% (Eid ul-Fitr 2017). The same measurement on random dates averaged +0.3% (standard deviation 21.8%), and none of 5,000 random sets of 13 dates had an average as low as the Eid average (Figure 2B). During the COVID-19 general holiday (26 March to 30 May 2020), weather-adjusted PM2.5 was 19.7% lower than in the weeks before and after. With 10 to 12 events, the smallest average effect the method could reliably distinguish from chance was about 13%.

**Figure 2.** Calibration. (A) Change in weather-adjusted PM2.5 during each Eid relative to nearby normal days. (B) Averages of 5,000 random sets of 13 dates (grey) and the average of the real Eids (green).

## Main test: no fall after enforcement actions
The pre-registered test included 12 verified enforcement actions grouped into 10 clusters (Table 2). Weather-adjusted PM2.5 fell after four clusters and rose after six (Figure 3A). The average change from the 30 days before to the 30 days after an action was +7.3%: air was slightly more polluted after enforcement actions, not less. Random sets of 10 dates had an average change of −1.6% (standard deviation 5.0%), and 97% of them were as low as or lower than the observed value (Figure 3B). H1, that weather-adjusted PM2.5 falls after enforcement actions, was therefore not supported (one-sided p = 0.97). Only 3% of random sets showed an average rise as large as +7.3%.

Because no fall was found, H2 (that a fall fades over time) could not be meaningfully tested. The rise was concentrated in the first 10 days after an action (+8.0%) and was small by days 21 to 30 (+1.5%).

**Figure 3.** Main result. (A) Change in weather-adjusted PM2.5, 30 days after versus 30 days before, for each cluster. (B) Averages of 1,000 random sets of 10 dates (grey) and the average of the real actions (red).

## Robustness
All pre-registered robustness checks gave the same result (Table 1). The average change remained positive when court summonses were excluded, when the January 2021 kiln drive was dated to 4 January, and with 15-day and 60-day windows.

**Table 1.** Robustness of the main result.

| Version | Average change | Clusters |
|---|---|---|
| Main test (30-day windows) | +7.3% | 10 |
| Court summonses excluded | +6.5% | 7 |
| January 2021 drive dated 4 January | +8.2% | 10 |
| 15-day windows | +10.5% | 9 |
| 60-day windows | +9.3% | 10 |

## Exploratory checks
The following checks were not pre-registered and should be read as exploratory. Pollution was not rising unusually before enforcement actions: the change from days 60–31 to days 30–1 before an action averaged +2.0%, similar to +1.6% before random dates (standard deviation 15.0%). However, actions tended to follow months that were cleaner than usual. In the 30 days before actions, weather-adjusted PM2.5 averaged +2.8%, compared with a typical +9.5%; in the 30 days after, it averaged +10.1%, close to the typical level (Figure 4). The rise after actions is therefore consistent with a return to normal levels rather than a worsening caused by the actions.

Season did not explain the result: random dates drawn from the same calendar months as the actions showed an average change of −2.1%, and only 0.2% of 2,000 month-matched random sets reached +7.3%. Courts also did not act during periods of unusually high raw pollution: raw PM2.5 in the 30 days before actions was 3.3% below the average for the month, compared with 2.9% above for random dates.

**Figure 4.** Weather-adjusted PM2.5 in the 30 days before (light) and after (dark) each enforcement cluster. The dashed line shows the typical level.

**Table 2.** Enforcement actions included in the main test.

| Cluster | Event | Date | Type | Action |
|---|---|---|---|---|
| 1 | E01 | 28 Jan 2019 | Court order | High Court orders DoE mobile courts twice a week against air polluters; fencing of construction sites; water spraying |
| 2 | E02 | 13 Mar 2019 | Court summons | High Court summons DoE air quality director and orders reports on steps taken |
| 3 | E03 | 5 May 2019 | Court summons | High Court summons chief executives of both Dhaka city corporations |
| 4 | E04 | 26 Nov 2019 | Court order | Illegal brick kilns in five districts to be shut within 15 days; road dust removal; water spraying |
| 5 | E08 | 13 Jan 2020 | Court order | Nine-point directive: kiln closures, seizure of black-smoke vehicles, covered trucks and construction materials |
| 6 | E10 | 24 Nov 2020 | Court order | Nine-point directive to be implemented within 30 days |
| 7 | E11 | 11 Jan 2021 | Demolition | DoE drive to demolish about 700 illegal kilns, 400 around Dhaka |
| 7 | E12 | 4 Feb 2021 | Court order | Three new directives, including regular water spraying on roads |
| 8 | E14 | 1 Mar 2022 | Court order | All illegal kilns in five districts to be demolished within 15 days |
| 9 | E15 | 20 Apr 2022 | Court summons | DoE Director General and five deputy commissioners summoned over kilns still operating |
| 10 | E24 | 2 Jan 2025 | Mobile court | DoE nationwide special anti-pollution drive begins |
| 10 | E25 | 12 Jan 2025 | Court order | Effective steps within seven days and compliance report |
