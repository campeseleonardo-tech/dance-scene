# Data schema (the shared contract)

Status: v2, 2026-10-21 (v1 of 2026-10-19 plus the clean-up of 2026-10-21). Every prompt and script depends on this file. If a column or allowed value changes, change it here first.

**Scope of data/ since 2026-10-21:** only the current project (15 cities, their 9 countries, GLOBAL, places of events in the comparison sets; breaking, salsa, bachata, mixed street styles, ALL). Rows of earlier, wider rounds live in archive/data_v1/ with the same columns; they are history, not evidence for the current analysis.

## 1. General rules
1. All data lives in `data/` as CSV files: UTF-8, comma separator, one header row, double quotes around any cell that contains a comma, no thousands separators, decimal point `.`, dates ISO (`2026-10-19`, or `2026-10` / `2026` when only that is known).
2. Column names and file names: English, snake_case. Cell text: English.
3. One row = one fact (or one event, one organisation, ...). Never put two facts in one cell.
4. Every fact, event and organisation row points to a row in `sources.csv` through `source_id`. Exception: rows with `evidence_type = not_found` point to the source(s) searched if any, otherwise `source_id` stays empty and `notes` lists what was searched and where.
5. No scores. In this phase we collect raw values with evidence only. No 0-5 ratings, no composite index.
6. Public sources only. No personal data of private individuals. Athletes: only publicly listed professional figures (name, discipline, base city, level).
7. Never invent a number, a source or a URL. If something is not found, write a `not_found` row; do not leave it out silently.
8. "Red Bull absent" is never written. Use `red_bull_involvement = not_found` and keep the search notes. Only a `confirmed_absent` value, backed by a named person or document, can say absent.
9. Do not overwrite or rename files in `data/` from another task: append rows, or edit your own rows (identified by `task_id`).
10. IDs are never reused. Once a row has an ID, it keeps it.

## 2. Allowed values (controlled lists)
- `evidence_type`: `found` (read directly in a source), `stated_by_organiser` (a figure or claim made by the organiser/owner of the thing, not independently checked), `not_found` (searched, nothing there), `inferred` (our own reasoning from other facts; say from what in `notes`).
- `confidence`: `H`, `M`, `L`. H = official source opened and read in this pass. M = reliable secondary source, or official source not re-opened. L = snippet only, estimate, Wikipedia without primary source, or contradictory.
- `access_status` (sources): `opened` (page content read in this pass), `rendered` (needed a JavaScript-rendering browser, content read), `blocked` (access refused or login/consent wall), `not_opened` (known only from a search snippet or from an earlier model, never opened by us).
- `place_type`: `city`, `country`, `global`.
- `role` (places): `deep`, `scan`, `benchmark`, `country`, `global`.
- `scope` (disciplines): `pilot_main`, `pilot_light`, `adjacent`, `out`.
- `red_bull_involvement` (events): `found` (Red Bull is organiser or named sponsor on an official page), `not_found` (organiser and sponsor pages checked, no Red Bull), `not_checked` (sponsor page not looked at yet), `stated_by_organiser`, `confirmed_absent`.

## 3. Files

### data/places.csv
`place_id, place_type, name, country_iso2, region, role, metro_definition, lat, lon, inclusion_reason, notes`
- `place_id`: cities use the 3-letter codes already in the workbook (SBG, INN, VIE, GRZ, MUC, MIL, BCN, AMS, BER, MAD, PAR, NYC, CLO); new cities get a new unique 3-4 letter code; countries use ISO2 (AT, DE, ...); the whole world is `GLOBAL`.
- `region`: `europe`, `north_america`, `latin_america`, `asia`, `africa`, `oceania`.
- `metro_definition`: the area the city figures refer to (e.g. "city proper", "Eurostat FUA", "NUTS3 region"). Never mix definitions silently.

### data/disciplines.csv
`disc_id, family, discipline, sub_style, scope, notes`
- Existing IDs are kept (URB-BRK, URB-HIP, CAR-SAL, CAR-BCH, ...). New: URB-WAA (waacking), URB-VOG (vogue). Kizomba and zouk move out of the Caribbean family (see C2). Tricking is `out`.
- Use `ALL` as `disc_id` in facts that are not discipline-specific (e.g. city population).

### data/signals.csv
`signal_id, signal, definition, unit, notes`
Existing: COM, SCH, SPA, EVT, CMP, ATH, ONL, LAD, PRC. New: ORG (organisations present), POP (population), POPY (share aged 15-34), STU (students), TOU (tourist nights), FUN (funding and support), REG (teaching regulation), INC (income and working conditions), MED (media and content).

### data/sources.csv
`source_id, url, title, publisher, source_type, access_date, access_status, notes`
- `source_id`: `S` + 5 digits (S00001). One row per URL; many facts share it.
- `source_type`: `official_redbull`, `organiser`, `federation`, `public_statistics`, `press`, `wikipedia`, `platform`, `registry`, `academic`, `other`.
- `access_date`: the day the page was opened. A source that was never opened has `access_status = not_opened` and an empty access date.

### data/facts.csv (the main table)
`fact_id, place_id, place_type, disc_id, signal_id, value, value_low, value_high, unit, period, evidence_type, confidence, source_id, task_id, notes`
- `fact_id`: `F` + 6 digits.
- `value` is a number or short text. Use `value_low` / `value_high` for ranges; leave `value` empty then.
- `period`: the year or date the value refers to (not the access date).
- `task_id`: the task of the plan that produced the row (e.g. `P4.2`).
- A `not_found` row has no value; `notes` lists the searches (queries and sites).

### data/events.csv
`event_id, name, series, level, place_id, venue, date_start, date_end, disc_id, organiser_org_id, red_bull_involvement, scale_value, scale_type, scale_evidence, source_id, confidence, task_id, notes`
- `series`: the brand or circuit (e.g. `Red Bull BC One`, `Juste Debout`, `Berlin Salsa Congress`). Same series spelling every time.
- `level`: `class_series`, `social_jam`, `local_battle`, `national`, `international`, `world_final`, `congress_festival`, `qualifier`, `other`.
- `scale_type`: `attendees`, `participants`, `seats`, `countries`, `none`. `scale_evidence` uses the `evidence_type` list.
- Past editions are separate rows (one row per edition, with its year in `date_start`).

### data/organisations.csv
`org_id, name, org_type, place_id, disc_id, scope, website_source_id, evidence_type, confidence, task_id, notes`
- `org_type`: `federation`, `school`, `studio_space`, `crew_collective`, `event_organiser`, `brand_sponsor`, `media`, `venue`, `public_funder`, `other`.
- `scope`: `local`, `national`, `international`.

### data/athletes.csv
`athlete_id, public_name, disc_id, base_place_id, country_iso2, level, red_bull_athlete, source_id, confidence, task_id, notes`
- Publicly listed professional figures only (e.g. Red Bull athlete pages, federation rankings). `red_bull_athlete` uses `found`, `not_found`, `not_checked`.

### data/redbull_finance.csv
`finance_id, entity, jurisdiction, financial_year, scope, metric, value, currency, unit, evidence_type, confidence, source_id, task_id, notes`
- `scope`: `group`, `region`, `business_unit`, `legal_entity`, `dance_related`. Only what is public. Missing breakdowns are `not_found` rows.

### data/relations.csv
Only for links that cannot be derived from the other files (events, organisations and facts already link to places, disciplines and sources through their ID columns; the viewer derives those automatically).
`rel_id, from_type, from_id, relation, to_type, to_id, evidence_type, confidence, source_id, task_id, notes`
- `*_type`: `place`, `discipline`, `org`, `event`, `athlete`, `series`.
- `relation`: `organises`, `sponsors`, `governs`, `member_of`, `qualifies_for`, `hosts`, `teaches`, `part_of`, `partner_of`.

### data/review_log.csv
`log_id, date, item, issue, action, task_id, notes`
Every correction, deletion, move to the archive and re-verification result goes here, one line each.

## 4. Quality checks (run by `scripts/validate_data.py`)
- Required columns present and in order; IDs unique; no empty required cell.
- Every `source_id`, `place_id`, `disc_id`, `signal_id`, `org_id` used in a row exists in its table.
- Controlled-list values only.
- `not_found` rows have non-empty `notes`; `found`/`stated_by_organiser` rows have a `source_id`.
- Dates ISO; numbers parse; `value_low <= value_high`.
- A source with `access_status = opened` or `rendered` has an `access_date`.
Run `python scripts/validate_data.py` after every change; then `python scripts/build_data_summary.py` to refresh research/data_summary.md.

## 5. Standard units in use (write them letter for letter)
New rows reuse these strings so that values measured the same way can be compared. A new unit is added here first.

| Signal | Unit | Counts |
|---|---|---|
| CMP | competitors in the national championship (results list) | dancers (people, or entries if names do not allow it) |
| SCH | schools with a weekly class (fixed search); weekly class slots (schools of R1.1) | schools; classes per week |
| COM | recurring socials or jams (named, active 2026) | recurring events |
| EVT | participants stated (dancers); countries of participants stated, main event; editions held (stated) | dancers; countries; editions (a number, never a year) |
| EVT | Latin events listed on goandance.com, next 12 months; ... , Europe, next 12 months; breaking events listed on and8.dance, next 12 months; breaking events listed, Europe, next 12 months | listings (platform counters, partial) |
| MED | spectators stated | spectators |
| MED | Instagram followers (profile page); Instagram posts (profile page); Facebook page followers; TikTok followers (profile page); TikTok likes (profile page); YouTube subscribers (channel page) | followers (accounts, not unique people) |
| MED | YouTube views, latest final video; YouTube views, most viewed final video; YouTube views, top dance video (non-competition) | views |
| MED | Instagram hashtag posts | reels shown on the public tag page |
| MED | congress attendance stated (sponsor pack); congress age range stated (sponsor pack) | dancers; age range (organiser statement, page or pack) |
| PRC | EUR full pass, main event; EUR full pass, largest event; EUR spectator ticket, main event | EUR per person |
| ORG | Red Bull dance events 2024-2026; Red Bull at Latin participation events (precedents); drinks brands named as sponsors (event) | events; brands |
| POP | persons | inhabitants, city proper unless notes say otherwise |
| LAD | rungs present | 1-5 (class, social/jam, local battle, national, international) |
| MED | Instagram average likes, last 6 posts (profile page) | likes per post (only when visible without login) |
| EVT | event days (stated); competition or battle section (yes/no); workshops offered (yes/no) | days; 1 = yes, 0 = no |
| PRC | EUR competitor entry fee | EUR per competitor (battle or competition registration) |
| EVT | events listed on <source>, snapshot | upcoming events shown by a listing page on the snapshot date (period) |
| PRC | sponsorship tier price stated | EUR per sponsorship tier (notes: tier and what it includes) |
| ORG | Red Bull roles stated at Hyrox events (precedents) | roles or event pages (one fact per source; notes say which) |
| EVT | races stated (season) | races (organiser announcement) |
| BEV | energy drink role at event stated | 1 per event and brand (notes: official drink, bar, sampling, title sponsor, other) |
| EVT | races held (season, Europe); finishers (season, Europe) | races; athletes (Hyrox seasons, period = season start year) |

Round Z keeps event sizes and social metrics in their own CSVs (research/sizes/, research/social/), with the columns given in project/prompt_round_z.md.
