# Repository instructions

## Mission

Maintain a portable, evidence-bounded Agent Skill for Lithuanian
written-to-spoken normalization, including preparation for stress restoration.

## Invariants

- Keep `skills/lt-text-normalizer/SKILL.md` vendor-neutral and canonical.
- Keep vendor manifests thin; do not duplicate linguistic rules in them.
- Do not claim that the repository implements the Kasparaitis rule system
  until rule-level coverage and reviewed evaluations exist.
- Keep all 60 numbered Kasparaitis publication blocks represented in
  `references/published-rule-catalog.md`. Catalog completeness is not
  executable-rule coverage or release approval.
- Keep exactly one section with at least one example and a guard for each
  K01–K60 block under `references/published-rule-families/`, and preserve
  paper-versus-schematic labels.
- Keep public implementation claims pinned and provenance-bounded in
  `references/implementation-landscape.md`; never equate a LIEPA-derived
  repository with the paper's system without direct evidence.
- Preserve stress-bearing source spans code-point-exactly, including combining
  grave, acute, and tilde marks; newly expanded words remain unstressed.
- Preserve and report unresolved spans instead of guessing.
- Never present agent output as corpus or synthetic ground truth.
- Do not add an open-source license without an explicit maintainer decision.
- Keep manifest and skill versions synchronized.

## Validation

Run `python3 scripts/validate_package.py` after every packaging or skill change.
Behavioral releases must additionally satisfy `docs/VALIDATION.md` using
reviewed fixtures.

## Skills Directory listing

The listing is <https://www.skillsdirectory.com/skills/meldynamics-lt-text-normalizer>.
The maintainer's API key is `SKILLS_DIRECTORY_API_KEY` in the untracked,
gitignored `.env` at the repository root. Load it into the environment and
send it as the `x-api-key` header; never print, log, or commit its value.

```bash
set -a; . ./.env; set +a
curl -s -H "x-api-key: $SKILLS_DIRECTORY_API_KEY" \
  https://www.skillsdirectory.com/api/v1/skills/meldynamics-lt-text-normalizer
```

API reference: <https://www.skillsdirectory.com/api-docs>. After a release,
check that the listing shows the new version; if it does not, ask the
maintainer to resync it from the Skills Directory dashboard.
