---
title: Layout and typography
description: The small set of views and design tokens that give the starter its appearance.
slug: theme-guide/layout
show_in_navigation: true
tags:
  - theme
  - accessibility
  - navigation
---

The layout provides a header, the page body, and a footer. Individual views
handle posts, pages, the home page, the not-found page, and tag listings.

## Readable defaults

The starter uses system fonts, a restrained accent color, and a limited reading
width. Thin borders separate content without turning every paragraph into a
card.

| Setting | Purpose |
| --- | --- |
| `--color-background` | The page background |
| `--color-text` | The primary text color |
| `--color-accent` | Links and small accents |
| `--content-width` | The maximum article width |
| `--gutter` | Space between content and the viewport |

Change these tokens in `src/assets/css/theme.css` to experiment with the design.
The dark-mode media query overrides the color tokens separately.

## Content should drive the layout

The main content stays in one column on small screens. The home page adds a
sidebar only when there is enough room, and the page-navigation links stack
vertically on narrower viewports.

Compare this page with the [Markdown topic](tags/markdown) to see the same
typography used in a longer article.

> Keep the compact reset and the visible focus styles when trying a different
> visual direction. They provide useful defaults without requiring a framework.

## A complete set of views

All seven theme roles are required by the current engine. In particular, keep
the tag-list and tag-detail views even when your first few documents have no
tags. They become useful as soon as content starts sharing topics.
