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

The sample application uses the published engine packages and a local copy or link of the theme sources. Run these commands from the sample application directory.

## Preview while editing

```shell
dotnet run -- --preview
```

Preview mode serves the generated site locally, including drafts and future-scheduled posts with visible status badges. Never deploy `preview/`. After changing Razor or C# sources, stop the preview and restart with a build so the running application uses the new components.

## Generate static output

```shell
dotnet run -- --build
```

The build command writes the static site to `dist`. Review that output before deploying it to a static host.

| Mode | Output | Use it for |
| --- | --- | --- |
| Preview | `preview/` | Local review only; includes unpublished content |
| Build | `dist/` | Eligible published content only; no status badges |

## Check the deployment base

For a site hosted at `https://example.com/project/`, configure `Site.BaseUrl` as `/project/`. The preview server mounts output at that prefix and redirects `/` to `/project/`. Configure the production host to mount generated files at the same path.

For a local subpath preview, follow the commands in the sample README. `Site.TimeZone` controls the publication instant for dates without offsets; the sample uses UTC. Generation captures one time snapshot. Rebuild at or after the publication time to publish scheduled content; there is no automatic publishing timer.

Before publishing, inspect a post, a page, the [tag index](tags), and the not-found output. Follow an image URL and a previous/next link as well as the header navigation.

## Keep experimenting

This is the last opted-in page in both preview and production, so it has no Next
link. Return through Previous, open the [guide index](theme-guide), or browse
the [reference notes](reference).
