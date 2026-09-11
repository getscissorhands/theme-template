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
    ├── TagListView.razor (optional)
    └── TagView.razor (optional)
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

#### Optional Tag Components

- `TagListView.razor` renders the tag index.
- `TagView.razor` renders the page for an individual tag.
- Both tag views are optional; omit them when the theme does not provide tag pages.

### UI Components

- Feel free to add extra UI components for each layout and page components.
- The list of UI components are below but not limited to:
  - Header
  - Footer
  - Sidebar
  - Navigation
  - Widgets

### CSS, JavaScripts & Favicons

- It's recommended to follow the default naming convention like `theme.css` and `theme.js`.
- If you prefer multiple CSS and JavaScript files, feel free to do so.
  - Make sure to include all CSS and JavaScript files in `theme.json` so that they're properly loaded.
- Keep manifest asset paths relative to the theme root, such as `/assets/css/theme.css`; `MainLayout.razor` converts them to base-relative theme URLs.

## Previewing Theme

1. Set environment variables for GitHub NuGet Package Registry.

    ```bash
    # zsh/bash
    source ./scripts/setup-gh-auth.sh --username "<GITHUB_USERNAME>" --token "<GITHUB_TOKEN>"
    ```

    ```powershell
    # PowerShell
    . ./scripts/setup-gh-auth.ps1 -Username "<GITHUB_USERNAME>" -Token "<GITHUB_TOKEN>"
    ```

   > **NOTE**: Make sure to **sourcing** the script instead of executing it.

1. Create a console app project by following the Getting Started section of [ScissorHands.NET](https://github.com/getscissorhands/Scissorhands.NET).
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
