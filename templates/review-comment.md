# Review Comment structure: a local reference for Software English

## Canonical sources

- Google Engineering Practices, "How to write code review comments":
  https://google.github.io/eng-practices/review/reviewer/comments.html
- Conventional Comments: https://conventionalcomments.org/

No standards body defines a review comment. Independent conventions
converge on the same core content. Treat this as convergent practice,
not a formal standard, the same way as for a PR Description.

The rule at SPEC §7.24 is Software English's own. Neither source
names it.

## What a review comment is

A review comment is a request, sent to the author of a change under
review, to change it. It is read by someone who has already made the
change and now has to act on the comment, or explain why not. A
comment that reads well on the first draft saves a round of
rewriting, and a round of waiting for the next review pass.

Both canonical sources converge on this: the comment states what is
wrong, what to do about it, and why, in that order. Google's guide
asks that a comment make its direction clear even where the writer
also explains their reasoning. Conventional Comments gives each
comment a label (`issue:`, `suggestion:`, `nitpick:`, `question:`,
and others) that states, before the prose does, how the author should
treat it.

## Structural conventions

A review comment has these parts. A short comment may state them in
one sentence; a longer one keeps them in this order:

1. **Problem.** The opening sentence: one plain statement of what is
   wrong with the change under review, naming the artefact concerned
   (SPEC §7.15, §7.24), before any evidence.
2. **Evidence.** Optional. A quoted line, a diff hunk, a log line, or
   a benchmark figure that supports the problem sentence. Evidence
   supports the problem statement; it does not replace it.
3. **Alternative.** The approach proposed instead of the one under
   review, including a bare request to remove the change with no
   replacement (SPEC §7.24).
4. **Steps.** What to do, concretely enough that the author can act
   with no further question: the file, the function, the flag, or the
   command, and the action on it (SPEC §7.24).
5. **Label.** Optional. A severity label in Conventional Comments'
   form, placed before the problem sentence: `issue:`, `suggestion:`,
   `nitpick:`, or `question:`.

## Software English addition: one rule for this type

This section is Software English's own rule, not the wording of
either source. SPEC §7.24 governs this type's content in full: the
problem sentence, the stated alternative, and steps concrete enough
to act on. The same rule governs a PR Description, narrowed to the
problem sentence only (SPEC Appendix F): a PR description states a
change already built, so it has no step left to give.

## Other rules that apply

- [SPEC §7.1](../spec/SPEC.md): the summary §7.1 requires is this
  type's problem sentence (SPEC §7.24). Report a missing or a late
  problem sentence under §7.24 only.
- [SPEC §7.7](../spec/SPEC.md): state the problem with the current
  version of the change. Do not narrate an earlier review round, or
  the conversation that produced this comment.
- [SPEC §7.14](../spec/SPEC.md): a step that points to a later pull
  request, or an issue id used in place of the step itself, is a
  fault. State the step.
- [SPEC §7.15](../spec/SPEC.md): the problem sentence and each step
  name the artefact concerned, not an abstract stand-in (`evidence`,
  `context`, `visibility`).
- [SPEC §7.16](../spec/SPEC.md) does not apply: a review comment is
  not a PR Description.

## How this differs from the neighbouring types

| Type | What it contains | State of the decision |
|---|---|---|
| ADR | One decision, its context, and its consequences | Taken |
| PR Description | One change, the problem it solves, and the evidence that it works | Made, with its checks stated |
| Review Comment | A problem with a change under review, its alternative, and concrete steps | Requested, not yet made |

A PR description states a change after it is made. A review comment
names a change not yet made, to the same change a PR description
accompanies. See [`templates/pull-request.md`](pull-request.md).

## Verify against the source

Check the canonical sources directly for anything not covered here.
Neither is a formal standard, and each can change with no version
number.
