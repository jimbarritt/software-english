# PR Description structure: a local reference for Software English

## Canonical sources

- Google Engineering Practices, "Writing good CL descriptions": https://google.github.io/eng-practices/review/developer/cl-descriptions.html
- Linux kernel, "Submitting patches", section "Describe your changes": https://www.kernel.org/doc/html/latest/process/submitting-patches.html#describe-your-changes
- GitHub Docs, "Linking a pull request to an issue": https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue

No standards body defines a pull request description. Independent
guides converge on the same core content. Treat this as convergent
practice, not a formal standard, the same way as for a Lab Notebook.

Google's guide describes a changelist (CL) description, the name
Google uses for one reviewed change. The kernel guide describes the
commit log of one patch. Both describe the text a reviewer reads
with one change, which is what a pull request description is.
GitHub's documentation defines the mechanics of a pull request, such
as a closing keyword, and not its content.

The section structure below, and the rules at SPEC §7.15 and §7.16,
are Software English's own. Neither guide names these sections.

## What a PR description is

A pull request (PR) description states a change already made, and
the evidence that it works. A reviewer reads it to decide whether to
approve the change, often before reading the diff. A later
maintainer reads it in the history to learn why the code has its
current form.

Write it for a reviewer who has not seen the diff. The diff shows
which lines changed. It does not show what was wrong before the
change, why the change takes this approach, which alternative was
rejected, or what was verified and what was not. A PR description
states those facts. It does not restate the diff file by file.

Both guides ask for the same content: the problem the change solves,
then what the change does and why, with any known shortcoming
named. The kernel guide also asks for a description a reviewer
understands without following a link.

## Structural conventions

A PR description has these parts, in this order:

1. **Title.** One line, in the imperative mood, that states what the
   change does: `Attach the receipt file to each settlement record`.
   Both guides ask for a first line that is complete alone, since a
   log or a list of changes shows the first line only.
2. **Summary.** One or two sentences that state what the change does
   (SPEC §7.1).
3. **Problem.** What was wrong or missing before the change. Name
   the file, the field, the record, or the request concerned (SPEC
   §7.15). State the problem here even where an issue also states
   it: a tracker id stops resolving once the tracker is migrated
   (SPEC §7.14).
4. **Change.** What the change does, at the level a reviewer checks
   against the diff. State the facts the diff does not show: why the
   change takes this approach, each alternative rejected and the
   reason, and each known shortcoming.
5. **Verification.** Each check that ran, with its result (SPEC
   §7.16): `` `make test`: passed, 212 tests ``.
6. **Not verified.** Each check that did not run, or could not run,
   and the reason: `` `make e2e`: not run, because the suite needs
   staging credentials ``. Leave this section out only where every
   relevant check ran.
7. **Closing keywords.** Optional. One line per issue the change
   resolves, in the form a tracker reads: `Closes #11`.

A short change may state the Problem and the Change in one paragraph
each, with no headings.

## Software English addition: two rules for this type

This section is Software English's own rule, not the wording of
either guide. Two rules govern this type's content. §7.16 applies to
a PR description and to no other type. §7.15 applies to every type,
and on a PR description it covers the problem statement and the
change statement.

- **No abstract stand-in for an artefact ([SPEC §7.15](../spec/SPEC.md)).**
  The problem statement and the change statement name the artefact
  concerned. `The report gave the operator no visibility` names no
  artefact. `The report listed no failed orders` names one. In a PR
  description, the nouns `evidence`, `context`, `visibility`,
  `coverage`, and `insight` are the common stand-ins. Each is
  correct where the thing named is itself abstract, so the rule
  needs judgement and is not a banned-word entry.
- **No check without its result ([SPEC §7.16](../spec/SPEC.md)).**
  Each verification entry pairs a check with its result. A bare
  `` `make test` `` reads as evidence and states none. A Not
  verified section is correct content, and the rule does not apply
  to it.

## Software English addition: read the whole description before presenting it

Read the whole description from start to end before presenting it,
as a reviewer reads it. A pass that corrects only the lines an
earlier pass flagged can leave a sentence that states no fact:

> It reports four counts, and a reason where the sync itself stopped.

The sentence names none of the four counts, and `where` stands in
for a condition. Fix:

> The summary reports the number of orders read, written, skipped,
> and failed. When the sync stops before the end of the ledger, the
> summary also states the reason.

A clean deterministic-tier result is necessary, and not sufficient.
The deterministic tier checks words, phrases, and sentence length.
It does not check whether a sentence names an artefact or states a
result.

## Other rules that apply

- [SPEC §7.7](../spec/SPEC.md): state what changed and why. Do not
  narrate how the change was arrived at: no account of review
  rounds, earlier attempts, or the conversation that produced it.
- [SPEC §7.14](../spec/SPEC.md): no follow-up pull request or later
  change named as a unit of work, and no issue id used as the
  pointer to later work. A closing-keyword line is exempt.
- [SPEC §7.9](../spec/SPEC.md) does not apply: a PR description is
  not a Reference document.

## How this differs from the neighbouring types

| Type | What it contains | State of the decision |
|---|---|---|
| ADR | One decision, its context, and its consequences | Taken |
| Design | The strategy for one system, its decisions, and what stays open | Taken, with named gaps |
| PR Description | One change, the problem it solves, and the evidence that it works | Made, with its checks stated |
| Reference | What the built system is | Built |

An ADR records one decision and its reason, and stays in the
repository as a record. A design document states a design before it
is built. A PR description states one change after it is made, and
the checks that show it works. A PR description may link to the ADR
or the design document the change implements, and does not restate
it. A commit message is not this type, and SPEC §7.16 does not apply
to it.

## Verify against the source

Check the canonical sources directly for anything not covered here.
None of the three is a formal standard, and each can change with no
version number.
