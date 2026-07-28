# /study/ Operating Rules

> Operational companion to `DESIGN.md` (rationale lives there; this file is what sessions follow). Tier 2 — researcher review before changes. Constitution (`/CLAUDE.md`) governs on conflict.

## 1. Roles

- **The assistant scaffolds, never interprets.** Organizes, counts, schedules, retrieves, validates, compares against documented references. Never drafts a reading, never supplies "the" interpretation, never generates classical quotes or school positions from memory.
- **Study sessions are not research sessions.** `study:` commits are exempt from the one-queue-task ritual but still run the test suite. Research work stays under the full constitution ritual.

## 2. Language

1. Quotes & literature notes: **source language always** (子平真诠 → Chinese, Pollack → English, Papus → French). Classical passages need a verified copy in `/sources/` or an explicit `unverified` tag — §1.2 applies inside `/study/`.
2. Insights & personal synthesis: **mixed language legitimate**; untranslatable terms stay native inline.
3. Nothing crosses into the corpus in mixed form — promotion re-tightens to corpus rules.
4. Meta-documents (plans, reviews, STATUS, this file): neutral ground.

## 3. Frontmatter conventions

- Every note: unique `id` (English/pinyin slug, canonical), `type`, `system` where applicable; native-language `title` + `aliases` for CJK-safe linking.
- **Machine-readable in frontmatter; prose in the body.** Inline `[[wiki-links]]` are navigation only — the graph is built from frontmatter fields.
- Typed edges carry provenance: `{target, source, verification}`. Edge `source:` = whose attribution (golden-dawn / muchery / 神煞…); `verification:` = corpus attestation status (`verified | unverified | 未考`).
- Every tradition-claim carries a `basis` entry: a citation into `/sources/`, `/lexicon/`, `/comparative/` — or the tag `未考`.
- **No derived data in frontmatter** (no counts, no hit rates — tooling computes those).

## 4. Tag registry

Fields = countable dimensions (controlled vocabulary, validator-checked). Tags = emergent themes. New tags are registered or merged here at weekly review. Claude may propose topic tags; judgment tags are the researcher's.

| tag | meaning |
|---|---|
| `早子时` | case/question touching the 早子时/晚子时 calendar dispute |
| `career-question` | reading/case on career matters |
| _(grows at weekly review)_ | |

Controlled vocabularies: `case_type: 命例 | historical-event | fiction | friend-reading | own-question` · `outcome/verdict: hit | miss | partial | void | pending` · `skill status: untested | learning | passed | stale`.

## 5. Templates

In `templates/` (Obsidian-usable): `daily.md`, `prediction.md`, `case.md`, `literature-note.md`. Daily note carries completion booleans `did_draw / did_reading / did_fsrs` — one tap in Obsidian properties; the note's existence implies the draw. **Bases habit view:** create a Base over `journal/daily/` with columns `date, did_draw, did_reading, did_fsrs` filtered to the current week — live habit table, no Claude needed.

## 6. Reading-time discussion (DESIGN §8.5)

Notes first, discussion second. Every substantive discussion ends with a 3–5 line harvest into the relevant note. Literature notes keep three strata unblended: **what the book says** (source-anchored, source language) / **what I think** (own voice, mixed language) / **what discussion surfaced** (marked; Claude-contributed facts are corpus-cited or labeled unsourced → `questions.md`).

## 7. Cadence

| When | What |
|---|---|
| Daily (Claude-free) | Draw + journal entry; FSRS cards; one recall prompt; toggle `did_*` |
| Weekly (Claude) | Review: resolve predictions → metrics → STATUS regeneration (archive old to `/log/status-archive/`); 未考 sweep; `questions.md` triage → queue proposals; tag registry; short quiz; skill-map update + focus ranking; validator; commit |
| Biweekly (Claude) | Pre-mentor stuck-list from journal; post-session brain-dump + day-2/7/14 review scheduling |
| Monthly (Claude) | Blind production test; one cross-lens session (bleed-gated, documented positions only); calibration snapshot |
| Phase boundary | Exit-criteria audit off skill map; re-plan next phase; Tier-2 review |

## 8. Quiz modes (DESIGN §8.2)

A recall (objective, checked hard) · B teach-back (Socratic, researcher/mentor judge) · C interpretation vs. documented reference (comparison key = a published human reading, never Claude's; divergence = data) · D cross-lens (documented positions only; unsourced characterizations labeled + auto-queued; separate scheduled activity, paused on contamination signs) · E 错题本-targeted drills.

## 9. Derived index — spec, trigger-gated (do NOT build early)

SQLite, rebuilt entirely from frontmatter, git-ignored: `nodes(id, type, system, title)` · `edges(from_id, to_id, type, source, note)` (index from/to) · `readings(id, date, outcome, falsifiable)` · `reading_cards(reading_id, card_id, misread)`. Recursive-CTE traversal helpers. **Build only when a trigger fires:** recurring multi-hop questions; repeatable integrity checks over a now-large corpus; calibration analytics over hundreds of predictions. Never: standalone graph DB, RDF, custom SR engine, capture app.

## 10. Firewalls

1. Study material is never a verified source.
2. Interpretive practice data is never research evidence (cases: `fixture_eligible` covers only the objective computational content, anonymized + reliability-flagged).
3. Unsourced school characterizations are labeled and queued, never asserted.
4. The derived index is never edited directly.
5. `/views/` artifacts are never truth.

## 11. Tiers

Tier 1: journal, cases, examples, quizzes, systems records, questions, working-table rows, reviews, STATUS regenerations. Tier 2: DESIGN.md, this file, skill-map structure, boundary rules, promotions into the corpus.
