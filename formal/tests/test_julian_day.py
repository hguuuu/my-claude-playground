"""Tests for formal.core.calendar.julian_day (task slice1-eng-001).

Known-answer fixtures come from Jean Meeus, *Astronomical Algorithms*,
2nd ed., ch. 7, plus independent standard epoch definitions (J2000.0,
MJD epoch, Unix epoch).  The attributed fixture table lives in
formal/tests/fixtures/julian_day_fixtures.md — keep the two in sync.

Runs under both pytest and `python3 -m unittest` (unittest.TestCase).
"""

import os
import sys
import unittest

# Make `formal.*` importable no matter how the runner was invoked.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from formal.core.calendar.julian_day import (  # noqa: E402
    CAL_GREGORIAN,
    CAL_JULIAN,
    CAL_MIXED,
    GREGORIAN_START_JDN,
    date_from_jdn,
    datetime_from_jd,
    day_of_week,
    day_of_week_name,
    days_in_month,
    is_leap_year,
    julian_day,
    julian_day_number,
    validate_date,
)


# ---------------------------------------------------------------------------
# Known-answer fixtures.
# Each row: (year, month, day, hour, minute, second, expected_jd, source)
# Mirror of formal/tests/fixtures/julian_day_fixtures.md (see per-row source
# attribution there).  All times UT; astronomical year numbering; CAL_MIXED.
# ---------------------------------------------------------------------------
KNOWN_JD = [
    (2000, 1, 1, 12, 0, 0.0, 2451545.0, "Meeus ch.7 table; J2000.0 epoch (IAU/USNO)"),
    (1999, 1, 1, 0, 0, 0.0, 2451179.5, "Meeus ch.7 table"),
    (1987, 6, 19, 12, 0, 0.0, 2446966.0, "Meeus ch.7 table"),
    (1900, 1, 1, 12, 0, 0.0, 2415021.0, "Meeus ch.7 table"),
    (1600, 1, 1, 0, 0, 0.0, 2305447.5, "Meeus ch.7 table"),
    (1600, 12, 31, 0, 0, 0.0, 2305812.5, "Meeus ch.7 table"),
    (837, 4, 10, 7, 12, 0.0, 2026871.8, "Meeus ch.7 table (Julian calendar)"),
    (-4712, 1, 1, 12, 0, 0.0, 0.0, "Meeus ch.7; ESAA JD epoch definition"),
    (1957, 10, 4, 19, 26, 24.0, 2436116.31, "Meeus ex. 7.a (Sputnik 1 launch day, 1957-10-04.81)"),
    (1858, 11, 17, 0, 0, 0.0, 2400000.5, "MJD epoch definition (ESAA/USNO)"),
    (1970, 1, 1, 0, 0, 0.0, 2440587.5, "Unix epoch, standard published value"),
]


class TestKnownAnswers(unittest.TestCase):
    """Cross-validated reference epochs (Meeus ch.7 + independent epochs)."""

    def test_known_julian_days(self):
        for year, month, day, hour, minute, second, expected, source in KNOWN_JD:
            with self.subTest(date=(year, month, day), source=source):
                jd = julian_day(year, month, day, hour, minute, second)
                self.assertAlmostEqual(jd, expected, places=6)

    def test_known_julian_day_numbers(self):
        # JDN = JD at noon of the same civil day.
        cases = [
            ((2000, 1, 1), 2451545),
            ((1999, 1, 1), 2451180),
            ((1987, 6, 19), 2446966),
            ((1858, 11, 17), 2400001),
            ((-4712, 1, 1), 0),
            ((1582, 10, 4), 2299160),   # last Julian day before the reform
            ((1582, 10, 15), 2299161),  # first Gregorian day (ESAA)
        ]
        for (y, m, d), expected in cases:
            with self.subTest(date=(y, m, d)):
                self.assertEqual(julian_day_number(y, m, d), expected)
        self.assertEqual(GREGORIAN_START_JDN, 2299161)

    def test_meeus_example_7c_inverse(self):
        # Meeus ex. 7.c: JD 1842713.0 corresponds to 333 January 27.5 (Julian).
        y, m, d, hh, mm, ss = datetime_from_jd(1842713.0)
        self.assertEqual((y, m, d, hh, mm), (333, 1, 27, 12, 0))
        self.assertAlmostEqual(ss, 0.0, places=6)

    def test_sputnik_inverse(self):
        # JD 2436116.31 -> 1957-10-04, 19:26:24 UT (0.81 of a day).
        y, m, d, hh, mm, ss = datetime_from_jd(2436116.31)
        self.assertEqual((y, m, d, hh, mm), (1957, 10, 4, 19, 26))
        self.assertAlmostEqual(ss, 24.0, places=2)


class TestReformGap(unittest.TestCase):
    """1582-10-05 .. 1582-10-14 do not exist in the default mixed calendar."""

    def test_gap_dates_rejected(self):
        for day in range(5, 15):
            with self.subTest(day=day):
                with self.assertRaises(ValueError):
                    julian_day_number(1582, 10, day)
                with self.assertRaises(ValueError):
                    julian_day(1582, 10, day, 6, 30, 0.0)

    def test_gap_edges_valid(self):
        self.assertEqual(julian_day_number(1582, 10, 4), 2299160)
        self.assertEqual(julian_day_number(1582, 10, 15), 2299161)

    def test_days_are_consecutive_across_the_gap(self):
        # Civil days 1582-10-01..04 then 15..20 have consecutive JDNs.
        days = [1, 2, 3, 4, 15, 16, 17, 18, 19, 20]
        jdns = [julian_day_number(1582, 10, d) for d in days]
        self.assertEqual(jdns, list(range(jdns[0], jdns[0] + len(days))))

    def test_gap_dates_valid_in_proleptic_calendars(self):
        # In proleptic Gregorian the gap dates exist (and precede 10-15).
        self.assertEqual(
            julian_day_number(1582, 10, 5, calendar=CAL_GREGORIAN), 2299151
        )
        # In proleptic Julian they exist too (offset by the 10-day drift).
        self.assertEqual(
            julian_day_number(1582, 10, 5, calendar=CAL_JULIAN), 2299161
        )

    def test_inverse_never_lands_in_the_gap(self):
        for jdn in range(2299155, 2299167):
            y, m, d = date_from_jdn(jdn)
            if (y, m) == (1582, 10):
                self.assertFalse(5 <= d <= 14, "inverse produced a gap date")


class TestRoundTrip(unittest.TestCase):
    """date -> JD(N) -> date identity over a wide spread of dates."""

    SAMPLE_YEARS = [-4712, -1000, -1, 0, 1, 333, 837, 1000, 1234, 1581,
                    1582, 1583, 1600, 1700, 1858, 1900, 1957, 2000, 2026, 2100]

    def _valid(self, y, m, d, cal):
        try:
            validate_date(y, m, d, cal)
            return True
        except ValueError:
            return False

    def test_jdn_round_trip_all_calendars(self):
        for cal in (CAL_MIXED, CAL_GREGORIAN, CAL_JULIAN):
            for y in self.SAMPLE_YEARS:
                for m in (1, 2, 6, 10, 12):
                    for d in (1, 15, 28, days_in_month(y, m, cal)):
                        if not self._valid(y, m, d, cal):
                            continue
                        with self.subTest(cal=cal, date=(y, m, d)):
                            jdn = julian_day_number(y, m, d, calendar=cal)
                            self.assertEqual(
                                date_from_jdn(jdn, calendar=cal),
                                (y, m, d),
                            )

    def test_jdn_inverse_round_trip_over_contiguous_range(self):
        # jdn -> date -> jdn identity across a contiguous block including
        # the reform, plus blocks near JD 0 and in the far future.
        for start in (-20, 2299100, 2451500):
            for jdn in range(start, start + 120):
                with self.subTest(jdn=jdn):
                    y, m, d = date_from_jdn(jdn)
                    self.assertEqual(julian_day_number(y, m, d), jdn)

    def test_jd_datetime_round_trip(self):
        times = [(0, 0, 0.0), (7, 12, 0.0), (12, 0, 0.0),
                 (19, 26, 24.0), (23, 59, 59.5)]
        for y in (-4712, 0, 837, 1582, 1583, 1999, 2000, 2026):
            for m, d in ((1, 1), (10, 4), (12, 31)):
                if not self._valid(y, m, d, CAL_MIXED):
                    continue
                for hh, mm, ss in times:
                    with self.subTest(date=(y, m, d, hh, mm, ss)):
                        jd = julian_day(y, m, d, hh, mm, ss)
                        ry, rm, rd, rhh, rmm, rss = datetime_from_jd(jd)
                        self.assertEqual((ry, rm, rd, rhh, rmm), (y, m, d, hh, mm))
                        self.assertAlmostEqual(rss, ss, places=3)


class TestJdnArithmetic(unittest.TestCase):
    """Integer date arithmetic on JDNs."""

    def test_year_length(self):
        self.assertEqual(
            julian_day_number(2000, 1, 1) - julian_day_number(1999, 1, 1), 365
        )
        self.assertEqual(
            julian_day_number(2001, 1, 1) - julian_day_number(2000, 1, 1), 366
        )

    def test_leap_rules_gregorian(self):
        # 1900 not leap (century), 2000 leap (quadricentennial).
        self.assertEqual(
            julian_day_number(1900, 3, 1) - julian_day_number(1900, 2, 28), 1
        )
        self.assertEqual(
            julian_day_number(2000, 3, 1) - julian_day_number(2000, 2, 28), 2
        )
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900, CAL_GREGORIAN))
        self.assertTrue(is_leap_year(1900, CAL_JULIAN))

    def test_astronomical_year_numbering(self):
        # Year 0 (= 1 BCE) exists and is a leap year in both calendars.
        self.assertTrue(is_leap_year(0, CAL_JULIAN))
        self.assertTrue(is_leap_year(0, CAL_GREGORIAN))
        self.assertEqual(days_in_month(0, 2, CAL_JULIAN), 29)
        # Dec 31 of year -1 is the day before Jan 1 of year 0.
        self.assertEqual(
            julian_day_number(0, 1, 1) - julian_day_number(-1, 12, 31), 1
        )

    def test_negative_jdn_supported(self):
        # Floor-division algorithms remain exact before JD 0.
        y, m, d = date_from_jdn(-1)
        self.assertEqual(julian_day_number(y, m, d), -1)
        self.assertEqual((y, m, d), (-4713, 12, 31))

    def test_jd_of_midnight_is_jdn_minus_half(self):
        self.assertEqual(julian_day(2000, 1, 1), 2451545 - 0.5)


class TestDayOfWeek(unittest.TestCase):
    def test_reference_weekdays(self):
        # JD 0 was a Monday (standard fact).
        self.assertEqual(day_of_week(0), 0)
        self.assertEqual(day_of_week_name(0), "Monday")
        # 2000-01-01 was a Saturday.
        self.assertEqual(day_of_week_name(julian_day_number(2000, 1, 1)), "Saturday")
        # Thursday 1582-10-04 was followed by Friday 1582-10-15.
        self.assertEqual(day_of_week_name(julian_day_number(1582, 10, 4)), "Thursday")
        self.assertEqual(day_of_week_name(julian_day_number(1582, 10, 15)), "Friday")

    def test_week_advances_by_one(self):
        base = julian_day_number(2026, 7, 15)
        for k in range(15):
            self.assertEqual(day_of_week(base + k), (day_of_week(base) + k) % 7)


class TestValidation(unittest.TestCase):
    def test_invalid_dates_rejected(self):
        bad = [
            (2000, 0, 1), (2000, 13, 1), (2000, 1, 0), (2000, 1, 32),
            (1999, 2, 29),                      # not a leap year
            (1900, 2, 29),                      # Gregorian century rule
        ]
        for y, m, d in bad:
            with self.subTest(date=(y, m, d)):
                with self.assertRaises(ValueError):
                    julian_day_number(y, m, d)

    def test_julian_leap_feb_29_1900_valid_in_julian(self):
        # 1900 IS a Julian leap year.
        julian_day_number(1900, 2, 29, calendar=CAL_JULIAN)  # must not raise

    def test_invalid_times_rejected(self):
        for h, mi, s in [(-1, 0, 0.0), (24, 0, 0.0), (0, 60, 0.0), (0, 0, 60.0)]:
            with self.subTest(time=(h, mi, s)):
                with self.assertRaises(ValueError):
                    julian_day(2000, 1, 1, h, mi, s)

    def test_unknown_calendar_rejected(self):
        with self.assertRaises(ValueError):
            julian_day_number(2000, 1, 1, calendar="hebrew")


if __name__ == "__main__":
    unittest.main()
