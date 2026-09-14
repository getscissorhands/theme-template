# ScissorHands.NET Sample

This project provides an end-to-end preview using the NuGet.org engine packages and the theme linked at `themes/theme-template` to `../../src`.

For an overview of the example content, see the [theme guide](contents/pages/theme-guide/index.md).

## Running the Sample

Run from this directory and select preview mode explicitly:

```bash
dotnet run -- --preview
```

When running from an IDE, pass `--preview` as an application argument.

Generate static files without starting the preview server:

```bash
dotnet run -- --build
```

Generated preview and build outputs are written to `preview/` and `dist/` respectively.

The sample starts with an empty `Plugins` array in `appsettings.json`. To enable plugins, see the [plugin guide](https://getscissorhands.app/docs/plugins/).