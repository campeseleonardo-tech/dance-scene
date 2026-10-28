#!/usr/bin/env python3
"""The 30 most followed Latin dancers, as used on page 2 of the summary, with the follower count next to each name.

Run:  python scripts/top30_latin.py
Reads data/athletes.csv (names), data/facts.csv (Instagram followers, athlete id in notes), data/artists/artist_reach.csv.
Writes data/dancers/top30_latin_dancers.csv (rank, name, style, country, followers, fact id) and
data/dancers/latin_dancers_not_in_top30.csv (artists read later, in rounds AA1/AB, with at least the 30th follower count).
Standard library only.
"""

import csv
import os
import re
import statistics

# Janis & Zoe (A00099): 1,000,000 followers, handle found by name search, bio does not name the dance style.
# Kept out of the list until Leonardo confirms the account by hand.
HOLD = set()  # nothing held back: Leonardo confirmed Janis & Zoe (A00099, bachata, over 1 million followers) on 2026-10-28
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rows(path):
    with open(os.path.join(ROOT, path), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def followers(text):
    m = re.match(r"^([\d.]+)\s*([KM]?)$", text.strip().replace(",", ""))
    if not m:
        return None
    return round(float(m.group(1)) * {"": 1, "K": 1000, "M": 1000000}[m.group(2)])


def main():
    names = {a["athlete_id"]: a for a in rows("data/core/athletes.csv")}
    best = {}
    for f in rows("data/core/facts.csv"):
        if f["unit"] != "Instagram followers (profile page)" or not f["value"] or not f["disc_id"].startswith("CAR"):
            continue
        m = re.search(r"athlete(?:_id)? (A\d+)", f["notes"])
        if m and m.group(1) not in HOLD:
            best.setdefault(m.group(1), f)
    top = sorted(best.items(), key=lambda kv: -int(kv[1]["value"]))[:30]
    os.makedirs(os.path.join(ROOT, "data", "dancers"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "dancers", "top30_latin_dancers.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank", "name", "style", "country", "instagram_followers", "fact_id", "athlete_id", "read_on"])
        for i, (aid, fact) in enumerate(top, 1):
            a = names[aid]
            style = {"CAR-BCH": "bachata", "CAR-SAL": "salsa"}.get(a["disc_id"], a["disc_id"])
            w.writerow([i, a["public_name"], style, a["country_iso2"], fact["value"], fact["fact_id"], aid, fact["period"]])
    values = [int(f["value"]) for _, f in top]
    cut = values[-1]
    print(f"top 30: total {sum(values):,}, median {statistics.median(values):,.0f}, 30th = {cut:,}")
    have = {re.sub(r"[^a-z]", "", names[aid]["public_name"].lower().replace(" y ", "").replace(" & ", "")) for aid, _ in top}
    extra = []
    for r in rows("data/artists/artist_reach.csv"):
        n = followers(r["instagram_followers"])
        key = re.sub(r"[^a-z]", "", r["artist_norm"].lower().replace(" & ", ""))
        if n and n >= cut and key not in have:
            extra.append((n, r))
    extra.sort(key=lambda x: -x[0])
    with open(os.path.join(ROOT, "data", "dancers", "latin_dancers_not_in_top30.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["artist", "instagram_followers", "bookings_in_sample", "base_country", "reading", "access_date"])
        for n, r in extra:
            w.writerow([r["artist_norm"], n, r["events_in_sample"], r["base_country"], r["notes"], r["access_date"]])
    print(len(extra), "artists read in rounds AA1/AB have at least the 30th count and are not in the top 30")


if __name__ == "__main__":
    main()
