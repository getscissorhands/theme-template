# Theme preview

This provides an end-to-end preview with the theme linked at `themes/theme-template` to `../../src`.

## Build

Set up the [theme link](../README.md#local-preview) before building. From the repository root:

```bash
dotnet restore && dotnet build
```

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
