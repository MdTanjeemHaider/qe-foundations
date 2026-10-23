# Pairing log -- roles and swap schedule

<!--
HOW TO USE: copy this file to  qe_foundations/docs/pairing_log.md.
Fill ONE row at the END of every 30-minute block (it takes one minute). The check
script counts the rows that are filled in; a 3-hour session has 5 driving blocks.
-->

## Roles card (keep it visible)

|                  | DRIVER                                                             | NAVIGATOR                                                                          |
| ---------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Hands            | the ONLY one on the keyboard                                       | off the keyboard                                                                   |
| Job              | turn the navigator's direction into code; think aloud while typing | read the rule, decide the next step, predict the result, spot typos and edge cases |
| Says things like | "I'm writing the WHERE clause now..."                              | "Predict first: which run_ids do we expect?"                                       |
| Never            | silently type something nobody asked for                           | grab the mouse or dictate character by character                                   |

**Swap** every 30 minutes, even in the middle of a rule. The outgoing driver commits and pushes
(your own Git name), the new driver runs `git pull`, then types.

## Pair

|           | Name              | Git user.name (as shown by `git log`) | Machine / repo owner |
| --------- | ----------------- | --------------------------------------- | -------------------- |
| Partner A | Md Tanjeem Haider | MdTanjeemHaider                         | X                    |
| Partner B | Brandon Wong      | Brand643                                |                      |

Branch: `feature/sql-validation-...`        Remote: ...

## Swap log (one row per block)

| Block | Clock time | Driver     | Navigator  | Goal of the block                                                                                      | Result (rules done, commit hash)                                           | Predictions: right / wrong |
| ----- | ---------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | -------------------------- |
| 1     | 0:00       | Md Tanjeem | Brandon    | Explore test_runs; fill the "Predicted" column; write R-01 to R-04                                     | R-01 to R-04, 91284e0fb367badb49d1154ba1caa8911f382844                    | right                      |
| 2     | 0:30       | Brandon    | Md Tanjeem | R-05 to R-08                                                                                           | R-05 to R-08, 965c73ce567b4668f3c5471f70d768170e1a3071                    | right                      |
| 3     | 1:00       | Md Tanjeem | Brandon    | R-09 to R-12, then E-01 and E-02                                                                       | R-09 to R-12, then E-01 and E-02, 47401c12c8b3fe4de6fb7f794f82f7ee680ed90f | right                      |
| 4     | 2:00       | Brandon    | Md Tanjeem | Python: `ValidationFailedError`, `run_rule`, `run_all`, `setup_logging`, `main` (the runner) | done, 3d8e323dcfd27345598a8199f6f2cc65ecbb8ef5                            | right                      |
| 5     | 3:00       | Md Tanjeem | Brandon    | Unit tests, defect checklist, 2 defect reports; run check_exercise.py and fix FAILs                    | done, 1ee1d37d7801084534d6038ce54d29eee7491843                            | right                      |

## Disagreements and how we settled them

Whenever we disagreed, we tried both appraoches and choose the one that felt cleaner and more efficient.

<!-- At least one honest example: what did you disagree about (query style, a rule's meaning, ...), and how did you decide? -->

## Hints we used

<!-- Which hint levels, for which rules? (Using hints is fine -- hiding it is not.) -->
