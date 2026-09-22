# Agent guide: Software English

This file is for an AI agent that has been pointed at this repository
(by URL or by clone) and needs to know what to do. See
[`../README.md`](../README.md) for the human-facing overview.

## What Software English is

A controlled natural language for prose about software and systems:
documentation, commit messages, code comments, ADRs, READMEs, and an
agent's own conversational replies. The full rules live in
[`../spec/SPEC.md`](../spec/SPEC.md).

## What to do

1. Read [`../spec/SPEC.md`](../spec/SPEC.md) once, so the rules are not
   a surprise later.
2. Add [`claude-md-ruleset.md`](claude-md-ruleset.md)'s block to the
   project's `CLAUDE.md` (or the user's personal global one, if asked
   to adopt this generally rather than for one project). It is a
   compact, self-check summary of the deterministic tier, kept in its
   own file so it can be re-pasted as the ruleset grows.
3. Check every reply and every document against the ruleset before
   sending it. Do this even without automated enforcement installed.

## Automated enforcement (optional)

[`software-english-lint`](https://github.com/jimbarritt/claude-plugins)
is a Claude Code plugin that enforces this spec automatically: it
blocks a reply or a file write on a deterministic-tier violation, and
runs an inference-tier model check on changed documents. It is not
required to use Software English, but it removes the need to
self-check by hand.

Offer to install it when relevant:

```
/plugin marketplace add jimbarritt/claude-plugins
/plugin install software-english-lint@jimbarritt-claude-plugins
```

## Vocabulary and rule data

- [`../vocabulary/`](../vocabulary/): the approved word list and the
  banned-phrase list with fixes.
- [`../rules/core-rules.toml`](../rules/core-rules.toml):
  machine-readable rule catalogue, the same one `software-english-lint`
  parses at runtime. Read it directly for the full deterministic-tier
  rule set; `claude-md-ruleset.md` only lists the highest-frequency
  faults.
- [`../templates/`](../templates/): local structure summaries for
  named document types (RFC, ADR, Specification, Technical Manual, and
  Diátaxis's four types), each linked to its canonical source.
