---
id: decision-pr4-adoption
lang: en
type: log
source: n/a
verification: n/a
date_added: 2026-07-29
tags: [decision, meta, workstream, pr4]
---

# Decision · PR #4 adopted manually, not merged (researcher, 2026-07-29)

**Decision:** PR #4 (`claude/columbia-spirituality-program-ny7ccd`, the calibration-session branch) is **closed without merging**. Its three content files are adopted into the main workstream by hand, refined per review; its branch-specific housekeeping is redone natively. The branch is **kept alive as a reference** — do not delete it.

## What was adopted (with refinements)

1. `seeds/scientific-perspective.md` — verbatim.
2. `schools/三问互补假说.md` — refined: `type: mapping` → `rule-commentary` (mapping is reserved for `/comparative`, brief §3); adoption-provenance note added.
3. `log/decisions/2026-07-28-source-credibility-principle.md` — refined: explicit two-way cross-link with `/sources/RELIABILITY.md` added (the review had flagged the missing link).

## What was deliberately NOT adopted

- The calibration branch's phase0-001 taxonomy (`map.md`, 古法-纳音/子平-格局/新派-旺衰 dirs) — already superseded by s0005's deeper enumeration; its one caught error (新派-旺衰 conflating 旺衰派 with 李涵辰新派) is recorded here so the negative result survives on main.
- The **phase0-002 v0 output** (obtainability survey + 6 intake task definitions) — researcher had withdrawn it pending a deep-research redo. It lives ONLY at commit `8a9ccec` on the reference branch. Status: reference material for comparison, **not citable, not buildable-on**. The 002 redo runs fresh, then diffs against v0 (fresh-then-compare avoids anchoring).
- The branch's session logs s0009–s0011 and its renumber record — they document that branch's internal history; this decision file is main's record of the episode instead.

## Why not merge

The PR's content was three small files; the rest was merge-sync housekeeping specific to that branch's history (its renumbering, its retirements, its conflict resolutions). Adopting manually gives main only reviewed, refined content; keeps main's history clean of a duplicated phase0-001 run and a withdrawn 002; and lets the branch serve as an untouched parallel reference for comparison. Review verdict and both review findings: session 0009 log.

## Session-number note

The reference branch internally used numbers 0009–0011; those never entered main's ledger. Main's sequence continues from 0008 → this adoption session is main's **0009**. The dead-branch numbers are historical artifacts of an unmerged branch; the sessions INDEX convention (date+slug = identity) makes this unambiguous.
