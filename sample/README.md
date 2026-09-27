# Theme preview

This project provides an end-to-end preview using the NuGet.org engine packages and the theme linked at `themes/theme-template` to `../../src`.

## Tested engine baseline

Restore and generation were verified with **`1.0.0-preview.20260927.1`** for all four packages: `ScissorHands.Core`, `ScissorHands.Plugin`, `ScissorHands.Theme`, and `ScissorHands.Web`.

`Directory.Packages.props` intentionally retains `1.*-*`; no lock file or exact pin is added. A future restore may select a newer release. From the repository root, check the actual resolved versions:

```bash
dotnet restore
dotnet list ThemeTemplate.slnx package --include-transitive
dotnet build
```

Use your renamed solution filename in a generated repository. Confirm the local theme link described in the [template README](../README.md) exists **before building** so the sample compiles the theme's Razor components. Its `bin`/`obj` exclusions must remain intact. Startup uses automatic discovery, not explicit layout registrations.

## Running the preview

Run from this directory:

```bash
dotnet run -- --preview
```

Generate static files without starting the preview server:

```bash
dotnet run -- --build
```

Generated preview and build outputs are written to `preview/` and `dist/` respectively.

**Never deploy `preview/`.** It deliberately includes unpublished content. Deploy only production `dist/`, with deletions enabled so withdrawn pages do not remain on the host. Keep the engine's output ownership ledger during in-place generation; clean old output once when upgrading from an engine without that ledger.

The launch profile supplies `http://localhost:5000`, not a mode. Open that URL after starting preview. Markdown/theme asset edits trigger regeneration; refresh the browser afterward. Stop preview before rebuilding Razor/C# components, then restart it.

## Localization migration

- Replace removed `Site.Locale` and `UseLocaleInUrl` settings with ordered `Site.Locales`. The sample declares `["en-US", "ko-KR"]`; English stays at unprefixed routes and Korean uses `ko-kr/`.
- Keep primary files directly in the existing `contents/pages/` and `contents/posts/` trees. Put translations beneath the additional-locale directory immediately inside those trees, such as `contents/pages/ko-kr/about.md`. Remove all frontmatter `locale` fields; do not add an `en-us/` directory.
- Pair translations by the primary slug. Paired posts must both declare the **same written calendar date**, even when their times/offsets differ.
- Supply application-owned `Theme.Localization` entries for **every** declared locale, including primary: nonblank `TranslationUnavailable`, `Draft`, and `ScheduledOn`. The latter is a complete format template containing a real `{0}` date argument, not only escaped `{{0}}`. Missing messages or malformed templates fail before rendering in both modes; package/English messages never fill declared-locale gaps.
- `Site.Theme` remains a slug string. Application messages are composed with the package's `theme.json`; do not replace its identity, stylesheets, or scripts.
- Omitted, null, or empty `Site.Locales` disables localization and leaves HTML language unspecified. English status messages remain available without enabling an English route. Locale-looking folders then become ordinary content, not excluded translations: move the sample's two `ko-kr` source directories **outside `contents`** before disabling locales to avoid duplicate explicit slugs or accidentally publishing translations as primary content.

The theme forwards `LocaleContext`, renders the three localization base components, and uses engine-prepared switcher/navigation/SEO URLs. A fallback keeps the requested route and UI language but annotates the article with its actual content language. Its canonical points to primary content; `hreflang` lists only actual translations. Home/tag collections and the shared `404.html` have switching links but no paired-document SEO or fallback notice. Other theme UI text is not automatically translated.

Fallback notices use `BannerAttributes` and the encoded `FallbackMessageContent`. Publication badges use `GetRegionAttributes`, each badge's `Attributes`, and `RenderContent(label)`. Preserve these receipts, regions, date/route attributes, and visible content when customizing; engine validation is intentional, not something to disable.

See the [versioned migration guide](https://github.com/getscissorhands/Scissorhands.NET/blob/v1.0.0-preview.20260927.1/docs/website-documentation.md#upgrading-to-vnext) for the full contract.

## Publication and timezone

`Site.TimeZone` is explicitly `UTC` in this sample. It determines the publication instant for date-only (midnight) and offset-free datetime values; explicit `Z`/numeric offsets remain authoritative. Invalid zones and ambiguous/nonexistent local DST times fail clearly. Authored dates remain unchanged in routes and badge labels.

Production excludes drafts and future-scheduled posts. A withheld primary also suppresses its translations. Preview includes them, including inherited statuses, with badges at the start of each affected article and beside home/individual-tag entries. A post can need both draft and scheduled badges; ordinary pages are not scheduled.

The theme formats dates explicitly as invariant `yyyy-MM-dd` inside the requested locale's message template. It consumes prepared status rather than rechecking frontmatter or the clock. Generation captures one time snapshot; rebuild at or after publication time to publish a scheduled post. There is no automatic publishing timer.

## Root and subpath hosting

The default `Site.BaseUrl` is `/`. For a subpath, stop preview and run these from `sample`:

```bash
dotnet run -- --Site:BaseUrl=/docs --preview
# Stop preview, then generate production output for the same mount:
dotnet run -- --Site:BaseUrl=/docs/ --Site:SiteUrl=https://example.com --build
```

Keep configuration options before the bare mode flag so command-line configuration does not consume the following option as the mode's value.

Both `/docs` and `/docs/` normalize to `/docs/`. Preview mounts output there: open `http://localhost:5000/docs/` or `/docs/ko-kr/about/`. GET/HEAD `/` redirects to `/docs/`, not to a locale-prefixed homepage. Unprefixed content/assets and other outside-prefix requests return 404. Theme CSS, JavaScript, favicon, and content images are served under the same mount.

Files stay directly in `preview/` or `dist/`; do not add a physical `docs` directory or prepend the base to prepared links. Configure the production host to mount `dist/` at `/docs/` and serve directory indexes. Use only the origin in `Site.SiteUrl`; preview substitutes its listening origin for canonical URLs. The shared `/docs/404.html` can be opened directly; preview does not rewrite arbitrary missing requests to it.

## Focused regression checks

Run both modes at `/` and `/docs/` after changing views, messages, or assets. No test project or browser dependency is required by the starter; use your browser and the generated HTML. Prefix the routes below with `/docs` for subpath checks.

| Route or check | Expected result |
| --- | --- |
| `/`, `/ko-kr/`, `/tags/`, `/ko-kr/tags/` | Primary stays unprefixed; locale-specific Home, Tags, article and tag links work; no document canonical/alternates |
| `/about/`, `/ko-kr/about/` | Real translations; self-canonical with reciprocal English/Korean alternates; no fallback notice |
| `/ko-kr/theme-guide/` | One Korean notice, English article `lang`, primary canonical, no Korean SEO alternate; navigation and Previous/Next remain Korean |
| `/ko-kr/2026/09/11/hello-scissorhands/` | Translated post, localized authored links, shared image resolves |
| `/2026/09/14/draft-post/` and Korean equivalent | Preview draft badge; Korean fallback also has a notice |
| `/2099/01/01/scheduled-post/` and Korean equivalent | Preview scheduled badge with `data-publication-date="2099-01-01"` |
| `/2099/02/01/draft-scheduled-post/` and Korean equivalent | Two preview badges; translation inherits draft despite no local draft flag |
| `/draft-example/`, `/ko-kr/draft-example/` | Preview draft page and inherited translation; badge beside their `draft-only` tag entries |
| `/tags/publication-preview/` and Korean equivalent | Each affected entry owns its region and badges, including both statuses on the combined post |
| Production `dist/` | No status markers, withheld articles, `draft-only`/`publication-preview` tags, or links/navigation to withheld content |
| `/404.html` | Shared 404 role, language links to homepages, no notice/status/document SEO |

In the browser, check 375px and desktop widths, light/dark and system preference, visible keyboard focus, Tab/Enter language switching, separate parent links/disclosure buttons, Escape dismissal/focus return, and readable notices/badges. Disable JavaScript and confirm language links and expanded nested navigation still work. Verify the colour toggle also works when storage is blocked.

For negative/disabled checks, use a disposable copy: remove each required message (including primary) or set `ScheduledOn` to `{{0}}` and confirm both modes fail with the locale/configuration path. Restore valid messages afterward. Move translations outside `contents`, set locales to `[]` (also try omitting the key), and verify generation succeeds without switcher, notices, or assumed `lang`, while preview badges use English. Restore the sample configuration/content before continuing.

Finally, test initialization in a generated repository: pull its initialization commit, confirm the slug/link/namespace alignment, restore, build, preview, and build static output again. Initialization uses the repository name unchanged for the slug and link directory. Only the C# namespace suffix is prefixed with `Theme_` and has punctuation replaced with underscores, allowing names such as `123-my.theme` without altering the slug. Check that the renamed theme's CSS, JavaScript, and favicon are present and served—not just that compilation succeeds.

With this engine baseline, automatic discovery reserves names that normalize to `default`, contain no letters or digits, or match any suffix of the built-in namespace `ScissorHands.Web` after punctuation and casing are ignored (for example, `web`, `Web`, or `s-web`). Initialization rejects these names before modifying files rather than selecting built-in views or adding a slug prefix. Choose a different repository name. Regression checks should confirm ordinary and numeric/punctuation names work, and reserved names fail with an actionable error.

The sample starts with an empty `Plugins` array in `appsettings.json`. To enable plugins, see the [plugin guide](https://getscissorhands.app/docs/plugins/).
