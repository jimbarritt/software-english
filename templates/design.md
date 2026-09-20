# Design document structure: a local reference cache for Software English

## Canonical sources

This file is a cache. It does not replace the canonical sources.

- Formal standard: IEEE Std 1016-2009, `IEEE Standard for Information Technology—Systems Design—Software Design Descriptions`: https://ieeexplore.ieee.org/document/5167255/
- Industry convention: Malte Ubl, "Design Docs at Google" (2020): https://www.industrialempathy.com/posts/design-docs-at-google/

IEEE 1016 defines the required information content and organisation of a software design description (SDD). The 2009 edition raised the document from a recommended practice to a full standard. It models the document after IEEE Std 1471-2000, taking the concepts of stakeholder, concern, view, and viewpoint from architecture description into design description.

"Design Docs at Google" describes the widely copied industry convention. A design document there is a relatively informal document, written by the author of a system before the coding starts. It records the high-level implementation strategy and the design decisions, and puts the emphasis on the trade-offs each decision weighed.

The two sources describe one document type at two levels of formality. IEEE 1016 governs what an SDD must contain to conform. The Google convention governs what a working team writes and reviews. A design document may follow either. Software English's own rules apply to both.

## What a design document is

A design document states a design that is chosen but not yet built. It holds three states of knowledge at once: what exists today, what the author decided, and what is not yet settled. That combination separates it from every other type in [Appendix F](../spec/SPEC.md).

Per the Google convention, a design document serves five purposes:

- it identifies design problems early;
- it records consensus;
- it forces cross-cutting concerns to be considered;
- it takes knowledge to people who join later;
- it records, afterwards, what was decided and why.

A design document has a lifecycle. It is written before the work, reviewed and revised during the design, and read afterwards as a record. An open question in it is correct content while the design is live, and a record of what was open at the time once the work is done.

## Structural conventions

The Google convention names five sections, in this order:

1. **Context and scope.** The state of the world the design starts from, stated objectively, in one or a few paragraphs. It orients a reader who was not present, and it does not argue for the design.
2. **Goals and non-goals.** Two bullet lists. A non-goal is not a negated goal (`the system does not crash` is not a non-goal). A non-goal is an outcome that could reasonably have been a goal and is deliberately not one. A design may still deliver a non-goal, where that costs nothing against the goals.
3. **The actual design.** The design itself, in as much detail as the decisions need, and short enough for a busy reviewer to read.
4. **Alternatives considered.** Each alternative that would reasonably have met a similar outcome, with the trade-offs it makes, and why those trade-offs led to the chosen design over it.
5. **Cross-cutting concerns.** The concerns outside the design's own subject that still apply to it: security, privacy, observability, and any other the organisation requires of every design.

IEEE 1016 organises the same material by viewpoint instead of by section. An SDD identifies its stakeholders and their concerns. It then holds one design view per viewpoint, each addressing the concerns assigned to it, plus the design rationale for the choices made. A document conforming to IEEE 1016 states its own identification, its stakeholders and concerns, its views and viewpoints, and its rationale.

## Software English addition: open questions and future extensions

This section is Software English's own rule, not IEEE 1016's wording and not the Google convention's. Neither source names these two sections. Both describe a document whose subject is a live design, which is what makes the two correct here.

A design document may hold:

- **An open-questions section.** Each entry names one unresolved question the design does not settle. §7.9 excludes such content from a Reference document. A design document holds it, because a reader needs to know what is unsettled before relying on the rest.
- **A future-extension section.** A capability the design permits and the current work does not build. Its purpose is forward-looking, so a reader can tell a deliberate extension point from an omission.

Every other rule that applies to a reference document applies to a design document unchanged. The sentence-level rules in SPEC §3 to §6 apply in full. [§7.7](../spec/SPEC.md) still forbids narrating how a decision was reached. A design document states each decision and the reason for it. It does not record who argued for what, or how many drafts came before.

[§7.9](../spec/SPEC.md), which forbids planning content, applies to a document whose type is Reference. It does not apply to a design document. Assigning the type Reference to a design document produces a finding against every entry in both sections above, which is why the type exists in its own right.

## How this differs from the neighbouring types

| Type | What it holds | State of the decision |
|---|---|---|
| ADR | One decision, its context, and its consequences | Taken |
| RFC | One proposal, put to readers for a response | Proposed, not taken |
| Design | The strategy for one system, its decisions, its alternatives, and what stays open | Taken, with named gaps |
| Reference | What the built system is | Built |

An ADR records a single decision after the fact, and a design document holds many decisions, some of them still open. An RFC exists to be answered, and a design document exists to be built from. A reference document describes a system that exists, and a design document describes one that does not yet.

## Verify against the source

This file is a cache, current as of 2026-09-20. IEEE Std 1016-2009 is a paid standard: the summary above reflects its published scope and abstract, not its full text. Check the canonical sources directly for anything not covered here.
