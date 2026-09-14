# Changelog

## 2.3.0
- Fixed bright/raw Discord scrollbars by overriding both native Discord scrollbar tokens and WebKit scrollbar rendering.
- Added customizable scrollbar width, thin width and track opacity.
- Reworked Discord Settings into a readable glass layer instead of fully transparent panes.
- Added separate settings/sidebar/content/card opacity variables so users can tune readability without changing the chat.
- Reinforced floating context/select menus with an opaque glass background and blur.
- Added styling for Settings range sliders/grabbers.

## 2.3.0

- Restored the original **small loader + remote core** architecture.
- `ChouquetteGlass.theme.css` is user-editable again instead of containing the entire theme.
- `cg2/cgtheme.css` now imports real font/layout/message/component/animation modules.
- Restored the animation import chain rather than silently folding/losing it.
- Added a standalone `ChouquetteGlass.preview.theme.css` for testing before GitHub Pages is updated.
- Preserved legacy user variable names for old personal configurations.
- Defined the previously missing `--color-secondary-light` variable.
- Added comments explaining public variables vs internal aliases.
- Kept a non-empty `cg2/chouquette-core.css` compatibility shim for 2.1 links.
