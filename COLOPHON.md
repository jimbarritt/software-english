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
tab-separated, not comma-separated. Every sense and fix column
contains ordinary English prose, and a comma appears in that prose
constantly (`name the action: read, write, upload, fetch, call`). A
comma-separated format would need every such field quoted, and any
quote character inside the field escaped. A tab does not appear in
ordinary English prose, so a plain split on tab needs no quoting or
escaping. The linter
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
faults have the same source: prose moved from a conversation,
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

Every rule in §8 is inference-based. A verbless sentence is detectable
only with part-of-speech tagging, and the linter uses the Python
standard library alone. A repeated bullet or sentence shape is
countable with a pattern. Neither check can show whether the flagged
text adds a fact. Each can flag a candidate for the model pass, but
neither meets §2's test for the deterministic tier. The catalogue
therefore has no deterministic register check.

§8.3, no-distributive-tail, is inference-based for the same reason. A
pattern finds `, and each` after a count. It cannot tell a property of
the document's layout from a property of the subject matter.

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
mark. Neither check can show whether a heading states its section's
content, so neither meets §2's test for the deterministic tier.

## Count and list: inference-based at error severity

§7.20, no-count-list-mismatch, started as a request for a fully
deterministic, blocking check: a number word before a colon list or an
and/or list, where the item count differs. A prototype of that literal
check, run against both this repository's and `claude-plugins`' own
real prose, found 15 matching sentences and flagged 7 of them. Every
one of the 7 was a false positive: an explanatory colon (`on both
flags: a pending rule is never a finding`), a quantity (`state the
result in one or two lines`), and a list item that itself contains
`or`/`and` (`two transports: an HTTP API, and an event or message API
over Kafka`).

The rule's own worked example shows why a comma alone cannot decide
this: `one of two modes: on the primary queue, with a priority flag,
or on a queue of its own` reads as three comma-separated items, or as
two items where `with a priority flag` modifies the first. The same
comma marks both a separator and a modifier boundary, and only
judgement separates them. §2's deterministic-tier bar needs a lookup
or a regular grammar with no interpretation of meaning; splitting
this list fails that test, so the rule stays inference-based.

The "error, not warning" half of the request still applies: tier and
severity are independent (§2), so §7.20 is the catalogue's first
inference-based rule at `error` severity. A finding under it states a
wrong fact, not a style preference, so a blocking severity fits even
where a model, not a lookup, makes the call.

`claude-plugins`' `swe` plugin adds a located-candidate detector for
this rule and for `define-before-use` (§7.4, newly catalogued by the
same change): deterministic Python that finds a site worth judging,
with no judgement of the fault itself, and no entry onto the findings
list.
The pattern is the same one `register_candidates_test.sh` and
`definite_phrase_candidates_test.sh` already establish for §8's and
§7.19's rules.

## Whole-document rules: three entries from a whole-file pass

`claude-plugins`' `/swe:lint-file` has a third pass that reads a whole
document, for faults that span more than one heading, paragraph, or
list item. That pass used three rule ids of its own, with no entry in
`rules/core-rules.toml`. Each now has a catalogue entry:
`summary-before-detail` (SPEC §7.1), `no-contradiction-between-sections`
(§7.21), and `no-precedent-before-subject` (§7.22).

§7.1 existed as one sentence with no catalogue entry. It keeps its
number. Its text now states what a summary is, its position in a
document, and two faults. The rule fires on every document type and at
every length.
lint-file's pass applies it only to a Design or an API Design document
of 300 lines or more. That narrower trigger is the tool's own choice,
the same way the pass applies §8.2 and §7.5 past one unit.

§7.21 and §7.22 are new entries at the end of §7, after §7.20, for the
same reason earlier additions went there: a rule inserted beside §7.1
or §7.10 would renumber rules the catalogue and the Contents list cite
by number.

§7.21 runs at `warning` severity, unlike §7.20. Both faults include a
false fact. The §7.20 fault is inside one sentence, and counting its
list checks it. The §7.21 fault spans sections. A scoped rule, a named
exception, or a recorded history reads as a contradiction until a
model judges the scope of each statement.

All three are inference-based. A parser can find a status marker, the
text before the first heading, or a section's paragraphs. None of
those checks can show whether two statements contradict each other,
whether a summary states the main fact, or which subject a paragraph
describes, so none meets §2's test for the deterministic tier.

## Reader-reaction prediction: one catalogued fault inside §5.3

§5.3 names three faults in one sentence: an editorial judgement, a
guess at how someone might react, and a remark about the writing. None
had a catalogue entry, so the inference tier had no rule id to judge a
prediction against. `no-reader-reaction-prediction` catalogues the
second fault, with advice that states no consequence included. §5.3
keeps its number; its text now states the fault, the fix, and what is
not the fault.

The rule is inference-based. A sentence with "you" as its subject can
be an instruction, a consequence, or a prediction, and only the stated
consequence separates them. The same is true of "it helps to", where
"it" can name a component. Five phrases with no correct use went into
`vocabulary/banned.tsv`: `you will be glad`, `you'll be glad`,
`before you find out`, `exactly what you want`, and
`may be what you want`. None occurred in either repository's prose
when they were added.

## Remark about the writing: a second catalogued fault inside §5.3

§5.3's third fault, a remark about the writing, had fixed phrases in
`vocabulary/banned.tsv` and no catalogue entry, so the inference tier
had no rule id to judge a paraphrase against. A navigational
announcement (`this is where the signing certificate comes in`) was
the false negative. `no-remark-about-the-writing` catalogues the third
fault, with the navigational announcement as one named form. §5.3
keeps its number.

It is not a fourth shape of §5.10. A framing device wraps a fact, and
its fix is the plain clause. A navigational announcement wraps none:
its plain clause ("the next section is for that") still states no
fact, so the fix deletes the sentence.

`comes in` and `come in` went into `vocabulary/banned.tsv`. The
anthropomorphism fixed list already reported `comes` in them, with a
fix that names a mechanism. "this is where" and "here is where" did
not, since "this is where the service writes its logs" names a
directory. Neither phrase occurred in either repository's prose when
they were added.

## Split contrast pair: a fourth catalogued fault beside §8's siblings

A full inference pass recorded a document clean while one list item
still read as model-generated. The shape was a run of three short
sentences: the first named A and B, the second stated a property of A
alone, and the third stated B's property in comparative form, with
its comparand only in the sentence before.
Each sentence states a fact alone, so a unit-by-unit judgement passed
all three.

None of the three rules the report named covers the shape.
`no-clipped-sentence-run` (§3.6) needs a pronoun chain with a changing
referent, and its own "not this fault" list excludes a run of named
subjects and a list item, both true here. `no-contrastive-framing`
(§5.7) needs an unstated, unasked case; both sides of this comparison
are stated. `no-entailed-restatement` (§7.12) needs a clause that
follows from the fact before it; the middle sentence here is not
entailed by the first, so cutting it would lose a fact.

`no-split-contrast-pair` catalogues the shape as §8.4, a new entry at
the end of §8 for the same reason §7.21 and §7.22 went at the end of
§7: a rule inserted beside §8.1 would renumber rules the catalogue and
the Contents list cite by number.

The fault does not depend on sentence length or on a pronoun, so §3.6
and §8.4 do not overlap: §3.6 excludes a list item on purpose, and
§8.4 includes one on purpose. The `claude-plugins` lint-file worklist
already judges each list item as one unit, so the rule needed no
change to that plugin's code, only a release-pin bump.

The rule is inference-based. A parser can find a comparative word, but
whether its comparand is in its own sentence needs judgement.

## Scope preamble: a new document rule at the end of §7

A caption above a table stated what the table showed, and both tiers
passed it. `no-remark-about-the-writing` (§5.3) judges a navigational
announcement, and it excludes `§4 lists the retry limits` on purpose,
since a reader can follow that reference to a fact. The caption had the
same grammar, with the block below it as the subject. The count
signpost in §7.6 needs a number word at the head of the sentence, and
the caption had none. §7.1 judges only the document's opening
paragraph.

`no-scope-preamble` catalogues the fault as §7.23: a sentence whose
subject is the document, the section, or the block it is in, and that
states only what the block after it shows. It is the body-level form
of §7.1's second fault. It is the last entry in §7, for the same
reason §7.21 and §7.22 are: an insertion would renumber rules the
catalogue and the Contents list cite by number.

The rule is inference-based. A parser can find `this section lists`,
but whether the block after it shows everything the sentence states
needs judgement. No phrase went into `vocabulary/banned.tsv`: `the
table lists only the regions that accept writes` states a fact the
table does not show. The claude-plugins lint-file worklist already
judges each paragraph and table as one unit, so the rule needed no
change to that plugin's code, only a release-pin bump.

## Scope escalation: a mixed semantic rule at the end of §5

A sentence in a PR description compared the problem with a smaller
one and stated no fact of its own: `that breaks more than the nightly
job`. Both tiers passed it. `no-remark-about-the-writing` (§5.3)
judges a sentence about the document's own sequence, not the subject.
`no-contrastive-framing` (§5.7) needs an unstated, unasked case; here
the lesser case is stated, not withheld. `no-split-contrast-pair`
(§8.4) needs the comparand in the sentence before; here it is in the
same sentence as the rank. None matched.

`scope-escalation` catalogues the fault as §5.12, a new entry at the
end of §5, for the same reason §7.23 and §8.4 went at the end of their
own sections: an insertion beside §5.1 would renumber rules the
catalogue and the Contents list cite by number. The issue that raised
it called the fault a sibling of §5.3's navigational announcement,
aimed at the subject rather than at the document, which is why §5 and
not §8 is its home.

The tier split follows the precedent of §5.3, §5.5, and §5.6. Five
fixed openers state an escalation and nothing else:
`not just, more than just, this is not only, this is bigger than, it goes further than`.
They went into `vocabulary/banned.tsv`, with two contracted forms
added, `isn't just` and `this isn't only`: banned-word matching
ignores case but not a contraction. `more than` on its own did not go
on the list, since a sentence such as `the import takes more than 30
seconds` states a measurement, and a flat lookup would report a
correct sentence.

Unlike most additions here, the fixed phrases already occurred in
prose outside this repository. `claude-plugins/swe` has four real
escalations on the fixed list, plus one false positive with the same
wording, where the sense is `only` rather than an escalation; that
false positive joins the accepted ones `carry` and `hold` already
have. Each occurrence becomes a banned-word error once the release
pin for `software-english` in `swe/software-english.json` changes to
the tag this change ships in; fixing the four escalations and the one
rewording is a follow-up in that repository, not part of this change.

The rule is inference-based. A parser can find `more than` after a
verb, but whether the noun phrase after it names a lesser case or a
quantity needs judgement. The claude-plugins lint-file worklist
already judges each sentence as a candidate, so the rule needed no
change to that plugin's code, only a release-pin bump.

## Review comment: a new type and a structural rule at the end of §7

A PR review comment took four rewrites before it read cleanly. The
deterministic tier passed every version, including the first: the
rules there score single words and sentence length, and the comment
had no banned word and no long sentence. What was wrong was
structural. The comment opened with evidence, dense and
diff-first, and stated its claim three paragraphs later.

No existing rule matched. `summary-before-detail` (§7.1) requires the
document's main fact first, but not which fact, so a comment that
opens with a true, on-topic sentence passes even where that sentence
is not the problem. `no-abstract-stand-in-for-artefact` (§7.15) names
artefacts, not structure: a comment can name every file it touches
and still bury its claim. `templates/pull-request.md` already named
each alternative rejected, in prose, with no rule behind it.

`problem-alternative-steps` catalogues the fault as §7.24, at the end
of §7, for the reason §7.14, §7.22, and §7.23 are there: an insertion
beside §7.1 would renumber rules the catalogue and the Contents list
cite by number. A review comment is not a PR Description: a PR
description states a change already made, and a review comment names
one not yet made, so the two needed separate types (SPEC Appendix F)
before the rule could be scoped correctly. Only the rule's first
check, the problem sentence, applies to a PR Description too: the
other two presuppose a change not yet built, which a PR description
is not.

The new type needed a local reference, `templates/review-comment.md`,
built the same way `templates/pull-request.md` is: a canonical-source
list, the type's own structure, and the one rule that is Software
English's own addition. README.md's type count and the intro deck's
rule count were updated with it.

The rule is inference-based: a parser can find the first paragraph of
a comment, but whether it states the problem, whether an alternative
is named, and whether a step can be acted on, each needs judgement.
The claude-plugins lint-file worklist already judges each paragraph
as a candidate, so the rule needed no change to that plugin's code,
only the usual release-pin bump.
