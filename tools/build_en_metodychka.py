#!/usr/bin/env python3
"""metodychka-<x>.html -> en/metodychka-<x>.html

Same approach as the lecture: the workbook body (from the progress bar to the footer) is a hand
translation kept in tools/en_src/metodychka-<x>.body.html. This script takes the Ukrainian page's
head, styles, access gate and progress script and swaps in the English body.
If the Ukrainian workbook text changes, update the body file by hand.

Usage: python3 tools/build_en_metodychka.py b [p d o m res beta]
       (no arguments = every workbook that already has a body file)

The bot «Опора» answers only in Ukrainian, so the English bodies leave out the bot blocks
until there is an English bot.
"""
import re, sys
from en_common import build, head, ROOT

TITLES = {
    'b':    ('Практикум Б', 'Workbook D: Desire'),
    'p':    ('Практикум П', 'Workbook B: Beliefs'),
    'd':    ('Практикум Д', 'Workbook A: Action'),
    'o':    ('Практикум О', 'Workbook E: Environment'),
    'm':    ('Практикум М', 'Workbook O: Opportunities'),
    'res':  ('Практикум Р', 'Workbook Res: Resources'),
    'beta': ('Практикум β', 'Workbook β: Conversion'),
}

GATE_END = '<!-- ===== КІНЕЦЬ ЗАМКА ДОСТУПУ ===== -->\n'


def build_one(x):
    name = f'metodychka-{x}.html'
    body_file = ROOT / 'tools' / 'en_src' / f'metodychka-{x}.body.html'
    src = (ROOT / name).read_text(encoding='utf-8')
    src = re.sub(r'<!--en-->.*?<!--/en-->', '', src, flags=re.S)
    # the body starts right after the access gate (every workbook has this marker;
    # not all of them have the PROGRESS comment) and ends with the footer
    i = src.index(GATE_END) + len(GATE_END)
    j = src.index('</footer>', i) + len('</footer>')
    if src[j:j + 1] == '\n':
        j += 1
    ua_body = src[i:j]
    en_body = body_file.read_text(encoding='utf-8')
    if not en_body.endswith('\n'):
        en_body += '\n'

    title_ua = re.search(r'<title>(.*?)</title>', src).group(1)
    en_title = TITLES[x][1] + ' · Beyond the Horizon'

    pairs = [
        (ua_body, en_body),
        ('<html lang="uk">', '<html lang="en">'),
        (f'<title>{title_ua}</title>',
         f'<title>{en_title}</title>\n<meta name="robots" content="noindex">\n' + head(name, name)),
        ('    ">Формула результату</div>', '    ">The Results Formula</div>'),
        ('">Цей матеріал відкривається за кодом доступу.<br>Введи код, який надійшов після оплати.</p>',
         '">This material opens with an access code.<br>Enter the code you received after payment.</p>'),
        ('placeholder="Код доступу"', 'placeholder="Access code"'),
        ('    ">Відкрити доступ</button>', '    ">Unlock</button>'),
        ('    ">Невірний код. Перевір і спробуй ще раз.</p>', '    ">Wrong code. Check it and try again.</p>'),
        ('">Немає коду? <a href="/formula-rezultatu-sales" style="color:#C9A84C; text-decoration:none;">Дізнатися про програму →</a></p>',
         '">No code? <a href="/en/formula-rezultatu-sales.html" style="color:#C9A84C; text-decoration:none;">Learn about the program →</a></p>'),
    ]
    # the gate carries a multi-line Ukrainian HTML comment (it contains "<body>", so the shared
    # one-line comment filter misses it); drop every HTML comment that has Cyrillic in it
    strip = lambda s: re.sub(r'<!--(?:(?!-->).)*?[А-Яа-яІіЇїЄєҐґ](?:(?!-->).)*?-->\n?', '', s, flags=re.S)
    build(name, name, pairs, post=strip)


if __name__ == '__main__':
    xs = sys.argv[1:] or [x for x in TITLES if (ROOT / 'tools' / 'en_src' / f'metodychka-{x}.body.html').exists()]
    for x in xs:
        build_one(x)
