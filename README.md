# Software English

**If you are an AI agent, read [`docs/agent-guide.md`](docs/agent-guide.md)
first.** It covers what to do with this repository, including a compact
ruleset for `CLAUDE.md` and an optional enforcement plugin.

A controlled natural language for software and systems engineering prose.

Software English restricts vocabulary and grammar so that prose about
systems, code, and engineering work reads the same way from any writer,
human or AI agent. It takes its structural approach (a restricted
vocabulary, one approved sense per word, simple grammar, short sentences)
from the general field of
[controlled natural languages](https://en.wikipedia.org/wiki/Controlled_natural_language).

Note: Software English does not copy or directly derive from ASD-STE100 (Simplified Technical
English). ASD-STE100 is a copyrighted source and also is specific to the aerospace industry. Software
English has the same approach but is tailored for the domain of software engineering.
See [NOTICE](./NOTICE) for more details.

## Scope

Software English applies to any prose written about software and
systems: documentation, commit messages, code comments, ADRs, READMEs,
and an AI agent's conversational replies.

Primary reader: a human. A future "profile" may target agent-to-agent
prose instead. Not yet built.

## Structure

| Path | Contents |
|---|---|
| [`spec/SPEC.md`](spec/SPEC.md) | the specification document |
| [`docs/agent-guide.md`](docs/agent-guide.md) | entry point for an AI agent: what to do with this repository |
| [`docs/claude-md-ruleset.md`](docs/claude-md-ruleset.md) | compact, copy-pasteable ruleset for a project's `CLAUDE.md` |
| [`vocabulary/`](vocabulary/) | the approved word list (closed vocabulary) |
| [`rules/core-rules.toml`](rules/core-rules.toml) | machine-readable rule catalogue for linter consumption |
| [`templates/`](templates/) | cached structure summaries for named document types (RFC, ADR, Specification, Technical Manual, and Diátaxis's four types), each linked to its canonical source |
| [`LICENSE`](./LICENSE) | Apache-2.0 |
| [`NOTICE`](./NOTICE) | origin and independence statement |
| [`COLOPHON.md`](COLOPHON.md) | format and tooling notes |

## Conformance tiers

- **Deterministic**: checkable by a parser or a word-list lookup alone
  (vocabulary membership, sentence length, banned grammatical forms).
- **Inference-based**: needs model judgement (anthropomorphism in
  paraphrase, commentary, hedging) that a script cannot check
  exhaustively.

See [`spec/SPEC.md`](spec/SPEC.md) §2 for the full definition.

## Status

Early draft. Built alongside a Claude Code plugin
([claude-plugins](https://github.com/jimbarritt/claude-plugins)) that
enforces it, but the spec is designed to stand on its own and to be
usable by any tool.

## Licence

Apache-2.0. See [LICENSE](./LICENSE) and [NOTICE](./NOTICE).

