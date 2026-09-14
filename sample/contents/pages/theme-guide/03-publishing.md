---
title: Publishing
description: Preview the theme locally, then generate files for a static host.
slug: theme-guide/publishing
show_in_navigation: true
tags:
  - theme
  - static-site
  - navigation
---

The sample application uses the published engine packages and a local copy or
link of the theme sources. Run these commands from the sample application
directory.

## Preview while editing

```shell
dotnet run --no-launch-profile -- --preview
```

Preview mode serves the generated site locally. After changing Razor or C#
sources, restart with a build so the running application uses the new components.

## Generate static output

```shell
dotnet run --no-launch-profile -- --build
```

The build command writes the static site to `dist`. Review that output before
deploying it to a static host.

| Mode | Output | Use it for |
| --- | --- | --- |
| Preview | `preview/` | Local content and theme review |
| Build | `dist/` | Files to publish |

## Check the deployment base

For a site hosted at `https://example.com/project/`, configure `Site.BaseUrl`
as `/project/`. Serve the generated files at that path on the destination host.
Changing the base URL does not itself mount the local preview server under
that prefix.

Before publishing, inspect a post, a page, the [tag index](tags), and the
not-found output. Follow an image URL and a previous/next link as well as the
header navigation.

## Keep experimenting

This is the last opted-in page in the sample's current source order, so it has
no Next link. Return through Previous, open the [guide index](theme-guide),
or browse the [reference notes](reference).
