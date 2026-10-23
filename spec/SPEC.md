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
  - [3.5 No em dash](#35-no-em-dash-deterministic)
  - [3.6 No clipped sentence run](#36-no-clipped-sentence-run-inference-based)
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
  - [5.5 No metaphor or analogy](#55-no-metaphor-or-analogy-mixed)
  - [5.6 No self-qualifying "honest"](#56-no-self-qualifying-honest-mixed)
  - [5.7 No contrastive framing](#57-no-contrastive-framing-inference-based)
  - [5.8 No undeclared state verb](#58-no-undeclared-state-verb-inference-based)
  - [5.9 No catch-all verb](#59-no-catch-all-verb-inference-based)
  - [5.10 No framing device](#510-no-framing-device-inference-based)
  - [5.11 No ownership or entitlement for a system](#511-no-ownership-or-entitlement-for-a-system-inference-based)
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
  - [7.14 No work breakdown or issue-tracker pointer](#714-no-work-breakdown-or-issue-tracker-pointer-inference-based)
  - [7.15 No abstract stand-in for an artefact](#715-no-abstract-stand-in-for-an-artefact-inference-based)
  - [7.16 No check without its result](#716-no-check-without-its-result-inference-based)
  - [7.17 No withholding heading](#717-no-withholding-heading-inference-based)
  - [7.18 No question or argument heading](#718-no-question-or-argument-heading-inference-based)
  - [7.19 No unstated presupposition](#719-no-unstated-presupposition-inference-based)
- [8. Register rules](#8-register-rules)
  - [8.1 No cadence device](#81-no-cadence-device-inference-based)
  - [8.2 No mechanical repetition](#82-no-mechanical-repetition-inference-based)
  - [8.3 No distributive tail](#83-no-distributive-tail-inference-based)
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

The rule also applies in reverse: do not split one fact across
several sentences (§3.6).

### 3.2 Sentence length (Deterministic)

20 words maximum, all sentence types. One limit, not split by
instruction/description: taken from plain-language guidance (15-20
words), not from an aerospace-manual procedure/description split.
Configurable: see [Appendix C](#appendix-c-configuration).

The limit is a ceiling, not a target. Writing toward it produces a run
of short, clipped sentences stitched together with pronouns; that
shape is its own fault (§3.6).

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

### 3.6 No clipped sentence run (Inference-based)

Vary sentence length. Keep one fact in one sentence where it fits
(§3.1). A run of three or more consecutive short sentences in one
paragraph is a fault when the run splits one fact into clipped pieces
and a chain of pronouns ("it", "its", "their", "this") joins the
pieces back together:

> That design defines two events on two topics. Its Processing section
> states them. Their contract is below. It states the payload of
> each, the topic and message key of each, and the AVRO schema of
> each. It also states where each is registered.

Four of the five sentences are under ten words, and together they
state one fact: what the design defines, and where. "Their contract
is below" states no fact. "Its", "Their", "It", "It" refer
in turn to the design, the events, and the contract, so the referent
changes between consecutive sentences. The rhythm is staccato, and a
pronoun whose referent changes from one sentence to the next makes a
reader resolve each one again.

Merge the pieces of one fact into sentences of different lengths, and
name the noun wherever a pronoun's referent would change:

> The design defines two events in its Processing section, each on
> its own topic. For each event, the contract below specifies the
> payload, the topic, the message key, and the AVRO schema. The
> contract also records where each schema is registered.

These are not this fault:

- a run of short sentences that each state a separate, complete fact
  with a named subject;
- a list item (§3.4), which is short by design;
- a numbered sequence of steps in a document of the Tutorial or
  How-to type (§7.8).

The 20-word limit (§3.2) is a ceiling, not a target, and pushes
writing toward this shape: do not meet the limit by splitting one
fact into several clipped sentences. Fix by merging, not by padding:
a merged sentence adds no word that states no fact (§5.4, §7.12),
and still obeys sentence length and one fact per sentence (§3.1),
since the fields of one contract are one fact.

Telling one fact split across sentences apart from several facts
stated in turn needs judgement, so this stays inference-based.

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

Deterministic-tier fixed list (verbs and adjectives that fail unless a
human referent is within four words before the match, in the same
clause):
`wants, tries, knows, believes, decides, gives up, waits patiently, gets confused, has patience, is happy, is confused, is smart, understands, thinks, remembers, forgets, hopes, assumes, agrees, refuses, prefers, cares, worries, struggles, learns, notices, realizes, realises, expects, intends, plans, chooses, likes, dislikes, enjoys, hates, asks, tells, answers, says, disagree, arrives, arrive, goes, comes, come, enters, enter, leaves, leave, moves, move`.

A human referent is a word that names a person or a group of people
(`user`, `customer`, `person`, `reviewer`, `team`, and similar), its
plural, or a personal pronoun (`I`, `you`, `we`, `she`, `they`,
`who`). The rule catalogue lists them in full. Any other subject is a
system, including a proper noun such as the name of a product, a
vendor, or a service:

> Postgres knows about the row.
> The worker asks the database whether the feature is enabled.
> The record arrives with a default status.

State the mechanism instead:

> Postgres contains the row.
> The worker queries the database for the feature flag.
> The record is created with a default status.

A verb of motion is on this list because motion is an act of a person.
A record, a message, or a file is sent, saved, added, or read. The
transport verbs `travels`, `lands`, and `reaches` are in
[`vocabulary/banned.tsv`](../vocabulary/banned.tsv), with `disagrees`
and `complains`, so the banned-word check reports them.

A human subject does not cause a match (`the reviewer expects a
passing test`). There is also no match when nothing precedes the match
in its clause, or only an imperative lead (`tell the user`, `do not
leave a heading empty`), or when the word directly before the match is
a determiner other than `this` or `that` (`the answers`, `a move`),
because the match is then a noun.

A person's name is not a human referent to this check
(`Jim knows the answer`). Name the role
(`the maintainer knows the answer`), or add the skip-line marker.

Inference-based tier: a paraphrase of the same fault not on the fixed
list (for example, `the cache is happy to serve stale data`) needs model
judgement.

Distinct from §5.11: a claim of ownership or entitlement (`its own
copy`, `is entitled to`, `deserves`) gives a system a status, not a
mind. Report it under §5.11.

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

So this rule fails only when a structure noun (other than a human
referent such as `user`) or a system-referring pronoun (`it`, `this`,
`that`) is within four words before the match. This condition is
narrower than the §5.1 condition, because each verb on this list also
has a literal or an adjectival use (`a live install`, `the rest of the
file`).

This rule exists because the fault is a default of fluent English, not a
vocabulary gap: a writer actively avoiding it can still produce it
without noticing. It cannot go in the flat banned-word list (§6) because,
unlike `reach` or `leverage`, these verbs have a correct use, and
whether a use is correct depends only on its subject.

A verb of motion (`goes`, `comes`, `moves`, `leaves`, `arrives`) is on
the §5.1 list, with the §5.1 human-referent condition: motion is an act
of a person, so `the schema does not move` and `the file does not move`
are the same fault. State the operation instead (`the schema does not
change`, `the file stays in the same directory`). A positional idiom
with no verb of its own (`pass over`, `behind the serialiser`) is on
neither list. §5.5 covers it at the inference tier, and lists the
motion idioms that need no subject check.

`belongs to` stays correct as this rule's fix: its object is a set
or a whole the subject is part of. §5.11 judges `belongs to` only
where its object is a system said to own the subject (`the lock
belongs to the process`).

### 5.3 No unstated commentary (Inference-based)

State facts. Do not add an editorial judgement, a guess at how someone
might react, or a remark about the writing itself, unless explicitly
asked for an opinion.

### 5.4 No hedging where a plain statement is true (Inference-based)

Cut a qualifier that adds no information (`essentially`, `basically`,
`in general`, `it's worth noting that`).

### 5.5 No metaphor or analogy (mixed)

State a fact or a mechanism directly. Do not explain it through a
comparison to something else:

> The retry queue is the system's safety net.
> Think of the cache as a waiting room for data.

State the mechanism instead:

> The retry queue saves a failed request for a later attempt.
> The cache saves a copy of data for a later request.

Deterministic-tier fixed list (in
[`vocabulary/banned.tsv`](../vocabulary/banned.tsv)): a formulaic
transport metaphor, where data, a message, or an event is given a
transport verb of its own:
`ride on, rides on, riding on, rode on, travel, travels, travelled, travelling, piggyback, hitch a ride, along for the ride, ferry, carried across, flows through, landed`.
State the mechanism instead: the event includes it, the topic
publishes it, the service sends it.

Deterministic-tier fixed list (in
[`vocabulary/banned.tsv`](../vocabulary/banned.tsv)): a verb of
physical possession (`carry`, `hold`), where a system, a structure, or
an abstract concept is said to have hands:
`carry, carries, hold, holds, holding, held`.
State the relation instead: the response contains the order list, the
cache has an entry for each user id. The request includes a
correlation id.

Deterministic-tier fixed list (in
[`vocabulary/banned.tsv`](../vocabulary/banned.tsv)): a formulaic
motion idiom, where the subject is inside the fixed phrase, so no
subject check is needed:
`where this leaves, where that leaves, where does this leave, where does that leave, as they come, as it comes`.
State the effect instead: what this means for the retry policy, add
more here, handle each event when the topic publishes it.

Inference-based tier: a metaphor or an analogy not on the fixed list
(for example, `the retry queue is the system's safety net`) needs
model judgement to recognise. This includes a positional idiom with no
verb of its own, given an abstract subject: `the field can be renamed
behind the serialiser` (renamed without changing the response), `a
second pass over the contract` (a second read of the contract). These
idioms are not on a fixed list, because each also names a literal
operation: `a second pass over the input`,
`the service runs behind the proxy`. A verb of motion itself
(`the published schema does not move`) is on the §5.1 fixed list.

The inference-based tier also includes a container-and-form noun
(`shape`, `layer`, `space`) applied to a schema, a type, an API, or a
contract in place of the fields, values, or operations it defines: `a
version fixed now would name a shape the schema does not have` (would
refer to fields the schema does not contain), `the contract is a thin
layer over the table` (has the same fields as the table), `the type
leaves no space for a null` (does not accept a null). The noun
`surface` (`the API surface`) is on the fixed list with the verb, so
banned-word catches it. These nouns are not on a fixed list, because
each also has a literal use: `the schema contains a version field`,
`the error shape as a type` where the type lists the fields, `the
network layer`, `disk space`. A schema that contains a field is
literal; the fault is the form noun standing in for the fields, not
the verb `contain`.

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
unasked question. A sentence of that shape is a reply to an objection,
not a statement of the fact:

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

### 5.8 No undeclared state verb (Inference-based)

Where a document declares an explicit status set for an entity (an
enum, a union type, a table of states, or a list of status values), a
sentence about a state change of that entity names a declared value. A
verb that names no declared status is a fault:

> The design of the two events `erp-sync` publishes when a journal
> entry sync settles: one per item, one per sync.

The document declares the sync status set as `pending`,
`in_progress`, `failed`, `completed`, and `completed_with_errors`. No
status is named `settled`. The verb also names two separate events at
once: the export of one journal entry, and the last status change of
the whole sync. A reader cannot tell which event the sentence means.

Name the declared status, or list each status the verb covers:

> `erp-sync` publishes two events. It publishes one per journal entry,
> after the export of that entry. It publishes one per sync, when the
> sync status changes to `completed`, `completed_with_errors`, or
> `failed`.

These are not this fault:

- a verb form of a declared value: `the sync completes` for
  `completed`, `the sync fails` for `failed`;
- a verb about an entity with no declared status set (§5.5 and §7.4
  still apply to it);
- a verb that names an action, not a state change: `the sync reads
  the ledger`.

The document supplies the status set, so the rule needs no access to
the codebase it describes. Finding the set needs comprehension, not a
lookup: it can be a TypeScript union, an Avro enum, a table, or a list
in prose. Linking a verb to the entity whose status it changes also
needs judgement. So this stays inference-based.

Three other rules have a nearby claim, and each misses this fault:

- §5.1: the verb gives the system no human trait.
- §5.5: the verb need not be a metaphor. A plain verb such as
  `finishes` or `ends` has the same fault when it covers more than one
  declared status and names none.
- §7.4: the verb is not an undefined term. Defining `settle` would add
  a second name for states the document already names, which is the
  fault itself.

### 5.9 No catch-all verb (Inference-based)

One verb names one relation within a paragraph. A content verb used
more than once in one paragraph is a fault when its occurrences name
different relations: one general verb stands in for several precise
ones, and a reader cannot tell the relations apart:

> That design defines two events on two topics. Its Processing section
> states them. Their contract is below. It states the payload of
> each, the topic and message key of each, and the AVRO schema of
> each. It also states where each is registered.

"States" names three relations here: a section that lists the events,
a contract that specifies each field, and a contract that records
where each schema is registered.

Name each relation, and use a distinct verb for each:

> The design defines two events in its Processing section, each on
> its own topic. For each event, the contract below specifies the
> payload, the topic, the message key, and the AVRO schema. The
> contract also records where each schema is registered.

These are not this fault:

- a verb repeated with the same relation each time (`each handler
  returns an error`, or a list where each entry `contains` its
  fields): there the same verb is correct, and a synonym would
  suggest a second relation that does not exist;
- a term the document defines, which keeps its one name (§6.1);
- a repetition inside a code span or a blockquote (§6.2, §6.3).

Fix by naming the relation, not by cycling through synonyms for its
own sake.

Two other rules have a nearby claim, and each misses this fault:

- §5.8: the verb need not describe a state change, and the document
  need not declare a status set.
- §5.5: the verb is literal, not a metaphor; it is only too general.

Naming the relation each occurrence states needs comprehension, so
this stays inference-based.

### 5.10 No framing device (Inference-based)

A declarative sentence states its fact as a plain clause. A framing
device wraps the fact in a frame that states nothing the plain clause
does not. Three shapes are this fault, and they often occur together:

> The gateway asks one question of all four: can this order ship on
> this date, and what reference does the carrier call need. A dispatch
> slot is named for that question rather than for the structure it was
> imported from, and the import is what reconciles the four structures
> down to it.

State each fact as a plain clause:

> The gateway needs two facts from each of the four structures:
> whether the order may ship on the date, and the reference the
> carrier call takes. A dispatch slot is a date range, a status, and a
> carrier reference. The import converts each of the four structures
> to a dispatch slot.

Cleft padding adds a copula and a relative pronoun around a plain
clause: `X is what Y`, `it is X that Y`, `what X does is Y`, `X is the
thing that Y`. The fix is always the same: drop the copula and the
relative pronoun. `The import is what reconciles the structures`
becomes `the import reconciles the structures`. An identity reading
does not exempt the shape: `the primary key is what the index is built
on` becomes `the index is built on the primary key`.

Rhetorical-question framing embeds a question as the subject or the
object of a declarative: `asks one question`, `answers two questions`,
`the question is whether`. The fact the question names is available
directly, so state it.

Naming-as-justification argues for the choice of a name: `is named
for`, `hence the name`, `the name reflects`. State what the named
thing is instead.

Test: rewrite the sentence as its plain clause. If a reader loses no
fact, the frame was a framing device.

These are not this fault:

- a `what` clause or a `which` clause that is the object of a content
  verb, not the complement of a copula: `the response contains what
  the caller requested`, `the log records which orders failed`;
- an indirect question that states the fact through its verb: `the
  config states whether retries are enabled`;
- `X is the N that Y`, where N is a noun that classifies X: `the cache
  is the store that the reader queries first`;
- a literal exchange between components: `the server returns a status code for each request`;
- an entry in a section that lists open questions, such as `Open
  questions` in a design document;
- a name stated as a fact a reader needs, such as a rename or a naming
  convention, or the choice of a name in the Decision section of an ADR;
- a heading (§7.18 judges it), quoted material (§6.3), or a literal
  token (§6.2).

Other rules have a nearby claim:

- §7.18 covers headings only, and this rule covers body prose only, so
  the two never judge one line.
- §5.7: where an `X rather than Y` contrast argues for a name, report
  the sentence under this rule only. Stating what the type is removes
  the contrast too. A contrast about behaviour stays a §5.7 finding.
- §5.9 ignores the copula of a cleft. Where `asks` or `answers` also
  repeats in the paragraph, report the sentence under this rule only,
  since the fix removes the verb.
- §5.1 and §5.5: where a system `asks` or `answers` a question that
  frames a fact, report it under this rule only. A human trait or a
  metaphor outside a question frame stays a finding under that rule.
- §7.15: where `question` or `answer` stands for the facts the
  sentence frames, report it under this rule only. Another abstract
  noun stays a §7.15 finding.
- §7.12 cuts a clause that follows from another fact. This rule keeps
  the one clause and removes the frame around it.

A parser can flag the cleft signatures. Telling a cleft apart from a
`what` clause or a classifying noun, and recognising a question or a
name used as a frame, needs judgement, so this stays inference-based.

### 5.11 No ownership or entitlement for a system (Inference-based)

This rule applies to every document type.

A plain possessive states a fact: a service has a config, a record has
an identifier. A possession or entitlement construction adds a second
layer. It states that the possessor owns the thing, or has the
standing to claim it. Only a person or an organisation of people has
that standing. A system, a service, a component, a process, a
document, a record, or an abstract concept does not.

The family has two groups:

- emphasis on a possessive: `own`, `its own`, `of its own`, `in its
  own right`;
- entitlement: `belongs to`, `is entitled to`, `has a right to`,
  `deserves`, `earns`, `claims`, `is owed`.

Fault:

> The dispatch queue's own copy of the manifest is rebuilt nightly.

Cutting `own` changes nothing the sentence states. Cut the layer and
keep the possessive:

> The dispatch queue's copy of the manifest is rebuilt nightly.

An idiom of standing is the same fault:

> The cache is a service in its own right.

Cut the idiom:

> The cache is a service.

An entitlement has no plain possessive under it. State the allocation,
and name the mechanism that makes it:

> Each partition is entitled to one consumer in the group.

> The group coordinator assigns each partition to one consumer in the
> group.

`belongs to` names the possessor in its object, not its subject:

> Each lock belongs to the process that acquired it.

> Only the process that acquired a lock can release it.

`deserves` and `earns` state a judgement of desert. State the fact
the judgement rests on, or the instruction it implies:

> The retry path deserves a dedicated thread pool.

> Run the retry path on a dedicated thread pool, so a burst of retries
> does not delay a new request.

Test: find the possessor. It is the subject of `deserves`, `earns`,
`claims`, `is owed`, `is entitled to`, or `has a right to`, the object
of `belongs to`, or the noun or pronoun before `own`. Where it is a
person or an organisation of people, the sentence is correct.
Otherwise, cut the layer, or replace it with a plain possessive, `has`,
or the mechanism that allocates the thing. If a reader loses no fact,
the layer was this fault.

These are not this fault:

- a plain possessive or a plain `has`, with any possessor: `the
  service's config`, `the record's identifier`, `the queue has three
  consumers`;
- a possessor that is a person or an organisation of people: `the
  user's own pen`, `the author's own draft`, `the team deserves the
  time`, `the company owns the domain name`, since an organisation can
  own property in law;
- an idiom of standing about a person: `she is a maintainer in her own
  right`;
- `own` that states a fact, one each and not shared: `each event on
  its own topic`, `each worker keeps its own copy of the cache`.
  Cutting `own` here loses the fact that no two share one, so the test
  above passes it;
- `belongs to` as classification or membership, the plain verb §5.2
  names: `a rule belongs to one tier`, `the record belongs to
  partition 3`. Where `is a member of` or `is part of` states the same
  fact, the verb classifies;
- a term of art that names an operation, not a standing: `the worker
  claims the next job`, where a claim is a lease the queue records, or
  `the deposit earns interest`;
- `claims that` in the sense of states (`the README claims that the
  tool supports Windows`), which names no standing. Where it marks the
  writer's doubt, §5.3 applies;
- quoted material (§6.3) or a literal token (§6.2).

Other rules have a nearby claim:

- §5.1 covers a category error about mind: wanting, trying, knowing,
  deciding. This rule covers a category error about status: the
  standing to own a thing or to claim a desert. Neither entails the
  other, and the fixes differ. §5.1 names the mechanism. This rule
  cuts the added layer and keeps the possessive. Where one sentence
  has both (`the cache knows its own size`), report two findings, one
  under each rule.
- §5.2 names `belongs to` as the plain classification verb that
  replaces a location verb. That use is correct here too: its object
  is a set or a whole, not a possessor. This rule fires on `belongs
  to` only where the object is a system said to own the subject. §5.2
  judges a location or motion verb, so the two rules never judge one
  verb.
- §5.5 bans `carry` and `hold` as verbs of physical possession, and
  replaces each with `has` or `contains`. This rule keeps the plain
  possession verb, and cuts an emphasis or an entitlement added to it.
  `in its own right` and `earns its place` are idioms, not
  comparisons: report them under this rule only.
- §5.3: `deserves` and `earns` can state the writer's judgement only.
  Where no fact remains once the judgement is cut (`the refactor
  deserves praise`), report it under §5.3 only, since the fix deletes
  the sentence. Where a fact remains, report it under this rule only.
- §5.4 cuts a qualifier that adds no information. `own` adds none
  either, but it attaches to a possessor, and whether it is a fault
  depends on the possessor. Report `own` under this rule only.
- §6.1 judges the sense of an approved word by lookup. No word in this
  family is in the approved vocabulary, so vocabulary-membership
  reports each one as unlisted, whatever the possessor. This rule
  judges the possessor, which no lookup reads.

Not a banned-word entry, and not a fixed list with a subject check
like §5.1's. Each construction is correct with a person as the
possessor. A subject check would also fire on three correct uses with
a system as the possessor: `belongs to` as classification, `own`
meaning one each, and a term of art. A parser can find each member of
the family. Whether the possessor is a person, and whether the cut
loses a fact, needs judgement, so this stays inference-based.

## 6. Vocabulary rules (Deterministic)

Software English uses a **closed, approved vocabulary**: a word not in the list, and
not a literal token (§6.2) or inside a quoted block (§6.3), fails the
deterministic check. This is a genuine departure from mainstream style
guides, which correct vocabulary rather than close it.

The vocabulary is organised by category, not as one flat list: see
[`vocabulary/`](../vocabulary/). Categories:

| Category | File | Contents |
|---|---|---|
| Operations | [`vocabulary/operations.tsv`](../vocabulary/operations.tsv) | Verbs naming a concrete system action: read, write, create, delete, return, reject, run, call, send, receive |
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

A question-shaped heading, `What this <verb>` or `Which <noun> <verb>`,
is the same fault when no noun follows `this`, or when the noun is a
part of a whole the document does not name.

Fault: the heading `What this costs`, where no noun follows `this`.
Fault: the heading `Which process owns the cache`, in a document that
defines no cache.
Fault: the heading `What an entry contains`, in a document that names
no store the entries are part of.
Fix: name the referent in the heading (`What the retry policy costs`,
`What a session-store entry contains`). For a definite noun such as
`the cache`, defining the referent before the heading also fixes it.

A bare `this`, `that`, or `it` in a heading is a fault even under a
parent heading that names a subject. A heading is also read alone: in a
contents list, in a link, or in a search result. The question shape is
not the fault; the missing referent is.

Distinct from §7.19's no-unstated-presupposition: a definite phrase
that contains a cardinal or a participle naming a completed act
(`the four surveyed carriers`, `the agreed plan`) needs an earlier
statement of a fact, not only an earlier noun. Where both rules match
one phrase, report it under §7.19 only.

This rule exists because the phrasing survives a move from a
conversation, where the referent is shared, into a standalone document,
where it is not.

### 7.6 No vacuous classification properties (Inference-based)

A property of a set that a reader can already see from the set's
members adds no fact. This rule names two faults.

A taxonomy property is a cardinality or exclusivity constraint
(`exactly one`, `at most one`, `mutually exclusive`,
`collectively exhaustive`, `no overlap`, `one and only one`) that
already follows from a classification's member definitions. State such
a constraint only where a mechanism reads it, and state it there, not
in the prose definition.

Fault: `The cache defines a memory tier, a disk tier, and a remote tier. Every entry belongs to exactly one tier.`
Fix: delete the second sentence. Where a check enforces the constraint,
state it in that check.

A count signpost is a sentence that starts with a numeral or a number
word and states only how many items follow it directly. A reader
counts the items, so the count states no fact. The trigger is a number
word at the head of a sentence, followed by a colon and a list, by an
ordered or unordered list, or by the same number of sentences that each
name one item.

Fault: `Three costs follow from that:` followed by a three-item list.
Fault: `Three routes drop an entry:` followed by a three-item list.
Fix: delete the sentence and start with the first item. Where the
sentence names what the items belong to, keep that noun and cut the
count: `The retry policy adds these costs:`.

Three exceptions:

- A count that states a fact beyond the number of items is not this
  fault: a part of a larger set (`Three of the five routes drop an
  entry:`), or a bound a mechanism checks.
- A count whose items do not follow it directly, such as a summary
  (§7.1) that states a count the body expands in separate sections, is
  not this fault.
- A number that is a quantity, not a count of the items
  (`Three retries run before the dead-letter write.`), is not this
  fault.

The phrases `two things` and `three things` are on the fixed list
(`vocabulary/banned.tsv`), and banned-word reports them. Distinct from
§8.1's no-cadence-device: a cadence device restates the sentence before
it, and a count signpost announces the items after it. Both triggers
are findable in the text. Whether a found instance states a fact beyond
the count needs judgement, so this stays inference-based.

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
PR Description, Specification, Technical Manual, and similar) governs structure and
required sections beyond Software English's own sentence-level rules. See
[Appendix F](#appendix-f-document-type-templates) for a by-reference list:
Software English does not redefine any of these structures, only points to each
one's canonical source.

### 7.9 No planning content in a reference document (Inference-based)

This rule is conditional on document type. It applies only to a document
whose type under §7.8 is Reference, the Diátaxis type listed in
[Appendix F](#appendix-f-document-type-templates). The other rules in §7
apply to every document, §7.14 included. Where §7.14 and this rule both
match one sentence in a Reference document, report it under §7.14 only.

A reference document describes. It contains no planning or task-oriented
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
yet built, so it contains what exists, what is decided, and what is still
open, all at once. It may contain an open-questions section and a
future-extension section, and both are correct content there. The
exemption covers those two sections' content only: §7.14 still applies
to a design document, and a design document does not divide its
subject into units of work, or point to later work by an
issue-tracker id. Every other rule in §7 applies to it unchanged,
§7.7 and §7.14 included: a design document states each decision and the
reason for it, and does not narrate how the decision was reached.
Assigning the type Reference to a design document produces a finding
against every entry in either section, so assign the type first. See
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

### 7.14 No work breakdown or issue-tracker pointer (Inference-based)

This rule applies to every document type, Design, API Design, and PR
Description included. It names two faults.

A work-breakdown sentence divides the subject into units of work:
what this piece of work covers, and what a later piece covers. A unit
of work is a change, a phase, a ticket, a milestone, or a follow-up.
The division is a scheduling choice. It states no fact about the
subject.

An issue-tracker pointer is an issue or pull-request id (`PROJ-142`,
`#42`, `repo#slug`) used as the pointer to work the document does not
itself state. The id names no fact inside the document, and it stops
resolving once the tracker is migrated, renamed, or closed.

Fault: a paragraph in a design document:
`This piece of work covers the read path. The write path follows in a later piece of work, tracked in PROJ-142.`
Fix: state the boundary as a fact of the design. List `The write path`
under non-goals, or state it under future extensions as a capability
the design permits:
`A write path: the order store accepts writes through the same schema.`

Test: remove the unit of work and the id. Keep any fact about the
subject that remains. Delete the sentence if none remains.

Three exceptions:

- An entry in a section headed References, Normative References,
  Informative References, or Bibliography may cite an issue or a pull
  request by its id and its title, as a source.
- A Lab Notebook entry names the task it belongs to, and a Portfolio
  Journal entry records work already done. Neither points to later
  work, so neither is this fault.
- In a PR Description, a closing-keyword line (`Closes #11`,
  `Fixes #10`) names an issue the change resolves, in the form a
  tracker reads to close the issue. It points to no later work, so it
  is not this fault. A sentence that points to a follow-up pull
  request or a later change is still this fault.

§7.9 forbids all planning content, in a Reference document only. It
exempts a design document's open questions and future extensions.
This rule names fewer faults and applies to every type: an open
question or a future extension that names no unit of work and no id
is not this fault.

This rule is Software English's own addition. Distinct from §7.5's
no-unanchored-reference: the id can resolve and still be this fault.
Telling a unit of work apart from a part of the subject needs
judgement, so this stays inference-based.

### 7.15 No abstract stand-in for an artefact (Inference-based)

This rule applies to every document type. On a PR Description,
listed in [Appendix F](#appendix-f-document-type-templates), its
scope is narrower: see the scope paragraph below.

A sentence about an artefact names it: a file, a type, a schema, a
field, a record, a table, an endpoint, a request, a response, a
message, or a topic. An abstract noun used in place of that artefact
is a fault. A reader cannot check a sentence against a noun that
names nothing in the system.

In a PR description, the common stand-ins are `evidence`, `context`,
`visibility`, `coverage`, and `insight`. In a reference or a design
document, the common substitutes are structural nouns: `shape`,
`form`, and `flavour`. The noun `surface` is on the fixed list, so
banned-word catches it (§5.5).

Fault: `The record written to the downstream system contained no
evidence.` The missing thing was a receipt file attached to the
record.
Fix: `The record written to the downstream system had no receipt
file attached.`

Fault: `The report gave the operator no visibility.`
Fix: `The report listed no failed orders.`

Fault: `The adapter maps all four shapes to this record.` `Shapes`
stands for four vendor payload structures, and `this record` for the
schema they are converted to. `Record` is on the artefact list, and
is still a stand-in here: the sentence refers to a schema, not to
one stored record.
Fix: `The adapter converts all four vendor payload structures to
this schema.`

A count of items the sentence never names is the same fault: `It
reports four counts` names none of the four.
Fix: `The summary reports the number of orders read, written,
skipped, and failed.`

On a PR description, the rule covers the problem statement and the
statement of what the change does: the sections headed Summary,
Problem, or Change, or, in a description with no headings, the
sentences that state what was wrong before the change and what the
change does. On every other document type, the rule covers the
whole document.

Test: ask which file, type, schema, field, record, request, or item
the noun refers to. Replace the noun with it when the answer names
one.

Four exceptions:

- A noun where the thing named is itself abstract, such as a
  measured quantity a tool reports (`Line coverage of the parser
  rose from 71% to 84%.`), is not this fault.
- A structural noun in its literal sense (`an HTML form`) is not
  this fault.
- A heading or a section name (`Context`), a document type name
  (`Evidence List`), or a literal token (§6.2), is not this fault.
- On a PR description, a sentence outside the problem statement and
  the change statement is not this fault.

Distinct from §5.5: where a sentence names the schema, type, API, or
contract, and a form noun stands in for its fields, values, or
operations, report it under §5.5 only. Where the sentence names no
artefact for the noun to belong to, report it under this rule only.

Not a banned-word entry: each noun has a correct abstract use, and a
word-list lookup reads one token, not the document the token is in.
Distinct from §7.13: that rule cuts an implementation unit a
reader's task does not act on. This rule requires the artefact a
reader checks a sentence against, which a reader's task does act
on. Telling an abstract stand-in apart from a correct abstract noun
needs judgement, so this stays inference-based. See
[`templates/pull-request.md`](../templates/pull-request.md).

### 7.16 No check without its result (Inference-based)

This rule is conditional on document type. It applies only to a
document whose type under §7.8 is PR Description, listed in
[Appendix F](#appendix-f-document-type-templates).

A verification entry pairs a check with its result. A check is a
command, a test suite, or a manual step. A check listed with no
result reads as evidence that the change works, and states no
result.

Fault: a Verification section with the single entry `` `make
test` ``.
Fix: `` `make test`: passed, 212 tests ``.

Fault: `Tested locally.`, which names no check and no result.
Fix: `` Ran the importer against `fixtures/ledger.csv`: 1,204 rows
written, 0 rejected. ``

A failing or a partial result is still a result: `` `make e2e`: 2
failures, both in `test_retry`, and both also fail on `main` `` is
not this fault.

Three exceptions:

- An entry in a section that lists what did not run, or could not
  run (headed Not verified or Not tested), such as `` `make e2e`:
  not run, because the suite needs staging credentials ``, is
  correct content in a PR description and is not this fault. It
  states a limit plainly.
- A command a reviewer is asked to run, in a section headed How to
  try it or How to reproduce, and a command the change adds or
  alters, named in the Change section, are not verification entries.
- A command followed directly by its pasted output is not this
  fault: the output is the result.

Telling a verification entry apart from a command named for another
reason needs judgement, so this stays inference-based.

### 7.17 No withholding heading (Inference-based)

This rule applies to every document type. Its scope is headings only,
at every level, the document title included. In body prose the same
words form no sentence, so the fault occurs only in a heading.

A heading names what its section states. A withholding heading names
the section only by what a reader gets from reading it: its meaning,
its consequence, its outcome, or a promise that it is notable. A
reader must read the section to learn what the heading refers to. A
heading is also read alone, in a contents list, a link, or a search
result, and there a withholding heading states nothing.

Fault: the heading `What this means for everything else`.
Fix: state the fact the section states: `Retries are capped at three attempts`.

Fault: the heading `What we found`, over a section that reports one
measurement.
Fix: `Cold start takes 200 ms`.

Fault: the heading `The surprising part`.
Fix: name the fact the section states: `The parser reads each file twice`.

A heading that names a subject, but refers to the section only by its
meaning, is the same fault: `What the retry cap means for the scheduler`.

Test: read the heading alone, without its section. Check whether it
names a fact the section states, or a subject and the property of it
the section states: a cost, a content, a limit, an owner, or a
behaviour. Where it names neither, write the fact as the heading.

Four exceptions:

- A heading that names a subject, or a subject and a property
  (`Retry policy`, `What a session-store entry contains`), is not this
  fault. A heading need not be a full sentence.
- A conventional section name is not this fault. It names the
  section's function, reads the same in any document of its type, and
  a reader looks the section up by it: `Summary`, `Context`,
  `Decision`, `Consequences`, `Recommendation`. Every section name a
  document type's template lists (§7.8) is one.
- A task heading in the imperative or the infinitive (`Install the
  CLI`, `How to try it`) is not this fault.
- A heading that is a literal token (§6.2), such as a command or a
  file name, is not this fault.

The formulaic phrases on the fixed list (`vocabulary/banned.tsv`),
such as `at a glance`, `the big picture`, and `the upshot`, are caught
by banned-word. This rule covers a withholding heading in words not on
the list.

Distinct from §7.5's no-unanchored-reference: that rule requires the
referent a heading names. A heading can name its referent and still
withhold its content. Where both rules match one heading, report it
under this rule only: the fix states the fact, and the fact names the
referent. A heading phrased as a direct question is a §7.18 finding,
not a finding under this rule. A metaphor in a heading is a §5.5
finding, and a heading that states what a subject does not do is a
§5.7 finding. This rule judges what a heading names, not how the
heading words it.

Telling a withholding heading apart from a heading that names a
subject needs judgement, so this stays inference-based.

### 7.18 No question or argument heading (Inference-based)

This rule applies to every document type. Its scope is headings only,
at every level, the document title included.

A heading states a claim. It does not ask a question the section then
answers, and it does not present a case for a claim. Two shapes are
this fault.

A question heading is a direct question: interrogative word order, a
question mark, or both. A rhetorical question is the common case. A
plain question is the same fault, because the heading is a question and
only the section states the claim.

Fault: the heading `Why would anyone run it twice?`
Fix: state the answer: `A second run reuses the cached result`.

Fault: the heading `Does the cache survive a restart?`
Fix: `A restart empties the cache`.

An argument heading announces a case for a claim, not the claim
itself.

Fault: the heading `The case for capping retries`.
Fault: the heading `In defence of a second run`.
Fix: state the claim (`Retries are capped at three attempts`), and
give the reasons in the section.

Test: state in one sentence the claim of the section. If the heading
is a question with that sentence as its answer, or a case for that
sentence, use the sentence as the heading.

Four exceptions:

- An indirect question in statement word order, with no question
  mark, is not this fault when it names its subject and the property
  the section states: `What a session-store entry contains`, `How the
  scheduler orders jobs`. §7.5 permits that shape when the heading
  names its referent.
- A task heading (`How to try it`, `How to reproduce`) names a task,
  not a question, and is not this fault.
- A section name that names questions, such as `Open questions` in a
  design document, is not this fault.
- A heading that is a literal token (§6.2), or a verbatim quotation
  (§6.3) that is the section's subject, such as an error message, is
  not this fault.

Where §7.17 also matches a heading
(`What does this mean for everything else?`), report it under this
rule only. Where §7.5 also matches, as the bare `it` in
`Why would anyone run it twice?` does, report it under this rule only:
the fix states the claim, and the claim names the subject. A metaphor
(§5.5) or a contrastive frame (§5.7) in the same heading is a separate
finding under that rule.

§8.1 excludes a heading because a heading is not a sentence. This rule
judges the heading itself, so the two do not overlap.

A parser can flag a heading that ends in a question mark. Deciding
whether the heading is a question answered by the section, a quoted
literal, or a case for a claim needs judgement, so this stays
inference-based.

### 7.19 No unstated presupposition (Inference-based)

This rule applies to every document type.

A definite noun phrase presupposes a fact. `The four surveyed
carriers` presupposes that a survey took place, and that it covered
four carriers. A document states that fact before the phrase that
refers to it. A reader can tell what kind of thing the noun names, but
not the fact the phrase depends on.

Either of two markers identifies the fault:

- a cardinal inside the phrase, a number word or a numeral (`the four
  carriers`, `the three tables`, `both options`), where no earlier
  sentence states that count;
- a past participle inside the phrase that names a completed act
  (`surveyed`, `rejected`, `agreed`, `measured`), where no earlier
  sentence states that the act took place, or what it covered.

Fault, as the first sentence of a document:

> The four surveyed carriers all reject a weekend dispatch slot.

No sentence states which four carriers, who surveyed them, or when.
State the fact before the phrase that refers to it:

> The dispatch team surveyed four carriers in March 2026: A, B, C,
> and D. None accepts a weekend dispatch slot.

The same phrase is correct once the document states the fact. After
the first sentence of the fix, `the four surveyed carriers` is
anchored. So is `the four tables` in a document that lists four
tables.

Test: for each definite phrase with a cardinal or a completed-act
participle, find the earlier sentence that states the count, or the
act and what it covered. Where no such sentence exists, write it
before the phrase. A heading is in scope, and is anchored when the
document states the fact before the heading.

These are not this fault:

- a phrase that points to where the document states the fact: `the
  four carriers listed in §3`;
- a cardinal whose items the same sentence names: `the three routes:
  read, write, and delete`;
- a cardinal that is part of a name or a literal token (`two-phase
  commit`, `the 404 response`), or a number that is a quantity, not a
  count of referents (`the 30-second timeout`);
- a participle that names a state or a kind, not a completed act
  (`the closed connection`, `the compiled binary`), or a declared
  status value (§5.8);
- an act the document type itself records, such as `the changed
  files` in a PR Description, whose subject is the change
  ([Appendix F](#appendix-f-document-type-templates));
- quoted material (§6.3) or a literal token (§6.2).

Other rules have a nearby claim:

- §7.5 requires an earlier noun for an abstract singular (`the
  design`, `the plan`). This rule requires an earlier statement of a
  fact, and the noun can be concrete and plural. Where both rules
  match one phrase, as `the agreed plan` does in a document that
  defines no plan, report it under this rule only: the fix states the
  agreement and names the plan.
- §7.15: where the head noun is abstract and names none of the items
  it counts (`It reports four counts`), report it under §7.15 only.
  Where the head noun names a concrete kind and only the count or the
  act is unstated, report it under this rule only.
- §7.6: a count signpost states a count the items directly after it
  already show. This fault states a count no earlier sentence
  supports.
- §7.4 covers a term whose meaning is not defined. Here the noun is
  understood; the document never states the fact it depends on.
- §7.7: state the fact the phrase depends on and its result, not the
  history of the work. A fix that adds who asked or what was
  discussed is a §7.7 finding.

Not a banned-word entry: each phrase is correct once the document
states the fact. A parser can find a cardinal or a participle inside
a definite phrase. Whether an earlier sentence states the fact needs
the whole document, not a lookup, so this stays inference-based.

## 8. Register rules

Register is the rhythm, emphasis, and formatting of a text, apart from
its grammar and its facts. A text can pass every rule in §3 to §7 and
still repeat a small set of patterns that a reader recognises as
generated by a language model. Each pattern adds no fact. A reader who
recognises one reads the text around it with less trust. These rules
judge the text, not its author: a human writer who uses the same
pattern makes the same fault.

### 8.1 No cadence device (Inference-based)

A cadence device is a sentence written for rhythm. It restates a fact
the sentence before it already states. Two shapes are this fault.

A verbless fragment, set as its own sentence after a longer sentence,
repeats or stresses that sentence:

> The consumer retries each failed message three times with
> exponential backoff, then writes it to the dead-letter topic. No
> silent drops.

"No silent drops" has no verb. It states nothing the first sentence
does not already state. Delete the fragment:

> The consumer retries each failed message three times with
> exponential backoff, then writes it to the dead-letter topic.

A matched pair is two sentences in the same grammatical shape, where
the second restates the first:

> The parser reads each file once. It never reads a file twice.

Both sentences name the same subject, verb, and object shape. The
second states the first fact again in negative form. Keep the first
sentence only:

> The parser reads each file once.

Test: delete the fragment, or the second sentence of the pair. If a
reader loses no fact, the sentence was a cadence device. If the
fragment named a fact the sentence before it does not state, write
that fact as a full sentence with a verb.

These are not this fault:

- a heading, a list item, a table cell, or a label such as `Fault:`,
  which is not a sentence;
- a one-word answer to a direct question in a chat reply, where the
  question supplies the verb;
- two sentences in the same shape that state two different facts
  ("A read takes a shared lock. A write takes an exclusive lock.");
- quoted material (§6.3).

§3.6 covers a run of short sentences that splits one fact into pieces.
This rule covers one sentence that repeats a fact already stated in
full. §7.12 covers a clause a reader can derive from a stated fact.
Where a restatement also repeats the shape of the sentence before it,
report it under this rule.

A parser can flag a sentence with no verb, or two sentences with the
same shape. Deciding whether the flagged sentence adds a fact needs
judgement, so this stays inference-based.

### 8.2 No mechanical repetition (Inference-based)

Repeat a form or a fact only where a reader needs it again. Three
patterns are this fault.

The same formatting on every item: a bold lead-in opens each bullet,
across a run of lists, and each lead-in restates the item it labels:

> - **Fast startup.** The service starts in 200 ms.
> - **Low memory.** The service uses 40 MB at idle.
> - **One config file.** The service reads one TOML file.

Each lead-in names what its sentence states. Remove the lead-ins:

> - The service starts in 200 ms.
> - The service uses 40 MB at idle.
> - The service reads one TOML file.

One fact restated in several places in different words: a measurement
given in the summary, again in the body, and again in a closing
section states one fact three times:

> Cold start takes 200 ms.
>
> The service is ready in a fifth of a second.
>
> Startup finishes in well under a quarter of a second.

State the measurement once, in the section where a reader looks for
it. The summary that §7.1 requires may state it a second time.

A contents list out of scale with the document: a contents list lets
a reader find a section without reading through. A document of under
about 300 lines takes none. A longer document lists its top-level
headings. It lists subsections only where a reader looks one up by
number, as in this specification. A contents list of twenty entries
on a 250-line document is this fault.

These are not this fault:

- a bold lead-in that is the term the item defines, or the name of a
  section the item describes, as in §2's list of tiers;
- a bold lead-in on one list where the items differ in kind and the
  lead-in names the kind;
- a value repeated in a code block or a literal token (§6.2), which a
  reader copies;
- a fact stated once in the summary (§7.1) and once in the body.

Telling a needed repetition apart from a mechanical one needs
judgement, so this stays inference-based. High false-positive risk:
this rule runs at warning severity, never error.

### 8.3 No distributive tail (Inference-based)

A distributive tail is a clause joined with `and` to a sentence that
states a count or a set. It gives one property to every member, with
`each`, `both`, or `every one of them`. The tail is this fault where
that property is a fact about the document's own layout:

> Four checks run on upload, and each is a step below.

The main clause states a fact about the system. The tail states where
the document describes each check. `And` joins two clauses of the same
kind, and these two clauses differ in kind. The tail sets out a note
on the document's structure as a second finding. Its property is a
modifier of the noun phrase, written as a clause. Write the property
as a modifier of the noun phrase:

> Four checks run on upload, described in the steps below.

The same fault with `both`:

> The service exposes two endpoints, and both are listed in the table.

Fix:

> The service exposes two endpoints, listed in the table.

Test: first, check that the property is about the document's layout,
not the subject matter. Then write it as a modifier of the noun
phrase. If a reader loses no fact, the tail was this fault.

A tail whose property is a fact about the members is correct:

> Three consumers read the topic, and each commits its offset
> independently.

The tail states a fact about the consumers, not about the document.
Keep it.

These are not this fault:

- a tail whose property is a fact about the subject matter, as in the
  consumer example;
- a distributive word in the main clause, with no tail joined by
  `and` (`Each of the four checks is a step in §4.`);
- a separate sentence that states where the document describes the
  members (`§4 describes each check.`);
- quoted material (§6.3).

Distinct from §8.1's no-cadence-device: a cadence device restates a
fact the sentence before it already states. A distributive tail adds a
fact about the document, inside the same sentence. Distinct from §7.6:
a count signpost states only how many items follow it directly. A
distributive tail is a clause joined to a count whose main clause
states a fact. Where a sentence states only a count of the items after
it, report it under §7.6 only.

A parser can find `, and each` or `, and both` after a count. Telling
a property of the layout from a property of the subject matter needs
judgement, so this stays inference-based.

## Appendices

### Appendix A. Machine-readable rule catalogue

Every deterministic-tier rule has a machine-readable entry under
[`rules/`](../rules/) (see
[`rules/core-rules.toml`](../rules/core-rules.toml)) naming: a rule ID,
the check type (`vocabulary`, `substitution`, `sentence-length`,
`tense-pattern`, `anthropomorphism`), its severity, and, for a
pattern-based rule, the regular expression or lookup it runs against.
[`rules/core-rules.toml`](../rules/core-rules.toml) is the catalogue,
in the singular: no other file duplicates it.

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

A word is added to the approved vocabulary when it names a real, recurring
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
row links to the canonical source and to a local reference file,
[`templates/`](../templates/), holding a fuller structure summary than
this table, so a reader or an agent can use the shape without reading
the canonical source first. Verify against the canonical source before
relying on a detail the local reference omits.

| Type | Canonical source | Local reference |
|---|---|---|
| RFC | [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.txt) (requirement keywords); [RFC 7322](https://www.rfc-editor.org/rfc/rfc7322.html) (style guide) | [`templates/rfc.md`](../templates/rfc.md) |
| ADR | Nygard, ["Documenting Architecture Decisions"](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011); [adr.github.io](https://adr.github.io/) | [`templates/adr.md`](../templates/adr.md) |
| Design | [IEEE Std 1016-2009](https://ieeexplore.ieee.org/document/5167255/) (software design descriptions); Ubl, ["Design Docs at Google"](https://www.industrialempathy.com/posts/design-docs-at-google/) (2020) | [`templates/design.md`](../templates/design.md) |
| API Design | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) and [RFC 9112](https://www.rfc-editor.org/rfc/rfc9112.html) (HTTP); [Apache Avro](https://avro.apache.org/docs/current/specification/) and [JSON Schema](https://json-schema.org/specification) (schema notation); [CloudEvents 1.0.2](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md) (event envelope) | [`templates/api-design.md`](../templates/api-design.md) |
| PR Description | Google Engineering Practices, ["Writing good CL descriptions"](https://google.github.io/eng-practices/review/developer/cl-descriptions.html); Linux kernel, ["Submitting patches"](https://www.kernel.org/doc/html/latest/process/submitting-patches.html#describe-your-changes) (describe your changes) | [`templates/pull-request.md`](../templates/pull-request.md) |
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
sections it has). A Technical Manual, per its own local reference above,
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
types must be told apart before §7.9 runs. §7.9's exemption covers open
questions and future extensions only; §7.14 applies to Design as to
every type.

API Design is a specialisation of Design: it keeps Design's seven
sections and adds API-specific content inside "The design." §7.9's
exemption for Design applies to it unchanged, and so does §7.14.
OpenAPI and AsyncAPI are cross-references in its local reference, a
generation target, not the document's own structure.

PR Description is the one type in this table whose subject is a
change already made, not a decision or a built system. A PR
description states the change and the evidence that it works. §7.9
does not apply to it: it is not a Reference document. §7.14 applies
to it as to every type, with its own exception for a closing-keyword
line. §7.15 also applies to every type, and on a PR description its
scope is the problem statement and the change statement. One rule
applies to a PR description and to no other type: §7.16 requires
each check it lists to state its result.

Lab Notebook, Portfolio Journal, Research Note, and PR Description
are each a convergent convention: independent sources describe the
same practice, with local variation, rather than one body defining a
single formal standard. Evidence List is one joint standard, set by
Cochrane and GRADE together. Each local reference states this
distinction for its own type.
