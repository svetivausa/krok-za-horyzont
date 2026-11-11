#!/usr/bin/env python3
"""formula-rezultata.html -> en/formula-rezultata.html
The lecture body is a hand translation kept in tools/en_src/formula-rezultata.body.html.
This script takes the Ukrainian page's head, styles, access gate and lab script, and swaps in
the English body. If the Ukrainian lecture text changes, update the body file by hand."""
import pathlib
from en_common import build, head, ROOT

START = '<!-- ═══════════════ STICKY MINI-FORMULA ═══════════════ -->'
END_MARK = '<footer>\n  Крок за горизонт · Лекція «Формула результату»\n</footer>\n'

src = (ROOT / 'formula-rezultata.html').read_text(encoding='utf-8')
i = src.index(START)
j = src.index(END_MARK) + len(END_MARK)
UA_BODY = src[i:j]
EN_BODY = (ROOT / 'tools' / 'en_src' / 'formula-rezultata.body.html').read_text(encoding='utf-8')

PAIRS = [
(UA_BODY, EN_BODY),
('<html lang="uk">', '<html lang="en">'),
('<title>Формула результату · Крок за горизонт</title>',
 '<title>The Results Formula · Beyond the Horizon</title>\n<meta name="robots" content="noindex">\n' + head('formula-rezultata.html', 'formula-rezultata.html')),
('    ">Формула результату</div>', '    ">The Results Formula</div>'),
('">Цей матеріал відкривається за кодом доступу.<br>Введи код, який надійшов після оплати.</p>',
 '">This material opens with an access code.<br>Enter the code you received after payment.</p>'),
('placeholder="Код доступу"', 'placeholder="Access code"'),
('    ">Відкрити доступ</button>', '    ">Unlock</button>'),
('    ">Невірний код. Перевір і спробуй ще раз.</p>', '    ">Wrong code. Check it and try again.</p>'),
('">Немає коду? <a href="/formula-rezultatu-sales" style="color:#C9A84C; text-decoration:none;">Дізнатися про програму →</a></p>',
 '">No code? <a href="/en/formula-rezultatu-sales.html" style="color:#C9A84C; text-decoration:none;">Learn about the program →</a></p>'),
]

build('formula-rezultata.html', 'formula-rezultata.html', PAIRS)
