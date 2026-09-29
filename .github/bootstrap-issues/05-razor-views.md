# Rewrite the seven Razor templates for the new theme

Implement the approved layout and content presentation in `src/`. Preserve the existing ScissorHands.NET view contracts rather than replacing the static Razor theme with a client-side application.

## Acceptance criteria

- [ ] `MainLayout`, `IndexView`, `PostView`, `PageView`, `NotFoundView`, `TagListView` and `TagView` remain present and inherit their matching theme bases.
- [ ] `MainLayout` continues forwarding general, tag, adjacent-page and locale context into `CascadingMainLayoutBase`.
- [ ] Posts, pages, tag views, 404, nested navigation, localization fallback and available previous/next links render correctly.
- [ ] Internal URLs and assets remain base-relative and use the appropriate engine helpers; metadata remains Razor-encoded while intended HTML content renders as HTML.
- [ ] Navigation, reading and essential content work without JavaScript; any optional interactions use plain JavaScript.
- [ ] The sample builds and its rendered pages reflect the new design, not just the Razor source.
