# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This file starts tracking changes with the repository-readiness update; it does
not reconstruct earlier release history.

## [Unreleased]

## [v1.0.0-preview.20260930.1] - 2026-09-30

### Changed

- Verified the latest floating ScissorHands.Theme and ScissorHands.Web NuGet releases (`1.0.0-preview.20260930.1`) and use the theme package's publication badge locale and settings context without shadowing inherited properties.

## [v1.0.0-preview.20260929.2] - 2026-09-29

### Added

- Eleven ordered development issues for new theme repositories, covering requirements, design, hero images, icons, Razor views, plugins, content, metadata, accessibility, agent guidance, and final preview.

### Changed

- New-repository initialization creates the issues with duplicate protection for retries and a manual dispatch fallback, then removes the issue definitions alongside the initialization workflow.
- Noted the generated development issues in the onboarding guide.

## [v1.0.0-preview.20260929.1] - 2026-09-29

### Added

- Post hero images for the English and Korean hello and scheduled examples, rendered with base-relative URLs.
- A GitHub link in the header and five locally stored SVG control icons.

### Changed

- Aligned the five Korean sample translations with their English counterparts, including metadata, links, and examples.
- Moved language switching into an accessible header dropdown that works without JavaScript.
- Grouped supporting Razor components under `src/Components/` and extracted recursive navigation markup, while keeping `MainLayout` at the root for theme discovery.
- Extended generated-repository initialization to use the repository description, personalize the sample title, and replace theme-slug and project-name placeholders in the guides.
- Removed the unused logo asset and shortened the onboarding and contributor guides.

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

[Unreleased]: https://github.com/getscissorhands/theme-template/compare/v1.0.0-preview.20260930.1...HEAD
[v1.0.0-preview.20260930.1]: https://github.com/getscissorhands/theme-template/compare/v1.0.0-preview.20260929.2...v1.0.0-preview.20260930.1
[v1.0.0-preview.20260929.2]: https://github.com/getscissorhands/theme-template/compare/v1.0.0-preview.20260929.1...v1.0.0-preview.20260929.2
[v1.0.0-preview.20260929.1]: https://github.com/getscissorhands/theme-template/compare/v1.0.0-preview.20260928.1...v1.0.0-preview.20260929.1
[v1.0.0-preview.20260928.1]: https://github.com/getscissorhands/theme-template/compare/v1.0.0-preview.20260915.1...v1.0.0-preview.20260928.1
[v1.0.0-preview.20260915.1]: https://github.com/getscissorhands/theme-template/tree/v1.0.0-preview.20260915.1