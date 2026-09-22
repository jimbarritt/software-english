# Colophon

Notes on format and tooling choices for this project.

## Rule catalogue format: TOML

The machine-readable rule catalogue ([`rules/core-rules.toml`](rules/core-rules.toml))
is TOML. The enforcement plugin
([`claude-plugins/software-english-lint`](https://github.com/jimbarritt/claude-plugins/tree/main/software-english-lint))
is a Python script with no third-party dependencies: Python's standard
library only.

YAML has no standard-library parser in Python. Parsing it would need
PyYAML as a dependency, or a hand-written parser for the YAML subset in
use. A hand-written parser is unsafe here, because an editor treats the
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
parses each row with a single `line.split("\t")` call: no CSV-parsing
library, no quoting logic.

GitHub's own file preview applies CSV-style quote rules to a `.tsv`
file: a double quote is legal only wrapping an entire field, never
mid-field. An in-line quoted word therefore uses a single quote instead
(`present tense of 'to be', singular`), which is not a special character
to that parser.

## Unanchored references: a document rule, inference-based

The rule `no-unanchored-reference` ([SPEC §7.5](spec/SPEC.md)) covers a
definite reference (`the design`, `the decision`, `the plan`,
`this change`) with no antecedent inside the document.

It is not a banned-word entry. Each phrase is correct when the document
defines its referent: a document that defines a design can call it
`the design`. Only the absence of an antecedent makes the phrase a
fault, and a word-list lookup reads one token, not the whole document.
The check therefore needs model judgement, so the rule is
inference-based.

It is a document rule, not a semantic rule, because the unit of the
check is the whole document: the same sentence passes in one document
and fails in another.

It is separate from `no-process-narration` (SPEC §7.7). That rule covers
prose that narrates a decision's history. An unanchored reference
narrates nothing; it names a thing the document does not identify. Both
faults come from the same source: prose moved from a conversation,
where the referent is shared, into a standalone document. Each fails on
a different mechanism, so each has its own rule.

## Planning content in a reference document: a conditional document rule

The rule `no-planning-content-in-reference` ([SPEC §7.9](spec/SPEC.md))
forbids planning or task-oriented content in a document of Diátaxis type
Reference: an open question, a next step, a statement of who does work or
when, a pointer to a plan document, or a statement of the document's own
purpose relative to a task in progress.

It is conditional on document type. Every other rule in SPEC §7 applies
to every document. This rule fires only after `document-type-template`
(SPEC §7.8) assigns the type Reference, because the same content is
correct in a plan, an RFC, or an ADR. The rule is §7.9, directly after
§7.8, for that reason.

It is Software English's own addition, not Diátaxis's wording.
Diátaxis's "describe, and only describe" guidance implies it but names no
concrete category for planning content. The local reference
([`templates/reference.md`](templates/reference.md)) marks the addition
as such, so a reader does not take it for Diátaxis's own text.

It is inference-based. Recognising planning content needs judgement:
`the plan` is correct in a plan document, and a pointer that states where
planning content belongs is itself planning content. A word-list lookup
cannot tell these apart.

It is separate from `no-process-narration` (SPEC §7.7) and
`no-unanchored-reference` (SPEC §7.5). Process narration is a decision's
history; an unanchored reference is a missing antecedent. Planning
content can be fully anchored and narrate nothing (a pointer to a plan
at a stated path) and still fail this rule, because a reference
document describes and does nothing else.
