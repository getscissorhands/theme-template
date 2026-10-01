# Finish onboarding and verify the new theme

Provide a clear path from cloning the new repository to reviewing its built site. Keep the root `README.md` focused on onboarding; leave engine details in the theme documentation and technical design.

## Acceptance criteria

- [ ] The personalized README accurately describes the finished theme, its prerequisites, the sample theme link, build and preview commands, and where to find design decisions.
- [ ] `dotnet restore && dotnet build` succeeds from the repository root and the sample preview or static build runs from `sample/`.
- [ ] Generated pages and assets are inspected for the representative content and states covered by the other issues.
- [ ] Any omitted validation or known limitations are recorded before declaring the theme ready.
