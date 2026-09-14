---
title: A Markdown style sampler
description: Headings, lists, quotes, tables, images, and code in one readable article.
slug: markdown-showcase
published: 2026-09-12
tags:
  - markdown
  - theme
  - static-site
---

A theme should make ordinary writing comfortable to read before it adds any
decoration. This article puts several common Markdown elements together so you
can compare spacing, contrast, and line length in the rendered result.

## Text with a little emphasis

Use **bold text** for a key idea, *emphasis* for a change in tone, and `inline code`
for a filename or configuration key. A paragraph should still read naturally
when those details appear together.

The [theme guide](theme-guide) explains how the template is organized. For the
engine implementation and additional examples, visit the
[ScissorHands.NET repository](https://github.com/getscissorhands/ScissorHands.NET).

### A smaller heading

Headings divide the article into sections rather than acting as a way to make
arbitrary text larger. This third-level heading belongs to the text section
above it.

## Lists and nested content

Keep the structure of an article visible:

- Content
    - Write a useful title and description in frontmatter.
    - Keep related paragraphs under a descriptive heading.
- Presentation
    - Let the theme supply colors and spacing.
    - Check the result in both light and dark mode.

An ordered list works well for a sequence:

1. Edit a Markdown source file.
2. Generate the site.
3. Open the article at a narrow viewport.
4. Follow its tags to discover related posts and pages.

> A good starter is small enough to understand and complete enough to change
> with confidence.
>
> Try increasing the default font size and check that the layout still works.

## An image from the content directory

![A hand holding scissors with two sparkles beside it.](images/sample.svg)

*This local illustration uses the same base-relative asset path on posts,
pages, and sites published under a subpath.*

## A compact comparison table

| Element | What to inspect | Expected behavior |
| --- | --- | --- |
| Heading | Size and spacing | The outline is easy to scan |
| Paragraph | Width and line height | Long passages remain readable |
| Tag | Wrapping and contrast | Labels remain recognizable as links |
| Image | Container width | The image fits without stretching the page |
| Code | Whitespace and overflow | Long lines scroll inside their block |

### Code preserves its formatting

```csharp
using ScissorHands.Web;

var app = new ScissorHandsApplicationBuilder(args).Build();
await app.RunAsync();
```

The next example deliberately includes a long line. On a phone, the code block
should scroll horizontally rather than widen the entire document.

```json
{
  "description": "A deliberately long sample value used to check horizontal scrolling inside a code block while the surrounding article stays within the viewport."
}
```

Fenced blocks demonstrate formatting, not a dependency on a client-side syntax
highlighting library.

---

## Continue exploring

Read the [layout and typography page](theme-guide/layout), compare the
[Markdown tag](tags/markdown), or open the [reference notes](reference) for a
small page that intentionally stays out of the main navigation.
