# ScissorHands.NET Sample

This project provides an end-to-end preview using the NuGet.org engine packages and the theme linked at `themes/theme-template` to `../../src`.

The About page opts into the header navigation with `show_in_navigation: true`. Additional opted-in pages appear in source-filename order and get automatic previous/next links. Nested slugs form the navigation hierarchy; nested `index.md` files without an explicit slug use the containing directory's route.

Run from this directory. The launch profile enables preview mode:

```bash
dotnet run -- --preview
```

The launch profile also starts preview mode automatically when run from an IDE.

Generate static files without starting the preview server:

```bash
dotnet run --no-launch-profile -- --build
```

Generated preview and build outputs are written to `preview/` and `dist/` respectively.

The sample starts with an empty `Plugins` array in `appsettings.json`. To enable plugins, see the [plugin guide](https://getscissorhands.app/docs/plugins/).