# julian_day — spec note

Component: `formal/core/calendar/julian_day.py` · Task: slice1-eng-001 ·
Tier-2 (foundational; changes require researcher review).

## What the module guarantees

- `julian_day_number(y, m, d, calendar=...) -> int` and its inverse
  `date_from_jdn(jdn, calendar=...)` are **exact integer arithmetic**,
  mutually inverse for every integer JDN (including negative JDNs, i.e.
  dates before −4712), in all three calendar modes.
- `julian_day(y, m, d, h, mi, s, calendar=...) -> float` returns the JD of
  a civil UT instant; `datetime_from_jd(jd, calendar=...)` inverts it.
  Float precision: a double JD near the modern era resolves ~4e-5 s;
  recovered seconds are rounded to 1e-4 s.
- Invalid dates/times raise `ValueError` (month/day ranges, leap rules per
  calendar, the 1582 reform gap, hour/minute/second ranges).
- `day_of_week(jdn) = jdn % 7`, 0 = Monday … 6 = Sunday (JD 0 was a
  Monday); the week runs uninterrupted across the 1582 reform.
- Pure stdlib; no external dependencies. Time scale is UT only — ΔT/TT,
  timezones, and 真太阳时 are separate, later Slice-1 components layered on
  top of this one.

## Conventions

- **Day boundary:** JD counts days from **noon**: JD *n*.0 = 12:00 UT;
  midnight of the day with number *jdn* is *jdn* − 0.5.
- **Year numbering:** astronomical. Year 0 = 1 BCE, −1 = 2 BCE, …,
  −4712 = 4713 BCE. Year 0 is a leap year under both calendars' rules.
- **Calendar boundary** (`calendar` parameter):
  - `CAL_MIXED` (default; historical civil reckoning): Julian calendar
    through 1582-10-04, Gregorian from 1582-10-15
    (`GREGORIAN_START_JDN = 2299161`). The dates 1582-10-05 … 1582-10-14
    never existed and are rejected.
  - `CAL_GREGORIAN`: proleptic Gregorian throughout (documented option
    flag; no gap).
  - `CAL_JULIAN`: proleptic Julian throughout, with the regular 4-year
    leap rule. The historical pre-8 CE leap-day irregularities are **not**
    modelled (documented limitation).

## Algorithm source

- Conversions: the parameterised integer Gregorian/Julian ↔ JDN algorithms
  in E. G. Richards, "Calendars", ch. 15 of the *Explanatory Supplement to
  the Astronomical Almanac*, 3rd ed. (Urban & Seidelmann eds., 2013);
  Gregorian direction equivalent to Fliegel & Van Flandern, *CACM* 11(10)
  657 (1968). All divisions are floor divisions — exact for all years.
- Known-answer fixtures: Jean Meeus, *Astronomical Algorithms*, 2nd ed.,
  ch. 7, plus independent epoch definitions (J2000.0, MJD, Unix). Fixture
  table with per-row attribution:
  `formal/tests/fixtures/julian_day_fixtures.md` (all rows pending-audit —
  no verified copies in `/sources/` yet).

## Tests

`formal/tests/test_julian_day.py` — known answers, reform-gap rejection
and continuity, round-trip properties over a wide date spread (all three
calendars), JDN integer arithmetic and leap rules, weekday derivation,
input validation. Run: `bash formal/tests/run_tests.sh`.
