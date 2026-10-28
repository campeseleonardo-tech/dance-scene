#!/usr/bin/env python3
"""How many congresses do a few artists reach? (page 4 of the summary, analysis.md sections 13 and 16)

Run:  python scripts/artist_concentration.py
Reads data/artists/lineups.csv (couples and solo artists; DJs and rows without a name are left out).
Greedy choice: the first artist is the one on most line-ups, each next artist is the one who adds most congresses
not yet reached. Prints the share of congresses with a published line-up reached by 5, 10 and 14 artists and
writes data/artists/artist_concentration.csv. Standard library only.
"""
import csv
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(ROOT, "data", "artists", "lineups.csv"), encoding="utf-8", newline="") as f:
    rows = [r for r in csv.DictReader(f) if r["artist_norm"] and r["kind"] in ("couple", "solo")]
events = defaultdict(set)
for r in rows:
    events[r["artist_norm"]].add(r["event_key"])
n = len({r["event_key"] for r in rows})
reached, out = set(), []
for k in range(1, 15):
    best = max(sorted(events), key=lambda a: (len(events[a] - reached), len(events[a])))
    reached |= events[best]
    out.append((k, best, len(events[best]), len(reached), len(reached) / n))
for k, a, b, c, s in out:
    if k in (5, 10, 14):
        print(f"{k} artists reach {c} of {n} congresses = {s:.0%}")
top = sorted(events, key=lambda a: (-len(events[a]), a))[:8]
print("most booked:", [(a, len(events[a])) for a in top])
with open(os.path.join(ROOT, "data", "artists", "artist_concentration.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["step", "artist_added", "congresses_of_this_artist", "congresses_reached_cumulative", "share_of_congresses_with_lineup", "congresses_with_lineup"])
    for k, a, b, c, s in out:
        w.writerow([k, a, b, c, f"{s:.3f}", n])
