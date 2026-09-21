# Telephones, codes, and URLs: K46–K50

These classes usually require digit-by-digit or symbol-by-symbol readings.
Classify them before any cardinal/year/date rule sees their digits.

## Telephone numbers

### K46 — telephone cue and digit separation

- Behavior: expand a telephone label, verbalize an international plus sign,
  and separate digits for digit-by-digit reading.
- Paper surface examples: `tel. 123 45 67`, `Tel. (8 5) 123 4567`, `Tel. 8
  612 34567`, and `T.: +370 612 34567`.
- Schematic result: `Tel. 8 612 34567` → `Telefonas 8 6 1 2 3 4 5 6 7`.
- Guard: require a telephone cue and a currently valid numbering grammar. The
  publication describes the numbering plan in force at its source date.

## Codes

### K47 — ISBN

- Behavior: spell the `ISBN` label and separate a 10- or 13-digit ISBN into
  individual digits, ignoring printed separators.
- Paper surface examples: `ISBN: 1909232424` and `ISBN
  978-609-420-425-8`.
- Schematic result: the second identifier's numeric part becomes `9 7 8 6 0 9
  4 2 0 4 2 5 8` after the label is spelled.
- Guard: the printed block does not validate the ISBN checksum. The paper adds
  pronunciation stress to letter names; this skill's default output does not.

### K48 — five-digit postal code

- Behavior: separate all five digits.
- Paper example: `03123 Vilnius` → `0 3 1 2 3 Vilnius`.
- Guard: this was valid for NAV/FLF, while DEL five-digit numbers were
  cardinals. Require postcode or domain evidence.

### K49 — study-program code

- Behavior: split the numeric parts of the observed parenthesized code while
  retaining `NX`.
- Paper example: `(6121NX025)` → `(6 1 2 1 NX 0 2 5)`.
- Guard: this is a fixed FLF-specific code shape, not a general alphanumeric
  identifier rule.

## Email addresses and URLs

### K50 — URL/email punctuation

- Behavior: verbalize `@`, remove protocol punctuation and nonnumeric slashes,
  and verbalize a dot between sufficiently long letter sequences.
- Paper example: `vardas.pavardenis@cr.vu.lt` is read with *taškas* for dots
  and *eta* for `@`.
- Schematic example: `aa@bb.lt` → `aa eta bb taškas lt` before any
  abbreviation spelling.
- Guard: the paper explicitly does not identify whole URLs. A new
  implementation should first parse a bounded URL/email span so these
  substitutions cannot alter ordinary punctuation or numeric fractions.
