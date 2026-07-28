---
id: study-system-design-v1
lang: en (native terms untranslated; language rules in §4 apply to content, not to this doc)
type: design
status: DRAFT — for researcher review; executes as the study-001 restructure on approval
date: 2026-07-28
tier: 2
supersedes: study/inbox filing plan of session 0002
---

# Study System × Research Corpus — Integration Design v1

> One repo, two engines: the **research corpus** (claims about traditions, grounded in verified sources) and the **study system** (claims about the researcher's competence and calibration, grounded in logged practice). This document specifies how they share one repository, one knowledge graph, and one trust model — without blurring roles.
>
> Sources for this design: PROJECT_BRIEF.md, CLAUDE.md, the researcher's 8-file study plan (`plan/00–07`), the Obsidian-vs-custom-KG decision analysis, and the design discussion of 2026-07-28. Where this doc and the constitution conflict, the constitution governs.

---

## 1. Principles

1. **Files are truth; everything else is a view.** Plain markdown + YAML frontmatter is the single source of truth. Obsidian is a reading/writing surface; the future SQLite index is a rebuildable cache; anything visual is a `/views/` artifact. Nothing durable lives only in a chat.
2. **Capture is never blocked by rigor; rigor runs in batch.** Daily practice writes at Obsidian speed. The constitution's machinery (validation, sourcing, promotion) runs at weekly review and in research sessions — where Claude does the lifting.
3. **The corpus is the answer engine; the study is the question engine.** Study claims about traditions either cite the corpus or are visibly tagged `未考`. Study questions become research tasks. Answers are written back to where the question arose.
4. **The assistant scaffolds, never interprets** (plan file 07, governing rule). Claude organizes, counts, schedules, retrieves, validates, compares against documented references — and never drafts a reading or supplies "the" interpretation.
5. **Nothing merges silently.** Attributions keep their source (GD ≠ Muchery ≠ 神煞); traditions keep their language; analogies keep their break-points; hits keep their scrutiny; study data never becomes research evidence through a side door.

---

## 2. Repository topology

```
/                          research corpus (constitution governs; §11a lists its updates)
├── CLAUDE.md              constitution (+ amendments in §11)
├── PROJECT_BRIEF.md
├── STATUS.md              THE dashboard — both engines, one page (§8.4); regenerated
│                          by Claude at every review/session close, read by the human
├── foundations/  schools/  lexicon/  sources/  comparative/  formal/  views/  seeds/
├── queue/                 ONE queue for both engines (study-originated tasks included)
├── log/                   sessions, decisions, dead-ends
│
└── study/                 the study system (this design)
    ├── DESIGN.md          this document
    ├── RULES.md           operating rules: language, templates, tag registry,
    │                      schema conventions, quiz cadence, SQLite schema v1 + triggers
    ├── skills.md          the skill map (§8.1)
    ├── questions.md       study→research trigger ledger (§3)
    ├── comparative-table.md   working table; entries promote to /comparative (§3)
    ├── 错题本.md           VIEW over cases with errors + extracted lessons (§6)
    ├── plan/              study-plan files 00–07 (moved from inbox)
    ├── journal/
    │   ├── daily/         daily 3-card draw entries (template in RULES.md)
    │   └── predictions/   falsifiable predictions, frontmatter-tracked
    ├── cases/             real-world case bank, longitudinal (§6)
    ├── examples/          worked-example reference bank, provenance-tagged (§7)
    ├── quizzes/           generated quizzes + results (§8.2)
    ├── reviews/weekly/    weekly review records
    └── systems/           per-card / per-十神 / per-hexagram / per-decan records
        ├── tarot/  bazi/  astrology/  iching/  lenormand/
```

**Obsidian opens the repo root as the vault** — links must cross the study↔corpus boundary; the shared graph is the point of one repo.

---

## 3. The loop (the core mechanism)

**Downward — study cites the corpus.** Every tradition-claim in a study record carries a `basis` entry: either a citation into `/sources/`, `/lexicon/`, or `/comparative/`, or the explicit tag `未考` (not yet sourced). The absence of an authentic answer is therefore machine-findable — the weekly `未考` sweep is a research backlog generated for free.

**Upward — study questions become research tasks.** One line in `questions.md` at the moment a question arises; keep studying. At weekly review, each question is triaged into a `/queue/` task by shape:

| Question shape | Session type |
|---|---|
| "What does the primary text actually say?" | `intake:` |
| "Is this attribution/claim historically real?" | `audit:` |
| "Which schools hold this? Where's the boundary?" | `phase0:` |
| "Can this be computed/verified?" | `engineering:` |

**Write-back.** A research session that answers a study question closes by flipping the study record's `未考` → citation and marking the question resolved. Debunked claims go to `/log/dead-ends.md`; the 错题本 links to them. The answer appears where the question arose.

**Promotion (study → corpus), one pattern everywhere:**

- `comparative-table.md` entry → `/comparative/` mapping note, **when both sides are quotable from verified material** (each side in its own language, break-point explicit, never an equivalence claim).
- `systems/` record insight → `/lexicon/` entry, written **fresh from a verified source** in an `intake:` session — never lifted from the study note.
- Case computational content → `/formal/tests/fixtures/charts/`, when anonymized + reliability-flagged (§6 firewall).
- Pattern noticed in practice → `/formal/exploratory/`, and onward per §1.4 of the brief only on data it was not discovered in.

---

## 4. Language rules (constitution §1.1 applied to /study/)

1. **Quotes and literature notes: always the source language.** 子平真诠 quoted in Chinese, Pollack in English, Papus in French. Classical passages additionally require a verified copy in `/sources/` or an explicit `unverified` tag — §1.2 does not stop at the study boundary.
2. **Insights and personal synthesis: mixed language is legitimate.** Study notes are the researcher's own voice; untranslatable terms (用神, 格局, decan, open reading) stay native inline.
3. **Nothing crosses into the corpus in mixed form.** Promotion is where language discipline re-tightens to the corpus rules.
4. Meta-documents (plans, reviews, STATUS, this doc) are neutral ground, like engineering logs.

---

## 5. Data conventions (what makes the knowledge graph derivable)

1. **Every note has a stable, unique `id`** — English/pinyin slug as canonical (CJK-safe linking); native-language `title` and `aliases` in frontmatter.
2. **Machine-readable in frontmatter; human prose in the body.** Anything a tool needs is a YAML field. Inline `[[wiki-links]]` are navigation only.
3. **Typed edges live in frontmatter, and every edge carries provenance:**

```yaml
---
id: card-3-of-swords
type: study-card-record
system: tarot-rws
title: Three of Swords
decan_attribution:
  - {target: lexicon/mercury-libra-2, source: golden-dawn, verification: 未考}
analogous_to:
  - {target: lexicon/某term, note: "break-point: ...", verification: 未考}
appeared_in: [journal/daily/2026-07-27]
---
```

Edge `source:` says *whose* attribution (GD / Muchery / 神煞 derivation); `verification:` says *how well-attested* per the corpus. Two halves of one trust model.
4. **No derived data in the truth layer.** Counts, hit rates, misread tallies are computed by tooling, never stored in frontmatter (they *will* drift stale).
5. **Tag registry** in RULES.md: fields for countable dimensions (controlled vocabulary, validator-checked); free `tags:` for emergent themes; new tags registered or merged at weekly review. Claude may propose topic tags; judgment tags are the researcher's.
6. **A frontmatter validator runs in the research test suite** (`run_tests.sh`): unique ids, no dangling refs, every tradition-claim has a `basis`, controlled vocabularies respected, no derived fields present.

---

## 6. Cases — the real-world case bank

**One case = one file = longitudinal record.** A 命例, a historical event read with known outcome, a fictional-character exercise, a friend reading, or an own question with a verifiable outcome. Every attempt appends to the same file — initial reading, mentor's take, re-reads with new skill, eventual outcome. Both hits and misses, with equal scrutiny: a hit's entry must say *why* it hit (specific mechanism vs. vague-enough-to-fit-anything).

```yaml
---
id: case-2026-007
type: case
case_type: 命例 | historical-event | fiction | friend-reading | own-question
systems: [bazi]
outcome_known: true
fixture_eligible: false      # §6 firewall below
attempts:
  - {date: 2026-07-28, verdict: partial, note: "..."}
tags: [早子时, career-question]
---
```

**错题本.md is a view, not a store:** an index over cases where something went wrong, plus the extracted lesson and drill target. It keeps its deliberate-practice function without being the only memory (an error-only log has the inverse of the Barnum bias).

**Firewall (constitution §1.4, hard rule):** a case's *computational* content (the chart itself — objective, right-answer-exists) may be promoted to `/formal/tests/fixtures/` when anonymized and reliability-flagged. A case's *interpretive* content (did the reading "work") is study-side forever for any case practiced on: interpretive hypotheses can never be confirmed on cases they were formed on. The prediction log and journal are calibration instruments, **never research evidence**.

---

## 7. Worked-example reference bank — `/study/examples/`

Published readings and worked analyses by other practitioners, collected as **reference material for practice**, per system.

- **Sources:** worked 命例 in texts already entering the corpus (千里命稿 is full of them — these double-file: corpus intake note + example-bank pointer), published spread readings, chart delineations, online cartomancy examples.
- **Provenance still applies, lightly:** every example records where it came from (book/URL/author, system, school if known) and defaults `verification: unverified`. An example from a classical text routes through the corpus (`/sources/`) like any other passage. Examples are *references*, never authorities — a published reading is **a** documented reading, not **the** answer.
- **What they enable:** interpretation practice with a comparison key that isn't Claude's opinion (§8.2, mode C). This is how personal interpretation becomes quizzable without breaking the never-interpret rule.

---

## 8. The assessment layer

### 8.1 Skill map — `study/skills.md`

Competency nodes per system — tarot (majors, minors, courts, spread production, open reading), 八字 (排盘, 十神, 藏干, 格局, 用神), scholarly track (Dummett thesis, Hanegraaff construct, correlative cosmology), astrology and Lenormand when they activate. Each node:

```yaml
- node: bazi/十神-assignment
  status: learning        # untested | learning | passed | stale
  evidence: quizzes/2026-07-25.md
  last_tested: 2026-07-25
  phase_criterion: P1     # exit criteria map onto nodes
```

Phase completion becomes readable off the map. **Passed decays to stale** after N untested weeks (spaced testing, not one-time certification). "What next" = stale nodes + 错题本 clusters + unpassed current-phase criteria, ranked at weekly review.

### 8.2 Quiz engine — modes

- **A. Recall** (objective answers; Claude checks hard): correspondences, 干支 arithmetic, 藏干, dates, trump orders, history theses. Sourced from `systems/` records + corpus. Daily micro-dose via FSRS flashcards; weekly batch in review.
- **B. Teach-back** (plan instrument #4): 2-minute recorded explanations (the Dummett thesis; where 五行/elements breaks). Claude prompts, times, and asks Socratic follow-ups; the pass judgment is the researcher's own + mentor's.
- **C. Interpretation practice against documented references** (new): Claude presents an example's spread/chart *without* its published reading → researcher reads → Claude reveals the reference and produces a **structural comparison** ("you anchored on X; the published reader anchored on Y's Z; you missed the reversal") plus hard flags on factual errors (wrong correspondence, wrong 十神). The comparison key is a documented human reading, never Claude's. Divergence from the reference is *data*, not failure — noted, and interesting divergences go to `questions.md`.
- **D. Cross-lens perspective** (new — the researcher's blind-spot request): "How would another school/system approach this?" answered **strictly from documented positions** — corpus notes, example-bank entries by school, school profiles from phase0 work. Rules:
  - Sourced or labeled: an answer either cites its documentation or is explicitly marked "general characterization, unsourced" and **auto-appended to `questions.md`** for verification. No silent improvisation of what 盲派 or Marseille "would say" — a fabricated school position is the same failure mode as a fabricated quote.
  - **Bleed-gated:** cross-lens sessions are a *separate, scheduled activity* (plan file 05's rule: comparison is a third activity), never mixed into same-day practice of either system, and paused entirely if a contamination warning sign fires.
  - Outputs feed `comparative-table.md` — this mode is the table's raw-material generator.
  - Honest expectation: this mode's power grows with the corpus. Early on the frequent answer is "not documented yet → queued," which is the loop working as designed.
- **E. 错题本-targeted drills:** generated from error clusters; results update the skill map.

### 8.3 Cadence

| When | What | Time |
|---|---|---|
| Daily | 3-card draw + journal (unchanged, protected above all); FSRS micro-review; one recall prompt | ≤ 5 min beyond the draw |
| Weekly | **Review session** (Claude-driven): resolve due predictions; metrics → STATUS.md; 未考 sweep → proposed queue tasks; questions.md triage; tag registry upkeep; short mixed quiz (A/B/E); skill-map update + next-week focus recommendation; validator run; commit | ~30 min |
| Biweekly | Pre-mentor prep: stuck-list assembled from journal (plan §9, automated); post-session brain-dump reminder + day-2/7/14 spaced review scheduling | ~10 min |
| Monthly | Blind production test administered (instrument #1); one cross-lens session (mode D); calibration snapshot | ~45 min |
| Phase boundary | Full exit-criteria audit off the skill map; re-plan next phase (files are living); Tier-2 review of any boundary/rule changes | session |

### 8.4 STATUS.md — the unified monitor

One page at repo root covering both engines, **regenerated by Claude, read by the human** (hand-maintaining a dashboard is the anti-pattern; the truth already lives in frontmatter, queue files, and the skill map — STATUS.md is a compiled view of it). Sections:

1. **Study:** current phase + criteria passed/open (from `skills.md`), **reading tracker** (current inside/outside books per system with progress, next up — compiled from literature-note frontmatter `status: reading, progress: ch N/M`), predictions due/overdue, 未考 count, daily-habit streak, last-review date.
2. **Research:** queue snapshot (todo/blocked, study-originated flagged), last session + type, unmerged Tier-2 branches awaiting review.
3. **Loop health:** open questions count, answers written back this cycle, promotions pending.
4. **Next actions:** the ranked focus list (stale skills, due reviews, next authorized research task).

Regeneration points: every weekly review, every research-session close, and on demand ("where am I?"). Because it is compiled, it can never silently drift from reality — and the compilation is itself validated (a STATUS claim with no backing file fails the check).

**Archive:** on every regeneration, the outgoing STATUS.md is snapshot to `log/status-archive/YYYY-MM-DD.md` before being replaced — a greppable progress-over-time record without git archaeology (git history remains the canonical backstop; the archive is the convenient view of it).

**Marking daily completion without Claude:** the daily note template carries three frontmatter booleans — `did_draw`, `did_reading`, `did_fsrs` — toggled with one tap in Obsidian's properties panel (mobile included); the note's existence already implies the draw happened. An **Obsidian Bases view over `journal/daily/`** gives a live this-week habit table with zero Claude involvement; the weekly review then compiles the same booleans into the STATUS streak. Truth in the daily files, two views over it — nothing to maintain by hand, nothing requiring a session.

**When to come to Claude — the honest division:**

| Cadence | Come to Claude? | Why |
|---|---|---|
| Daily | **No** — by design | The daily ritual (draw, journal template, FSRS cards, one recall prompt) is deliberately Claude-free. Protecting a friction-free daily habit is worth more than any daily optimization; the template already tells you what to do. |
| Weekly / biweekly / monthly | **Yes** — these ARE Claude sessions | Review, mentor-prep, quiz batches, blind-test administration, cross-lens sessions are Claude-driven by design (§8.3). |
| Anytime | **Optional** | "What's next?" / "Where am I on X?" — answered from STATUS.md + skills.md + queue in seconds, any session, no ceremony. Every session I open on this repo starts by reading STATUS.md (file 07's rule), so orientation is automatic. |
| Scheduled (opt-in) | Claude comes to **you** | This environment supports scheduled Routines: a weekly firing that opens the review session and pings you, a biweekly mentor-prep reminder. Off by default — enable when the habit is stable, not before (07 §6: habit before tooling). **Standing follow-up:** revisit enabling these ~4 weeks after migration (≈ late Aug 2026); carried in STATUS.md next-actions until resolved. |

### 8.5 Perspective boundaries — what Claude is and is not

**Is:** coverage auditor (cards never drawn, nodes untested, claims 未考), consistency checker ("your March note says X, yesterday assumes Y — reconcile," with dates, never silently picking), vagueness detector (unfalsifiable-as-stated predictions flagged before logging), Socratic examiner, structural comparator against documented readings, retriever of documented school positions.
**Is not:** a judge of whether a reading is *right*, an author of interpretations, a source of school positions beyond what is documented — and never a generator of classical quotes from memory.

---

## 9. Tooling stack & roadmap

**Now (no database):** Obsidian at repo root; **core features only** for structure — Bases for dashboards/tables over frontmatter, properties, native search; plugins limited to Spaced Repetition/FSRS (job: retention) and optionally Breadcrumbs (job: browsing typed chains). Dataview/Datacore explicitly avoided as foundations (maintenance risk). Claude Code operates on the same files: weekly review, quiz generation, validation, ad-hoc corpus queries.

**Trigger-gated build (spec'd now, built only when a trigger fires):** derived **SQLite index** — `nodes(id, type, system, title)`, `edges(from_id, to_id, type, source, note)`, `readings(id, date, outcome, falsifiable)`, `reading_cards(reading_id, card_id, misread)` — indexed from/to columns, recursive-CTE traversal helpers, built entirely FROM frontmatter, git-ignored, rebuildable from scratch. Triggers: (a) recurring multi-hop questions ("all cards whose decan ruler is Mars that appeared in misread readings"); (b) need for repeatable integrity checks across a now-large corpus; (c) real calibration analytics (Brier score by phase/system) over hundreds of predictions.
**Not built, ever, absent extraordinary cause:** a standalone graph DB, RDF/OWL, a custom SR engine, a capture app. The dominant risk is tool-building as procrastination; triggers are the guardrail.

---

## 10. User-experience walkthroughs

**A morning (2 min + the draw).** Phone or paper → daily note from template. Cards linked `[[Three of Swords]]`. One falsifiable prediction line. Done — no rigor, no Claude.

**A study session (Obsidian).** Reading 千里命稿, you hit a 十神 assignment that seems to contradict your teacher's method. Open `systems/bazi/shishen-…`: the record shows `basis: 未考` on that point. One line in `questions.md` ("千里命稿 lecture N vs 老师 on X — which is 子平 orthodox?"). Keep reading. Total detour: 40 seconds.

**A weekly review (~30 min, Claude-driven).** Claude: "Two predictions due — outcomes? … Logged: 1 hit 1 miss; calibration updated. This week's 未考 sweep found 4 unsourced claims; your questions.md has 3 entries. Proposed queue tasks: one `intake:` (千里命稿 lecture N — also seeds the example bank), one `audit:` (GD decan attribution origin), one deferred. Approve? … Quiz: 6 recall items (2 missed → skill map: 藏干 stays *learning*), one teach-back prompt. Next-week focus: 藏干 drills + the 排盘 criterion — it's the last P1 node untested. Committing."

**A research session closing the loop (separate hat).** Queue task `intake: 千里命稿 lecture N` runs under full ritual — tests, source into `/sources/`, note in Chinese, provenance schema. Closing step: your study record's `未考` flips to a verified citation; `questions.md` marks the question answered. Next Obsidian session, the answer sits inline where you first hit the gap. If the claim died instead: `/log/dead-ends.md` entry, 错题本 links it.

**A monthly cross-lens session (mode D, scheduled, separate).** "This month's case: case-2026-004. Documented positions on this chart shape: 子平 profile says A (cite); 盲派 — nothing in the corpus yet; general characterization would be B — **unsourced, queued for verification**. Contrast worth a table entry?" → `comparative-table.md` gains a row with an explicit break-point; one line lands in `questions.md`.

**A phase boundary.** Skill map shows P1: 6/7 criteria evidence-linked; blind production passed twice. Claude assembles the exit audit; you and your mentor make the call ("am I there yet?"); P2 file is re-planned from what actually happened; Tier-2 commit records the boundary.

---

## 11. Governance

- **Commit prefix `study:`** added to the constitution's conventions (Tier-2 amendment). Study-only commits are exempt from the one-queue-task session ritual (a journal commit is not a research session) but still run the test suite (validator included, cheap).
- **Tier 1:** all study leaf content — journal, cases, examples, quizzes, systems records, questions, working-table entries, reviews.
- **Tier 2:** this document, RULES.md, the boundary rules, skill-map *structure*, constitution amendments, and every promotion into the corpus (which lands under corpus rules anyway).
- **Firewalls restated in one place:** (1) study material is never a verified source; (2) interpretive practice data is never research evidence; (3) unsourced school characterizations are labeled and queued, never asserted; (4) the derived index is never edited directly; (5) `/views/` artifacts are never truth.

## 11a. Updates to the research engine itself

The corpus's constitution is unchanged in substance, but integration touches the research side in seven places:

1. **Task provenance:** queue task files gain an optional `origin:` field (e.g. `origin: study/questions.md#2026-07-30-a`). The **session-close ritual gains one step**: if the completed task has a study origin, write the answer back (flip the `未考` tag, mark the question resolved) before committing. This is what makes the loop close mechanically rather than by memory.
2. **Queue discipline:** study-originated tasks enter as proposals at weekly review — they do **not** jump the queue; the researcher still authorizes what runs, and the one-task-per-session rule is untouched. Demand from the study side informs priority; it never overrides it.
3. **Intake sessions gain a light secondary output:** when a source contains worked examples (千里命稿's 命例 are the immediate case), the intake note also files pointers into `/study/examples/`. One extra list, no new session type.
4. **`/seeds/` gains two files:** `lenormand.md` and `易经.md` — both are now *active study* topics but not research workstreams; research-side ideas they generate get captured as seeds per §1.5 rather than expanding scope. (六爻 keeps its own seed; 占筮 practice and the 周易 text tradition are related but distinct threads.)
5. **`/comparative/` INDEX documents its inflow:** the promotion criterion (both sides source-backed) so future sessions know where mapping notes come from and what bar they passed.
6. **The validator checks both directions:** study→corpus links must resolve (no dangling citations), and corpus note ids become load-bearing — renaming a lexicon entry now breaks study records, so id stability is enforced, not just conventional.
7. **Phase-0 gains a concrete consumer:** cross-lens mode (§8.2 D) is only as good as the school profiles — `phase0-001` (流派 enumeration) and the profile fan-out are now the highest-leverage research tasks for the study engine, which is worth weighing when authorizing the first depth session.

## 12. Migration plan (executes on approval as `study-001`)

1. Move `plan/00–07` from `inbox/` to `study/plan/`; retire the inbox.
2. Write `RULES.md` (language rules, templates, tag registry seed, frontmatter conventions, SQLite schema v1 + triggers, cadences) and `skills.md` seeded from Phase 1 exit criteria — several likely already passed given the headstart; first weekly review tests them.
3. Generate the first root `STATUS.md` (both engines, per §8.4); create `log/status-archive/`. Daily template includes the `did_*` completion booleans + a Bases habit view spec.
4. Create `journal/`, `cases/`, `examples/`, `quizzes/`, `reviews/weekly/`, `systems/*` with INDEX stubs + templates; `questions.md`, `comparative-table.md`, `错题本.md`.
5. Amend CLAUDE.md: `study:` prefix, ritual exemption, session-close write-back step, firewall pointers (Tier-2, this branch).
6. Research-engine updates per §11a: `origin:` convention documented in `/queue/INDEX.md`, seeds `lenormand.md` + `易经.md`, `/comparative/` INDEX promotion criterion, re-point `slice1-train-001/002` into the study system (still doubling as time-module fixtures).
7. Wire the frontmatter validator stub into `formal/tests/run_tests.sh` (two-way link checking).
8. Update `/queue/` and all touched INDEXes; session log; "ready for review."
