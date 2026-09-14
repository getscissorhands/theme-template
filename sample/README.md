# ScissorHands.NET Sample

This project provides an end-to-end preview using the NuGet.org engine packages and the theme linked at `themes/theme-template` to `../../src`.

The About page and Theme guide opt into the header navigation with `show_in_navigation: true`. Opted-in pages appear in source-filename order and get automatic previous/next links. Nested slugs form the navigation hierarchy; nested `index.md` files without an explicit slug use the containing directory's route.

## Content Tour

| Source under `contents/` | Features to explore |
| --- | --- |
| `posts/hello-scissorhands.md` | Basic dated post and the generation pipeline |
| `posts/markdown-showcase.md` | Emphasis, nested lists, quotes, tables, local image, and wide code blocks |
| `posts/designing-for-readers.md` | Longer prose, shared tags, and an accessibility review checklist |
| `pages/about.md` | Top-level navigation entry and the start of the reading sequence |
| `pages/theme-guide/index.md` | Directory-index route and a parent navigation node |
| `pages/theme-guide/01-layout.md` | An ordered child page with an explicit, stable slug |
| `pages/theme-guide/02-recipes/01-content.md` | A nested page under a non-clickable Recipes group |
| `pages/theme-guide/03-publishing.md` | The last page in the sequence, with no Next link |
| `pages/reference.md` | Published and tagged, but excluded from navigation |
| `pages/draft-example.md` | Excluded from output, navigation, and the tag index |
| `pages/not-found.md` | The custom 404 view |

The guide's numeric source prefixes control reading order without becoming part of its explicit child URLs. The `theme` tag is shared by posts and pages, so its detail view exercises both lists. Markdown links and the local illustration use base-relative paths.

## Running the Sample

Run from this directory. The launch profile enables preview mode:

```bash
dotnet run -- --preview
```

The launch profile also starts preview mode automatically when run from an IDE.

Generate static files without starting the preview server:

```bash
dotnet run --no-launch-profile -- --build
```

Generated preview and build outputs are written to `preview/` and `dist/` respectively.

The sample starts with an empty `Plugins` array in `appsettings.json`. To enable plugins, see the [plugin guide](https://getscissorhands.app/docs/plugins/).