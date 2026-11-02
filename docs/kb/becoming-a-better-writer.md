# Becoming a Better Writer: tips compared with Software English

2026-11-02

## Summary

Gergely Orosz's article "Becoming a Better Writer" gives software
engineers practical writing advice. Eight of its eleven editing tips
match a Software English rule, in full or in part. Three tips differ in
part from a rule, and four cover areas that Software English does not
address.

The article also gives evidence for Software English. Engineers write
more words than code, and writing has a larger effect on a career as
an engineer becomes more senior. Writing also helps readers who do not
share a native language.

## Source

- Article: Gergely Orosz, "Becoming a Better Writer", The Pragmatic
  Engineer, 18 January 2022:
  https://newsletter.pragmaticengineer.com/p/becoming-a-better-writer
- The article was paid until October 2026, when the author made it
  free.
- Jim Barritt found the article through a post by Steve Yegge on
  Mastodon.
- This note works from a copy saved on 2026-11-02. The copy does not
  include two embedded posts from X, by Curtis Einsmann and by Chris
  Henson.

## The article's evidence for Software English

Three claims in the article support a controlled language for
engineering prose.

- **Engineers write more than they code.** The article states that an
  engineer at a high-growth company or a large technology company
  probably writes more words each day than lines of code. Its list of
  everyday writing includes commit summaries, code review comments,
  chat messages, planning documents and postmortems. Most of these are
  in the scope of Software English.
- **Writing is part of senior hiring.** Amazon starts its screening of
  engineering managers with a writing exercise. Stripe and TrueLayer
  set writing exercises for senior engineering roles.
- **Writing helps readers with no shared native language.** The article
  quotes Steven Sinofsky on this point. ASD-STE100 was written for the
  same reason, for aerospace maintenance manuals.

> Writing (and reading) really helps people if they are remote, if
> there is not a shared native language, or both.

## The tips, and the rule that covers each

Relation values:

- **Match**: a Software English rule states the same advice.
- **Partial**: a rule covers part of the advice, or states it
  differently.
- **Not covered**: no rule addresses it.
- **Out of scope**: the advice is about the writing process or a
  career, not about the text.

### Editing

| Tip from the article | Software English | Relation |
|---|---|---|
| Re-read the text as its recipient. Check tone, accuracy and context. | §7.4 define before use, §7.5 no unanchored reference, §7.19 no unstated presupposition | Partial |
| Break the text into paragraphs of one thought each. | §3.3 one topic per paragraph | Match |
| Make paragraphs shorter for text that a reader reads on a phone. | No rule names the medium. | Not covered |
| Remove filler, such as an apology wrapped round a question. | §5.3 no unstated commentary, §5.4 no hedging, and the banned-word list | Match |
| Keep a document short, for example the Amazon six-page limit. | No rule sets a document length. | Not covered |
| Use shorter sentences. A tool such as Hemingway Editor highlights long ones. | §3.2 sentence length, 20 words, checked by a script | Match |
| Check the grammar, for example with Grammarly. | §4 grammar rules cover tense, voice, verb form, person and mood. No rule checks spelling or general grammar. | Partial |
| Use a bulleted list for several points, and a numbered list for items of several paragraphs. | §3.4 lists | Match |
| Use bold sparingly. Put the bold at the start of a sentence, not inside it. | §8.2 no mechanical repetition treats a run of bold lead-ins that restate their items as a fault. | Partial |
| Use a diagram or a screenshot where it shows more than words. | No rule covers pictures. | Not covered |
| Value a reader's time more than your own. | §7.1 summary before detail, and the stated purpose of Software English | Match |

### Feedback

| Tip from the article | Software English | Relation |
|---|---|---|
| Ask colleagues for feedback, with specific questions. | No rule. | Out of scope |
| Hire an editor, or write for a publication that edits. | No rule. | Out of scope |
| Use automated tools, and reject a suggestion that is wrong or does not fit. Learn which rules to ignore. | Rule severities, `.swe-ignore`, the skip-line marker, and `/swe:feedback` in `swe`, the Claude Code plugin that checks Software English | Partial |

### Improving

| Tip from the article | Software English | Relation |
|---|---|---|
| Read fiction, and study how it varies sentence length and rhythm. | §3.6 no clipped sentence run requires varied sentence length. §8.1 forbids a sentence written only for rhythm. | Partial |
| Collect well-written emails, proposals, postmortems and tickets, and copy their structure. | §7.8 document type, with a template and a canonical source for each of the 15 types | Match |
| Learn to touch type. | No rule. | Out of scope |
| Write weekly updates, project summaries, meeting summaries and proposals, and edit them with more care. | No document type exists for a status update, a meeting summary or a postmortem. | Not covered |

## Differences in approach

### Bold lead-ins

The article recommends bold on the first words of a sentence, so a
reader can scan the document. §8.2 accepts a bold lead-in that names a
term or a kind. It reports a run of lists where every item has a bold
lead-in that restates the item. The two positions are the same for one
bold lead-in on each distinct item. They differ on a bold lead-in on every
item of every list.

### Tool suggestions

The article advises a writer to reject a tool suggestion that is wrong
or that does not fit their style. In the `swe` plugin, a deterministic
error blocks a commit, a publish or a message until the text is fixed.
A writer who judges a finding wrong records it with
`/swe:feedback false-positive`. Confirmed feedback can change the rule
for every writer. In Software English, prose that reads the same from
every writer takes priority over individual style.

### Rhythm

The article recommends fiction as a model for varied sentence length
and rhythm. Software English requires varied sentence length (§3.6).
It also forbids a sentence that exists only for rhythm (§8.1).
Software English has no rule for storytelling, because its scope is
technical prose.

### The register of the article

The article is written for a general reader. Its prose uses phrases
that Software English reports, for example "writing muscle",
"superpower", "rinse and repeat" and "level up". These phrases do not
change the advice. They show that Software English is stricter than
general writing advice.

## Candidate additions to Software English

These additions follow from the tips that Software English does not
cover, or covers in part:

- a rule on bold inside a sentence, as a register rule;
- a rule or a guideline on paragraph length for text read on a phone,
  such as a chat message or an email;
- guidance on when a diagram states a fact better than prose, for the
  Design and Technical Manual types;
- document types for a status update, a meeting summary and a
  postmortem.

## References on good writing

The article recommends or cites these resources. Each one is a
candidate source for a future rule or a document type.

### Free resources

- Julian Shapiro, "The Writing Well Handbook": https://www.julian.com/guide/write/intro
- Ankur Tyagi, "A software developer's guide to writing": https://theankurtyagi.com/a-software-developers-guide-to-writing/
- Google, technical writing courses: https://developers.google.com/tech-writing
- Leadership Lab, "The Craft of Writing Effectively", a video of about
  90 minutes: https://www.youtube.com/watch?v=vtIzMaLkCaM
- Steven Sinofsky, `Writing is Thinking`: https://medium.learningbyshipping.com/writing-is-thinking-an-annotated-twitter-thread-2a75fe07fade
- Gergely Orosz, "Undervalued software engineering skills: writing well": https://blog.pragmaticengineer.com/on-writing-well/
- Will Larson, "Weekly updates": https://lethain.com/weekly-updates/
- Cloudflare, "Understanding how Facebook disappeared from the
  Internet", an example of a postmortem that uses a picture for most
  paragraphs: https://blog.cloudflare.com/october-2021-facebook-outage/
- Who Pays Technical Writers, a list of publications that pay for
  articles and often edit them: https://whopaystechnicalwriters.com/

### Books

- William Zinsser, "On Writing Well"
- Benjamin Dreyer, "Dreyer's English"
- William Strunk Jr and E. B. White, "The Elements of Style"
- Piotr Sarna and Cynthia Dunlop, "Writing for Developers", Manning: https://www.manning.com/books/writing-for-developers

### Tools

- Hemingway Editor, for readability: https://hemingwayapp.com/
- Grammarly, for grammar, readability and tone: https://www.grammarly.com/
- Excalidraw, Lucidchart and Miro, for diagrams
