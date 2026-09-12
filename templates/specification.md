# Structural conventions for a formal technical specification (Software English reference cache)

## Canonical sources

- W3C QA Framework: Specification Guidelines — https://www.w3.org/TR/qaframe-spec/
- RFC 2119, Key words for use in RFCs to Indicate Requirement Levels — https://www.rfc-editor.org/rfc/rfc2119.txt

## Conformance structure

Guidance from the W3C QA Framework document:

- A specification must include a conformance clause. The clause states what may conform and how. It defines what an implementer must do to achieve conformance. It may reference other parts of the specification for detail.
- A specification must identify the classes of products the requirements apply to. A class of products is a type of product or service that implements the technology, for example content, producers, protocols, APIs, agents, or guidelines. Similar products group into generic categories. Each class appears in the specification's scope section.
- The conformance clause must state how to tell normative content from informative content.
- Normative content is prescriptive: it states requirements. Informative content is for information only: it does not state requirements.
- A specification should label each section heading as normative or informative, for example with a parenthetical mark such as "Glossary (Non-Normative)".
- A specification should list, in the conformance section, every section of the document together with its normative or informative status.
- A specification should avoid language that sounds normative inside an informative section.

The fetched summary of the W3C document did not return exact clause numbers (for example "3.2.1") for each guideline above. Check the source page directly for the numbering and for surrounding guidelines not covered here.

## Requirement keywords

From RFC 2119. Many non-RFC specifications, including W3C specifications, reuse these keywords by reference rather than redefining them. A specification that does this must cite RFC 2119 in its conformance clause.

- **MUST**, **REQUIRED**, **SHALL** — mean that the definition is an absolute requirement of the specification.
- **MUST NOT**, **SHALL NOT** — mean that the definition is an absolute prohibition of the specification.
- **SHOULD**, **RECOMMENDED** — mean that valid reasons may exist, in particular circumstances, to ignore a particular item, but the full implications must be understood and weighed before choosing a different course.
- **SHOULD NOT**, **NOT RECOMMENDED** — mean that valid reasons may exist, in particular circumstances, when the particular behaviour is acceptable or even useful, but the full implications should be understood and the case weighed before implementing any behaviour described with this label.
- **MAY**, **OPTIONAL** — mean that an item is optional. One implementer may include the item because a market requires it, or because the implementer judges that it improves the product. Another implementer may omit the same item.

RFC 2119 also notes that these terms hold weight only when capitalised, and that overuse of the terms hides the critical requirements in a specification.

## Verify against the source

This file is a cache, current as of 2026-09-12. Check the canonical sources above directly for anything not covered here, and for exact section numbering in the W3C document.
