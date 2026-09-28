---
title: Writing content
description: Use frontmatter to control page routes, navigation visibility, and shared topics.
slug: theme-guide/recipes/writing
show_in_navigation: true
tags:
  - markdown
  - theme
  - navigation
---

The `01-writing.md` source filename places this page first within the Recipes
directory. Its explicit slug keeps the public URL independent of the numeric
prefix and places it under the non-clickable Recipes group in navigation.

## Page frontmatter

```yaml
---
title: A useful page
description: A short summary for readers.
slug: guide/useful-page
show_in_navigation: true
tags:
  - writing
  - theme
---
```

The title is displayed by the page template. Start the body with an introduction and use second-level headings for its sections to avoid repeating that title.

### Navigation is an opt-in

Set `show_in_navigation: true` to include a page in the header and previous/next sequence. Posts do not join that sequence, even if the same field is present.

A page with the setting omitted or set to `false` still has a route. The
[unlisted recipe](theme-guide/recipes/unlisted) shares this source directory
but stays outside navigation and the reading sequence. This page keeps the
non-clickable Recipes group visible. If an existing parent page is hidden from
navigation, its descendants are hidden from that navigation branch too.

### Tags connect different kinds of content

The [theme topic](tags/theme) combines dated posts with guide pages. The [reference notes](reference) also appear there despite being absent from the main navigation.

### Drafts are different

`draft: true` excludes a document from production builds, rather than merely hiding its navigation entry. Preview includes drafts with required badges on articles and listing entries. Future-scheduled posts are also preview-only, and translations inherit a primary document's withheld status. Never deploy `preview/`.

## Write portable links

Use a site-base-relative path such as `[Theme guide](theme-guide)`, rather than `/theme-guide` or `../theme-guide`. The generated document's base URL lets the same link work when the static output is hosted below a subpath.

For content images, use the same convention:

```markdown
![A description of the illustration.](images/sample.svg)
```

The engine copies content assets into the output; the browser resolves their URLs relative to the document's base.
