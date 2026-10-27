# Intro to Software English: the deck

A 15 to 20 minute talk for engineers. It covers the writing habits of
AI agents, the ASD-STE100 background, Software English with its two
rule tiers, and the `swe` Claude Code plugin.

## Files

| File | Contents |
|---|---|
| `intro-to-software-english.md` | The deck, in [Marp](https://marp.app/) Markdown. Speaker notes are in HTML comments under each slide. |
| `theme.css` | The Marp theme. |
| `build.sh` | Builds the deck to HTML and PDF. |
| `samples/gmail-messages-before.md` | A Gmail API reference in the register an agent produces with no rule in force. 48 deterministic errors in 108 lines. |
| `samples/gmail-messages-after.md` | The same facts in Software English. 0 errors, both tiers. |
| `build/` | The built HTML and PDF. |

## Build

```sh
./build.sh          # build/intro-to-software-english.html and .pdf
./build.sh --png    # also one PNG per slide in build/slides/
```

The script needs `node`, `npx`, Playwright with its Chromium, and
`pdftoppm` for the PNG step. Marp renders the HTML. Playwright prints
the HTML to PDF, one page per slide, because Marp's own PDF export
needs a browser with open network access.

## Lint

The deck, this file, and the "after" sample pass both tiers of the
`swe` check. The "before" sample is listed in `.swe-ignore` at the
repository root: its faults are the content of the talk.
