# Pre-registration: Do Crackdowns Clear the Air?
Prantique Roy · registered 27 Oct 2026, before the main analysis was run

## Question
Is weather-adjusted PM2.5 at the U.S. Embassy monitor in Dhaka lower in the 30 days
after an enforcement action than in the 30 days before?

## Already done (results known)
- Data: hourly PM2.5, U.S. Embassy Dhaka (OpenAQ sensors 4680 and 24434), Mar 2016 – Mar 2025;
  66,679 valid hours, 2,478 days with 18+ valid hours.
- Weather model: gradient boosting on daily weather and season, tested on unseen years (R² = 0.80).
  Outcome = weather-adjusted PM2.5 (% above or below expected).
- Calibration: 13 Eid holidays averaged −43.5% vs normal days; 0 of 5,000 random-date sets
  came close. COVID general holiday: −19.7%.
- Smallest detectable average effect across 12 events: about 13%.

## Events (frozen list)
The 12 verified, testable events in data/enforcement_timeline.csv as of 27 Oct 2026:
E01, E02, E03, E04, E08, E10, E11, E12, E14, E15, E24, E25.
Excluded: E18, E19 (no data after the event, Feb–Mar 2023 gap). Unverified events are not used
in the main test.
Events less than 30 days apart are merged into one cluster dated by the first event:
E11+E12 (Jan–Feb 2021) and E24+E25 (Jan 2025). This gives 10 clusters.

## Main test
1. For each cluster: effect = mean weather-adjusted PM2.5 on days +1 to +30, minus the mean on
   days −30 to −1. The event day itself is left out. For E08 (order issued late on 13 Jan 2020),
   day +1 is 14 Jan.
2. Days in an Eid window (Eid −1 to +3) or the COVID holiday (26 Mar – 30 May 2020) are dropped.
3. A cluster needs at least 15 days of data on each side.
4. Average the effects across clusters.
5. Placebo: repeat steps 1–4 on 1,000 sets of random dates (at least 40 days from any event, Eid
   or the COVID holiday). The p-value is the share of random sets with an average as low or lower.

## Hypotheses
H1: The average effect is negative (one-sided test, p < 0.05).
H2: Any fall fades: the effect on days +21 to +30 is smaller than on days +1 to +10.
H3 (exploratory only): physical enforcement (demolitions, mobile courts) shows a larger fall
than court orders. Only 2 verified physical events exist, so H3 cannot be properly tested.

## Robustness checks (decided now)
- Drop summonses (E02, E03, E15).
- Use 4 Jan 2021 instead of 11 Jan 2021 for E11.
- Windows of 15 and 60 days instead of 30.
- Add the unverified events, if their second sources are found.

## How results will be reported
All results will be reported whether or not they are significant. If no effect is found,
the paper will state that effects smaller than about 13% could not be detected.

## Known limitations
One monitor for the whole city; enforcement may start before or after the official date;
neighbouring events (44–50 days apart) have overlapping windows; about half of Dhaka's PM2.5
may come from outside Bangladesh.

## Use of AI
Code, the candidate event search and date checks were done with AI assistance (Claude).
All decisions listed here were reviewed and agreed by me.
