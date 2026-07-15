---
task_id: slice1-eng-004
type: engineering
tier: 2
status: todo
depends_on: [slice1-eng-001]
lang: en
date_added: 2026-07-13
component: calendar/timezone-history
---

# slice1-eng-004 · Timezone history & civil-offset resolution

**One line:** Resolve the civil UTC offset in force at a given place+instant — including China's 1949 unification to UTC+8, pre-unification zones, pre-standard-time LMT, and DST periods.

## Deliverable
- Offset resolver (place + instant → offset), backed by a documented historical zone source (e.g. tz database), with the China-unification and LMT-era cases explicitly handled.

## Done-when
- Fixtures for: China pre/post 1949 unification, a DST-edge birth, and a pre-standard-time LMT birth. Suite green.

## Notes / guardrails
- Tier-2. Several famous inter-school disputes are calendar/timezone disputes in disguise — correctness here is prerequisite to everything (§10.4).
