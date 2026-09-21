# Dates, years, and times: K19–K45

Read this branch only after distinguishing a calendar date, a standalone year,
and a clock time from identifiers, scores, measurements, and bare cardinals.
Validate actual calendar/time values separately from matching their shape.

## Long and short dates

### K19 — preposition-tagged long date

- Behavior: stage a year-marker, genitive-month, day, and day-marker date so
  the year and day become ordinals and the preposition controls day case.
- Paper example: `Nuo 2013 m. sausio 4 d.` → `Nuo du tūkstančiai tryliktų
  metų sausio ketvirtos dienos`.
- Guard: require the complete date structure and a valid month/day.

### K20 — inflect the day abbreviation

- Behavior: expand `d.` from singular genitive, accusative, or instrumental
  metadata.
- Paper rule examples: `«SG» d.` → `dienos`; `«SA» d.` → `dieną`; `«SI» d.`
  → `diena`.
- Guard: these are internal tagged forms; the full written word *diena* follows
  a separate preservation path in the paper.

### K21 — long date without a preposition

- Behavior: assign singular accusative to the day.
- Paper example: `2013 m. sausio 14 d. įvyko` → `du tūkstančiai tryliktų metų
  sausio keturioliktą dieną įvyko`.
- Guard: do not transfer this default to the paper's short-date format.

### K22 — long date missing `m.`

- Behavior: accept the observed irregular form lacking the year abbreviation.
- Paper surface example: `2018 sausio 5 d. baigiasi terminas` is handled as a
  long date despite the missing `m.`.
- Guard: only five source cases motivated this rule; preserve other malformed
  dates rather than repairing them by analogy.

### K23 — long date with a day range

- Behavior: render both days as singular accusative ordinals and the day unit
  as plural instrumental.
- Paper example: `2013 m. sausio 14–15 d.` → `du tūkstančiai tryliktų metų
  sausio keturioliktą penkioliktą dienomis`.
- Guard: the paper accepts observed dash/hyphen spacing and ignores a preceding
  preposition; that dataset choice needs independent review.

### K24 — preposition before a yearless month-name date

- Behavior: insert genitive metadata after a selected preposition so the next
  date rule can consume it.
- Paper example: `Nuo sausio 14 d.` → `Nuo «PG» sausio 14 d.` (intermediate).
- Guard: closed preposition and month lists only.

### K25 — tagged yearless date

- Behavior: normalize month name plus day using inherited preposition case.
- Paper example: `Nuo «PG» sausio 14 d.` → `Nuo sausio keturioliktos dienos`.
- Guard: require the K24 tag or equivalent reviewed parser evidence.

### K26 — yearless date without a preposition

- Behavior: normalize sentence-initial or lowercase month plus day with an
  accusative day.
- Paper example: `Sausio 14 d.` → `Sausio keturioliktą dieną`.
- Guard: capitalization alone must not decide whether a month word is a date.

### K27 — yearless date with a day range

- Behavior: make both days singular accusative and the day unit plural
  instrumental.
- Paper example: `sausio 14–15 d.` → `sausio keturioliktą penkioliktą
  dienomis`.
- Guard: range syntax and both day values must be valid.

### K28 — year and month with `mėn.` under a preposition

- Behavior: make the year genitive and inflect the month unit from inherited
  case.
- Paper example: `iki 2013 m. sausio mėn.` → `iki du tūkstančiai tryliktų
  metų sausio mėnesio`.
- Guard: distinguish year `m.` from metre and month `mėn.` from other senses.

### K29 — year and month with `mėn.` without a preposition

- Behavior: default the month unit to singular accusative.
- Paper example: `2013 m. sausio mėn.` → `du tūkstančiai tryliktų metų sausio
  mėnesį`.
- Guard: require the complete year-month structure.

### K30 — inflect the month abbreviation

- Behavior: expand `mėn.` in genitive, accusative, or instrumental singular.
- Paper rule examples: `«SG» mėn.` → `mėnesio`; `«SA» mėn.` → `mėnesį`;
  `«SI» mėn.` → `mėnesiu`.
- Guard: internal metadata must not survive in final output.

### K31 — year plus nominative month

- Behavior: expand the year marker while retaining a nominative month when no
  day or month abbreviation follows.
- Paper example: `2013 m. sausis` → `du tūkstančiai tryliktų metų sausis`.
- Guard: nominative *sausis* is distinct from genitive *sausio* in full dates.

### K32 — preposition before “this year” date

- Behavior: insert genitive metadata after *nuo*, *iki*, or *ligi* before
  abbreviated or full “this year.”
- Paper example: `Iki š. m. sausio 14 d.` → `Iki š. m. «PG» sausio 14 d.`
  (intermediate).
- Guard: the tag only licenses the subsequent recognized date structure.

### K33 — expand `š. m.`

- Behavior: expand the abbreviation while preserving initial capitalization.
- Paper example: `š. m.` → `šių metų`.
- Guard: exact abbreviation only; do not treat unrelated initials as this
  phrase.

### K34 — tagged short numeric date

- Behavior: stage `YYYY MM DD` or `YYYY-MM-DD` under inherited preposition
  case, turning the month code into metadata.
- Paper example: `Nuo 2013 01 04` → `Nuo 2013-ų metų «01mėn» «SG» 04 «FO»
  «SG» d.` (intermediate).
- Guard: validate separator consistency and the calendar date.

### K35 — numeric month-code mapping

- Behavior: map codes 01–12 to genitive Lithuanian month names.
- Paper rule examples: `«01mėn»` → `sausio`; `«12mėn»` → `gruodžio`.
- Guard: the paper elides mappings 02–11 in print; the semantic month mapping
  is clear, but the exact source regexes are unavailable.

### K36 — short numeric date without a preposition

- Behavior: render the paper's short format with a nominative singular day.
- Paper example: `2013 01 04` → `du tūkstančiai tryliktų metų sausio ketvirta
  diena`.
- Guard: retain this format-specific behavior; it differs from K21.

## Standalone years and year ranges

### K37 — year with *metai* or `m.`

- Behavior: select year case from the full year word, a preposition tag, or a
  default instrumental reading.
- Paper examples: `2001 metus` → `du tūkstančiai pirmus metus`; `iki 2021 m.`
  uses genitive; bare `2001 m.` uses instrumental.
- Guard: the paper restricts this year heuristic to 1500–2059.

### K38 — bare year before punctuation

- Behavior: read a 1500–2059 value before punctuation or end of text as a
  pronominal nominative-plural year.
- Paper example: `Vilniaus universiteto leidykla, 2016.` → `Vilniaus
  universiteto leidykla, 2016-ieji.` before numeral expansion.
- Guard: this is a corpus heuristic; reject identifiers and plausible
  cardinals.

### K39 — compact year range

- Behavior: normalize four-digit endpoints separated by slash, dash, or
  hyphen using inherited genitive/accusative or default instrumental.
- Paper surface examples: `nuo 2008/2009 m.`, `apie 1665–1670 m.`, and
  `(1950 - 1997)`.
- Guard: the printed rules do not check that years are consecutive or infer
  case from the word after the range.

### K40 — explicit *nuo … iki …* year range

- Behavior: stage both year endpoints as genitive ordinals and share the final
  year unit.
- Paper example: `nuo 1981 iki 1986 metų` → `nuo 1981-ų iki 1986-ų «PG» metų`
  before numeral realization.
- Guard: fixed paired-preposition construction only.

## Clock times and ranges

### K41 — time followed by `val.`

- Behavior: read the hour as a singular accusative ordinal and nonzero minutes
  as a cardinal; omit `00` minutes.
- Paper example: `13:15 val.` → `tryliktą valandą penkiolika minučių`.
- Guard: require `val.` and valid 0–24 hour/00–59 minute ranges to avoid scores
  and decimal durations.

### K42 — time under a genitive preposition

- Behavior: inflect the hour and hour unit as singular genitive and minutes as
  plural genitive.
- Paper context example: `iki 13 val.` → `iki tryliktos valandos`.
- Guard: only an established genitive tag licenses this branch.

### K43 — compact time range

- Behavior: rewrite a compact range into explicit *nuo … val. iki … val.* for
  subsequent time rules.
- Paper example: `13.55–14.15 val.` → `nuo 13.55 val. iki 14.15 val.`.
- Guard: both endpoints must be valid times; do not read score ranges as time.

### K44 — explicit time range missing first `val.`

- Behavior: insert the unit after the first endpoint.
- Paper example: `nuo 9:00 iki 16:30 val.` → `nuo 9:00 val. iki 16:30 val.`.
- Guard: exact *nuo … iki … val.* construction only.

### K45 — paired times under one governing tag

- Behavior: copy case metadata to both clock-time conjuncts joined by *ir* or
  *arba*.
- Paper surface examples: `tarp 18.55 val. ir 21.17 val.` and `tarp 3 ir 4
  val.`
- Guard: both conjuncts must be recognized as the same time construction.
