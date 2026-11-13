#!/usr/bin/env python3
"""bambuk-treker.html -> en/bambuk-treker.html and vhid.html -> en/vhid.html
Same localStorage key and the same Supabase account as the Ukrainian tracker. The magic link
always returns to /vhid (the only allowed redirect URL); /vhid forwards /en/ paths straight back."""
from en_common import build, head

GATE = [
    ('    ">Формула результату</div>', '    ">The Results Formula</div>'),
    ('">Цей матеріал відкривається за кодом доступу.<br>Введи код, який надійшов після оплати.</p>',
     '">This material opens with an access code.<br>Enter the code you received after payment.</p>'),
    ('placeholder="Код доступу"', 'placeholder="Access code"'),
    ('    ">Відкрити доступ</button>', '    ">Unlock</button>'),
    ('    ">Невірний код. Перевір і спробуй ще раз.</p>', '    ">Wrong code. Check it and try again.</p>'),
    ('">Немає коду? <a href="/formula-rezultatu-sales" style="color:#C9A84C; text-decoration:none;">Дізнатися про програму →</a></p>',
     '">No code? <a href="/en/formula-rezultatu-sales.html" style="color:#C9A84C; text-decoration:none;">Learn about the program →</a></p>'),
]

BAMBUK = GATE + [
    ('<html lang="uk">', '<html lang="en">'),
    ('<title>Бамбук · Крок за горизонт</title>',
     '<title>Bamboo · Beyond the Horizon</title>\n<meta name="robots" content="noindex">\n' + head('bambuk-treker.html', 'bambuk-treker.html')),
    ('<div class="series">Крок за горизонт · Трекер</div>', '<div class="series">Beyond the Horizon · Tracker</div>'),
    ('<h1 class="title">Бамбук</h1>', '<h1 class="title">Bamboo</h1>'),
    ('<p class="subtitle">твоя петля результату. День за днем.</p>', '<p class="subtitle">your results loop. Day by day.</p>'),
    ("<p>Пам'ятаєш бамбук із лекції? Роками він росте під землею, а потім злітає вгору.</p>",
     "<p>Remember the bamboo from the lecture? For years it grows underground, and then it shoots up.</p>"),
    ('<p>Тут те саме. Ти не побачиш стрибка за один день. Ти побачиш його через деякий час.</p>',
     "<p>It's the same here. You won't see a leap in a single day. You'll see it after a while.</p>"),
    ('<p>Заходь щодня на пів хвилини. Три дотики. І дивись, як з маленького складається твоє ВЕЛИКЕ.</p>',
     '<p>Drop in every day for half a minute. Three touches. And watch your BIG thing build up from small ones.</p>'),
    ('<p>Твоя вчорашня нотатка: <span class="q">«<span id="betaQuote"></span>»</span>.</p>',
     '<p>Your note from yesterday: <span class="q">“<span id="betaQuote"></span>”</span>.</p>'),
    ('<p>Сьогодні це вже працює на тебе. Ось так рефлексія стає паливом.</p>',
     "<p>Today it's already working for you. That's how reflection becomes fuel.</p>"),
    ('<p>Тебе не було кілька днів. Це не провал.</p>', "<p>You've been away for a few days. That's not a failure.</p>"),
    ('<p>Бамбук у цей час ріс під землею, там, де не видно. Коріння теж робота.</p>',
     "<p>Meanwhile the bamboo was growing underground, where no one can see. Roots are work too.</p>"),
    ('<p>Просто продовж звідти, де ти зараз.</p>', "<p>Just carry on from where you are now.</p>"),
    ('        Тут поки порожньо. Твій перший день стане першим коліном.<br>\n        Почни знизу. Далі рости буде твій бамбук і ти з ним.',
     "        It's empty here for now. Your first day will become the first segment.<br>\n        Start at the bottom. From there, your bamboo will grow, and you with it."),
    ('>висота умовна. Важлива не цифра, а те, що вона росте.</div>',
     ">the height is symbolic. What matters isn't the number, but that it grows.</div>"),
    ('<div class="cloud-invite-label">Твій бамбук</div>', '<div class="cloud-invite-label">Your bamboo</div>'),
    ('<div class="cloud-invite-title" id="cloudInviteTitle">Уже три дні</div>',
     '<div class="cloud-invite-title" id="cloudInviteTitle">Three days already</div>'),
    ('<p class="cloud-invite-text">Твій бамбук росте, і цей прогрес варто зберегти. Увійди, і він залишиться з тобою назавжди, на будь-якому пристрої, з телефона чи ноутбука. Не тільки тут, у цьому браузері.</p>',
     "<p class=\"cloud-invite-text\">Your bamboo is growing, and this progress is worth keeping. Sign in, and it'll stay with you for good, on any device, phone or laptop. Not just here, in this browser.</p>"),
    ('<a class="cloud-invite-btn" href="/vhid?next=/bambuk-treker">Зберегти мій прогрес →</a>',
     '<a class="cloud-invite-btn" href="/en/vhid.html?next=/en/bambuk-treker.html">Save my progress →</a>'),
    ('<button class="cloud-invite-dismiss" id="cloudInviteDismiss">Не зараз</button>',
     '<button class="cloud-invite-dismiss" id="cloudInviteDismiss">Not now</button>'),
    ('<div class="q-label">Наскільки сьогодні ти рухаєшся до свого результату?</div>',
     '<div class="q-label">How much are you moving towards your result today?</div>'),
    ('<div class="scale-ends"><span>зовсім ні</span><span>повний хід</span></div>',
     '<div class="scale-ends"><span>not at all</span><span>full speed</span></div>'),
    ('<div class="q-label">Скільки в тебе зараз палива?</div>', '<div class="q-label">How much fuel do you have right now?</div>'),
    ('<div class="scale-ends"><span>бак порожній</span><span>повний бак</span></div>',
     '<div class="scale-ends"><span>empty tank</span><span>full tank</span></div>'),
    ('<div class="q-label">Що сьогодні спрацювало? Один рядок.</div>', '<div class="q-label">What worked today? One line.</div>'),
    ('placeholder="напиши те, що хочеш забрати з цього дня"', 'placeholder="write what you want to take from this day"'),
    ('<div class="principle-sub">це і є твоя β. Маленький принцип, який завтра стане паливом.</div>',
     "<div class=\"principle-sub\">this is your β. A small principle that will become fuel tomorrow.</div>"),
    ('<button class="save-btn" id="saveBtn" disabled>записати день</button>',
     '<button class="save-btn" id="saveBtn" disabled>save the day</button>'),
    ('<div class="saved-title">Записано. Одне коліно бамбука додано.</div>',
     '<div class="saved-title">Saved. One more bamboo segment added.</div>'),
    ('<div class="saved-sub">Завтра додаси наступне.</div>', "<div class=\"saved-sub\">Tomorrow you'll add the next one.</div>"),
    ('<button class="edit-link" id="editLink">змінити сьогоднішній запис</button>',
     "<button class=\"edit-link\" id=\"editLink\">edit today's entry</button>"),
    ('<a class="bridge-btn" href="https://t.me/opora_krok_bot" target="_blank" rel="noopener">поговорити про це з Опорою</a>',
     '<a class="bridge-btn" href="https://t.me/opora_krok_bot?start=en" target="_blank" rel="noopener">talk it over with Opora</a>'),
    ('<div class="bridge-sub">було щось важливе сьогодні? Опора допоможе докопатись, звідки це і що з цим робити далі.</div>',
     '<div class="bridge-sub">did something important happen today? Opora will help you dig into where it comes from and what to do with it next.</div>'),
    ('<a class="back-link" href="/metodychka-beta">← Повернутись до практикуму β</a>',
     '<a class="back-link" href="/en/metodychka-beta.html">← Back to Workbook β</a>'),
    ('    Твій бамбук росте на цьому пристрої. Заходь звідси ж, щоб бачити весь свій ріст.',
     '    Your bamboo grows on this device. Come back from here to see all of your growth.'),
    ("' колін\">');", "' segments\">');"),
    ('aria-label="Бамбук: \' +', 'aria-label="Bamboo: \' +'),
    ("' у петлі · висота твого бамбука: <strong>'", "' in the loop · your bamboo\\'s height: <strong>'"),
    ("""  function dayWord(n) {
    var n10 = n % 10, n100 = n % 100;
    if (n10 === 1 && n100 !== 11) return 'день';
    if (n10 >= 2 && n10 <= 4 && (n100 < 12 || n100 > 14)) return 'дні';
    return 'днів';
  }""", """  function dayWord(n) { return n === 1 ? 'day' : 'days'; }"""),
    ("""  function pluralDays(n) {
    var mod10 = n % 10, mod100 = n % 100;
    if (mod100 >= 11 && mod100 <= 14) return 'днів';
    if (mod10 === 1) return 'день';
    if (mod10 >= 2 && mod10 <= 4) return 'дні';
    return 'днів';
  }""", """  function pluralDays(n) { return n === 1 ? 'day' : 'days'; }"""),
    ("textContent = 'Уже ' + days + ' ' + pluralDays(days);", "textContent = days + ' ' + pluralDays(days) + ' already';"),
    ("n.textContent = 'Твій прогрес зберігається у твоєму акаунті. Він з тобою на будь-якому пристрої.';",
     "n.textContent = 'Your progress is saved in your account. It stays with you on any device.';"),
]

VHID = [
    ('<html lang="uk">', '<html lang="en">'),
    ('<title>Вхід · Крок за горизонт</title>',
     '<title>Sign in · Beyond the Horizon</title>\n<meta name="robots" content="noindex">\n' + head('vhid.html', 'vhid.html')),
    ('<div class="logo-dot">К</div>', '<div class="logo-dot">B</div>'),
    ('<h1>Вхід у Крок за горизонт</h1>', '<h1>Sign in to Beyond the Horizon</h1>'),
    ('<p class="subtitle">Без пароля. Введи пошту, і ми надішлемо посилання для входу.</p>',
     "<p class=\"subtitle\">No password. Enter your email, and we'll send you a sign-in link.</p>"),
    ('<label for="email">Твоя пошта</label>', '<label for="email">Your email</label>'),
    ('onclick="onSubmitEmail()">Отримати посилання для входу</button>', 'onclick="onSubmitEmail()">Get a sign-in link</button>'),
    ('      Натискаючи кнопку, ти погоджуєшся зі збереженням твого прогресу і пошти для роботи сервісу.',
     '      By pressing the button, you agree that your progress and email will be stored for the service to work.'),
    ('<div class="sent-title">Лист уже летить</div>', '<div class="sent-title">The email is on its way</div>'),
    ('      Перевір пошту <strong id="sentEmail"></strong> і натисни на посилання.<br>\n      Якщо листа нема, зазирни в Спам.',
     "      Check <strong id=\"sentEmail\"></strong> and click the link.<br>\n      The email is in Ukrainian; just press the button in it. If it isn't there, check your Spam folder."),
    ('onclick="onResend()" disabled>Надіслати ще раз (60)</button>', 'onclick="onResend()" disabled>Send again (60)</button>'),
    ('<div class="logged-title">Ти всередині</div>', "<div class=\"logged-title\">You're in</div>"),
    ('<a class="btn" id="continueBtn" href="/">Продовжити →</a>', '<a class="btn" id="continueBtn" href="/en/">Continue →</a>'),
    ('onclick="onSignOut()">Вийти</button>', 'onclick="onSignOut()">Sign out</button>'),
    ("return fromStore || '/';", "return fromStore || '/en/';"),
    ("submitBtn.textContent = on ? 'Надсилаємо…' : 'Отримати посилання для входу';",
     "submitBtn.textContent = on ? 'Sending…' : 'Get a sign-in link';"),
    ("continueBtn.textContent = (nextParam === '/') ? 'На головну →' : 'Продовжити →';",
     "continueBtn.textContent = (nextParam === '/en/') ? 'To the homepage →' : 'Continue →';"),
    ("resendBtn.textContent = 'Надіслати ще раз (' + left + ')';", "resendBtn.textContent = 'Send again (' + left + ')';"),
    ("resendBtn.textContent = 'Надіслати ще раз';", "resendBtn.textContent = 'Send again';"),
    ("showError('Перевір адресу, здається, в ній помилка');", "showError('Check the address, there seems to be a typo');"),
    ("showError('Не вдалося надіслати. Спробуй ще раз за хвилину.');", "showError(\"Couldn't send it. Try again in a minute.\");"),
]

build('bambuk-treker.html', 'bambuk-treker.html', BAMBUK)
build('vhid.html', 'vhid.html', VHID)
