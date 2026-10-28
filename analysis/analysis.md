# Dance Scene Atlas: can Red Bull enter the Latin dance market, how, and where?

Status: round V, 2026-10-21; reviewed by Claude the same day (all 123 cited ids checked against data/; V2 offices added). Evidence base: data/*.csv only (ids in brackets: F = fact, E = event, A = athlete, O = organisation). **computed** = calculated here, formula next to it.
**Important:** the three research tasks of this round (V1 congress sponsors, V2 Red Bull offices, V3 Red Bull audience statements) could not be run: the working session had no access to the open web (see section 7 and analysis/method.md). Every part of the analysis that depends on them is marked **pending**. Nothing was estimated to fill the gap.

## 1. The question and the answer in 5 lines

1. Question: can Red Bull enter the Latin (salsa, bachata) dance market, with what format, and where?
2. Two markets (H1, **supported in a revised form**, rounds X and Y): breaking is a few global spectacle brands (and Red Bull's media) on top of about 210 small, one-day, cheap battles a year; Latin is a broad, stable market of about 450-750 congresses and festivals a year in Europe, three days long and paid by the dancers (full pass about EUR 115). The typical Latin event is more followed than the typical breaking event (p = 0.02). Reference: Hyrox, a fast-growing participation market where Red Bull is a partner, has about 45-60 European races a year (section 11).
3. Attention (H3, **a tendency, not proven**): line-up artists have more followers than their events in both worlds (median ratio 13 in Latin, 8 in breaking); the samples are small and the resolved artists are the better known ones (sections 9-10).
4. Entry (H2, **plausible, not proven**): Red Bull runs participation activations (dance zones, fitness zones, sampling), and no Red Bull presence at a Latin congress was found in 9 countries (all confidence L). Who else sponsors congresses is **pending** (V1). Best fit: product presence at the largest congresses, not a new competition.
5. Where (H4): Paris, Barcelona, Madrid (5 of 6 criteria), then Milan; Paris is the most robust (top also without country-level data). Red Bull office locations were added in the review (confidence L).

## 2. H1 - Two markets

Counts below are of different kinds; the kind is in each cell.

| Block | Breaking (reference) | Latin (case) | Reading |
|---|---|---|---|
| Participation: national championship competitors (dancers) | FR 125 (F001331), DE 107 (F001330), AT 59 (F001336), ES 46 (F001344) | ES 123 (F001334, M), FR 65 (F001332) | Same small size: competitions are not where the mass is |
| Participation: pilot schools, weekly slots (minimums, L unless noted) | Vienna: at least 1 school (F001654), 2 slots (F001660, H) | Vienna: at least 3 schools (F001652, F001653), 30 salsa + 5 bachata slots (F001658, F001659); Milan: at least 8 salsa + 3 bachata slots (F001661, F001662, H) | Latin larger, but only 2 cities, minimums |
| Events: largest stated size | Spectators: IBE 10,000 attendees (E000109), Juste Debout 12,000 (E000107), 6,000 seats per day (F001572) | Paying dancers: Croatian Summer Salsa Festival over 5,000 (E000074), Amsterdam 2,000-2,500 (E000072, E000113), Paris more than 1,500 (F001966) | Different kinds: spectators vs participants. Not additive |
| Events: full pass (EUR, dancers) | not applicable (spectator events) | 120 Graz (F001594), 160 BCN Dance Life (F001598), 190 Warsaw El Sol (F001602) | Latin events are paid participation |
| Audience: YouTube subscribers (followers of channels) | BC One 1,210,000 (F001580), Red Bull Dance 991,000 (F001581) | World Salsa Summit 104,000 (F001649), Euroson 17,800 (F001650), WLDC 7,450 (F001648), The Summit 6,740 (F001651) | Breaking 10-170x larger (channels) |
| Audience: event accounts, Instagram followers | Red Bull Dance 3,000,000 (F001729), BC One 957,000 (F001670), Summer Dance Forever 283,000 (F001737) | Euroson 58,000 (F001675), Croatian 45,000 (F001688), BIG 34,000 (F001694) | Breaking events are brands |
| Reach of dancers, Instagram followers, top 30 each | total 4,330,700; median 108,000; Neguin 795,000 (F001847), Terra 340,000 (F001873), Lil Zoo 244,000 (F001851) | total 6,479,000; median 119,000; Janis & Zoe 1,000,000 (F002887), Ataca y La Alemana 900,000 (F001759), Daniel y Desiree 734,000 (F001761) | Same order of size: medians within 10%, Latin total 1.5x the breaking total (**computed** from the 30 + 30 facts, script scripts/analysis_v.py). **Updated in round AC (2026-10-28):** the first version read only the 30 + 30 dancers of round U; the Instagram counts of 18 dancers of round X (facts F002878-F002928: 10 Latin, 8 breaking) were on file but written as "(athlete A000xx" instead of "athlete_id A000xx", so the script did not see them. With them and 3 Latin dancers read in round AA1/AB (entered in data/ in round AC) 10 Latin (among them Janis & Zoe, 1,000,000, identity confirmed by the author on 2026-10-28) and 2 breaking dancers enter the top 30 and the totals are 6,479,000 (was 4,842,000) and 4,330,700 (was 4,087,700), the medians 119,000 (was 81,000) and 108,000 (was 105,000). See section 16 |
| Top videos outside Red Bull competitions (views) | 100m, 91m, 51m (F001919-F001921), battles | 291m (F001909, possibly audio-led), 99m (F001910), 42m (F001911), performances | Different content |
| Hashtags (Instagram reels) | #breakdance 13m (F001888) | #bachata 38m (F001885, includes music), #salsadance 3.1m (F001886), #bachatadance 875k (F001887) | Latin larger, ambiguous tags |

**Event markets compared on equal terms (round W, added in the review).** Two sets of 20 independent European events, Red Bull events and accounts excluded (lists and selection in analysis/method.md; "largest" cannot be measured exactly because most sizes are unpublished).

| Indicator (unit) | Breaking set | Latin set | Reading |
|---|---|---|---|
| Instagram followers per event account (followers) | 15 accounts: total 1,233,784, median 30,000 (WDSF all-dancesport account excluded) | 17 accounts: total 296,203, median 15,000 | Breaking events tend to be more followed (median 2x), but the difference is not robust: 90% intervals 14k-152k vs 9k-25k, two-sided p = 0.17 (section 9). The breaking top are global touring brands (Summer Dance Forever 283k, World Breaking Classic 210k, BOTY 162k, Freestyle Session 158k) |
| Size stated by the organiser | Spectators: IBE 10,000 visitors, Juste Debout 6,000 seats; competitors: Outbreak 2,000, national finals 107-125 | Dancers: Croatian 5,000, Amsterdam 2,000, Paris 1,500+, Luxembourg Unified 1,500+, SoulDance 1,000+ | Breaking publishes spectators, Latin publishes paying dancers |
| Price per person (EUR) | Spectator ticket: Juste Debout 35, Check The Style 40 (2 of 20) | Full pass: 115 to 245 (9 of 20; e.g. BCN Dance Life 160, BSWC 180, El Sol 210, BIG Milan 245) | A Latin attendee pays about 4x a breaking spectator |
| Calendar, Europe, next 12 months (listings) | and8.dance: 64 | goandance: 158 salsa + 220 bachata (overlapping lists) | Latin events are more numerous; different platforms, read as order of magnitude only |
| Editions | IBE 25th, Juste Debout 20th | Croatian 23rd, El Sol 21st, Festival de Cuba 21st | Both markets are mature |
| Drinks sponsors (partners pages read) | IBE 0, Breakin' Convention 0 | Croatian: Freixenet | Partners pages mostly not published; Red Bull named nowhere |

**Computed**, per flagship event: Latin 2,000 dancers x EUR 150 (middle of the passes on file) = about EUR 300,000; breaking 10,000 visitors x EUR 35 = about EUR 350,000. Same order of money, different source: participants vs spectators (plus sponsors and media for breaking, not measured).

**Verdict: partly supported.** Audience: breaking clearly larger for competition channels; for independent event accounts only a tendency (section 9). Dancers' reach: equal. Participation: Latin larger in the only two cities measured and in congress sizes, but those are minimums and organiser statements, and competition sizes are equal. **Weakest evidence:** participation (two cities, confidence L, minimums) and the 291m video (may be an audio-led upload).

## 3. H3 - Where Latin attention lives

Revised in the robustness review (section 9): the first version compared the top 30 dancers with a mixed list of event accounts and gave 8.5 (Latin) vs 1.25 (breaking). With the two equal event sets of round W:

| World | Top 30 dancers, median followers (90% CI) | Event accounts, W set, median (90% CI) | Ratio dancer / event (**computed**, 90% CI) |
|---|---|---|---|
| Latin | 119,000 (85,500-178,000) | 15,000 (9,085-25,000), n = 17 | **7.9** (4.7-16.8) |
| Breaking | 108,000 (84,500-121,000) | 30,000 (14,000-152,000), n = 15 | **3.6** (0.7-7.9) |

Round AC update (2026-10-28): the table above is recomputed with 43 Latin and 38 breaking dancers on file (top 30 each; section 16). Before: Latin 81,000 (56,000-114,500), ratio 5.4 (3.1-10.9); breaking 105,000 (76,000-118,000), ratio 3.5 (0.7-7.5).

Unit: Instagram followers (accounts, not unique people). **Reading:** in both worlds the most followed dancers have more followers than the events; the gap looks larger in Latin, but the intervals overlap, so this is a tendency. A further bias: the top 30 dancers are the maximum of a very large population of accounts, while events are a few dozen; a fair test compares dancers and events drawn in the same way (round X). For a brand this says where attention may be, not who to pay (see section 4).
**Limits:** Instagram only; counts are rounded by the platform (K/M, confidence M); the Latin list is bachata-heavy (22 of 30 are bachata, 8 salsa, per disc_id in athletes.csv; it was 18 and 12 before round AC) and most dancers have no country on file; the top Latin video is a music video; the event-account list is partial (accounts that were blocked are not_found, F001895, F001896).

## 4. H2 - How Red Bull could enter Latin

**Evidence on file**
- Red Bull participation activations (round U, events.csv): Dance Your Style zone at Open'er 2026 (E000144), DYS Weekender London (E000145), fitness zone at Rock for People (E000146), Hyrox Vienna (E000147), Sweat the Deck (E000149), F45 sampling partnership (E000150), Wings for Life World Run (E000151). None is Latin.
- Red Bull at Latin congresses: no sponsor, partner, sampling or bar found in AT, DE, CH, IT, ES, FR, NL, UK, PL (F001970-F001978, confidence L, only the pages searched).
- Other sponsors of congresses (V1): **pending**. Known from round U: Croatian Summer Salsa Festival lists Freixenet (sparkling wine), Maistra, City of Rovinj, tourist boards (relations of E000074); 10 congresses had no public sponsor pack (F001956-F001965). So whether a drinks brand or an energy competitor is already there is **unknown**.
- Congress profile (organiser statements, dancers): Croatian over 5,000 dancers, 90 countries, ages about 20-60, 8 days of parties (F001967, E000074); Amsterdam 2,000 (F001965); Paris more than 1,500 (F001966); El Sol 4 nights (E000142 notes).
- Red Bull's own audience statements (V3): **pending**.

**Entry formats to evaluate** (not to assume)

| Format | Why it fits the evidence | What it needs | Main risk |
|---|---|---|---|
| A. Product presence at the largest congresses (sampling, night bar, energy partner of the socials) | Congresses are long nights of dancing; 1,500-5,000+ paying dancers each; Red Bull already samples at F45 studios (E000150) | Agreement with the organiser; stock and staff at the event; a measure (cans, contacts) | The sponsor field is unknown (V1 pending); organisers publish no packs, so price and availability are unknown |
| B. A Red Bull night or showcase inside an existing congress, built around the most followed couples | Attention sits with the couples (section 3); the congress already brings the crowd | A congress partner, a fee for performers who are already booked as artists | Reads as influencer marketing if badly done; the 291m reach number is partly music |
| C. A Latin zone inside an existing Red Bull dance event | Precedent: Dance Your Style zone at Open'er (E000144), Weekender London (E000145); no new event to build | A Red Bull event that already has a public (Vienna, Paris, Madrid, Barcelona, London per H4 table) | Breaking audience is not Latin audience; Latin dancers may not travel to a breaking event |

Dancers are **not** proposed as sponsored influencers. They dance; the reach of their profiles is a measure of where attention is, not a channel to buy.

## 5. H4 - Where it would take root

Criteria (each 1 point): (1) Red Bull dance event 2024-2026 in the city; (2) Red Bull national office in the city or its metro (V2, added by Claude in the review from web search snippets: organisations O00109-O00117, confidence L); (3) Latin congress or festival on file in the city or its metro; (4) country has at least 10 Latin listings on goandance in the next 12 months (salsa + bachata, 10 = median of the 9 countries, **computed**); (5) a national Latin championship with competitors on file; (6) at least one top-30 Latin dancer based in the country (athletes.csv). Columns 4-6 are **(country)**.

| City | RB dance events 2024-26 | RB office | Latin congress/festival on file (stated size) | Latin listings in country, salsa+bachata (country) | National Latin championship competitors (country) | Top-30 Latin dancers based in country (country) | Population (city proper) | Met |
|---|---|---|---|---|---|---|---|---|
| Paris | E000011 | O00113 (L) | E000140 (more than 1,500) | 16 (F001933, F001942) | 65 (F001332) | 0 | no city-proper value; 13,125,142 is a FUA (F000047, L) | **5 of 6** |
| Barcelona | E000125 | no (Madrid) | E000075 (Santa Susanna, near BCN; size nf; pass 160) | 120 (F001932, F001941; L) | 123 (F001334) | 1 (A00037) | 1,729,963 (F000043) | **5 of 6** |
| Madrid | E000001 | O00112 | none | 120 | 123 | 1 | 3,339,931 (F000045) | **5 of 6** |
| Milan | none | O00111 | E000139 (Sesto San Giovanni, adjacent; size nf) | 28 (F001931, F001940) | nf | 1 (A00051) | 1,349,930 (F000041) | **4 of 6** |
| Amsterdam | E000124 | O00114 | E000072, E000113 (2,000-2,500) | 6 (F001934, F001943) | nf | 0 | 873,338 (F001583) | **3 of 6** |
| London | E000004, E000028 | O00115 | E000141 (size nf) | 3 (F001935, F001944) | nf | 0 | 8,866,541 (F001163) | **3 of 6** |
| Berlin | E000002 | no (Munich) | E000071 (size nf) | 54 (F001930, F001939; L) | nf | 0 | 3,685,265 (F000039) | **3 of 6** |
| Warsaw | none | O00116 | E000142 (size nf; pass 190) | 10 (F001936, F001945) | nf | 0 | 1,863,056 (F001584) | **3 of 6** |
| Munich | none | O00110 | none on file (Bavarian Bachata Congress O00103 is an account, no event row) | 54 | nf | 0 | 1,505,005 (F000036) | **2 of 6** |
| Rome | none | no (Milan) | none | 28 | nf | 1 | 2,770,226 (F001162) | **2 of 6** |
| Salzburg | none (F001315) | O00109 (Fuschl am See, metro) | none | 4 | nf | 0 | 157,000 (F000033) | **1 of 6** |
| Vienna | E000031 | no (Fuschl) | none | 4 (F001929, F001938) | nf | 0 | 2,040,914 (F000030) | **1 of 6** |
| Innsbruck | E000006 | no (Fuschl) | none | 4 | nf | 0 | 131,358 (F000034) | **1 of 6** |
| Graz | none | no (Fuschl) | E000086 (size nf; pass 120) | 4 | nf | 0 | 302,749 (F000035, L) | **1 of 6** |
| Zurich | E000027 | no (Baar, Zug: O00117) | none | 1 (F001937, F001946) | nf | 0 | 700,889 (F001190) | **1 of 6** |

Notes: counts are listings, not unique events (an event may be in both salsa and bachata); "nf" = not found or not measurable. Santa Susanna and Sesto San Giovanni are separate municipalities (places SSN, SSG), counted as metro with that caveat. 24 of the 30 Latin dancers have no country on file, so criterion 6 is weak. E000032 (a "Salzburg" Dance Your Style row) was corrected to Basel in the data (F001315).

**Top 3-5** (updated in the review with the office criterion)
1. **Paris (5 of 6).** Logistics: Red Bull France office (O00113, L) and BC One cypher in Aubervilliers (E000011). Latin: a congress with more than 1,500 dancers in the city (F001966), a national circuit with 65 competitors (F001332). The only city at the top in both the full and the city-only view.
2. **Barcelona (5).** Logistics: Dance Your Style national final on 5 Sep 2026 (E000125) to attach to; the office is in Madrid. Latin: Spain is the strongest country on every country column; a bachata congress nearby with a 160 EUR pass (F001598).
3. **Madrid (5).** Logistics: Red Bull Spain office (O00112) and BC One Cypher Spain (E000001). Latin: same Spanish market, 123 championship competitors (F001334); no congress in the city on file.
4. **Milan (4).** Logistics: Red Bull Italy office (O00111), but no Red Bull dance event 2024-2026. Latin: Italy third in listings (28) and an adjacent congress (E000139).
5. **Amsterdam and London (3).** Office, a Red Bull dance event and a congress in the city, but thin Latin listings in their countries; strong at city level (see sensitivity).

**Sensitivity: remove the country columns (4-6).** Only criteria 1-3 remain: Paris, Amsterdam and London score 3; Barcelona, Madrid, Milan, Berlin and Warsaw 2; the rest 1 or 0. Paris stays at the top in both views; Barcelona and Madrid owe their rank to Spain's country-level strength; Amsterdam and London rise when only city facts count. Barcelona's congress point rests on Santa Susanna being counted as its metro. The office criterion rests on search snippets (confidence L) and should be confirmed on official pages.

**Salzburg.** Red Bull's home region (group headquarters in Fuschl am See, O00109, counted as Salzburg metro), but on file it scores 1 of 6: no Red Bull dance event 2024-2026 (F001315), no Latin congress, Austria thin (4 Latin listings). An activation in Salzburg would be a home-region pilot rather than a market choice.

## 6. Congress economics

Stated sizes (dancers, organiser statements; lower bounds where "over") and full passes on file:

| Congress | Dancers | Source |
|---|---|---|
| Croatian Summer Salsa Festival | over 5,000 | F001967 |
| Amsterdam International Salsa Festival | 2,000 (2026), 2,500 (2025) | F001965, E000113 |
| Paris International Salsa Congress | more than 1,500 | F001966 |

Full passes (EUR): 120 Graz (F001594), 160 BCN Dance Life (F001598), 190 El Sol Warsaw (F001602). The three passes belong to different congresses, so they are a range, not the price of one event.

**Computed** gross pass revenue = dancers x lowest or highest pass on file (120 / 190), a theoretical ceiling if every dancer paid a full pass:
- Amsterdam 2026: 2,000 x 120 = EUR 240,000 to 2,000 x 190 = EUR 380,000. 2025: 2,500 x 120 = 300,000 to 2,500 x 190 = 475,000.
- Paris: 1,500 x 120 = 180,000 to 1,500 x 190 = 285,000 (lower bound on dancers).
- Croatia: 5,000 x 120 = 600,000 to 5,000 x 190 = 950,000 (lower bound on dancers).

**Calendar (listings next 12 months, salsa + bachata, goandance, partial, ES and DE bachata page counters L):** crowded: Spain 120, Germany 54, Italy 28; thin: Switzerland 1, UK 3, Austria 4. France 16, Poland 10, Netherlands 6.

**Not known (questions, no estimates):** venue and hotel costs; artist and instructor fees; staff and sound costs; share of dancers on discounted or party-only passes; sponsor income; how many of the 2,000 are foreign (12 countries among the first 24 pre-registered, F001965 notes); repeat rate; costs of a smaller congress in a thin market such as Austria.

## 7. What we could not measure and why

- Round V research tasks: no open web access in the working session; V1 (congress sponsors) and V3 (Red Bull audience statements) not run (manual list items 34, 36); V2 done afterwards in the review (O00109-O00117).
- City-level participation: platforms and schools cannot be counted from desk research; only Vienna and Milan minimums (confidence L).
- Social platforms: no logins; TikTok, Facebook and YouTube mostly not read; Instagram counts rounded.
- Missing sponsor packs: none public for 10 congresses (round U).
- Red Bull offices: added in the review from search snippets (L), to confirm on official pages. Salzburg manual data: pending.
- Paris city-proper population not verified (F000048).

## 8. Evidence index

- Section 2: F001331, F001330, F001336, F001344, F001334, F001332, F001654, F001660, F001652, F001653, F001658, F001659, F001661, F001662, E000109, E000107, F001572, E000074, E000072, E000113, F001966, F001594, F001598, F001602, F001580, F001581, F001649, F001650, F001648, F001651, F001729, F001670, F001737, F001675, F001688, F001694, F001847, F001873, F001851, F001759, F001761, F001763, F001909-F001911, F001919-F001921, F001885-F001888.
- Section 3: F001729, F001670, F001895, F001896, athletes A00024-A00026 (U3.2 list).
- Section 4: E000144-E000147, E000149-E000151, F001970-F001978, F001956-F001965, F001967, E000142, E000075.
- Section 5: E000125, E000001, E000011, E000002, E000027, E000004, E000028, E000006, E000031, E000124, E000071, E000139, E000140, E000141, E000142, E000086, E000072, E000113, E000075, F001929-F001946, F001334, F001332, A00037, A00051, F000030, F000033-F000036, F000039, F000041, F000043, F000045, F000047, F000048, F001162, F001163, F001190, F001583, F001584, F001315, O00103, O00109-O00117.
- Section 6: F001965, F001966, F001967, E000113, F001594, F001598, F001602, F001929-F001946.

## 9. Robustness, limits and possible bias (review of 2026-10-21)

Numbers from `python scripts/robustness.py` (seeded bootstrap, 10,000 resamples; permutation test, 10,000 shuffles; data/ only).

| Comparison | Latin | Breaking | Test | Reading |
|---|---|---|---|---|
| Event accounts (W sets), median Instagram followers | 15,000 (90% CI 9,085-25,000), n = 17 | 30,000 (14,000-152,000), n = 15 | P(breaking event > Latin event) = 0.71; p = 0.17 | Tendency, not robust |
| Top 30 dancers, median Instagram followers | 119,000 (85,500-178,000) | 108,000 (84,500-121,000) | P = 0.42; p = 0.56 | No difference (round AC update; before: 81,000 vs 105,000, p = 0.35) |
| Dancer / event ratio | 7.9 (4.7-16.8) | 3.6 (0.7-7.9) | intervals overlap | Tendency, not robust (before: 5.4 vs 3.5) |
| Price per person | full pass, n = 8 of 20: median 152, range 115-245 | spectator ticket, n = 2 of 20: 35, 40 | too few breaking prices | Direction clear, sample thin |
| Stated size | dancers, n = 5 of 20: 1,000-5,000 | dancers n = 3 (107, 125, 2,000), spectators n = 2 (6,000, 10,000) | too few | Reporting conventions differ |

**Confidence per conclusion**

| Conclusion | Confidence | Why |
|---|---|---|
| Red Bull's breaking media (BC One, Red Bull Dance) dwarf every Latin channel | High | 10-170x, many sources |
| Competitions are small in both worlds | Medium | 6 national finals counted |
| Latin congresses sell participation at EUR 115-245 per person | Medium | 8 prices, organiser pages |
| Independent breaking events are more followed than Latin events | Rejected for typical events (round X, p = 0.02 the other way); true only for flagships | random samples of 30 + 30 |
| Latin attention sits with dancers more than in breaking | Low | overlapping intervals, selection bias |
| Same order of money per flagship event | Low | two examples, computed |
| Red Bull is absent from Latin congresses | Medium-low | not found in 9 countries; partner pages rarely published |
| Paris, Barcelona, Madrid as entry points | Medium | depends on country-level columns and office rows |

**Possible confirmation bias (named, not hidden)**
1. Selection: the 20 + 20 events are the most visible ones we could find, not a random sample; the breaking top are global touring brands, the Latin ones mostly local congresses.
2. Asymmetric comparison: top-30 dancers (maximum of thousands of accounts) against a few dozen events.
3. Reporting conventions: Latin organisers state dancers, breaking organisers state spectators; part of "participation vs spectacle" may come from how each scene communicates.
4. No search for counter-evidence yet: paid participation in breaking (battle entry fees, workshop passes; Outbreak states 2,000 participants) and spectators in Latin (shows, finals with an audience).

**Tests written before new data (round X), with what would weaken each hypothesis**
- H1 weakens if, in a random sample of events, breaking events show paid participant numbers or prices close to Latin ones, or Latin events show spectator audiences close to breaking ones.
- H1 (audience) is confirmed only if the follower difference between random samples of 30 + 30 events is significant (two-sided p < 0.05).
- H3 weakens if, with dancers drawn from the line-ups of randomly sampled events, the dancer / event ratio is the same in both worlds.
- H2 weakens if drinks or energy brands already sponsor most large congresses, or if organisers say a drinks partner is not wanted.

## 10. Round X: random samples and the tests of section 9 (review of 2026-10-21)

**Sampling.** Frames of events in Europe from 2026-11-01 to 2027-10-31 (data/samples/): Latin from goandance.com, all salsa and bachata listings read page by page (222 events, 188 eligible); breaking from and8.dance (71, 51 eligible; and8 is a battle registry, not the full European calendar). 30 events drawn per world with scripts/draw_sample.py (seed 20261021); frames not edited after the draw. Numbers from `python scripts/robustness.py` (section "Round X").

| Measure | Latin (30 random events) | Breaking (30 random events) | Test |
|---|---|---|---|
| Instagram followers per event, median (90% CI) | 4,461 (3,527-7,528), n = 17 | 1,641 (420-3,017), n = 23 | P(breaking > Latin) = 0.26; p = 0.02 |
| Same, events without an account counted as 0 | 2,455 (n = 29) | 1,257 (n = 26) | direction unchanged |
| Event days, median | 3 (range 1-7) | 1 (range 1-6) | |
| Price per person | full pass: median EUR 115 (45-179), n = 23; party-only ticket EUR 59-89, n = 4 | no full pass found; spectator ticket median EUR 8.50 (0-14), n = 6; entry fee median EUR 10 (0-25), n = 5 | |
| Competition or battle section | 14 of 21 read | 28 of 28 read (battles by definition of the frame) | |
| Workshops | 22 of 23 read | 5 of 6 read | |
| Stated participants / spectators | 1 / 0 | 0 / 0 | sizes are almost never published |
| Line-up artists, Instagram followers, median | 59,000, n = 12 | 13,000, n = 8 | p = 0.20 |
| Frame size (listings, next 12 months, Europe) | 188 eligible | 51 eligible | different platforms |

**The tests written before the data (section 9)**
- *H1, audience side ("confirmed only if random samples differ significantly")*: they differ significantly, **in the opposite direction**: the typical Latin event is more followed than the typical breaking event. Breaking's audience advantage exists only at the top (global touring brands, Red Bull media). **Rejected for typical events; holds for flagships.**
- *H1, participation side ("weakens if breaking shows paid participation close to Latin")*: it does not: breaking events are mostly one day, with tickets around EUR 9 and entry fees around EUR 10; Latin events last 3 days and sell passes around EUR 115. But breaking events are participatory too (every sampled event is a battle where dancers compete, most with workshops). **Supported in a revised form: both worlds are participatory at the base; Latin monetises participation, breaking monetises attention at the top.**
- *Counter-evidence for Latin*: 14 of 21 Latin events read have a competition section, and 5 of 20 flagship congresses sell show or party-only tickets (EUR 15-65, round X4). Latin is not purely social.
- *H3 ("weakens if line-up artists show the same ratio in both worlds")*: ratios 13 (Latin) vs 8 (breaking): same direction as H3, but 12 + 8 artists and the better known ones resolved: **not proven**.
- *H2 (sponsors)*: partners sections were not readable for the 55 new events (JavaScript pages): **untested**; only talks with organisers can settle it.

**Remaining biases.** The two frames come from different platforms (a ticket marketplace for Latin, a battle registry for breaking): goandance lists mainly paid multi-day events, and8 also small jams. A fair reading is "the typical listed event" in each world. 12 of 29 Latin and 3 of 26 breaking sampled events have no Instagram account found; counting them as 0 does not change the direction. BIG Milan full pass: EUR 245 (round W) vs EUR 170 (round X re-read), both kept.

**What this changes for Red Bull.** The Latin market has a broad, followed middle: many multi-day events where paying adults dance for 3 days and nights. Breaking's middle is thin: small one-day battles, with the audience concentrated on a few global brands, one of them Red Bull's own. That strengthens H2 as a format (product presence across many mid-size congresses) and weakens any idea of a single big Latin "show" event.

## 11. Round Y: census of the European event market (latin, breaking, Hyrox as reference)

Sources and method: analysis/method.md; lists in data/events/by_source/; merge and estimates `python scripts/census_merge.py`; tables `python scripts/census_stats.py` (Russia, Belarus, Turkey excluded). Window: 2024-11 to 2027-10. Hyrox is the reference: a participation market where Red Bull already plays.

**Sources.** Latin: latindancecalendar.com (763 listings), salsavida.com (299), goandance.com (206). Breaking: and8.dance (480); no second public calendar of comparable size exists (web search found 11 events, 5 of them on and8; WDSF 1). Hyrox: hyrox.com (137), rundida.com (52), hybridfitnessmedia.com (22).

| Distinct events (all sources merged) | Past 12-24 months | Past 0-12 months | Next 12 months |
|---|---|---|---|
| Latin | 304 | 305 | 450 |
| Breaking | 210 | 212 | 60 |
| Hyrox | 41 | 61 | 45 |

Past Latin rows come from one source only (latindancecalendar.com via archived pages): the past columns undercount Latin. Breaking events are announced late, so its next-12-months column undercounts breaking.

**How big is each market (events per year in Europe)?**
- Latin: at least 450 events in the next 12 months across three sources. The overlaps give estimates of 330 to 760 (Chapman, pairwise); they disagree because the lists are not independent (the big events are on every list), which pushes the estimates down: read **about 450-750 Latin congresses and festivals a year**, of which goandance covers about 27-63% and latindancecalendar 27-44%.
- Breaking: **about 210 events a year on and8.dance** (past 12 months). Its coverage cannot be estimated without a second calendar; the 11 events found by web search were 5 on and8 (weak hint of about half).
- Hyrox: **about 45-60 races a year in Europe**, almost fully listed (rundida's 39 upcoming races are all on hyrox.com).

**Trend (same source, past 12-24 vs 0-12 months; and archived snapshots).**

| Source | Past 12-24 m | Past 0-12 m | Change | Archived snapshots of the listing page (Europe) |
|---|---|---|---|---|
| latindancecalendar.com (Latin) | 304 | 304 | 0% | 348 (Oct 2024), 391 (Nov 2025), 178 live (cause of the drop not tested) |
| and8.dance (breaking) | 210 | 206 | -2% | 41 (Oct 2024), 63 (Jul 2025), 53 live |
| hyrox.com (Hyrox) | 41 | 50 | +22% | 24 (Nov 2024), 47 (Sep 2025), 45 live |

Reading: **Latin and breaking are stable; Hyrox is growing fast** (season target 107 race weekends and 2 million athletes in 2026/27, trade report, confidence L).

**Where the events are (next 12 months).** Latin: Spain 21%, Germany 13%, Italy 10%, France 9%, Greece 5%, UK 4%. Cities named in the lists (all periods): Barcelona 50, Amsterdam 19, London 17, Paris 17, Athens 17, Berlin 16, Prague 15, Budapest 12, Hamburg 11. Breaking (and8): Germany 25%, France 17%, Switzerland 17% (and8 is strongest in German-speaking countries: platform bias). Hyrox: France 16%, UK 16%, Netherlands 11%; cities Paris 7, London 7, Rotterdam 5, Barcelona 4, Amsterdam 4.

**Hyrox as the reference for Red Bull.**
- Red Bull is named on all 15 Hyrox race pages read; as event or finish-zone partner on 9 (task Y5, relations `partner_of`); listed among Hyrox's global sponsors since 2020 (Wikipedia, L).
- Price per athlete: EUR 60-89, median 75 (rundida, n = 10).
- Size: 175,000 competitors in 65 races worldwide in 2023 (Wikipedia, L): about 2,700 per race (**computed**).

| | Hyrox (Red Bull partner) | Latin congresses (Red Bull absent) |
|---|---|---|
| Events per year in Europe | about 45-60 | about 450-750 |
| Size per event | about 2,700 athletes (2023 average, computed, L) | 1,000-5,000 dancers at flagships; typical size unknown |
| Price per participant | EUR 60-89 per race | EUR 115 typical full pass, up to 245 (round X) |
| Days | 1-3 (race weekend) | 3 typical |
| Trend | growing fast | stable |
| Organisers | one company (one partnership covers every race) | hundreds of independent organisers |

**What this means.** Red Bull already backs a participation market of about 50 European races a year. The Latin congress circuit is about ten times as many events, its participants pay more per head and stay longer, and it is stable rather than growing. The real difference is **fragmentation**: Hyrox is one organiser, so one partnership reaches every race; Latin is hundreds of independent organisers. An entry therefore needs a way to reach many congresses at once (a circuit, a platform, or the 20-30 largest congresses) or must start with a few large ones.

**Business case, light (only what is public).** No European Latin or breaking event publishes a sponsor pack with prices (7 searches, EN/FR/ES/DE); SalsaVida sells event promotion at about EUR 89 a month (L). Market volume (dancers per year) cannot be computed: typical congress sizes are not published. A scenario for later talks, **not a finding**: 450-750 events x 300-1,000 dancers each = about 135,000-750,000 congress participations a year in Europe (both ranges are assumptions to test with organisers).

**Limits.** Breaking has one calendar; past Latin events come from one source; cities are missing for many rows (country only); Hyrox past races partly from archived pages; sizes almost never published.

## 12. Round Z: large events, breaking count, social attention (review of 2026-10-21)
Data: data/sizes/ (candidates.csv, event_sizes.csv, large_events.csv, hyrox_finishers.csv, breaking_officialpages.csv), data/samples/event_social.csv, log analysis/method.md. Method: cloud agent with full web access; sizes from search results and organiser or press statements (no site reads in most cases), so almost all figures are claims (confidence L-M). large_events.csv is Claude's curated table (one line per event and people type, with what is in and out of the comparison and why).

**Large events, Europe, last 12 months (latest stated edition 2024-2026; Red Bull events, events outside Europe or the window, and mixed street-dance events left out):**

| | Latin | Breaking |
|---|---|---|
| Events with >= 300 people taking part (dancers) | 12 | 2 |
| Events with >= 1,000 taking part | 10 | 1 (Outbreak Europe) |
| Events with >= 3,000 taking part | 2-3 (Croatian Summer Salsa Festival, Berlin Salsacongress, Amsterdam at the high end) | 0 |
| Dancers at the events with >= 1,000 | about 23,000-26,500 | about 2,000 |
| Events with >= 3,000 spectators or visitors | none stated | 3 (Notorious IBE 10,000; Battle Pro 4,500 planned; Outbreak 3,200, year unconfirmed) |

Reading: Latin's large events are many and made of paying participants; breaking's are few and made of spectators. This is the two-markets thesis seen at the top of the market. Limits: 20 of 30 Latin candidates and 15 of 26 breaking candidates have no stated size, so the counts are lower bounds; Latin figures are self-declared ("over 2,500 dancers") and round numbers. Juste Debout (6,000-12,000 spectators) is left out because it has no breaking category; with it, breaking would have 4 spectator events of 3,000+.

**Breaking total count (Z2):** no second breaking calendar exists that can be harvested (bboyrankingz.com is a hijacked page, bboyevent.com stopped in 2020, federation calendars blocked or absent). The census stays at about 210 breaking events a year on and8.dance. Of 11 breaking events found on official pages, 7 are on and8.dance (64%); because these are mostly flagships, and8's coverage of small events is probably lower, so the true total is probably above about 330 a year. It cannot be placed against Latin's 450-750 with the same method. The 11-event list is kept out of data/events/by_source/ (moved to data/sizes/) so that it does not enter the capture-recapture estimates.

**Breaking total count, update of round AC (2026-10-28):** a second calendar *can* be harvested by hand: breaking-calendar.com (the author's export of 2026-10-28, 197 events in 2026, 135 of them past). Matched with the and8 side of the census, Europe 2026: 205 and 96 events, 62 in both; Chapman (205+1)(96+1)/(62+1)-1 = **316** (and8 covers 65%); past part 263, upcoming part 51 (about 300 a year). This replaces "probably above about 330" by an estimate of **about 300 (263-316)**, inside the range on page 2 ("210 to about 330"). Confidence L-M (lists not independent, breaking-calendar thin in the past). probreakingtour.com is not usable as a calendar (US recap archive). Details: section 16 and analysis/method.md.

**Social attention (Z3):** Instagram blocked the cloud session; follower counts come from search-result snippets of unknown date, no likes or comments, no YouTube or TikTok. Medians: large events, Latin 9,568 followers (n = 10) vs breaking 49,000 (n = 6); random typical events, Latin 3,040 (n = 17 with a profile found) vs breaking 2,800 (n = 8). Too thin and too old to change the round X result (typical Latin events more followed, p = 0.02); it confirms that breaking's attention advantage sits at the top. Engagement (likes, comments) remains unmeasured.

**Hyrox (Z5):** 2025, worldwide: 89 races, 779,073 finishers, about 8,750 per race; London ExCeL over 34,000. The deck's "about 2,700 per race" (2023) is replaced. European totals are not published.

**Drinks brands (Z4):** none recorded (sites were not opened). Still a question for the organiser talks.

**Point figures used in the deck (v16, 2026-10-21), so that each number on a slide can be traced:**
- Latin events per year: about 600 = central value between the 450 counted (next 12 months, 3 calendars) and the overlap estimates (330-760, section 11).
- Breaking events per year: about 330 = 210 counted on and8.dance / 0.64 (share of the 11 official-page events that and8 lists, section 12); a minimum, since that check covered mostly flagships.
- Hyrox: 61 European races counted in the last 12 months (census, past 0-12 months).
- Latin large events: 10 with 1,000+ dancers, about 25,000 dancers in total (central values of data/sizes/large_events.csv); average of the 10 largest about 2,400.
- Ticket money per flagship (computed): Latin 2,000 x EUR 150 = 300,000; breaking 10,000 x EUR 35 = 350,000; Hyrox 8,750 x EUR 75 (rundida median) = 656,000.
- Dancer-nights (computed): pilot 2,000 x 3 = 6,000; 10 largest 25,000 x 3 = 75,000; circuit 600 x 300 (assumed typical size) = 180,000 entries a year.
- Revenue per can: Red Bull 2025, EUR 12.2bn / 13.97bn cans (press) = about EUR 0.87.
- Country shares: census, Latin next 12 months; breaking and Hyrox past 0-12 months (scripts/census_stats.py and merged_events.csv).

## 13. Round AA1: prices and line-ups of 162 Latin events (first look, 2026-10-21)
Data: data/prices/latin_events_detail.csv, data/artists/ (lineups.csv, name_map.csv, artist_reach.csv), log analysis/method.md. Sample: 150 random Latin events of the next 12 months + 12 large; 149 in scope (13 were weekly parties or one-day workshops).

**Coverage (what is usable):** days 92% (usable); full pass price 54% of in-scope events (80; usable, but the tier is unknown for 70, so early bird and door prices are mixed); venue type 50% (usable with care); line-up 57 events (38%, 52 of them from goandance pages, bachata- and Spain-heavy: usable for concentration, with that bias); competition and live band only as "yes" (absence not recorded: not usable as a rate); stated size 9 (not usable); party pass 14, hotel package 14 (examples only); Instagram followers for 11 of the 40 most booked artists (examples only).

**Prices (random sample, n = 76):** median full pass EUR 110 (25th-75th percentile 90-130; 90% bootstrap interval of the median 99-119), range 45-250. By length: 1-2 days EUR 87 (n = 6), 3 days EUR 114 (n = 37), 4+ days EUR 110 (n = 37): price rises little with length, so a longer event costs less per day. By country (n >= 5): ES 115 (23), IT 118 (8), DE 105 (12), PL 130 (6), FR 130 (5). Events in hotels EUR 130 (n = 21). Correlation with price (Spearman): number of artists 0.30 (n = 45), days 0.22 (n = 80): weak. Party-only passes: median about EUR 65 (n = 14).

**Line-ups (57 events, 416 distinct artists, median 9 per event):** 319 artists appear once; 40 appear 3+ times. Most booked: Cristian & Gabriella 7, Melvin & Gatica 6, Ronald & Alba 6, Kike & Nahir 5, Terry & Cecile 5, Sakis & Mia 5. Concentration: the top 10 appear at 54% of the events, the top 20 at 67%, the top 40 at 77%. Set cover (greedy): 5 artists reach 44% of the events, 10 reach 68%, 14 reach 81%. Reading: a small group of artists connects most congresses; a partnership with about 15 artists would touch four in five events. Limit: only 38% of events had a readable line-up, mostly goandance listings (bachata-heavy, Spain 20 of 57), so the concentration may be overstated for salsa and for events outside goandance.

## 14. Rounds AB and AA3: checks after the overnight round (2026-10-22)
**Events, second pass (AB part B).** 104 events revisited on official sites (86 read, 18 blocked). No filled value was overwritten (21 changes were "unknown" turned into a value). Now: full pass price for 91 of 149 in-scope events (random sample n = 85: median EUR 110, quartiles 88-133, 90% interval of the median 99-119: unchanged); price tier known for 21 only; line-ups 61 events (from 57); competition and live band still recorded only as "yes" (not usable as rates). By length: 3 days EUR 105 (n = 42), 4+ days EUR 115 (n = 40); price per day median EUR 31.5. Hotels EUR 123 (n = 28). Hotel packages: 16 examples, bases too different to average. Line-ups: 452 distinct teachers and couples; top 10 at 61% of events, 14 artists reach 80% (same result as section 13). Most booked: Cristian & Gabriella 8, Kike & Nahir, Melvin & Gatica, Ronald & Alba 6. Artists' base country (51 of 60): Spain 27, Italy 7, Cuba 5, France 3, Mexico 2: the circuit's artists are mostly based in Spain. Instagram followers: 26 of 60.

**Cities, fixes (AB part A).** Brussels-Capital Region added (1,255,834; use it instead of the municipality); Prague population added from the Czech Statistical Office (age share missing); London air passengers (177.6M, UK CAA 2024) and nights (153.7M, ONS + VisitBritain) added as documented exceptions; Red Bull offices: Prague, Athens (Marousi), Budapest, Bucharest yes, Brussels no (market served from Menen); Red Bull dance events 2024-2026 for all 24 cities (London 3; most cities 0-1).

**Cost benchmarks (AA3, data/economics/cost_benchmarks.csv, 76 rows).** Usable as model inputs: ticketing fees (Eventbrite, 9 countries), card payment fees (Stripe, PayPal, Mollie, SumUp), music rights (GEMA EUR 152 per night for about 500 m2 and 500-1,500 people; AKM minimum EUR 54), sound and light (Germany: EUR 545 per day up to 400 people, EUR 985 up to 1,000), parquet dance floor (EUR 540 per day for 36 m2, about EUR 15 per m2), insurance (UK table, about EUR 80-1,000 per event by attendance), photographer (EUR 620-1,450 per day), wristbands (about EUR 50 per 1,000), flights (Ryanair average fare EUR 51, without extras), hotel room-block commission (Kempinski 12%). Weak or wrong: VAT (only standard rates; reduced rates for cultural events exist in several countries, e.g. AT 13%, DE 7%, IT 10%, FR 5.5%, NL 9%, and must be checked per case); venues (only two small halls in Graz, about 240 people); artist fees (private lesson rates, not congress fees: not usable); first aid (none); the Seattle hotel row (US, dropped from the model).

## 15. Congress model and city rankings (2026-10-22)
**Congress model: analysis/congress_model.xlsx** (built by `python scripts/build_congress_model.py`, formulas checked against the same model in Python after recalculation in LibreOffice). Sheets: README, Inputs (colour-coded: public source, market data, assumption, to fill), Results, Model, Sensitivity, Country, Market, Sources. No Red Bull sheet (the author's decision: not relevant until Red Bull's role at an event is known). With the default inputs (Austria, standard VAT, listed full pass EUR 110 with 10% average discount, party pass EUR 65, placeholders for artist fees EUR 800, hall rent and hotel price):

| | 300 dancers | 800 dancers | 2,000 dancers |
|---|---|---|---|
| Revenue | EUR 24,163 | EUR 66,434 | EUR 169,085 |
| Costs | EUR 35,325 | EUR 70,774 | EUR 140,645 |
| Result | EUR -11,162 | EUR -4,340 | EUR 28,440 |
| Break-even dancers (same set-up) | 462 | 863 | 1,588 |
| Break-even full pass (listed) | EUR 186 | EUR 121 | EUR 81 |

Reading: with these inputs a congress pays off only from roughly 900-1,000 dancers, or with a higher pass in a smaller format. The result moves most with the number of dancers and the pass price (20% swing: about EUR 22,000 and 17,000 in the medium scenario); among costs, artist fees, hall rent and sound come first. All three are placeholders or single benchmarks: the model is as good as the offers that replace them.

**City rankings: analysis/city_ranking.md** (`python scripts/city_ranking.py`; data data/cities/). 24 cities, 12 indicators, two views, 2,000 random block weightings.
- *Red Bull entry* (Latin scene, Red Bull on the ground, reach): Paris 1st (top 3 under 100% of weightings), London 2nd (88%), Amsterdam 3rd (79%), then Barcelona (strongest Latin scene, 50 events, but no Red Bull office in the city), Berlin, Madrid, Vienna. Salzburg 21st. Robust: the top 3 stay the same when any one indicator is removed.
- *New congress* (demand, access, room in the market, cost): no clear winner; Prague, Madrid, London, Paris, Budapest and Warsaw are within 0.02 points and each is in the top 3 under only 33-49% of weightings. Cheaper, less crowded capitals (Prague, Budapest, Warsaw) rank high because of low price levels and few large congresses nearby. Salzburg is last. Read as a short list, not a ranking.
- Limits: price level is national; tourism nights are regional (London: UK sources); OpenStreetMap counts all dance schools; Prague's age share is missing (counted as the median).


## 16. Round AC: the author's exports of 2026-10-28 (matched with the data on file)

Inputs: seven files saved by the author from the browser (raw page copies, not published; the tidy exports are in data/events/by_source/exports/). Each result is labelled confirmed / corrected / new / contradicted. Europe is the focus; America is reported apart and never mixed into the European counts.

**Numbers on pages 1-3 of the summary: before and after**

| Number on the pages | Before | After round AC | Why |
|---|---|---|---|
| Top 30 Latin dancers, total followers (page 2) | 4.8 million (4,842,000) | **6.5 million (6,479,000)** | 10 dancers enter the list, 10 leave; +34% |
| Top 30 Latin dancers, median (page 2) | 81,000 | **119,000** | +47% |
| Top 30 breaking dancers, total (page 2) | 4.1 million (4,087,700) | **4.3 million (4,330,700)** | 2 breakers enter (Lil Amok 208,000, Franky Dee 74,000), 2 leave; +6% |
| Top 30 breaking dancers, median (page 2) | 105,000 | **108,000** | +3% |
| Title "about the same reach" | holds | holds | medians 119,000 vs 108,000 (p = 0.56); the Latin total is now 1.5x the breaking one (6.5 vs 4.3 million). The title is still true for the typical dancer, but the totals no longer look equal |
| Breaking events a year, "210 to about 330" (page 2) | 210-330 | unchanged | Chapman on breaking-calendar.com gives 263-316, about 300 |
| Maps, past 12 months (page 2) | Latin ES 25%, FR 12%, DE 10%, IT 7%; breaking DE 26%, FR 14%, CH 12%, IT 8% | unchanged | census untouched; breaking Germany 26% in the union of the two calendars; Spain first in the goandance export (33%) |
| Prices (page 2): full pass EUR 110, day pass EUR 84 | | unchanged | goandance "From" median EUR 100 (3+ day events, n = 226); on the same 63 events our full pass median is 110 and "From" 100 |
| "No Red Bull presence found" (page 1) | | unchanged, better supported | 20 largest congresses read by the author: 2 list partners, none an energy drink |
| 1,541 events researched (page 1) | | unchanged | the exports are cross-checks, not merged into merged_events.csv |

### Top 30 Latin dancers
- How the list was built (round U, 2026-10-21, task U3.2): 52 candidates looked at, found from three line-up pages (BSWC 2027, Milano Sensual Congress 2026, Berlin Salsacongress 2026), the headliners of the largest congresses, the creators of the top videos and champions known from the sources; 38 handles read on the public profile page; ranked by Instagram followers; 30 kept. The log says "not a closed list".
- Why the follower counts were not visible next to the names: names are in data/athletes.csv, counts in data/facts.csv, and the only link is the text "athlete_id A000xx" inside the free-text notes column. data/dancers/top30_latin_dancers.csv now puts rank, name, style, country, followers and fact id in one table (scripts/top30_latin.py).
- **Gap found:** a second note format, "(athlete A000xx", was used for 18 dancers of round X (X3, line-up artists of the random samples: 10 Latin, 8 breaking), and 3 Latin dancers read in round AA1/AB were never entered in data/. The first top 30, scripts/analysis_v.py and scripts/robustness.py missed them. Fixed: the scripts read both formats; the three AA1/AB dancers are now in data/ (A00141-A00143, F003205-F003207, S00766-S00768).
- Entered the Latin list: Janis & Zoe 1,000,000 (identity confirmed by the author, 2026-10-28: bachata dancers with over 1 million followers); Marco Espejo 216,000; Antony & Belen 160,000; Melvin y Gatica 120,000; Seo Fernandez 118,000; Gero y Migle 111,000; Cristian y Gabriella 76,000; Sakis y Mia 68,000; Miguel y Sunsire 47,000; Gaby & Estefy 46,000. Left it (now rank 31 and below): Judith Cordero 41,000, Evelyn La Negra 41,000, Adrian Ros 35,000, Denisse Cambria 34,000, Griselle Ponce 34,000, Charlie y Vero 28,000, Irene y Tomas 24,000, Cristian Vergari 24,000, Frankie Martinez 22,000, Rodrigo Cortazar 42,000. The 30th is now Gaby & Estefy, 46,000 (was 22,000). Bachata 22 of 30, salsa 8 (was 18 and 12). The top 5 hold 3,397,000, 52% of the total.
- **Janis & Zoe** (F002887, A00099): the handle was found by name search and the bio does not name the dance style; the author confirmed on 2026-10-28 that they are bachata dancers with over 1 million followers, so they are in the list (notes of A00099 and F002887 updated). Held back (profile found without a bio check, round AB, 22 Oct): Maykel Fonts 166,000, Antonio & Jasmina Berardi 105,000, Jorge Camaguey 97,000, Barbara Jimenez 68,000, Eneris Mulgado 57,800, Fadi Fussion 56,000 (data/dancers/latin_dancers_not_in_top30.csv). If all of these were accepted too, the total would be 6,702,000, the median 120,000 and the cut 68,000 (Latin and breaking lists would then differ even more).
- Consistency: four dancers read twice (Kike y Nahir 436K, Ronald y Alba 196K, Pablo y Raquel 130K, Evelyn La Negra 41K) have the same count in both rounds. One conflict: Terry y Cecile 56,000 (round U) against 47,000 (round AB, "personal account of Terry, no couple account verified"); the round U value is kept.
- Antonio & Jasmina Berardi: not in athletes.csv; in the line-ups of two sampled events and in the goandance directory (3 events, 7 goandance followers, a platform count that is not Instagram). Their Instagram count (105,000, profile found, identity not bio-checked) is above the new cut-off of 42,000: their absence is a gap of the selection method, not a real result. To enter they need more than 42,000 verified followers.

### Dancer / event ratio and robustness
scripts/robustness.py after the update: Latin median 119,000 (90% CI 85,500-178,000), breaking 108,000 (84,500-121,000), P(breaking dancer > Latin dancer) = 0.42, p = 0.56. Dancer / event ratio: Latin 7.9 (4.7-16.8), breaking 3.6 (0.7-7.9); before 5.4 and 3.5. The direction of H3 is the same and a little stronger; the intervals still overlap: **tendency, not proven**. Caution: part of the 30 dancers are line-up artists drawn at random in round X, so each list now mixes two selection routes (in both worlds).

### Breaking: breaking-calendar.com and probreakingtour.com
- breaking-calendar.com, 214 events (197 in 2026). Europe 2026: and8 side 205, breaking-calendar 96, both 62; Chapman 316; and8 covers 65%; union 239. Past part 263, upcoming part 51. **About 300 a year (263-316), confidence L-M.** The 25-day check of 28 Oct (19 of 27) is confirmed (19 of 28 in the export).
- Only on breaking-calendar: 34 events (Germany 11, UK 9, France 5). Only in the census: 143. and8 is weak on the UK (1 UK event in 2026 against 13). The German-speaking lead is **not** an and8 artefact: Germany 25% (and8), 31% (breaking-calendar), 26% (union).
- Red Bull in Europe 2026: BC One Cypher Austria, Switzerland, Belgium and the Dance Your Style World Final in Zurich; all already in the census. Outside Europe: 6 BC One Cyphers in Japan; BC One Camp (26 Nov) and World Final (29 Nov) in Toronto.
- probreakingtour.com: 80 recaps 2019-2026, US events only, a recap archive and not a calendar; 1 of 80 is on breaking-calendar.

### America (second region, reported apart)
Breaking-calendar lists 6 events in North America in 2026 (USA 3, Canada 3, two of them Red Bull events in Toronto) and 2 in Latin America; probreakingtour shows about 11-14 US recaps a year. The US scene is thinly covered by both lists, so no US count is attempted and nothing is added to the European numbers. The goandance export has 20 listings outside Europe (Turkey 8, which the census definition puts outside Europe, Thailand 2, Morocco 2, one each in Bolivia, Cuba, Vietnam, Malaysia, UAE, China, Egypt, Japan), no large congress in the Americas. Red Bull's America presence on file is the Toronto BC One finals. What it adds: the European definition leaves out Japan, where breaking-calendar lists 76 events in 2026, more than any European country (Germany 32 in the same list).

### Latin: goandance events (317 listings, 9 Oct 2026-3 Dec 2027)
- 297 European listings, Spain 33%: confirmed. 80% of the 3+ day European listings of the window 22 Oct-31 Dec (53 of 66) are in the census; 5 of the 13 missing are in scope. Annual count not recomputed (sources not independent), "450-750" unchanged.
- "From" prices: median EUR 100 (3+ days, n = 226); our full pass median EUR 110 on the 63 matched events (goandance "From" 100): **confirmed**. "From" is the cheapest tier shown, so a lower bound.
- Stated sizes: confirmed BCN Sensual Family 2,000, Luxembourg 1,500, Transilvania 1,000. New (organiser statements, L): All Stars Festival Budapest 1,500, ABCD Festival London 2,500, Latina Istriana 1,500, Latin Dreams Festival 1,000+, Salsa Festival Prague 450+, Costa Dorada 500.

### Artists: goandance directory (3,215 artists, 627 with events)
- The 14 artists with most events (Masa & Polina 16, Cristian y Gabriella 14, Alfredo & Andrea 10, Melvin y Gatica 10, Ronald & Alba 9, ...) are all in our line-up sample: **confirmed** (Spearman 0.51 on 320 shared artists).
- **Corrected in scale:** "5 artists reach 44% of the events, 10 reach 68%, 14 reach 81%" holds for the 57 congresses with a readable line-up. In the directory the top 14 hold 132 artist-slots, at most 42% of the 317 listings (top 5 at most 19%, top 10 at most 32%). Quote 44/68/81% only with "of 57 congresses with a published line-up".
- goandance followers (Cristian y Gabriella 50) are tiny and are not a reach measure; never compared with Instagram.

### WDSF athletes and sponsors
- WDSF hip hop and breaking: 972 rows, 494 with a breaking result, mostly Asia (China 144); Europe 184 (Italy 18, Poland 17, Belgium 17, Germany 14). New, but a registry of federation athletes: it does not reproduce the event map and is not used. WDSF Caribbean: 25 rows, incomplete export, not used.
- **V1 answered.** The author read the sites of the 20 largest Latin congresses: 18 show no sponsor (the author's reading, who also noted that some seem promoted by goandance and that organisers seem to fund themselves, sometimes several schools together). Two list partners: Croatian Summer Salsa Festival (City of Rovinj, Rovinj tourist board, Maistra, Freixenet, Istria county tourist board; on file already) and the Sofia congress (Los Pambos Events, Ouzo Zorbas, White Water, Nektar Natura, Savoy, Arteks, Tuborg Zero; now in data/). Drinks brands found: wine, spirits, water, juice, alcohol-free beer. **No energy drink and no Red Bull.** "No Red Bull presence found" is unchanged; the bar is not taken by an energy brand at the congresses read.

### What is not claimed
Yearly counts stay estimates with ranges; the top 30 is the maximum of what was found, not a census of dancers; Instagram counts are rounded by the platform; nothing from the exports was added to merged_events.csv.

## 17. Round AD: all data merged, one event count, 30 representative events per world (2026-10-28)

**Merge.** The two event exports of round AC (breaking-calendar.com, goandance.com) now enter `data/events/merged_events.csv` (Europe, Nov 2024 - Oct 2027; goandance rows only for events of 3+ days that are not kizomba, zouk, flamenco, classes or retreats). Census in scope: 1,608 events (Latin 1,092, breaking 516), up from 1,541 (1,059 and 482). Details and the old/new table of every number: `analysis/method.md`.

**Events a year.** One window and one method for both worlds: calendar year 2026, Europe, all sources merged and deduplicated: **Latin 406, breaking 238** (before the merge 396 and 205). Breaking: and8.dance 205 + breaking-calendar.com 96 - 62 in both = 239 before the other sources. The count is a minimum for both worlds (listings only). The plan asked for "at least 450" for Latin; the next-12-months count is 482 but breaking has only 75 announced events in that window, so it is not comparable and is not used.

**Typical event (N = 30 per world, as far as readable).** Rule written before reading any count of the new draw (`analysis/method.md`, section 3; `scripts/draw_rep30.py`, seed 20261028): non-flagship events of the merged census, 30 places split by country in proportion to the census (largest remainder), round X events first inside each country, then a seeded shuffle; events with no account are reported, not replaced by zeros. Counts: public Instagram profile pages read in the browser on 2026-10-28 (round X counts of 2026-10-21 are kept); `data/samples/rep30_sample.csv`, rows in `data/samples/event_social.csv` with `sample` = `rep30`.

| | Latin | Breaking |
|---|---|---|
| Events with a follower count | **18** of 30 places | **30** of 30 places |
| Median followers (90% bootstrap interval) | **5,344** (3,604-8,398) | **1,689** (938-3,955) |
| Countries filled | ES 6/8, DE 3/3, IT 3/3, FR 2/3, RO, BG, NL, SE 1/1 each; GB, AT, BE, CH, CZ, GR, HU, PL 0/1-2 | all 14 countries filled |
| Test | P(breaking > Latin) = 0.02; permutation test of the difference of medians p = 0.02; Mann-Whitney p = 0.014 | |

Reading: the typical Latin event is about 3 times as followed as the typical breaking event; direction and size agree with round X (4,461 vs 1,641, p = 0.02). Limits: for Latin, 12 places stay empty because the Instagram account of the candidate events could not be found in the time available (event pages and organiser websites rarely link it; web search found almost none), so the Latin sample is tilted to events with a visible account and to Spain, Germany and Italy; `the movement ARENA` appears twice in breaking with one account (272 followers; two editions of the same event). Follower counts are accounts of the event or of its organiser. Stated n is the real n; no value was invented.

**Flagship points (unchanged).** Summer Dance Forever 283,000; BC One 957,000 (Red Bull's channel); Croatian Summer Salsa Festival 45,000.

**Typical-event numbers elsewhere.** Page 1 card "60 events" (price and line-up sample, 30 Latin and 30 breaking) is unchanged: it is a different reading of the same kind of events.
