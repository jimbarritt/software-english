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

## Work breakdown and tracker pointers: an unconditional sibling of §7.9

The rule `no-work-breakdown-or-tracker-pointer` (SPEC §7.14) covers two
of the faults §7.9 names for a Reference document: a sentence that
divides the subject into units of work, and an issue-tracker id used as
the pointer to later work. It extends both to every document type,
Design, API Design, and PR Description included.

`no-planning-content-in-reference` is conditional on document type,
because most of what it forbids is correct content in a plan, an RFC,
or an ADR. The two narrower faults §7.14 covers are not: a work
breakdown is a scheduling choice, not a fact about the subject, in any
document type, and a tracker id stops resolving for a later reader
wherever it appears. §7.14 therefore has no `applies_to_document_type`
key and takes precedence over §7.9 where both would otherwise match the
same sentence in a Reference document.

§7.14 sits at the end of SPEC §7, after §7.13, rather than beside
§7.9. Every rule in §7 before it is cross-referenced from the TOML
catalogue and from `SPEC.md`'s own Contents list by number; inserting
it as "§7.9a" or renumbering §7.10 onward would break both, for a rule
that is a sibling of §7.9 in concern only, not in its conditioning.

A design document's open-questions and future-extension sections stay
exempt from §7.14, for the same reason §7.9 exempts them: a design
document names what is still unsettled or what a future capability
would add, with no unit of work and no tracker id attached. An entry
that does name one is a §7.14 finding regardless of the section it
sits in.

## PR Description: a type with one conditioned rule

The PR Description type (SPEC Appendix F) has one rule of its own,
`no-check-without-result` (SPEC §7.16). It is conditional on
document type, the way `no-planning-content-in-reference` (§7.9) is,
because the fault depends on the document a sentence is in: a bare
command is correct as a How-to guide step.

`no-abstract-stand-in-for-artefact` (SPEC §7.15) was first written
against PR Description, and is now unconditional. An abstract noun
in place of a named artefact is the same fault in a Reference or a
Design document: `the adapter maps all four shapes to this record`
names neither the payload structures nor the schema. Only its scope
stays conditional. On a PR description it covers the problem
statement and the change statement, the sections a reviewer checks
against the diff. A Reference or a Design document has no such pair
of sections, so the whole document is in scope.

Where §7.15 and `no-metaphor-or-analogy` (§5.5) both match a
structural noun such as `shape`: a form noun standing in for the
fields of a named schema is a §5.5 finding, and a noun standing in
for an artefact the sentence does not name is a §7.15 finding.

Neither rule is a banned-word entry. Each substitute noun has a
correct abstract use (`line coverage rose to 84%`), and a word-list
lookup reads one token, not the document the token is in.

Both rules sit at the end of SPEC §7, after §7.14, for the reason
§7.14 itself sits there: a rule inserted beside §7.9 would renumber
rules the catalogue and the Contents list cite by number.

No standards body defines a pull request description. Appendix F
cites two industry guides that converge on the same content, and the
local reference marks its section structure and both rules as
Software English's own, the same way `templates/design.md` marks its
own open-questions addition.

## Register: a new section, inference-based only

SPEC §8 contains rules on register: rhythm, emphasis, and formatting
patterns that add no fact. These rules sit in a section of their own,
after §7. They judge patterns across sentences and across a whole
document, and that fits neither §3's sentence structure nor §7's
document structure.

Both rules are inference-based. A verbless sentence is detectable only
with part-of-speech tagging, and the linter uses the Python standard
library alone. A repeated bullet or sentence shape is countable with
a pattern. Neither check decides whether the flagged text adds a
fact. Each can flag a candidate for the model pass, but neither meets
§2's test for the deterministic tier. The catalogue therefore has no
deterministic register check.

## Headings: two document rules, judged on the heading alone

The rules `no-withholding-heading` (SPEC §7.17) and
`no-question-or-argument-heading` (SPEC §7.18) judge a heading as a
unit. Each fault occurs only in a heading: in body prose, neither
shape forms a sentence a writer produces.

Both are document rules, beside `no-unanchored-reference` (§7.5), for
the reason §7.5 gives: a heading is also read alone, in a contents
list, a link, or a search result. They are not register rules. §8
judges rhythm and repetition across sentences, and these rules judge
what one heading names.

Both are new entries at the end of §7, after §7.16, for the same
reason §7.14 is there: a rule inserted beside §7.5 would renumber
rules the catalogue and the Contents list cite by number.

Neither rule requires a heading to be a full sentence. A heading that
names a subject (`Retry policy`), or a subject and a property
(`What a session-store entry contains`), passes both. §7.5's own fixed
headings, the noun-phrase headings `templates/technical-manual.md`
recommends, and each template's section names stay correct.

Both are inference-based. The fixed list already contains formulaic
heading phrases (`at a glance`, `the big picture`), and banned-word
catches them. A parser can also flag a heading that ends in a question
mark. Neither check decides whether a heading states its section's
content, so neither meets §2's test for the deterministic tier.
