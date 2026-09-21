#!/usr/bin/env python3
"""Writes rules/core-rules.yaml from rules/core-rules.toml.

The TOML file is the catalogue. SPEC Appendix A names it, and the swe
plugin parses it directly. The YAML file holds the same catalogue for a
reader or a tool that reads YAML, and nothing reads it today.

The two were kept in step by hand until 2026-09-21, and had drifted: the
YAML held 10 of the catalogue's 20 rules, cited SPEC §7.6 for a rule the
TOML places at §7.8, and carried a note claiming the reference
implementation hardcoded its rules in Python, which stopped being true
once the plugin began parsing the TOML. Generating the YAML removes the
hand step that allowed any of that.

Usage:
  scripts/generate-rules-yaml.py            writes rules/core-rules.yaml
  scripts/generate-rules-yaml.py --check    exits 1 if the file on disk
                                            differs from the output
  scripts/generate-rules-yaml.py --stdout   writes to stdout

Standard library only: this repository carries no dependencies, and a
catalogue that needs an installed package to regenerate would be one
more thing to keep working.
"""

import sys
import textwrap
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOML_PATH = ROOT / "rules" / "core-rules.toml"
YAML_PATH = ROOT / "rules" / "core-rules.yaml"

# Written first on every rule, in this order, so a reader meets each rule
# the same way. Every other field follows in the order the TOML gives it.
LEADING_FIELDS = ("id", "tier", "check", "severity", "description")

HEADER = """\
# Software English rule catalogue, in YAML.
#
# GENERATED FILE. Do not edit by hand. Edit rules/core-rules.toml, then
# run scripts/generate-rules-yaml.py. CI checks that this file matches
# what that script produces.
#
# rules/core-rules.toml is the catalogue itself: SPEC Appendix A names
# it, and the swe plugin parses it directly. This file holds the same
# rules for a reader or a tool that reads YAML.
#
# Each entry names a tier ("deterministic" or "inference-based") and a
# severity ("error", blocking, or "warning", advisory-only). See
# SPEC.md §2.
"""


def quote(value):
    """A double-quoted YAML scalar. Used for every string outside a
    description, so a regular expression, an em dash, or a leading
    indicator character needs no case of its own."""
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def scalar(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    return quote(str(value))


def folded(text, indent):
    """A folded block scalar (>-), wrapped. A block scalar holds a colon,
    an em dash, and a quote mark literally, so a description needs no
    escaping and stays readable."""
    pad = " " * indent
    # break_on_hyphens must stay off: wrapping "learning-oriented" across
    # two lines makes the folded scalar rejoin it as "learning- oriented",
    # which corrupts the rule text with nothing to show for it.
    # break_long_words likewise, so a long token stays whole.
    lines = textwrap.wrap(
        " ".join(text.split()),
        width=72 - indent,
        break_on_hyphens=False,
        break_long_words=False,
    )
    return "\n".join(pad + line for line in lines)


def emit_field(name, value, indent):
    pad = " " * indent
    if isinstance(value, list):
        if not value:
            return f"{pad}{name}: []"
        items = "\n".join(f"{pad}  - {scalar(v)}" for v in value)
        return f"{pad}{name}:\n{items}"
    return f"{pad}{name}: {scalar(value)}"


def render(catalogue):
    out = [HEADER, f'version: {quote(str(catalogue["version"]))}', "", "rules:"]

    for rule in catalogue["rules"]:
        out.append(f'  - id: {quote(rule["id"])}')
        for name in LEADING_FIELDS:
            if name == "id" or name not in rule:
                continue
            if name == "description":
                out.append("    description: >-")
                out.append(folded(rule["description"], 6))
            else:
                out.append(emit_field(name, rule[name], 4))
        for name, value in rule.items():
            if name in LEADING_FIELDS:
                continue
            out.append(emit_field(name, value, 4))
        out.append("")

    exemptions = catalogue.get("exemptions")
    if exemptions:
        out.append("exemptions:")
        for name, value in exemptions.items():
            out.append(emit_field(name, value, 2))
        out.append("")

    return "\n".join(out).rstrip("\n") + "\n"


def main():
    args = set(sys.argv[1:])
    with TOML_PATH.open("rb") as f:
        catalogue = tomllib.load(f)
    text = render(catalogue)

    if "--stdout" in args:
        sys.stdout.write(text)
        return 0

    if "--check" in args:
        current = YAML_PATH.read_text() if YAML_PATH.exists() else ""
        if current == text:
            print(f"{YAML_PATH.relative_to(ROOT)} matches core-rules.toml.")
            return 0
        print(
            f"{YAML_PATH.relative_to(ROOT)} does not match core-rules.toml.\n"
            "Run scripts/generate-rules-yaml.py and commit the result.",
            file=sys.stderr,
        )
        return 1

    YAML_PATH.write_text(text)
    print(f"Wrote {YAML_PATH.relative_to(ROOT)} from core-rules.toml "
          f"({len(catalogue['rules'])} rules).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
