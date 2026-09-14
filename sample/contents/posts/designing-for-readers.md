---
title: Designing a small site for readers
description: A practical reading checklist for mobile layouts, keyboard navigation, and progressive enhancement.
slug: designing-for-readers
published: 2026-09-13
tags:
  - accessibility
  - theme
  - static-site
---

This second article gives the home page a more realistic list of dated posts.
Its tags overlap with the style sampler and the guide, so a topic page can show
both **Posts** and **Pages** without treating them as the same kind of content.

## Start with a narrow screen

At a small width, the header links wrap and the home-page sidebar follows the
post list. The article itself remains a single column.

Try reading with a larger browser font size as well as a narrower window.
Content should remain usable without shrinking the type to fit.

### A reading checklist

- Look for a clear page title and a consistent heading hierarchy.
- Check that long titles and tag labels have room to wrap.
- Read a code block without losing your place in the paragraph above it.
- Switch between the system's light and dark appearances.
- Check that the sidebar does not interrupt an article's reading flow.

## Navigate without a mouse

Use the Tab key to reach the header links, article links, and page-navigation
links. A visible focus outline should identify the current target.

The [theme guide](theme-guide) includes several opted-in pages. Move through
them with their Previous and Next links, then inspect the nested Recipes group
in the header. The group is a label, not a link to a missing page.

> Navigation is part of the document. It should not depend on JavaScript just
> to reveal the available pages.

## Enhance only what needs a script

The footer's local-time display is intentionally small. When JavaScript runs,
it fills a `time` element and refreshes once per minute. Without JavaScript,
that optional line stays hidden while the rest of the footer remains visible.

The content, tags, and page navigation work in either case. This makes the
clock an example to remove or replace, rather than a requirement for using
the theme.

## Review before publishing

The [publishing page](theme-guide/publishing) explains the preview and build
commands. The [theme tag](tags/theme) provides another way to navigate the
sample, including the reference page that does not appear in the header.
