# Changelog

## 2.0.0 — 2026-09-14

- Rebuilt Chouquette Glass for the current Discord visual refresh.
- Added a current BetterDiscord single-file entry point: `ChouquetteGlass.theme.css`.
- Replaced most exact Discord hash selectors with native tokens or semantic prefix selectors.
- Added Translucence 2.x as the modern glass compatibility base.
- Added readability controls for line height, letter spacing and word spacing.
- Preserved the cyan glass/neon identity and Baloo Bhaijaan 2 typography.
- Reworked selected-channel, mention, friends activity, composer and role hover effects.
- Disabled continuous mention flicker by default while keeping it as an opt-in variable.
- Added reduced-motion support.
- Added BetterDiscord UI styling using the stable `.bd-*` namespace.
- Added a build helper and legacy URL shims.
- Preserved the historical source under `legacy-original/`.
- Fixed malformed legacy comment syntax around the Server Boost panel rule and retired other dead declarations from active code.
