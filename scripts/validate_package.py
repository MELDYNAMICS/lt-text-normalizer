#!/usr/bin/env python3
"""Validate the portable skill package without third-party dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME = "lt-text-normalizer"
VERSION = "0.9.2"


def load_json(relative_path: str) -> dict:
    path = ROOT / relative_path
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise AssertionError(f"{relative_path} must contain a JSON object")
    return payload


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def frontmatter_metadata(frontmatter: str) -> dict[str, str]:
    lines = frontmatter.splitlines()
    try:
        start = lines.index("metadata:") + 1
    except ValueError:
        return {}

    metadata: dict[str, str] = {}
    for line in lines[start:]:
        if line and not line.startswith(" "):
            break
        match = re.fullmatch(r"  ([A-Za-z0-9_-]+):\s*(.+)", line)
        if match is not None:
            metadata[match.group(1)] = match.group(2).strip("\"'")
    return metadata


def validate_skill() -> None:
    skill_path = ROOT / "skills" / NAME / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    require(match is not None, "SKILL.md must start with YAML frontmatter")
    frontmatter = match.group(1)
    require(re.search(rf"^name:\s*{re.escape(NAME)}\s*$", frontmatter, re.MULTILINE) is not None,
            "SKILL.md name is missing or inconsistent")
    require(re.search(r"^description:\s*.+$", frontmatter, re.MULTILINE) is not None,
            "SKILL.md description is missing")
    require(frontmatter_metadata(frontmatter).get("version") == VERSION,
            "SKILL.md metadata.version is missing or inconsistent")
    require("references/examples.md" in text,
            "SKILL.md must route demonstrations and fixtures to the examples")
    require("references/publication-examples.md" in text,
            "SKILL.md must route literature-backed fixtures to the cited examples")
    require("references/published-rule-families/README.md" in text,
            "SKILL.md must route normalization classes through the hierarchical rule index")
    require("references/published-rule-catalog.md" in text,
            "SKILL.md must link the complete published-rule catalog for audits")
    require("references/implementation-landscape.md" in text,
            "SKILL.md must route implementation comparisons to the provenance reference")
    require("Do not require a model identifier" in text,
            "SKILL.md must accept text without an integration declaration")
    require("return only the normalized Lithuanian text" in text,
            "SKILL.md must define plain normalized-text output")
    require("report it as unresolved" in text,
            "SKILL.md must preserve and report unresolved spans")
    require("U+0300" in text and "U+0301" in text and "U+0303" in text,
            "SKILL.md must preserve all supported stress marks")
    require(not (skill_path.parent / "references" / "model-input-contract.md").exists(),
            "legacy model-input-contract.md must not be shipped")
    require((skill_path.parent / "references" / "examples.md").is_file(),
            "examples.md is missing")
    require((skill_path.parent / "references" / "publication-examples.md").is_file(),
            "publication-examples.md is missing")
    catalog_path = skill_path.parent / "references" / "published-rule-catalog.md"
    require(catalog_path.is_file(), "published-rule-catalog.md is missing")
    catalog = catalog_path.read_text(encoding="utf-8")
    rows = re.findall(r"^\| `K(\d{2})` \| \((\d+)\) \|", catalog, re.MULTILINE)
    expected = [(f"{number:02d}", str(number)) for number in range(1, 61)]
    require(rows == expected,
            "published-rule catalog must map every block K01-K60 exactly once and in order")
    require("1,590" in catalog and "771" in catalog,
            "published-rule catalog must disclose the unavailable reported rule inventories")
    require("literature_catalogued_only" in catalog,
            "published-rule catalog must declare its non-executable review state")

    implementation_path = skill_path.parent / "references" / "implementation-landscape.md"
    require(implementation_path.is_file(), "implementation-landscape.md is missing")
    implementation = implementation_path.read_text(encoding="utf-8")
    for required_marker in (
        "not_publicly_located",
        "1bdfc01bf0cc094118746c3210565d0dd2a21590",
        "579bd605a703c6eb53a9c7998b253161474c73b1",
        "2baec9a28c0c506075a7c5bd26c86502144d5d95",
        "std::regex_replace",
    ):
        require(required_marker in implementation,
                f"implementation landscape is missing provenance marker: {required_marker}")

    rule_directory = skill_path.parent / "references" / "published-rule-families"
    branch_names = (
        "01-numbers-and-ordinals.md",
        "02-dates-years-and-times.md",
        "03-telephones-codes-and-urls.md",
        "04-abbreviations-and-letter-sequences.md",
    )
    router = rule_directory / "README.md"
    require(router.is_file(), "published-rule family router is missing")
    router_text = router.read_text(encoding="utf-8")
    for branch_name in branch_names:
        require(branch_name in router_text,
                f"published-rule family router does not link {branch_name}")

    sections: dict[int, str] = {}
    for branch_name in branch_names:
        branch_path = rule_directory / branch_name
        require(branch_path.is_file(), f"published-rule branch is missing: {branch_name}")
        branch_text = branch_path.read_text(encoding="utf-8")
        matches = list(re.finditer(r"^### K(\d{2})\b.*$", branch_text, re.MULTILINE))
        for index, match in enumerate(matches):
            rule_number = int(match.group(1))
            require(rule_number not in sections,
                    f"duplicate published-rule example section: K{rule_number:02d}")
            end = matches[index + 1].start() if index + 1 < len(matches) else len(branch_text)
            sections[rule_number] = branch_text[match.start():end]

    require(sorted(sections) == list(range(1, 61)),
            "published-rule branches must contain exactly one section for every rule K01-K60")
    for rule_number, section in sections.items():
        evidence_example = re.search(
            r"^- (?:Paper[^:\n]*\bexamples?\b[^:\n]*|Schematic (?:example|result)):"
            r"[ \t]*\S.*$",
            section,
            re.MULTILINE,
        )
        require(evidence_example is not None,
                f"K{rule_number:02d} must contain a non-empty paper- or "
                "schematic-labelled example")
        require(re.search(r"^- Guard:[ \t]*\S.*$", section, re.MULTILINE) is not None,
                f"K{rule_number:02d} must contain a non-empty guard")


def validate_literature_candidates() -> None:
    path = ROOT / "tests" / "literature-candidates.jsonl"
    require(path.is_file(), "literature candidate fixture file is missing")
    records = []
    identifiers = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(
                f"invalid JSON in {path.relative_to(ROOT)} line {line_number}: {error}"
            ) from error
        require(record.get("review_state") == "literature_candidate_unreviewed",
                f"literature candidate line {line_number} has an invalid review state")
        require("allowed_outputs" not in record,
                f"unreviewed literature candidate line {line_number} must not define gold output")
        require(isinstance(record.get("input"), str) and record["input"],
                f"literature candidate line {line_number} is missing input")
        identifier = record.get("id")
        require(isinstance(identifier, str) and identifier,
                f"literature candidate line {line_number} is missing an id")
        require(identifier not in identifiers,
                f"duplicate literature candidate id: {identifier}")
        identifiers.add(identifier)
        source = record.get("source")
        require(isinstance(source, dict) and source.get("work") and source.get("section")
                and source.get("url"),
                f"literature candidate line {line_number} is missing source provenance")
        require(isinstance(record.get("focus"), list) and record["focus"],
                f"literature candidate line {line_number} is missing test focus")
        require(isinstance(record.get("review_note"), str) and record["review_note"],
                f"literature candidate line {line_number} is missing its review note")
        records.append(record)
    require(records, "literature candidate fixture file is empty")


def validate_manifests() -> None:
    portable = load_json("plugin.json")
    codex = load_json(".codex-plugin/plugin.json")
    claude = load_json(".claude-plugin/plugin.json")
    marketplace = load_json(".claude-plugin/marketplace.json")

    for label, manifest in (("portable", portable), ("Codex", codex), ("Claude", claude)):
        require(manifest.get("name") == NAME, f"{label} manifest name is inconsistent")
        require(manifest.get("version") == VERSION, f"{label} manifest version is inconsistent")

    require(portable.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "portable plugin schema is missing or unsupported")
    require(codex.get("skills") == "./skills/", "Codex manifest must expose ./skills/")
    require(claude.get("skills") == [f"./skills/{NAME}"],
            "Claude manifest must expose the canonical skill")

    plugins = marketplace.get("plugins")
    require(isinstance(plugins, list) and len(plugins) == 1,
            "Claude marketplace must contain exactly one plugin")
    require(plugins[0].get("name") == NAME, "Claude marketplace plugin name is inconsistent")
    require(plugins[0].get("version") == VERSION,
            "Claude marketplace plugin version is inconsistent")


def validate_repository() -> None:
    required = (
        "README.md",
        "AGENTS.md",
        "CITATION.cff",
        "LICENSE",
        "docs/EVIDENCE.md",
        "docs/VALIDATION.md",
    )
    for relative_path in required:
        require((ROOT / relative_path).is_file(), f"required file is missing: {relative_path}")

    skill_directories = sorted(
        path.name for path in (ROOT / "skills").iterdir() if path.is_dir()
    )
    require(skill_directories == [NAME],
            "skills directory must contain only the canonical named skill")

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    require(re.search(rf"^version:\s*[\"']?{re.escape(VERSION)}[\"']?\s*$",
                      citation, re.MULTILINE) is not None,
            "CITATION.cff version is missing or inconsistent")
    evidence = (ROOT / "docs" / "EVIDENCE.md").read_text(encoding="utf-8")
    require(f"Version {VERSION}" in evidence,
            "docs/EVIDENCE.md version is missing or inconsistent")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    require("Creative Commons Attribution 4.0 International Public License"
            in license_text and "Section 8 -- Interpretation" in license_text,
            "LICENSE must contain the canonical CC BY 4.0 legal text")

    unfinished_marker = "[" + "TODO:"
    for path in ROOT.rglob("*"):
        is_text_source = path.suffix in {".cff", ".json", ".md", ".py", ".txt", ".yaml", ".yml"}
        if path.is_file() and ".git" not in path.parts and is_text_source:
            require(unfinished_marker not in path.read_text(encoding="utf-8"),
                    f"unfinished scaffold marker in {path.relative_to(ROOT)}")


def main() -> None:
    validate_skill()
    validate_literature_candidates()
    validate_manifests()
    validate_repository()
    print(f"Package validation passed: {ROOT}")


if __name__ == "__main__":
    main()
