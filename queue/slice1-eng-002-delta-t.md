---
task_id: slice1-eng-002
type: engineering
tier: 2
status: todo
depends_on: [slice1-eng-001]
lang: en
date_added: 2026-07-13
component: calendar/delta-t
---

# slice1-eng-002 · ΔT (TT − UT1) model

**One line:** ΔT model so dynamical-time calculations (节气, ephemeris) map back to civil UT.

## Deliverable
- ΔT(year) implementation over the historical range needed; documented model + validity range.

## Done-when
- Fixtures against published ΔT tables at sampled years; tolerance stated. Suite green.

## Notes / guardrails
- Tier-2. Record the model source and its stated uncertainty — ΔT is estimated, not exact, for historical/future dates.
