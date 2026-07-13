---
task_id: slice1-eng-003
type: engineering
tier: 2
status: todo
depends_on: [slice1-eng-001]
lang: en
date_added: 2026-07-13
component: calendar/sidereal-time
---

# slice1-eng-003 · Sidereal time

**One line:** GMST / LMST from JD + longitude — needed by the natal-chart client (house/ascendant work downstream).

## Deliverable
- GMST(JD) and LMST(JD, longitude) functions with documented formula source.

## Done-when
- Known-answer fixtures vs published almanac values; suite green.

## Notes / guardrails
- Tier-2. Keep longitude sign convention explicit and tested (east-positive vs west-positive is a classic bug).
