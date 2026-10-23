
# Retrospective -- Thursday Pair Exercise (SQL Validation)

## Pair and branch

We worked together on the QE Foundations project using the `feature/sql-validation-MdTanjeemHaider-Brand643` branch. We collaborated on the SQL validation queries, Python runner, unit tests, and documentation.

## What we built

We created SQL queries to validate test-run data and identify problems such as missing values, invalid statuses, incorrect durations, and inconsistent failure messages. We also worked on a Python runner to execute the queries and report PASS or FAIL for each validation rule. Finally, we added unit tests and documentation to explain the defects found.

## How the pairing worked

We used the driver and navigator approach, taking turns driving and reviewing the work. The driver focused on writing the code, while the navigator checked the requirements, considered edge cases, and helped identify mistakes. This helped us review the queries together and understand why each validation rule was needed.

## The hardest rule

R-11 was one of the more challenging rules because it checks two different conditions: FAILED and ERROR runs need a non-blank failure message, while PASSED runs must not have a failure message. We had to use parentheses and combine conditions with OR to make sure the query checked both cases correctly.

## A surprise in the data

One important thing we learned was that unusual-looking data is not always invalid. For example, a duration of zero milliseconds is allowed for a skipped test. This showed us why we need to understand the requirements before writing validation queries instead of flagging every unusual value as a defect.

## SQLite and SQL pitfalls we hit

We learned that NULL values need to be checked with `IS NULL` rather than `= NULL`. We also learned that `TRIM()` helps detect leading and trailing spaces, `BETWEEN` includes both endpoints, and SQLite's `LIKE` operator can be case-insensitive for certain patterns. Another important lesson was to use parentheses when combining AND and OR conditions to avoid incorrect results.

## Skills we connected from this week

We connected SQL validation with the Python skills we learned earlier in the week. The Python runner uses packages and imports, custom exceptions, logging, and unit tests to make the validation process repeatable. Git branching, commits, and pulling changes also helped us practise collaborating on a shared project.

## What we would do differently

We would spend more time predicting which rows each query should return before running it. We would also test edge cases such as NULL values, blank strings, whitespace, and legal zero-duration runs earlier. Finally, we would commit and push smaller changes more frequently so that problems are easier to identify and resolve.
