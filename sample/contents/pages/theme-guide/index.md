---
title: Theme guide
description: A short tour of the template's layout, content, and publishing features.
show_in_navigation: true
tags:
  - theme
  - navigation
  - directory-index
---

This is a directory landing page. Its source is `pages/theme-guide/index.md`, and it has no explicit `slug`, so the engine gives it the route `theme-guide`.

## Follow the guide

1. [Layout and typography](theme-guide/layout) introduces the Razor views and the starter stylesheet.
2. [Writing content](theme-guide/recipes/content) shows page frontmatter and the difference between navigation and tags.
3. [Publishing](theme-guide/publishing) covers local preview and static output.

The Previous and Next links follow the engine's reading sequence. The directory index comes before its children, then numeric source prefixes order the remaining pages. Explicit slugs keep the child URLs independent of those prefixes.

## Notice the Recipes group

There is no `theme-guide/recipes/index.md` in this sample. The [Writing content page](theme-guide/recipes/content) has a nested slug, so the engine creates a non-clickable **Recipes** group to hold it in the header.

The theme renders the hierarchy as nested lists. Use the arrow next to Theme guide to open its dropdown, then expand Recipes to reach Writing content. On mobile, those sections expand within the header instead of floating over the page. The links stay visible with JavaScript disabled.

## More than one way to find a page

This guide is both an opted-in navigation page and a member of the [theme tag](tags/theme). Those are independent choices: the [reference notes](reference) are tagged but intentionally omitted from the header and the reading sequence.
