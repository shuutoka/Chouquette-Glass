# Chouquette Glass 2.3

This revision restores the **original project architecture** instead of flattening the theme into one accidental monolith.

## 2.3 readability fixes
Discord 2026 renders Settings and scrollbars differently from the 2023 client. Version 2.3 gives Settings a dedicated glass surface and maps Chouquette Glass scrollbar variables to Discord's current native scrollbar tokens. The chat remains highly transparent; Settings are intentionally darker for readability.


## Which file do I use?

- **`ChouquetteGlass.preview.theme.css`** — use this **right now** in BetterDiscord to test the 2.3 code. It is a standalone bundle and does not depend on the GitHub repository already being updated.
- **`ChouquetteGlass.theme.css`** — the small public/user file. It imports `https://shuutoka.github.io/Chouquette-Glass/cg2/cgtheme.css` and then exposes the variables users are expected to edit.
- **`cg2/theme.css`** — compatibility copy matching the location used by the historical repository.

After the new `cg2/` folder has been pushed to GitHub and GitHub Pages has deployed it, `ChouquetteGlass.theme.css` becomes the recommended distributed file.

## Import chain

```text
ChouquetteGlass.theme.css
└─ https://shuutoka.github.io/Chouquette-Glass/cg2/cgtheme.css
   ├─ font.css
   ├─ layout.css
   ├─ messages.css
   ├─ components.css
   └─ animations/animations.css
      ├─ composer-buttons.css
      ├─ mention.css
      ├─ friends-activity.css
      ├─ roles-anim.css
      ├─ sound-para-anim.css
      ├─ spotify.css
      └─ new-posts.css
```

Every imported file contains actual CSS. There are no placeholder/empty modules in this tree.

## Customisation

The public `.theme.css` intentionally keeps the old Chouquette variables (`--color-cyan`, `--color-secondary`, `--background-image-*`, etc.) and adds a few glass/readability variables. The maintained modules translate those user variables to the internal modern values.

This means a user can keep a tiny personalized theme file while the CSS behind it is updated centrally.

## Development workflow

1. Edit files under `cg2/`.
2. Run `python tools/build-preview.py`.
3. Copy `ChouquetteGlass.preview.theme.css` to BetterDiscord's themes directory and reload Discord.
4. When satisfied, push the repository. GitHub Pages updates the remote import used by the small public file.

The preview exists because BetterDiscord loads a theme as one CSS file; remote imports are fine for distribution, but local multi-file development is best bundled before testing.
