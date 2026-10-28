# Dance Scene: breaking vs Latin, two dance markets

*Work in progress, October 2026.* Public data, scripts and analysis behind a three-page summary.

**Page:** https://campeseleonardo-tech.github.io/dance-scene/ · **Summary (PDF):** [docs/Dance_Scene_summary.pdf](docs/Dance_Scene_summary.pdf)

## The question

Red Bull is the reference point in breaking dance events. At salsa and bachata congresses thousands of adults dance, pay and travel, yet no Red Bull presence was found there.
How do the two markets compare, and is there room for Red Bull in Latin?

## The answer in four lines

1. **Latin has more events, and they last mostly three days:** about 406 counted events in Europe in 2026 against 238 for breaking.
2. **The typical Latin dancer pays around 13 times the price of a breaking spectator:** full pass EUR 110 (median of 76 sampled passes) against a spectator ticket of EUR 10 (breaking: median of a random sample of 30 events).
3. **In Europe, Latin leads in Spain, breaking in the German-speaking countries:** past 12 months, Spain 25 % of the Latin listings, Germany 27 % of the breaking ones.
4. **Breaking attention sits at the top, with Red Bull; Latin's attention is on the dancers:** a typical Latin event has 5,344 Instagram followers against 1,689 for breaking; the 30 most followed Latin dancers have 6.5 million followers (median 119,000), the 30 breakers 4.3 million (median 108,000).

Event counts are minimums, shares are of listings (not people) and followers show attention, not attendance. Read the cautions below before quoting a number.

## What is inside

| Folder | Content |
|---|---|
| [docs/](docs/) | The landing page (GitHub Pages) and the summary PDF |
| [analysis/](analysis/) | [analysis.md](analysis/analysis.md) (every number with the id of its source row), [method.md](analysis/method.md) (rounds, sources, sampling, tests, biases), [city_ranking.md](analysis/city_ranking.md), [congress_model.xlsx](analysis/congress_model.xlsx) (economics of a Latin congress, editable inputs) |
| [data/](data/) | The curated tables; one line per file in [data/README.md](data/README.md), column contract in [data/schema.md](data/schema.md) |
| [scripts/](scripts/) | The scripts that rebuild the published numbers from the published data ([scripts/README.md](scripts/README.md)) |

Start with the PDF, then [analysis/analysis.md](analysis/analysis.md). Everything in `data/` is public information: event listings from public calendars, Instagram follower counts read on public profile pages, official statistics. Organisations and public professional figures only (event organisers, artists and competitors with a public profile); no private individuals.

## Method in one paragraph

A census of event calendars (and8.dance and breaking-calendar.com for breaking; goandance.com, latindancecalendar.com and salsavida.com for Latin) merged and de-duplicated, with a capture-recapture estimate of what the calendars miss. Random samples of events per world (30 + 30, and a representative sample of 30 per world matched to the country mix of the census) for Instagram followers and prices. Flagship events read page by page. Bootstrap intervals and permutation tests for the comparisons. The scripting for the collected data was carried out with the help of Claude Code. Details in [analysis/method.md](analysis/method.md).

## Cautions

- Event counts are minimums, since no calendar lists every event. In Europe the breaking calendar seems to be strongest in German-speaking countries, and a recapture estimate on two calendars gives about 300 breaking events a year.
- Past Latin listings come mainly from one calendar (latindancecalendar.com, 303 of 306).
- Shares are of listings, not people. Sizes are stated by organisers. Followers show attention, not attendance.
- The follower lists of dancers are the most followed among the dancers found, not a census.
- Sample sizes are small (Latin n = 18 of 30 places, breaking n = 30 in the representative sample); intervals are in the analysis.

## Reproduce

Python 3.10 or later; `pip install -r requirements.txt` only for the Excel model. Every script runs from the repository root and writes next to the published data:

```
python scripts/census_merge.py     # data/events/merged_events.csv
python scripts/stats_ad.py         # 406 Latin and 238 breaking events in 2026, shares per country
python scripts/rep30_sample.py     # typical event: 5,344 vs 1,689 followers
python scripts/top30_latin.py      # top 30 Latin dancers (6.5 million, median 119,000)
python scripts/top30_breaking.py   # top 30 breakers (4.3 million, median 108,000)
python scripts/artist_concentration.py   # 5 / 10 / 14 artists reach 43 / 67 / 79 % of 61 congresses
```

Scripts that need working notes which are not published are left out; [scripts/README.md](scripts/README.md) lists them.

## Sources and licence

Event listings come from the calendars named above; [data/core/sources.csv](data/core/sources.csv) holds the URL and access date of every other source.

- Scripts: MIT ([LICENSE](LICENSE)).
- Own texts, analysis and compiled tables: CC BY 4.0; third-party listing data stays under its sources' terms ([LICENSE-DATA.md](LICENSE-DATA.md)).

If you are named in the data and want a row corrected or removed, write to the address below.

## Contact

Leonardo Campese, Salzburg. Project management (IPMA Level D), 3 years of R&D projects at KTM; MSc Innovation & Product Management; salsa and bachata dancer.
campese.leonardo@gmail.com · [linkedin.com/in/leonardocampese](https://www.linkedin.com/in/leonardocampese)
