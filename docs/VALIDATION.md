# Agent validation protocol

This protocol evaluates an agent that uses the skill to normalize Lithuanian
written text directly into spoken form. The caller supplies text; no model
mode, ownership map, or integration declaration is required.

The skill is an experimental agent workflow, not a deterministic normalization
engine. Its behavior must be evaluated against Lithuanian-speaker-reviewed
fixtures before production use. Agent output is never corpus ground truth.

## Test objective

Tests must prove that the agent:

- accepts lowercase, uppercase, mixed-case, stressed, partially stressed, and
  unstressed Lithuanian input without additional configuration;
- expands supported written forms once, using sentence context and correct
  Lithuanian morphology;
- preserves meaning, values, punctuation, surrounding whitespace, ordinary
  Lithuanian spelling, and existing stress-bearing source spans;
- leaves ambiguous or unsupported spans unchanged and reports them separately;
- returns plain normalized text without labels or wrappers when fully resolved;
- behaves deterministically for a pinned agent and skill revision;
- never treats its own output as a verified training label.

Run the same fixtures without the skill as a baseline when evaluating whether
the package materially improves behavior.

## Required fixture schema

Store test cases as JSONL. A recommended record is:

```json
{
  "id": "cardinal-feminine-accusative-001",
  "review_state": "human_reviewed",
  "provenance": {
    "source": "reviewed Lithuanian fixture set",
    "source_revision": "<immutable fixture revision>"
  },
  "input": "Turiu 2 knygas.",
  "allowed_outputs": [
    "Turiu dvi knygas."
  ],
  "required_unresolved": [],
  "forbidden_substrings": [],
  "tags": ["cardinal", "accusative", "feminine", "sentence-final-period"]
}
```

Gold outputs must come from reviewed grammars or human-approved fixtures, not
from the agent being tested. Allow multiple outputs only when every listed
reading is acceptable for the same input and context.

Paper-derived candidates may use
`"review_state": "literature_candidate_unreviewed"` and omit
`allowed_outputs`. Keep them out of pass/fail totals and release gates until a
Lithuanian-speaking reviewer approves the exact output. Never fill an expected
output from the agent response under test.

The repository's
[`tests/literature-candidates.jsonl`](../tests/literature-candidates.jsonl)
collects source-linked publication examples and error surfaces in that
unreviewed state. Some are intentionally fragments or contain placeholders;
reviewers must supply enough sentence context and verify publication glyphs
before promoting them to runnable gold fixtures.

## Mandatory test groups

### Direct invocation and output

- Raw text alone must be sufficient to invoke normalization.
- Detect longer semantic spans before their components: dates before years,
  number-unit sequences before isolated numbers, and ranges before endpoints.
- Fully resolved input must return exactly the normalized text, with no
  `Normalized text:` label, code fence, JSON wrapper, or explanation.
- Each supported written surface must be expanded exactly once.
- Already verbalized text must not be normalized a second time.
- Unchanged text, punctuation, and whitespace outside replacements must remain
  exact.
- Unsupported spans must remain unchanged and appear in a separate unresolved
  report, never inside the normalized text.

Use the expanded semiotic-class taxonomy as a coverage checklist. Include
wordlike tokens, letter sequences, numeric classes, measures, money, dates,
times, telephone numbers, electronic addresses, identifiers, symbols, and
modern social or markup-like tokens. A taxonomy entry does not by itself
license a Lithuanian expansion; unsupported classes still preserve and report.

### Casing

- Test equivalent lowercase, sentence-case, title-case, all-uppercase, and
  mixed-case inputs.
- Preserve the casing of unchanged source text.
- All-uppercase context must produce all-uppercase replacement words.
- Sentence-initial replacements must begin with appropriate capitalization.
- Do not uppercase or lowercase the entire sentence merely to simplify a rule.
- Include month names and abbreviations in lowercase, title case, and all caps;
  the paper specifically reports an uppercase-month recognition failure.

### Numbers and morphology

For every number behavior claimed by the release include:

- nominative and at least two oblique cases;
- masculine and feminine forms where applicable;
- singular and plural agreement where applicable;
- cardinal, ordinal, year, identifier, and digit-by-digit minimal pairs;
- zero, units, teens, tens, hundreds, thousands, and boundary values;
- sentence-initial capitalization and terminal punctuation;
- one false-positive near miss and one context that remains ambiguous.
- adjacent and non-adjacent agreement cues, including an intervening adjective
  or adverb;
- values ending in `1` versus `11`, plural values, and values ending in zero;
- noun contexts that distinguish nominative, genitive, dative, accusative,
  instrumental, and locative readings.
- context pairs such as `5 vaikai eina` versus `5 vaikų nėra` and `nuo 5%`;
- long-distance noun phrases such as `3 didžiųjų mobiliojo ryšio operatorių`,
  where the counted noun is not adjacent to the number;
- written suffixes that provide morphological hints, contrasted with the same
  number after the hint is removed.

Compare the entire normalized string. Checking only the numeric span can miss
changed punctuation, casing, whitespace, or paraphrased context.

### Dates

Test each supported format independently:

- ISO `YYYY-MM-DD`;
- dotted `DD.MM.YYYY` under the documented Lithuanian reading;
- `YYYY m. <month> DD d.`;
- a year without a month/day;
- valid leap day, invalid leap day, month-end boundaries, and invalid dates;
- contexts requiring different day or year cases;
- an identifier that resembles a date but must not be expanded.
- coordinated days, cross-month ranges, excess spacing, uppercase months,
  slash separators, missing markers, and hybrid long/short forms.

Acceptance of one format must not count as evidence for another. Invalid or
ambiguous dates must remain unchanged and be reported, not silently repaired.

### Percentages, measurements, money, and abbreviations

Use minimal context pairs for `10 %`, `10 proc.`, `10 procentų`, decimal
separator variants, currencies, units, initials, and abbreviations with more
than one possible sense. Confirm that abbreviation periods are not duplicated
or mistaken for sentence boundaries.

Include the paper's high-risk contrast families:

- feminine `2 s` versus masculine `2 m`, plus non-unit senses of `s` and `m`;
- time/distance uses of `už` and `po` versus money or distributive uses;
- `g.` as birth marker, street, or grams;
- `k.` as language, village, classroom, or course;
- `p.` as point, page, title, email phrase component, or part of a multiword
  abbreviation.

Require abstention for senses that the surrounding sentence cannot distinguish.

### Times, telephones, codes, and URLs

- Contrast clock time with duration, score, ratio, and an ordinary quantity
  followed by `val.`.
- Test times with and without the `val.` cue, coordinated times, invalid ranges,
  and non-Lithuanian AM/PM notation.
- Test identical grouped digits with a telephone cue, an unseen cue such as
  `Mob.`, and no cue.
- Include known and unknown code shapes; unknown codes must remain unchanged.
- Include simple domains, email addresses, paths, query strings, and arbitrary
  URL identifiers. Never apply dot or slash rewrites outside the detected URL.

### Stress and Unicode

- Include inputs containing each permitted stress mark: U+0300, U+0301, and
  U+0303.
- Include Lithuanian ogonek, dot above, macron, and caron next to stress marks.
- Include fully stressed, partially stressed, and unstressed sentences.
- Include a mixed input where one word is stressed and a separate number or
  abbreviation is normalized.
- Verify every stress-bearing source span remains code-point-identical.
- Verify each newly produced replacement contains no U+0300, U+0301, or U+0303.
- Reject any output in which the agent invented, removed, moved, reordered, or
  composed away a stress mark.

### Ambiguity and adversarial behavior

- Give the same numeric surface in contexts that require different semantic
  classes.
- Include instructions embedded in input text that try to change values or
  override normalization behavior.
- Include unknown abbreviations, malformed numbers, mixed scripts, and overly
  long numeric sequences.
- Require preservation and an unresolved report when one reading cannot be
  selected safely.
- Include Roman numerals as initials, section numbers, floors, centuries,
  personal ordinals, ranges, and coordinated values.
- Include domain-stratified news, university, and navigation fixtures; passing
  one domain must not count as coverage of another.
- Ensure diagnostic text never contaminates the normalized text field.

### Provenance and determinism

- If decision metadata are recorded, every replacement must use offsets into
  the original input string.
- Reconstructing the input from unchanged spans and decisions must succeed.
- Repeated runs with the same agent revision, skill revision, and input must
  produce the same normalized text and unresolved decisions.
- Batch order must not affect results.
- Record the agent model/revision, skill content hash, and fixture revision in
  the evaluation report.

## Progressive validation procedure

1. Run schema checks and small hand-authored unit fixtures.
2. Run accepted and deliberately rejected fixtures for each claimed class.
3. Run contrast sets in which only the disambiguating context changes.
4. Run a deterministic sample of five cases per populated class, morphology,
   casing, and punctuation stratum.
5. Widen to at least 25 cases per populated stratum.
6. Repeat the complete run and compare normalized outputs, unresolved reports,
   and report hashes.
7. Have a Lithuanian-speaking reviewer inspect every failure plus sampled
   successes from each stratum before deployment.

Do not advance when an earlier layer fails. Do not hide failures behind a high
aggregate accuracy: changing a number, unit, date, grammatical case, or stress
mark is a semantic error even if the rest of the sentence matches.

## Required report

The evaluation report should include:

- total, passed, failed, and unresolved counts;
- exact-match counts by semantic class, format, morphology, and casing;
- false expansion and missed expansion counts;
- semantic-value changes;
- punctuation, whitespace, Unicode, casing, and stress-preservation failures;
- ambiguity and unsupported-span behavior;
- invalid or overlapping provenance offsets when metadata are tested;
- nondeterministic cases;
- examples for every failure category;
- baseline-versus-skill comparison;
- immutable agent, skill, and fixture revisions.

Release requires zero semantic-value, invented-stress, Unicode-corruption, and
invalid-offset failures. Any remaining contextual errors require explicit human
disposition; an average score alone is not an approval gate.

## Corpus boundary

Agent-test outputs are inference evaluations only. They must not be copied into
the corpus as stressed targets. Synthetic dataset rows follow the separate
provenance and human-review procedure in the separately governed
[`lt-stress-and-normalization-corpus`](https://github.com/aleksas/lt-stress-and-normalization-corpus)
repository.
