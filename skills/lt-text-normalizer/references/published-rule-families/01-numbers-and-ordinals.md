# Numbers and ordinals: K01–K18

Read this branch for cardinal numbers, units of measure, Arabic ordinals, or
Roman numerals. The examples explain published behavior; they do not enable a
runtime rewrite by themselves.

## General rewrite mechanics

### K01 — capture and reorder

- Behavior: demonstrate that captured spans can be reordered in replacement.
- Paper example: `p. 7` → `7 p.`
- Guard: this is an explanatory regex example, not a general page-number rule.

## Cardinal numerals and units

### K02 — preposition-derived instrumental tag

- Behavior: add plural-instrumental metadata before a digit after *su*,
  *sulig*, or *ties*.
- Paper example: `su 5` → `su «PI» 5` (intermediate form).
- Guard: other prepositions and the context-sensitive *už*/*po* cases belong
  to the larger, unpublished inventory.

### K03 — propagate case through a compound measurement

- Behavior: copy the governing tag to each number-unit pair.
- Paper example: `«PG» 5 km 300 m` → `«PG» 5 km «PG» 300 m`.
- Guard: require a recognized descending compatible-unit structure.

### K04 — copy metadata across a number

- Behavior: retain the tag before the number and duplicate it after the
  number for a following magnitude or unit.
- Schematic example: `«PA» 234 km` → `«PA» 234 «PA» km`.
- Guard: the tags are internal cascade state and must not reach normalized
  output.

### K05 — split large numerals into magnitude groups

- Behavior: introduce billion, million, thousand, and remainder groups while
  propagating metadata.
- Paper example: `«PA» 123456789234 km` is staged as `«PA» 123 «PA» mlrd
  «PA» 456 «PA» mln «PA» 789 «PA» tūkst «PA» 234 «PA» km`.
- Guard: the paper elides part of the exact rule family; do not infer arbitrary
  precision or grouping syntax.

### K06 — feminine cardinal realization

- Behavior: select the form of digit 4 from case, number, gender, and cardinal
  metadata.
- Paper example: `«PA» 4 «FC»` → `keturias`.
- Guard: this is one cell from an unprinted numeral paradigm.

### K07 — inflect a magnitude word

- Behavior: inflect *milijonas* from the governing case metadata.
- Paper example: `«PA» mln` → `milijonus`.
- Guard: abbreviation recognition and number agreement must already be
  resolved.

### K08 — inflect a measurement unit

- Behavior: inflect kilometre from the governing case metadata.
- Paper example: `«PI» km` → `kilometrais`.
- Guard: confirm that `km` is a unit and not part of another token.

The section also imposes unnumbered agreement rules. A final 1 other than 11
selects a singular unit; the unit controls the final digit's gender; and
values ending in 0 or 11–19 select a genitive unit locally. Paper examples
include `2 s` → `dvi sekundės` and `2 m` → `du metrai`.

## Arabic and Roman ordinals

### K09 — explicit ordinal ending overrides preposition case

- Behavior: reset preposition-derived case before an Arabic numeral carrying
  a recognized hyphenated ordinal ending.
- Paper example: `Apie 2004-ųjų pabaigą` → `Apie du tūkstančiai ketvirtųjų
  pabaigą`.
- Guard: require the full valid ordinal ending; do not override case for a
  bare cardinal.

### K10 — repair the digit-4 ordinal stem

- Behavior: replace the cardinal stem created during staged expansion with
  the correct ordinal stem.
- Paper example: `keturi-ųjų` → `ketvirtųjų`.
- Guard: apply only to the staged digit-plus-ending construction.

### K11 — repair a compound tens ordinal

- Behavior: attach a feminine ordinal ending to the tens expression in the
  form described by the printed pattern.
- Schematic example: `dvidešimt-oji` → `dvidešimtoji`.
- Guard: this illustrates the printed pattern; the publication does not print
  a complete ordinal morphology table.

### K12 — noun cue marks an Arabic ordinal

- Behavior: tag numbers before auditorium, cabinet/classroom, or article
  abbreviations as gendered ordinals.
- Paper examples: `104 aud.` → `šimtas ketvirta aud.`; `104A kabinetas` →
  `šimtas ketvirtas A kabinetas`; `90 str.` → `devyniasdešimtas str.`
- Guard: use only the closed noun/abbreviation cues.

### K13 — feminine ordinal realization

- Behavior: realize digit 4 as a feminine ordinal using inherited case.
- Paper rule example: `«SA» 4 «FO»` → `ketvirtą`.
- Guard: this is one representative digit/paradigm cell.

### K14 — Roman numeral agreement with the following word

- Behavior: inflect Roman numeral I from selected endings of the following
  Lithuanian word.
- Paper examples: `I etapas` → `pirmas etapas`; `I kvietimo` → `pirmo
  kvietimo`; `I vieta` → `pirma vieta`.
- Guard: the paper says analogous rules reach Roman 30 but does not print
  them. A suffix heuristic is not a full morphological parser.

### K15 — isolated Roman ordinals

- Behavior: expand a boundary-delimited Roman numeral as a nominative
  singular ordinal.
- Paper example: `III. Antikos istorijos` → `trečias. Antikos istorijos`.
- Guard: do not match inside a larger Roman numeral or word. The paper treats
  `I.` and `V.` as initials under its dataset policy.

### K16 — repair Roman ordinal plus explicit ending

- Behavior: combine the staged Roman expansion with a written pronominal
  plural ending.
- Paper example: `I-ieji rūmai` → `pirmas-ieji rūmai` → `pirmieji rūmai`.
- Guard: only recognized ordinal endings may trigger the repair.

### K17 — Roman numeral plus `a.`

- Behavior: choose a floor or century reading and inflect the century reading
  from nearby context.
- Paper examples: `III a.` → `trečias aukštas`; `XIX a. pradžioje` →
  `devyniolikto amžiaus pradžioje`.
- Guard: the floor reading for I–IV is FLF-specific; DEL used century. Abstain
  when domain and syntax do not disambiguate.

### K18 — Roman fraction

- Behavior: interpret a Roman numerator/denominator as an ordinal part out of
  a cardinal total.
- Paper examples: `III/IV d.` → `trečia dalis iš keturių`; `III/IV` → `trečia
  iš keturių`.
- Guard: only III/IV is printed; no general Roman-fraction grammar is supplied.
