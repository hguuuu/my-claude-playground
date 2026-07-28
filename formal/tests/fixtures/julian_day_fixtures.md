# Julian Day known-answer fixtures

Task: slice1-eng-001. Consumed by `formal/tests/test_julian_day.py`
(the `KNOWN_JD` table there must stay in sync with this file).

Conventions: all times UT; astronomical year numbering (year 0 = 1 BCE);
mixed civil calendar (Julian through 1582-10-04, Gregorian from 1582-10-15).
Dates before the reform are therefore Julian-calendar dates.

Cross-validation policy (§1.3): every row names its source. Meeus counts as
one source; rows whose value is also fixed by an independent standard
definition (IAU/USNO/ESAA epoch definitions, POSIX) name that second source.
Rows recorded from training knowledge only were included **only where the
value is certain**; uncertain candidates were omitted rather than guessed
(see "Deliberately omitted" below).

Verification status of every row: **pending-audit** — to be re-checked
against physical copies of the cited books in an audit session (no verified
copy exists in `/sources/` yet).

## Fixture table

| date (UT, astronomical years) | expected JD | source | verified-against-source |
|---|---|---|---|
| 2000-01-01 12:00 (Gregorian) | 2451545.0 | Meeus, *Astronomical Algorithms* 2nd ed., ch. 7 table; independently the J2000.0 epoch definition (IAU 1994 / USNO, ESAA) | pending-audit |
| 1999-01-01 00:00 (Gregorian) | 2451179.5 | Meeus ch. 7 table | pending-audit |
| 1987-06-19 12:00 (Gregorian) | 2446966.0 | Meeus ch. 7 table | pending-audit |
| 1900-01-01 12:00 (Gregorian) | 2415021.0 | Meeus ch. 7 table | pending-audit |
| 1600-01-01 00:00 (Gregorian) | 2305447.5 | Meeus ch. 7 table | pending-audit |
| 1600-12-31 00:00 (Gregorian) | 2305812.5 | Meeus ch. 7 table | pending-audit |
| 837-04-10 07:12 (Julian) | 2026871.8 | Meeus ch. 7 table (837 April 10.3) | pending-audit |
| -4712-01-01 12:00 (Julian) | 0.0 | Meeus ch. 7; independently the JD epoch definition (ESAA: JD 0 = 4713 BCE Jan 1.5, Julian proleptic) | pending-audit |
| 1957-10-04 19:26:24 (Gregorian) | 2436116.31 | Meeus ch. 7, example 7.a (Sputnik 1 launch day, 1957 October 4.81) | pending-audit |
| 1858-11-17 00:00 (Gregorian) | 2400000.5 | Modified Julian Date epoch definition, MJD = JD − 2400000.5 (ESAA/USNO; independent of Meeus) | pending-audit |
| 1970-01-01 00:00 (Gregorian) | 2440587.5 | Unix/POSIX epoch as JD, standard published value (independent of Meeus) | pending-audit |
| JD 1842713.0 → 333-01-27 12:00 (Julian) | (inverse fixture) | Meeus ch. 7, example 7.c | pending-audit |
| 1582-10-04 (Julian) JDN 2299160 → next civil day 1582-10-15 (Gregorian) JDN 2299161 | (reform-boundary fixture) | ESAA ch. 15 (Richards, "Calendars"); the reform gap is also stated in Meeus ch. 7 | pending-audit |

## Deliberately omitted (uncertain from training knowledge — never fabricate)

- The negative-year rows of the Meeus ch. 7 table (−123, −122, −1000,
  −1001 entries): remembered values failed an internal consistency
  cross-check, so none were included. Add in an audit session with the
  book open.
- Meeus example 7.b (interval between two dates) and the other worked
  exercises of ch. 7: exact operands not remembered with certainty.
