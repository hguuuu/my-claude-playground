# INDEX — /queue

> Map-of-content. One task per file, small granularity (one term / one source / one module component).
> Take exactly ONE task per session (§8). Update this map when tasks are added, taken, or completed.

**Legend:** status `todo` = ready · `blocked` = waiting on a dependency · `done` = completed (row kept for the record) · Tier 2 = branch + researcher review before merge.

**`origin:` convention:** tasks born from study questions carry `origin: study/questions.md#<entry>` in frontmatter. Session close then writes the answer back (CLAUDE.md ritual). Study-originated tasks enter as *proposals* at weekly review — they never jump the queue; the researcher authorizes what runs.

## Phase 0 — survey before depth (§6)

| task | tier | status | depends on |
|------|------|--------|-----------|
| `phase0-001-liupai-enumeration` — 八字流派与方法族枚举 | 1 | **done** (session 0005; duplicate run s0009 superseded) | — |
| `phase0-002-source-obtainability` — 一手文献可得性与存续清查 | 1 | **done·provisional** (s0010) — 研究者决定：或以 deep-research 重做，修订暂缓 | — |
| `phase0-003-draft-boundary` — 起草 boundary.md v0 | 2 | todo (unblocked; Tier-2 须授权；002 若重做或需重开) | ~~001~~, ~~002~~ |
| `phase0-004-school-profile-fanout` — 逐流派一页 profile（fan-out） | 1 | todo (unblocked) | ~~001~~ |

## Intake — 文本入库（源自 phase0-002 清查；随 002 重做决定一并复审）

| task | tier | status | depends on |
|------|------|--------|-----------|
| `intake-001-三命通会` — ctext 转写+四库扫描双形态 | 1 | todo | — |
| `intake-002-渊海子平` — 宋核明辑，层积标注 | 1 | todo | — |
| `intake-003-子平真诠评注` — ⚠ 剥层：沈原文 vs 徐评注 | 1 | todo | — |
| `intake-004-李虚中命书` — 古法代表，托名存疑 | 1 | todo | — |
| `intake-005-滴天髓原文` — 只入赋文层 | 1 | todo | — |
| `intake-006-穷通宝鉴` — 并立造化元钥异本比对案 | 1 | todo | — |

## Slice 1 — calendar / time module (§7), one component per task

| task | tier | status | depends on |
|------|------|--------|-----------|
| `slice1-eng-001-julian-day` — Julian Day arithmetic | 2 | **done** (session 0004) | — |
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
| `meta-001-source-reliability-metric` — reliability metric + encounter register | 2 | **done** (session 0006) | — |
| `meta-002-wenxianxue-subgrading` — A-class sub-grading from 文献学 (deferred half of meta-001) | 2 | todo (s0010 survey 的甲/乙/丙分级是其粗稿素材) | — |

## Study track — researcher's parallel study plan (`/study/`)

| task | tier | status | depends on |
|------|------|--------|-----------|
| `study-001-process-inbox` — migration executed per `study/DESIGN.md` §12 (session 0003) | 2 | done | — |

Note: `slice1-train-001/002` deliverables re-pointed into `/study/quizzes/` (DESIGN §11a.6); still cross-check the time module.

## Notes
- The 流派 taxonomy is a Phase-0 **output**, not a founding assumption — the current 6-school layout in `/schools/` is s0005's, provisional by design.
- phase0-002 status is **provisional** by researcher decision (2026-07-28): main's 001 depth raised the bar; a deep-research redo of 002 is under consideration. Do not build load-bearing work on the s0010 survey without checking.
- These definitions are provisional — the researcher reviews and adjusts before depth sessions are authorized.
