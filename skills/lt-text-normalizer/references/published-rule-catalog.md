# Published-rule catalog

Source: Pijus Kasparaitis, [“Normalization of Lithuanian Text Using Regular
Expressions”](https://arxiv.org/abs/2312.17660), arXiv:2312.17660v2, 2024.
The inspected PDF has SHA-256
`50266a8d2b32aa4d53c72076cea4d5a2dfa1ed5c44b7810587f83c27c443eb99`.

## Scope and status

This is a semantic inventory of every numbered rule block printed in the
paper: (1) through (60). It deliberately paraphrases the transformations
instead of republishing the regex source. The paper reports 1,590 rules for
the DEL/FLF experiments and 771 for NAV, but does not print or link the full
rule files. Consequently:

- `published-block coverage` is 60/60;
- `reported implementation-rule coverage` is unknown, not 60/1,590;
- every item below has status `literature_catalogued_only`;
- cataloguing a block does not make it executable, reviewed, or release
  approved;
- ellipses and “analogous rules” in the paper are recorded as unrecoverable
  variants, not silently reconstructed.

This file is the audit inventory. For normal use, start with the
[hierarchical rule router](published-rule-families/README.md), then read only the
relevant class branch. Each K01–K60 section there contains behavior, at least
one paper or clearly marked schematic example, and a guard.

For runtime normalization, use a catalogued item only to identify a candidate
semantic class and required context. A production rewrite still needs a
precise grammar, positive and negative fixtures, cross-class ambiguity checks,
and Lithuanian-speaker review. Preserve and report a span if those
prerequisites are absent.

## Processing model in the paper

The rules form an ordered cascade. Wider contexts (for example, full dates)
run before narrower ones (for example, years and bare numbers). Earlier rules
may insert temporary tags for number, case, gender, and cardinal/ordinal
status; later rules consume or duplicate those tags. This ordering is part of
the behavior: treating the entries below as independent substitutions would
not reproduce the system. Dataset-specific choices in the paper are evidence
about those datasets, not universal Lithuanian rules.

The paper's taxonomy covers `EXPN` (expand an abbreviation), `LSEQ` (spell a
letter sequence), `ASWD` (read as a word), `NUM` (cardinal), `NORD` (ordinal),
`NTEL` (telephone), `NTIME` (time), `NDATE` (date), `NYEAR` (year), `NCODE`
(code), `URL`, `MISSP` (misspelling), and `NONE` (leave unchanged). `MISSP` is
explicitly outside the paper's implementation. `NONE` is a classification
outcome rather than a numbered rewrite.

## Complete numbered inventory

### General transformation

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K01` | (1) | Demonstrates capture-and-reorder by moving a page abbreviation after its following number. | An explanatory regex example, not a claimed general normalization class. |

### Cardinal numerals and units (§6.1)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K02` | (2) | Insert plural-instrumental metadata before a digit after *su*, *sulig*, or *ties*. | One member of a larger, unprinted preposition inventory; *už* and *po* need unit/context-sensitive handling. |
| `K03` | (3) | Copy case/number metadata to each number in a compound distance or duration such as kilometres plus metres. | Descending compatible unit sequence only; do not infer this structure from adjacency alone. |
| `K04` | (4) | Place a second copy of the case/number tag after a tagged number so a following magnitude or unit can consume it. | Internal cascade operation, not user-visible output. |
| `K05` | (5) | Split up-to-12-digit numerals into billion, million, thousand, and remainder groups, propagating metadata. | The paper abbreviates intermediate magnitudes because final inflection is deferred; exact omitted variants are unavailable. |
| `K06` | (6) | Select the feminine cardinal form of digit 4 from case/number metadata. | Representative of an unprinted numeral paradigm, not a complete digit grammar. |
| `K07` | (7) | Inflect the magnitude abbreviation for million from case metadata. | Representative cases are printed; the full magnitude inventory is not. |
| `K08` | (8) | Inflect kilometre from case metadata. | Representative unit only. Unit sense, gender, and agreement must already be resolved. |

The surrounding prose adds three necessary constraints: a final 1 other than
11 selects a singular unit; unit gender controls the last digit's gender; and
values ending in 0 or 11–19 select a genitive unit, overriding the
preposition-derived case locally. These constraints are source behavior even
though they are not separately numbered.

### Ordinal numerals (§6.2)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K09` | (9) | Replace a preposition-derived case tag with nominative metadata before an Arabic ordinal carrying an explicit hyphenated ending. | The written ordinal ending has priority only after the complete ordinal form is recognized. |
| `K10` | (10) | Repair the digit-4 cardinal stem plus an explicit pronominal ordinal ending to the correct ordinal stem. | One printed form from a larger inflectional family. |
| `K11` | (11) | Convert a compound tens expression whose final component carries a feminine ordinal ending into a correctly formed ordinal. | A representative morphology repair; nearby number words and ending must match. |
| `K12` | (12) | Mark Arabic numbers before auditorium, classroom/cabinet, or article abbreviations as ordinals with the appropriate gender. | Domain lexemes are closed cues; arbitrary noun following a number is insufficient. |
| `K13` | (13) | Realize feminine ordinal digit 4 from case metadata, defaulting to nominative when untagged. | Representative paradigm only. |
| `K14` | (14) | Inflect Roman numeral I to agree with selected endings of the following Lithuanian word. | The paper says analogous rules cover other Roman numerals up to 30; that unprinted set cannot be reconstructed as published regex coverage. |
| `K15` | (15) | Expand isolated Roman I–VI as nominative singular ordinals with boundary guards. | Printed subset of I–XXX. `I.` and `V.` are deliberately treated as initials in this dataset policy. |
| `K16` | (16) | Repair a Roman-numeral expansion followed by an explicit plural pronominal ending. | Representative correction only; do not concatenate arbitrary endings. |
| `K17` | (17) | Expand Roman numeral plus `a.` as floor or century, with following lowercase context selecting genitive century and sentence-final context selecting nominative century. | The floor/century choice is dataset-specific: FLF used floors for I–IV, while DEL treated `a.` as century. Ambiguous uses must abstain. |
| `K18` | (18) | Expand a Roman fraction, optionally followed by the abbreviation for “part,” as “ordinal part out of cardinal denominator.” | Printed only for III/IV; no general fraction grammar is supplied. |

### Dates (§6.3)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K19` | (19) | Recognize a preposition-tagged long date with year marker, genitive month name, day, and day marker; render year and day as ordinals and propagate day case. | Full month alternation is elided in print. Year/month remain genitive; the preposition controls the day. |
| `K20` | (20) | Expand the day abbreviation in singular genitive, accusative, or instrumental from metadata. | The printed table omits other forms; a written full word for day is left as written in this path. |
| `K21` | (21) | Normalize a long date without a preposition, assigning singular accusative to the day. | Requires the complete long-date structure. |
| `K22` | (22) | Normalize the observed irregular long-date form that omits the year abbreviation. | Paper reports only five examples; treat as narrow evidence, not permission for broad malformed-date repair. |
| `K23` | (23) | Normalize a long date containing a day range; render both days as singular accusative ordinals and the day unit as plural instrumental. | Allows paper-observed dash/hyphen spacing; any preposition is ignored by this dataset rule. A missing-year-marker companion is mentioned but not printed. |
| `K24` | (24) | Insert genitive metadata between selected prepositions and a genitive month name when the date has no year. | Closed preposition and month lists; this only prepares later date handling. |
| `K25` | (25) | Normalize a preposition-tagged month-name plus day date without a year. | The inherited preposition metadata controls the day. |
| `K26` | (26) | Normalize a month-name plus day date without year or preposition, including sentence-initial capitalization. | Assigns singular accusative to the day. |
| `K27` | (27) | Normalize a yearless month-name date with a day range. | Both days are singular accusative; the day unit is plural instrumental; the paper ignores a preceding preposition. |
| `K28` | (28) | Normalize a preposition-tagged year, month, and month abbreviation when no day is given. | Year and month remain genitive; the preposition determines the month-unit inflection. |
| `K29` | (29) | Normalize year, month, and month abbreviation without a preposition. | Defaults the month unit to singular accusative. |
| `K30` | (30) | Expand the month abbreviation in singular genitive, accusative, or instrumental from metadata. | Representative three-case realization only. |
| `K31` | (31) | Normalize year marker plus a nominative month name when neither day nor month abbreviation is present. | The month remains nominative; do not conflate with the genitive month used in full dates. |
| `K32` | (32) | Insert genitive metadata after *nuo*, *iki*, or *ligi* before “this year” in abbreviated or full form. | Preparatory rule for the yearless date path. |
| `K33` | (33) | Expand the “this year” abbreviation to its full genitive-plural phrase, preserving initial capitalization. | Exact abbreviation only. |
| `K34` | (34) | Normalize a preposition-tagged short numeric date (`YYYY MM DD`) into year, coded month, and ordinal day components. | The source pattern permits space or hyphen separators; ranges and calendar validity need separate validation. |
| `K35` | (35) | Map numeric month codes 01–12 to genitive Lithuanian month names. | The middle ten mappings are elided in the paper; their semantic values are clear but their exact source regexes are not printed. |
| `K36` | (36) | Normalize a short numeric date without a preposition, using a nominative singular day in the paper's output. | This differs from the long-date default and must remain format-specific. |

### Years (§6.4)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K37` | (37) | Normalize years in the paper's 1500–2059 range with explicit *metus* or `m.`, selecting case from the word, preposition tag, or default instrumental. | Range bound and precedence are corpus-derived. A full *metai* paradigm is discussed but not fully printed. |
| `K38` | (38) | Treat a bare 1500–2059 number before punctuation or end of text as a pronominal nominative-plural year. | A strong corpus heuristic, not semantic certainty; identifiers and cardinals need negative tests. |
| `K39` | (39) | Normalize two four-digit years separated by slash, dash, or hyphen, using preposition-derived genitive/accusative or default instrumental. | Does not verify consecutiveness and does not infer case from a following year word. |
| `K40` | (40) | Normalize the explicit “from YEAR to YEAR years” construction with genitive metadata. | Fixed *nuo … iki …* shape only. |

### Time (§6.5)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K41` | (41) | Normalize hour-only, `HH:00`, and `HH:MM` forms followed by `val.`; hours are singular accusative ordinals and minutes cardinals. | `val.` is required to avoid scores and other numerics; hour/minute ranges are checked. Zero minutes are omitted. |
| `K42` | (42) | Normalize the same time forms under inherited singular-genitive metadata. | Minutes become plural genitive; accusative prepositions need no separate rewrite in the paper. |
| `K43` | (43) | Rewrite a compact time range into an explicit *nuo … val. iki … val.* structure for later rules. | Both endpoints must be valid time-shaped values; optional minutes are retained. |
| `K44` | (44) | Insert the missing `val.` after the first endpoint of an already explicit *nuo … iki … val.* range. | Exact paired-preposition structure only. |
| `K45` | (45) | Duplicate inherited case metadata across two times or hours joined by *ir* or *arba*. | Both conjuncts must share the recognized time structure. |

### Telephone numbers (§6.6)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K46` | (46) | Expand telephone labels and separate national or international telephone digits for digit-by-digit reading, verbalizing plus where present. | Several Lithuanian grouping conventions are accepted only after a telephone cue; the publication predates later numbering-plan changes and requires current validation. |

### Codes (§6.7)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K47` | (47) | Spell the ISBN label and separate 10- or 13-digit ISBNs for digit-by-digit reading. | ISBN structure and checksum are not validated by the printed block; paper-added pronunciation accents are outside this skill's unstressed-output policy. |
| `K48` | (48) | Separate every digit of a five-digit value as a postal code. | Valid only for the paper's NAV/FLF datasets; DEL five-digit values were cardinals. Never use without postcode/domain evidence. |
| `K49` | (49) | Separate the numeric portions of the observed parenthesized study-program code while retaining its letters. | FLF-specific fixed code shape. |

### URLs (§6.8)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K50` | (50) | Verbalize `@`, remove protocol and nonnumeric slashes, and verbalize a dot between sufficiently long letter sequences. | The paper explicitly does not detect complete URLs. These global substitutions can affect non-URLs and require scoped URL/email parsing in a new implementation. |

### Abbreviations read as words (§6.9)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K51` | (51) | Replace selected non-Lithuanian letters with Lithuanian pronunciation-oriented spellings. | Only `ł` and `ü` examples are printed; this is transliteration, not a complete alphabet policy. |
| `K52` | (52) | Remove an abbreviation-final period or add pronunciation stress to selected abbreviations read as words. | Lexicon-specific. This skill must not add the paper's stress marks to newly expanded text. |
| `K53` | (53) | Apply pronunciation-oriented orthographic transcriptions to selected foreign navigation words meaning street/road/avenue. | Closed lexicon and domain-specific; paper-added stress is excluded by this skill's output policy. |

### Letter sequences (§6.10)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K54` | (54) | Detect a consonant-only abbreviation of bounded length and tag each letter for spelling, marking the last letter for accent. | Paper used seven length-specific rules for lengths 1–7 but prints only length 3. Boundary inventory and accent behavior are source-specific. |
| `K55` | (55) | Convert tagged consonants to Lithuanian letter names, distinguishing medial and final accented realization. | Partial letter-name table shown; generated stress conflicts with this skill's unstressed-expansion boundary. |
| `K56` | (56) | Spell selected uppercase abbreviations containing vowels using explicit dictionary entries and Lithuanian letter names. | Closed lexicon. The proposed general 2–3-letter uppercase fallback was not implemented in the paper. |

### Abbreviations to expand (§6.11)

| ID | Paper block | Semantic operation | Essential boundary or limitation |
|---|---:|---|---|
| `K57` | (57) | Expand a closed list of stable abbreviations such as registration/serial number, telephone, email, language, acting role, example, and “that is.” | The block contains multiple lexicon entries, not a productive abbreviation grammar. Unit abbreviations are discussed elsewhere and depend on numeric metadata. |
| `K58` | (58) | Expand selected abbreviations that occur at sentence end while retaining terminal punctuation. | Closed list; distinguish abbreviation punctuation from the sentence boundary. |
| `K59` | (59) | Inflect the abbreviation for “senior/chief” from the ending of the following word. | The paper calls this error-prone and recommends leaving such forms unchanged rather than broadly applying complex guesses. |
| `K60` | (60) | Attempt to inflect the abbreviation for “saint” from a following name or noun ending. | The paper likewise advises against expansion because reliable morphology is difficult; default treatment here is abstention. One printed replacement appears suspicious and requires source-author clarification. |

## Unnumbered and unavailable behavior

The catalog is complete for numbered printed blocks, not for the executable
system reported in the experiments. In particular, the publication omits:

- most of the 1,590 DEL/FLF and 771 NAV regex rules;
- full numeral and ordinal paradigms;
- most Roman-numeral agreement rules through 30;
- complete preposition, unit, magnitude, month, abbreviation, and
  pronunciation lexicons;
- dataset rule files, exact cascade order, and a machine-readable test set;
- executable rules for `MISSP`; and
- a standalone numbered rule for `NONE`, whose intended action is no rewrite.

Do not fill these gaps from intuition and call the result a reproduction.
Record new rules as project extensions with independent provenance and
validation.
