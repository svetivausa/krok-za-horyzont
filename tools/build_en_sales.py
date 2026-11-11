#!/usr/bin/env python3
"""formula-rezultatu-sales.html -> en/formula-rezultatu-sales.html
EN offers only two packages (The Map $19, The Route $49); the "Провідник" package is left out.
Option values stay Ukrainian ('Карта', 'Маршрут') because /api/subscribe maps them to MailerLite groups."""
from en_common import build, head

PROVIDNYK_CARD = '''      <div class="package-card">
        <div class="package-name">«Провідник»</div>
        <div class="package-tagline">Зрозуміти, опрацювати і пройти зі Світ</div>
        <div class="package-price">3 490 <span>грн</span></div>
        <div class="package-divider"></div>
        <ul class="package-features">
          <li>Все з пакету «Маршрут»</li>
          <li>14 днів особистого супроводу від Світлани</li>
          <li>Особиста сесія 60 хв - розбір твоєї формули</li>
          <li>Пріоритетна відповідь протягом 24 годин</li>
        </ul>
        <a href="#form" class="btn btn-primary package-btn" onclick="setPackage('Провідник')">Обрати «Провідник»</a>
      </div>

'''
STEP3 = '''      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <h4>Підтримка і розбір особистої формули</h4>
          <p>У пакеті «Провідник» - особиста сесія зі Світланою і 14 днів особистого супроводу. Розбираємо твою конкретну ситуацію.</p>
        </div>
      </div>
'''

FORMULA = 'R = D × B × A × E × O × Res × β'

PAIRS = [
('<html lang="uk">', '<html lang="en">'),
('<title>Формула результату | Крок за горизонт</title>',
 '<title>The Results Formula | Beyond the Horizon</title>\n'
 '<meta name="description" content="A neuroscience-based program for people who are tired of trying hard without real progress. Find where the glitch is. Fix it. Move.">\n'
 + head('formula-rezultatu-sales.html', 'formula-rezultatu-sales.html')),
('grid-template-columns: repeat(3, 1fr);\n    gap: 1.2rem;',
 'grid-template-columns: repeat(2, 1fr);\n    gap: 1.2rem;\n    max-width: 760px;\n    margin-left: auto;\n    margin-right: auto;'),
(PROVIDNYK_CARD, ''),
(STEP3, ''),
('            <option value="Провідник">«Провідник» - 3 490 грн</option>\n', ''),

# HEADER / HERO
('<a href="/" class="site-logo">Крок за <span>горизонт</span></a>\n  <span><a href="#form" class="header-cta">Залишити заявку</a></span>',
 '<a href="/en/" class="site-logo">Beyond the <span>Horizon</span></a>\n'
 '  <span><a href="/formula-rezultatu-sales.html" class="header-cta" hreflang="uk" lang="uk" title="Українська версія" style="margin-right:.5rem;background:transparent;color:var(--brown);border:1px solid var(--cream-dark);">UA</a>'
 '<a href="#form" class="header-cta">Apply</a></span>'),
('<div class="hero-eyebrow">Авторська програма Світлани Сліпченко</div>', '<div class="hero-eyebrow">An original program by Svitlana Slipchenko</div>'),
('      Формула результату:<br>\n      чому все є, а <em>результату немає</em>',
 '      The Results Formula:<br>\n      you have everything, so why <em>no results</em>?'),
('Нейронаукова програма для тих, хто втомився старатися без відчутного руху вперед. Зрозумій де збій. Виправ його. Рухайся.',
 'A neuroscience-based program for people who are tired of trying hard without real progress. Find where the glitch is. Fix it. Move.'),
('R = Б × П · Д × О × М × Рес × β', FORMULA),
('<a href="#form" class="btn btn-primary">Залишити заявку</a>', '<a href="#form" class="btn btn-primary">Apply</a>'),
('<a href="#packages" class="btn btn-outline">Переглянути пакети</a>', '<a href="#packages" class="btn btn-outline">See the packages</a>'),

# PAIN
('<div class="section-eyebrow">Впізнаєш себе?</div>', '<div class="section-eyebrow">Sound familiar?</div>'),
('<h2 class="section-title">Ти робиш все «як треба».<br>Але щось не так.</h2>', '<h2 class="section-title">You do everything “right”.<br>But something\'s off.</h2>'),
('Читаєш книги, ходиш на тренінги, ставиш цілі. І все одно є відчуття що крутишся на місці. Що справжнього - свого - ще не почалося.',
 'You read books, go to trainings, set goals. And you still feel like you\'re spinning in place. Like the real thing, your own thing, hasn\'t started yet.'),
('<div class="pain-card">Робиш з відчуття «треба», а не «хочу» - і не розумієш звідки втома</div>', '<div class="pain-card">You act out of “I should”, not “I want”, and can\'t figure out where the exhaustion comes from</div>'),
('<div class="pain-card">Знаєш що можеш більше, але роки йдуть, а «більше» так і не настає</div>', '<div class="pain-card">You know you can do more, but the years go by and “more” never arrives</div>'),
('<div class="pain-card">Спираєшся на чужі думки, схвалення, очікування - а не на себе</div>', '<div class="pain-card">You lean on other people\'s opinions, approval and expectations, not on yourself</div>'),
('<div class="pain-card">Багато зусиль, мало результату - і не розумієш де саме щось іде не так</div>', '<div class="pain-card">Lots of effort, little result, and you can\'t see where exactly things go wrong</div>'),
('<div class="pain-card">Старт є, середина є, а до фінішу чомусь не доходить</div>', '<div class="pain-card">There\'s a start, there\'s a middle, but somehow you never reach the finish</div>'),
('<div class="pain-card">Відчуваєш що живеш «поряд» зі своїм життям, а не всередині нього</div>', '<div class="pain-card">You feel like you\'re living “next to” your life, not inside it</div>'),

# WHAT IS
('<div class="section-eyebrow">Що це таке</div>', '<div class="section-eyebrow">What it is</div>'),
('<h2 class="section-title">Не мотивація.<br>Не <em>«повір у себе»</em>.<br>Механіка.</h2>', '<h2 class="section-title">Not motivation.<br>Not <em>“believe in yourself”</em>.<br>Mechanics.</h2>'),
('<p>Результат - це не везіння і не характер. Це система з семи компонентів. Якщо хоча б один дорівнює нулю - результат теж нуль. Незалежно від того як сильно ти стараєшся.</p>',
 '<p>Results aren\'t luck and they aren\'t character. They\'re a system of seven components. If even one of them is zero, the result is zero too. No matter how hard you try.</p>'),
('<p>Формула результату - це авторська нейронаукова програма яка дає тобі карту: де саме в тебе збій, і що з цим робити конкретно.</p>',
 '<p>The Results Formula is an original neuroscience-based program that gives you a map: where exactly your glitch is, and what to do about it, concretely.</p>'),
('<p>Не загальні поради. Твоя особиста точка входу.</p>', '<p>Not general advice. Your personal entry point.</p>'),
('<div class="formula-comp-letter">Б</div>Бажання - справжнє паливо', '<div class="formula-comp-letter">D</div>Desire - the real fuel'),
('<div class="formula-comp-letter">П</div>Переконання - фільтр реальності', '<div class="formula-comp-letter">B</div>Beliefs - the filter on reality'),
('<div class="formula-comp-letter">Д</div>Дії - якість і вектор руху', '<div class="formula-comp-letter">A</div>Action - the quality and direction of movement'),
('<div class="formula-comp-letter">О</div>Обставини - поле де ти граєш', '<div class="formula-comp-letter">E</div>Environment - the field you play on'),
('<div class="formula-comp-letter">М</div>Можливості - що помічає мозок', '<div class="formula-comp-letter">O</div>Opportunities - what your brain notices'),
('<div class="formula-comp-letter">Р</div>Ресурси - паливо для руху', '<div class="formula-comp-letter" style="font-size:.8em;">Res</div>Resources - energy for the journey'),
('<div class="formula-comp-letter">β</div>Петля росту - множник досвіду', '<div class="formula-comp-letter">β</div>The growth loop - the experience multiplier'),

# FOR WHOM
('<div class="section-eyebrow">Для кого</div>', '<div class="section-eyebrow">Who it\'s for</div>'),
('<h2 class="section-title">Ця програма для тебе, якщо...</h2>', '<h2 class="section-title">This program is for you if...</h2>'),
('<p>Ти відчуваєш, що живеш за чужим сценарієм і давно не пам\'ятаєш чого хочеш насправді</p>', '<p>You feel like you\'re living someone else\'s script and lost track long ago of what you really want</p>'),
('<p>Ти стараєшся, але результат не відповідає вкладеним зусиллям</p>', '<p>You try hard, but the results don\'t match the effort you put in</p>'),
('<p>Тобі бракує внутрішньої опори - рішення приймаються через страх або думку інших</p>', '<p>You lack inner support: decisions get made out of fear or other people\'s opinions</p>'),
('<p>Ти починаєш і кидаєш, або робиш все правильно але без руху вперед</p>', '<p>You start and quit, or do everything right but don\'t move forward</p>'),
('<p>Ти хочеш зрозуміти механіку, а не просто «повірити в себе»</p>', '<p>You want to understand the mechanics, not just “believe in yourself”</p>'),
('<p>Ти готовий(а) до чесного погляду на себе без самозвинувачення</p>', '<p>You\'re ready to take an honest look at yourself, without self-blame</p>'),

# HOW IT WORKS
('<div class="section-eyebrow">Як це працює</div>', '<div class="section-eyebrow">How it works</div>'),
('<h2 class="section-title">Три кроки до <em>ясності</em></h2>', '<h2 class="section-title">Two steps to <em>clarity</em></h2>'),
('<h4>Інтерактивна лекція з симулятором</h4>', '<h4>An interactive lecture with a simulator</h4>'),
('<p>Дізнаєшся як працює кожен з семи компонентів. Власноруч бачиш у симуляторі як підсилення або ослаблення одного елемента змінює весь результат.</p>',
 '<p>You learn how each of the seven components works. In the simulator you see with your own eyes how strengthening or weakening one element changes the whole result.</p>'),
('<h4>Сім практикумів з ботом «Опора»</h4>', '<h4>Seven workbooks with the “Opora” bot</h4>'),
('<p>Покроково опрацьовуєш кожен компонент у своєму житті. Бот «Опора» веде тебе через вправи, відповідає на питання і не дає зупинитися на півдорозі.</p>',
 '<p>Step by step, you work through each component in your own life. The “Opora” bot guides you through the exercises, answers questions and doesn\'t let you stop halfway. The workbooks are being translated into English and are released one by one; until each one is ready, you get the Ukrainian version.</p>'),

# PACKAGES
('<div class="section-eyebrow">Пакети програми</div>', '<div class="section-eyebrow">Program packages</div>'),
('<h2 class="section-title">Обери свій формат</h2>', '<h2 class="section-title">Choose your format</h2>'),
('<p class="section-lead">Перший потік - обмежена кількість місць.</p>', '<p class="section-lead">First cohort, limited places.</p>'),
('<div class="package-name">«Карта»</div>', '<div class="package-name">The Map</div>'),
('<div class="package-tagline">Зрозуміти механіку</div>', '<div class="package-tagline">Understand the mechanics</div>'),
('<div class="package-price">590 <span>грн</span></div>', '<div class="package-price"><span>$</span>19</div>'),
('<li>Інтерактивна лекція «Формула результату»</li>', '<li>The Results Formula interactive lecture</li>'),
('<li>Симулятор компонентів - побач результат воочію</li>', '<li>A component simulator: see the result for yourself</li>'),
('<li>Довічний доступ до матеріалів</li>', '<li>Lifetime access to the materials</li>'),
("onclick=\"setPackage('Карта')\">Обрати «Карту»</a>", "onclick=\"setPackage('Карта')\">Choose The Map</a>"),
('<div class="package-badge">Найпопулярніший</div>', '<div class="package-badge">Most popular</div>'),
('<div class="package-name">«Маршрут»</div>', '<div class="package-name">The Route</div>'),
('<div class="package-tagline">Зрозуміти і опрацювати</div>', '<div class="package-tagline">Understand and work it through</div>'),
('<div class="package-price">1 490 <span>грн</span></div>', '<div class="package-price"><span>$</span>49</div>'),
('<li>Інтерактивна лекція з симулятором</li>', '<li>The interactive lecture with the simulator</li>'),
('<li>7 практикумів з покроковими вправами</li>', '<li>7 workbooks with step-by-step exercises (English versions released one by one)</li>'),
('<li>Бот «Опора» - підтримка протягом усього шляху</li>', '<li>The “Opora” bot: support along the whole way</li>'),
("onclick=\"setPackage('Маршрут')\">Обрати «Маршрут»</a>", "onclick=\"setPackage('Маршрут')\">Choose The Route</a>"),

# OBJECTIONS
('<div class="section-eyebrow">Питання</div>', '<div class="section-eyebrow">Questions</div>'),
('<h2 class="section-title">Що тебе може зупиняти</h2>', '<h2 class="section-title">What might be holding you back</h2>'),
('onclick="toggleObj(this)">За плечима вже багато курсів, а нічого не змінилося</div>', 'onclick="toggleObj(this)">I\'ve already taken lots of courses and nothing changed</div>'),
('<div class="obj-a">Це і є одна з ознак що якийсь компонент у тебе на нулі. Курси дають знання, але якщо П (переконання) або Б (бажання) не в порядку, жодні знання не перетворяться на результат. Тут ми спочатку знаходимо збій, а потім вже працюємо.</div>',
 '<div class="obj-a">That\'s one of the signs that one of your components is at zero. Courses give knowledge, but if B (beliefs) or D (desire) is off, no amount of knowledge turns into results. Here we find the glitch first, and only then get to work.</div>'),
('onclick="toggleObj(this)">Чи не ще одна «мотиваційна» програма?</div>', 'onclick="toggleObj(this)">Isn\'t this just another “motivational” program?</div>'),
('<div class="obj-a">Ні. Мотивація не лікується мотивацією. Тут нейронаука і конкретна механіка: чому мозок саботує, як працює петля β, чому обставини впливають на тебе більше ніж ти думаєш. Жодних «повір у себе».</div>',
 '<div class="obj-a">No. Motivation can\'t be cured with motivation. This is neuroscience and concrete mechanics: why the brain sabotages, how the β loop works, why your environment affects you more than you think. No “believe in yourself”.</div>'),
('onclick="toggleObj(this)">Скільки часу це займає?</div>', 'onclick="toggleObj(this)">How much time does it take?</div>'),
('<div class="obj-a">Лекція - близько 40 хвилин. Кожен практикум - 20-30 хвилин. Загалом 3-4 години розподілених у зручному для тебе темпі. Доступ безстроковий - повертайся коли зручно.</div>',
 '<div class="obj-a">The lecture takes about 40 minutes. Each workbook, 20-30 minutes. 3-4 hours in total, spread out at whatever pace suits you. Access never expires, so come back whenever you like.</div>'),
('onclick="toggleObj(this)">Що якщо мені не підійде?</div>', 'onclick="toggleObj(this)">What if it doesn\'t work for me?</div>'),
('<div class="obj-a">Напиши мені. Разом розберемося. Якщо матеріал справді не дав тобі нічого нового - поговоримо про це чесно.</div>',
 '<div class="obj-a">Write to me. We\'ll figure it out together. If the material truly gave you nothing new, we\'ll talk about it honestly.</div>'),
('onclick="toggleObj(this)">Коли починати?</div>', 'onclick="toggleObj(this)">When do I start?</div>'),
('<div class="obj-a">Відразу після підтвердження заявки. Доступ відкривається протягом 24 годин після отримання оплати.</div>',
 '<div class="obj-a">Right after your application is confirmed. I\'ll send you a payment link (card or PayPal), and access opens within 24 hours of payment.</div>'),

# AUTHOR
('<div class="section-eyebrow">Хто за цим стоїть</div>', '<div class="section-eyebrow">Who\'s behind it</div>'),
('<div class="author-avatar">С</div>', '<div class="author-avatar">S</div>'),
('<div class="author-name">Світлана Сліпченко</div>', '<div class="author-name">Svitlana Slipchenko</div>'),
('<div class="author-title">Психолог · 40 років стажу</div>', '<div class="author-title">Psychologist · 40 years of practice</div>'),
('<p>Психолог з 40-річним стажем. Ведуча авторського тренінгу «Крок за горизонт». Заслужений тренер України з кікбоксингу. Співавтор книги «Тайський бокс для тебе».</p>',
 '<p>A psychologist with 40 years of practice. Leader of the original “Beyond the Horizon” training. Honored Coach of Ukraine in kickboxing. Co-author of the book “Thai Boxing for You”.</p>'),
('<p>Виховала 8 Чемпіонів Світу з кікбоксингу. Тому коли говорю про Формулу результату - це не теорія. Це те що я бачила в дії сотні разів: на рингу, в залі, в житті.</p>',
 '<p>I coached 8 world kickboxing champions. So when I talk about the Results Formula, it isn\'t theory. It\'s something I\'ve seen in action hundreds of times: in the ring, in the gym, in life.</p>'),
('<p>Результат - це система. І її можна збудувати. Я знаю як.</p>', '<p>Results are a system. And a system can be built. I know how.</p>'),
('<p>Формула результату - це не теорія з книжки. Це роки спостережень за собою і людьми, підкріплені нейронаукою. Я вивела її тому що сама потребувала чіткої карти, а не натхненних слів.</p>',
 '<p>The Results Formula isn\'t book theory. It\'s years of watching myself and other people, backed by neuroscience. I worked it out because I needed a clear map myself, not inspiring words.</p>'),
('<p>Зараз я допомагаю людям знаходити їхній збій і починати рухатися. Не швидко. Але справжньо.</p>',
 '<p>Now I help people find their glitch and start moving. Not fast. But for real.</p>'),

# FORM
('<div class="section-eyebrow">Перший потік</div>', '<div class="section-eyebrow">First cohort</div>'),
('<h2 class="section-title" style="color:var(--cream);">Залиш заявку.<br>Я напишу тобі особисто.</h2>', '<h2 class="section-title" style="color:var(--cream);">Apply.<br>I\'ll write to you personally.</h2>'),
('<p class="section-lead">Місць обмежено. Після заявки я зв\'яжуся з тобою протягом 24 годин і надішлю деталі.</p>',
 '<p class="section-lead">Places are limited. After you apply, I\'ll get in touch within 24 hours with the details and a payment link.</p>'),
('<label class="form-label" for="nameInput">Як до тебе звертатися</label>', '<label class="form-label" for="nameInput">What should I call you</label>'),
('placeholder="Твоє ім\'я"', 'placeholder="Your name"'),
('placeholder="твій@email.com"', 'placeholder="you@email.com"'),
('<label class="form-label" for="packageSelect">Пакет</label>', '<label class="form-label" for="packageSelect">Package</label>'),
('<option value="">Обери пакет</option>', '<option value="">Choose a package</option>'),
('<option value="Карта">«Карта» - 590 грн</option>', '<option value="Карта">The Map - $19</option>'),
('<option value="Маршрут">«Маршрут» - 1 490 грн</option>', '<option value="Маршрут">The Route - $49</option>'),
('          Залишити заявку\n        </button>', '          Apply\n        </button>'),
('<p class="form-fine">Натискаючи кнопку, ти погоджуєшся що я зв\'яжуся з тобою щодо програми. Ніякого спаму.</p>',
 '<p class="form-fine">By clicking the button, you agree that I\'ll contact you about the program. No spam.</p>'),
('<h3>Заявку отримано!</h3>', '<h3>Application received!</h3>'),
('<p>Я напишу тобі особисто протягом 24 годин. Перевір пошту і, якщо хочеш, одразу напиши мені в Telegram - так швидше.</p>',
 '<p>I\'ll write to you personally within 24 hours. Check your email, and if you like, message me on Telegram right away, it\'s faster.</p>'),
('<p>© 2026 Світлана Сліпченко · <a href="/">Крок за горизонт</a></p>', '<p>© 2026 Svitlana Slipchenko · <a href="/en/">Beyond the Horizon</a></p>'),

# JS: tell the API (and the Telegram notification) this is an English application
("body: JSON.stringify({ email, name, type, package: pkg })",
 "body: JSON.stringify({ email, name, type, lang: 'en', package: pkg + ' (EN, ' + ({'Карта':'$19','Маршрут':'$49'})[pkg] + ')' })"),
]

build('formula-rezultatu-sales.html', 'formula-rezultatu-sales.html', PAIRS)
