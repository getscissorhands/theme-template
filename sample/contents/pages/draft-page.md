---
title: Draft page
description: A preview-only page whose Korean translation inherits its draft status.
slug: draft-page
draft: true
show_in_navigation: true
tags:
  - draft-only
---

This page declares `draft: true`, so preview includes it in the site navigation
and displays a draft badge on the page and its [tag entry](tags/draft-only).
Its Korean translation has no draft flag but inherits the primary page's status.

Production builds exclude both routes, their navigation entries, and the
`draft-only` tag. A draft is not merely an unlisted page: the published
[reference notes](reference) stay available even though they are outside
navigation. Never deploy preview output.
