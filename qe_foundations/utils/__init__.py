"""Public utility helpers for qe_foundations."""

from qe_foundations.utils.strings import is_valid_email, normalize_whitespace, slugify, mask_email
from qe_foundations.utils.numbers import clamp, is_positive_int,percent
from qe_foundations.utils.dates import add_days, is_weekend, timestamp_for_filename, days_between
from qe_foundations.utils.data_gen import FIRST_NAMES, ROLES, make_users

__all__ = [
    # strings
    "normalize_whitespace",
    "slugify",
    "is_valid_email",
    " mask_email",
    # numbers
    "is_positive_int",
    "clamp",
    "percent",
    # dates
    "add_days",
    "is_weekend",
    "timestamp_for_filename",
    "days_between",
    # data_gen
    "FIRST_NAMES",
    "ROLES",
    "make_users",
]