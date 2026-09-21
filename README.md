# Lithuanian Text Normalizer

[![skills.sh](https://skills.sh/b/MELDYNAMICS/lt-text-normalizer)](https://skills.sh/MELDYNAMICS/lt-text-normalizer/lt-text-normalizer)

An experimental, vendor-neutral Agent Skill that defines how an agent may
convert written Lithuanian into context-appropriate spoken-form Lithuanian.
New expansions remain unaccented, while stress already present in the input is
preserved exactly for pipelines that perform stress restoration separately.

> [!IMPORTANT]
> This repository currently contains agent instructions and a validation
> protocol, not a deterministic Lithuanian normalization engine. Unsupported
> or ambiguous spans must be preserved and reported. Do not use agent output
> as corpus ground truth.

## Repository layout

```text
plugin.json                              portable Agent Plugin manifest
skills/lt-text-normalizer/               canonical Agent Skill
  references/examples.md                 preserve/expand/abstain examples
  references/publication-examples.md     attributed literature examples
  references/published-rule-catalog.md   all 60 published rule blocks
  references/published-rule-families/    class router and per-rule examples
  references/implementation-landscape.md public-code provenance and limits
.codex-plugin/plugin.json                Codex compatibility manifest
.claude-plugin/plugin.json               Claude Code plugin manifest
.claude-plugin/marketplace.json          Claude Code marketplace entry
docs/EVIDENCE.md                         publication alignment and limitations
docs/VALIDATION.md                       behavioral evaluation protocol
scripts/validate_package.py              dependency-free package checks
```

The canonical behavior lives only in
[`skills/lt-text-normalizer/SKILL.md`](skills/lt-text-normalizer/SKILL.md).
Vendor manifests package that same skill; they must not fork its linguistic
rules.

## Use

Give the installed skill Lithuanian text directly:

```text
Normalize this Lithuanian text: Turiu 2 knygas.
```

For a fully resolved input, the skill returns only:

```text
Turiu dvi knygas.
```

No model identifier or normalization declaration is required. The skill accepts
uppercase, lowercase, mixed-case, stressed, partially stressed, and unstressed
input. Ambiguous spans remain unchanged and are reported separately.

## Installation

### skills.sh

Install the skill for a supported agent directly from the public repository:

```bash
npx skills add MELDYNAMICS/lt-text-normalizer
```

### Agent Skills-compatible hosts

Clone this private repository, then install or copy
`skills/lt-text-normalizer/` into the host's skills directory. The
folder follows the [Agent Skills specification](https://agentskills.io/specification).

### Codex and ChatGPT

The repository root is a portable Agent Plugin and also contains a Codex
compatibility manifest. Add the repository through the host's repository or
local plugin flow. The package layout follows OpenAI's
[plugin packaging documentation](https://developers.openai.com/plugins/build/plugins).

### Claude Code

Add the public GitHub repository as a Claude Code marketplace, then install the
plugin:

```text
/plugin marketplace add MELDYNAMICS/lt-text-normalizer
/plugin install lt-text-normalizer@meldynamics-lt-language-tools
```

Claude can select the skill automatically from a normalization request. To
invoke it explicitly, use `/lt-text-normalizer:lt-text-normalizer` followed by
the Lithuanian text. The same skill may also be copied directly into a Claude
skills directory.

### Hermes and other agents

Clone the repository and copy `skills/lt-text-normalizer/` to the
agent's Agent Skills directory. For Hermes, that is normally
`~/.hermes/skills/lt-text-normalizer/`.

## Validate

```bash
python3 scripts/validate_package.py
```

Before any production claim, run the behavioral protocol in
[`docs/VALIDATION.md`](docs/VALIDATION.md) against reviewed Lithuanian gold
fixtures and publish immutable agent, skill, and fixture revisions.
Source-linked, non-gold review candidates are available in
[`tests/literature-candidates.jsonl`](tests/literature-candidates.jsonl).

See the skill's
[`behavioral examples`](skills/lt-text-normalizer/references/examples.md)
for direct normalization, casing, ambiguity, Unicode stress, and output
patterns. The separate
[`publication examples`](skills/lt-text-normalizer/references/publication-examples.md)
retain publication provenance and limitations. The
[`published-rule catalog`](skills/lt-text-normalizer/references/published-rule-catalog.md)
maps every numbered block (1)–(60) in the paper and explicitly records the
unavailable remainder of its reported implementation. The
[`rule router`](skills/lt-text-normalizer/references/published-rule-families/README.md)
splits those rules into four class branches and gives every rule a paper or
clearly marked schematic example plus a usage guard.

For implementation work, the
[`implementation landscape`](skills/lt-text-normalizer/references/implementation-landscape.md)
records pinned public LIEPA-derived code, rule-asset hashes, license signals,
and why those projects must not be represented as the paper's exact system.

## Research and corpus boundary

[`docs/EVIDENCE.md`](docs/EVIDENCE.md) records what the current specification
does and does not implement from the referenced literature. Corpus-derived and
synthetic training artifacts remain governed by the separate
[`lt-stress-and-normalization-corpus`](https://github.com/aleksas/lt-stress-and-normalization-corpus)
project. Runtime acceptance does not authorize reusing an agent's output as a
training label.

## License

This work is licensed under the
[Creative Commons Attribution 4.0 International License](LICENSE). When sharing
or adapting it, credit “MELDYNAMICS — Lithuanian Text Normalizer,” link to this
repository and the license, and indicate material changes.
