# INDEX — /log/sessions

> Map-of-content. Keep current: this is how sessions orient without reading everything (PROJECT_BRIEF §2).

**Purpose:** One entry per session: task ID, what, why, decisions, next. Read the last few at every session open.

Tier 1. 八字 session logs in Chinese; engineering-session logs may be either language.

## Session-ID convention (since 2026-07-28)

`NNNN-YYYY-MM-DD-<slug>` — **the date is part of the ID.** Parallel sessions on different branches cannot see each other's numbers, so the date+slug is the collision-proof identity; the sequence number is finalized at merge time (whoever merges second renumbers, patching self-references). Frontmatter `id:` carries the full form (e.g. `session-0004-2026-07-15-slice1-eng-001`).

**Renumber record (2026-07-28):** research-branch sessions originally numbered 0002/0003/0004 were renumbered to 0004/0005/0006 after the study-track sessions (merged to main first) took 0002/0003. Commit messages predating the renumber cite the old numbers; map: old-0002→0004 (slice1-eng-001), old-0003→0005 (phase0-001), old-0004→0006 (meta-001).

**Renumber record (2026-07-28, second):** calibration-branch sessions originally numbered 0002/0003 were renumbered to 0009/0010 at merge-sync (s0011), after main's 0002–0008 took precedence by merge order. Commit messages predating the renumber cite the old numbers; map: old-0002→0009 (phase0-001 duplicate run), old-0003→0010 (phase0-002).

## Contents

| session | date | type | task | status |
|---------|------|------|------|--------|
| `0001-2026-07-13-init` | 2026-07-13 | `engineering:` | repo initialization per brief §11 | merged (PR #1) |
| `0002-2026-07-28-study-track` | 2026-07-28 | `engineering:` | add `/study/` track + inbox | merged (PR #2) |
| `0003-2026-07-28-study-migration` | 2026-07-28 | `engineering:` | study-001: execute migration per `study/DESIGN.md` §12 | merged (PR #2) |
| `0004-2026-07-15-slice1-eng-001` | 2026-07-15 | `engineering:` | Julian Day arithmetic module + tests | merged (PR #3) |
| `0005-2026-07-15-phase0-001` | 2026-07-15 | `phase0:` | 八字流派与方法族枚举（含对抗性核查补记） | merged (PR #3) |
| `0006-2026-07-16-meta-001` | 2026-07-16 | `engineering:` | source-reliability metric + encounter register | merged (PR #3) |
| `0007-2026-07-28-meta-prefix` | 2026-07-28 | `meta:` | add `meta:` session type (constitution amendment) | merged (PR #3) |
| `0008-2026-07-28-pre-pr-audit` | 2026-07-28 | `audit:` | 合并前全量审计（拦截2处经典直引；清除pyc） | merged (PR #3) |
| `0009-2026-07-28-phase0-001-dup` | 2026-07-28 | `phase0:` | 流派枚举（重复执行，凭通识）——分类法已由 s0005 取代；三问互补假说存续 | superseded (record kept) |
| `0010-2026-07-28-phase0-002` | 2026-07-28 | `phase0:` | 一手文献可得性清查（v0 输出已撤回出 PR，或以 deep-research 重做；见 git history） | run recorded; output withdrawn |
| `0011-2026-07-28-merge-sync` | 2026-07-28 | `meta:` | merge main; adjudicate duplicated phase0-001; renumber; STATUS regen | ready for review |

Note: sessions 0004–0006 predate 0002–0003 in wall-clock time — the sequence reflects merge order, the dates reflect when the work happened (see convention above).
