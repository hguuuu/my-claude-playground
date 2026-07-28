# Study System, Journaling & Knowledge Base Maintenance Plan

*Companion to the study plan. Architecture principle: **files are truth; chats are ephemeral.***

## 1. Architecture (where things live)

| Layer | Role | Not its role |
|---|---|---|
| **Markdown repo / Obsidian vault (git)** | Single source of truth: status, checklists, journals, records, notes | — |
| **Claude.ai Project** | Discussion, research, lesson prep; project memory = *continuity only* | Storage/record |
| **Claude Code on the repo** | Maintenance engine: weekly reviews, status updates, analytics, spaced repetition | Interpretation |
| **MCP connectors / agents** | Optional later convenience (direct vault access from Claude.ai) | A new source of truth |

**Conversation hygiene:** one conversation per topic/session, never mega-chats; new chat at topic change or sluggishness; project memory bridges. After substantive Claude.ai sessions, paste a 3–5 line takeaway into the relevant repo file. In Claude Code, `/clear` between tasks; commit after every meaningful unit of work.

## 2. What gets recorded, why, and how it's used

| Record | What it contains | Why needed / used for |
|---|---|---|
| **STATUS.md** | Current phase, active foci, exit-criteria checkboxes, metrics, next actions | The dashboard; first thing read every session; the *assessment instrument* for phase completion |
| **Phase files** (`plan/phases/`) | Goals, books+rationale, practice, exit criteria as `- [ ]` | Phase-start orientation; criteria checked off as passed; re-planned at boundaries |
| **Daily draw journal** (`journal/daily/`) | 3-card timeline draw: cards, pre-book interpretation, book/mentor comparison, prediction, outcome | Retrieval practice + the application-skill feedback loop; raw material for per-card history |
| **Prediction log** (`journal/predictions/`) | Falsifiable claim, confidence, resolve-by date, outcome status (frontmatter) | Calibration evidence — the anti-Barnum instrument; machine-countable hit rate |
| **Per-card / per-十神 / per-hexagram / per-decan records** (`systems/`) | Fixed-field records: meanings, attributions (GD, Muchery — kept distinct), image notes, personal notes, links to every reading it appeared in | Correspondence backbone; spaced-repetition source; each card's note accumulates its *real-reading history* — how personal understanding grows beyond keywords |
| **Literature notes** (per book) | Own-words summaries, 2–5 sentences per idea, with source anchor | Prevent rereading; feed permanent notes; the teach-back prep |
| **Permanent notes (Zettelkasten layer)** | Atomic cross-system insights, densely linked ("神煞 derive from 三合+十二长生"; "where 五行/elements breaks") | Where the comparative project lives; finds relationships across topics/phases the folders can't show |
| **Comparative table** | Western form \| Chinese form \| where the analogy breaks | The East–West bridge artifact; the bleed-rule guardrail |
| **错题本 (error log)** | Misjudged 命例/readings, with the correction | Deliberate-practice targeting: what to drill, what to bring to teachers |
| **Weekly reviews** (`reviews/weekly/`) | Progress, resolved predictions, gaps, next actions | The maintenance heartbeat; audit trail of the whole program |
| **Lesson notes** | Post-session free-recall brain dump, reconciled with notes | Biweekly-cadence retention (day 2/7/14 reviews source from these) |

## 3. Journal templates

**Daily entry** (`journal/daily/YYYY-MM-DD.md`):
```markdown
---
date: 2026-07-27
system: tarot
type: daily-draw
cards: [Two of Swords, The Star, Knight of Wands]
positions: [past, present, future]
---
## Reading — before any book
...
## Book/mentor comparison — where I differed
...
## Prediction (falsifiable, dated)
"..." → logged in predictions/
## Outcome (filled later) + what I'd read differently now
...
```
Link every card to its note (`[[The Star]]`). Handwritten morning draws are fine — transfer prediction + outcome lines to markdown.

**Prediction entry:** frontmatter `made / resolve_by / system / claim / confidence / status(open|verified-correct|verified-wrong|void)` + basis + outcome.

## 4. Repo structure

```
divination-study/
├── CLAUDE.md            # Claude Code instructions (role: scaffold, never interpret)
├── STATUS.md
├── plan/                # these very documents + phases/
├── systems/{tarot,bazi,astrology,iching,lenormand}/
├── journal/{daily,predictions}/
├── reviews/weekly/
├── knowledge-base/      # comparative tables; later CSV/DB
└── tools/               # later: scripts
```
Start with only CLAUDE.md, STATUS.md, plan/, journal/. Add the rest when actually needed.

## 5. Tooling roadmap — functionality, purpose, development goal

**Governing rule: the assistant scaffolds — organizes, checks off, counts, schedules, retrieves — and never interprets. Every interpretation is written by me first.** The development goal is to *understand the different aspects carefully*, so each tool exists to sharpen a specific feedback or retrieval loop, not to shortcut learning.

| Stage | Functionality | Purpose / goal |
|---|---|---|
| **Now (Week 0)** | Files + daily logging by hand, no automation | Habit before tooling — the classic failure is over-engineering first |
| **Weeks 1–4** | **Weekly review procedure** in CLAUDE.md: Claude Code reads the week's entries, resolves due predictions (asking me outcomes), recomputes metrics, updates STATUS.md, writes the review, commits | Turns files into a living dashboard; enforces the verification loop |
| **Month 2+** | **Analytics script** over frontmatter: prediction hit rate, calibration by confidence, draws/week, most-frequent + most-misread cards | Objective assessment evidence (§7 of overview); focuses mentor time on weak spots |
| **Month 3+** | **Spaced repetition** over `systems/` records (expanding intervals; interleaved multi-system decks) — Obsidian SR plugin or Claude Code-built | Retention of correspondences/十神/hexagrams without rote drudgery; interleaving auto-spaces |
| **Month 3+** | **Correspondence lookup**: query a card → decan, planet/sign, Kabbalah path, Muchery card, related 神煞 note — *presented for me to interpret* | Cross-system retrieval; feeds the comparative project |
| **Later, on real friction** | Filesystem/Obsidian MCP connector (direct Claude.ai↔vault); scheduled weekly digest; knowledge-graph layer only if cross-system entity graphing outgrows linked notes | Convenience only; never a new source of truth |

**CLAUDE.md must state:** read STATUS.md first; never overwrite my interpretations; note conflicts with dates rather than silently picking; date/filename conventions; the weekly-review procedure; commit discipline.

## 6. Failure modes to guard against

- **Chat history as the only record** — compaction is lossy; memory summaries drift. Anything durable that exists only in a chat is at risk: land it in a file.
- **Fragmentation** — every new tool must read/write the same vault or it doesn't get adopted.
- **Over-engineering before habit** — if daily logging slips below ~5 days/week for 3 weeks, *simplify capture*, don't add tooling.
- **Tooling as interpretation crutch** — the moment a tool drafts a reading, the design has failed its goal.

**Upgrade triggers:** manual metric-counting becomes a chore → analytics script. Frequent Claude.ai↔repo copy-paste → MCP connector. Vault exceeds ~200 files / working-set strain → directory index files.
