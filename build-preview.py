from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "cg2" / "cgtheme.css"
MAIN = ROOT / "ChouquetteGlass.theme.css"
OUTPUT = ROOT / "ChouquetteGlass.preview.theme.css"

IMPORT_RE = re.compile(r'@import\s+url\(["\']([^"\']+)["\']\)\s*;')


def inline_css(path: Path, seen=None):
    """Inline local relative imports, keep external imports (e.g. Google Fonts)."""
    if seen is None:
        seen = set()

    path = path.resolve()
    if path in seen:
        return ""
    seen.add(path)

    text = path.read_text(encoding="utf-8")
    parts = []
    pos = 0

    for match in IMPORT_RE.finditer(text):
        parts.append(text[pos:match.start()])
        target = match.group(1)

        if target.startswith("./"):
            target_path = (path.parent / target).resolve()
            parts.append(f"\n/* ---- inlined: {target_path.relative_to(ROOT)} ---- */\n")
            parts.append(inline_css(target_path, seen))
        else:
            parts.append(match.group(0))

        pos = match.end()

    parts.append(text[pos:])
    return "".join(parts)


main = MAIN.read_text(encoding="utf-8")
meta = main[:main.index("/*\n * IMPORTANT")]
user_root = main[main.index(":root {"):]

OUTPUT.write_text(
    meta.replace("@version 2.2.0", "@version 2.2.0-preview")
    + "\n/* Standalone local preview build. */\n"
    + inline_css(ENTRY)
    + "\n/* ---- user configuration (same variables as the small loader) ---- */\n"
    + user_root,
    encoding="utf-8",
)

print(OUTPUT)
