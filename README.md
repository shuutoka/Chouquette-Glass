# Chouquette Glass 2.0

Modernized version of **Chouquette Glass** for current Discord + BetterDiscord.

The original theme was built around Discord class names whose generated suffixes changed repeatedly. Version 2.0 therefore avoids exact Discord hashes wherever practical, relies primarily on Discord design tokens, and uses semantic class-prefix selectors only for the remaining component-specific details.

## Install / test

1. Install and enable BetterDiscord.
2. Copy **`ChouquetteGlass.theme.css`** into the BetterDiscord themes folder.
   - Windows: `%appdata%\BetterDiscord\themes`
3. Enable **Chouquette Glass** in Discord → Settings → BetterDiscord → Themes.
4. Keep Discord on a dark theme for the intended appearance.

`ChouquetteGlass.theme.css` is the distributed/testable file. It imports the actively maintained **Translucence 2.x** compatibility base by CapnKitten, then applies the Chouquette Glass visual layer.

## What changed from the old repository

- Rebuilt the glass/transparency layer for modern Discord.
- Removed dependence on hundreds of obsolete exact hash selectors such as `.chat__52833` or `.panels__58331`.
- Preserved the cyan/blue glass identity, selected-channel neon, translucent panels, custom scrollbar, message styling, popouts and BetterDiscord styling.
- Preserved the **Baloo Bhaijaan 2** font and added conservative line/letter/word spacing for message readability.
- Reworked mention highlighting. Continuous flicker is now disabled by default; it can still be enabled with one variable.
- Reworked composer-button hover animations to be subtler and less distracting.
- Added `prefers-reduced-motion` support.
- Removed the expired signed Discord-CDN wallpaper preset.
- Fixed legacy CSS mistakes and removed dead rules from the active theme.
- Added comments around fragile/important sections.
- Preserved the untouched historical CSS under `legacy-original/` for reference.

## Main customization variables

Edit the `:root` section near the top of `cg2/chouquette-core.css` (or directly in the generated theme while testing):

```css
--cg-background-image: url("DIRECT_HTTPS_IMAGE_URL");
--cg-font-family: "Baloo Bhaijaan 2", "gg sans", sans-serif;
--cg-message-line-height: 1.42;
--cg-message-letter-spacing: 0.012em;
--cg-message-word-spacing: 0.025em;
--cg-panel-blur: 8px;
--cg-accent: rgb(17 194 194);
--cg-neon: #0088ff;
```

To restore the old animated mention glow:

```css
--cg-mention-animation: cg-mention-pulse 1.8s ease-in-out infinite alternate;
```

## Development

The editable source is:

- `cg2/chouquette-core.css`

Regenerate the BetterDiscord file with:

```bash
python tools/build-theme.py
```

Check that the generated file is in sync with:

```bash
python tools/build-theme.py --check
```

The old `cg2/theme.css` and `cg2/cgtheme.css` paths are now compatibility shims for existing GitHub Pages links.

## Why use a compatibility base?

Discord's generated component hashes are not a stable API. A glass theme has to touch a large number of surfaces, so importing an actively maintained compatibility layer is substantially more robust than freezing hundreds of current hashes into Chouquette Glass. Chouquette's actual visual identity and accessibility/readability tweaks remain in this repository.

## Legacy archive

Everything from the uploaded historical version is preserved unchanged in `legacy-original/`.
