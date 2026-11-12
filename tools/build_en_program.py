#!/usr/bin/env python3
"""formula-program.html -> en/formula-program.html
Same access codes and localStorage key as the Ukrainian page. Lecture -> /en/formula-rezultata.html,
workbooks -> Ukrainian originals until they are translated (phase 2)."""
from en_common import build, head, ROOT

# workbooks that already have an English page (built by build_en_metodychka.py)
GLYPH_FILE = {'β': 'beta', 'Б': 'b', 'П': 'p', 'Д': 'd', 'О': 'o', 'М': 'm', 'Р': 'res'}
TRANSLATED = {x for x in GLYPH_FILE.values() if (ROOT / 'en' / f'metodychka-{x}.html').exists()}

PROV = '''      <div class="gate-pkg">
        <div class="gate-pkg-name">«Провідник»</div>
        <div class="gate-pkg-price">3 490 грн</div>
        <div class="gate-pkg-row yes">✓ Лекція</div>
        <div class="gate-pkg-row yes">✓ 7 практикумів</div>
        <div class="gate-pkg-row yes">✓ Сесія + підтримка</div>
      </div>
'''

def nav(src, glyph_ua, glyph_en, title_ua, title_en, sub_ua, sub_en):
    note = '' if GLYPH_FILE.get(glyph_ua) in TRANSLATED else ' · in Ukrainian'
    return (f'<span class="nav-glyph">{glyph_ua}</span>\n      <span class="nav-label">{title_ua}<small>{sub_ua}</small></span>',
            f'<span class="nav-glyph"{" style=\"font-size:.7em\"" if len(glyph_en) > 2 else ""}>{glyph_en}</span>\n      <span class="nav-label">{title_en}<small>{sub_en}{note}</small></span>')

PAIRS = [
('<html lang="uk">', '<html lang="en">'),
('<title>Формула результату · Програма</title>', '<title>The Results Formula · Program</title>\n<meta name="robots" content="noindex">\n' + head('formula-program.html', 'formula-program.html')),
('grid-template-columns: repeat(3, 1fr);', 'grid-template-columns: repeat(2, 1fr);'),
(PROV, ''),
('<div class="gate-logo">Формула результату</div>', '<div class="gate-logo">The Results Formula</div>'),
('<p class="gate-sub" style="margin-bottom:1.5rem;">Введи код доступу, який надійшов після оплати.</p>',
 '<p class="gate-sub" style="margin-bottom:1.5rem;">Enter the access code you received after payment.</p>'),
('<div class="gate-pkg-name">«Карта»</div>', '<div class="gate-pkg-name">The Map</div>'),
('<div class="gate-pkg-price">590 грн</div>', '<div class="gate-pkg-price">$19</div>'),
('<div class="gate-pkg-row yes">✓ Лекція</div>', '<div class="gate-pkg-row yes">✓ Lecture</div>'),
('<div class="gate-pkg-row no">✗ Практикуми</div>', '<div class="gate-pkg-row no">✗ Workbooks</div>'),
('        <div class="gate-pkg-row no">✗ Сесія</div>\n', ''),
('<div class="gate-pkg-name">«Маршрут»</div>', '<div class="gate-pkg-name">The Route</div>'),
('<div class="gate-pkg-price">1 490 грн</div>', '<div class="gate-pkg-price">$49</div>'),
('<div class="gate-pkg-row yes">✓ 7 практикумів</div>', '<div class="gate-pkg-row yes">✓ 7 workbooks</div>'),
('placeholder="Код доступу"', 'placeholder="Access code"'),
('<button class="gate-btn" id="gateBtn">Відкрити доступ</button>', '<button class="gate-btn" id="gateBtn">Unlock</button>'),
('<p id="gateError">Невірний код. Перевір і спробуй ще раз.</p>', '<p id="gateError">Wrong code. Check it and try again.</p>'),
('<p class="gate-footer">Немає коду? <a href="/formula-rezultatu-sales">Дізнатися про програму →</a></p>',
 '<p class="gate-footer">No code? <a href="/en/formula-rezultatu-sales.html">Learn about the program →</a> · <a href="/formula-program.html" hreflang="uk" lang="uk" title="Українська версія">UA</a></p>'),
('aria-label="Меню"', 'aria-label="Menu"'),
('<span id="topBarTitle">Формула результату</span>', '<span id="topBarTitle">The Results Formula</span>'),
('<a href="/" style="display:inline-flex;', '<a href="/en/" style="display:inline-flex;'),
('        ← Крок за горизонт\n', '        ← Beyond the Horizon\n'),
('<div class="sidebar-logo">Формула результату</div>', '<div class="sidebar-logo">The Results Formula</div>'),
('<div class="sidebar-tagline">Програма</div>', '<div class="sidebar-tagline">Program</div>'),
('<div class="sidebar-section">Лекція</div>', '<div class="sidebar-section">Lecture</div>'),
('data-src="/formula-rezultata"', 'data-src="/en/formula-rezultata.html"'),
('<span class="nav-label">Інтерактивна лекція<small>Формула результату</small></span>', '<span class="nav-label">Interactive lecture<small>The Results Formula</small></span>'),
('<div class="sidebar-section">Практикуми</div>', '<div class="sidebar-section">Workbooks</div>'),
nav('', 'β', 'β', 'Практикум β', 'Workbook β', 'Індивідуальна формула', 'Your personal formula'),
nav('', 'Б', 'D', 'Практикум Б', 'Workbook D', 'Бажання', 'Desire'),
nav('', 'П', 'B', 'Практикум П', 'Workbook B', 'Переконання', 'Beliefs'),
nav('', 'Д', 'A', 'Практикум Д', 'Workbook A', 'Дії', 'Action'),
nav('', 'О', 'E', 'Практикум О', 'Workbook E', 'Обставини', 'Environment'),
nav('', 'М', 'O', 'Практикум М', 'Workbook O', 'Можливості', 'Opportunities'),
nav('', 'Р', 'Res', 'Практикум Р', 'Workbook Res', 'Ресурси', 'Resources'),
('<iframe id="contentFrame" src="/formula-rezultata" title="Програма"></iframe>', '<iframe id="contentFrame" src="/en/formula-rezultata.html" title="Program"></iframe>'),
("var currentSrc = '/formula-rezultata';", "var currentSrc = '/en/formula-rezultata.html';"),
('<div class="lock-title">Практикуми не входять у твій пакет</div>', '<div class="lock-title">Workbooks aren\'t included in your package</div>'),
('<div class="lock-pkg-badge">Твій пакет</div>', '<div class="lock-pkg-badge">Your package</div>'),
('<div class="lock-pkg-name">«Карта»</div>', '<div class="lock-pkg-name">The Map</div>'),
('<div class="lock-pkg-item yes">✓ Інтерактивна лекція</div>', '<div class="lock-pkg-item yes">✓ Interactive lecture</div>'),
('<div class="lock-pkg-item no">✗ 7 практикумів</div>', '<div class="lock-pkg-item no">✗ 7 workbooks</div>'),
('          <div class="lock-pkg-item no">✗ Сесія</div>\n', ''),
('<div class="lock-pkg-price">590 грн</div>', '<div class="lock-pkg-price">$19</div>'),
('<div class="lock-pkg-badge">Апгрейд</div>', '<div class="lock-pkg-badge">Upgrade</div>'),
('<div class="lock-pkg-name">«Маршрут»</div>', '<div class="lock-pkg-name">The Route</div>'),
('<div class="lock-pkg-item yes">✓ 7 практикумів</div>', '<div class="lock-pkg-item yes">✓ 7 workbooks</div>'),
('<div class="lock-pkg-price">1 490 грн</div>', '<div class="lock-pkg-price">$49</div>'),
('<a href="/formula-rezultatu-sales" class="lock-upgrade">Перейти до програми →</a>', '<a href="/en/formula-rezultatu-sales.html" class="lock-upgrade">Go to the program →</a>'),
]

PAIRS += [(f'data-src="/metodychka-{x}"', f'data-src="/en/metodychka-{x}.html"') for x in sorted(TRANSLATED)]

build('formula-program.html', 'formula-program.html', PAIRS)
