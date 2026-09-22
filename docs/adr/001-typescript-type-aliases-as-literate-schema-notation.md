# ADR 1: TypeScript type aliases as the literate schema notation

## Status

Accepted, 2026-09-22.

## Context

Software English adds an API Design document type, a
specialisation of the Design type, for HTTP APIs and event or message
APIs. The planning record is `tasks/future-api-design-doc-template.md`
on the `planning` branch of `jimbarritt/claude-plugins`.

A document of that type defines the entities in an API's requests,
responses, and messages. Each
entity definition serves two consumers with different needs. A person
reviewing the design reads the definition to learn the shape of the
data. A schema registry, a validator, or a code generator consumes a
formal schema, in Avro or JSON Schema. Avro and JSON Schema are
verbose: the JSON Schema for a two-level entity is about three times
the length of the equivalent TypeScript, and neither is laid out for a
person reading top to bottom. The document therefore holds two layers:
a literate definition in the body, and the formal schema in an
appendix.

The literate layer has one criterion: the number of constructs a
reader has to hold to parse it. A design document exists to be read,
so fewer constructs is better, and a construct that names something
outside the domain (a transport term, a decorator) costs more than one
that names the domain thing.

Nine notations were assessed on that criterion against one example, an
order with lines.

TypeScript type aliases use one keyword, `type`, and mark only the
optional field, so a required field has no marker. A constraint the
type system cannot express (a timestamp format, a decimal string, a
minimum) goes in a trailing comment. Most readers of a design document
already read TypeScript.

TypeSpec (Microsoft, version 1.16.0) reads like TypeScript with
decorators for constraints. Its compiler emits OpenAPI 3 and JSON
Schema 2020-12; a compiled example confirmed both emitters, and that
one interface line emits an endpoint with its responses. It costs five
constructs (`model`, `scalar`, `enum`, decorators, and `#{ }` object
values) where TypeScript costs one, and it has no Avro emitter.

Avro IDL and Protobuf both name a domain entity in transport terms,
`record` and `message`, so parsing them requires a translation from the
domain model to the transport's model. Protobuf also puts a field number
on every line, requires a zero enum value, and has no required marker
in proto3.

GraphQL SDL names an entity `type` and costs about as many constructs
as TypeScript. It marks every required field with `!`, so the common
case has a marker; it has no string-literal union; and a named
alias needs a `scalar` declaration. Fewer readers know it.

CUE puts the constraint in the type (`quantity: int & >=1`) and exports
JSON Schema and OpenAPI, at the cost of its definition syntax and a
small readership. Smithy uses decorators and a `structure` keyword, the
same cost as TypeSpec. Zod and TypeBox are code, not notation. A field
table has no nesting, so it fails at an entity with lines.

## Decision

We will write the literate definition of each entity in an API Design
document as TypeScript type aliases.

The definition uses the `type` keyword only. `interface` is not used:
both declare the same shape, and one keyword is fewer than two. A union
of string literals defines an enumeration. A trailing comment states
any constraint the type system does not express: a format such as
RFC 3339, a decimal string, a minimum, a uniqueness rule.

The formal schema, in Avro or JSON Schema, is in an appendix of the
same document. It is the artefact a registry or a validator consumes.

## Consequences

The body of an API Design document is readable by anyone who reads
TypeScript, and it defines each entity in the domain's own terms.

No tool derives the formal schema from the TypeScript definition, or
the reverse. The two layers are kept in step by hand, and a review of
the document checks that they agree. A generator from the formal layer
to OpenAPI or AsyncAPI remains possible, since that layer is a standard
format. TypeSpec was assessed for that role and is not part of the
document.

A constraint stated in a comment is checked by no tool. The formal
schema in the appendix is where a constraint is enforced.

The rules here (the `type` keyword only, a trailing comment for a
constraint) are Software English's own convention, not a rule of any
external standard. They belong in the API Design type's local
reference file when that type is added to Appendix F of the
specification.
