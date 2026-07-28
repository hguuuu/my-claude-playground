---
task_id: study-001
type: intake
tier: 1
status: blocked
depends_on: [researcher upload to /study/inbox/]
lang: en
date_added: 2026-07-28
component: study/intake
---

# study-001 · Process the first `/study/inbox/` upload

**One line:** Read what the researcher actually uploaded to `/study/inbox/`, file it under `/study/` with a structure that fits the material, and open follow-on `/queue/` tasks — without doing the research itself.

## Deliverable
- Uploaded files filed under `/study/` (structure decided from the content, not guessed beforehand).
- `/study/INDEX.md` contents table updated.
- New `/queue/` task files for any real research work the material implies — one unit per task (§8).
- Out-of-scope material appended to the matching `/seeds/` file (§1.5).

## Done-when
- `inbox/` contains only things not yet looked at.
- Every follow-on is a queue task, not work done inline.

## Notes / guardrails
- **Do not treat course material as a source.** Anything it quotes from a classical text is `verification: unverified` until a copy lands in `/sources/` and an `audit:` session checks it (§1.2).
- **Language policy holds** (§1.1): 八字 study notes in Chinese, astrology in English. No summarizing one tradition in the other's language.
- Split this task if the upload turns out to cover more than one tradition — one intake task per tradition, per §8 granularity.
- Tier 1 (additive leaf content), but any change to the boundary rules in `/study/INDEX.md` is Tier 2.
