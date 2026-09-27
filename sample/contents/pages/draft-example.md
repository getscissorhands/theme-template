---
title: Unpublished draft example
description: A preview-only page, with an inherited draft status on its translation.
slug: draft-example
draft: true
show_in_navigation: true
tags:
  - draft-only
---

Preview includes this page, its navigation entry, and its tag with a visible draft badge. Its Korean translation inherits the draft status even though the translation does not set `draft: true`.

Production builds exclude both versions, their navigation entries, and the unique tag. Never deploy preview output.
