# PROJECT BRIEF — 命理 · Astrology · Tarot Research System

## Instructions for the Claude Code Agent

> **Status of this document:** Founding brief. You (the CC agent) will use this to initialize the repository. Sections marked 【living】 are expected to be revised as research progresses — but only via the Tier-2 review process defined in §9. Everything else changes only by explicit instruction from the researcher (Haiwen).

-----

## 0. Vision

A long-horizon, multi-lingual research and continuous-learning system covering:

- **八字命理** (first workstream) — later expanding to 风水、六爻、紫微斗数、七政四余
- **Western astrology / natal chart reading** (second workstream)
- **Tarot** (parallel, long-run workstream — world-construction and psychology oriented)

Core thesis: every 八字流派 is a different **rule set over the same combinatorial base** (10 天干 × 12 地支). By encoding the base formally and expressing each school as structured, testable rules, schools become comparable, evaluable, and — carefully — statistically analyzable against other symbol systems. Astrology receives the same treatment on its own base (ephemeris + aspect relations). The formal layer is the language-neutral bridge between traditions.

This is a **garden, not a project**: it does not need to be finished; it needs to never be corrupted. Depth-first vertical slices on trustworthy bedrock.

-----

## 1. The Constitution (non-negotiable rules)

### 1.1 Language policy — NO TRANSLATION

- Every note is written **in the language of its source tradition**. 八字 corpus: Chinese. Western astrology corpus: English. No exceptions.
- Never paraphrase a Chinese source in English or vice versa — not in notes, not in logs, not in commit messages about that content. Session logs for 八字 work are written in Chinese.
- Canonical example (cite this when the policy needs justification): **火 ≠ fire.** 火 is a symbol within the 生克 cycle system; “fire” carries Greek elemental baggage. They are two different symbols. Translation is where distortion enters.
- Cross-language contact happens **only** in `/comparative`: mapping notes that quote each side in its own language and analyze the structural relationship (“analogous in X way, divergent in Y way”). Mapping notes are never equivalence claims.
- The formal layer (code) is the neutral ground: identifiers may use pinyin/romanization, but semantics are defined by spec files pointing to native-language sources.

### 1.2 Citation verification — the anti-hallucination rule

- **Never cite a classical passage unless a verified copy of the source text exists in the repo** (from ctext.org, scanned editions, or materials provided by the researcher).
- Any claim sourced from web research is tagged `unverified` in frontmatter until checked against a primary text in an audit session.
- Distinguish, always and explicitly: 原文 / 后世注释 (e.g., 任铁樵注) / modern interpretation. Never present a commentary layer as the original.
- Fabricating or “reconstructing from memory” a classical quote is the single worst failure mode in this project.

### 1.3 Testing discipline — CS design principles apply to everything

- Every table (万年历, 节气 boundaries, 干支 cycles, timezone history, ephemeris outputs) and every formula has a test suite.
- **Run the full test suite at session start and before every commit.** No commit with failing tests. A silently corrupted foundational table poisons everything downstream.
- Cross-validation tests: pillar outputs verified against independent published sources; ephemeris output against published almanac data; tricky-case fixtures (LMT-era births, China timezone unification, DST edges, 节气-boundary births, 早子时/晚子时 cases).

### 1.4 Statistical guardrail — exploratory vs. confirmatory

- Exploratory correlation runs across systems are welcome and logged in `/formal/exploratory/`.
- Any interesting pattern is **promoted to a hypothesis file** (`/formal/hypotheses/`): stated precisely, with a pre-specified test, then tested on data it was NOT discovered in (fresh charts from the test bank).
- A finding never grades its own homework. Multiple-comparisons risk is assumed by default.
- Before asking whether a claim is true, record whether it is testable as stated (see rubric axis 4).

### 1.5 Scope control — seeds, not scope creep

- When you encounter anything out of the current workstream’s scope (风水 insight, 六爻 resource, tarot idea), **append it to the relevant file in `/seeds/` and move on.** One file per future topic. Seed files accumulate notes, questions, and resource links; when a topic activates, its seed file becomes the Phase-0 starting brief.

-----

## 2. Repository layout

```
/CLAUDE.md              ← distilled constitution + session ritual (you create from §1, §8)
/PROJECT_BRIEF.md       ← this document
/log/                   ← ADR-style session records + research journal
    /decisions/         ← one file per significant decision
    /sessions/          ← one entry per session (task ID, what, why, next)
    /dead-ends.md       ← negative results: disproven rules, misattributions, failed leads
/queue/                 ← task queue as markdown files (one task per file, small granularity)
/foundations/           ← shared bedrock 【living, Tier-2】
    /calendar/          ← 节气, 万年历, 真太阳时, timezone history, ΔT — notes + data
    /ganzhi/            ← 天干地支 base system, 五行, 生克, 刑冲合害 definitions
    /boundary.md        ← THE boundary document: shared bedrock vs. school-specific 【living】
/schools/               ← one directory per 流派 (子平/, 盲派/, …)
    /<school>/profile.md    ← Phase-0 one-pager 【living】
    /<school>/sources/      ← per-source intake notes
    /<school>/rules/        ← commentary on rule extraction (specs live in /formal/specs)
    /<school>/evaluation.md ← rubric scoring, 4 axes
/lexicon/               ← concept registry, one file per term, native language only
                          wiki-links [[term]] for cross-referencing; includes 文字演变 research
/sources/               ← verified primary texts (ctext dumps, scans, researcher-provided)
/comparative/           ← cross-system mapping notes (the ONLY bilingual zone)
/formal/                ← the computational layer
    /core/              ← time module, pillar construction, relation algebra, ephemeris
    /specs/             ← rule specs as JSON/YAML (first-class, see §4)
    /tests/             ← test suites + fixtures + test chart bank (anonymized, reliability-flagged)
    /exploratory/       ← correlation runs, notebooks
    /hypotheses/        ← promoted hypotheses with pre-specified tests
/views/                 ← GENERATED interactive artifacts (HTML/React) — never source of truth
/seeds/                 ← 风水.md, 六爻.md, 紫微斗数.md, 七政四余.md, tarot-world.md, …
```

Each directory gets an `INDEX.md` (map-of-content) so sessions can orient without reading everything. Keep indexes current — they are your context-budget management.

**Canonical-content principle:** knowledge lives in plain text (markdown + structured data). Anything interactive in `/views` is a generated artifact, rebuilt from specs/lexicon by script, and may be deleted at any time without information loss.

-----

## 3. Provenance schema (YAML frontmatter, required on every note)

```yaml
---
id: unique-slug
lang: zh | en
type: source-note | lexicon | rule-commentary | mapping | evaluation | log
source: 渊海子平            # primary text, edition if known
source_layer: 原文 | 注释 | modern    # which stratum this note reports
era: 宋 | 明 | 清 | modern | disputed
school: 子平 | 盲派 | shared | n/a
verification: verified | unverified   # per §1.2
reliability: 可考程度初评 (short free text, revisited in audit)
date_added: YYYY-MM-DD
tags: []
---
```

Adjust fields per note type, but `lang`, `type`, `verification`, and `source` are always required. The schema itself is Tier-2 【living】.

-----

## 4. Rule data model — rules are first-class entities

A rule spec is **not** a child of a school. It is an independent object with many-to-many source links:

```yaml
rule_id: ...
statement_zh: ...            # precise statement in source language
formalization: ...           # pointer to code implementing it, if implemented
attestations:
  - {source: 渊海子平, location: 卷X, layer: 原文, verification: verified}
  - {source: 三命通会, location: 卷Y, layer: 原文, verification: verified}
  - {source: 盲派口诀, location: ..., note: modified form — 修改点如下}
schools_using: [子平, 盲派]
variants: []                 # documented modifications by school
status: extracted | formalized | evaluated
```

Convergent attestation across independent sources is itself evidence on the 可考 axis — recording attestations feeds the rubric directly, it is not bookkeeping.

-----

## 5. Evidence rubric — four independent axes, never collapsed into one score

1. **可考 (Attestation):** Does a primary text exist? Dating? Authorship disputes (e.g., 滴天髓)? How many commentary layers between original and modern form? Which layer are we actually reading?
1. **可修复 / Internal coherence:** Self-consistent? Complete (output for every possible chart, or requires ad hoc judgment)? Deterministic, or smuggles in reader discretion? — This axis becomes fully computable once rules are in spec form.
1. **Cross-system convergence:** Independent traditions arriving at structurally similar concepts is interesting signal about shared human observation — tracked separately from truth claims.
1. **Empirical status:** Deliberately separate and honest. First record whether the claim is testable *as stated* (note Barnum/base-rate concerns), then and only then design tests. Default posture: document what the system says with precision; stay agnostic on prediction until a real test exists.

-----

## 6. Phase 0 — survey before depth (first research phase, bounded)

Because 八字 resources are deeply intertwined, a bounded mapping phase precedes depth-work, to prevent mistaking one school’s convention for universal foundation:

1. Enumerate major 流派 and method families.
1. One-page profile per school: core premise, key texts, relationships/shared material with other schools, preliminary 可考 impression. 【living — allowed to be wrong, revised as depth-work corrects it】
1. Draft `/foundations/boundary.md`: what is shared bedrock (building blocks for all interpretation) vs. school-specific. 【living】
1. Simple reliability & survivability sourcing pass: which methods survived history in what form, what primary sources are actually obtainable.

Phase-0 outputs are explicitly provisional. Their revision history (via Tier-2 commits) is a record of the researcher’s evolving understanding — that record is itself valuable.

-----

## 7. Milestone sequencing (depth-first vertical slices)

- **Slice 1 (first engineering milestone): the calendar/time module.** 真太阳时, timezone history (incl. China unification), ΔT, Julian day arithmetic, sidereal time, 节气 boundaries. One module, two clients (pillar construction + natal charts). Fully verifiable — right answers exist. Includes the researcher’s own training need: thorough time-conversion calculation and timetable-usage exercises tied to her chart calculation course.
- **Slice 2: pillar construction**, verified against course materials and known charts. Includes the 早子时/晚子时 question documented as a calendar-dispute case study.
- **Slice 3: 旺相休囚死 as a computable, season-indexed function** over the encoded base.
- **Slice 4: one school, one primary text** — full rule extraction into specs, with evaluation.
- Then: expand by slice. Astrology workstream begins alongside (course-driven): ephemeris integration, chart calculation, aspects as relations — same rigor, own language, own tests.
- Tarot: parallel, slower cadence; lives initially as design/psychology notes and a seed of the world-construction task. Step-out sessions from detail work into human-concern-oriented framing are legitimate work.

End-to-end slice 1+2 = trustworthy bedrock. Everything after is expansion.

-----

## 8. Session types & ritual

**Every session, same open:** read `CLAUDE.md` → read last N entries in `/log/sessions/` → run full test suite → pick ONE task from `/queue/`.
**Every session, same close:** write session log entry (what, why, decisions, next) → update queue → commit per §9.

Task granularity: one term, one source, one chapter of rule extraction. Never large enough to half-finish ambiguously.

Session types (tag in log + commit message):

- `phase0:` — survey/mapping work
- `intake:` — process ONE source: extract, tag provenance, file notes
- `synthesis:` — write across existing notes ONLY; no new claims from memory
- `engineering:` — formal layer work; tests mandatory
- `audit:` — re-verify citations and claims from earlier sessions against `/sources/`; clear `unverified` tags or flag problems; run periodically, this is what makes the corpus trustworthy over time

Negative results go to `/log/dead-ends.md` — disproven rules, misattributions (“claimed classical rule is a 20th-century invention”), failed leads. These are high-value findings; never silently drop them.

-----

## 9. Commit structure — semantic units, two trust tiers

**Commit = completed task.** Content change + session log entry + queue update sealed together, referencing the task ID. Tests must pass. `git log` is a secondary research journal.

- **Tier 1 — auto-commit to main:** additive leaf content. Source notes, lexicon entries, seed appends, log entries, exploratory analysis. Low blast radius.
- **Tier 2 — branch + researcher review:** load-bearing changes. Foundational tables, time module, rule spec modifications, `boundary.md` revisions, anything touching the constitution or provenance schema, promotion of findings to `/formal/hypotheses/`. Open a branch, do the work, end the session log with “ready for review.” The researcher merges.

Conventions: commit messages follow the language policy (八字 content commits in Chinese) and are prefixed with session type (`intake:`, `synthesis:`, `engineering:`, `audit:`, `phase0:`).

-----

## 10. Decision record (from founding discussions — why things are the way they are)

1. **Two-layer design** (knowledge corpus + computational layer) — because every 流派 is a rule set over the same combinatorial base; encoding the base makes schools comparable and testable rather than prose.
1. **No-translation policy** — languages carry the tradition; 火 ≠ fire. Cross-language contact confined to `/comparative` mapping notes. Formal layer is the neutral bridge.
1. **Lexicon as concept registry, not glossary** — each concept lives in its native language; includes 文字演变 (character/word evolution) research for every significant term (why 金木水火土 as symbols, etc.).
1. **Calendar module first** — several famous inter-school disputes are calendar disputes in disguise; time correctness is prerequisite to everything; it is also fully verifiable, making it the ideal first slice.
1. **Citation-verification rule** — LLMs fabricate classical Chinese quotes convincingly; the repo’s trustworthiness depends on the verified-source requirement plus periodic audit sessions.
1. **Rules as first-class entities with many-to-many attestation** — because rules recur across sources; convergent attestation is 可考 evidence.
1. **Four-axis rubric, never collapsed** — attestation, coherence, convergence, and empirical status are different kinds of evidence; conflating them is where rigor dies.
1. **Exploratory/confirmatory split** — cross-system statistics will produce chance patterns; hypotheses must be tested on data they weren’t discovered in.
1. **Phase-0 survey before depth** — sources intertwine; the boundary between shared bedrock and school convention must be mapped (provisionally) before deep dives, and revised as understanding improves.
1. **Semantic commits, two trust tiers** — commit history as research journal; human review gate only where blast radius is high.
1. **Garden framing** — depth-first slices, seeds directory for captured ambition, indexes for context management. Never needs to be finished; must never be corrupted.

-----

## 11. Your first session (initialization task)

1. Create the directory skeleton per §2 with `INDEX.md` stubs.
1. `/CLAUDE.md` is already provided in the repo root. Do NOT rewrite it. Verify it against §1 and §8 of this brief; if you find a genuine conflict or omission, report it in the session log for researcher review (CLAUDE.md is Tier-2).
1. Create `/queue/` with initial tasks: Phase-0 survey tasks (§6) and Slice-1 engineering tasks (§7), small granularity.
1. Create `/seeds/` stubs: 风水.md, 六爻.md, 紫微斗数.md, 七政四余.md, tarot-world.md — each with a one-line scope note.
1. Set up the test harness skeleton in `/formal/tests/` (even before there is code — fixtures directory, runner script, the session-start test command).
1. Initialize git, commit as `engineering: repo initialization per PROJECT_BRIEF`.
1. Write the first session log entry.

Do not begin research content in the initialization session. Bedrock first.