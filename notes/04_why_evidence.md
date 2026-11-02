# Why didn't crackdowns clean the air? Evidence notes
Compiled 2 Nov 2026 with AI assistance (Claude). Exploratory: not part of the pre-registered test (https://osf.io/6bsek).
Data checks: notebooks/07_why_checks.ipynb

## 1. What the data says (exploratory checks)

| Check | Result | What it means |
|---|---|---|
| Was pollution already rising before actions? | Pre-trend +2.0% vs +1.6% on random dates (SD 15%) | No. Actions did not follow an unusual rise. |
| Level in the 30 days before actions | +2.8%, vs a typical +9.5% | Actions tended to come after a slightly *cleaner* than usual month. |
| Level in the 30 days after actions | +10.1%, close to typical (+9.5%) | After actions, air was about normal, not unusually bad. |
| Does season explain the +7.3%? | Random dates in the same months average −2.1%; only 0.2% as high | No. Season does not explain it. |
| Do courts act when headline PM2.5 is high? | Raw PM2.5 before actions −3.3% vs normal for the month (random dates +2.9%) | No. Orders were not timed to bad-air spikes. |

**Main interpretation:** the +7.3% is best read as a *return to normal*, not as crackdowns making air worse. Actions happened to come after slightly cleaner-than-usual months; afterwards, air went back to its usual level. Either way, there is no sign of a cleaning effect. With only 10 clusters, this pattern could be partly chance.

Court hearings follow the court's own schedule (petitions, compliance deadlines), not daily air quality, which may explain why timing looks unrelated to raw pollution.

## 2. What courts and officials have said about compliance

**Orders repeatedly ignored**
- 5 Feb 2023: the High Court said none of its earlier directives had been carried out in any meaningful way, ordered compliance within two weeks and warned it would summon officials. (Financial Express, 6 Feb 2023: https://thefinancialexpress.com.bd/national/no-steps-for-controlling-air-pollution-angers-hc-1675604584)
- 31 Jan 2023: "We have to say again and again to implement the court directives. We are ashamed of ourselves for this." (Financial Express: https://mail.thefinancialexpress.com.bd/national/hc-wants-to-know-what-steps-taken-to-reduce-air-pollution-1675171816?amp=true)
- Mar 2022: TBS reported that the 2019–2020 court directives were "ignored evidently". (https://www.tbsnews.net/node/390350)
- 12 Jan 2025: HRPB lawyer Manzill Murshid said pollution fell somewhat when the nine directives were implemented, but rose again because of lax enforcement. (Daily Observer: https://observerbd.com/news/507177)

**Brick kilns: legal delays and capture**
- 17 May 2022: DoE told the High Court 314 of 411 illegal kilns in the five districts were shut, but about 275 writ petitions had been accepted and six-month stay orders delayed action against some kilns. (Daily Star: https://www.thedailystar.net/environment/pollution/air-pollution/news/314-illegal-brick-kilns-shut-down-5-districts-doe-hc-3025656)
- 20 Apr 2022: four deputy commissioners reported closing 114 kilns, while 318 were said to be still operating. (Financial Express: https://old.thefinancialexpress.com.bd/national/hc-summons-dg-of-doe-dcs-to-appear-before-it-on-may-17-1650450824)
- 27 Nov 2023: High Court bench: DoE officials "give permission to the illegal brick kiln owners to operate as they are managed by the owners." HRPB cited reports of certificates being sold to illegal kilns in Savar. (Daily Star: https://www.thedailystar.net/environment/news/environment-officials-managed-kiln-owners-3480611)
- Kiln numbers kept rising: about 4,959 in 2013 to about 8,000 in 2018. (TBS, Mar 2022: https://www.tbsnews.net/node/390350)

**Capacity**
- May 2019: DoE had only one magistrate in Dhaka to run mobile courts against polluters. (Daily Star: https://www.thedailystar.net/city/air-pollution-in-dhaka-high-court-summons-dhaka-city-ceo-1739086)
- Jan 2022: Transparency International Bangladesh reported about 60% of DoE posts vacant, and alleged bribery in licensing. (TBS interview with Dr Iftekharuzzaman: https://www.tbsnews.net/node/355870)

**Not only local**
- About half of Dhaka's annual PM2.5 may come from outside Bangladesh (about 43% in the dry season). (Sarwar et al., 2023)
- Enforcement focused mainly on brick kilns, while vehicles, road dust, small industry and biomass burning were not addressed together. (Prof. Abdus Salam, quoted in TBS, Mar 2022)

## 3. Possible explanations (to discuss and decide)
1. **Orders without enforcement.** Court orders are words; the evidence shows repeated non-compliance, so an order date may not mark any real change.
2. **Weak capacity and capture.** Few magistrates, many vacancies, and alleged collusion with kiln owners.
3. **Legal delays.** Stay orders slow kiln closures, so effects (if any) are spread out over months.
4. **Too small to detect.** Any effect smaller than about 13% cannot be detected with 10 clusters, and half the pollution comes from outside the country.
5. **Timing.** Hearings follow court schedules; the +7.3% looks like a return to normal after slightly cleaner months.

## 4. What I think
*My own choices, 2 Nov 2026; wording drafted with AI help.*

The explanation I find most convincing is pollution from outside Bangladesh. If about half of Dhaka's PM2.5 comes from across the border, then even a well-enforced local crackdown can only change part of what the monitor measures. The second reason is that enforcement focused mostly on brick kilns, while vehicles, road dust and other sources were left alone, so one order or one drive could only touch a small share of the problem.

For a crackdown to work, I think four things are needed: enforcement that continues for months instead of a single order or drive; public records of what was enforced and when, so anyone can check compliance; more staff and magistrates at the DoE; and work with India on cross-border pollution, since local action alone cannot reach that half.

A point I still need to think about: during Eid, PM2.5 fell by about 44% when local activity stopped. This shows local sources still matter a lot, so outside pollution limits how much a crackdown can achieve, but it does not fully explain why I found no effect at all.
