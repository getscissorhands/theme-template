---
title: Unlisted recipe
description: A published nested page omitted from navigation and the reading sequence.
slug: theme-guide/recipes/unlisted
show_in_navigation: false
tags:
  - theme
  - navigation
  - visibility
---

This page sits beside [Writing content](theme-guide/recipes/writing) under
`theme-guide/02-recipes/`. Its route is generated in both preview and production,
but `show_in_navigation: false` keeps it out of the header and the automatic
Previous/Next reading sequence.

Writing content remains visible, so Recipes stays in the header as a
non-clickable group even though it has no directory index. If both pages were
hidden, that group would disappear from navigation without removing either
route. Hiding their existing parent, Theme guide, would also hide the branch.

Find this page through the [theme tag](tags/theme) or the
[guide index](theme-guide). Navigation visibility is not access control.
