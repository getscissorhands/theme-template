# Theme preview

This app previews the theme linked at `themes/<theme-slug>` to `../../src` (`themes/theme-template` here) using ScissorHands.NET packages from NuGet. Create the link as described in the [template README](../README.md) before building; linked Razor sources must be included, but their `bin`/`obj` directories excluded.

## Build and run

Restore and generation were verified with **`1.0.0-preview.20260928.1`** for Core, Plugin, Theme, and Web. `Directory.Packages.props` intentionally floats on `1.*-*`, so future restores may select a newer release. From the repository root:

```sh
dotnet restore
dotnet list ThemeTemplate.slnx package --include-transitive
dotnet build
```

Use the renamed solution in a generated repository. From `sample`, run either mode explicitly:

```sh
dotnet run -- --preview
# Stop preview before rebuilding Razor/C# components or running build mode:
dotnet run -- --build
```

The launch profile serves preview at `http://localhost:5000/`; the mode is not selected by the profile. Markdown and theme asset edits trigger regeneration; refresh the browser afterward. Output goes to `preview/` or `dist/`. **Never deploy `preview/`**: it includes drafts and scheduled posts. Deploy only `dist/` with deletions enabled to remove withdrawn pages; preserve the engine's output ownership ledger for in-place builds.

`Theme.HeroImages` supplies the optional home illustration (`Source` and `Alt`; use `""` for decorative art). Set it to `[]` to omit the image. Posts use `hero_image` frontmatter: the paired hello posts share `images/hello-world.png`, while the scheduled pairs share `images/scheduled-post.svg`. URLs work under a subpath. Startup uses automatic theme discovery.

## Locales and publication

- Ordered `Site.Locales` replaces `Site.Locale`/`UseLocaleInUrl`. Here English is unprefixed and Korean uses `ko-kr/`. Keep primary files in `contents/pages/` and `contents/posts/`, translations directly under their `ko-kr/` subdirectories; do not add frontmatter `locale` or a primary `en-us/` directory. Pair by slug; paired posts need the same written calendar date.
- Set nonblank `Theme.Localization.TranslationUnavailable`, `Draft`, and `ScheduledOn` for **each** declared locale, including primary. `ScheduledOn` must contain an actual `{0}` date placeholder. Invalid or missing messages fail before rendering; package messages do not fill gaps. These application messages belong in `sample/appsettings.json`, not `src/theme.json`.
- Disabling locales (omitting or emptying `Site.Locales`) removes locale routes, switching, and HTML language. Move both `ko-kr` source directories **outside `contents` first** or they become ordinary content and may duplicate slugs.

Five Korean source files translate their English counterparts; other Korean routes intentionally show English content with a fallback notice. The requested route/UI language stays Korean, the article is marked with its content language, and its canonical points to the primary route. `hreflang` lists only real translations. The header dropdown works without JavaScript; home/tag pages and the shared 404 switch languages without paired-document SEO. Other theme UI text is not automatically translated.

`Site.TimeZone` is `UTC`; it determines midnight for date-only and offset-free publication dates. Production withholds drafts and future-scheduled posts (and translations of withheld primaries); preview shows their inherited badges on articles and listings. Rebuild at publication time to publish scheduled content; there is no timer. The theme formats authored dates as `yyyy-MM-dd` inside the requested locale's badge message.

When customizing, preserve the fallback notice's `BannerAttributes`/encoded content and badges' `GetRegionAttributes`, attributes, and rendered labels. See the [versioned migration guide](https://github.com/getscissorhands/Scissorhands.NET/blob/v1.0.0-preview.20260928.1/docs/website-documentation.md#upgrading-to-vnext) for the complete engine contract.

## Root and subpath hosting

The default `Site.BaseUrl` is `/`. For a subpath, stop preview and run from `sample`:

```sh
dotnet run -- --Site:BaseUrl=/docs --preview
# Stop preview first:
dotnet run -- --Site:BaseUrl=/docs/ --Site:SiteUrl=https://example.com --build
```

Keep configuration options before the mode flag. Both `/docs` and `/docs/` normalize to `/docs/`. Preview mounts there and redirects GET/HEAD `/` to `/docs/`; other requests outside the prefix return 404. Output stays directly in `preview/` or `dist/`, not a physical `docs` directory. Mount `dist/` at `/docs/` on your production host and serve directory indexes. Use only the origin in `Site.SiteUrl` (preview substitutes its own); the shared `/docs/404.html` is not an automatic rewrite for missing URLs.

## Focused regression checks

Use generated HTML and a browser in both modes at `/` and `/docs/` (prefix the routes below with `/docs` for the latter).

| Routes | Check |
| --- | --- |
| `/`, `/ko-kr/`, `/tags/`, `/ko-kr/tags/`, `/404.html` | Locale links work; home/tag/404 have no paired-document SEO or fallback notice |
| `/about/`, `/ko-kr/about/`, English/Korean hello posts | Real translations have reciprocal alternates and self-canonicals; paired heroes and content resolve |
| `/ko-kr/theme-guide/`, `/ko-kr/reference/` | English fallback content has one Korean notice and primary canonical; reference stays outside navigation but is tagged |
| `/theme-guide/recipes/writing/`, `/theme-guide/recipes/unlisted/` and Korean routes | Nested group is non-clickable; writing joins reading order, unlisted does not |
| `/2026/09/12/markdown-showcase/` | Shared content image resolves |
| `/draft-page/`, `/2026/09/14/draft-post/`, `/2099/01/01/scheduled-post/`, `/2099/02/01/draft-scheduled-post/` and Korean routes | Preview shows inherited draft/scheduled badges, including both on the combined post, and tagged listing entries have badges |
| Production `dist/` | No withheld routes, badges, tags, or links to unpublished content |

Check mobile/desktop, light/dark, keyboard and Escape handling, and the language dropdown without JavaScript. For negative tests, use a disposable copy: missing localization messages or `ScheduledOn` set to `{{0}}` must fail; when testing disabled locales, move `ko-kr` directories outside `contents` first. Restore the sample afterward.

## Generated repositories

If Actions is disabled, apply the initialization naming rules manually: lowercase the repository name, replace `_` and `.` with `-`, and keep existing hyphens (e.g., `My.Theme_Name` becomes `my-theme-name`). A slug must contain a letter or digit. Do not use `default`, `plugins`, `plugin-template`, `theme-template`, `scissorhands-core`, `scissorhands-plugin`, `scissorhands-theme`, or `scissorhands-web`.

Use the slug for `src/<slug>.csproj`, `<slug>.slnx` (and its project reference), `src/theme.json`'s `slug`, `sample/appsettings.json`'s `Site.Theme`, and the sample theme link; set `Site.Author` to the repository owner. Only the manifest display name keeps the original repository name. In `src/_Imports.razor`, use `ScissorHands.Theme.` plus PascalCase nonempty slug segments; prefix the suffix with `_` if it starts with a digit (`123-my.theme` becomes `ScissorHands.Theme._123MyTheme`). Build and run the generated sample to confirm theme discovery and served assets; names such as `web` can still conflict with built-in themes even if the initializer accepts them.

The sample starts with an empty `Plugins` array in `appsettings.json`. To enable plugins, see the [plugin guide](https://getscissorhands.app/docs/plugins/).
