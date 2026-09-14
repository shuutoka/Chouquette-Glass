from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
imports = re.compile(r'@import\s+url\(["\']([^"\']+)["\']\)\s*;')
errors=[]
for p in ROOT.rglob('*.css'):
    if p.stat().st_size == 0:
        errors.append(f'EMPTY: {p.relative_to(ROOT)}')
    text=p.read_text(encoding='utf-8')
    for target in imports.findall(text):
        if target.startswith('./'):
            q=(p.parent/target).resolve()
            if not q.exists(): errors.append(f'MISSING IMPORT: {p.relative_to(ROOT)} -> {target}')
# exact Discord hashes such as foo__a1b2c3 are intentionally forbidden in maintained modules
hash_pat=re.compile(r'\.[A-Za-z][\w-]*__[0-9a-fA-F]{5,8}\b')
for p in (ROOT/'cg2').rglob('*.css'):
    if p.name == 'theme.css': continue
    text=p.read_text(encoding='utf-8')
    for m in hash_pat.finditer(text): errors.append(f'FIXED HASH: {p.relative_to(ROOT)} {m.group(0)}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: non-empty modules, local imports resolved, no fixed Discord hashes.')
