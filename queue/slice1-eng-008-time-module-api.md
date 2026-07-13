---
task_id: slice1-eng-008
type: engineering
tier: 2
status: blocked
depends_on: [slice1-eng-001, slice1-eng-002, slice1-eng-003, slice1-eng-004, slice1-eng-005, slice1-eng-006]
lang: en
date_added: 2026-07-13
component: core/time-module
---

# slice1-eng-008 · Unify into one time module (two clients)

**One line:** Compose 001–006 into a single `formal/core` time module with a clean API serving both clients: pillar construction AND natal-chart calculation.

## Deliverable
- One module, documented public API; both client entry points can obtain 真太阳时, 节气 boundaries, JD, sidereal time, ΔT, resolved offset from it.
- `formal/core/INDEX.md` updated.

## Done-when
- Full suite green; API smoke-tested from both client directions.

## Notes / guardrails
- Tier-2. This closes the Slice-1 bedrock. End log "ready for review".
