#!/usr/bin/env python3
"""Rank 24 European cities for (a) Red Bull's first Latin activation and (b) a new Latin congress.

Run:  python scripts/city_ranking.py
Reads data/cities/city_list.csv, data/cities/city_indicators.csv (round AA2 + fixes of round AB),
data/events/merged_events.csv, data/sizes/large_events.csv and data/prices/latin_events_detail.csv.
Writes data/cities/city_ranking.csv and analysis/city_ranking.md.
Method: every indicator becomes a percentile rank (0-1) across the cities (missing = median, flagged);
a view is the mean of its blocks, a block the mean of its indicators (negative indicators are reversed).
Robustness: 2,000 random block weights (Dirichlet, all parameters 1, seed 20261021) and leave-one-indicator-out.
Standard library only.
"""

import csv
import math
import os
import random
import statistics
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CITIES = os.path.join(ROOT, "data", "cities")
SEED = 20261021
DRAWS = 2000

ALIAS = {"wien": "vienna", "munchen": "munich", "milano": "milan", "roma": "rome", "warszawa": "warsaw",
         "praha": "prague", "bruxelles": "brussels", "koln": "cologne", "zuerich": "zurich", "athina": "athens",
         "bucuresti": "bucharest", "malaga": "malaga"}

# coordinates of the cities of the large Latin events (data/sizes/large_events.csv)
LARGE_COORDS = {"Rovinj": (45.08, 13.64), "Berlin": (52.52, 13.40), "Amsterdam": (52.37, 4.90), "Sofia": (42.70, 23.32),
                "Girona": (41.98, 2.82), "Paris": (48.86, 2.35), "Luxembourg": (49.61, 6.13), "Cluj-Napoca": (46.77, 23.60),
                "Bucharest": (44.43, 26.10), "Lloret de Mar": (41.70, 2.85), "Norway": (59.91, 10.75), "Malmo": (55.60, 13.00)}

LABELS = {
    "latin_events": "Latin events in the city, 3 years (census)",
    "large_150km": "Latin events with 1,000+ dancers within 150 km",
    "hyrox": "Hyrox races in the city, 3 years (census)",
    "country_crowding": "Latin events in the country, next 12 months (census)",
    "C1_population": "Population",
    "C2_young_adults_share": "Share aged 20-39 (%)",
    "C3_air_passengers": "Air passengers a year",
    "C5_tourism_nights": "Tourism nights a year (region)",
    "C7_dance_venues_osm": "Dance schools and venues (OpenStreetMap)",
    "C8_cost_level": "Price level (country, EU = 100)",
    "C9_rb_dance_events": "Red Bull dance events 2024-2026",
    "C10_rb_office": "Red Bull office in the metro",
}

VIEWS = {
    "Red Bull entry": {
        "Latin scene": [("latin_events", 1), ("large_150km", 1), ("C7_dance_venues_osm", 1)],
        "Red Bull on the ground": [("C9_rb_dance_events", 1), ("C10_rb_office", 1), ("hyrox", 1)],
        "Reach": [("C1_population", 1), ("C2_young_adults_share", 1), ("C3_air_passengers", 1)],
    },
    "New congress": {
        "Demand": [("latin_events", 1), ("C7_dance_venues_osm", 1), ("C1_population", 1), ("C2_young_adults_share", 1)],
        "Access": [("C3_air_passengers", 1), ("C5_tourism_nights", 1)],
        "Room in the market": [("large_150km", -1), ("country_crowding", -1)],
        "Cost": [("C8_cost_level", -1)],
    },
}


def norm(s):
    k = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower().strip()
    return ALIAS.get(k, k)


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def load():
    cities = list(csv.DictReader(open(os.path.join(CITIES, "city_list.csv"), encoding="utf-8")))
    vals = {c["city"]: {} for c in cities}
    src = {}
    for r in csv.DictReader(open(os.path.join(CITIES, "city_indicators.csv"), encoding="utf-8")):
        if not r["value"] or r["city"] not in vals:
            continue
        ind = r["indicator"]
        if ind in vals[r["city"]] and "use this one" not in r["notes"]:
            continue
        vals[r["city"]][ind] = float(r["value"])
        src.setdefault(ind, r["source_name"])
    census = [r for r in csv.DictReader(open(os.path.join(ROOT, "data", "events", "merged_events.csv"), encoding="utf-8"))
              if r["country_iso2"] not in ("TR", "RU", "BY")]
    large = [r for r in csv.DictReader(open(os.path.join(ROOT, "data", "sizes", "large_events.csv"), encoding="utf-8"))
             if r["world"] == "latin" and r["in_comparison"] == "yes"]
    for c in cities:
        name, iso = c["city"], c["country_iso2"]
        v = vals[name]
        v["latin_events"] = sum(1 for r in census if r["world"] == "latin" and norm(r["city"]) == norm(name))
        v["hyrox"] = sum(1 for r in census if r["world"] == "hyrox" and norm(r["city"]) == norm(name))
        v["country_crowding"] = sum(1 for r in census if r["world"] == "latin" and r["period"] == "next 12 months"
                                    and r["country_iso2"] == iso)
        here = (float(c["lat"]), float(c["lon"]))
        v["large_150km"] = sum(1 for r in large if km(here, LARGE_COORDS[r["city"]]) <= 150)
    return cities, vals, src


def percentile(vals, key, names):
    present = {n: vals[n][key] for n in names if key in vals[n]}
    ordered = sorted(present.values())
    out, missing = {}, []
    for n in names:
        if n in present:
            below = sum(1 for x in ordered if x < present[n])
            equal = sum(1 for x in ordered if x == present[n])
            out[n] = (below + (equal - 1) / 2) / (len(ordered) - 1) if len(ordered) > 1 else 0.5
        else:
            out[n] = 0.5
            missing.append(n)
    return out, missing


def scores(view, pct, weights=None, drop=None):
    blocks = VIEWS[view]
    names = list(next(iter(pct.values())).keys())
    w = weights or [1 / len(blocks)] * len(blocks)
    out = {}
    for n in names:
        total = 0
        for (bname, inds), wb in zip(blocks.items(), w):
            parts = [(pct[k][n] if sign > 0 else 1 - pct[k][n]) for k, sign in inds if k != drop]
            total += wb * (statistics.mean(parts) if parts else 0.5)
        out[n] = total
    return out


def ranks(sc):
    order = sorted(sc, key=lambda n: -sc[n])
    return {n: i + 1 for i, n in enumerate(order)}


def main():
    cities, vals, src = load()
    names = [c["city"] for c in cities]
    keys = sorted({k for v in VIEWS.values() for inds in v.values() for k, _ in inds})
    pct, missing = {}, {}
    for k in keys:
        pct[k], missing[k] = percentile(vals, k, names)
    rng = random.Random(SEED)
    results = {}
    for view, blocks in VIEWS.items():
        base = scores(view, pct)
        base_rank = ranks(base)
        top3 = {n: 0 for n in names}
        top5 = {n: 0 for n in names}
        allr = {n: [] for n in names}
        for _ in range(DRAWS):
            g = [rng.gammavariate(1, 1) for _ in blocks]
            w = [x / sum(g) for x in g]
            r = ranks(scores(view, pct, w))
            for n in names:
                allr[n].append(r[n])
                top3[n] += r[n] <= 3
                top5[n] += r[n] <= 5
        loo = {n: [] for n in names}
        for k in {k for inds in blocks.values() for k, _ in inds}:
            r = ranks(scores(view, pct, drop=k))
            for n in names:
                loo[n].append(r[n])
        results[view] = {n: (base[n], base_rank[n], statistics.median(allr[n]), top3[n] / DRAWS, top5[n] / DRAWS,
                             min(loo[n]), max(loo[n])) for n in names}

    with open(os.path.join(CITIES, "city_ranking.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["view", "city", "score", "rank", "median_rank_random_weights", "p_top3", "p_top5", "best_rank_leave_one_out", "worst_rank_leave_one_out"])
        for view, res in results.items():
            for n, (s, r, mr, p3, p5, lo, hi) in sorted(res.items(), key=lambda x: x[1][1]):
                w.writerow([view, n, round(s, 3), r, mr, round(p3, 3), round(p5, 3), lo, hi])

    lines = ["# City ranking: where to start a Latin activation, and where to start a new congress", "",
             "Generated by `python scripts/city_ranking.py` (do not edit by hand). 24 cities: the 15 project cities and every city with 8+ Latin events in the census.",
             "", "## Method", "",
             "Each indicator is turned into a percentile rank between 0 and 1 across the 24 cities (a missing value counts as the median and is flagged below). "
             "A block is the mean of its indicators; a view is the mean of its blocks (equal weights). Indicators marked (-) count against a city.",
             ""]
    for view, blocks in VIEWS.items():
        lines.append(f"- **{view}:** " + "; ".join(f"{b} = " + ", ".join(LABELS[k] + (" (-)" if s < 0 else "") for k, s in inds) for b, inds in blocks.items()))
    lines += ["", f"Robustness: {DRAWS} random sets of block weights (each block can weigh from almost 0 to almost all) give each city a median rank and the share of draws in which it is in the top 3 and top 5; "
              "leave-one-out removes one indicator at a time and shows the best and worst rank the city reaches.", ""]
    for view, res in results.items():
        lines += [f"## {view}", "", "| Rank | City | Score | Median rank, random weights | In top 3 | In top 5 | Rank range, one indicator removed |", "|---|---|---|---|---|---|---|"]
        for n, (s, r, mr, p3, p5, lo, hi) in sorted(res.items(), key=lambda x: x[1][1]):
            lines.append(f"| {r} | {n} | {s:.2f} | {mr:g} | {p3:.0%} | {p5:.0%} | {lo}-{hi} |")
        lines.append("")
    lines += ["## Indicator values", "", "| City | " + " | ".join(LABELS[k] for k in keys) + " |", "|---|" + "---|" * len(keys)]
    for n in names:
        cells = []
        for k in keys:
            v = vals[n].get(k)
            cells.append("missing" if v is None else (f"{v:,.0f}" if v >= 100 else f"{v:g}"))
        lines.append(f"| {n} | " + " | ".join(cells) + " |")
    lines += ["", "Sources: census lists (data/events/by_source/), data/sizes/large_events.csv, data/cities/city_indicators.csv; source per indicator: "
              + "; ".join(f"{LABELS[k]}: {src[k]}" for k in keys if k in src) + ".",
              "Missing values (counted as the median): " + ("; ".join(f"{LABELS[k]}: {', '.join(m)}" for k, m in missing.items() if m) or "none") + ".",
              "Limits: price level is a country value; tourism nights are for the NUTS 3 region (London: UK sources, wider definition); OpenStreetMap counts all dance schools, not only Latin, and depends on how well each city is mapped; "
              "Latin events count only listings that name the city."]
    with open(os.path.join(ROOT, "analysis", "city_ranking.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    for view, res in results.items():
        top = sorted(res.items(), key=lambda x: x[1][1])[:6]
        print(view + ": " + ", ".join(f"{n} ({r}; top3 {p3:.0%})" for n, (s, r, mr, p3, p5, lo, hi) in top))


if __name__ == "__main__":
    main()
