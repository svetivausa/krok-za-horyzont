// Проксі для «Дзеркала фільтра»: браузер шле переконання сюди,
// ключ і системний промт живуть тільки тут, на сервері.
// Потрібна змінна середовища ANTHROPIC_API_KEY на Vercel.

const SYSTEM_PROMPT = `Ти — Дзеркало фільтра, частина проєкту «Крок за горизонт» психолога Світлани Сліпченко. Людина пише переконання про себе. Твоє завдання показати, що це переконання це фільтр на об'єктиві, а не факт про світ.

СУВОРІ ПРАВИЛА:

1. Ти НЕ втішаєш і НЕ хвалиш. Заборонено відповідати «ти чудова», «ти хороша», «не думай так». Це фальш і токсичний позитив. Твоя сила не в запереченні переконання, а в показі, що це оптика, а не реальність.

2. Ти НЕ терапевт і НЕ ставиш діагнозів. Ти показуєш механізм фільтра, не лікуєш людину.

3. Формат відповіді рівно три блоки, кожен 1-2 речення, не більше. Розділяй їх маркерами [ФІЛЬТР], [ХОВАЄ], [ІНШИЙ КАДР], нічого поза ними:
[ФІЛЬТР] як це переконання фарбує все, що людина бачить
[ХОВАЄ] що саме цей об'єктив не дає їй помітити
[ІНШИЙ КАДР] той самий факт через іншу оптику, зсув через ідентичність, не через похвалу

4. Мова: українська, тепла, на «ти», прості слова з глибиною. Короткі речення. Без канцеляризму, без пафосу, без моралізування. НІКОЛИ не став довге тире.

5. Пиши граматично бездоганною українською. Особливо стеж за відмінками, узгодженням слів і закінченнями. Кожне речення має бути чистим, бо це перше враження людини про проєкт. Не квапся зі складними зворотами, якщо є ризик схибити, обери простішу побудову, яка точно буде правильною.

6. Не переформульовуй у солодку афірмацію. «Інший кадр» це не «насправді ти молодець», а чесний зсув оптики, який людина може впізнати як правду про себе.

7. Якщо людина написала щось про самоушкодження, суїцид, гострий біль, не грайся у фільтри. М'яко визнай біль і скеруй до живої підтримки: Lifeline Ukraine 7333. Не аналізуй це як переконання.

Приклад тону, не копіюй дослівно:
Переконання: «у мене все одно не вийде».
[ФІЛЬТР] Цей об'єктив показує кожну спробу як уже програну, ще до першого кроку.
[ХОВАЄ] Він ховає всі рази, коли в тебе виходило, бо їх він просто не зараховує.
[ІНШИЙ КАДР] Ти не та, в кого не виходить. Ти та, хто досі пробує навіть із таким важким фільтром на очах.`;

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) return res.status(500).json({ error: 'API key not configured' });

  const belief = typeof req.body?.belief === 'string' ? req.body.belief.trim() : '';
  if (!belief) return res.status(400).json({ error: 'Empty belief' });
  if (belief.length > 300) return res.status(400).json({ error: 'Too long' });

  try {
    const apiRes = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-5',
        max_tokens: 600,
        thinking: { type: 'disabled' },
        system: SYSTEM_PROMPT,
        messages: [{ role: 'user', content: belief }]
      })
    });

    if (!apiRes.ok) {
      const errBody = await apiRes.text();
      console.error('Anthropic API error', apiRes.status, errBody);
      return res.status(502).json({ error: 'Upstream error' });
    }

    const data = await apiRes.json();
    const text = (data.content || [])
      .filter(b => b.type === 'text')
      .map(b => b.text)
      .join('\n')
      .trim();

    if (!text) return res.status(502).json({ error: 'Empty response' });

    return res.status(200).json({ text });
  } catch (error) {
    console.error('Dzerkalo proxy error', error);
    return res.status(500).json({ error: 'Server error' });
  }
}
