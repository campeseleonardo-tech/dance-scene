# Method

How the numbers were produced, in the order of the work. Every number in [analysis.md](analysis.md) cites the id of its row in `data/core/` (F fact, E event, A athlete, O organisation). Collection was done in rounds between 19 and 28 October 2026 from public sources only; the scripting for the collected data was carried out with the help of Claude Code.

## 1. Question and hypotheses

Breaking is a spectacle market (few practise, many watch; Red Bull is in it). Latin dance (salsa, bachata) is a participation market (many dance, pay, travel; Red Bull is not found in it). Four hypotheses, each stated before the data that tests it:

- **H1** Two markets: Latin is larger in participation, breaking in audience.
- **H2** A brand like Red Bull could enter Latin through product presence at congresses and socials, not through a competition.
- **H3** Latin attention sits with the dancers and the congresses as gatherings, not with event or competition brands.
- **H4** An activation would take root where Latin is strong and Red Bull already operates (cities).

Status after the last round: H1 supported in a revised form; H2 plausible, not proven; H3 a tendency, not proven; H4 answered with the data on file (Paris, Barcelona, Madrid). Validation talks with organisers are planned.

## 2. Rules

1. Compare like with like. Say whether a number counts dancers, spectators, followers or listings. Red Bull's own events and accounts are never the comparator.
2. Every number has a source and a date; estimates have ranges and a confidence (H, M, L); `not_found` is a valid answer, with the searches written down.
3. Public sources only; organisations and public professional figures only (name, follower count, public role); no private individuals.
4. Social platforms: only what a public page shows without login; no scraping. Counts are rounded by the platform (K, M).
5. Never write "absent": write `not_found` with the pages checked.
6. Standard units (data/schema.md, section 5).

## 3. Event census (Europe, November 2024 to October 2027)

Lists from five calendars: and8.dance and breaking-calendar.com (breaking), goandance.com, latindancecalendar.com and salsavida.com (Latin); Hyrox race lists as a participation reference. `census_merge.py` normalises names, dates and countries, joins the same event across calendars (same country, dates within one day, shared words in the name), keeps Latin events of three days or more that are not kizomba, zouk, flamenco, classes or retreats, and removes Russia, Belarus and Turkey. Result: 1,608 events in scope (Latin 1,092, breaking 516), merged into 1,777 rows with the other regions.

Events a year: calendar year 2026, all sources merged, **Latin 406, breaking 238**. A count is a minimum for both worlds. Capture-recapture (Chapman estimator) on pairs of calendars estimates what a calendar misses: for breaking, two calendars give 263-316, about 300 events a year in Europe. The method assumes independent lists, which is only roughly true.

## 4. Samples

- **Round X:** frames of upcoming events (Latin 222 from goandance, breaking 71 from and8.dance), 30 events drawn per world with a fixed seed, frames not edited after the draw. Instagram followers, prices and line-up artists read for each.
- **Representative sample of 30 per world (round AD):** non-flagship events of the merged census; 30 places split by country in proportion to the census (largest remainder); round X events first inside each country, then a seeded shuffle (seed 20261028). Events whose Instagram account was not found are reported, not replaced by zeros: Latin n = 18 of 30 places, breaking n = 30.
- **Prices:** 150 random Latin events of the next twelve months plus 12 large ones read on official pages (162 events; 84-91 full pass prices). Full pass median EUR 110 (n = 76 in the random sample).
- **Flagship events** (Croatian Summer Salsa Festival, IBE, BC One and others) read one by one: sizes stated by organisers, sponsors, partner pages.

## 5. Tests

Bootstrap intervals (10,000 resamples, seeded) for medians and ratios; permutation tests (10,000 shuffles) on the difference of medians; Mann-Whitney for the typical event. Tests and the result that would weaken each hypothesis were written before the new data were read (analysis.md, sections 9-10). The typical Latin event has more followers than the typical breaking event (p = 0.02); the 30 most followed dancers do not differ (medians 119,000 vs 108,000, p = 0.56); the dancer/event ratio is 7.9 (Latin) vs 3.6 (breaking) with overlapping intervals, a tendency.

## 6. City ranking and congress model

Twenty-four cities, twelve indicators from public statistics (population and age, air passengers, tourist nights, dance venues in OpenStreetMap, price level, Red Bull offices, Latin events, large Latin events nearby), two views (Red Bull entry; new congress), 2,000 random block weightings and leave-one-out checks (`city_ranking.py`). The congress model is an Excel workbook built from public cost benchmarks and the sampled prices, with editable inputs (`build_congress_model.py`); its result is a scenario for discussion, not a forecast.

## 7. Known biases

1. Selection: the flagship and comparison sets are the most visible events found, not a random sample.
2. Asymmetry: the top 30 dancers are the maximum of thousands of accounts; events are a few dozen. The lists are the most followed among the dancers found, not a census.
3. Reporting conventions: Latin organisers state dancers, breaking organisers state spectators; part of "participation vs spectacle" may come from how each scene communicates.
4. Coverage: past Latin listings come mainly from one calendar (303 of 306); breaking calendars are strongest in German-speaking countries; goandance favours Spain and bachata.
5. Platforms: Instagram only; accounts, not people; blocked profiles are `not_found`.
6. Missing: sponsor packs of congresses are rarely public; city-level numbers of schools and participants cannot be counted from desk research.

## 8. What is not published

Working notes, raw page copies and the lists of federation athletes (which include young athletes) are not part of this repository. Event rows keep facts only: name, city, country, dates, price, source and URL; long text copied from third-party pages was dropped.
