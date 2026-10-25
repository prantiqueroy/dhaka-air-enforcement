# Do Crackdowns Clear the Air?
## Testing whether enforcement actions lower PM2.5 in Dhaka, 2016–2025

Prantique Roy · Independent research project · Dhaka, Bangladesh
Code and data: https://github.com/prantiqueroy/dhaka-air-enforcement

### Question
When the government or the courts crack down on air pollution in Dhaka, is the air
measurably cleaner afterwards, and for how long?

### Why it matters
Since 2019, the High Court has issued repeated directives on Dhaka's air (including the
nine-point directive of January 2020), and the Department of Environment has run mobile
courts and brick kiln demolitions. Yet annual PM2.5 remains 5–6 times the national
standard (Sarwar et al., 2023). Published studies describe Dhaka's pollution patterns, but
I have not found one that systematically tests whether enforcement actions are followed by
cleaner air. Two points shape the design: about half of Dhaka's PM2.5 may come from outside
Bangladesh (Sarwar et al., 2023), and even the 2020 COVID lockdown reduced PM2.5 by only
about 11% (Sarkar & Khan, 2021). Any crackdown effect is therefore likely to be small, and
the method must separate it from the much larger effect of weather.

### Data
- Hourly PM2.5 from the U.S. Embassy monitor, March 2016 – March 2025 (72,035 hours,
  via OpenAQ). Already downloaded and documented.
- Hourly weather (wind, rain, temperature, humidity) from Open-Meteo / ERA5. Downloaded.
- An enforcement timeline of 40+ dated actions (court orders, mobile courts, kiln
  demolitions, bans), each confirmed by two independent sources. In progress.

### Method
1. Clean the data using the rules in Sarwar et al. (2023).
2. Remove the effect of weather with a regression model, leaving "weather-adjusted" PM2.5.
3. Check the method can detect real drops, using Eid holidays and the 2020 lockdown.
4. For each enforcement action, compare adjusted PM2.5 in the 30 days after with the
   30 days before.
5. Repeat on 1,000 random dates to check the result is not due to chance.
6. Compare which kinds of action (court order, physical enforcement, announcement)
   leave a measurable trace.
Hypotheses will be registered on OSF before the main analysis.

### Expected findings (hypotheses)
H1. Enforcement actions are followed by a small fall in weather-adjusted PM2.5.
H2. Any fall fades within four weeks.
H3. Physical enforcement (demolitions, mobile courts) has a larger effect than orders
    and announcements.
A null result will be reported as a finding.

### Limitations
One monitor cannot represent the whole city. Announcement dates may not match when
enforcement began. The design can show association, not proof of cause.

### Outputs and timeline (Oct – Dec 2026)
Research paper (3,000–4,000 words), open dataset of enforcement actions, public code,
a two-page policy brief in English and Bangla, and a newspaper op-ed.
Main analysis by mid-November; paper draft by late November.

### About me
I am Prantique Roy, an HSC graduate of Notre Dame College, Dhaka. As part of the
Bangladesh youth delegation at COP30, I attended several sessions on air pollution and
kept relating them to the air in my own city. This project is my attempt to test one of
those questions with Dhaka's own data.
