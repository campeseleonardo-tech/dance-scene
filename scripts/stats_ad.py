#!/usr/bin/env python3
"""Round AD: numbers of the summary from data/events/merged_events.csv (Europe, Nov 2024 - Oct 2027).
Run: python scripts/stats_ad.py     Prints totals, shares per period, 2026 counts; writes analysis/summary_stats_ad.json."""
import csv, json, os
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = {"RU", "BY", "TR"}
rows = [x for x in csv.DictReader(open(os.path.join(ROOT, "data/events/merged_events.csv"), encoding="utf-8"))
        if x["world"] in ("latin", "breaking") and x["country_iso2"] not in OUT and "2024-11-01" <= x["date_start"] <= "2027-10-31"]
res = {"total": len(rows)}
for w in ("latin", "breaking"):
    ws = [x for x in rows if x["world"] == w]
    res[w] = {"total": len(ws), "y2026": sum(1 for x in ws if x["date_start"].startswith("2026"))}
    res[w]["periods"] = {}
    for per in ("past 12-24 months", "past 0-12 months", "next 12 months"):
        sub = [x for x in ws if x["period"] == per]
        c = Counter(x["country_iso2"] for x in sub)
        res[w]["periods"][per] = {"n": len(sub), "top": [(k, v, round(100 * v / len(sub))) for k, v in c.most_common(6)]}
    print(w, res[w]["total"], "2026:", res[w]["y2026"])
    for per, v in res[w]["periods"].items(): print("  ", per, v["n"], v["top"])
print("total", res["total"])
json.dump(res, open(os.path.join(ROOT, "analysis/summary_stats_ad.json"), "w"), indent=1)
