# Abbreviations and letter sequences: K51–K60

Choose among “read as a word,” “spell as letters,” “expand,” and “leave
unchanged” before applying a rule. These branches are lexicon-heavy and the
paper sometimes inserts synthesizer-oriented stress; generated stress is not
part of this skill's output.

## Abbreviations or foreign words read as words

### K51 — selected foreign-letter transliteration

- Behavior: replace listed non-Lithuanian letters with Lithuanian
  pronunciation-oriented spellings.
- Paper examples: `Czesławą Miłoszą` → `Czeslavą Miloszą`; `Münsterio` →
  `Miunsterio`.
- Guard: only `ł` and `ü` transformations are printed; this is not a general
  transliteration standard.

### K52 — lexicon entries read as words

- Behavior: remove an abbreviation-final period or add synthesizer-oriented
  stress for selected entries that should be pronounced as words.
- Paper examples: `prof.` is read as *prof* without the abbreviation period;
  `BUS` and `ARKSI` receive pronunciation stress in the paper's output.
- Skill rendering example: `prof.` → `prof`; preserve `BUS` or `ARKSI`
  unchanged unless a reviewed unstressed rendering can represent the intended
  pronunciation without inventing stress.
- Guard: closed lexicon only; do not strip arbitrary terminal periods.

### K53 — foreign navigation words

- Behavior: apply a pronunciation-oriented Lithuanian transcription to a
  closed list of foreign street/road/avenue words.
- Paper examples, shown here without paper-added stress: `Ulica` → `Ulyca`;
  `Strasse` → `Štrase`; `Avenue` → `Aveniu`.
- Guard: navigation-domain lexicon only. The unstressed spellings require
  Lithuanian review before runtime enablement.

## Letter sequences

### K54 — detect consonant-only abbreviations

- Behavior: tag every consonant for spelling and mark the final one for the
  paper's accented letter-name realization.
- Schematic example: `LSP` → `«Spell»L«Spell»S«SpellA»P`.
- Guard: the paper used seven separate length rules for 1–7 letters and prints
  only the three-letter form. Boundaries must exclude ordinary word material.

### K55 — realize tagged consonant names

- Behavior: convert `Spell`/`SpellA` tags to Lithuanian letter names, with the
  paper accenting the final name.
- Paper-level example: `LSP` → `el-es-pė` when generated stress is omitted for
  downstream stress restoration.
- Guard: the printed block shows consonant groups rather than a complete
  machine-readable alphabet; internal tags must not survive.

### K56 — dictionary spelling for uppercase sequences with vowels

- Behavior: use explicit abbreviation entries when consonant-only detection
  cannot apply.
- Paper examples, shown without generated stress: `VU` → `vė-u`; `SA` →
  `es-a`; `BKKI` → `bė-ka-ka-i`.
- Guard: closed dictionary only. The paper discusses but does not implement a
  fallback for every short uppercase word.

## Abbreviations expanded to words

### K57 — stable abbreviation dictionary

- Behavior: expand a closed list whose meanings are treated as stable in the
  source domain.
- Paper examples: `pvz.` → `pavyzdžiui`; `t. y.` → `tai yra`; `angl.` →
  `angliškai`; `el. p.` → `elektroninis paštas`.
- Guard: keep each surface in an explicit lexicon and preserve capitalization
  where the rule defines it.

### K58 — sentence-final abbreviation dictionary

- Behavior: expand selected phrases while retaining one terminal period.
- Paper examples: `ir kt.` → `ir kita.`; `ir pan.` → `ir panašiai.`; `ir t.
  t.` → `ir taip toliau.`
- Guard: distinguish the abbreviation's period from sentence punctuation and
  never duplicate it.

### K59 — context-inflected `vyr.`

- Behavior: infer an inflected expansion of “senior/chief” from the following
  word ending.
- Paper examples: `vyr. redaktorės` → `vyriausiosios redaktorės`; `vyr.
  redaktorė` → `vyriausioji redaktorė`; `vyr. redaktorius` → `vyriausiasis
  redaktorius`.
- Guard: the paper explicitly calls this approach complex and error-prone and
  recommends leaving such forms unchanged. Default action is abstention.

### K60 — context-inflected `šv.`

- Behavior: infer an inflected expansion of “saint/holy” from the following
  name or noun ending.
- Paper examples: `Šv. Jonų` → `Šventų Jonų`; `šv. Kalėdų` → `šventų
  Kalėdų`; `Šv. Onos` → `Šventos Onos`; `Šv. Jeronimo` → `Švento Jeronimo`.
- Guard: the paper also recommends not expanding this family because reliable
  morphology is difficult. Default action is abstention; one printed
  replacement appears suspicious and needs source-author clarification.
