# RFC structure reference (cache for Software English)

## Canonical sources

- Requirement keyword definitions: https://www.rfc-editor.org/rfc/rfc2119.txt
- Structural and editorial conventions: https://www.rfc-editor.org/rfc/rfc7322.html

This file is a cache. It does not replace the canonical sources. Check the
canonical source directly for anything not covered here.

## Required structure

Source: RFC 7322, the RFC Style Guide.

### Front matter

The RFC Editor supplies these parts:

- First-page header (author or editor name, organisation, ISSN)
- Full title, centred
- Abstract (required)
- RFC Editor or Stream Note (optional)
- Status of This Memo (required)
- Copyright Notice (required)
- Table of Contents (required)

### Body section order

RFC 7322 states this order as strongly recommended:

1. Introduction (required)
2. Requirements Language (if the document uses RFC 2119 keywords)
3. Main content sections (document-specific)
4. IANA Considerations (required in Internet-Drafts)
5. Internationalization Considerations (if applicable)
6. Security Considerations (required)
7. References
   - Normative References
   - Informative References
8. Appendices (labelled A, B, and so on)

### Back matter

Not numbered:

- Acknowledgements (optional)
- Contributors (optional)
- Author's Address or Authors' Addresses (required)

### Key requirements

- Abstract: required. It must be self-contained, with no citations.
- Introduction: required. It states motivation and applicability.
- References: split into Normative and Informative subsections when both
  types exist.
- Security Considerations: required in every RFC.
- Author's Address / Authors' Addresses: required contact details for each
  listed author.

RFC 7322 covers further editorial detail (pagination, notation, terminology
tables, and so on) not reproduced here. Read the source document for those
rules.

## Requirement keywords

Source: RFC 2119.

- **MUST**, **REQUIRED**, **SHALL**: the definition is an absolute
  requirement of the specification.
- **MUST NOT**, **SHALL NOT**: the definition is an absolute prohibition of
  the specification.
- **SHOULD**, **RECOMMENDED**: valid reasons may exist, in particular
  circumstances, to ignore the item, but the full implications must be
  understood and weighed before a different course is chosen.
- **SHOULD NOT**, **NOT RECOMMENDED**: valid reasons may exist, in
  particular circumstances, when the described behaviour is acceptable or
  useful, but the full implications should be understood and the case
  weighed before that behaviour is implemented.
- **MAY**, **OPTIONAL**: the item is optional.

## Verify against the source

This cache is current as of 2026-09-12. Check the canonical sources directly
for anything not covered here, or if a detail appears outdated.
