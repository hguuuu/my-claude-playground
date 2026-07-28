---
task_id: slice1-eng-001
type: engineering
tier: 2
status: done  # session 0004, 2026-07-15
depends_on: []
lang: en
date_added: 2026-07-13
component: calendar/julian-day
---

# slice1-eng-001 · Julian Day arithmetic

**One line:** JD / JDN conversions with correct Julian↔Gregorian reform handling — the numeric spine every later time calc sits on. Build first.

## Deliverable
- `calendar` core: (Y,M,D,h,m,s, UT) ↔ Julian Day; JDN for date arithmetic; explicit Gregorian-reform cutover handling (proleptic where declared).
- Spec/doc alongside code pointing at the authorities used.

## Done-when
- `test_*.py` under `formal/` with known-answer fixtures (standard JD reference epochs) — cross-validated against ≥1 independent published source (§1.3).
- `bash formal/tests/run_tests.sh` green.

## Notes / guardrails
- Tier-2 (foundational). Branch + researcher review; end log "ready for review".
- One module, two clients (pillar construction + natal charts) — no school-specific assumptions here.
