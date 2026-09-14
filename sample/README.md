# Theme preview

This project provides an end-to-end preview using the NuGet.org engine packages and the theme linked at `themes/theme-template` to `../../src`.

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

The sample starts with an empty `Plugins` array in `appsettings.json`. To enable plugins, see the [plugin guide](https://getscissorhands.app/docs/plugins/).
