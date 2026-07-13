---
task_id: slice1-eng-006
type: engineering
tier: 2
status: todo
depends_on: [slice1-eng-001, slice1-eng-002]
lang: en
date_added: 2026-07-13
component: calendar/节气
---

# slice1-eng-006 · 节气 boundaries (apparent solar longitude)

**One line:** Compute the 24 节气 instants as apparent-solar-longitude crossings (每 15°) — the true month boundaries for 八字 (not lunar months).

## Deliverable
- `节气(year)` → the 24 boundary instants (UT), from solar longitude; documented solar-position source; consumes ΔT (002).

## Done-when
- Fixtures vs a published 万年历 / almanac for sampled years (esp. 立春 as year-pillar boundary); tolerance stated; suite green.

## Notes / guardrails
- Tier-2 (foundational table). Keep 节气 names native.
- Feeds the 早子时/晚子时 and 节气-boundary-birth cases (see slice1-eng-007) — but those are documented as calendar-dispute case studies in Slice-2, not decided here.
