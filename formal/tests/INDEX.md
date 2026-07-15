# INDEX — /formal/tests

> Map-of-content stub. Keep current: this is how sessions orient without reading everything (PROJECT_BRIEF §2).

**Purpose:** Test suites + fixtures + test chart bank (anonymized, reliability-flagged). Run at session start and before every commit.

Session-start command: `bash formal/tests/run_tests.sh`. See runner + fixtures/.

## Contents

- `test_julian_day.py` — known-answer + property tests for `formal/core/calendar/julian_day.py` (Meeus ch.7 epochs, 1582 reform gap, round trips, JDN arithmetic, weekday). Fixtures: `fixtures/julian_day_fixtures.md`.
