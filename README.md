# qe-foundations

A small Python package of shared foundations (string, number, date and test-data
helpers) used across the QE course exercises and demos.

## Project 1 milestone — Week 2, Monday

**What exists now**

- `qe_foundations/` package with `__version__ = "0.1.0"`.
- `qe_foundations/utils/` sub-package re-exporting every helper:
  - `strings.py` — `normalize_whitespace`, `slugify`, `is_valid_email`
  - `numbers.py` — `is_positive_int`, `clamp`, `percent`
  - `dates.py`   — `add_days`, `is_weekend`, `timestamp_for_filename`
  - `data_gen.py`— `FIRST_NAMES`, `ROLES`, `make_users`
- `tests/` and `data/` placeholders (`.gitkeep`).
- `docs/structure.md` describing the folder layout.
- `smoke_utils.py` to verify the package imports and works.

**Coming Tuesday–Friday**

- N/A

## Setup

1. **Create a virtual environment**

   ```bash
   python -m venv .venv
   ```
2. **Activate it**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   ```bash
   source .venv/bin/activate
   ```
3. **Install dependencies**

   ```
   python -m pip install -r requirements.txt
   ```
4. **Verify the Setup**

   ```
   python smoke_utils.py
   ```

**Usage**

```python
from datetime import date
from qe_foundations.utils import slugify, make_users, add_days, is_weekend

print(slugify("  Login Page: Happy Path "))   # login-page-happy-path
print(make_users(3, seed=1))                  # deterministic user dicts
print(add_days(date(2025, 1, 31), 1))         # 2025-02-01
print(is_weekend(date(2025, 2, 1)))           # True (Saturday)
```
