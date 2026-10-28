# Scripts

Run everything from the repository root (on Windows set `PYTHONUTF8=1` first, so that names with accents print). Python 3.10 or later, standard library only, except `build_congress_model.py` (`pip install -r requirements.txt`). Paths are set at the top of each script (`ROOT` and the folders under `data/`).

| Script | Command | Reads | Writes |
|---|---|---|---|
| validate_data.py | `python scripts/validate_data.py` | data/core/*.csv | prints errors and warnings against data/schema.md (two tables of the working project are not published: it warns that they are empty) |
| census_merge.py | `python scripts/census_merge.py` | data/events/by_source/ | data/events/merged_events.csv; prints the capture-recapture estimates |
| census_stats.py | `python scripts/census_stats.py` | data/events/ | prints the census tables (events per world, period, country) |
| stats_ad.py | `python scripts/stats_ad.py` | data/events/merged_events.csv | analysis/summary_stats_ad.json; prints events per year and shares per country (406 Latin, 238 breaking in 2026) |
| draw_sample.py | `python scripts/draw_sample.py data/samples/latin_frame.csv 30` | a sampling frame | `<frame>_sample.csv` with the draw order (seeded) |
| rep30_sample.py | `python scripts/rep30_sample.py` | data/samples/rep30_draw.csv, rep30_reads.csv | data/samples/rep30_sample.csv, analysis/summary_rep30.json; medians 5,344 vs 1,689 followers |
| robustness.py | `python scripts/robustness.py` | data/core/ | prints bootstrap intervals and permutation tests (event accounts, top 30 dancers, ratios) |
| top30_latin.py | `python scripts/top30_latin.py` | data/core/athletes.csv, facts.csv, data/artists/artist_reach.csv | data/dancers/top30_latin_dancers.csv, latin_dancers_not_in_top30.csv |
| top30_breaking.py | `python scripts/top30_breaking.py` | data/core/athletes.csv, facts.csv | data/dancers/top30_breaking_dancers.csv |
| artist_concentration.py | `python scripts/artist_concentration.py` | data/artists/lineups.csv | data/artists/artist_concentration.csv (5, 10, 14 artists reach 43, 67, 79 % of 61 congresses) |
| city_ranking.py | `python scripts/city_ranking.py` | data/cities/, data/events/merged_events.csv, data/sizes/, data/prices/ | data/cities/city_ranking.csv, analysis/city_ranking.md |
| build_congress_model.py | `python scripts/build_congress_model.py` | data/economics/cost_benchmarks.csv, data/prices/latin_events_detail.csv | analysis/congress_model.xlsx (formulas; recalculate with LibreOffice, or press Ctrl+Shift+F9) |

## Not published

These scripts of the working project read files that are not part of this repository (raw copies of web pages, working notes), so they cannot run here and are left out: the draw of the representative sample (`draw_rep30.py`; its result, `data/samples/rep30_draw.csv`, is published and `rep30_sample.py` rebuilds the sample from it), the parsers of the saved calendar pages, the summary builders, and the data summary generator. The numbers they produced are in the published tables.

## Numbers the published scripts reproduce

Latin 406 and breaking 238 events in Europe in 2026; past 12 months Latin ES 25 %, breaking DE 27 %; typical event 5,344 (Latin, n = 18) vs 1,689 (breaking, n = 30) followers; top 30 dancers 6.5 million / median 119,000 (Latin) and 4.3 million / median 108,000 (breaking); the most booked artists cover 43 / 67 / 79 % of 61 congresses.
