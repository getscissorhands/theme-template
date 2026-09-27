# Theme Template

A starter theme for ScissorHands.NET with Razor views, responsive styling, light/dark mode, and sample content. No UI framework or JavaScript build step is required.

Tested with **ScissorHands.NET `1.0.0-preview.20260927.1`** (Core, Plugin, Theme, and Web). Central package declarations retain the `1.*-*` floating policy; see the [sample guide](sample/README.md) to verify your resolved versions and migrate older configurations.

See the **[theme documentation](https://getscissorhands.app/docs/themes/)** for setup, configuration, component APIs, navigation, and customization.

## Prerequisites

- [.NET 10+ SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [Visual Studio 2026](https://visualstudio.microsoft.com/) or [VS Code](https://code.visualstudio.com/) with [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)

## Getting Started

Create your repository with [![Use this template](https://img.shields.io/badge/Use_this_template-2ea44f?style=for-the-badge&logo=github&logoColor=white)](https://github.com/getscissorhands/theme-template/generate), then clone it locally.

The initialization workflow renames the solution/project, updates `src/theme.json`, `Site.Theme`, and the explicit namespace in `src/_Imports.razor`, and creates the sample's theme link. The repository name is used unchanged as the theme slug and link directory, without an added prefix. Pull that initialization commit before editing. If Actions is disabled, perform those changes manually: keep the manifest slug, theme-link directory, and `Site.Theme` identical, and keep all seven views in one namespace whose suffix matches the slug after punctuation and casing are ignored. Use a valid C# namespace (for example, `my-site` can use `ScissorHands.Theme.Theme_my_site`). Initialization rejects names that conflict with built-in theme discovery, such as `default` and `web`, rather than silently changing the slug; see the [sample guide](sample/README.md) for naming constraints.

## Theme Layout

```text
src/
├── assets/
│   ├── css/
│   │   └── theme.css
│   ├── images/
│   │   └── logo.png
│   └── js/
│       └── theme.js
├── favicon.ico
├── theme.json
├── _Imports.razor
├── LanguageSwitcher.razor
├── LocalizationMetadata.razor
├── LocalizationFallbackBanner.razor
├── PublicationBadges.razor
├── MainLayout.razor
├── IndexView.razor
├── PostView.razor
├── PageView.razor
├── NotFoundView.razor
├── TagListView.razor
└── TagView.razor
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
New-Item -ItemType Directory -Path .\sample\themes -Force
New-Item -ItemType SymbolicLink -Path .\sample\themes\<theme-slug> -Target ..\..\src
```

Then build and preview from the repository root:

```bash
dotnet restore
dotnet build
cd sample
dotnet run -- --preview
```

Open `http://localhost:5000/`. The sample includes English, Korean, missing translations, and preview-only publication statuses. Stop preview before rebuilding Razor components.

**Never deploy `preview/`: it includes drafts and future-scheduled content.** Generate deployable output with `dotnet run -- --build` from `sample`, then deploy only `dist/`. See the [sample guide](sample/README.md) for subpath hosting, migration, and regression checks.
