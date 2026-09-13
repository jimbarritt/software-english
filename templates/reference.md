# Reference (Diátaxis documentation type): cached reference for Software English

## Canonical sources

- Framework overview: https://diataxis.fr/
- Reference page: https://diataxis.fr/reference/

## What a reference document is

Diátaxis names four documentation types: tutorials, how-to guides, technical reference, and explanation. It places these four in a systematic relationship and organises documentation around the structure of the need each type serves.

A reference guide is information-oriented. Diátaxis describes it as a technical description of machinery and how to operate it, giving "propositional or theoretical knowledge that a user looks to in their work." It serves a user who needs a fact while working, not a reader working through material start to finish: "one hardly reads reference material; one consults it."

Reference material is led by the product it describes, not by the user's task or goal. Diátaxis states its only purpose is "to describe, as succinctly as possible, and in an orderly way." Users need reference material because they need truth and certainty, described as "firm platforms on which to stand while they work," so reference must be authoritative, with no doubt or ambiguity.

## Structural conventions

Diátaxis gives concrete writing guidance for reference material:

- Mirror the structure of the product in the structure of the documentation, so a reader can navigate the two together.
- Keep the material consistent: use standard, predictable patterns so a reader can find information where they expect it, in a familiar form.
- Describe, and only describe. Do not explain or instruct within a reference document; link to explanation or how-to material instead.
- Write in an austere, neutral, factual style: neutrality, objectivity, and factuality over narrative.
- State facts directly, for example: "You must use a. You must not apply b unless c."
- List commands, options, features, and limitations in full.
- Use examples only to illustrate a stated fact, not to explain or instruct.

## Software English addition: no planning or task-oriented content

This section is Software English's own rule ([SPEC §7.9](../spec/SPEC.md)), not Diátaxis's wording. It follows from the "describe, and only describe" guidance above, but names a concrete category that guidance does not.

A reference document holds no planning or task-oriented content. This excludes:

- an open question;
- a "next steps" section or sentence;
- a statement of who will do work, or when;
- a pointer to a plan document or a task list;
- a statement of the document's own purpose relative to a task or a decision in progress.

A sentence that states where planning content belongs is itself planning content, even when it points away from the document. Put such content in the plan document, or delete it.

## How this differs from explanation

A reference document is information-oriented: it describes what something is, states the facts of a system accurately and completely, and serves a user who needs to check a detail while working. An explanation is understanding-oriented: it addresses why something is the way it is, giving background, context, and reasoning, and serves a reader seeking deeper understanding of a topic, not one looking up a fact or completing a task. Reference states; explanation clarifies.

## Verify against the source

This file is a cache, current as of 2026-09-12. Check the canonical sources directly (https://diataxis.fr/reference/ and https://diataxis.fr/) for anything not covered here, and for any update to the framework's wording.
