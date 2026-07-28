---
id: skill-map
type: skill-map
---

# Skill Map

> Competency nodes per system. `status: untested | learning | passed | stale` — **passed decays to stale after 6 untested weeks.** `evidence` links the quiz/blind-test/mentor check that established the status; never hand-asserted. Phase exit criteria map onto nodes so phase completion is readable off this file. Structure is Tier 2; status updates are Tier 1 (weekly review).
>
> Seeded 2026-07-28 from Phase 1 exit criteria (`plan/02`). All nodes start `untested` — the headstart likely passes several; **the first weekly review tests them** rather than waiting out the calendar (plan file 01 §7).

## Phase 1 criteria nodes

```yaml
- node: tarot/blind-production-3card
  status: untested          # pass = coherent+specific, aloud, no books, twice 2 weeks apart
  evidence: null
  last_tested: null
  phase_criterion: P1
- node: tarot/fools-journey-narration
  status: untested
  evidence: null
  last_tested: null
  phase_criterion: P1
- node: scholarly/hanegraaff-construct-teachback
  status: untested
  evidence: null
  last_tested: null
  phase_criterion: P1
- node: bazi/yinyang-wuxing-shengke-on-sight
  status: untested          # 阴阳五行 生克 relationships on sight
  evidence: null
  last_tested: null
  phase_criterion: P1
- node: bazi/ganzhi-wuxing-attributes-on-sight
  status: untested          # 天干地支 五行 attributes on sight
  evidence: null
  last_tested: null
  phase_criterion: P1
- node: bazi/hand-cast-chart-wannianli
  status: untested          # hand-cast from 万年历, 十神 assignment teacher-checked
  evidence: null
  last_tested: null
  phase_criterion: P1
- node: practice/six-week-logged-streak
  status: untested          # ≥6 weeks daily draws with predictions + outcomes
  evidence: null
  last_tested: null
  phase_criterion: P1
- node: mentor/readiness-confirmed
  status: untested          # the "am I there yet?" conversation held
  evidence: null
  last_tested: null
  phase_criterion: P1
```

## Ongoing competency nodes (not phase-gated)

```yaml
- node: tarot/majors-0-7
  status: learning          # mentorship: done 7/17 per plan 00
  evidence: null
  last_tested: null
- node: tarot/majors-8-14
  status: learning          # mentorship: late July
  evidence: null
  last_tested: null
- node: bazi/paipan-drill
  status: learning
  evidence: null
  last_tested: null
- node: bazi/shishen-identification
  status: learning
  evidence: null
  last_tested: null
```

Later phases add nodes as they activate (minors/courts, 格局, 藏干, Marseille open reading, casting, decans, Lenormand grammar…).
