# Chouquette Glass modernization audit

## Why the old 2023 theme broke

The legacy source was built around Discord class names with generated trailing
hashes. Routine Discord rebuilds changed those hashes, so rules stopped matching
one section after another. The old source also mixed layout fixes, animation,
palette and feature-specific styling in one large file, making partial breakage
hard to diagnose.

The first 2.0 modernization attempt was too conservative: it delegated most of
the actual glass transformation to another imported theme and then layered
Chouquette-specific accents on top. If that import or its current selectors did
not match a user's Discord build, Chouquette Glass visibly did very little.

## 2.1 strategy

2.1 makes the core appearance self-contained:

1. Wallpaper is painted explicitly at `html/body` level.
2. Discord's current visual-refresh `--bg-overlay-*` tokens are defined.
3. Major layout surfaces are targeted directly using semantic class prefixes.
4. Opaque paint layers are cleared explicitly.
5. The 2023 screenshots are treated as the visual specification.
6. Exact trailing Discord hashes remain absent from maintained code.
7. BetterDiscord's own `.bd-*` classes are still safe to target exactly.

## Known limits

Discord theming is unofficial and Discord can rename even the semantic prefix of
a component. A future redesign can therefore still require maintenance. The new
structure limits those repairs to small named sections instead of hundreds of
one-build hash replacements.

The default "Minsk" wallpaper is an old external URL inherited from the legacy
theme. If that host disappears, set `--cg-background-image` to a new direct HTTPS
image URL. A built-in gradient remains visible as a fallback.
