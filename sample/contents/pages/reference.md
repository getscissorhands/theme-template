---
title: Reference notes
description: A tagged page that is published without joining the main navigation.
slug: reference
show_in_navigation: false
tags:
  - reference
  - theme
  - markdown
---

Not every published page needs a place in the header. This page uses `show_in_navigation: false`, so it stays out of the main navigation and the automatic Previous/Next sequence.

It is still reachable through links and the [theme tag](tags/theme), where it appears beside opted-in pages and dated posts.

> Navigation visibility is a presentation setting, not access control. Do not place private content in a generated site and rely on an absent menu link to protect it.

## Useful source locations

| Source | What it demonstrates |
| --- | --- |
| `pages/about.md` | A single page opted into navigation |
| `pages/theme-guide/index.md` | A directory landing page |
| `pages/theme-guide/01-layout.md` | Source ordering with a stable slug |
| `pages/theme-guide/02-recipes/01-content.md` | A missing-parent navigation group |
| `posts/markdown-showcase.md` | A longer article with varied Markdown |
| `pages/draft-example.md` | A source excluded from generated output |

Return to the [theme guide](theme-guide) or read more in the
[upstream engine sample](https://github.com/getscissorhands/ScissorHands.NET/tree/vnext/samples/ScissorHands.Sample).
