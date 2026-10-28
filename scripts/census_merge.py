#!/usr/bin/env python3
"""Merge the event lists of round Y, find the same event across sources, estimate the true number of events.

Run:  python scripts/census_merge.py
Reads every data/events/by_source/*.csv except merged_events.csv. Each list has the columns
source, world, name, city, country_iso2, date_start, date_end, price_eur, listing_url, notes
(world = latin | breaking | hyrox; date_start ISO; price_eur optional). One file per source and world,
for example data/events/by_source/latin_goandance.csv.

Writes data/events/merged_events.csv (one row per distinct event, with the sources that list it)
and prints, per world: events per source, overlaps, the Chapman capture-recapture estimate of the total
for each pair of sources, events per country and per period. Standard library only.
"""

import csv
import glob
import itertools
import os
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CENSUS = os.path.join(ROOT, "data", "events", "by_source")
OUT = os.path.join(ROOT, "data", "events", "merged_events.csv")
TODAY = date(2026, 10, 21)
STOP = {"the", "festival", "fest", "congress", "congreso", "congresso", "kongress", "international", "int",
        "edition", "ed", "weekend", "weekender", "event", "salsa", "bachata", "breaking", "battle", "jam",
        "dance", "danza", "baile", "tanz", "de", "di", "la", "le", "el", "and", "y", "e", "et", "und", "vol",
        "hyrox", "world", "championship", "championships", "open", "cup"}
MAX_DAYS = 3        # same event if the start dates differ by at most this
MIN_JACCARD = 0.5   # and the names share at least this share of distinctive words


def norm_tokens(name):
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    words = re.findall(r"[a-z]+", text)
    return {w for w in words if w not in STOP and len(w) > 1}


def parse_date(s):
    try:
        y, m, d = (int(x) for x in s[:10].split("-"))
        return date(y, m, d)
    except (ValueError, AttributeError):
        return None


def period(d):
    if d is None:
        return "unknown"
    if d > TODAY:
        return "next 12 months"
    if (TODAY - d).days <= 365:
        return "past 0-12 months"
    if (TODAY - d).days <= 730:
        return "past 12-24 months"
    return "older"


def same_event(a, b):
    if a["world"] != b["world"] or a["country_iso2"] != b["country_iso2"]:
        return False
    if a["_d"] and b["_d"] and abs((a["_d"] - b["_d"]).days) > MAX_DAYS:
        return False
    same_city = a["city"].strip().lower() == b["city"].strip().lower() and a["city"].strip() != ""
    if same_city and a["_d"] and a["_d"] == b["_d"]:
        return True  # same city, same start day, same world: one event under two names
    ta, tb = a["_t"], b["_t"]
    if not ta or not tb:
        return False
    return len(ta & tb) / len(ta | tb) >= MIN_JACCARD


EXPORTS = os.path.join(CENSUS, "exports")
EXPORT_MAX_DAYS = 1   # round AD: same rule as scripts/match_exports.py (dates within 1 day, same country, half of the words)
NOT_LATIN_SCOPE = re.compile(r"kizomba|zouk|flamenco|retreat|workshop(?:s)? only|class(?:es)?|course|tango|swing|lindy|urban kiz", re.I)


def export_event(a, b):
    """Round AD matching rule for export rows against census rows."""
    if a["world"] != b["world"] or a["country_iso2"] != b["country_iso2"] or not a["_d"] or not b["_d"]:
        return False
    if abs((a["_d"] - b["_d"]).days) > EXPORT_MAX_DAYS:
        return False
    ta, tb = a["_t"], b["_t"]
    if not ta or not tb:
        return False
    return len(ta & tb) / len(ta | tb) >= MIN_JACCARD or (min(len(ta), len(tb)) >= 2 and len(ta & tb) >= min(len(ta), len(tb)))


def load_exports():
    """Europe rows of the two event exports of round AC (breaking-calendar.com, goandance.com).
    probreakingtour (US only) and the WDSF lists are not events of Europe and stay out.
    goandance rows enter only when they last 3 days or more and are not kizomba, zouk, flamenco, classes or retreats
    (the same congress/festival scope as the Latin census)."""
    rows, skipped = [], Counter()
    for fname in ("breaking_calendar_com.csv", "latin_goandance_export.csv"):
        with open(os.path.join(EXPORTS, fname), encoding="utf-8", newline="") as handle:
            for r in csv.DictReader(handle):
                if r.get("region") != "Europe" or r.get("country_iso2", "").strip().upper() in {"RU", "BY", "TR"}:
                    skipped[(fname, "outside Europe")] += 1
                    continue
                r["_d"] = parse_date(r.get("date_start", ""))
                if r["_d"] is None or not date(2024, 11, 1) <= r["_d"] <= date(2027, 10, 31):
                    skipped[(fname, "outside the Nov 2024 - Oct 2027 window")] += 1
                    continue
                if r["world"] == "latin":
                    end = parse_date(r.get("date_end", ""))
                    if end is None or (end - r["_d"]).days < 2:
                        skipped[(fname, "less than 3 days")] += 1
                        continue
                    if NOT_LATIN_SCOPE.search(r["name"]):
                        skipped[(fname, "kizomba, zouk, flamenco, classes or retreat")] += 1
                        continue
                r["_t"] = norm_tokens(r.get("name", ""))
                r["country_iso2"] = r["country_iso2"].strip().upper()
                rows.append(r)
    return rows, skipped


def chapman(n1, n2, m):
    return (n1 + 1) * (n2 + 1) / (m + 1) - 1


def main():
    rows = []
    for path in sorted(glob.glob(os.path.join(CENSUS, "*.csv"))):
        if os.path.basename(path).startswith("merged_events"):
            continue
        with open(path, encoding="utf-8") as handle:
            for r in csv.DictReader(handle):
                r["_d"] = parse_date(r.get("date_start", ""))
                r["_t"] = norm_tokens(r.get("name", ""))
                r["world"] = r.get("world", "").strip().lower()
                r["country_iso2"] = r.get("country_iso2", "").strip().upper()
                rows.append(r)
    if not rows:
        print("No lists in data/events/by_source/ yet.")
        return 0

    clusters = []  # each: list of rows
    for r in rows:
        for c in clusters:
            # two rows of the same source are two listed editions, never one event
            if all(x["source"] != r["source"] for x in c) and any(same_event(r, x) for x in c):
                c.append(r)
                break
        else:
            clusters.append([r])

    # round AD: export rows join the cluster they match; the others are new events
    added = Counter()
    exp_rows, skipped = load_exports()
    for r in exp_rows:
        for c in clusters:
            if any(export_event(r, x) for x in c):
                if all(x["source"] != r["source"] for x in c):
                    c.append(r)
                    added[(r["source"], "joined an existing event")] += 1
                else:
                    added[(r["source"], "already in the census (same source)")] += 1
                break
        else:
            clusters.append([r])
            added[(r["source"], "new event")] += 1
    for k, v in sorted(added.items()):
        print("export", k, v)
    for k, v in sorted(skipped.items()):
        print("export skipped", k, v)

    with open(OUT, "w", encoding="utf-8", newline="") as handle:
        w = csv.writer(handle, lineterminator="\n")
        w.writerow(["event_key", "world", "name", "city", "country_iso2", "date_start", "period", "sources", "n_sources", "price_eur"])
        for i, c in enumerate(clusters, 1):
            first = c[0]
            prices = [x.get("price_eur", "") for x in c if x.get("price_eur", "")]
            w.writerow([f"K{i:05d}", first["world"], first["name"], first["city"], first["country_iso2"],
                        first.get("date_start", ""), period(first["_d"]), ";".join(sorted({x["source"] for x in c})),
                        len({x["source"] for x in c}), prices[0] if prices else ""])
    print(f"Wrote {OUT}: {len(rows)} listings, {len(clusters)} distinct events")

    by_world = defaultdict(list)
    for c in clusters:
        by_world[c[0]["world"]].append(c)
    for world, cs in sorted(by_world.items()):
        print(f"\n## {world}: {len(cs)} distinct events")
        sources = Counter(s for c in cs for s in {x['source'] for x in c})
        for s, n in sources.most_common():
            print(f"- {s}: {n} events")
        for label, sub in (("all periods", cs), ("next 12 months only (both lists show upcoming events)", [c for c in cs if period(c[0]["_d"]) == "next 12 months"])):
          print(f"Pairwise overlap and Chapman estimate of the total, {label} (assumes the two lists are independent):")
          for a, b in itertools.combinations(sorted(sources), 2):
            sets = [{x["source"] for x in c} for c in sub]
            n1 = sum(1 for s in sets if a in s)
            n2 = sum(1 for s in sets if b in s)
            m = sum(1 for s in sets if a in s and b in s)
            est = chapman(n1, n2, m)
            print(f"  {a} ({n1}) x {b} ({n2}): {m} in both -> about {est:,.0f} events in total; "
                  f"{a} covers about {n1 / est:.0%}, {b} about {n2 / est:.0%}" if est > 0 else f"  {a} x {b}: no estimate")
        print("By period:", dict(Counter(period(c[0]["_d"]) for c in cs)))
        print("Top countries:", Counter(c[0]["country_iso2"] for c in cs).most_common(12))
        print("Top cities:", Counter((c[0]["city"], c[0]["country_iso2"]) for c in cs).most_common(12))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
