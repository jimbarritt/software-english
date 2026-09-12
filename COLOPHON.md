# Colophon

Notes on format and tooling choices for this project.

## Rule catalogue format: TOML

The machine-readable rule catalogue ([`rules/core-rules.toml`](rules/core-rules.toml))
is TOML. The enforcement plugin
([`claude-plugins/software-english-lint`](https://github.com/jimbarritt/claude-plugins/tree/main/software-english-lint))
is a Python script with no third-party dependencies — Python's standard
library only.

YAML has no standard-library parser in Python. Parsing it would need
PyYAML as a dependency, or a hand-written parser for the YAML subset in
use — a hand-written parser is unsafe here, because an editor treats the
file as full YAML, so a contributor can use a construct the hand-written
parser does not accept, and the failure is silent or cryptic.

TOML has had a standard-library parser (`tomllib`) since Python 3.11.
Its `[[rules]]` array-of-tables, string arrays, and multi-line strings
cover every field shape the catalogue needs, comments included. The
linter parses the catalogue directly with `tomllib`; it does not
hardcode a duplicate copy of the rules in Python.

JSON also has a standard-library parser (`json`) but does not support
comments, and a multi-line rule description would need an escaped `\n`
sequence instead of a natural line break. Both properties make a diff or
a direct read of the file harder to follow than the same change in TOML.

## Vocabulary format: TSV, not CSV

The vocabulary files ([`vocabulary/*.tsv`](vocabulary/)) are
tab-separated, not comma-separated. Every sense and fix column holds
ordinary English prose, and a comma appears in that prose constantly
(`name the action: read, write, upload, fetch, call`). A comma-separated
format would need every such field quoted, and any quote character
inside the field escaped. A tab does not appear in ordinary English
prose, so a plain split on tab needs no quoting or escaping. The linter
parses each row with a single `line.split("\t")` call — no CSV-parsing
library, no quoting logic.

GitHub's own file preview applies CSV-style quote rules to a `.tsv`
file: a double quote is legal only wrapping an entire field, never
mid-field. An in-line quoted word therefore uses a single quote instead
(`present tense of 'to be', singular`), which is not a special character
to that parser.
