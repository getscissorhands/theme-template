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

If the link is missing, run one of the following from the repository root. Replace `theme-template` with the `Site:Theme` value in `sample/appsettings.json` if you renamed the theme.

**PowerShell (`pwsh`)**

```powershell
New-Item -ItemType Directory -Path .\sample\themes -Force | Out-Null
New-Item -ItemType SymbolicLink -Path .\sample\themes\theme-template -Target ..\..\src
```

**Bash**

```bash
mkdir -p sample/themes
ln -s ../../src sample/themes/theme-template
```

On Windows, creating symbolic links may require Developer Mode or an elevated shell.

Then build and preview from the repository root:

```shell
dotnet build
cd sample
dotnet run -- --preview
```

See the [preview instructions](sample/README.md) for generating static files and locating the output.

## Theme Layout

The theme files live under [`src/`](src/):

```text
src/
|-- assets/
|   |-- css/
|   |   `-- theme.css
|   |-- images/
|   |   `-- logo.png
|   `-- js/
|       `-- theme.js
|-- favicon.ico
|-- theme.json
|-- ThemeTemplate.csproj
|-- _Imports.razor
|-- MainLayout.razor
|-- IndexView.razor
|-- PostView.razor
|-- PageView.razor
|-- NotFoundView.razor
|-- TagListView.razor
`-- TagView.razor
```

The [`sample/`](sample/) directory contains the local preview application and example Markdown content.
