"""qe_foundations/ingestion/readers.py  -  TASK 4 (about 35 min)

One reader per format. Each returns a LIST OF RAW RECORDS and only deals with
FORMAT problems (is this valid CSV / JSON / XML? are the columns there?).
Business rules (is the status allowed? is the duration negative?) belong to
validation.py, NOT here.

Always open files through open_source() from contexts.py.
See README Task 4 for the exact contract of each reader.
"""

import csv
import json
import xml.etree.ElementTree as ET

from .contexts import open_source
from .exceptions import MalformedSourceError, MissingColumnsError
from .validation import REQUIRED_FIELDS


def read_csv_records(path):
    """CSV -> list of raw dicts, one per data row (use csv.DictReader)."""
    with open_source(path) as file:
        reader = csv.DictReader(file)
        field_names = reader.fieldnames

        missing = []
        if field_names == None:
            missing = list(REQUIRED_FIELDS)
            raise MissingColumnsError(path, missing)

        for field_name in REQUIRED_FIELDS:
            if field_name not in field_names:
                missing.append(field_name)

        if missing:
            raise MissingColumnsError(path, missing)

        return list(reader)


def read_json_records(path):
    """JSON -> list of raw records. Expected shape: {"suite": ..., "tests": [...]}."""
    with open_source(path) as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise MalformedSourceError(path, f"invalid JSON at line {e.lineno} column {e.colno}: {e.msg}") from e

        if not isinstance(data, dict):
            raise MalformedSourceError(path, "the top level is not an object")

        if "tests" not in data:
            raise MalformedSourceError(path, "missing 'tests' key")

        tests = data["tests"]
        if not isinstance(tests, list):
            raise MalformedSourceError(path, "not a list")

        return data["tests"]

def read_xml_records(path):
    """XML -> list of raw dicts, one per <testcase> element at ANY depth."""
    with open_source(path) as file:
        try:
            root = ET.parse(file).getroot()
        except ET.ParseError as e:
            raise MalformedSourceError(path, e) from e

        records = []
        for case in root.iter("testcase"):
            records.append(
                {
                    "id": case.attrib.get("id"),
                    "status": case.attrib.get("status"),
                    "title": case.findtext("title"),
                    "duration": case.findtext("duration")
                }
            )

        return records