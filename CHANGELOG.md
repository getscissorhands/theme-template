# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This file starts tracking changes with the repository-readiness update; it does
not reconstruct earlier release history.

## [Unreleased]

### Added

- GitHub releases with generated notes for new `v*` tag pushes, gated on a
  successful Release solution build. Release versions are extracted from tags.

### Changed

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

[Unreleased]: https://github.com/getscissorhands/theme-template/compare/v1.0.0-preview.20260915.1...HEAD
[v1.0.0-preview.20260915.1]: https://github.com/getscissorhands/theme-template/tree/v1.0.0-preview.20260915.1