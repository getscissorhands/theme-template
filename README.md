# Theme Template

A ScissorHands.NET starter theme with Razor views, responsive CSS, plain JavaScript, and sample content. No UI framework or asset build step is required.

## Get started

Install the [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0), then [create a repository from this template](https://github.com/getscissorhands/theme-template/generate) and clone it. After the initialization workflow commits its changes, pull them before editing. It derives the theme slug from the repository name and aligns the project, solution, manifest, namespace, configuration, and sample theme link. If Actions is disabled, follow the naming instructions in the [sample guide](sample/README.md) manually.

The sample needs `sample/themes/<theme-slug>` linked to `../../src`. Initialization creates the link; if it is missing, run one of these from the repository root, replacing `theme-template` with `Site:Theme` from `sample/appsettings.json` if renamed:

```sh
mkdir -p sample/themes
ln -s ../../src sample/themes/theme-template
```

```powershell
New-Item -ItemType Directory -Path .\sample\themes -Force
New-Item -ItemType SymbolicLink -Path .\sample\themes\theme-template -Target ..\..\src
```

Build from the repository root, then run the preview from `sample`:

```sh
dotnet restore
dotnet build
cd sample
dotnet run -- --preview
```

Open `http://localhost:5000/`. Stop preview before rebuilding Razor components. To generate deployable static output instead, run `dotnet run -- --build` from `sample`; it writes to `sample/dist/`.

**Never deploy `sample/preview/`: it includes drafts and scheduled posts.** See the [sample guide](sample/README.md) for package versions, localization, subpath hosting, and regression checks, and the [theme documentation](https://getscissorhands.app/docs/themes/) for engine APIs and customization.

## Where to edit

- `src/`: Razor views and `theme.json`; `src/assets/` contains CSS, JavaScript, and theme images.
- `sample/`: Preview app, settings, and example Markdown content.
- `src/assets/images/logo.png`: An unused "Your logo" placeholder; reference it from a view or stylesheet if needed.
