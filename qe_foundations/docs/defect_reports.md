# Defect reports (top 2 findings)

## Defect report 1

**Title:** Invalid Test Execution Duration

**Rule:** R-04 - Validity: `duration_ms` must be present and not negative.

**Environment / when:** Database; identified on Thursday

**Query:**

```sql
SELECT run_id
FROM test_runs
WHERE duration_ms IS NULL OR duration_ms < 0;
```

**Evidence:** The query identifies records with missing or negative execution durations. Affected run IDs: 5009, 5016. Observed duration values: 5009, 5016.

**Impact:** Missing or negative durations can make test execution reports and performance analysis inaccurate. Negative durations are invalid, and missing durations prevent reliable measurement of execution time.

**Severity (suggested) and why:** High - invalid duration data can affect QA reporting and performance investigations.

**Question or false-alarm check:** Could a duration of 0 milliseconds be mistaken for a defect? No. Zero is explicitly allowed, including for skipped tests, and this query correctly does not flag it.

---

## Defect report 2

**Title:** Inconsistent Failure Messages and Test Statuses

**Rule:** R-11 - Consistency: FAILED/ERROR runs need a failure message; PASSED runs must not have one.

**Environment / when:** Database; identified on Thursday

**Query:**

```sql
SELECT run_id
FROM test_runs
WHERE (status IN ('FAILED', 'ERROR')
       AND (failure_message IS NULL OR TRIM(failure_message) = ''))
   OR (status = 'PASSED'
       AND failure_message IS NOT NULL
       AND TRIM(failure_message) <> '');
```

**Evidence:** The query identifies FAILED or ERROR runs with missing or blank failure messages and PASSED runs with non-blank failure messages. Affected run IDs: 5003, 5012, 5033. Observed status and failure-message values: 5003, 5012, 5033.

**Impact:** Missing failure information makes it harder for QA engineers to investigate failed tests and identify root causes. Inconsistent failure messages can also reduce confidence in test reports.

**Severity (suggested) and why:** High - missing diagnostic information can delay troubleshooting and make automated test results less useful.

**Question or false-alarm check:** Could a SKIPPED run with a skip reason be incorrectly flagged? It should not be. The query does not flag SKIPPED runs. Also, the current query does not flag PASSED runs whose failure message is an empty string or whitespace only; those should be considered under the requirement that PASSED runs must have no failure message.
