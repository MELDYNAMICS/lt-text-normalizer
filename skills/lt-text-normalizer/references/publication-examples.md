# Publication examples

Source: Pijus Kasparaitis, [“Normalization of Lithuanian Text Using Regular
Expressions”](https://arxiv.org/abs/2312.17660), arXiv:2312.17660v2, 2024.
The PDF inspected for this inventory has SHA-256
`50266a8d2b32aa4d53c72076cea4d5a2dfa1ed5c44b7810587f83c27c443eb99`.

## How to use these examples

These are publication-attributed examples, not automatically approved
production rules or corpus labels. Keep the following provenance with every
derived fixture:

```json
{
  "source": "Kasparaitis 2024",
  "source_revision": "arXiv:2312.17660v2",
  "source_pdf_sha256": "50266a8d2b32aa4d53c72076cea4d5a2dfa1ed5c44b7810587f83c27c443eb99",
  "source_section": "<section>",
  "source_page": "<printed page>",
  "validation_state": "literature_example_unreviewed"
}
```

Promote an example to `human_reviewed` only after a Lithuanian-speaking
reviewer confirms the orthography, intended semantic class, morphology, and
fit with this skill's unstressed spoken-form output. PDF extraction can corrupt
Lithuanian combining characters; verify the original page rather than copying
an extracted glyph blindly.

The paper's system targets a synthesizer directly and sometimes adds
pronunciation or stress information to abbreviations. This skill has a
different boundary: newly expanded words remain unaccented, while stress
already supplied in the user's input is preserved exactly. Do not transfer
paper-added stress into new normalizer output.

For runtime lookup, start with the
[hierarchical rule router](published-rule-families/README.md), which provides one
class branch and at least one example for every K01–K60 block. For the source's
complete numbered audit inventory and omitted material, use
[the published-rule catalog](published-rule-catalog.md). This page keeps a
small set of visually checked examples; it is not the coverage inventory.

## Selected examples

| Paper location | Written input | Paper expansion | What it demonstrates | Skill treatment |
|---|---|---|---|---|
| §6.1, p. 6 | `2 s` | `dvi sekundės` | Unit gender selects the feminine numeral. | Candidate only when the seconds/unit rule and context are approved. |
| §6.1, p. 6 | `2 m` | `du metrai` | A masculine unit selects the masculine numeral. | Candidate only when `m` unambiguously means metres. |
| §6.2, p. 7 | `III a.` | `trečias aukštas` | The FLF-domain example reads small Roman numerals plus `a.` as a floor. | Never universalize: the paper reports a different century reading in another dataset. Require domain/context evidence or abstain. |
| §6.2, p. 8 | `XIX a. pradžioje` | `devyniolikto amžiaus pradžioje` | Following context selects the century reading and genitive form. | Use as a contrast with the floor example, not as evidence that every `a.` means century. |
| §6.5, p. 11 | `13:15 val.` | `tryliktą valandą penkiolika minučių` | Hours use an ordinal form; minutes use a cardinal form. | Require the `val.` cue, valid hour/minute ranges, and an unambiguous clock-time context. |

## Error-analysis test priorities

Section 8 is especially useful for tests because it records where the paper's
rules failed. Treat the surfaces below as regression-test candidates, not as
ready-made gold outputs. A Lithuanian-speaking reviewer must approve the exact
expected text.

| Risk | Paper evidence | Test implication |
|---|---|---|
| Longer-class precedence | A date contains a year, and complex number-unit sequences contain smaller numbers. | Detect the longest semantic span first; test dates versus years and grouped measures versus isolated cardinals. |
| Year heuristic leakage | The 1500–2059 heuristic missed ancient years and selected the wrong case in noun-modifying contexts. | Contrast modern years, ancient years, identifiers, ranges, and genitive versus instrumental contexts. |
| Date case from syntax | Long and short dates without prepositions were sometimes assigned a default case that disagreed with the surrounding sentence. | Test nominative, genitive, and accusative date contexts rather than one default reading. |
| Orthographic variation | Long dates failed with slash separators, extra spaces, uppercase month names, or a missing `d.` marker. | Add exact variants such as `iki VASARIO 28 d.` and spacing/separator near misses; never silently repair an invalid date. |
| Coordinated dates and times | Conjunctions and ranges such as several days or `9 arba 10 val.` were not handled. | Test single values separately from coordinated values and cross-month ranges. |
| Time versus duration | `8 val. per 5 darbo dienas` was confused with clock time; forms without `val.` and `6:00 PM` were unsupported. | Contrast clock readings, durations, scores, and non-Lithuanian time formats. |
| Cardinal versus ordinal | `15 p.`, `1 priedas`, classroom numbers, and Roman numerals lacked reliable class cues. | Add minimal pairs for page/point, quantity/ordinal, floor/century, initials, and Roman ranges. |
| Distant agreement cues | `2 akademinės val.` and `per beveik 100 pozicijų` separate the number from the word or preposition that determines morphology. | Test intervening adjectives and adverbs; do not limit context to adjacent tokens. |
| Right-context inflection | The paper lists noun contexts requiring nominative, genitive, dative, accusative, instrumental, and locative readings. | Cover all productive cases and ensure the following noun can govern the numeral. |
| Telephone cue dependence | Uncued numbers and cues such as `Mob.` were misclassified. | Test recognized cues, unseen cues, and ordinary grouped numbers with identical surfaces. |
| Open-ended codes and URLs | Unseen code shapes and URLs with query strings were error-prone. | Preserve and report unknown formats instead of applying global punctuation rewrites. |
| Abbreviation polysemy | `g.`, `k.`, and `p.` each had several unrelated expansions. | Build context pairs for every approved sense and require abstention when context is insufficient. |
| Existing stress near abbreviations | `Šv.` expansion failed before stressed or syllabified following words such as `Šv. Jõnų`. | Test abbreviation expansion next to stressed text while requiring the source stress span to remain exact. |

The paper also reports large differences among news, university, and navigation
data. Keep domain-stratified fixtures and do not treat success in one domain as
coverage of another.

## Required contrast tests

For every publication-derived positive example, add at least one case that
must not inherit the same rewrite:

- Contrast `2 s` with contexts where `s` is a letter, variable, or unknown
  abbreviation.
- Contrast `2 m` with contexts where `m` means year, minute, a variable, or an
  unsupported abbreviation.
- Test `III a.` in both floor and century contexts and include an unresolved
  context. Dataset-specific precedence is not semantic evidence.
- Contrast `XIX a. pradžioje` with an initial or abbreviation-period near miss.
- Contrast `13:15 val.` with a score, ratio, identifier, invalid time, and a
  time lacking the `val.` cue.

Do not add a rule merely because its positive paper example matches. A release
still requires exact parsing, morphology, negative fixtures, overlap checks,
and human review.
