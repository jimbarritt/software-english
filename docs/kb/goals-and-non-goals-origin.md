# Goals and Non-Goals: origin and structured alternatives

2026-09-22

## Verdict

"Goals and Non-Goals" is a Google convention. No source claims to have
invented it, and no earlier, unrelated use of the same paired heading
exists. Other companies now copy it directly into their own design and
RFC templates, rather than reinventing it independently.

## Origin

The most-cited source is Malte Ubl's
["Design Docs at Google"](https://www.industrialempathy.com/posts/design-docs-at-google/).
It documents Google's internal template, and does not claim to have
originated it.

Its stated reason for the section: a non-goal is not a negated goal.
"The system shouldn't crash" does not belong there. A non-goal is
something that could reasonably have been a goal and was explicitly
declined, for example ACID compliance, when the system being designed
is a database.

Other companies' public templates copy the same heading directly.
[Squarespace's RFC template](https://engineering.squarespace.com/s/Squarespace-RFC-Template.pdf)
is one example: "Overview: Goals and Non-Goals" as a heading,
unchanged.

## A ruled-out lead

IETF working-group charters are older, and also pair a stated aim with
a stated boundary, so they looked like a plausible earlier source.
[RFC 1603](https://www.rfc-editor.org/rfc/rfc1603) and
[RFC 2418](https://www.rfc-editor.org/rfc/rfc2418.html) require a
charter to state "Goals and milestones": a timetabled list of
deliverables, not a Goals/Non-Goals pair. Checked directly against
both RFCs: neither contains a "Non-Goals" heading. Same shape, a
stated aim against a stated boundary, different pairing, no textual
link to the Google-style heading.

## Structured alternatives

| Alternative | What it changes | Adopted by |
|---|---|---|
| Goal paired with a success criterion | Each Goal states how you will know it succeeded, not only what it aims at | [Kubernetes Enhancement Proposals](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template) |
| Five-part scope statement | Objectives, deliverables, scope boundaries and exclusions, constraints, acceptance criteria, instead of two headings | PMI-style project scope statements |
| In scope / Out of scope | Names a boundary rather than an aspiration, so it is not misread as a wish list | Common alongside Goals/Non-Goals, rarely a full replacement |

Of the three, the Kubernetes fix is the most direct answer to "goals
and non-goals reads informally": same two headings, but a Goal is no
longer just a stated aim.

## Recommendation

Keep the two headings, and require each Goal to state how its success
will be checked, not only what it aims at. That is the Kubernetes fix,
it has a name and a template behind it, and it corrects the actual
gap: a bare bullet list of aims reads informally because none of them
are checkable claims.

## Sources

- [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/), Malte Ubl
- [Squarespace RFC Template](https://engineering.squarespace.com/s/Squarespace-RFC-Template.pdf)
- [RFC 1603](https://www.rfc-editor.org/rfc/rfc1603), [RFC 2418](https://www.rfc-editor.org/rfc/rfc2418.html)
- [Kubernetes KEP template](https://github.com/kubernetes/enhancements/tree/master/keps/NNNN-kep-template)
