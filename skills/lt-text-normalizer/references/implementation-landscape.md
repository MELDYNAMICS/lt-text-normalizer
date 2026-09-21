# Implementation landscape

Observed: 2026-09-20. This reference separates the implementation described by
Kasparaitis from older public Lithuanian TTS normalizers. Read it only when
reproducing, implementing, or comparing engines; ordinary inference should use
the class-level rule router instead.

## Exact publication implementation

Kasparaitis's [arXiv:2312.17660v2 paper](https://arxiv.org/abs/2312.17660)
says its normalizer uses C++
`std::regex_replace`, with all rules in one ordered file. It reports 1,590
DEL/FLF rules and 771 NAV rules. No repository, source-code link, rule-file
download, or supplementary artifact is identified in the paper.

Inspected artifacts:

- PDF SHA-256:
  `50266a8d2b32aa4d53c72076cea4d5a2dfa1ed5c44b7810587f83c27c443eb99`
- arXiv v2 source archive SHA-256:
  `36019e70bb2bbcb2aabcc19034309c9c5e0cc2969f96b52494f1e6be1ce4b1ea`
- source-archive contents: `regex_PK_Arxiv.tex`, `regex_PK_Arxiv.bbl`, and
  `PRIMEarxiv.sty` only

The exact executable system is therefore `not_publicly_located`, not proven
absent. To claim a reproduction, obtain from the author the ordered DEL/FLF
and NAV rule files, evaluation tables, encoding, build instructions, version
identifier, and reuse terms.

Search boundary: the check covered the arXiv metadata and v2 source archive,
exact-title/author searches, public GitHub repository and code searches for the
paper title, author address, and distinctive printed-rule literals, plus the
trees of the related repositories below. No exact-system result was found.
This is a dated public-artifact search, not proof that private, offline, or
later-published files do not exist.

## Related public implementations

These repositories are useful engineering references, but none is evidence of
the exact 2024 paper system.

### LIEPA/LithUSS in `aleksas/laba-diena-tts`

- Repository: <https://github.com/aleksas/laba-diena-tts>
- Inspected revision:
  `1bdfc01bf0cc094118746c3210565d0dd2a21590`
- Declared repository license: BSD-2-Clause
- Relevant engine:
  [`native-modules/TextNormalization/TextNormalization.cpp`](https://github.com/aleksas/laba-diena-tts/blob/1bdfc01bf0cc094118746c3210565d0dd2a21590/native-modules/TextNormalization/TextNormalization.cpp)
- Rule dispatcher:
  [`rules.txt`](https://github.com/aleksas/laba-diena-tts/blob/1bdfc01bf0cc094118746c3210565d0dd2a21590/applications/android/app/src/main/assets/liepa_rules/rules.txt),
  92 lines, SHA-256
  `3743a2f685d2e630eb48bd6eddfa162ad86bcaf6f61efc30fbe121bd8c3809bf`
- Numeral/ordinal replacements:
  [`skaitm.txt`](https://github.com/aleksas/laba-diena-tts/blob/1bdfc01bf0cc094118746c3210565d0dd2a21590/applications/android/app/src/main/assets/liepa_rules/skaitm.txt),
  1,036 lines, SHA-256
  `346a81cf7d8f7eda4e0c565d7f847691a71f4c04f2b7eb1a458fb2119cba6130`

The normalization source identifies the LIEPA project, Tomas Anbinderis, and
2015. The repository says its source came from the LIEPA speech-synthesizer
distribution. It uses a custom directive format such as `Date`, `Numbers`, and
`ReplaceWithFile`, not the paper's stated ordered `std::regex_replace` file.

### `liepa-project/liepa2-nao_sintezatorius`

- Repository: <https://github.com/liepa-project/liepa2-nao_sintezatorius>
- Inspected revision:
  `579bd605a703c6eb53a9c7998b253161474c73b1`
- Declared repository license: MIT
- [`rules.txt`](https://github.com/liepa-project/liepa2-nao_sintezatorius/blob/579bd605a703c6eb53a9c7998b253161474c73b1/src/liepaTTS/src/rules.txt):
  57 lines, SHA-256
  `03beeeda4a20af9f09719506d7e6ec8ef992cf94cf20f3a083db86f6290b6b12`
- [`skaitm.txt`](https://github.com/liepa-project/liepa2-nao_sintezatorius/blob/579bd605a703c6eb53a9c7998b253161474c73b1/src/liepaTTS/src/skaitm.txt):
  781 lines, SHA-256
  `22e0fd2e53382f455656a82f0ac52e845a1160fbe559fbd9c72ee4320d7630df`

This is another older LIEPA-derived custom-rule implementation. Its formats,
counts, and revision history do not match the publication's reported system.

### `aleksas/phonology_engine`

- Repository: <https://github.com/aleksas/phonology_engine>
- Inspected revision:
  `2baec9a28c0c506075a7c5bd26c86502144d5d95`
- The repository includes a C++ `TextNormalization` component derived from the
  older Lithuanian TTS stack.
- GitHub exposes no SPDX license for the inspected revision. Treat it as
  reference-only unless reuse rights are established separately.

## Reuse and comparison rules

1. Do not label any related repository as “the Kasparaitis 1,590-rule
   implementation” without provenance connecting its files to the paper.
2. Pin every inspected repository revision and hash imported rule assets.
3. Audit file-level provenance and licensing, not only the repository badge;
   bundled LIEPA assets may have their own history or terms.
4. Detect and convert the legacy character encoding explicitly. Do not repair
   mojibake by visual guesswork.
5. Keep synthesizer-oriented capitalization, syllable markers, and generated
   stress out of this skill's unaccented normalized output.
6. Compare behavior using reviewed fixtures by semantic class. Similar rule
   counts or examples do not establish equivalence.
7. Record reusable behavior as a separately provenanced project extension,
   not as a missing publication rule.
