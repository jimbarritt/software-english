# Gmail API: the Messages resource

This is the "before" sample for the Intro to Software English talk. It
was written in the register an AI agent falls into when nobody asks it
not to. Every fact in it is correct. The prose around the facts is the
subject of the talk.

## Overview

Let's dive into the Messages resource — the beating heart of the Gmail
API. Essentially, a message is an email, and this resource is how you
list them, read them, and send them. Simple as that. Under the hood,
Gmail wants every message to live inside a thread, so you'll notice
each message carries a `threadId` alongside its own `id` — think of
the thread as the envelope and the message as the letter inside.

Crucially, this isn't just a thin wrapper over IMAP. It's a genuinely
robust, modern REST surface, and once you understand how the pieces fit
together, working with it feels seamless.

## Listing messages

To list messages, you simply call `GET /gmail/v1/users/{userId}/messages`.
The `userId` can be the user's email address, but in practice you'll
almost always want to pass the special value `me` — the API knows who
you are from the access token, so why spell it out?

Here's the thing: the list endpoint doesn't actually return messages.
It returns message *references* — just an `id` and a `threadId` for
each one. No subjects, no bodies, nothing. This trips up a lot of
people, so it's worth noting up front. The idea is that you fetch the
full message separately when you really need it.

The parameters you'll care about:

- `q` — a search query, using exactly the same syntax as the Gmail
  search box (`from:alice is:unread newer_than:7d` and so on). This is
  incredibly powerful once you get the hang of it.
- `maxResults` — how many references to return per page. Defaults to
  100, caps out at 500.
- `pageToken` — for pagination. More on that in a sec.
- `labelIds` — only return messages that have *all* of these labels.
- `includeSpamTrash` — exactly what it sounds like.

Pagination is handled gracefully: each page comes back with a
`nextPageToken`, and you just feed it into the next call. When the
token is gone, you're done. There's also a `resultSizeEstimate` field,
but take it with a pinch of salt — it's an estimate, not a promise.

## Getting a message

`GET /gmail/v1/users/{userId}/messages/{id}` is where the real payload
lives. The key decision here is the `format` parameter, and it really
pays to get this right:

- `full` — the whole message, parsed into a MIME tree of parts. This
  is the default and it's what most people reach for.
- `metadata` — just the headers and the labels. Pair it with
  `metadataHeaders` to pick exactly which headers you want back — a
  nice touch.
- `minimal` — ids and labels only. Lightweight and fast.
- `raw` — the entire RFC 2822 message as one base64url-encoded string.
  Perfect if you've already got a MIME parser you trust.

It's not about which format is "best" — it's about which one matches
what you're going to do with the data. Fetching `full` when you only
needed a subject line is wasteful, and the API won't stop you.

Note that the body text in a `full` response is base64url-encoded,
sitting inside `payload.parts[].body.data`. Don't forget to decode it!
Also keep in mind that a multipart message nests parts inside parts,
so you'll probably want a small recursive helper to walk the tree.

## Sending a message

Sending is where things get interesting. You `POST` to
`/gmail/v1/users/{userId}/messages/send` with a body containing a
single field, `raw`, which is — you guessed it — the complete RFC 2822
message, base64url-encoded. So the workflow is: build the MIME message
yourself, encode it, hand it over. Gmail takes it from there and
handles delivery, threading, and the Sent label for you. No manual
bookkeeping required.

If you want the message to land in an existing thread, just include a
`threadId` in the request body and make sure the `Subject` matches and
the `References` / `In-Reply-To` headers are set correctly. Gmail is
smart enough to figure out the rest.

## Scopes

Each of these operations needs the right OAuth scope — this is
important, so bear with me:

| Operation | Scope |
|---|---|
| List, get | `https://www.googleapis.com/auth/gmail.readonly` |
| Send | `https://www.googleapis.com/auth/gmail.send` |
| Modify labels | `https://www.googleapis.com/auth/gmail.modify` |

Obviously you should request the narrowest scope that does the job.
Users are (rightly!) nervous about granting full mailbox access, and a
scope you don't need is a scope you'll have to explain.

## What's next

We'll add a section on the `modify` and `trash` endpoints in a
follow-up, and there's an open question about whether batch requests
deserve their own page. Watch this space.
