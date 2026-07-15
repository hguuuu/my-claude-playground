# Founding Conversation Record

## Design discussion preceding PROJECT_BRIEF.md

> Date: 2026-07-12
> Participants: Haiwen (researcher) & Claude
> Purpose: Primary record of the brainstorming and design decisions that produced PROJECT_BRIEF.md. Kept in `/log/decisions/` as the origin document. Where this record and PROJECT_BRIEF.md disagree, the brief governs.

-----

## Haiwen — opening message

I’m trying to start a research project with Claude Code and we are right before setting up the repo. Let’s first brainstorm and discuss how to format and conduct this massive research project. And then let’s create a prompt that I will be providing to the CC agent with all the discussion, brainstorming, setup, proposal, and everything else (records of some of our important conversation as well for sure). This is some rough ideas I have as of right now that we can work on top of.

### Attached rough notes (founding ideas, verbatim)

1. The goal of the research and continuous learning process is to 八字（later expanding to 风水and八卦六爻 etc）and tarot + astrology （reading natal chart etc）. This will be a multi-language research and learning process, and I’m interested in researching in different languages since that would best capture the cultural influence more accurately
1. The first three topics I am starting on will be 八字 tarot and charts.
1. For each topic I will need historical/background research first because these will be crucial understanding the details later on. These all evolved with culture, some changing from time to time and some remained. The ways to understand and interpret them is very different from time to time/culture to culture/society to society, etc
1. This will be especially important for 八字。传统命理八字在发展过程中曾经过很多变化，也拥有多个流派。但是每一个流派本质上都是基于原始的10天干+12地支的不同排列组合，在其中寻找各类不同的规律和解读方式。不同流派更多是来自于对于不同关系和关系组合的理解。it is thus fairly important to look at it as a math/stats/technical perspective and conduct part of the experiment in a very ML/CS/foundational science way. There should be rigorous way of interpreting them, but a lot of research will be needed before coming into conclusion. 因此需要先对八字有基本知识，然后再针对每一个流派或者说不同流派中不同的方法进行理解以及重新整合。我们当然需要一些基本research来决定这个boundary画在什么地方，哪些是shared knowledge是所有具体解读的building blocks，哪些是可一个个分开研究的topic。而且不同流派以及不同的解读方式在历史进展过程中留存程度也有所不同，我们还需要针对不同方法的可靠性&可考&可修复性进行简单的evaluation，这就需要一个初步的research和sourcing。而且这些了解的过程中我们也会开始和风水&六爻易经有所重合，于是可以慢慢pull out common内容。这里的重合并不是指的具体内容，而是那些”concept”（大量内容其实有被总结写成类似周易道德经四书五经等等的文字，但是历史变化文化文字的演变社会环境的变化，很多文字需要被在现代社会用新的语言，甚至是数学统计计算机这些designed to be less ambiguous的语言被重新理解，思考，然后也许应用）。另外我们还需要进行一些文字演变的学习。比如金木水火土在这里更多是作为一个”符号”使用，那为什么用的是这两个文字呢？对于出现的所有名字名词都需要做演变的research来更好地理解。
1. We can maybe go to astrology/charts next since this will be a more relevant topic. This is also “reading” on “time” and stars. To be fair this will be closer to 七政四余/紫微斗数, which we will be get to as well later on. However let’s treating it as the next topic for now since there are more documentation/books/research materials regarding charts and astrology in general. There are different styles of chart reading, and then a lot of symbols and “mythology” which are very important knowledge since they are, similar to what mentioned before for 八字, a part of word&cultural evolution that leads to today’s understanding. I’m taking a chart calculation course right now and I think this is a good place to start understanding what charts are and how stars work. Different tables and calculations, 3D simulations and other visual formats, concepts and ideas shared with or different from eastern ones we discussed earlier will be very important and crucial here. The two methods should be similar but complementary, and the challenge here is to learn astrology in a similar scientific way as discussed in the previous item, and then identify what & how much are similar or different to the bazi interpretations. I want to also make a note here that the language usage (English or Chinese or any other commonly used language in the field) should all be carefully preserved and studied since they all make minute but significant differences.
1. Now Tarot. Tarot is a slightly different story here. While the previous two are trying to explain/interpret the world into symbols, “translations”, and relations (maybe more that I didn’t carefully narrate here), tarot is more of “creating” a large enough world that hopefully contains everything natural or supernatural that human can sense. The building of this tarot world (just like designing a tarot deck) will be a very comprehensive task and related to psychology. I think this is more of something that we should discuss in a long run, especially since our knowledge will be rapidly evolving with the research from the two previous topics. This will be parallel workstream because it is very helpful to sometimes step out of those intricate details and try to look at things from a very specific, human-oriented (or how about human concern oriented)

-----

## Claude — initial architecture proposal

The failure mode for something this big isn’t bad research — it’s context loss and drift across CC sessions.

**Two-layer repo, not one.** Layer one is the knowledge corpus: bilingual markdown notes with strict provenance metadata (source, language, era, 流派, reliability rating). Layer two is computational: Python encoding of the formal structures — 10 天干 × 12 地支, pillar construction, relation operators (合冲刑害, 十神, 旺相休囚死 as a season-indexed function). The key insight in note 4 is exactly right: every 流派 is a different *rule set over the same combinatorial base*. Encoding the base as data structures early makes each school a comparable, testable set of functions rather than prose. Same pattern later for astrology (Swiss Ephemeris for calculation, aspects as relations), which sets up cross-system comparison.

**Directory structure should mirror epistemic boundaries:** `/foundations` (shared building blocks — calendar math, 干支, 五行), `/schools` (one folder per 流派 with rules, sources, evaluation of 可靠/可考/可修复), `/lexicon` (etymology workstream — one file per term, tracking character evolution, why 金木水火土 as symbols), `/formal` (code), `/comparative` (bazi ↔ astrology mappings, later concept pulls into 易经/风水), `/tarot` (parallel workstream), `/log` (decision records + research journal).

**CC-specific pieces where most people under-invest:**

- A `CLAUDE.md` acting as project constitution: methodology rules (“never translate-and-discard,” “every claim gets a source tag,” “distinguish 原文 / 后世注释 / modern interpretation”)
- Custom skills for repeatable workflows: source intake, term etymology research, school evaluation rubric
- ADR-style decision records, since CC sessions are stateless — each session reads the log, does bounded work, writes back what it decided and why
- A task queue as markdown files so “what’s next” survives across sessions

**Methodological flag:** for the rigorous/statistical ambition, write down early what counts as evidence. Internal consistency of a school, historical attestation, and predictive claims are three very different evaluation axes — conflating them is where this kind of project gets muddy. Make that rubric one of the first artifacts.

**Questions asked:** How will CC get source material? (Answer: both web research and researcher-fed materials.) Primary end goal? (Answer: all of personal knowledge system / reading tooling / publishable research — evolving.) Note format preference? (Answer: to be discussed — see next section.)

-----

## Haiwen — on note formats

Let’s discuss this. I think different content might be more suitable for different note format. In addition to the proposed ideas, some might even be helpful to be interactive (or website like html etc).

## Claude — mixed-format design

Agreed — mixed formats is right, with one firm principle: **canonical content lives in plain text (markdown + structured data); anything interactive is a generated view, never the source of truth.** If HTML pages become where knowledge lives, diffability is lost, CC can’t edit reliably, and content forks. Generate views from data; regenerate anytime.

The mapping:

- **Markdown with YAML frontmatter** — sources, research notes, essays, decision logs. Frontmatter carries the provenance schema, making everything greppable and queryable without a database.
- **Wiki-links within markdown** — for the lexicon/etymology layer where the value is cross-linking (庚 → 五行 → 旺相休囚死 → seasonal tables). Obsidian-compatible `[[links]]` are plain text: graph without lock-in.
- **JSON/YAML rule specs** — 流派 rules and relation definitions as structured data with markdown commentary alongside. This makes schools comparable and testable: the Python layer consumes specs directly, so “how do 子平 and 盲派 differ on this chart” becomes computable.
- **Python + notebooks** — pillar construction, relation algebra, ephemeris calc, statistical evaluation.
- **Generated HTML/React** — 干支 relation graphs, seasonal qi-strength visualizations, natal chart wheels, side-by-side school comparisons. Build artifacts in `/views`, produced by scripts from specs and lexicon. Also where 3D/visual astrology course material lands.

This degrades gracefully: day one needs only markdown + frontmatter; specs, code, and views come online as workstreams mature, without restructuring.

-----

## Haiwen

What are some other things that I’m missing here? Let’s discuss some of the evidence rubric and session scoping?

## Claude — gaps, rubric, session design

**Gaps identified:**

1. **The calendar problem.** Deserves its own foundational module, built early. Pillar construction depends on 节气 boundaries (not lunar months), 真太阳时 vs. clock time, timezone history, calendar reforms. Several famous inter-school disputes are calendar disputes in disguise — the 早子时/晚子时 debate being the classic. Computationally exact time is prerequisite to everything, and the first concrete win for the formal layer.
1. **Citation verification against hallucination.** The single biggest operational risk: LLMs fabricate classical Chinese quotes very convincingly. Hard rule: CC may never cite a classical passage unless a verified copy exists in the repo (ctext.org, scanned editions, researcher-provided). Web-researched claims tagged `unverified` until checked.
1. **A canonical term table.** Without it, terminology silently forks across sessions. The lexicon does double duty: etymology research and enforced consistency.
1. **A dead-ends log.** Negative results (“this claimed rule is a 20th-century invention misattributed to 三命通会”) are among the most valuable findings and the first thing lost across sessions.
1. **A test chart bank.** Anonymized charts with reliability flags (historical birth data is often shaky) for testing rule implementations and comparing school outputs.

**Evidence rubric — four independent axes, never collapsed:**

1. **Attestation (可考):** primary text existence, dating, authorship disputes (滴天髓 as prime example), how many commentary layers between original and modern version — are we reading 原文 or 任铁樵’s annotations?
1. **Internal coherence (可修复):** self-consistent? complete (output for every chart, or ad hoc judgment required)? deterministic, or smuggling in reader discretion? Fully computable once rules are in spec form.
1. **Cross-system convergence:** independent traditions arriving at structurally similar concepts is signal about shared human observation — tracked separately from truth claims.
1. **Empirical status:** deliberately separate and honest. Record whether a claim is testable as stated (Barnum/base-rate concerns) before asking whether it’s true. Rigorous position: document what the system says with precision; stay agnostic on prediction until a real test is designed.

**Session scoping:**

- Every session: read `CLAUDE.md` → read last N log entries → pick one task from queue. End: write ADR-style entry, update queue, commit with task ID.
- Session types with different rules: *intake* (one source, extract, tag provenance), *synthesis* (write across existing notes only — no new claims from memory), *engineering* (formal layer), *audit* (re-verify earlier citations against source files — what makes the corpus trustworthy over time).
- Task granularity: one term, one source, one chapter. Never half-finish ambiguously.
- Index file (map-of-content) per directory for orientation without reading everything — context-budget management.

-----

## Haiwen — three directives

1. The entire 八字 project should be researched and documented without translation. There should not be any translation in this research. We need to be very careful on how to maintain the credibility of the two languages.
1. Agreed the calendar problem is big; a foundational module at the beginning is a great idea. I also need to go through thorough timezone/time-conversion calculation and timetable-usage training for chart calculation at the beginning.
1. Is this too big a scale of project? There is much shared information, so we want to be careful how we structure and maintain it.

## Claude — language policy, calendar module, scale

**No-translation policy — a cleaner design.** Rule: every note is written in the language of its source tradition. 八字 corpus in Chinese, astrology corpus in English. Consequences:

- The lexicon becomes a **concept registry**, not a bilingual glossary: each entry in its native language; cross-system connections are explicit *mapping notes* (“structurally analogous in X way, divergent in Y”) — never equivalence claims. More honest: 五行 ≠ “elements”; forcing translation is exactly how distortion enters.
- `/comparative` is the only place both languages coexist — quoting each side in its own language, analyzing the relationship.
- The formal layer is the true bridge: pinyin identifiers allowed, semantics defined by spec files pointing to native-language sources. Code as language-neutral common ground — fitting the math-as-disambiguation instinct from the founding notes.
- Constitution rule: CC never paraphrases Chinese sources in English or vice versa, even in commit messages or logs. 八字 session logs in Chinese.

**Calendar module — one module, two clients.** 真太阳时, timezone history, ΔT, Julian day arithmetic, sidereal time serve both pillar construction and natal chart calculation. First engineering milestone: a time module with a test suite of known-tricky cases (LMT-era births, China timezone unification, DST edges, 节气-boundary births). Ideal first vertical slice because it is fully verifiable — right answers exist. Researcher’s course training maps directly onto it.

**Scale: too big as a project, fine as a garden.**

- Depth-first, not breadth-first: structure holds full ambition from day one; work proceeds as narrow vertical slices (time module → pillar construction → 旺相休囚死 as computable function → one school’s rules from one primary text), each independently useful and complete.
- Shared things built exactly once, with stricter quality bars (foundations, lexicon, time module, provenance schema). School research is additive leaf content.
- A `not-now.md` as scope control (later upgraded to `/seeds/` — see below).
- The session ritual is itself the scale defense: bounded tasks, written state, no session needs the whole project in its head. A garden doesn’t need to be finished; it needs to never be corrupted.
- Concrete milestone: end-to-end slice #1 = time module + pillar construction verified against course materials and known charts.

-----

## Haiwen — five refinements

1. Very important to highlight that 五行 does not equal elements, because fire and 火 are two different symbols!
1. The formal layer is an interesting middle ground: statistical comparison across systems becomes possible — interesting correlations can trigger later rounds of research!
1. Love the calendar module — but apply CS design principles to maintenance of all modules and formal layers. Keep testing suites to ensure validity of tables and formulas at all times!
1. Depth-first yes, but before digging deep we need a rough idea of the other possibilities to avoid fundamental misunderstanding, since 八字 resources are intertwined. Preliminary research on the general options with rough ideas of each, grouped and articulated correctly, then go deeper. If an extracted rule is used across multiple resources, record that.
1. Keep `not-now.md`, but also allow jotting notes/questions/resources encountered, so when we move to a topic we have starting points and pre-listed questions.

## Claude — consequences of the refinements

1. **火 ≠ fire goes in the constitution as the canonical example** — 火 is a symbol within a generative/conquest cycle system; “fire” carries Greek elemental baggage. One sentence that justifies the entire no-translation policy to any future session.
1. **Statistical comparison with a guardrail:** many correlations across two rich symbol systems will produce impressive-looking patterns by chance (multiple comparisons). Workflow: exploratory runs welcome and logged; anything interesting is promoted to a *hypothesis file* — stated precisely, tested on data it was NOT discovered in (fresh charts from the test bank). Exploration triggers research rounds; it never grades its own homework. Exploratory vs. confirmatory is cheap to enforce structurally and makes eventual findings mean something.
1. **Testing as standing infrastructure:** every table (节气 boundaries, 干支 cycles, ephemeris outputs) and formula gets a suite; CC runs the full suite at session start and before every commit. Cross-validation against independent published sources. CI discipline even if it’s just a script.
1. **Survey-before-depth becomes Phase 0:** enumerate major 流派 and method families; one-page profile each (core premise, key texts, shared material, preliminary 可考 impression); draft the **boundary document** (shared bedrock vs. school-specific — the question from the founding notes). The map is allowed to be wrong and gets revised by depth-work; it prevents mistaking one school’s convention for universal foundation. The shared-rule point implies **rules are first-class entities with many-to-many source links**: a rule spec carries its own attestation list (appears in 渊海子平 ch. Y, restated in 三命通会 ch. Z, modified by school W). Convergent attestation is itself 可考 evidence — recording it feeds the rubric.
1. **`not-now.md` becomes `/seeds/`** — one file per future topic (风水, 六爻, 紫微斗数, tarot-world), accumulating notes, questions, resource links. Constitution rule: out-of-scope encounters get appended to the seed file, then move on. When a topic activates, its seed file is the Phase-0 starting brief.

-----

## Haiwen — commit structure question

1. Love the statistical guardrail — the hypothesis step is crucial!
1. The one-pager and boundary document will be super helpful; Phase 0 can be wrong, and some layers are designed to be “allowed to be updated as research goes on.”
1. How do we structure commits? Should I initiate them, or make it automatic (after a defined number of changes)?

## Claude — semantic commits, two trust tiers

Neither pure option — the right unit is **semantic, not volumetric or manual**. “Every N changes” produces meaningless commits; researcher-initiated everything creates a bottleneck.

**Commit = completed task.** Content change + session log entry + queue update sealed together, referencing the task ID. Every commit is a self-describing research event; `git log` becomes a secondary research journal. Tests must pass before any commit.

**Two trust tiers:**

- **Tier 1 — auto-commit to main:** additive leaf content (source notes, lexicon entries, seed appends, log entries, exploratory analysis). Low blast radius.
- **Tier 2 — branch + researcher review:** load-bearing changes (foundational tables like 万年历/节气 data, time module, rule spec modifications, boundary document revisions, constitution/schema changes, promotion of findings to hypotheses). CC opens a branch, ends the session log with “ready for review”; the researcher merges.

This gives “allowed to be updated” layers a concrete mechanism: revisions arrive as reviewable diffs with reasoning in the commit message — the history records the researcher’s evolving understanding.

Conventions: commit messages follow the language policy (八字 content commits in Chinese) and are prefixed with session type (`intake:`, `synthesis:`, `engineering:`, `audit:`, `phase0:`).

-----

## Outcome

Haiwen approved; Claude produced **PROJECT_BRIEF.md** consolidating all of the above, plus a review noting:

1. §11 has the init session distill `CLAUDE.md` from the brief — researcher should personally verify the distillation preserved §1, especially the no-translation rule and the 火 ≠ fire example.
1. The task queue is the researcher’s bottleneck: Phase-0 task definition (which 流派, which texts count as primary) needs human judgment; early sessions will surface questions.
1. Deliberate gap: no schools/texts enumerated in the brief — that taxonomy must be a Phase-0 research output, not a founding assumption. Examples in the brief are illustrative only.
1. Open tension: 八字 logs are in Chinese, but engineering sessions touch both traditions’ code — resolved implicitly (formal layer = neutral ground, engineering logs may be either language); add a hard rule to the constitution if desired.