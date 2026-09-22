# API Design document structure: a local reference cache for Software English

## Canonical sources

- Parent type: [Design](design.md), by IEEE Std 1016-2009 and Ubl,
  "Design Docs at Google" (2020).
- HTTP semantics: RFC 9110, `HTTP Semantics` (IETF, June 2022, STD 97):
  https://www.rfc-editor.org/rfc/rfc9110.html
- HTTP message syntax: RFC 9112, `HTTP/1.1` (IETF, June 2022, STD 99):
  https://www.rfc-editor.org/rfc/rfc9112.html
- Schema notation: Apache Avro Specification (Apache Software
  Foundation, 1.12.2): https://avro.apache.org/docs/current/specification/
- Schema notation: JSON Schema, 2020-12 (OpenJS Foundation):
  https://json-schema.org/specification
- Event envelope convention: CloudEvents 1.0.2 (CNCF):
  https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md
- Cross-reference, a generation target: OpenAPI (OpenAPI Initiative):
  https://spec.openapis.org/oas/latest.html
- Cross-reference, a generation target: AsyncAPI (AsyncAPI Initiative):
  https://www.asyncapi.com/docs/reference/specification/v3.1.0

## What an API Design document is

An API Design document is a specialisation of the Design type
([`templates/design.md`](design.md)). It states the design of one API:
chosen and not yet built, or already built and now recorded. It covers
two transports: an HTTP API, and an event or message API over Kafka
topics with Avro payloads and a schema registry.

No source defines "API design document" as a structured document
type. The structure below is Software English's own addition. Each
part inside it cites the standard that governs its own syntax: request
and response syntax from RFC 9112, schema notation from Avro or JSON
Schema, event envelope fields from CloudEvents where a document uses
it.

OpenAPI and AsyncAPI are cross-references, not the structure an API
Design document follows. An API Design document may generate an
OpenAPI or an AsyncAPI document later. It does not reuse either one's
own document shape.

## Structural conventions

An API Design document keeps the Design type's seven sections, in the
Design type's own order. Section 3, "The design," holds five
API-specific subsections in place of open prose:

1. **Context and scope**, per the Design type.
2. **Goals and non-goals**, per the Design type.
3. **The design.**
   1. **Entity schema.** One TypeScript `type` alias per entity, in
      the domain's own terms. A trailing comment states any constraint
      the type system cannot express: a format such as RFC 3339, a
      decimal string, a minimum value. See "Schema notation" below.
   2. **HTTP endpoints.** One subsection per endpoint: a signature
      line (method, path, a one-line purpose), then at least one
      example request and response, in the raw HTTP format below.
   3. **Events and messages.** One subsection per topic: the topic
      name, the message key, the schema subject and version, any
      headers sent, and an example value, in the format below.
   4. **Errors.** The error shape as a `type`, a table of status codes
      and their meaning, and one example.
   5. **Versioning and compatibility.**
4. **Alternatives considered**, per the Design type.
5. **Cross-cutting concerns**, per the Design type: security,
   authentication, observability, idempotency, and rate limits are
   common entries for an API.
6. **Open questions**, per the Design type.
7. **Future extensions**, per the Design type.

Appendix A holds prior art. Appendix B holds the formal schema, in
Avro or JSON Schema. Appendix C holds a generated artefact, an OpenAPI
or an AsyncAPI document, where one exists.

Entity schema comes before the endpoints and the messages, because an
endpoint or a message example refers to an entity's type.

## Schema notation

An entity has two layers. The body holds a literate definition, for a
person reading the document. Appendix B holds the formal schema, the
artefact a registry or a validator consumes. The two layers state the
same entity in different notations, and a review checks that they
agree.

The literate layer uses TypeScript `type` aliases, decided in
`docs/adr/001-typescript-type-aliases-as-literate-schema-notation.md`.
The rule: `type` only, never `interface`. A union of string literals
defines an enumeration. A trailing comment states a constraint the
type system does not express.

```typescript
type OrderLine = {
  sku: string;
  quantity: number; // minimum 1
  unitPriceMinorUnits: number;
};

type Order = {
  id: string; // format ord_<26-character ULID>
  status: "placed" | "shipped" | "delivered" | "cancelled";
  placedAt: string; // RFC 3339 timestamp
  lines: OrderLine[];
};
```

The formal layer, in Appendix B, is Avro or JSON Schema. Which one to
use follows what the API's own registry uses: Avro for a Kafka topic
with a schema registry, JSON Schema otherwise.

## HTTP example format

A request and response example follows the HTTP/1.1 message syntax of
RFC 9112: a start line, headers, a blank line, then a body. This
matches the `.http` file convention used by several editors.

```http
POST /orders HTTP/1.1
Content-Type: application/json

{ "lines": [{ "sku": "SKU-1", "quantity": 2, "unitPriceMinorUnits": 500 }] }

HTTP/1.1 201 Created
Content-Type: application/json
Location: /orders/ord_01J8ZK3QW4N9X2M7P5R1T6V0B8

{ "id": "ord_01J8ZK3QW4N9X2M7P5R1T6V0B8", "status": "placed", ... }
```

## Message example format

A topic example mirrors the HTTP example's shape: a request line's
role is played by `topic` and `key`, and `schema` names the registry
subject and version, the one field with no HTTP equivalent.

```text
topic:   orders.order-placed.v1
key:     ord_01J8ZK3QW4N9X2M7P5R1T6V0B8
schema:  orders.order-placed.v1-value, version 3

headers:
  <any headers actually sent, plain key: value>

value:
{ ... Avro record rendered as JSON, in the entity schema's shape ... }
```

`value` is the Avro record rendered as JSON, since binary Avro is not
readable, and uses the same TypeScript type as the entity schema.
`headers` is empty by default. A document whose API uses CloudEvents
states that in its context section, and its `headers` block then
follows CloudEvents' own attribute names, cited by reference.

## Software English addition

This file's structure, the two example formats, and the
literate-schema rule are Software English's own addition. No cited
source defines a document type for API design, an HTTP-and-message
example pairing, or a `type`-only rule for a literate schema. Each
part inside the structure still cites the standard that governs its
own syntax.

Every rule that applies to a Design document applies to an API Design
document unchanged, including the rules stated in
[`templates/design.md`](design.md): the open-questions and
future-extension sections are correct content, and §7.7 still forbids
narrating how a decision was reached.

Section 3's style rule: every endpoint and every topic shows at least
one example request and response, or one example message value.

## Verify against the source

This file is a cache, current as of 2026-09-22. Check the canonical
sources directly for anything not covered here, RFC 9110 and RFC 9112
in particular: both define more header and status semantics than this
cache states.
