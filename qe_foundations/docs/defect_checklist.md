# Expected-defect checklist (fill in as you go)

<!--
PURPOSE: this is your "answer sheet" for the data. Writing the PREDICTION before you run a
query is the single best habit for catching false passes.
HOW: for each rule, (1) write what you EXPECT in the "Predicted" column BEFORE running the
query, (2) run it, (3) write the run_ids it actually returned in "Defects found (run_ids)"
(comma-separated, 4-digit ids), (4) note anything surprising. Do not delete rows.
check_exercise.py compares this table with what your queries return.
-->

| Rule | Defects found (run_ids) | Predicted (before running) | Notes / surprises |
| ---- | ----------------------- | -------------------------- | ----------------- |
| R-01 | 3                       | 3                          |                   |
| R-02 | 2                       | 2                          |                   |
| R-03 | 4                       | 4                          |                   |
| R-04 | 2                       | 2                          |                   |
| R-05 | 2                       | 2                          |                   |
| R-06 | 2                       | 2                          |                   |
| R-07 | 3                       | 3                          |                   |
| R-08 | 3                       | 3                          |                   |
| R-09 | 3                       | 3                          |                   |
| R-10 | 2                       | 2                          |                   |
| R-11 | 3                       | 3                          |                   |
| R-12 | 4                       | 4                          |                   |
| E-01 | 1                       | 1                          |                   |
| E-02 | 1                       | 1                          |                   |

## Decoys: rows that look odd but are LEGAL (we must not flag them)

<!-- List at least two run_ids and say why they are fine, e.g. "run 5xxx: SKIPPED with 0 ms -- skipped tests take no time." -->

## Rows reported by more than one rule

<!-- Which run_ids appear in two or more rules? Is that OK? (Each rule must be testable on its own.) -->

## Open questions for the product owner

<!-- Rules that are really business decisions (like "is a price of 0 allowed?" in the lesson). -->
