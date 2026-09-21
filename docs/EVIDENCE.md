# Evidence, scope, and publication alignment

## Current claim

Version 0.9.2 is a behavioral specification for direct agent-mediated
Lithuanian text normalization. It accepts raw text without an integration
declaration and defines context-aware expansion, casing, ambiguity handling,
Unicode and stress preservation, provenance, and validation requirements. It
does not ship the regular-expression system, grammars, lexicon, or evaluated
rule coverage described in the Lithuanian normalization literature.

Accordingly, this release must not be described as an implementation or
reproduction of Kasparaitis's system. Conceptual alignment is meaningful;
operational coverage has not yet been measured.

The skill includes a small, attributed set of visually checked examples, a
semantic catalog of all 60 numbered rule blocks printed in sections 3 and 6,
and a hierarchical class reference with an example and a guard for every
block. Examples are labelled as paper examples or schematic illustrations.
They remain literature evidence—not approved executable rules or gold
fixtures—and each enabled behavior requires contextual negative tests and
human review.

## Alignment with published Lithuanian normalization work

Pijus Kasparaitis,
[“Normalization of Lithuanian Text Using Regular Expressions”](https://arxiv.org/abs/2312.17660),
provides the closest Lithuanian-specific reference. The skill follows several
of its high-level concerns:

- distinguish detection/classification from expansion;
- treat numbers, dates, times, abbreviations, Roman numerals, and symbols as
  separate normalization classes;
- use context and morphology when selecting Lithuanian word forms;
- preserve format-specific behavior rather than treating all numeric-looking
  strings alike.

The present repository reproduces the publication's **printed numbered
inventory at the semantic level**: 60 of 60 blocks are mapped in
[`published-rule-catalog.md`](../skills/lt-text-normalizer/references/published-rule-catalog.md).
That is 100% catalog coverage of the numbered blocks, not implementation
coverage. The paper reports 1,590 rules for DEL/FLF and 771 for NAV, but the
full rule files, complete cascade order, and lexicons are not published in the
paper. The repository therefore has unknown coverage of the reported regex
implementation and zero rules approved for production by this catalog alone.

Do not collapse those measurements into one “adherence percentage.” Report at
least these dimensions separately:

| Dimension | Current evidence |
|---|---:|
| Printed numbered blocks semantically catalogued | 60/60 (100%) |
| Reported 1,590-rule DEL/FLF implementation reproduced | Unknown; source rules unavailable |
| Catalog blocks implemented as deterministic rules here | 0/60 |
| Catalog blocks approved by reviewed behavioral tests here | 0/60 |
| Primary examples transcribed in `publication-examples.md` | 5 |
| Source-linked, unreviewed literature test candidates | 16 |
| Rule blocks with a routed explanatory example and guard | 60/60 (100%) |

The catalog also records the paper's cascade ordering, unnumbered constraints,
dataset-specific choices, and places where the publication uses ellipses or
mentions analogous rules without printing them.

## Public implementation search

The arXiv v2 source archive contains only the paper's TeX, bibliography, and
style file. It does not contain the C++ implementation, ordered regex file, or
evaluation data. Related public LIEPA/LithUSS implementations exist, including
`aleksas/laba-diena-tts`, `liepa-project/liepa2-nao_sintezatorius`, and
`aleksas/phonology_engine`, but their age, custom rule formats, rule counts,
and provenance do not establish them as the paper's 1,590/771-rule system.
Pinned revisions, hashes, license signals, and reuse requirements are recorded
in the skill's
[`implementation-landscape.md`](../skills/lt-text-normalizer/references/implementation-landscape.md).

## LLM evidence

- Wong et al.,
  [“PolyNorm: Few-Shot LLM-Based Text Normalization for Text-to-Speech”](https://aclanthology.org/2025.emnlp-industry.6/),
  directly evaluate Lithuanian among eight languages. This supports studying
  an agent-mediated inference path, but not treating free-form LLM output as
  linguistic ground truth.
- Zhang et al.,
  [“A Chat about Boring Problems: Studying GPT-Based Text Normalization”](https://doi.org/10.1109/ICASSP48485.2024.10447169),
  support linguistically informed prompting and error-taxonomy-based
  evaluation. Their experiments are not Lithuanian-specific.

## Related normalization evidence

- Balčiūnas,
  [“Context based number normalization using skip-chain conditional random fields”](https://ceur-ws.org/Vol-2470/p7.pdf),
  models Lithuanian numeral case, type, and gender separately and shows why
  distant nouns, verbs, and prepositions matter. Its examples support
  long-distance morphology tests, not automatic adoption of its model output
  as this repository's gold data.
- van Esch and Sproat,
  [“An Expanded Taxonomy of Semiotic Classes for Text Normalization”](https://www.isca-archive.org/interspeech_2017/esch17_interspeech.pdf),
  provides a broad coverage checklist for non-standard tokens. The taxonomy is
  language-general; it does not supply Lithuanian verbalizations.

## Requirements before a stronger release claim

1. Implement a deterministic candidate grammar or constrained service for
   every enabled high-risk class.
2. Map each implemented rule family to the cited publication and record
   deliberate deviations.
3. Add Lithuanian-speaker-reviewed positive, negative, ambiguity, morphology,
   punctuation, Unicode, and provenance fixtures.
4. Report class-specific precision, recall, exact match, semantic-value
   errors, unsupported spans, and deterministic rebuild hashes.
5. Pin the skill, agent model, grammar, lexicon, and fixture revisions.

Until those gates pass, keep the release version below 1.0 and label it
experimental.
