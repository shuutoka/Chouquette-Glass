#!/usr/bin/env python3
"""Small no-dependency audit for fragile exact Discord hashes in active sources."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / "cg2" / "chouquette-core.css", ROOT / "ChouquetteGlass.theme.css"]

patterns = {
    "exact class selector": re.compile(r"\.[A-Za-z][A-Za-z0-9-]*(?:__|_)[0-9a-f]{5,6}\b", re.I),
    "hash pinned in attribute selector": re.compile(r'\[class\*=["\'][^"\']*(?:__|_)[0-9a-f]{5,6}["\']\]', re.I),
}

failed = False
for path in FILES:
    text = path.read_text(encoding="utf-8")
    file_hits = []
    for label, pattern in patterns.items():
        for match in sorted(set(pattern.findall(text))):
            file_hits.append((label, match))
    if file_hits:
        failed = True
        print(f"{path.relative_to(ROOT)}: fragile Discord hashes found:")
        for label, item in file_hits:
            print(f"  [{label}] {item}")

if failed:
    raise SystemExit(1)
print("No exact Discord hash selectors found in active Chouquette sources.")
