# Theme Template

A starter theme for ScissorHands.NET with Razor views, responsive styling, light/dark mode, and sample content. No UI framework or JavaScript build step is required.

See the **[theme documentation](https://getscissorhands.app/docs/themes/)** for setup, configuration, component APIs, navigation, and customization.

## Prerequisites

- [.NET 10+ SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [Visual Studio 2026](https://visualstudio.microsoft.com/) or [VS Code](https://code.visualstudio.com/) with [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)

## Getting Started

Create your repository with [![Use this template](https://img.shields.io/badge/Use_this_template-2ea44f?style=for-the-badge&logo=github&logoColor=white)](https://github.com/getscissorhands/theme-template/generate), then clone it locally.

On the initial push, the initialization workflow configures the theme and opens a set of development issues in the new repository. If that run does not start automatically, run **Initialize template repository** from the Actions tab. The workflow removes itself and its issue definitions after successful initialization.

## Theme Layout

```text
src/
├── assets/
│   ├── css/
│   │   └── theme.css
│   ├── images/
│   │   └── icons/
│   │       ├── chevron-down.svg
│   │       ├── globe.svg
│   │       ├── github.svg
│   │       ├── moon.svg
│   │       └── sun.svg
│   └── js/
│       └── theme.js
├── favicon.ico
├── theme.json
├── ThemeTemplate.csproj
├── _Imports.razor
├── MainLayout.razor
├── IndexView.razor
├── PostView.razor
├── PageView.razor
├── NotFoundView.razor
├── TagListView.razor
├── TagView.razor
└── Components/
    ├── LanguageSwitcher.razor
    ├── LocalizationMetadata.razor
    ├── LocalizationFallbackBanner.razor
    ├── PublicationBadges.razor
    └── NavigationItems.razor
```

## Local Preview

The sample needs a symbolic link at `sample/themes/<theme-slug>` pointing to `src`, with the relative target `../../src`. The repository initialization workflow creates this link; create it manually if it is missing.

If the link is missing, run one of the following from the repository root. Replace `<theme-slug>` with the `Site:Theme` value in `sample/appsettings.json` if you renamed the theme.

```bash
# zsh/bash
mkdir -p sample/themes
ln -s ../../src sample/themes/<theme-slug>
```

```powershell
# PowerShell
New-Item -ItemType Directory -Path ./sample/themes -Force
New-Item -ItemType SymbolicLink -Path ./sample/themes/<theme-slug> -Target ../../src
```

Then build and preview from the repository root:

```bash
dotnet restore && dotnet build
cd sample
dotnet run -- --preview
```

Open `http://localhost:5000/`. The sample includes English, Korean, missing translations, and preview-only publication statuses. Stop preview before rebuilding Razor components.
