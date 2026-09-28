# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This file starts tracking changes with the repository-readiness update; it does
not reconstruct earlier release history.

## [Unreleased]

## [v1.0.0-preview.20260928.1] - 2026-09-28

### Added

- Theme-owned language switching, canonical/alternate metadata, fallback notices, and preview publication badges using the engine's validated rendering contracts.
- English/Korean sample translations and draft, scheduled, combined, inherited, and missing-translation examples; root/subpath and browser regression guidance.
- Expanded sample nested navigation and reading-order cases, including an unlisted tagged page.
- A configurable homepage hero showing the first `Theme.HeroImages` entry, with a sample SVG illustration and descriptive alt text.
- ScissorHands.NET attribution in the theme footer.
- GitHub releases with generated notes for new `v*` tag pushes, gated on a
  successful Release solution build. Release versions are extracted from tags.

### Changed

- Verified ScissorHands.NET `1.0.0-preview.20260928.1` for Core, Plugin, Theme, and Web while retaining central `1.*-*` package floating.
- Migrated the sample from removed `Site.Locale` to ordered `Site.Locales`, directory translations, and complete application-owned `Theme.Localization` messages; explicitly configured UTC publication time.
- Forwarded locale context and preserved engine-prepared navigation/URLs, content language, required publication regions, and encoded notice/badge receipts.
- Forwarded validated `ThemeSettings` to child views and switched publication badges from removed `ThemeManifest.Localization` to `ThemeSettings.Localization`. Moved the sample from removed `Site.HeroImage` to `Theme.HeroImages` with subpath-safe image URLs.
- Initialization now derives a shared lowercase theme slug at the start of the workflow, replacing repository-name underscores and periods with hyphens. Project/solution filenames, the manifest, configuration, Razor namespace, theme link, and commit staging stay aligned while the display name retains the repository name. An explicit reserved list rejects `default`, `plugins`, `plugin-template`, `theme-template`, `scissorhands-core`, `scissorhands-plugin`, `scissorhands-theme`, and `scissorhands-web` with an actionable error.
- Generated Razor namespace suffixes use PascalCase instead of an unconditional `Theme_` prefix, adding `_` only for digit-leading identifiers. Slugs containing no letters or digits are rejected at the start of initialization.
- Updated migration and preview guidance: preview mounts `Site.BaseUrl` and includes unpublished content. **Never deploy preview output**; deploy production builds only.
- Renamed the CI workflow from `.github/workflows/ci.yml` to
  `.github/workflows/main.yaml`.

## [v1.0.0-preview.20260915.1] - 2026-09-15

### Added

- Contribution, community conduct, security reporting, and support guidance.
- Git attributes for text normalization, script line endings, and binary files.
- Weekly Dependabot checks for GitHub Actions and NuGet.
- Code ownership and GitHub Sponsors configuration.

### Changed

- Replaced Markdown issue templates with structured YAML forms tailored to the
  theme starter.
- Updated workflow actions to `actions/checkout@v7` and
  `actions/setup-dotnet@v6`.

[Unreleased]: https://github.com/getscissorhands/theme-template/compare/v1.0.0-preview.20260928.1...HEAD
[v1.0.0-preview.20260928.1]: https://github.com/getscissorhands/theme-template/compare/v1.0.0-preview.20260915.1...v1.0.0-preview.20260928.1
[v1.0.0-preview.20260915.1]: https://github.com/getscissorhands/theme-template/tree/v1.0.0-preview.20260915.1