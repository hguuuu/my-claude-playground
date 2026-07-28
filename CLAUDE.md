# CLAUDE.md — Operating Rules

> Distilled from PROJECT_BRIEF.md (which governs on any conflict). Read that brief for reasoning, schemas, and sequencing. This file is Tier-2: never modify without researcher review.

## What this repo is

A long-horizon research system: 八字命理 (Chinese corpus), Western astrology (English corpus), tarot (parallel), with a shared computational layer. A garden, not a project — it never needs to be finished; it must never be corrupted.

## Constitution — non-negotiable

### Language: NO TRANSLATION

- Every note is written in the language of its source tradition. 八字 → Chinese. Astrology → English. No exceptions.
- Never paraphrase a Chinese source in English or vice versa — not in notes, logs, or commit messages about that content. 八字 session logs are written in Chinese. Engineering-session logs may be in either language (the formal layer is neutral ground).
- Why: **火 ≠ fire.** 火 is a symbol in the 生克 cycle system; “fire” carries Greek elemental baggage. Translation is where distortion enters.
- Cross-language contact happens ONLY in `/comparative` mapping notes — each side quoted in its own language, relationships analyzed, never equivalence claims.

### Citations: verified sources only

- NEVER cite a classical passage unless a verified copy exists in `/sources/`. No reconstructing quotes from memory — this is the project’s worst failure mode.
- Web-researched claims are tagged `verification: unverified` until checked against a primary text in an audit session.
- Always distinguish 原文 / 后世注释 / modern interpretation. Never present a commentary layer as the original.

### Testing: CS discipline everywhere

- Run the full test suite at session start and before every commit. No commit with failing tests.
- Every table (万年历, 节气, 干支 cycles, timezone history, ephemeris) and every formula has tests, including cross-validation against independent published sources.

### Statistics: exploration never grades its own homework

- Exploratory correlation runs → `/formal/exploratory/`, logged freely.
- Interesting patterns → promoted to `/formal/hypotheses/` with a precisely stated claim and pre-specified test, then tested on data they were NOT discovered in.
- Record whether a claim is testable as stated before asking whether it is true.

### Scope: seeds, not creep

- Out-of-scope encounters (风水, 六爻, 紫微斗数, 七政四余, tarot ideas, stray resources) → append to the matching file in `/seeds/`, then return to the task.

## Session ritual — every session, no exceptions

**Open:** read this file → read `/STATUS.md` → read the last few entries in `/log/sessions/` → run the test suite → take exactly ONE task from `/queue/`.
**Close:** write a session log entry (what, why, decisions, next) → **if the task has a study `origin:`, write the answer back** (flip the `未考` tag in the study record; mark the question resolved in `/study/questions.md`) → update `/queue/` → regenerate `/STATUS.md` (archive the outgoing copy to `/log/status-archive/`) → commit per the rules below.

Task granularity: one term, one source, one chapter. Never large enough to half-finish ambiguously.

Session types (prefix log + commit message):

- `phase0:` survey/mapping work
- `intake:` process ONE source — extract, tag provenance (schema in brief §3), file notes
- `synthesis:` write across existing notes ONLY; no new claims from memory
- `engineering:` formal layer; tests mandatory
- `audit:` re-verify earlier citations/claims against `/sources/`; clear or flag `unverified` tags
- `study:` study-system activity (`/study/` — journal, reviews, quizzes, cases). Exempt from the one-queue-task ritual; still runs the test suite before commit. Governed by `/study/RULES.md`.

Negative results (disproven rules, misattributions, failed leads) → `/log/dead-ends.md`. High value; never silently drop.

## Commits — semantic, two tiers

Commit = one completed task: content + session log + queue update, referencing the task ID. Message prefixed with session type; 八字-content commits written in Chinese.

- **Tier 1 (auto-commit to main):** additive leaf content — source notes, lexicon entries, seed appends, logs, exploratory analysis.
- **Tier 2 (branch + researcher review):** load-bearing changes — foundational tables, time module, rule specs, `/foundations/boundary.md`, this file, the brief, provenance schema, hypothesis promotions. Open a branch; end the session log with “ready for review.”

## Study system (`/study/`)

The researcher's learning engine, integrated per `study/DESIGN.md` (Tier-2), operated per `study/RULES.md`. Constitution-level facts: **study material is never a verified source; interpretive practice data is never research evidence; study content enters the corpus only by promotion — written fresh from verified sources.** The assistant scaffolds study work, never interprets. Study→research questions flow through `/study/questions.md` into `/queue/` (task `origin:` field); answers are written back at session close. Root `/STATUS.md` is the generated two-engine dashboard.

## Key structural facts

- Canonical knowledge lives in plain text. `/views/` holds generated interactive artifacts only — never edit knowledge there.
- Rules are first-class entities in `/formal/specs/` with many-to-many attestation lists (brief §4); convergent attestation is 可考 evidence.
- Evaluation uses four independent axes, never collapsed: 可考 attestation / internal coherence (可修复) / cross-system convergence / empirical status (brief §5).
- Keep every directory’s `INDEX.md` current — indexes are how sessions orient without reading everything.