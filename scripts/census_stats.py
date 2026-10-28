#!/usr/bin/env python3
"""Tables of the round Y census for analysis/analysis.md section 11.

Run:  python scripts/census_merge.py   (first: writes data/events/merged_events.csv)
      python scripts/census_stats.py
Reads data/events/by_source/*.csv only. Standard library only.
"""

import csv
import glob
import os
import statistics
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CENSUS = os.path.join(ROOT, "data", "events", "by_source")
TODAY = "2026-10-21"
YEAR_AGO = "2025-10-21"
TWO_YEARS_AGO = "2024-10-21"
OUT_OF_SCOPE = {"TR", "RU", "BY"}  # listed by some sources, outside the scope of the census


def period(d):
    if not d:
        return "unknown"
    if d > TODAY:
        return "next 12 months"
    if d > YEAR_AGO:
        return "past 0-12 months"
    if d > TWO_YEARS_AGO:
        return "past 12-24 months"
    return "older"


def load(path):
    with open(path, encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main():
    merged = [r for r in load(os.path.join(ROOT, "data", "events", "merged_events.csv")) if r["country_iso2"] not in OUT_OF_SCOPE]
    print("Countries outside scope removed:", ", ".join(sorted(OUT_OF_SCOPE)))
    print("## Distinct events per world and period (all sources merged)")
    print("| World | Past 12-24 months | Past 0-12 months | Next 12 months | Total |")
    print("|---|---|---|---|---|")
    for w in ("latin", "breaking", "hyrox"):
        c = Counter(r["period"] for r in merged if r["world"] == w)
        print(f"| {w} | {c['past 12-24 months']} | {c['past 0-12 months']} | {c['next 12 months']} | {sum(c.values())} |")

    print("\n## Same source over time (trend without mixing sources)")
    print("| Source | Past 12-24 months | Past 0-12 months | Change | Next 12 months |")
    print("|---|---|---|---|---|")
    for name in ("latin_latindancecalendar", "breaking_and8", "hyrox_official"):
        path = os.path.join(CENSUS, name + ".csv")
        if not os.path.exists(path):
            continue
        c = Counter(period(r["date_start"][:10]) for r in load(path) if r["country_iso2"].strip().upper() not in OUT_OF_SCOPE)
        a, b = c["past 12-24 months"], c["past 0-12 months"]
        change = f"{(b - a) / a:+.0%}" if a else "n/a"
        print(f"| {name} | {a} | {b} | {change} | {c['next 12 months']} |")

    print("\n## Next 12 months, top countries (merged)")
    for w in ("latin", "breaking", "hyrox"):
        c = Counter(r["country_iso2"] for r in merged if r["world"] == w and r["period"] == "next 12 months")
        total = sum(c.values())
        top = ", ".join(f"{k} {v} ({v / total:.0%})" for k, v in c.most_common(6))
        print(f"- {w} ({total}): {top}")

    print("\n## Cities named in the lists, all periods (many rows have no city)")
    for w in ("latin", "hyrox"):
        c = Counter(r["city"] for r in merged if r["world"] == w and r["city"])
        print(f"- {w}: " + ", ".join(f"{k} {v}" for k, v in c.most_common(10)))

    print("\n## Prices shown in the lists")
    for path in sorted(glob.glob(os.path.join(CENSUS, "*.csv"))):
        if path.endswith("merged_events.csv"):
            continue
        p = []
        for r in load(path):
            try:
                p.append(float(r["price_eur"]))
            except (KeyError, ValueError):
                pass
        if p:
            print(f"- {os.path.basename(path)}: n = {len(p)}, median EUR {statistics.median(p):.0f}, range {min(p):.0f}-{max(p):.0f}")


if __name__ == "__main__":
    main()
