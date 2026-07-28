# INDEX — /queue

> Map-of-content. One task per file, small granularity (one term / one source / one module component).
> Take exactly ONE task per session (§8). Update this map when tasks are added, taken, or completed.

**Legend:** status `todo` = ready · `blocked` = waiting on a dependency · `done` = completed (row kept for the record) · Tier 2 = branch + researcher review before merge.

**`origin:` convention:** tasks born from study questions carry `origin: study/questions.md#<entry>` in frontmatter. Session close then writes the answer back (CLAUDE.md ritual). Study-originated tasks enter as *proposals* at weekly review — they never jump the queue; the researcher authorizes what runs.

## Phase 0 — survey before depth (§6)

| task | tier | status | depends on |
|------|------|--------|-----------|
| `phase0-001-liupai-enumeration` — 八字流派与方法族枚举 | 1 | **done** (session 0003) | — |
| `phase0-002-source-obtainability` — 一手文献可得性与存续清查 | 1 | todo | — |
| `phase0-003-draft-boundary` — 起草 boundary.md v0 | 2 | blocked | ~~001~~, 002 |
| `phase0-004-school-profile-fanout` — 逐流派一页 profile（fan-out） | 1 | todo (unblocked) | ~~001~~ |

## Slice 1 — calendar / time module (§7), one component per task

| task | tier | status | depends on |
|------|------|--------|-----------|
| `slice1-eng-001-julian-day` — Julian Day arithmetic | 2 | **done** (session 0002) | — |
| `slice1-eng-002-delta-t` — ΔT (TT−UT1) model | 2 | todo (unblocked) | ~~001~~ |
| `slice1-eng-003-sidereal-time` — sidereal time (GMST/LMST) | 2 | todo (unblocked) | ~~001~~ |
| `slice1-eng-004-timezone-history` — timezone history & civil offset | 2 | todo (unblocked) | ~~001~~ |
| `slice1-eng-005-true-solar-time` — 真太阳时 | 2 | todo | ~~001~~, 004 |
| `slice1-eng-006-jieqi-boundaries` — 节气 boundaries | 2 | todo | ~~001~~, 002 |
| `slice1-eng-007-tricky-fixtures` — tricky-case fixture bank | 2 | todo | 004, 005, 006 |
| `slice1-eng-008-time-module-api` — unify into one module, two clients | 2 | blocked | 001–006 |
| `slice1-train-001-timezone-conversion-drills` — researcher time-conversion drills | 1 | todo | — |
| `slice1-train-002-timetable-usage-drills` — researcher 万年历 usage drills | 1 | todo | — |

## Meta / methodology

| task | tier | status | depends on |
|------|------|--------|-----------|
| `meta-001-source-reliability-metric` — reliability metric + encounter register | 2 | **done** (session 0004) | — |
| `meta-002-wenxianxue-subgrading` — A-class sub-grading from 文献学 (deferred half of meta-001) | 2 | todo | — |

## Study track — researcher's parallel study plan (`/study/`)

| task | tier | status | depends on |
|------|------|--------|-----------|
| `study-001-process-inbox` — migration executed per `study/DESIGN.md` §12 (session 0003) | 2 | done | — |

Note: `slice1-train-001/002` deliverables re-pointed into `/study/quizzes/` (DESIGN §11a.6); still cross-check the time module.

## Notes
- The 流派 taxonomy is a Phase-0 **output**, not a founding assumption — `/schools/` is intentionally empty until `phase0-001` runs.
- Suggested first depth task after review: `slice1-eng-001` (numeric spine) or `phase0-001` (map before digging). Researcher to authorize.
- These definitions are provisional — the researcher reviews and adjusts before the first research session is authorized.
