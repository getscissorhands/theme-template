# Theme Template

A starter theme for ScissorHands.NET with Razor views, responsive styling, light/dark mode, and sample content. No UI framework or JavaScript build step is required.

See the **[theme documentation](https://getscissorhands.app/docs/themes/)** for setup, configuration, component APIs, navigation, and customization.

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) to build and preview the theme.
- [Visual Studio 2026](https://visualstudio.microsoft.com/) or [VS Code](https://code.visualstudio.com/) with [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit), recommended for Razor editing and IntelliSense.

## Get Started

Use **Use this template** on GitHub to create your repository, then clone it locally.

## Preview Locally

The sample needs a symbolic link at `sample/themes/<theme-slug>` pointing to `src`, with the relative target `../../src`. The repository initialization workflow creates this link; create it manually if it is missing.

From the repository root:

```shell
dotnet build
cd sample
dotnet run -- --preview
```

See the [preview instructions](sample/README.md) for generating static files and locating the output.

## Project Layout

- [`src/`](src/): Razor views and theme metadata.
- [`src/assets/`](src/assets/): CSS, JavaScript, and theme images.
- [`sample/`](sample/): Local preview application and example Markdown content.
