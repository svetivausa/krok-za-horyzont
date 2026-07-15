// js/supabase-client.js
// Спільний модуль для роботи з Supabase на всіх сторінках, де потрібен акаунт.
// Anon key публічний за дизайном — безпеку забезпечує Row Level Security на сервері.
//
// ┌─────────────────────────────────────────────────────────────┐
// │  ВСТАВ СВОЇ ДВА ЗНАЧЕННЯ (Supabase → Settings → API):        │
// │  1. Project URL      → SUPABASE_URL                          │
// │  2. anon public key  → SUPABASE_ANON_KEY                     │
// └─────────────────────────────────────────────────────────────┘

const SUPABASE_URL = 'https://qqxcxsxmoelcmyletirl.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_Ym6yiNiTjNT-pJ0Oq_axMQ_A1avpJs8';

const sb = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// Поточна користувачка або null
async function getCurrentUser() {
  const { data: { session } } = await sb.auth.getSession();
  return session ? session.user : null;
}

// Надіслати magic link на пошту
async function sendMagicLink(email) {
  return sb.auth.signInWithOtp({
    email: email.trim().toLowerCase(),
    options: { emailRedirectTo: window.location.origin + '/vhid' }
  });
}

// Вихід
async function signOut() {
  await sb.auth.signOut();
}

// Записати подію (тихо, без блокування інтерфейсу)
async function trackEvent(event, meta = {}) {
  const user = await getCurrentUser();
  if (!user) return;
  sb.from('events').insert({ user_id: user.id, event, meta })
    .then(() => {}, () => {}); // помилка аналітики не має ламати сторінку
}

// Зберегти прогрес продукту (upsert по user_id + product)
async function saveProgress(product, dataObj) {
  const user = await getCurrentUser();
  if (!user) return { offline: true };
  return sb.from('progress').upsert(
    { user_id: user.id, product, data: dataObj, updated_at: new Date().toISOString() },
    { onConflict: 'user_id,product' }
  );
}

// Завантажити прогрес продукту
async function loadProgress(product) {
  const user = await getCurrentUser();
  if (!user) return null;
  const { data } = await sb.from('progress')
    .select('data').eq('user_id', user.id).eq('product', product).maybeSingle();
  return data ? data.data : null;
}

// Разова міграція локальних даних у хмару після першого входу.
// Викликати почнемо на тижні 2 — зараз лише фундамент.
async function migrateLocalData(product, localStorageKey) {
  const user = await getCurrentUser();
  if (!user) return;
  const migratedFlag = 'migrated_' + product;
  if (localStorage.getItem(migratedFlag)) return;

  const raw = localStorage.getItem(localStorageKey);
  if (raw) {
    const cloud = await loadProgress(product);
    if (!cloud) {                       // у хмарі порожньо: заливаємо локальне
      await saveProgress(product, JSON.parse(raw));
      trackEvent('migrated_local_data', { product });
    }
    // якщо в хмарі щось уже є, локальне НЕ перезаписує хмарне
  }
  localStorage.setItem(migratedFlag, '1');
}
