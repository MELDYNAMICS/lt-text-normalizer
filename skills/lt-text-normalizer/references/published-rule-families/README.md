# Published-rule family router

Use this page to load only the rule family needed for the current span. Do not
read every branch for an ordinary normalization request.

1. Classify the candidate span from its full sentence context.
2. Open exactly one primary branch below. Open a second branch only when two
   classes genuinely compete.
3. Use the examples to understand the published behavior and its boundary.
   `Paper example` means the surface or transformation appears in the
   publication. `Schematic example` is an explicitly marked illustration of
   the printed rule semantics, not a quotation or gold label.
4. Treat the published behavior as evidence, not as an executable rule.
   Rewrite only when full context supports one defensible Lithuanian reading;
   otherwise preserve and report the span.

## Branches

| Candidate class | Rule range | Read |
|---|---:|---|
| General rewrite mechanics, cardinal numbers, units, Arabic/Roman ordinals | K01–K18 | [Numbers and ordinals](01-numbers-and-ordinals.md) |
| Calendar dates, years, clock times, and their ranges | K19–K45 | [Dates, years, and times](02-dates-years-and-times.md) |
| Telephone numbers, ISBN/postal/study codes, email addresses, and URLs | K46–K50 | [Telephones, codes, and URLs](03-telephones-codes-and-urls.md) |
| Words read aloud, letter sequences, and expandable abbreviations | K51–K60 | [Abbreviations and letter sequences](04-abbreviations-and-letter-sequences.md) |

For coverage auditing rather than runtime routing, read the
[60-block master catalog](../published-rule-catalog.md). For the small set of
examples checked directly against rendered PDF pages, read
[the provenance examples](../publication-examples.md).

## Shared cautions

- The publication's rules are an ordered cascade; intermediate `«…»` tags in
  examples are implementation metadata, not spoken output.
- The paper reports 1,590 DEL/FLF rules and 771 NAV rules, but publishes only
  60 numbered blocks. “All rules” in this package means every published block,
  not unavailable source code.
- Dataset-specific precedence is not semantic evidence. In particular,
  five-digit codes, Roman numeral plus `a.`, and the abbreviation `m.` vary by
  dataset and context.
- The paper sometimes inserts pronunciation stress. This skill does not copy
  that generated stress into newly normalized words; it preserves only stress
  already present in the user's input.
