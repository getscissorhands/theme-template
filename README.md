# Theme Template

This is the theme template for ScissorHands.NET, which provides the basic theme structure.

## Theme Structure

This is the overall structure of the theme.

```text
.
└── src/
    ├── assets/
    │   ├── css/
    │   │   └── theme.css
    │   ├── images/
    │   │   └── logo.png
    │   └── js/
    │       └── theme.js
    │
    ├── favicon.ico
    │
    ├── theme.json
    │
    ├── _Imports.razor
    ├── MainLayout.razor
    ├── IndexView.razor
    ├── PostView.razor
    ├── PageView.razor
    ├── NotFoundView.razor
    ├── TagListView.razor
    └── TagView.razor
```

> **IMPORTANT**: It's strongly recommended to place all the theme files under the `src` directory for better local testing purpose.

## Getting Started

### Theme Manifest &ndash; `theme.json`

- `theme.json` defines the metadata of the theme.

    ```jsonc
    {
      "name": "Theme Template",
      "version": "1.0.0",
      "description": "A theme template for ScissorHands.NET",
      "slug": "theme-template",
      "stylesheets": [
        "/assets/css/theme.css"
      ],
      "scripts": [
        "/assets/js/theme.js"
      ]
    }
    ```

  You can have one or more CSS and JavaScript files. If you choose to do so, make sure to include them all in this `theme.json`.
  The `Stylesheets` and `Scripts` collections on the resulting `ThemeManifest` are read-only after construction, so declare all entries in the manifest instead of modifying them at runtime.

### Components

Theme components are discovered automatically. A ScissorHands.NET app does not need to register them with `AddLayouts`; its `Program.cs` only needs to build and run the application:

```csharp
using ScissorHands.Web;

var app = new ScissorHandsApplicationBuilder(args).Build();
await app.RunAsync();
```

Discovery matches the normalized suffix of the theme component namespace to the `Site:Theme` setting. For this template, `"Theme": "theme-template"` matches the `Template` suffix in the `ScissorHands.Theme.Template` namespace.

#### `_Imports.razor` Global Component

- Set up the namespace of your theme so its normalized suffix matches `Site:Theme`.
- Examples:
  - `@namespace MyScissorHands.Theme.AwesomeTemplate`

#### `MainLayout.razor` Layout Component

- This is the overall HTML layout structure.
- It calls both UI components and plugin components.
- It renders the engine's `NavigationTree` between Home and Tags, including nested pages and non-clickable groups. With JavaScript, arrow buttons open dropdowns on desktop and expandable sections on mobile. Parent-page links remain independent of their toggles.
- Enter or Space toggles a submenu, Tab follows its links, and Escape closes the current branch and returns focus to its toggle. Clicking outside or moving focus outside a branch closes it. Without JavaScript, the buttons stay hidden and the nested links remain visible.
- It forwards `PageNavigation` and all four tag parameters through `CascadingMainLayoutBase` so child views receive their data.
- Keep internal links and theme asset URLs base-relative (for example, `themes/...` rather than `/themes/...`) so the `<base href="@Site.BaseUrl">` element also works when `Site:BaseUrl` is a subpath.
- To change the way of displaying the `@PageTitle` value, override the `CalculatePageTitle()` method:

    ```csharp
    @code {
        protected override string CalculatePageTitle()
        {
            // ADD LOGIC HERE
        }
    }
    ```

- To change the way of displaying the `@PageDescription` value, override the `CalculatePageDescription()` method:

    ```csharp
    @code {
        protected override string CalculatePageDescription()
        {
            // ADD LOGIC HERE
        }
    }
    ```

- To change the way of displaying the `@PageLocale` value, override the `CalculatePageLocale()` method:

    ```csharp
    @code {
        protected override string CalculatePageLocale()
        {
            // ADD LOGIC HERE
        }
    }
    ```

#### `IndexView.razor` Page Component

- This is the landing page of your static website.

#### `PostView.razor` Page Component

- This is the blog post page.

#### `PageView.razor` Page Component

- This is the non-blog post page.
- It displays page tags and the engine-prepared previous/next links, omitting unavailable links.

#### Page Navigation

Pages opt into navigation through frontmatter:

```yaml
---
title: About
slug: about
show_in_navigation: true
---
```

The sample About page uses this setting; no hard-coded About link is needed in the layout. Pages without the setting, drafts, posts, and the 404 page are excluded from the navigation sequence. An existing hidden parent also hides its descendants from navigation. Page and tag content generation remain independent of this opt-in.

Navigation order follows source filenames, with `index.md` first in each directory and directories traversed depth-first. Use filenames such as `01-start.md` and `02-customize.md` to control order, and explicit `slug` values to keep URLs stable when renaming files. The hierarchy is derived from the resolved slugs, including non-clickable groups for missing parent pages.

A nested page such as `pages/guide/index.md` without an explicit slug now resolves to `guide`, not `guide/index`. Set an explicit slug if migrating an existing `/index` URL.

Content and tag links use the package's shared `GetContentUrl` and `GetTagUrl` helpers for escaping and normalization. The index view calls `ContentUrlHelper.GetTagUrl` directly because `IndexViewBase` only exposes the content helper. Navigation URLs are already formatted by the engine and are rendered unchanged.

#### Tag Components

- `TagListView.razor` renders the tag index.
- `TagView.razor` renders the page for an individual tag.
- The included index, post, and page views link their tags to these pages.
- Starting with `1.0.0-preview.20260914.1`, themes must provide all seven roles: main layout, index, post, page, not-found, tag list, and tag view. Both tag components are required; the engine no longer falls back to built-in tag views.

### UI Components

- Feel free to add extra UI components for each layout and page components.
- The list of UI components are below but not limited to:
  - Header
  - Footer
  - Sidebar
  - Navigation
  - Widgets

### CSS, JavaScripts & Favicons

- The included `theme.css` provides a compact reset and a responsive, accessible editorial starter with cool blue-gray and deep slate backgrounds to distinguish it from the built-in theme's warmer palette.
- The navigation's sun/moon button switches between light and dark mode. The theme follows the system preference until a visitor chooses a mode, then remembers that choice in browser storage. Saved preferences are applied before styles load to avoid a flash of the wrong background.
- The included `theme.js` progressively enhances the colour-mode toggle, hierarchical navigation, and the footer's localized current time. Without JavaScript, colours follow the system preference, navigation stays expanded, and the toggle and optional clock line stay hidden.
- Both files are intentionally framework-free and can be replaced or removed as the theme evolves.
- It's recommended to follow the default naming convention like `theme.css` and `theme.js`.
- If you prefer multiple CSS and JavaScript files, feel free to do so.
  - Make sure to include all CSS and JavaScript files in `theme.json` so that they're properly loaded.
- Keep manifest asset paths relative to the theme root, such as `/assets/css/theme.css`; `MainLayout.razor` converts them to base-relative theme URLs.

## Previewing Theme

The solution uses centrally managed `1.*-*` package versions in `Directory.Packages.props`. This includes stable and preview releases within major version 1. To refresh cached floating resolutions, run `dotnet restore --force-evaluate --no-http-cache` from the repository root. The template uses APIs introduced in `1.0.0-preview.20260914.1`.

1. Create an empty web app.

    ```bash
    dotnet new web -n MyScissorHandsApp
    ```

1. Add the latest preview of `ScissorHands.Web` from [NuGet.org](https://www.nuget.org/packages/ScissorHands.Web).

    ```bash
    dotnet add ./MyScissorHandsApp package ScissorHands.Web --prerelease
    ```

   No custom NuGet source or GitHub Packages credentials are required.

1. Add `appsettings.json` that defines the site manifest and plugin manifest.

    ```jsonc
    {
      "Logging": {
        "LogLevel": {
          "Default": "Information",
          "Microsoft": "Warning",
          "Microsoft.Hosting.Lifetime": "Information"
        }
      },
    
      "Site": {
        "Title": "ScissorHands.NET &ndash; Theme Template",
        "Description": "Theme template for ScissorHands.NET static site generator.",
        "Author": "ScissorHands Team",
        "Theme": "theme-template"
      },
    
      "Plugins": [
        {
          "Name": "My Awesome Plugin",
          "Options": {
            "Option1": true,
            "Option2": "lorem ipsum",
            "Option3": 100
          }
        }
      ]
    }
    ```

1. Create a symbolic link under the `themes` directory. Make sure that the symbolic directory should follow the theme's slug.
1. Add a couple of markdown files representing both blog posts and pages.
1. Run the blog app.

    ```bash
    dotnet run -- --preview
    ```

1. Verify the generated HTML properly renders your theme.

## Validating Package Updates

Run `dotnet build` from the repository root to check compatibility with the restored packages. Then run `dotnet run -- --preview` from `sample` to inspect the theme locally.

Check the home page, posts, pages, tags, and previous/next links. Try the hierarchical navigation with a mouse, keyboard, and a mobile viewport; links should remain available when JavaScript is disabled. The starter does not require Python, Node.js, or a browser testing framework.
