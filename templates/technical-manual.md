# Technical manual structure: a cached reference for Software English

A technical manual describes how a system works, for a human or agent audience. This file lists the structural conventions that apply to that document type.

## Canonical sources

- Google developer documentation style guide: https://developers.google.com/style
- Microsoft Writing Style Guide: https://learn.microsoft.com/en-us/style-guide/
- Diátaxis framework: https://diataxis.fr/

This file is a cache. It does not replace these sources.

## Structural conventions

### Headings: task-based vs conceptual

Google's style guide sets two heading forms, chosen by content type:

- Task-based headings (quickstarts, how-to guides, tutorials) start with a bare infinitive verb: "Create an instance", not "Creating an instance".
- Conceptual headings use a noun phrase and avoid an "-ing" opening word: "Migration to Google Cloud", not "Migrating to Google Cloud".

A technical manual describes a system's components and behaviour, so its headings are mainly conceptual (noun phrases), not task-based.

Google also states:

- Use sentence case for all headings and titles.
- Each page has one unique top-level heading (H1).
- Heading levels follow in order; do not skip from H1 to H3.
- A heading is always followed by content; do not leave a heading empty.
- Do not use numbers to show sequence in headings; use the heading hierarchy instead.

Microsoft's style guide adds:

- A top-level heading states the main point of its section and divides content into major subjects.
- Add a second-level heading only when a top-level section holds two or more distinct sub-topics. If there are not at least two, skip the second-level heading.
- Do not place two headings in a row with no text between them. That pattern signals a structure problem.
- Keep headings short. Put the most important word first.
- Use parallel sentence structure for all headings at the same level: for example, noun phrases for top-level headings, infinitive phrases ("To configure X") for task headings.
- Use sentence-style capitalisation (capitalise the first word, proper nouns, and the first word after a colon; nothing else).
- Do not end a heading with a period.

### Summary-first structure

Microsoft's guidance on scannable content states:

- Content near the top of a page ("above the fold") is the content most likely to be read. Lead with the point a reader needs most.
- In left-to-right languages, readers scan a page in an F-shape, giving the most attention to the upper-left area. Place the most important information there.
- Write short headings, short sentences, and short paragraphs. Three to seven lines is a reasonable paragraph length.
- In a long document, add a table of contents and links to subheadings, so a reader can navigate directly to a section.
- Place important keywords near the start of headings, table entries, and paragraphs.

Google's style guide follows the same pattern: its own pages open with a page summary that states the main points before the full content follows.

### Reference material

Google's style guide separates procedures (task-based, numbered steps) from reference and conceptual content:

- A procedure is a sequence of numbered steps for a task. Each step starts with an imperative verb.
- A procedure states where an action happens before what to do.
- Reference and conceptual material does not follow the numbered-step form. It states facts about a system: components, parameters, behaviour.

Neither source fetched for this file provides a single named structure for a full reference document (for example, a fixed sequence of sections such as "Overview / Components / Configuration / Errors"). Where a manual needs that level of structural specification, check the canonical sources directly, or apply a project-specific structure and record it separately.

## Document purpose (Diátaxis)

Diátaxis names four documentation types, distinguished by the need each
serves: [Tutorial](../templates/tutorial.md) (learning),
[How-to guide](../templates/how-to-guide.md) (goal),
[Reference](../templates/reference.md) (information), and
[Explanation](../templates/explanation.md) (understanding) — see each
file for its full cached definition.

A technical manual that describes how a system works is reference and
explanation content. It states facts about the system's parts and
behaviour, and explains why the system is built that way. Per Diátaxis,
it is not a tutorial (it does not teach through a guided lesson) and not
a how-to guide (it does not walk through steps toward one goal). Mixing
those forms into a manual works against the distinction Diátaxis sets
out.

## Verify against the source

This cache is current as of 2026-09-12. For anything not covered here, check the canonical sources directly.
