# INDEX — /formal/tests/fixtures

> Map-of-content stub. Keep current: this is how sessions orient without reading everything (PROJECT_BRIEF §2).

**Purpose:** Test fixtures: known-answer tables and tricky-case inputs (LMT-era births, China timezone unification, DST edges, 节气-boundary births, 早子时/晚子时).

Subdir: `charts/` = anonymized test chart bank with reliability flags.

## Contents

- `julian_day_fixtures.md` — Julian Day known-answer table with per-row source attribution (Meeus ch.7 + independent epoch definitions); all rows pending-audit. Mirrors `KNOWN_JD` in `../test_julian_day.py`.
