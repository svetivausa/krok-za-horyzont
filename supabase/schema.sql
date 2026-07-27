-- ═══════════════════════════════════════════════════════════════
-- Supabase, тиждень 1 · Схема + політики безпеки
-- Виконати ОДНИМ скриптом у Supabase → SQL Editor.
-- Безпечно запускати на чистому проєкті krok-za-horyzont.
-- ═══════════════════════════════════════════════════════════════

-- ─────────────────────────────────────────────
-- КРОК 1. Структура бази даних
-- ─────────────────────────────────────────────

-- 1. Профілі користувачів
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  name text,
  created_at timestamptz not null default now()
);

-- Автостворення профілю при реєстрації
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = public
as $$
begin
  insert into public.profiles (id, email)
  values (new.id, new.email);
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- 2. Прогрес у продуктах (одна людина + один продукт = один рядок)
create table public.progress (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  product text not null,          -- 'bambuk', 'practicum-beta', 'practicum-p' ...
  data jsonb not null default '{}'::jsonb,  -- те, що зараз лежить у localStorage, як є
  updated_at timestamptz not null default now(),
  unique (user_id, product)
);

-- 3. Журнал подій (для воронки і майбутніх кейсів)
create table public.events (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  event text not null,            -- 'opened_practicum', 'completed_exercise' ...
  meta jsonb,                     -- {"product": "practicum-beta", "exercise": 3}
  created_at timestamptz not null default now()
);

create index events_user_idx on public.events (user_id, created_at);
create index progress_user_idx on public.progress (user_id);


-- ─────────────────────────────────────────────
-- КРОК 2. Політики безпеки (Row Level Security)
-- Правило одне: кожна бачить і змінює тільки своє.
-- ─────────────────────────────────────────────

alter table public.profiles enable row level security;
alter table public.progress enable row level security;
alter table public.events   enable row level security;

-- profiles: читати і оновлювати тільки свій
create policy "own profile select" on public.profiles
  for select using (auth.uid() = id);
create policy "own profile update" on public.profiles
  for update using (auth.uid() = id);

-- progress: повний доступ тільки до своїх рядків
create policy "own progress select" on public.progress
  for select using (auth.uid() = user_id);
create policy "own progress insert" on public.progress
  for insert with check (auth.uid() = user_id);
create policy "own progress update" on public.progress
  for update using (auth.uid() = user_id);

-- events: писати і читати тільки свої
create policy "own events insert" on public.events
  for insert with check (auth.uid() = user_id);
create policy "own events select" on public.events
  for select using (auth.uid() = user_id);

-- Видалення рядків користувачам свідомо НЕ даємо: журнал подій і прогрес
-- не повинні зникати випадково. Світлана має повний доступ через панель Supabase.


-- ─────────────────────────────────────────────
-- КРОК 3. Table-level GRANT для ролі authenticated
-- ─────────────────────────────────────────────
-- RLS вмикає перевірку рядків, АЛЕ не видає базового права на таблицю.
-- Таблиці, створені через SQL Editor, не завжди успадковують дефолтні
-- привілеї Supabase — і тоді навіть залогінений користувач (роль
-- authenticated) отримує "42501: permission denied for table" при будь-якому
-- читанні/записі через API, а синхронізація тихо падає (помилка ловиться і
-- гаситься на клієнті). RLS-політики вище все одно обмежують доступ рядками
-- (auth.uid() = user_id), тож ці GRANT безпечні. anon свідомо БЕЗ прав —
-- застосунок звертається до цих таблиць лише коли людина увійшла.

grant usage on schema public to authenticated;
grant select, insert, update on public.progress to authenticated;
grant select, insert          on public.events   to authenticated;
grant select, update          on public.profiles to authenticated;
