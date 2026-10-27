# Gmail API: the Messages resource

A Reference for the Messages resource of the Gmail API, version 1.

## Overview

A message is one email. Each message has an `id` and a `threadId`.
The `threadId` names the thread that contains the message. The
resource has three operations: list, get, and send.

Every request path starts with `/gmail/v1/users/{userId}`. `userId`
is the user's email address, or the value `me`. `me` names the user
that the access token identifies.

## List messages

`GET /gmail/v1/users/{userId}/messages` returns references to
messages. A reference has two fields, `id` and `threadId`, and no
other field. A separate get request returns the content of a message.

Parameters:

| Parameter | Meaning |
|---|---|
| `q` | A search query. The syntax is the Gmail search box syntax, for example `from:alice is:unread newer_than:7d`. |
| `maxResults` | The number of references per page. The default is 100. The maximum is 500. |
| `pageToken` | The token of the page to return. |
| `labelIds` | Return only a message that has every label in the list. |
| `includeSpamTrash` | When `true`, the result includes messages in Spam and Trash. |

A response has three fields:

- `messages`: the references on this page;
- `nextPageToken`: the token of the next page. The field is absent on
  the last page;
- `resultSizeEstimate`: an estimate of the total number of results.
  The value is not exact.

A request with `pageToken` set to the `nextPageToken` of a response
returns the next page.

## Get a message

`GET /gmail/v1/users/{userId}/messages/{id}` returns one message. The
`format` parameter selects what the response contains:

| `format` | Response |
|---|---|
| `full` | The headers, the labels, and the body, parsed into a tree of MIME parts. This is the default. |
| `metadata` | The headers and the labels, with no body. `metadataHeaders` lists the headers to return. |
| `minimal` | The `id`, the `threadId`, and the labels. |
| `raw` | The complete RFC 2822 message as one base64url-encoded string. |

In a `full` response, the body of a part is base64url-encoded, in
`payload.parts[].body.data`. A multipart message has a part that
contains other parts. A client decodes each body and reads each level
of the tree.

## Send a message

`POST /gmail/v1/users/{userId}/messages/send` sends one message. The
request body has one required field, `raw`: the complete RFC 2822
message, base64url-encoded. The client builds the MIME message and
encodes it. Gmail delivers the message, adds it to a thread, and adds
the `SENT` label.

A request with `threadId` set adds the message to that thread. The
`Subject` header must match the thread, and the `References` and
`In-Reply-To` headers must name a message in it.

## Scopes

Each operation requires an OAuth scope:

| Operation | Scope |
|---|---|
| List, get | `https://www.googleapis.com/auth/gmail.readonly` |
| Send | `https://www.googleapis.com/auth/gmail.send` |
| Modify labels | `https://www.googleapis.com/auth/gmail.modify` |

A request with a narrower scope than the operation requires returns
HTTP 403.
