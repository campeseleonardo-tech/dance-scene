# Data

One line per file. All CSV are UTF-8, comma separated, one header row, dates ISO. Rows is the number of data rows. Every table either carries a source and date column or says below where its sources are. Column contract of `core/`: [schema.md](schema.md).

## core/ (the evidence base)

Rows are linked by id: facts point to places, disciplines, signals and sources; events to organisations; athletes to disciplines. Every fact has a `source_id` (row of `sources.csv`) and a `confidence`: H official page opened, M reliable secondary source, L snippet or estimate. `not_found` rows document searches that gave nothing.

| File | Counts | Rows |
|---|---|---|
| core/facts.csv | One measured value per row (followers, prices, sizes, populations, counts), with unit, period, evidence type and confidence | 1,973 |
| core/sources.csv | One row per URL: publisher, type, access date, access status | 597 |
| core/events.csv | Events of the comparison sets and Red Bull dance events: place, dates, level, scale | 226 |
| core/organisations.csv | Organisers, federations, brands, Red Bull offices | 141 |
| core/athletes.csv | Public professional dancers and line-up artists: name, discipline, country | 135 |
| core/relations.csv | Links between organisations, events and athletes | 93 |
| core/places.csv | Cities, countries and GLOBAL, with the definition of each area | 122 |
| core/disciplines.csv | Breaking, salsa, bachata and adjacent styles | 30 |
| core/signals.csv | The kinds of indicator (events, audience, price, population ...) | 19 |

## events/ (census of the European calendars)

| File | Counts | Rows |
|---|---|---|
| events/merged_events.csv | One row per distinct event, all calendars merged (key, world, name, city, country, date, period, sources, price) | 1,777 |
| events/by_source/latin_latindancecalendar.csv, latin_goandance.csv, latin_salsavida.csv | Latin congress and festival listings per calendar, read October 2026 | 763 / 206 / 299 |
| events/by_source/breaking_and8.csv, breaking_websearch.csv, breaking_wdsf.csv | Breaking listings per source (and8.dance, web search, one federation calendar entry) | 480 / 11 / 1 |
| events/by_source/hyrox_*.csv | Hyrox races, the participation reference | 137 / 52 / 22 |
| events/by_source/exports/breaking_calendar_com.csv | breaking-calendar.com calendar, saved 28 October 2026 | 214 |
| events/by_source/exports/latin_goandance_export.csv | goandance.com listings, saved 28 October 2026 (the page text column is dropped) | 317 |
| events/by_source/exports/breaking_probreakingtour.csv | probreakingtour.com recaps 2019-2026, US only, not used in the counts | 80 |

Source columns: `source`, `listing_url`, `date_start`. Window of the counts: Europe, November 2024 to October 2027.

## samples/ (random samples and Instagram readings)

| File | Counts | Rows |
|---|---|---|
| samples/latin_frame.csv, breaking_frame.csv (+ `_sample`) | Round X sampling frames of upcoming events and the 30-event random draws (seed in the method) | 222 / 71 (30 each) |
| samples/aa_latin_frame.csv (+ `_sample`) | Frame of 450 Latin events and the 150-event draw read for prices and line-ups | 450 (150) |
| samples/size_frame_latin.csv, size_frame_breaking.csv (+ `_sample`) | Frames for event sizes and the draws | 607 / 422 (40 / 30) |
| samples/rep30_draw.csv, rep30_reads.csv, rep30_sample.csv | Representative sample of 30 events per world matched to the country mix; the draw order, the Instagram readings and the resulting sample | 1,331 / 49 / 171 |
| samples/event_social.csv | Instagram (and other) counts of event accounts, with profile URL and access date | 223 |

## prices/, artists/, sizes/, cities/, economics/, dancers/

| File | Counts | Rows |
|---|---|---|
| prices/latin_events_detail.csv | Prices, days, venue and line-up fields of 162 Latin events, read from official pages in October 2026 | 162 |
| artists/lineups.csv | Artists listed in the line-ups of sampled congresses (as listed and normalised) | 849 |
| artists/name_map.csv | Spellings merged to one artist name | 184 |
| artists/artist_reach.csv | The 60 most booked artists: Instagram followers where a public profile was found, access date | 60 |
| artists/artist_concentration.csv | How many congresses the most booked artists reach (output of `artist_concentration.py`) | 14 |
| sizes/event_sizes.csv, large_events.csv, candidates.csv | Sizes stated by organisers (dancers, spectators), the table of large events, the candidate list | 56 / 25 / 71 |
| sizes/hyrox_finishers.csv, breaking_officialpages.csv | Hyrox finishers per race, breaking flagship pages | 7 / 11 |
| cities/city_list.csv, city_indicators.csv, city_ranking.csv | 24 cities, 12 indicators with source and year, the two rankings with their robustness | 24 / 193 / 48 |
| economics/cost_benchmarks.csv | Public cost benchmarks for an event (venue, sound, staff ...), with source and year | 76 |
| dancers/top30_latin_dancers.csv, top30_breaking_dancers.csv | The 30 most followed Latin dancers and breakers found, by name, with Instagram followers, the fact id and the reading date (October 2026) | 30 / 30 |
| dancers/latin_dancers_not_in_top30.csv | Artists read later whose count would reach the Latin list, held back until the profile is checked | 6 |

The dancer lists are public professional figures and counts shown on their public profile pages; they are the most followed among the dancers found, not a census. Followers are accounts, not unique people.
