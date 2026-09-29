# Support zero or more hero images on the homepage

The starter's `IndexView.razor` displays only the first `ThemeSettings.HeroImages` entry. Support an optional, manual-only hero carousel using the existing configured images, without making hero images a prerequisite for a usable homepage.

## Acceptance criteria

- [ ] Zero configured images show no empty image, broken control or unused carousel region.
- [ ] One configured image displays without carousel controls; two or more display one image at a time with previous/next controls and no automatic advancement.
- [ ] Images use the content-image URL helper, preserve configured alternative text, and adapt to mobile and desktop widths.
- [ ] Controls have accessible names, keyboard operation and a clear indication of the active image.
- [ ] With JavaScript unavailable, at least the first image remains visible and the rest of the homepage remains usable.
- [ ] The sample configuration demonstrates both a multi-image case and a way to check the zero- and one-image cases.
