#!/usr/bin/env python3
"""Check the CSV tables against the data contract (data/schema.md, section 4).

Run:  python scripts/validate_data.py [folder]
Without a folder it checks data/ when that folder holds CSV files, otherwise archive/viewer/sample_data/ (the old test data).
Exit code 0 only when there are no errors. Warnings do not stop the build.
Standard library only.
"""

import csv
import datetime
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA_DIR = os.path.join(ROOT, "data", "core")
SAMPLE_DIR = os.path.join(ROOT, "archive", "viewer", "sample_data")

EVIDENCE = ["found", "stated_by_organiser", "not_found", "inferred"]
CONFIDENCE = ["H", "M", "L"]
ACCESS_STATUS = ["opened", "rendered", "blocked", "not_opened"]
PLACE_TYPE = ["city", "country", "global"]
PLACE_ROLE = ["deep", "scan", "benchmark", "country", "global"]
REGION = ["europe", "north_america", "latin_america", "asia", "africa", "oceania"]
DISC_SCOPE = ["pilot_main", "pilot_light", "adjacent", "out"]
SOURCE_TYPE = ["official_redbull", "organiser", "federation", "public_statistics", "press",
               "wikipedia", "platform", "registry", "academic", "other"]
EVENT_LEVEL = ["class_series", "social_jam", "local_battle", "national", "international",
               "world_final", "congress_festival", "qualifier", "other"]
RED_BULL = ["found", "not_found", "not_checked", "stated_by_organiser", "confirmed_absent"]
SCALE_TYPE = ["attendees", "participants", "seats", "countries", "none"]
ORG_TYPE = ["federation", "school", "studio_space", "crew_collective", "event_organiser",
            "brand_sponsor", "media", "venue", "public_funder", "other"]
ORG_SCOPE = ["local", "national", "international"]
RB_ATHLETE = ["found", "not_found", "not_checked"]
FIN_SCOPE = ["group", "region", "business_unit", "legal_entity", "dance_related"]
REL_TYPE = ["place", "discipline", "org", "event", "athlete", "series"]
RELATION = ["organises", "sponsors", "governs", "member_of", "qualifies_for", "hosts",
            "teaches", "part_of", "partner_of"]

# Each table: columns in order, required columns, id column, allowed values,
# date and number columns, and the column that holds the source_id.
TABLES = {
    "places.csv": {
        "columns": ["place_id", "place_type", "name", "country_iso2", "region", "role",
                    "metro_definition", "lat", "lon", "inclusion_reason", "notes"],
        "required": ["place_id", "place_type", "name", "role"],
        "id": "place_id",
        "enums": {"place_type": PLACE_TYPE, "role": PLACE_ROLE, "region": REGION},
        "numbers": ["lat", "lon"],
    },
    "disciplines.csv": {
        "columns": ["disc_id", "family", "discipline", "sub_style", "scope", "notes"],
        "required": ["disc_id", "family", "discipline"],
        "id": "disc_id",
        "enums": {"scope": DISC_SCOPE},
    },
    "signals.csv": {
        "columns": ["signal_id", "signal", "definition", "unit", "notes"],
        "required": ["signal_id", "signal"],
        "id": "signal_id",
    },
    "sources.csv": {
        "columns": ["source_id", "url", "title", "publisher", "source_type", "access_date",
                    "access_status", "notes"],
        "required": ["source_id", "url", "title", "source_type", "access_status"],
        "id": "source_id",
        "enums": {"source_type": SOURCE_TYPE, "access_status": ACCESS_STATUS},
        "dates": ["access_date"],
    },
    "facts.csv": {
        "columns": ["fact_id", "place_id", "place_type", "disc_id", "signal_id", "value",
                    "value_low", "value_high", "unit", "period", "evidence_type", "confidence",
                    "source_id", "task_id", "notes"],
        "required": ["fact_id", "place_id", "place_type", "disc_id", "signal_id",
                     "evidence_type", "confidence", "task_id"],
        "id": "fact_id",
        "enums": {"place_type": PLACE_TYPE, "evidence_type": EVIDENCE, "confidence": CONFIDENCE},
        "dates": ["period"],
        "numbers": ["value_low", "value_high"],
        "source_col": "source_id",
    },
    "events.csv": {
        "columns": ["event_id", "name", "series", "level", "place_id", "venue", "date_start",
                    "date_end", "disc_id", "organiser_org_id", "red_bull_involvement",
                    "scale_value", "scale_type", "scale_evidence", "source_id", "confidence",
                    "task_id", "notes"],
        "required": ["event_id", "name", "series", "level", "place_id", "date_start",
                     "red_bull_involvement", "confidence", "task_id"],
        "id": "event_id",
        "enums": {"level": EVENT_LEVEL, "red_bull_involvement": RED_BULL,
                  "scale_type": SCALE_TYPE, "scale_evidence": EVIDENCE,
                  "confidence": CONFIDENCE},
        "dates": ["date_start", "date_end"],
        "numbers": ["scale_value"],
        "source_col": "source_id",
    },
    "organisations.csv": {
        "columns": ["org_id", "name", "org_type", "place_id", "disc_id", "scope",
                    "website_source_id", "evidence_type", "confidence", "task_id", "notes"],
        "required": ["org_id", "name", "org_type", "place_id", "evidence_type", "confidence",
                     "task_id"],
        "id": "org_id",
        "enums": {"org_type": ORG_TYPE, "scope": ORG_SCOPE, "evidence_type": EVIDENCE,
                  "confidence": CONFIDENCE},
        "source_col": "website_source_id",
    },
    "athletes.csv": {
        "columns": ["athlete_id", "public_name", "disc_id", "base_place_id", "country_iso2",
                    "level", "red_bull_athlete", "source_id", "confidence", "task_id", "notes"],
        "required": ["athlete_id", "public_name", "disc_id", "red_bull_athlete", "confidence",
                     "task_id"],
        "id": "athlete_id",
        "enums": {"red_bull_athlete": RB_ATHLETE, "confidence": CONFIDENCE},
        "source_col": "source_id",
    },
    "redbull_finance.csv": {
        "columns": ["finance_id", "entity", "jurisdiction", "financial_year", "scope", "metric",
                    "value", "currency", "unit", "evidence_type", "confidence", "source_id",
                    "task_id", "notes"],
        "required": ["finance_id", "entity", "financial_year", "scope", "metric",
                     "evidence_type", "confidence", "task_id"],
        "id": "finance_id",
        "enums": {"scope": FIN_SCOPE, "evidence_type": EVIDENCE, "confidence": CONFIDENCE},
        "dates": ["financial_year"],
        "numbers": ["value"],
        "source_col": "source_id",
    },
    "relations.csv": {
        "columns": ["rel_id", "from_type", "from_id", "relation", "to_type", "to_id",
                    "evidence_type", "confidence", "source_id", "task_id", "notes"],
        "required": ["rel_id", "from_type", "from_id", "relation", "to_type", "to_id",
                     "evidence_type", "confidence", "task_id"],
        "id": "rel_id",
        "enums": {"from_type": REL_TYPE, "to_type": REL_TYPE, "relation": RELATION,
                  "evidence_type": EVIDENCE, "confidence": CONFIDENCE},
        "source_col": "source_id",
    },
    "review_log.csv": {
        "columns": ["log_id", "date", "item", "issue", "action", "task_id", "notes"],
        "required": ["log_id", "date", "item", "issue", "action", "task_id"],
        "id": "log_id",
        "dates": ["date"],
    },
}

ID_PATTERNS = {
    ("facts.csv", "fact_id"): (r"F\d{6}", "F + 6 digits, for example F000001"),
    ("sources.csv", "source_id"): (r"S\d{5}", "S + 5 digits, for example S00001"),
}

DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
NUMBER_RE = re.compile(r"^-?\d+(\.\d+)?$")


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, message):
        self.errors.append(f"ERROR   {where}: {message}")

    def warn(self, where, message):
        self.warnings.append(f"WARNING {where}: {message}")


def where(name, row, column=""):
    """Plain location text: file, row number, id (if any), column."""
    text = f"{name}, row {row['_row']}"
    ident = row.get(TABLES[name].get("id", ""), "")
    if ident:
        text += f" ({ident})"
    if column:
        text += f", column {column}"
    return text


def valid_date(text):
    if not DATE_RE.match(text):
        return False
    parts = text.split("-")
    try:
        datetime.date(int(parts[0]), int(parts[1]) if len(parts) > 1 else 1,
                     int(parts[2]) if len(parts) > 2 else 1)
    except ValueError:
        return False
    return True


def data_has_rows():
    """True when data/ holds at least one CSV with a data row (a header-only file does not count)."""
    if not os.path.isdir(DATA_DIR):
        return False
    for file_name in os.listdir(DATA_DIR):
        if not file_name.lower().endswith(".csv"):
            continue
        with open(os.path.join(DATA_DIR, file_name), encoding="utf-8-sig", errors="replace") as handle:
            if sum(1 for line in handle if line.strip()) > 1:
                return True
    return False


def pick_folder(folder=None):
    """Return (folder, is_sample). The sample is used until data/ has at least one data row."""
    if folder:
        folder = os.path.abspath(folder)
    elif data_has_rows():
        folder = DATA_DIR
    else:
        folder = SAMPLE_DIR
    return folder, os.path.abspath(folder) != os.path.abspath(DATA_DIR)


def read_table(name, path, report):
    """Return the data rows as dicts (with '_row'), or [] when the table cannot be used."""
    try:
        with open(path, newline="", encoding="utf-8-sig") as handle:
            raw = list(csv.reader(handle))
    except UnicodeDecodeError:
        report.error(name, "file is not UTF-8 text; save it again as CSV UTF-8")
        return []
    if not raw:
        report.error(name, "file is empty; it needs at least the header row")
        return []
    expected = TABLES[name]["columns"]
    header = [cell.strip() for cell in raw[0]]
    if header != expected:
        missing = [c for c in expected if c not in header]
        extra = [c for c in header if c not in expected]
        report.error(name, "header row does not match data_schema.md (row 1). "
                     f"Missing: {', '.join(missing) or 'none'}. "
                     f"Unexpected: {', '.join(extra) or 'none'}. "
                     f"Required order: {','.join(expected)}")
        return []
    rows = []
    for row_number, cells in enumerate(raw[1:], start=2):
        if not any(cell.strip() for cell in cells):
            continue
        if len(cells) != len(expected):
            report.error(name, f"row {row_number} has {len(cells)} cells, expected "
                         f"{len(expected)} (check commas and double quotes)")
            continue
        row = {col: cell.strip() for col, cell in zip(expected, cells)}
        row["_row"] = row_number
        rows.append(row)
    return rows


def check_rows(name, rows, report):
    spec = TABLES[name]
    id_col = spec.get("id")
    seen = set()
    for row in rows:
        for col in spec["required"]:
            if not row[col]:
                # A blank scope is allowed for the pseudo-discipline ALL only.
                if name == "disciplines.csv" and col == "scope" and row["disc_id"] == "ALL":
                    continue
                report.error(where(name, row, col), "required value is empty")
        if id_col and row[id_col]:
            if row[id_col] in seen:
                report.error(where(name, row, id_col), f"duplicate id {row[id_col]}")
            seen.add(row[id_col])
            pattern = ID_PATTERNS.get((name, id_col))
            if pattern and not re.fullmatch(pattern[0], row[id_col]):
                report.error(where(name, row, id_col), f"id must be {pattern[1]}")
        for col, allowed in spec.get("enums", {}).items():
            if row[col] and row[col] not in allowed:
                report.error(where(name, row, col),
                             f"'{row[col]}' is not allowed; use one of: {', '.join(allowed)}")
        for col in spec.get("dates", []):
            if row[col] and not valid_date(row[col]):
                report.error(where(name, row, col),
                             f"'{row[col]}' is not a date; use YYYY-MM-DD, YYYY-MM or YYYY")
        for col in spec.get("numbers", []):
            if row[col] and not NUMBER_RE.match(row[col]):
                report.error(where(name, row, col),
                             f"'{row[col]}' is not a number (use a decimal point, no separators)")
        check_evidence_and_source(name, row, report)
    check_table_rules(name, rows, report)


def check_evidence_and_source(name, row, report):
    spec = TABLES[name]
    evidence = row.get("evidence_type", "")
    if evidence in ("not_found", "inferred") and not row.get("notes"):
        report.error(where(name, row, "notes"),
                     f"'{evidence}' rows need notes (searches made, or the reasoning)")
    source_col = spec.get("source_col")
    if source_col and evidence != "not_found" and not row[source_col]:
        report.error(where(name, row, source_col),
                     "source_id is required (point to a row in sources.csv)")


def check_table_rules(name, rows, report):
    """Rules that only apply to one table."""
    for row in rows:
        if name == "sources.csv":
            status = row["access_status"]
            if status in ("opened", "rendered") and not row["access_date"]:
                report.error(where(name, row, "access_date"),
                             f"'{status}' sources need the date the page was opened")
            if status == "not_opened" and row["access_date"]:
                report.error(where(name, row, "access_date"),
                             "'not_opened' sources must have an empty access_date")
            if row["url"] and not re.match(r"^https?://", row["url"]):
                report.error(where(name, row, "url"), "URL must start with http:// or https://")
        if name == "places.csv":
            if bool(row["lat"]) != bool(row["lon"]):
                report.error(where(name, row, "lat/lon"), "give both lat and lon, or neither")
            if NUMBER_RE.match(row["lat"]) and not -90 <= float(row["lat"]) <= 90:
                report.error(where(name, row, "lat"), "latitude must be between -90 and 90")
            if NUMBER_RE.match(row["lon"]) and not -180 <= float(row["lon"]) <= 180:
                report.error(where(name, row, "lon"), "longitude must be between -180 and 180")
        if name == "facts.csv":
            if row["evidence_type"] != "not_found" and not row["value"] and not (
                    row["value_low"] and row["value_high"]):
                report.error(where(name, row, "value"),
                             "give a value, or value_low and value_high, unless not_found")
            numeric = NUMBER_RE.match(row["value_low"]) and NUMBER_RE.match(row["value_high"])
            if numeric and float(row["value_low"]) > float(row["value_high"]):
                report.error(where(name, row, "value_low"), "value_low is larger than value_high")
        if name == "events.csv":
            if row["red_bull_involvement"] == "confirmed_absent" and not row["notes"]:
                report.error(where(name, row, "notes"),
                             "confirmed_absent needs notes naming the person or document")
            both_dates = valid_date(row["date_start"]) and valid_date(row["date_end"])
            if row["date_start"] and row["date_end"] and both_dates and row["date_end"] < row["date_start"]:
                report.error(where(name, row, "date_end"), "date_end is before date_start")
            if row["scale_type"] == "none" and row["scale_value"]:
                report.error(where(name, row, "scale_value"),
                             "scale_value is given but scale_type is 'none'")
        if name == "athletes.csv" and row["red_bull_athlete"] == "not_found" and not row["notes"]:
            report.error(where(name, row, "notes"), "not_found rows need notes naming the searches")
        if name == "redbull_finance.csv" and row["value"] and not row["unit"]:
            report.error(where(name, row, "unit"), "a value needs a unit")


def check_links(tables, report):
    """Every id used in a row must exist in its table (schema section 4)."""
    place_types = {r["place_id"]: r["place_type"] for r in tables["places.csv"]}
    disc_ids = {r["disc_id"] for r in tables["disciplines.csv"]}
    signal_ids = {r["signal_id"] for r in tables["signals.csv"]}
    source_ids = {r["source_id"] for r in tables["sources.csv"]}
    org_ids = {r["org_id"] for r in tables["organisations.csv"]}
    event_ids = {r["event_id"] for r in tables["events.csv"]}
    athlete_ids = {r["athlete_id"] for r in tables["athletes.csv"]}
    targets = {"place": place_types, "discipline": disc_ids, "org": org_ids,
               "event": event_ids, "athlete": athlete_ids}

    def link(name, row, column, valid, label):
        if row[column] and row[column] not in valid:
            report.error(where(name, row, column), f"{row[column]} is not a known {label} id")

    for row in tables["facts.csv"]:
        link("facts.csv", row, "place_id", place_types, "place")
        link("facts.csv", row, "disc_id", disc_ids, "discipline")
        link("facts.csv", row, "signal_id", signal_ids, "signal")
        link("facts.csv", row, "source_id", source_ids, "source")
        known = place_types.get(row["place_id"])
        if known and known != row["place_type"]:
            report.error(where("facts.csv", row, "place_type"),
                         f"place_type is '{row['place_type']}' but places.csv says '{known}'")
    for row in tables["events.csv"]:
        link("events.csv", row, "place_id", place_types, "place")
        link("events.csv", row, "disc_id", disc_ids, "discipline")
        link("events.csv", row, "organiser_org_id", org_ids, "organisation")
        link("events.csv", row, "source_id", source_ids, "source")
    for row in tables["organisations.csv"]:
        link("organisations.csv", row, "place_id", place_types, "place")
        link("organisations.csv", row, "disc_id", disc_ids, "discipline")
        link("organisations.csv", row, "website_source_id", source_ids, "source")
    for row in tables["athletes.csv"]:
        link("athletes.csv", row, "base_place_id", place_types, "place")
        link("athletes.csv", row, "disc_id", disc_ids, "discipline")
        link("athletes.csv", row, "source_id", source_ids, "source")
    for row in tables["redbull_finance.csv"]:
        link("redbull_finance.csv", row, "source_id", source_ids, "source")
    for row in tables["relations.csv"]:
        link("relations.csv", row, "source_id", source_ids, "source")
        for side in ("from", "to"):
            kind = row[f"{side}_type"]
            if kind in targets:
                link("relations.csv", row, f"{side}_id", targets[kind], kind)


def check_warnings(tables, report):
    for row in tables["sources.csv"]:
        if row["access_status"] == "not_opened":
            report.warn(where("sources.csv", row), "source was never opened")
    for row in tables["facts.csv"]:
        if row["confidence"] == "L":
            report.warn(where("facts.csv", row), "confidence is L")
    used_places = {row["place_id"] for row in tables["facts.csv"]}
    for row in tables["places.csv"]:
        if row["place_id"] not in used_places:
            report.warn(where("places.csv", row), "place has no facts")


def check_folder(folder):
    """Return (report, tables). tables maps file name -> list of row dicts."""
    report = Report()
    tables = {}
    for name in TABLES:
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            report.warn(name, "file not found; treated as an empty table")
            tables[name] = []
            continue
        tables[name] = read_table(name, path, report)
        check_rows(name, tables[name], report)
    check_links(tables, report)
    check_warnings(tables, report)
    return report, tables


def main(argv):
    folder, is_sample = pick_folder(argv[1] if len(argv) > 1 else None)
    print(f"Checking: {folder}")
    if is_sample:
        print("NOTE: this is not data/ (sample data or another folder). The viewer shows a SAMPLE DATA banner.")
    if not os.path.isdir(folder):
        print(f"ERROR   folder not found: {folder}")
        return 1
    report, tables = check_folder(folder)
    for line in report.errors + report.warnings:
        print(line)
    rows = sum(len(v) for v in tables.values())
    print(f"Checked {len(TABLES)} tables, {rows} rows: "
          f"{len(report.errors)} error(s), {len(report.warnings)} warning(s).")
    if report.errors:
        print("RESULT: FAILED. Fix the errors above.")
        return 1
    print("RESULT: OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
