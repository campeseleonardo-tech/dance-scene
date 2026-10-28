#!/usr/bin/env python3
"""Round AD: build the representative samples from data/samples/rep30_draw.csv (order) and rep30_reads.csv (readings).

Run:  python scripts/rep30_sample.py
Walks each country's candidates in draw order until its quota is filled with events that have a follower count.
Round X events use the counts of 2026-10-21 (analysis/method.md). A candidate that is in the draw list but
has no row in rep30_reads.csv and lies inside the first ten candidates of its country was checked on its listing
page only (no Instagram link): it counts as account_not_found. Candidates beyond that were not examined: the walk
stops there and the country stays short. Writes data/samples/rep30_sample.csv and prints medians and n.
"""
import csv, json, os, statistics
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
draw = list(csv.DictReader(open(os.path.join(ROOT, "data/samples/rep30_draw.csv"), encoding="utf-8")))
reads = {r["event_key"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data/samples/rep30_reads.csv"), encoding="utf-8"))}
rows, short = [], {}
for world in ("latin", "breaking"):
    for c in dict.fromkeys(x["country"] for x in draw if x["world"] == world):
        sub = [x for x in draw if x["world"] == world and x["country"] == c]
        q, have = int(sub[0]["quota"]), 0
        nonx = [x for x in sub if not x["from_round_x"]]
        for x in sub:
            if have >= q:
                break
            if x["from_round_x"]:
                st = "read" if x["x_followers"] != "" else "account_not_found"
                val, src = x["x_followers"], "round X, read 2026-10-21"
            else:
                rd = reads.get(x["event_key"])
                if rd is None:
                    if nonx.index(x) < 10:
                        st, val, src = "account_not_found", "", "listing page shows no Instagram link; not searched further"
                    else:
                        short[(world, c)] = q - have
                        break
                else:
                    st, val, src = rd["status"], rd["followers"], "read 2026-10-28 " + (rd["handle"] and "@" + rd["handle"])
            rows.append({"world": world, "country": c, "event_key": x["event_key"], "name": x["name"], "date_start": x["date_start"],
                         "status": st, "followers": val, "source": src})
            if st == "read":
                have += 1
        else:
            pass
        if have < q:
            short.setdefault((world, c), q - have)
with open(os.path.join(ROOT, "data/samples/rep30_sample.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
    w.writeheader(); w.writerows(rows)
res = {}
for world in ("latin", "breaking"):
    sub = [r for r in rows if r["world"] == world]
    vals = [int(r["followers"]) for r in sub if r["status"] == "read"]
    nf = sum(1 for r in sub if r["status"] != "read" and r["status"] != "duplicate_account")
    res[world] = {"n": len(vals), "median": statistics.median(vals), "values": sorted(vals), "events_examined": len(sub), "without_account_found": nf,
                  "countries": dict(Counter(r["country"] for r in sub if r["status"] == "read"))}
    print(world, "n =", len(vals), "median", statistics.median(vals), "not found", nf, "of", len(sub), "examined; short:", {k[1]: v for k, v in short.items() if k[0] == world})
json.dump(res, open(os.path.join(ROOT, "analysis/summary_rep30.json"), "w"), indent=1)
