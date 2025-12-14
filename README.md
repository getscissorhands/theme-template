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
    │   │   └── image.png
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

### GitHub NuGet Package Registry

1. Set environment variables for GitHub NuGet Package Registry.

    ```bash
    # zsh/bash
    export GH_PACKAGE_USERNAME="<GITHUB_USERNAME>"
    export GH_PACKAGE_TOKEN="<GITHUB_TOKEN>"
    ```

    ```bash
    # PowerShell
    $env:GH_PACKAGE_USERNAME = "<GITHUB_USERNAME>"
    $env:GH_PACKAGE_TOKEN = "<GITHUB_TOKEN>"
    ```

1. Add a NuGet package for the theme.

    ```bash
    dotnet add package ScissorHands.Theme --prerelease
    ```

### `theme.json`

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
- Feel free to organise with your taste.

#### `IndexView.razor` Page Component

- This is the landing page of your static website.

#### `PostView.razor` Page Component

- This is the blog post page.

#### `PageView.razor` Page Component

- This is the non-blog post page.

#### Other UI Components

- Feel free to add extra UI components for each layout and page components.
- The list of possible UI components are:
  - Header
  - Footer
  - Sidebar
  - Navigation
  - Widgets

### CSS, JavaScripts & Favicons

- It's recommended to follow the default naming convention like `theme.css` and `theme.js`.
- If you prefer multiple CSS and JavaScript files, feel free to do so.
  - Make sure to include all CSS and JavaScript files in `theme.json` so that they're properly loaded.

## Testing Theme

1. Create a class library project by following the Getting Started section of [ScissorHands.NET](https://github.com/getscissorhands/Scissorhands.NET).
1. Create a symbolic link under the `themes` directory. Make sure that the symbolic directory should follow the theme's slug.
1. Add a couple of markdown files representing both blog posts and pages.
1. Run the blog app.

    ```bash
    dotnet run -- --preview
    ```

1. Verify the generated HTML properly renders your theme.
