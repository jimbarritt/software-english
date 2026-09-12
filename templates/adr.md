# ADR structure: a local reference cache for Software English

## Canonical sources

This file is a cache. It does not replace the canonical sources.

- Original format: Michael Nygard, "Documenting Architecture Decisions" (2011): https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Community reference and template catalogue: https://adr.github.io/

Nygard's post defines the original canonical ADR format. The adr.github.io site hosts community variants and tools built on that format.

## Required structure (Nygard's original format)

An ADR has five parts.

1. **Title.** A short noun phrase. Example from the post: "ADR 1: Deployment on Ruby on Rails 3.0.10".
2. **Status.** One of: proposed, accepted, deprecated, or superseded. A superseded status names the ADR that replaces it.
3. **Context.** The forces at play: technological, political, social, and project-local. Context uses value-neutral language. It states facts, not arguments.
4. **Decision.** The response to the context, in full sentences with active voice, in the form "We will…".
5. **Consequences.** The resulting context after the decision applies. This includes positive, negative, and neutral outcomes for the team and the project.

Other conventions Nygard's post states:

- File location: the project repository, under `doc/arch/adr-NNN.md`.
- Format: lightweight text markup (Markdown or Textile).
- Length: one or two pages.
- Numbering: sequential and monotonic. A number is never reused.
- Immutability: a superseded ADR stays in the repository, with its status updated to "superseded". It is not deleted or rewritten.
- Writing style: full sentences in paragraphs. The post advises against bullet points, calling them "an excuse for writing sentence fragments".

## Common variants

Other ADR templates exist beyond Nygard's original. One example is MADR (Markdown Architectural Decision Records). The adr.github.io site catalogues these variants and related tooling. This file does not document each variant. Check adr.github.io for the current list.

## Verify against the source

This cache reflects the source pages as fetched on 2026-09-12. For anything not covered here, check the canonical sources directly.
