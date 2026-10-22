"""qe_foundations/ingestion/validation.py  -  TASK 5 (about 25 min)

validate_record() decides whether ONE raw record is acceptable.

IMPORTANT: this is VALIDATION OF EXTERNAL DATA. Raise exceptions here.
Do NOT use `assert` in this file (assertions can be switched off with `python -O`).
See README Task 5 for the exact rules.
"""

from .exceptions import InvalidValueError, MissingFieldError
import math

REQUIRED_FIELDS = ("id", "title", "status", "duration")
VALID_STATUSES = ("pass", "fail", "blocked")


def validate_record(row, raw):
    """Turn one raw record into a clean dict, or raise a RecordValidationError.

    row : 1-based record number in the file (used in error messages)
    raw : whatever the reader produced for that record (usually a dict)

    Returns {"id": str, "title": str, "status": str, "duration": float}.
    """
    if not isinstance(raw, dict):
        raise InvalidValueError(row, "record", raw, "a dict")

    for field in REQUIRED_FIELDS:
        value = raw.get(field)
        if isinstance(value,str):
            value = value.strip()

        if value == "" or value == None:
            raise MissingFieldError(row, field)

    status = raw["status"]
    if not isinstance(status, str):
        raise InvalidValueError(row, "status", raw["status"], f"any of the following: {VALID_STATUSES}")

    status = status.strip().lower()
    if status not in VALID_STATUSES:
        raise InvalidValueError(row, "status", raw["status"], f"any of the following: {VALID_STATUSES}")

    duration = raw["duration"]
    if isinstance(duration,bool):
        raise InvalidValueError(row, "duration", duration, "an number greater than 0")

    try:
        float(duration)
    except (TypeError, ValueError):
        raise InvalidValueError(row, "duration", duration, "an number greater than 0")

    duration = float(duration)
    if duration < 0 or math.isnan(duration) or math.isinf(duration):
        raise InvalidValueError(row, "duration", duration, "an number greater than 0")

    return {
        "id": str(raw["id"]).strip(),
        "title": str(raw["title"]).strip(),
        "status": status,
        "duration": duration,
    }
