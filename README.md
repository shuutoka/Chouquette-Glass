# Chouquette Glass 2.1

A modern restoration of the old **Chouquette Glass** BetterDiscord theme.
Version 2.1 targets the appearance visible in the author's 2023 screenshots:
a wallpaper-first Discord UI with dark translucent blue glass, cyan accents and
high-contrast rounded text.

## Install

1. Copy `ChouquetteGlass.theme.css` into the BetterDiscord themes folder.
2. Enable **Chouquette Glass** in BetterDiscord.
3. Reload Discord with `Ctrl+R` after replacing an older version.
4. Disable other full UI themes while testing. Small CSS snippets can still be
   used, but another full theme can override Chouquette Glass backgrounds.

The root `ChouquetteGlass.theme.css` is the file intended for normal use.
Everything under `cg2/` is the maintainable source/development layout.

## Change the wallpaper

Near the start of `ChouquetteGlass.theme.css`, edit:

```css
--cg-background-image: url("https://example.com/my-wallpaper.jpg");
```

Use a direct HTTPS image URL. The included fallback gradient makes a broken old
wallpaper URL obvious without returning Discord to an opaque default theme.

## Readability controls

The main user-facing values are grouped at the top of the CSS:

```css
--cg-message-font-size: 16px;
--cg-message-line-height: 1.38;
--cg-letter-spacing: 0.006em;
--cg-word-spacing: 0.015em;
```

The original `Baloo Bhaijaan 2` font is kept because it is part of the theme's
identity and was used in the old code. If it cannot load, Discord falls back to
`gg sans`.

## Transparency controls

The most useful values are:

```css
--cg-global-tint: rgb(5 9 28 / 0.46);
--cg-sidebar: rgb(18 24 58 / 0.38);
--cg-chat: rgb(13 16 43 / 0.23);
--cg-input: rgb(3 9 27 / 0.48);
--cg-popout: rgb(3 9 24 / 0.66);
```

Lower alpha = more wallpaper visible. Higher alpha = easier reading on a busy
wallpaper.

## Why the CSS looks different from the 2023 version

Discord generates new trailing class hashes frequently. The old theme contained
hundreds of exact selectors such as `.chatContent__5dca8`, which eventually stop
matching. The maintained source instead uses semantic prefix selectors such as:

```css
[class*="chatContent_"]
[class*="sidebarList_"]
[class*="channelTextArea_"]
```

It also defines Discord's newer `--bg-overlay-*` design variables. This does not
make a third-party Discord theme permanently update-proof, but it removes the
largest source of needless breakage.

## Repository layout

- `ChouquetteGlass.theme.css` — install this in BetterDiscord.
- `cg2/chouquette-core.css` — maintained theme source.
- `cg2/theme.css` / `cg2/cgtheme.css` — compatibility/development loaders.
- `legacy-original/` — untouched 2023 source for historical reference.
- `VISUAL_REFERENCE.md` — written target extracted from the old screenshots.
- `tools/` — small audit/build utilities retained from the modernization work.

## Troubleshooting

If enabling the theme changes the font/cyan accents but not the wallpaper or
panels, first disable other full themes and reload Discord. If the wallpaper is
missing but the fallback blue gradient appears, replace the old wallpaper URL
with a current direct image URL.

If Discord later changes a semantic class prefix, update only the relevant
section in `cg2/chouquette-core.css`; do not copy the new trailing hash into the
source unless there is no practical alternative.
