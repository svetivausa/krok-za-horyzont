export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  const { email, name, type, package: pkg } = req.body;
  const apiKey = process.env.MAILERLITE_API_KEY;
  const groupMap = {
    'analytic': 'Аналітик', 'impulsive': 'Імпульсивний', 'integrator': 'Інтегратор', 'observer': 'Споглядач',
    'formula-b':    'Формула - Бажання',
    'formula-p':    'Формула - Переконання',
    'formula-d':    'Формула - Дії',
    'formula-o':    'Формула - Обставини',
    'formula-m':    'Формула - Можливості',
    'formula-res':  'Формула - Ресурси',
    'formula-beta': 'Формула - β',
    'formula-application-карта':     'Формула - Заявка - Карта',
    'formula-application-маршрут':   'Формула - Заявка - Маршрут',
    'formula-application-провідник': 'Формула - Заявка - Провідник'
  };
  const groupName = groupMap[type];
  if (!groupName) return res.status(400).json({ error: 'Unknown type' });

  // Сповіщення в Telegram надсилається незалежно від MailerLite —
  // заявку не можна втратити через те, що групу ще не створили.
  if (type.startsWith('formula-application-')) {
    await notifyTelegram({ name, email, package: pkg });
  }

  try {
    const groupsRes = await fetch('https://connect.mailerlite.com/api/groups?limit=25', { headers: { 'Authorization': `Bearer ${apiKey}`, 'Content-Type': 'application/json', 'Accept': 'application/json' } });
    const groupsData = await groupsRes.json();
    const group = groupsData.data?.find(g => g.name === groupName);
    if (!group) return res.status(400).json({ error: 'Group not found: ' + groupName });
    await fetch('https://connect.mailerlite.com/api/subscribers', { method: 'POST', headers: { 'Authorization': `Bearer ${apiKey}`, 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify({ email, fields: { name }, groups: [group.id] }) });
    return res.status(200).json({ success: true });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}

async function notifyTelegram({ name, email, package: pkg }) {
  const token = process.env.TELEGRAM_NOTIFY_BOT_TOKEN;
  const chatId = process.env.TELEGRAM_NOTIFY_CHAT_ID;
  if (!token || !chatId) return;
  const text =
    '🎯 Нова заявка на «Формулу результату»\n\n' +
    `Ім'я: ${name}\n` +
    `Email: ${email}\n` +
    `Пакет: ${pkg}`;
  try {
    await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chat_id: chatId, text })
    });
  } catch (e) {
    console.error('Telegram notify error', e);
  }
}
