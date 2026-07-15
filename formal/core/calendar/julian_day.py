"""Julian Day arithmetic — the numeric spine of the calendar/time module.

Task: slice1-eng-001 (Slice 1, calendar/time module — PROJECT_BRIEF §7).

What this module provides
-------------------------
* ``julian_day_number(year, month, day, calendar=...)`` — Julian Day Number
  (JDN), an integer labelling a whole calendar day.  Exact integer
  arithmetic; safe for date arithmetic (differences, weekday, cycles).
* ``julian_day(year, month, day, hour, minute, second, calendar=...)`` —
  Julian Day (JD) as a float, for a civil time in Universal Time (UT).
* ``date_from_jdn(jdn, calendar=...)`` — inverse of ``julian_day_number``.
* ``datetime_from_jd(jd, calendar=...)`` — inverse of ``julian_day``.
* ``day_of_week(jdn)`` — weekday derived from the JDN.
* Helpers: ``is_leap_year``, ``days_in_month``, ``validate_date``.

Algorithm source (do not modify without re-checking against the books)
----------------------------------------------------------------------
The calendar <-> JDN conversions are the standard integer-arithmetic
algorithms published in:

* E. G. Richards, "Calendars", chapter 15 of the *Explanatory Supplement
  to the Astronomical Almanac*, 3rd ed. (S. E. Urban & P. K. Seidelmann,
  eds., University Science Books, 2013) — the parameterised integer
  Gregorian/Julian <-> JDN algorithms.
* Equivalent to H. F. Fliegel & T. C. Van Flandern, "A Machine Algorithm
  for Processing Calendar Dates", *Communications of the ACM* 11(10),
  p. 657 (1968) for the Gregorian direction.

All divisions in these formulas are FLOOR divisions (Python ``//``), which
makes them exact for all years, positive and negative, i.e. valid over the
whole proleptic range (unlike the truncation-sensitive form in Meeus).

Known-answer test values are taken from Jean Meeus, *Astronomical
Algorithms*, 2nd ed. (Willmann-Bell, 1998), chapter 7 ("Julian Day"),
plus independent standard epoch definitions (J2000.0, MJD epoch, Unix
epoch); see formal/tests/fixtures/julian_day_fixtures.md.

Conventions (binding for all clients of this module)
----------------------------------------------------
* **Time scale:** all civil times are Universal Time (UT).  This module is
  pure calendar arithmetic; ΔT / TT and timezone handling are separate,
  later components.
* **Day boundary:** JD is the astronomical day count starting at **noon**:
  JD n.0 is 12:00 UT, JD n.5 is 00:00 UT of the next calendar day.  The
  integer JDN of a calendar day equals the JD at that day's noon:
  ``jd(00:00) == jdn - 0.5``.
* **Year numbering:** astronomical year numbering everywhere.  Year 0 =
  1 BCE, year -1 = 2 BCE, ..., year -4712 = 4713 BCE.  There is no year
  gap and the leap rules apply uniformly (year 0 is a leap year).
* **Calendar boundary** (``calendar`` parameter):
    - ``CAL_MIXED`` (default, historical civil reckoning): the Julian
      calendar through 1582-10-04, then the Gregorian calendar from
      1582-10-15 (the papal reform).  The dates 1582-10-05 .. 1582-10-14
      **do not exist** and raise ``ValueError``.
    - ``CAL_GREGORIAN``: proleptic Gregorian for all dates (the Gregorian
      rules extended indefinitely backwards; no gap).
    - ``CAL_JULIAN``: proleptic Julian for all dates (regular 4-year leap
      rule; the historical pre-8 CE leap-day irregularities are NOT
      modelled — documented limitation).
* **Weekday:** ``day_of_week(jdn) == jdn % 7`` with 0 = Monday .. 6 =
  Sunday (JD 0 = -4712-01-01 Julian was a Monday).

No external dependencies; pure Python stdlib.
"""

import math
from typing import NamedTuple

__all__ = [
    "CAL_MIXED",
    "CAL_GREGORIAN",
    "CAL_JULIAN",
    "GREGORIAN_START_JDN",
    "CalendarDate",
    "CalendarDateTime",
    "is_leap_year",
    "days_in_month",
    "validate_date",
    "julian_day_number",
    "julian_day",
    "date_from_jdn",
    "datetime_from_jd",
    "day_of_week",
    "day_of_week_name",
]

# Calendar-selection flags (see module docstring, "Calendar boundary").
CAL_MIXED = "mixed"          # Julian <= 1582-10-04, Gregorian >= 1582-10-15
CAL_GREGORIAN = "gregorian"  # proleptic Gregorian throughout
CAL_JULIAN = "julian"        # proleptic Julian throughout

_CALENDARS = (CAL_MIXED, CAL_GREGORIAN, CAL_JULIAN)

# JDN of 1582-10-15 Gregorian, the first day of the reformed calendar.
# 1582-10-04 Julian is JDN 2299160; the two days are consecutive.
GREGORIAN_START_JDN = 2299161


class CalendarDate(NamedTuple):
    year: int
    month: int
    day: int


class CalendarDateTime(NamedTuple):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: float


def _check_calendar(calendar):
    if calendar not in _CALENDARS:
        raise ValueError(
            "unknown calendar %r (expected one of %s)" % (calendar, ", ".join(_CALENDARS))
        )


# ---------------------------------------------------------------------------
# Leap years and month lengths
# ---------------------------------------------------------------------------

_DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap_year(year, calendar=CAL_MIXED):
    """True if February of ``year`` has 29 days under ``calendar``.

    Astronomical year numbering; Python ``%`` on negative ints is a floor
    modulus, so the rules hold for negative years (year 0 and -4 are
    Julian leap years; year 0 and -400 are Gregorian leap years).
    In CAL_MIXED, February 1582 and earlier is Julian; 1583+ Gregorian.
    """
    _check_calendar(calendar)
    if calendar == CAL_JULIAN or (calendar == CAL_MIXED and year < 1583):
        return year % 4 == 0
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month, calendar=CAL_MIXED):
    """Number of days in the given month (1..12).

    Note: in CAL_MIXED, October 1582 nominally reports 31 — the missing
    dates 5..14 are handled as a gap by ``validate_date``, not as a short
    month.
    """
    if not 1 <= month <= 12:
        raise ValueError("month must be in 1..12, got %r" % (month,))
    if month == 2 and is_leap_year(year, calendar):
        return 29
    return _DAYS_IN_MONTH[month - 1]


def validate_date(year, month, day, calendar=CAL_MIXED):
    """Raise ValueError if (year, month, day) is not a valid calendar date.

    In CAL_MIXED, the reform gap 1582-10-05 .. 1582-10-14 is invalid.
    """
    _check_calendar(calendar)
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("year, month, day must be integers")
    if not 1 <= month <= 12:
        raise ValueError("month must be in 1..12, got %r" % (month,))
    if not 1 <= day <= days_in_month(year, month, calendar):
        raise ValueError("day %r invalid for %d-%02d" % (day, year, month))
    if calendar == CAL_MIXED and (year, month) == (1582, 10) and 5 <= day <= 14:
        raise ValueError(
            "1582-10-%02d does not exist: the Gregorian reform removed "
            "1582-10-05 .. 1582-10-14 (Julian through 1582-10-04, Gregorian "
            "from 1582-10-15). Use calendar=CAL_GREGORIAN or CAL_JULIAN for "
            "a proleptic reckoning." % day
        )


# ---------------------------------------------------------------------------
# Calendar date -> JDN  (Richards / ESAA 3rd ed. ch. 15; Fliegel &
# Van Flandern 1968).  Floor division throughout; exact for all years.
# ---------------------------------------------------------------------------

def _jdn_gregorian(year, month, day):
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    return day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045


def _jdn_julian(year, month, day):
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    return day + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083


def julian_day_number(year, month, day, calendar=CAL_MIXED):
    """Julian Day Number (integer) of a calendar date.

    The JDN labels the whole calendar day; it equals the JD at that day's
    noon (12:00 UT).  Validates the date, including the 1582 reform gap
    in CAL_MIXED.
    """
    validate_date(year, month, day, calendar)
    if calendar == CAL_JULIAN:
        return _jdn_julian(year, month, day)
    if calendar == CAL_GREGORIAN:
        return _jdn_gregorian(year, month, day)
    # CAL_MIXED: Gregorian from 1582-10-15, Julian through 1582-10-04.
    if (year, month, day) >= (1582, 10, 15):
        return _jdn_gregorian(year, month, day)
    return _jdn_julian(year, month, day)


def julian_day(year, month, day, hour=0, minute=0, second=0.0, calendar=CAL_MIXED):
    """Julian Day (float) of a civil date and time in UT.

    JD n.0 = 12:00 UT; midnight (00:00 UT) of a day with number ``jdn``
    is ``jdn - 0.5``.  ``second`` may be fractional.
    """
    if not 0 <= hour <= 23:
        raise ValueError("hour must be in 0..23, got %r" % (hour,))
    if not 0 <= minute <= 59:
        raise ValueError("minute must be in 0..59, got %r" % (minute,))
    if not 0 <= second < 60:
        raise ValueError("second must satisfy 0 <= s < 60, got %r" % (second,))
    jdn = julian_day_number(year, month, day, calendar)
    day_fraction = (hour * 3600.0 + minute * 60.0 + second) / 86400.0
    return jdn - 0.5 + day_fraction


# ---------------------------------------------------------------------------
# JDN / JD -> calendar date  (inverse algorithms, same sources)
# ---------------------------------------------------------------------------

def _date_from_jdn_gregorian(jdn):
    a = jdn + 32044
    b = (4 * a + 3) // 146097
    c = a - (146097 * b) // 4
    d = (4 * c + 3) // 1461
    e = c - (1461 * d) // 4
    m = (5 * e + 2) // 153
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    year = 100 * b + d - 4800 + m // 10
    return CalendarDate(year, month, day)


def _date_from_jdn_julian(jdn):
    c = jdn + 32082
    d = (4 * c + 3) // 1461
    e = c - (1461 * d) // 4
    m = (5 * e + 2) // 153
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    year = d - 4800 + m // 10
    return CalendarDate(year, month, day)


def date_from_jdn(jdn, calendar=CAL_MIXED):
    """Calendar date (year, month, day) of an integer Julian Day Number.

    Inverse of ``julian_day_number``.  In CAL_MIXED the switch happens at
    GREGORIAN_START_JDN (JDN 2299161 = 1582-10-15 Gregorian; JDN 2299160 =
    1582-10-04 Julian) — every integer JDN maps to exactly one civil date.
    """
    _check_calendar(calendar)
    if not isinstance(jdn, int):
        raise ValueError("jdn must be an integer, got %r" % (jdn,))
    if calendar == CAL_JULIAN:
        return _date_from_jdn_julian(jdn)
    if calendar == CAL_GREGORIAN:
        return _date_from_jdn_gregorian(jdn)
    if jdn >= GREGORIAN_START_JDN:
        return _date_from_jdn_gregorian(jdn)
    return _date_from_jdn_julian(jdn)


def datetime_from_jd(jd, calendar=CAL_MIXED):
    """Civil date and UT time of a Julian Day (float).

    Inverse of ``julian_day``.  Returns CalendarDateTime(year, month, day,
    hour, minute, second) with integer hour/minute and float second.

    Precision note: a double-precision JD near the modern era (~2.4e6 days)
    resolves time only to ~4e-5 s, so the recovered seconds are rounded to
    1e-4 s to absorb representation noise.  A value that rounds up to
    exactly 24:00:00 rolls over to the next day.
    """
    jdn = math.floor(jd + 0.5)
    seconds = round((jd + 0.5 - jdn) * 86400.0, 4)
    if seconds >= 86400.0:
        jdn += 1
        seconds = 0.0
    year, month, day = date_from_jdn(jdn, calendar)
    hour = int(seconds // 3600.0)
    seconds -= hour * 3600.0
    minute = int(seconds // 60.0)
    second = round(seconds - minute * 60.0, 4)
    if second >= 60.0:  # defensive: absorb any residual rounding edge
        second = 0.0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
    return CalendarDateTime(year, month, day, hour, minute, second)


# ---------------------------------------------------------------------------
# Weekday
# ---------------------------------------------------------------------------

_WEEKDAY_NAMES = (
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
)


def day_of_week(jdn):
    """Weekday of a Julian Day Number: 0 = Monday .. 6 = Sunday.

    ``jdn % 7`` — JD 0 (-4712-01-01 Julian) was a Monday.  The seven-day
    week runs uninterrupted across the 1582 reform (Thursday 1582-10-04
    was followed by Friday 1582-10-15).
    """
    if not isinstance(jdn, int):
        raise ValueError("jdn must be an integer, got %r" % (jdn,))
    return jdn % 7


def day_of_week_name(jdn):
    """English weekday name for a Julian Day Number."""
    return _WEEKDAY_NAMES[day_of_week(jdn)]
