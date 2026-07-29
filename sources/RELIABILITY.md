# RELIABILITY.md — source-reliability metric

> **Status: Tier-2** (schema-adjacent — adds a source-level labeling layer alongside claim-level `verification`). v1, session 0006 (2026-07-16), per researcher directive: *keep every encountered resource, including unconfirmed ones; label all sources, past and future.*
> Grounded in a deep-research survey of established grading frameworks (16 adversarially-verified findings; see §5). One planned section is deferred (§6).

## 1. The two-layer principle (load-bearing)

**Source-level reliability and claim-level verification are graded independently and never merged.**

- The **source layer** (this metric) labels *where information came from* — attached in `/sources/register/`.
- The **claim layer** (`verification: verified | unverified` in note frontmatter, §1.2 of the brief) records whether *a specific claim* has been checked against a primary text in `/sources/`.
- A reliable-class source can carry a wrong claim; a marketing page can carry a true one. This mirrors NATO doctrine requiring the two dimensions be estimated independently (STANAG 2003 / AJP-2.1), and GRADE-CERQual's model of grading synthesized findings separately from the documents beneath them. It is the same discipline as our four-axes rule: different kinds of evidence never collapse into one score. Researcher-decision grounding: `/log/decisions/2026-07-28-source-credibility-principle.md` (credibility is graded relatively — transmission confidence + perspective-of-source; no absolute truth value; divergence between sources is data).

## 2. Label format

```
<Class letter><Access digit>[-<flags>]     e.g.  D3-门 ,  B3-I ,  E3-C$
```

## 3. Dimensions

### Class (what kind of source) — anchored by observable type, not judgment

| | Class | Anchor |
|---|---|---|
| **A** | 一手原典（已核验） | Verified copy of a primary text living in `/sources/` proper. Only an `audit:` session can assign A. |
| **B** | Academic / official | Peer-reviewed publication, academic-press monograph, national standard, official record — named, institutionally accountable. |
| **C** | Bibliographic infrastructure | Text repositories & catalogs (ctext, 书格, library records, publisher pages). Reliable *about* texts (editions, dates, existence) — grades nothing about content truth. |
| **D** | Named practitioner / enthusiast | Signed writing with accountable authorship; typically carries 门户 stance. |
| **E** | Anonymous / aggregated / commercial | Encyclopedic crowd entries, unsigned aggregator sites, marketing pages, forums. Kept as leads, never as support. |
| **F** | Known-bad | Caught fabricating or repeatedly wrong *in our own audits*. Retained in register (the record of unreliability is itself a finding). |

### Access (how we actually saw it) — pure observable fact

| | Access |
|---|---|
| **1** | Original / full text read directly |
| **2** | Full text via trustworthy reproduction |
| **3** | Snippet/snapshot layer only (e.g. 403-blocked, search-cache) |
| **4** | Second-hand paraphrase (someone else describing it) |
| **5** | Existence known only (bibliographic trace, dead link) |

### Flags (orthogonal markers, combine freely)

`I` independently derived · `C` 疑转抄 (suspected copy-chain) · `P` 当事人自证 (self-interested party attesting own claim) · `$` commercial interest · `门` school-partisan stance · `X` currently unreachable

## 4. Usage rules

1. **Register everything.** Every source encountered in any session gets a register row (label + one-line impression + which task met it) — including, especially, unconfirmed ones: today's unusable source may align with future research. Registration ≠ endorsement. Deleting a record is information loss; labeling it down is not.
2. **Labels travel with citations.** Quoting or relying on a registered source anywhere in the repo, carry its label.
3. **Promotion to A** happens only by a verified copy entering `/sources/` proper, via `audit:` or `intake:` with verification.
4. **Labels are recorded judgments, not measurements.** When in doubt between two classes, take the lower and note why.
5. **Audit re-checks labels.** Periodic `audit:` sessions re-grade a sample of register rows. (Rationale in §5, finding on aggregation.)

## 5. Design rationale — what the verified research dictated

Sixteen findings survived 3-0/2-1 adversarial verification (sources: Irwin & Mandel 2019, *Intelligence & National Security*, tandfonline.com/doi/abs/10.1080/02684527.2019.1569343; Kelly, Budescu, Dhami & Mandel 2025, *Judgment and Decision Making* 20:e36, cambridge.org [abstract-layer only, 403]; arXiv:2405.19968; GRADE-CERQual, link.springer.com/article/10.1186/s13012-017-0688-3; ICD-203 reliability study, ncbi.nlm.nih.gov/pmc/articles/PMC6330287). Design responses:

- **Documented failure: raters interpret the same alphanumeric ratings inconsistently — even the same rater across occasions.** → Our two graded dimensions are anchored to *observable* facts (source type; how we accessed it), not judgment words like "usually reliable." The genuinely subjective content moves into free-text impressions and flags.
- **Documented failure: certainty-words like "confirmed" overstate what's knowable.** → No grade in this metric asserts truth. Truth-adjacent status lives only in the claim layer, whose `verified` has a mechanical criterion: a copy exists in `/sources/` and was checked.
- **Documented failure: in practice raters collapse the two Admiralty axes into one (credibility halo).** → Our second axis (Access) is not a judgment at all — you cannot halo a fact about whether you read the full text.
- **Documented finding: individual grading has poor inter-rater reliability; aggregating many raters approaches near-perfect (ICC 0.498 → 0.897).** → Single-session labels are provisional by design; audit sessions re-grade samples, and disagreement between sessions is recorded, not overwritten.
- **CERQual's model: claim-confidence graded on multiple components of which source quality is only one.** → Confirms the two-layer split: our claim layer (and eventually the rule-attestation model, brief §4) weighs source labels as *one input*, never the whole story.

## 6. Deferred (recorded, not silently dropped)

The survey's 史学 source-criticism, 中文文献学（版本学/校勘学/辨伪学）, and SIFT/lateral-reading verification passes were lost to a session usage limit (claims drafted but unverified — not written into this spec). Impact: the **sub-grading of A-class texts** (edition quality, commentary strata, 辨伪 status — exactly what 版本学/辨伪学 would inform) is postponed to queue task `meta-002`. Until then, A-class entries carry free-text edition notes only.
