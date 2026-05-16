export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  const { email, name, type } = req.body;
  const apiKey = process.env.MAILERLITE_API_KEY;
  const groupMap = { 'analytic': 'Аналітик', 'impulsive': 'Імпульсивний', 'integrator': 'Інтегратор', 'observer': 'Споглядач' };
  const groupName = groupMap[type];
  if (!groupName) return res.status(400).json({ error: 'Unknown type' });
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
