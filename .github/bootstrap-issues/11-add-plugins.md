# Add selected ScissorHands.NET plugins

Choose and configure existing ScissorHands.NET plugins that support the new theme's goals. Do not implement new plugins or add a plugin framework to the theme. Identify the plugins and their purpose from the PRD, TRD and TDD before changing the sample's currently empty `Plugins` configuration.

## Acceptance criteria

- [ ] Each selected plugin has a documented purpose and is compatible with the theme's ScissorHands.NET version and static output.
- [ ] Required plugin packages and settings are added through the repository's existing package and configuration conventions; credentials and environment-specific secrets are not committed.
- [ ] Any theme-side presentation uses the existing `Plugins` context and preserves its forwarding through `MainLayout`.
- [ ] The sample preview demonstrates the selected plugins, and the theme still renders when `Plugins` is empty.
- [ ] Setup instructions and any plugin-specific content requirements are documented for someone creating the finished theme.
