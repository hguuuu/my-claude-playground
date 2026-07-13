---
task_id: slice1-eng-005
type: engineering
tier: 2
status: todo
depends_on: [slice1-eng-001, slice1-eng-004]
lang: en
date_added: 2026-07-13
component: calendar/真太阳时
---

# slice1-eng-005 · 真太阳时 (true/apparent solar time)

**One line:** 真太阳时 = civil clock time → standard-meridian time (via 004) + longitude correction + equation of time. The input pillar construction actually needs.

## Deliverable
- `真太阳时(instant, longitude, offset)` composing longitude correction + equation of time; documented equation-of-time source.

## Done-when
- Fixtures at solstice/equinox-adjacent dates (equation-of-time extrema) cross-checked against published values; suite green.

## Notes / guardrails
- Tier-2. Keep the term 真太阳时 native — do NOT collapse it to an English gloss in code semantics; identifier may be pinyin/romanized, meaning is defined by the spec pointing at the source (§1.1).
