# Software English: Specification

**Status:** Draft v0.1. No versioning or governance process yet: see
[Appendix D](#appendix-d-vocabulary-governance). Vocabulary is a seed set,
not exhaustive.

## Contents

<!-- Update Contents when a heading changes -->

- [1. Introduction](#1-introduction)
- [2. Conformance](#2-conformance)
- [3. Structure rules](#3-structure-rules)
  - [3.1 One fact per sentence](#31-one-fact-per-sentence-inference-based)
  - [3.2 Sentence length](#32-sentence-length-deterministic)
  - [3.3 One topic per paragraph](#33-one-topic-per-paragraph-inference-based)
  - [3.4 Lists](#34-lists-inference-based)
- [4. Grammar rules](#4-grammar-rules)
  - [4.1 Tense](#41-tense-mixed)
  - [4.2 Voice](#42-voice-inference-based)
  - [4.3 Verb forms](#43-verb-forms-inference-based)
  - [4.4 Person](#44-person-inference-based)
  - [4.5 Mood](#45-mood-inference-based)
- [5. Semantic rules](#5-semantic-rules)
  - [5.1 No anthropomorphism](#51-no-anthropomorphism-mixed)
  - [5.2 No location or motion verb for an abstract subject](#52-no-location-or-motion-verb-for-an-abstract-subject-deterministic)
  - [5.3 No unstated commentary](#53-no-unstated-commentary-inference-based)
  - [5.4 No hedging where a plain statement is true](#54-no-hedging-where-a-plain-statement-is-true-inference-based)
  - [5.5 No metaphor or analogy](#55-no-metaphor-or-analogy-inference-based)
  - [5.6 No self-qualifying "honest"](#56-no-self-qualifying-honest-mixed)
  - [5.7 No contrastive framing](#57-no-contrastive-framing-inference-based)
- [6. Vocabulary rules](#6-vocabulary-rules-deterministic)
  - [6.1 One sense per word](#61-one-sense-per-word-deterministic)
  - [6.2 Literal tokens](#62-literal-tokens-deterministic)
  - [6.3 Quoted material](#63-quoted-material-deterministic)
- [7. Document rules](#7-document-rules)
  - [7.1 Summary before detail](#71-summary-before-detail-inference-based)
  - [7.2 Match structure to purpose](#72-match-structure-to-purpose-inference-based)
  - [7.3 No warning or caution blocks](#73-no-warning-or-caution-blocks-inference-based)
  - [7.4 Define before use](#74-define-before-use-inference-based)
  - [7.5 No unanchored reference](#75-no-unanchored-reference-inference-based)
  - [7.6 No vacuous classification properties](#76-no-vacuous-classification-properties-inference-based)
  - [7.7 No process narration](#77-no-process-narration-inference-based)
  - [7.8 Document type](#78-document-type-inference-based)
  - [7.9 No planning content in a reference document](#79-no-planning-content-in-a-reference-document-inference-based)
  - [7.10 No out-of-scope comparand](#710-no-out-of-scope-comparand-inference-based)
  - [7.11 Completion marker](#711-completion-marker-deterministic)
  - [7.12 No entailed restatement](#712-no-entailed-restatement-inference-based)
  - [7.13 No mechanism for outcome](#713-no-mechanism-for-outcome-inference-based)
- [Appendices](#appendices)
  - [Appendix A. Machine-readable rule catalogue](#appendix-a-machine-readable-rule-catalogue)
  - [Appendix B. Enforcement and fact preservation](#appendix-b-enforcement-and-fact-preservation)
  - [Appendix C. Configuration](#appendix-c-configuration)
  - [Appendix D. Vocabulary governance](#appendix-d-vocabulary-governance)
  - [Appendix E. Licence and origin](#appendix-e-licence-and-origin)
  - [Appendix F. Document type templates](#appendix-f-document-type-templates)

## 1. Introduction

Software English is a controlled natural language for
prose about software and systems engineering: documentation, chat replies
from an AI agent, commit messages, code comments, ADRs, and READMEs.

The primary reader is a human. Software English does not target machine parsing as a
first-class goal, but its restricted grammar and closed vocabulary make
machine checking possible. That is the mechanism, not the purpose.

The same restriction likely benefits an agent reading Software English prose as
context, not only a human: fewer word senses to disambiguate, and shorter,
single-fact sentences with less to track. This is a secondary benefit, not
a design goal. The agent-targeted profile below is where an agent-first
variant would instead make it one.

A future **profile** may retarget Software English at agent-to-agent prose. This
specification does not define one yet.

## 2. Conformance

Software English defines two conformance tiers. Each tier holds a set of rules:

- **Deterministic**: checkable by a parser or a word-list lookup alone,
  with no semantic judgement. A linter enforces a deterministic rule
  without help.
- **Inference-based**: needs sense disambiguation or contextual judgement
  (for example, detecting anthropomorphism in an unlisted paraphrase, or
  detecting editorial commentary). A model applies an inference-based
  rule; a linter cannot verify it exhaustively.

A rule is admitted to the deterministic tier only if a lookup or a regular
grammar can decide it without interpreting meaning. Anything else is
inference-based by default.

Tier is separate from severity. A deterministic rule can still run at
`warning` severity (advisory, non-blocking) rather than `error`
(blocking): see [`rules/core-rules.toml`](../rules/core-rules.toml).
`vocabulary-membership` runs at `warning` while the vocabulary is a seed
set ([Appendix D](#appendix-d-vocabulary-governance)), so an unlisted but
valid word does not block a turn.

## 3. Structure rules

### 3.1 One fact per sentence (Inference-based)

One sentence states one instruction or one fact. Do not use "and" or a
mid-sentence "then" to join two instructions that read better as two
sentences. A sentence-initial "then" naming what happens next is not a
join and is allowed.

### 3.2 Sentence length (Deterministic)

20 words maximum, all sentence types. One limit, not split by
instruction/description: taken from plain-language guidance (15-20
words), not from an aerospace-manual procedure/description split.
Configurable: see [Appendix C](#appendix-c-configuration).

### 3.3 One topic per paragraph (Inference-based)

A paragraph holds one topic. Split a paragraph that starts to cover a
second topic.

### 3.4 Lists (Inference-based)

Use a list where an instruction has more than one step or a description
has more than one item. Do not write a list as a single run-on sentence
with commas.

### 3.5 No em dash (Deterministic)

Do not use an em dash (`—`), in a sentence or in a list item. It most
often splices two clauses together without stating how they relate,
the opposite of §3.1's one-fact-per-sentence rule:

> The prose is dense — read it twice.

Split into two sentences, or state the relation directly:

> The prose is dense. Read it twice.
> Because the prose is dense, read it twice.

A list item that labels with an em dash uses a colon instead:

> Type — meaning
> Type: meaning

This rule is unconditional, with no exception for a use that reads
correctly, the same precedent as a flat entry in
[`vocabulary/banned.tsv`](../vocabulary/banned.tsv). Quoted material
(§6.3) is already exempt, for the case a fix would otherwise misquote
someone else's exact words.

## 4. Grammar rules

### 4.1 Tense (mixed)

Use simple present, simple past, or simple future:
`the API will change in v2`. Do not use the continuous (`is testing`) to
describe what a system or a process does (Deterministic: checkable by
pattern, and blocking). Avoid the perfect (`has tested`) for the same
purpose, except where the perfect states a fact about history that
simple past cannot:
`the API has changed twice since v1`
(Inference-based: telling the two apart needs judgement, so this runs
advisory-only, not blocking).

### 4.2 Voice (Inference-based)

Use active voice. Name the actor. "The consumer times out after 1
second", not "a timeout occurs".

### 4.3 Verb forms (Inference-based)

Do not use a gerund ("-ing") as the subject or object of a sentence about
a system's behaviour. "The retry runs a second attempt", not "Retrying
runs a second attempt".

### 4.4 Person (Inference-based)

Second person for instructions ("Run the migration"), third person for
description ("The migration script updates the schema"). Configurable:
see [Appendix C](#appendix-c-configuration).

### 4.5 Mood (Inference-based)

Imperative for instructions. Configurable: see
[Appendix C](#appendix-c-configuration).

## 5. Semantic rules

### 5.1 No anthropomorphism (mixed)

A system, service, component, or process has no human trait, feeling, or
intent. State the mechanism.

Deterministic-tier fixed list (verbs/adjectives that fail when a
structure noun (§6, [`vocabulary/structure.tsv`](../vocabulary/structure.tsv))
or a system-referring pronoun (`it`, `this`, `that`) appears within
four words before the match):
`wants, tries, knows, believes, decides, gives up, waits patiently, gets confused, has patience, is happy, is confused, is smart, understands, thinks, remembers, forgets, hopes, assumes, agrees, refuses, prefers, cares, worries, struggles, learns, notices, realizes, expects, intends, plans, chooses, likes, dislikes, enjoys, hates`.
The nearby-subject requirement exists so that a human subject
(`the reviewer expects a passing test`) does not trigger a false match.

Inference-based tier: a paraphrase of the same fault not on the fixed
list (for example, `the cache is happy to serve stale data`) needs model
judgement.

### 5.2 No location or motion verb for an abstract subject (Deterministic)

A location or motion verb (`sits`, `lives`, `resides`, `stands`, `rests`,
and similar) standing in for a plain classification verb (`is`,
`belongs to`) is a deterministic-tier failure when its subject is
abstract, not physical:

> A rule sits in one tier.
> A rule lives in one tier.

The same verbs are correct English for a physical or human subject:

> The operator sits at the console.
> The user lives in London.

So this rule applies the same condition as §5.1: a nearby structure noun
(excluding a human referent such as `user`) or a system-referring pronoun.

This rule exists because the fault is a default of fluent English, not a
vocabulary gap: a writer actively avoiding it can still produce it
without noticing. It cannot go in the flat banned-word list (§6) because,
unlike `reach` or `leverage`, these verbs have a correct use: only the
subject decides.

### 5.3 No unstated commentary (Inference-based)

State facts. Do not add an editorial judgement, a guess at how someone
might react, or a remark about the writing itself, unless explicitly
asked for an opinion.

### 5.4 No hedging where a plain statement is true (Inference-based)

Cut a qualifier that adds no information (`essentially`, `basically`,
`in general`, `it's worth noting that`).

### 5.5 No metaphor or analogy (Inference-based)

State a fact or a mechanism directly. Do not explain it through a
comparison to something else:

> The retry queue is the system's safety net.
> Think of the cache as a waiting room for data.

State the mechanism instead:

> The retry queue holds a failed request for a later attempt.
> The cache holds a copy of data for a later request.

Recognising a metaphor or an analogy needs judgement; no fixed word
list applies.

### 5.6 No self-qualifying "honest" (mixed)

"Honest" and its forms name a real, checkable property: an honest
mistake, an honest broker, an honest error. That use stays approved.

A separate use marks a statement as the writer's own frank opinion,
where the word adds no information over stating the opinion plainly:

> My honest take is that this approach is too complex.
> The honest framing is that we are behind schedule.

State the opinion without the qualifier instead:

> My take is that this approach is too complex.
> The framing is that we are behind schedule.

Deterministic-tier fixed list (in
[`vocabulary/banned.tsv`](../vocabulary/banned.tsv)):
`honest take, honest opinion, honest assessment, honest feedback, to be honest, honestly speaking`.

Inference-based tier: a paraphrase of the same fault not on the fixed
list (for example, `if I'm honest, the design needs a rethink`) needs
model judgement to tell it apart from a literal use of "honest".

### 5.7 No contrastive framing (Inference-based)

A sentence states what happens. It does not state what does not
happen, what a component cannot do, or how a case differs from an
unasked question. That shape answers an objection instead of stating
the fact:

> A file write is the one exception: Claude Code cannot undo a write
> already on disk. Claude still sees the report and fixes the file.

State the trigger and the outcome directly:

> When a file write breaks a rule, Claude reads the printed report and
> fixes the file.

Marker words: `the one exception`, `cannot`, `still`, `the difference
is`, `not that`, `unlike`. None of these is a fault by itself: `cannot`
states a real, load-bearing limit in a reference document as plainly
as any other fact. The fault is the sentence's shape, framed against an
unstated contrast, not the presence of any one word. Recognising the
shape needs judgement, so this stays inference-based.

## 6. Vocabulary rules (Deterministic)

Software English uses a **closed, approved vocabulary**: a word not in the list, and
not a literal token (§6.2) or inside a quoted block (§6.3), fails the
deterministic check. This is a genuine departure from mainstream style
guides, which correct vocabulary rather than close it.

The vocabulary is organised by category, not as one flat list: see
[`vocabulary/`](../vocabulary/). Categories:

| Category | File | Contents |
|---|---|---|
| Operations | [`vocabulary/operations.tsv`](../vocabulary/operations.tsv) | Verbs naming a concrete system action: read, write, create, delete, return, reject, run, call, hold, send, receive |
| Structure | [`vocabulary/structure.tsv`](../vocabulary/structure.tsv) | Nouns naming a system part or a relationship: service, component, process, request, response, queue, cache, consumer, producer |
| Qualities | [`vocabulary/qualities.tsv`](../vocabulary/qualities.tsv) | Adjectives describing a measurable or checkable property: valid, empty, full, available, closed, open, synchronous |
| Connectives | [`vocabulary/connectives.tsv`](../vocabulary/connectives.tsv) | Function words: articles, conjunctions, prepositions, pronouns, common auxiliary verbs |
| Banned | [`vocabulary/banned.tsv`](../vocabulary/banned.tsv) | Words that are not approved, each with an approved replacement: kept for words a writer uses out of habit, so the linter gives a direct fix |

Word admission and vocabulary growth are governed separately: see
[Appendix D](#appendix-d-vocabulary-governance).

### 6.1 One sense per word (Deterministic)

A sense is approved per **(word, part of speech)** pair, not per bare
word: "open" as a verb ("open the connection") and "open" as an
adjective ("the connection is open") are two separate, both-approved
entries. Within one part of speech, only the software/systems sense is
approved: using the word in a different sense for the same part of
speech is a deterministic-tier failure even though the word itself is
approved.

### 6.2 Literal tokens (Deterministic)

A proper noun, an identifier, a file path, a command, a flag, a version
number, a URL, or a code span (a **literal token**) is not checked
against the vocabulary. The linter detects these structurally, by
pattern, never by a list:

- inside a code fence, code span, link target, or HTML tag;
- an acronym (two or more consecutive capitals, e.g. "HTTP", "JSON");
- `snake_case`, `dotted.name`, or a path-like token containing `_ . / -`
  with adjoining alphanumerics;
- `camelCase` (an internal capital not at the start of the token);
- a version number (`\d+(\.\d+)+`, with an optional leading "v");
- capitalised, and not at the start of a sentence (a sentence-initial
  capital is not, by itself, a literal-token signal: only a
  mid-sentence capital is).

Prefer a code span for an identifier, command, or flag over relying on
capitalisation alone.

### 6.3 Quoted material (Deterministic)

A Markdown blockquote (a line starting with `>`) is not checked. It holds
someone else's words, quoted verbatim, including a quoted example of a
Software English fault, such as this specification's own illustrations of banned or
anthropomorphic phrasing. Do not edit the wording inside a blockquote to
satisfy a deterministic-tier rule; edit the surrounding prose instead, or
use a code span (§6.2) for a short quoted fragment inline within a
sentence.

## 7. Document rules

### 7.1 Summary before detail (Inference-based)

A document opens with a one-line summary before detail (borrowed from
Rust's documentation convention).

### 7.2 Match structure to purpose (Inference-based)

A tutorial, a how-to, a reference, and an explanation each answer a
different question and should not be mixed in one document (the Diátaxis
split).

### 7.3 No warning or caution blocks (Inference-based)

Do not use a step-numbered warning/caution block convention. State a
risk as a plain sentence instead.

### 7.4 Define before use (Inference-based)

Define a named term before its first normative use. Introducing a term
and relying on it in the same sentence, without stating what it means,
forces a reader to infer the definition from usage instead.

### 7.5 No unanchored reference (Inference-based)

A definite reference (`the design`, `the decision`, `the plan`,
`this change`, and similar) needs an antecedent inside the document.
A reader without the writer's context cannot resolve a reference the
document does not anchor. The fault can appear in a heading or in body
prose.

A reference is anchored when the document names its referent before the
reference, or when the reference points to where the document defines it
(`the approach in §3`). The same phrases are correct when anchored: a
document that defines a design can call it `the design`.

Fault: the heading `Facts that shape the design` in a document that
defines no design.
Fix: name the referent (`Facts that shape the retry policy`), or define
it before the reference.

This rule exists because the phrasing survives a move from a
conversation, where the referent is shared, into a standalone document,
where it is not.

### 7.6 No vacuous classification properties (Inference-based)

Do not state a property of a classification that already follows from
its member definitions. State a cardinality or exclusivity constraint
(`exactly one`, `at most one`, `mutually exclusive`,
`collectively exhaustive`, `no overlap`, `one and only one`) only where
a mechanism reads it, and state it there, not in the prose definition.

### 7.7 No process narration (Inference-based)

A document about a decision states the decision and the reason for it.
It does not narrate how the decision was reached: who asked, what was
discussed, how many attempts came before it, or what changed between
drafts. The discussion is not the fact; the decision and its reason are.

Fault: `The project owner later asked why, and asked for alternatives.`
Fix: state the constraint and the choice it produced directly, with no
reference to the discussion that surfaced it.

### 7.8 Document type (Inference-based)

Identify a document's target type before writing it. A type (RFC, ADR,
Specification, Technical Manual, and similar) governs structure and
required sections beyond Software English's own sentence-level rules. See
[Appendix F](#appendix-f-document-type-templates) for a by-reference list:
Software English does not redefine any of these structures, only points to each
one's canonical source.

### 7.9 No planning content in a reference document (Inference-based)

This rule is conditional on document type. It applies only to a document
whose type under §7.8 is Reference, the Diátaxis type listed in
[Appendix F](#appendix-f-document-type-templates). The other rules in §7
apply to every document.

A reference document describes. It holds no planning or task-oriented
content:

- no open question;
- no next step;
- no statement of who does work, or when;
- no pointer to a plan document or a task list;
- no statement of the document's own purpose relative to a task or a
  decision in progress.

A sentence that states where planning content belongs is itself planning
content, even when it points away from the document.

Fault: a closing paragraph in a reference document:
`Implementation planning belongs in the plan at doc/planning/plan.md, not in this document.`
Fix: delete the paragraph. Put the pointer in the plan document or in the
document that assigns the task.

This rule is Software English's own addition, not Diátaxis's wording.
Diátaxis's guidance for reference material, "describe, and only
describe," implies it but names no concrete category for planning
content. See [`templates/reference.md`](../templates/reference.md).

A Design document is not a Reference document, and this rule does not
apply to it. A design document states a design that is chosen and not
yet built, so it holds what exists, what is decided, and what is still
open, all at once. It may hold an open-questions section and a
future-extension section, and both are correct content there. Every
other rule in §7 applies to it unchanged, §7.7 included: a design
document states each decision and the reason for it, and does not
narrate how the decision was reached. Assigning the type Reference to a
design document produces a finding against every entry in either
section, so assign the type first. See
[`templates/design.md`](../templates/design.md).

### 7.10 No out-of-scope comparand (Inference-based)

A reader-facing document names only what the reader's task needs. A
comparison to another artefact outside that task, even one stated
plainly with no contrastive framing (§5.7), is a fault when the reader
has no reason to know the other artefact or resolve it against
anything they are doing:

> claude-plugins is a plugin marketplace. ag-harness-library instead
> ships a flat zip, unpacked once into an empty project folder.

`ag-harness-library` is a fact about the author's other work, not
about installing or using a plugin from this marketplace. Cut it, or
move it to an agent-facing file (a `CLAUDE.md`, a design note) whose
reader already holds that context:

> claude-plugins is a plugin marketplace. It hosts plugins that
> install into Claude Code and stay live across projects.

Test: remove the sentence. If the reader can still complete the task
the document serves, the sentence was out of scope.

This differs from §7.5's no-unanchored-reference: that rule fails a
reference with no antecedent to resolve. Here the reference resolves
fine (a working link); the fault is that the reader's task never
needed it. Recognising what a reader's task needs, as against what the
writer's own working context happened to include, needs judgement, so
this stays inference-based.

### 7.11 Completion marker (Deterministic)

Where enforcement rewrites prose to conform, a completed, conforming
response or document ends with the marker line `swe: checked`. Its
absence signals the mechanism did not run or did not complete. See
[Appendix B](#appendix-b-enforcement-and-fact-preservation) for the
check enforcement must run before adding this marker to a rewrite.

### 7.12 No entailed restatement (Inference-based)

A clause that follows from a fact the document already states, given
what the intended reader knows, adds nothing. Cut the clause; keep the
fact it derives from:

> claude-plugins hosts plugins that install into Claude Code
> (`~/.claude/`) and stay live across projects.

A reader who knows `~/.claude/` is the global, not per-project,
configuration directory already has "stays live across projects" once
they read where a plugin installs:

> claude-plugins hosts plugins that install into Claude Code
> (`~/.claude/`).

Test: delete the clause. If the intended reader can still derive it
from the remaining text, with no new fact, the clause was entailed and
the cut was correct.

Sibling of §7.6, which covers the same fault inside a taxonomy
definition specifically. This rule is the general case: any clause
derivable from a fact stated in the same sentence or the one before it.

Two exceptions:

- A clause naming a distinct consequence, not a rephrase (a mechanism,
  a scope, a limit the reader could not derive alone), is not this
  fault, even when it follows closely from what came before.
- A document whose type (§7.8) is a Tutorial does not carry this rule:
  restating a fact for a learner is the genre's own purpose, not a
  fault.

High false-positive risk, since the test rests on a model of what the
reader already knows: runs at `warning` severity, never `error`.

### 7.13 No mechanism for outcome (Inference-based)

A reader-facing sentence states an outcome at the level the reader
acts on. It names an implementation unit (a hook, a handler, a count
of components) only where the reader's task acts on that unit:

> Enforces Software English on agent prose via five hooks.

State the outcome, not the mechanism that produces it:

> Lints Claude Code output against Software English.

Test: change the mechanism and keep the outcome (one hook instead of
five, a different internal name for the input). If the sentence's use
to the reader does not change, the mechanism was at the wrong level
for this reader.

Distinct from §7.4's define-before-use: an undefined term like `hooks`
is a symptom here, not the fault. Defining it would make the sentence
longer without fixing what is wrong: the mechanism does not belong in
this reader's sentence at all, defined or not.

## Appendices

### Appendix A. Machine-readable rule catalogue

Every deterministic-tier rule has a machine-readable entry under
[`rules/`](../rules/) (see
[`rules/core-rules.toml`](../rules/core-rules.toml)) naming: a rule ID,
the check type (`vocabulary`, `substitution`, `sentence-length`,
`tense-pattern`, `anthropomorphism`), its severity, and, for a
pattern-based rule, the regular expression or lookup it runs against.

[`rules/core-rules.toml`](../rules/core-rules.toml) is the catalogue.
[`rules/core-rules.yaml`](../rules/core-rules.yaml) holds the same rules
in YAML, written from the TOML by
[`scripts/generate-rules-yaml.py`](../scripts/generate-rules-yaml.py).
Edit the TOML, then run that script. CI checks that the two agree.

### Appendix B. Enforcement and fact preservation

Enforcement checks changed lines only by default (the lines a diff
against the prior committed state shows as added or modified), not a
whole file. Whole-file checking runs only on explicit request. See the
[`claude-plugins`](https://github.com/jimbarritt/claude-plugins)
[`software-english-lint`](https://github.com/jimbarritt/claude-plugins/tree/main/software-english-lint)
plugin for the reference implementation.

A rewrite must never drop a fact. Before a rewrite is accepted:

1. Extract, from the original text, every number, date, version string,
   URL, code span, and capitalised proper noun, by exact string match.
2. Extract the same set from the rewritten text.
3. Compare the two sets by exact match first. Run a second, fuzzy pass
   only on items with no exact match on the other side: normalised edit
   distance (Levenshtein distance divided by the longer string's length)
   of 0.15 or less counts as the same item (catches a reordered name or
   a minor formatting change, not a dropped one).
4. Any item present in the original with no exact or fuzzy match in the
   rewrite fails the rewrite. Fail closed: do not accept a rewrite that
   fails this check.

### Appendix C. Configuration

The following are configurable per adopter, with Software English's own defaults
shown:

| Setting | Default |
|---|---|
| Dialect | British English |
| Person (instructions) | Second person |
| Mood (instructions) | Imperative |
| Sentence length | 20 words |
| Completion marker | `swe: checked` |

### Appendix D. Vocabulary governance

A word enters the approved vocabulary when it names a real, recurring
concept in software/systems engineering prose and has one dominant sense
in that context. No formal versioning yet.

The vocabulary is a seed set, not exhaustive; it grows the same way
[`vocabulary/banned.tsv`](../vocabulary/banned.tsv) already worked in an
earlier prototype: one entry per real correction.

### Appendix E. Licence and origin

Software English is Apache-2.0 licensed. See [LICENSE](../LICENSE) and
[NOTICE](../NOTICE) for the origin statement distinguishing Software English from
ASD-STE100.

### Appendix F. Document type templates

By reference only: Software English does not redefine any of these structures. Each
row links to the canonical source and to a local cached reference file,
[`templates/`](../templates/), holding a fuller structure summary than
this table, so a reader or an agent can use the shape without fetching
the canonical source first. Verify against the canonical source before
relying on a detail the cache omits; each cached file states its own
last-verified date.

| Type | Canonical source | Cached reference |
|---|---|---|
| RFC | [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.txt) (requirement keywords); [RFC 7322](https://www.rfc-editor.org/rfc/rfc7322.html) (style guide) | [`templates/rfc.md`](../templates/rfc.md) |
| ADR | Nygard, ["Documenting Architecture Decisions"](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011); [adr.github.io](https://adr.github.io/) | [`templates/adr.md`](../templates/adr.md) |
| Design | [IEEE Std 1016-2009](https://ieeexplore.ieee.org/document/5167255/) (software design descriptions); Ubl, ["Design Docs at Google"](https://www.industrialempathy.com/posts/design-docs-at-google/) (2020) | [`templates/design.md`](../templates/design.md) |
| Specification | [W3C QA Framework: Specification Guidelines](https://www.w3.org/TR/qaframe-spec/); RFC 2119 keywords (above) | [`templates/specification.md`](../templates/specification.md) |
| Technical Manual | [Google developer documentation style guide](https://developers.google.com/style); [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/); [Diátaxis](https://diataxis.fr/) | [`templates/technical-manual.md`](../templates/technical-manual.md) |
| Tutorial | [Diátaxis](https://diataxis.fr/tutorials/) | [`templates/tutorial.md`](../templates/tutorial.md) |
| How-to guide | [Diátaxis](https://diataxis.fr/how-to-guides/) | [`templates/how-to-guide.md`](../templates/how-to-guide.md) |
| Reference | [Diátaxis](https://diataxis.fr/reference/) | [`templates/reference.md`](../templates/reference.md) |
| Explanation | [Diátaxis](https://diataxis.fr/explanation/) | [`templates/explanation.md`](../templates/explanation.md) |
| Lab Notebook | Purrington, ["Maintaining a laboratory notebook"](https://colinpurrington.com/tips/lab-notebooks/); [Rice University lab notebook guidelines](http://www.owlnet.rice.edu/~bios311/bios311/nbguidelines.html) | [`templates/lab-notebook.md`](../templates/lab-notebook.md) |
| Portfolio Journal | Janz (1982), ["Initial comparisons of patterned behavior-based interviews versus unstructured interviews"](https://psycnet.apa.org/record/1989-98087-011); Evans, ["Get your work recognized: write a brag document"](https://jvns.ca/blog/brag-documents/) (2019) | [`templates/portfolio-journal.md`](../templates/portfolio-journal.md) |
| Research Note | Umit, [survey of political science journals' research-note policies](https://resulumit.com/blog/polisci-research-notes/) | [`templates/research-note.md`](../templates/research-note.md) |
| Evidence List | [Cochrane Handbook, Chapter 14](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14) | [`templates/evidence-list.md`](../templates/evidence-list.md) |

The last four rows above the Lab Notebook row are
[Diátaxis](https://diataxis.fr/)'s own four documentation types, a
system distinct from RFC, ADR, and Specification, distinguishing document
purpose (why a document exists) rather than document format (what
sections it has). A Technical Manual, per its own cached reference above,
maps onto Reference and Explanation content, not Tutorial or How-to guide
content.

Design cites two sources describing one type at two levels of
formality. IEEE 1016 sets what a software design description must
contain to conform, organised by stakeholder, concern, view, and
viewpoint. The Google convention describes what a working team writes
and reviews before it builds, organised as context and scope, goals and
non-goals, the design, alternatives considered, and cross-cutting
concerns. A design document may follow either.

Design is also the one type in this table that §7.9 names directly. A
design document holds an open question and a future extension as
correct content, where a Reference document holds neither, so the two
types must be told apart before §7.9 runs.

Lab Notebook, Portfolio Journal, and Research Note are each a
convergent convention: independent sources describe the same practice,
with local variation, rather than one body defining a single formal
standard. Evidence List is one joint standard, set by Cochrane and
GRADE together. Each cached reference states this distinction for its own
type.
