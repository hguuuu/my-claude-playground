---
id: session-0003-study-migration
lang: en
type: log
session_type: engineering
task: study-001 — execute the study-system migration per study/DESIGN.md §12
date: 2026-07-28
tier: 2
status: ready for review
---

# Session 0003 — study-system migration (study-001)

**Session type:** `engineering:` (structural, Tier 2). Executes the migration plan of `study/DESIGN.md` v1.3, which was drafted and iterated with the researcher across this session's design discussion (see the doc's own commit trail, v1 → v1.3).

## What

All eight §12 steps:

1. `plan/00–07` moved from `study/inbox/` to `study/plan/`; inbox retired.
2. `study/RULES.md` written (roles, language rules, frontmatter conventions, tag registry seed, cadences, quiz modes, SQLite schema v1 + build triggers, firewalls, tiers). `study/skills.md` seeded from Phase 1 exit criteria — 8 criterion nodes + 4 ongoing nodes, all `untested`/`learning`; first weekly review tests them against the headstart.
3. First root `STATUS.md` generated (two-engine dashboard); `log/status-archive/` created. Templates written (`daily` with `did_*` booleans, `prediction`, `case`, `literature-note` with the three-strata structure).
4. Working files created: `questions.md`, `comparative-table.md` (seeded with the plan's known break-points), `错题本.md` (as a view over `cases/`). Directory skeleton + INDEX stubs: `journal/{daily,predictions}`, `cases/`, `examples/`, `quizzes/`, `reviews/weekly/`, `systems/{tarot,bazi,astrology,iching,lenormand}`, `templates/`.
5. **CLAUDE.md amended (Tier 2):** session ritual now opens with `/STATUS.md` and closes with the study write-back step + STATUS regeneration/archival; `study:` session type added (ritual-exempt, tests still mandatory); a "Study system" section states the constitution-level firewalls and points to DESIGN/RULES.
6. Research-engine updates per DESIGN §11a: `origin:` convention documented in `queue/INDEX.md` (with the no-queue-jumping rule); seeds `lenormand.md` + `易经.md` added (易经 note in Chinese per §1.1); `/comparative/INDEX.md` documents its promotion inflow criterion; `slice1-train-001/002` deliverables re-pointed to `/study/quizzes/` (still double as time-module cross-checks).
7. `formal/tests/test_frontmatter.py` — validator v1 (unique ids repo-wide, required fields per note type, controlled vocabularies; no external deps). Suite discovers it: 3 passed. Two-way link resolution + basis-tag checks are in-file TODOs, deferred until records exist to check.
8. Queue + all touched INDEXes updated; `study-001` closed (`done`, re-classed tier 1→2 with the reason recorded in the task file).

## Why (key decisions)

- **DESIGN.md is the rationale record** — this log doesn't repeat it. The doc was reviewed by the researcher iteratively through v1.3 before execution was authorized ("go ahead and execute the migration").
- **`study-001` scope change recorded, not hidden:** originally "file the inbox upload" (tier 1); became "execute the integration design" (tier 2) through the design discussion. The task file documents the re-class.
- **Validator kept v1-honest:** it checks what exists (ids, fields, vocab) and defers what doesn't yet (link targets, basis tags) as explicit TODOs — a green suite that overclaims would be worse than a small one.
- **skills.md statuses deliberately conservative:** everything `untested` despite the headstart; evidence links must come from actual quiz/blind-test/mentor events (first weekly review), never from assertion.

## Next

- Researcher review & merge of this branch (constitution amendment + all study structure).
- First weekly review: calibrate skill map + reading tracker, start the daily habit, first STATUS regeneration.
- Authorize the first research task — recommend `phase0-001` (流派 enumeration; now also cross-lens mode's prerequisite per DESIGN §11a.7).
- Standing: revisit scheduled Routines ≈ late Aug (tracked in STATUS next-actions).

**Ready for review.**
