#!/usr/bin/env python3
"""Draw a reproducible random sample of events from a sampling frame (round X, plan B).

Run:  python scripts/draw_sample.py data/samples/latin_frame.csv 30
      python scripts/draw_sample.py data/samples/breaking_frame.csv 30
The frame is a CSV with at least the columns frame_id, world, name, city, country_iso2, date_start,
listing_url. Rows with `exclude` set to anything non-empty are left out (write the reason there).
Writes <frame>_sample.csv next to the frame (same columns plus draw_order) and prints it.
The seed is fixed, so the same frame always gives the same sample. Standard library only.
"""

import csv
import random
import sys

SEED = 20261021


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 1
    path, n = argv[1], int(argv[2])
    with open(path, encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    eligible = [r for r in rows if not (r.get("exclude") or "").strip()]
    eligible.sort(key=lambda r: r["frame_id"])
    rng = random.Random(SEED)
    sample = eligible if n >= len(eligible) else rng.sample(eligible, n)
    out = path.replace(".csv", "_sample.csv")
    fields = list(rows[0].keys()) + ["draw_order"]
    with open(out, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for i, r in enumerate(sample, 1):
            writer.writerow({**r, "draw_order": i})
    print(f"Frame {path}: {len(rows)} rows, {len(eligible)} eligible; sample of {len(sample)} written to {out}")
    for i, r in enumerate(sample, 1):
        print(f"{i:>2} {r['frame_id']} {r['name']} ({r['city']}, {r['country_iso2']}, {r['date_start']})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
