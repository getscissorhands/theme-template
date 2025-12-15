# Theme Template

Theme template for ScissorHands.NET, which provides the basic theme structure

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
    └── PageView.razor
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

### Components

#### `_Imports.razor` Global Component

- Set up namespace of your theme.
- Examples:
  - `@namespace MyScissorHands.Theme.AwesomeTemplate`

#### `MainLayout.razor` Layout Component

- This is the overall HTML layout structure.
- It calls both UI components and plugin components.

#### `IndexView.razor` Page Component

- This is the landing page of your static website.

#### `PostView.razor` Page Component

- This is the blog post page.

#### `PageView.razor` Page Component

- This is the non-blog post page.

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

## Previewing Theme

1. Set environment variables for GitHub NuGet Package Registry.

    ```bash
    # zsh/bash
    export GH_PACKAGE_USERNAME="<GITHUB_USERNAME>"
    export GH_PACKAGE_TOKEN="<GITHUB_TOKEN>"
    ```

    ```powershell
    # PowerShell
    $env:GH_PACKAGE_USERNAME = "<GITHUB_USERNAME>"
    $env:GH_PACKAGE_TOKEN = "<GITHUB_TOKEN>"
    ```

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
        "Theme": "theme-template",
        "ContentRoot": "contents",
        "Output": "dist",
        "PreviewOutput": "preview",
        "BaseUrl": "/",
        "IncludeDateInPostUrl": false
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
