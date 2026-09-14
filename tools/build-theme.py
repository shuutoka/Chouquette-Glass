#!/usr/bin/env python3
"""Build the single-file BetterDiscord theme from cg2/chouquette-core.css."""
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "cg2" / "chouquette-core.css"
OUT = ROOT / "ChouquetteGlass.theme.css"

HEADER = r'''/**
 * @name Chouquette Glass
 * @author Shuutoka
 * @version 2.0.0
 * @description Chouquette Glass modernized for current Discord/BetterDiscord: translucent cyan glass UI with readability-focused typography.
 * @source https://github.com/shuutoka/Chouquette-Glass
 * @website https://github.com/shuutoka/Chouquette-Glass
 */

/*
 * Compatibility base: Translucence 2.x by CapnKitten.
 * It tracks Discord's current UI while Chouquette Glass adds its own palette,
 * readability choices, neon states and legacy-inspired details on top.
 */
@import url("https://capnkitten.github.io/BetterDiscord/Themes/Translucence/css/source.css");

'''

def rendered() -> str:
    return HEADER + CORE.read_text(encoding="utf-8").rstrip() + "\n"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if the generated theme is out of date")
    args = parser.parse_args()
    content = rendered()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != content:
            print("ChouquetteGlass.theme.css is out of date. Run: python tools/build-theme.py")
            return 1
        print("Generated theme is up to date.")
        return 0
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
