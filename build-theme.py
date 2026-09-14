from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "cg2" / "chouquette-core.css"
OUT = ROOT / "ChouquetteGlass.theme.css"

HEADER = """/**
 * @name Chouquette Glass
 * @author Shuutoka
 * @version 2.1.0
 * @description Modern restoration of Chouquette Glass for current Discord/BetterDiscord. Screenshot-faithful transparent blue/cyan glass UI with readability-focused typography.
 * @source https://github.com/shuutoka/Chouquette-Glass
 * @website https://github.com/shuutoka/Chouquette-Glass
 */

/*
 * Chouquette Glass 2.1 is intentionally self-contained for its core look.
 * Only the font is downloaded externally; if Google Fonts is unavailable,
 * Discord falls back to gg sans and the rest of the theme still works.
 */

"""

OUT.write_text(HEADER + CORE.read_text(encoding="utf-8"), encoding="utf-8")
print(f"Built {OUT}")
