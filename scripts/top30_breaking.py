#!/usr/bin/env python3
"""The 30 most followed breaking dancers found (page 2 of the summary: 4.3 million, median 108,000).

Same rule as scripts/robustness.py (dancer_followers): Instagram followers (profile page) of data/facts.csv,
one fact per athlete, athlete id in the notes column, every discipline that is not Caribbean (CAR-*).
Names come from data/athletes.csv. Writes data/dancers/top30_breaking_dancers.csv. Standard library only.
Run:  python scripts/top30_breaking.py
"""
import csv
import os
import re
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IG = "Instagram followers (profile page)"


def rows(path):
    with open(os.path.join(ROOT, path), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main():
    names = {a["athlete_id"]: a for a in rows("data/core/athletes.csv")}
    best = {}
    for f in rows("data/core/facts.csv"):
        if f["unit"] != IG or f["evidence_type"] == "not_found" or f["place_id"] != "GLOBAL" or not f["value"]:
            continue
        if f["disc_id"].startswith("CAR-"):
            continue
        m = re.search(r"athlete(?:_id)? (A\d{5})", f["notes"])
        if m and m.group(1) in names:
            best.setdefault(m.group(1), f)
    top = sorted(best.items(), key=lambda kv: -float(kv[1]["value"]))[:30]
    os.makedirs(os.path.join(ROOT, "data", "dancers"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "dancers", "top30_breaking_dancers.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["rank", "name", "country", "instagram_followers", "fact_id", "athlete_id", "read_on"])
        for i, (aid, fact) in enumerate(top, 1):
            a = names[aid]
            w.writerow([i, a["public_name"], a["country_iso2"], int(float(fact["value"])), fact["fact_id"], aid, fact["period"]])
    values = [float(f["value"]) for _, f in top]
    print(f"top 30: total {sum(values):,.0f}, median {statistics.median(values):,.0f}, 30th = {values[-1]:,.0f}")


if __name__ == "__main__":
    main()
