# Ingestion module - design notes (Week 2, Day 2)

Answer in your own words, 2-4 sentences each. Replace every line that starts with

## 1. Exceptions or assertions?

In `validate_record` I raise exceptions for a negative duration, but in
`IngestionReport.check_invariants` I use `assert`. Why is each the right tool there?

A negative duration is bad input data. It has to be caught and reported even when Python runs with the O flag that disables assertions. That is what exceptions do. In check_invariants I check my own bookkeeping, like valid plus rejected equalling rows seen. That can only go wrong if my code has a bug. So I want an assert to crash "loudly" right there.

## 2. Stop or collect?

Why is a malformed JSON file a `SourceError` that stops loading, while a record with
a bad status is a `RecordValidationError` that is collected? Who benefits from this split?

A malformed JSON file has no reliable way to split into records. The parser fails so the whole file is unusable and it stops with a SourceError. A bad status only affects one record. The other rows are still fine so I collect it and keep going with a RecordValidationError.

## 3. What did the context managers buy you?

Name two things that `open_source` / `LoadSession` do for the caller that you would otherwise
have to remember to do at every call site.

open_source gives me guaranteed closing plus UTF8 and BOM handling. It also turns OS and decoding errors into my own exception types. LoadSession records the start time the outcome and the elapsed seconds automatically.

## 4. Your hardest bad-input case

Which sample file or record took you longest to handle, and what was the cause?

N/A
