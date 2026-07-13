---
task_id: slice1-eng-007
type: engineering
tier: 2
status: todo
depends_on: [slice1-eng-004, slice1-eng-005, slice1-eng-006]
lang: en
date_added: 2026-07-13
component: tests/tricky-fixtures
---

# slice1-eng-007 · Tricky-case fixture bank

**One line:** Assemble the standing regression fixtures that guard the time module against the known-hard cases (§1.3).

## Deliverable
- Fixtures under `formal/tests/fixtures/` for: LMT-era births, China timezone unification, DST edges, 节气-boundary births, 早子时/晚子时. Each fixture states its expected answer AND its authoritative source.

## Done-when
- Fixtures wired into the suite; `run_tests.sh` exercises them; suite green.

## Notes / guardrails
- Tier-2 (validation infra is first-class). 早子时/晚子时 is recorded here as a *case*, not resolved as doctrine — its resolution is a Slice-2 calendar-dispute study.
