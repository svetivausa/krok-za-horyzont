"""Shared helper for building /en/ pages from Ukrainian originals by exact replacement.
Every pair must match at least once, otherwise the build fails, so a later change in the
Ukrainian page is never silently left untranslated."""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CYR = '[А-Яа-яІіЇїЄєҐґ]'


def build(src_name, dst_name, pairs, post=None):
    out = (ROOT / src_name).read_text(encoding='utf-8')
    missing = []
    for ua, en in pairs:
        if ua not in out:
            missing.append(ua[:100])
        out = out.replace(ua, en)
    if post:
        out = post(out)
    # drop Ukrainian-only code comments
    out = re.sub(r'/\*[^*]*' + CYR + r'[^*]*\*/', '/* */', out)
    out = re.sub(r'(?m)^\s*//[^\n]*' + CYR + r'[^\n]*\n', '', out)
    out = re.sub(r'(?<=[\s;{},])//[^\n]*' + CYR + r'[^\n]*$', '', out, flags=re.M)
    out = re.sub(r'<!--[^>]*' + CYR + r'[^>]*-->', '', out)
    if missing:
        print('NOT FOUND in', src_name, *missing, sep='\n  ')
        sys.exit(1)
    dst = ROOT / 'en' / dst_name
    dst.parent.mkdir(exist_ok=True)
    dst.write_text(out, encoding='utf-8')
    left = [l.strip()[:140] for l in out.splitlines() if re.search(CYR, l)]
    print(f'written en/{dst_name}; lines with Cyrillic left: {len(left)}')
    for l in left:
        print('   ', l)


def head(ua_path, en_path):
    """canonical + hreflang block for a page pair (paths without leading slash)."""
    base = 'https://www.svitlana-slipchenko.pp.ua/'
    return (f'<link rel="canonical" href="{base}en/{en_path}">\n'
            f'<link rel="alternate" hreflang="uk" href="{base}{ua_path}">\n'
            f'<link rel="alternate" hreflang="en" href="{base}en/{en_path}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{base}{ua_path}">')
