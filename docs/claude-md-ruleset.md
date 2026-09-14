# Compact ruleset for CLAUDE.md

Paste this block into a project's `CLAUDE.md` (or a personal global one)
to adopt Software English. This is a summary for self-checking, not a
replacement for [`../spec/SPEC.md`](../spec/SPEC.md). This file changes
as the deterministic tier grows; re-paste it when it does.

---

## Software English

Write all prose in Software English:
https://github.com/jimbarritt/software-english/blob/main/spec/SPEC.md

Check your own reply against the spec before sending it. Get it right
the first time, rather than relying on a rewrite. If the
[`software-english-lint`](https://github.com/jimbarritt/claude-plugins)
Claude Code plugin is installed, it checks every reply and every
changed document too, as a backstop.

The deterministic-tier faults a writer produces most often, so check
for these before sending:

- An em dash. Use a period, a colon, or a comma instead.
- A filler intensifier: `simply`, `essentially`, `basically`,
  `genuinely`, `really`, `actually`, `obviously`, `clearly`. Cut it.
- The continuous tense for system behaviour (`is testing`,
  `is running`). Use the simple tense (`tests`, `runs`).
- A human trait, feeling, or intent given to a system, service,
  component, or process. State the mechanism instead.

### Where it does not apply

- Code itself. Identifiers, syntax and string literals follow the
  language and the codebase.
- Text quoted or repeated verbatim: tool output, error messages, file
  contents, another person's words.

### Conflicts

If a rule makes a technical fact wrong, keep the fact and break the
rule. A term with one correct name keeps that name.

---
