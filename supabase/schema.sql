-- Learn Language Academy by Parth
-- Initial database foundation. Safe to run once in the Supabase SQL Editor.
-- User data is isolated by auth.uid() through Row Level Security.

create extension if not exists pgcrypto;

-- Learner profile: one row per authenticated Supabase user.
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null default 'Learner',
  native_language_code text not null default 'en',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Course catalogue is shared curriculum content.
create table if not exists public.languages (
  code text primary key,
  name text not null,
  native_name text not null,
  flag_emoji text not null default '',
  created_at timestamptz not null default now()
);

create table if not exists public.courses (
  id uuid primary key default gen_random_uuid(),
  language_code text not null references public.languages(code) on delete restrict,
  interface_language_code text not null default 'en',
  title text not null,
  description text not null default '',
  is_published boolean not null default false,
  created_at timestamptz not null default now(),
  unique (language_code, interface_language_code)
);

create table if not exists public.course_levels (
  id uuid primary key default gen_random_uuid(),
  course_id uuid not null references public.courses(id) on delete cascade,
  code text not null,
  title text not null,
  description text not null default '',
  sort_order integer not null,
  unique (course_id, code),
  unique (course_id, sort_order)
);

create table if not exists public.units (
  id uuid primary key default gen_random_uuid(),
  level_id uuid not null references public.course_levels(id) on delete cascade,
  title text not null,
  description text not null default '',
  sort_order integer not null,
  unique (level_id, sort_order)
);

create table if not exists public.lessons (
  id uuid primary key default gen_random_uuid(),
  unit_id uuid not null references public.units(id) on delete cascade,
  title text not null,
  subtitle text not null default '',
  lesson_type text not null default 'lesson'
    check (lesson_type in ('lesson', 'revision', 'checkpoint', 'exam')),
  content jsonb not null default '{}'::jsonb,
  xp_reward integer not null default 10 check (xp_reward >= 0),
  sort_order integer not null,
  is_published boolean not null default false,
  created_at timestamptz not null default now(),
  unique (unit_id, sort_order)
);

-- Vocabulary can be attached to a lesson and reused in review.
create table if not exists public.vocabulary (
  id uuid primary key default gen_random_uuid(),
  language_code text not null references public.languages(code) on delete restrict,
  term text not null,
  translation text not null,
  pronunciation text not null default '',
  part_of_speech text not null default '',
  example_sentence text not null default '',
  example_translation text not null default '',
  notes text not null default '',
  created_at timestamptz not null default now(),
  unique (language_code, term, translation)
);

create table if not exists public.lesson_vocabulary (
  lesson_id uuid not null references public.lessons(id) on delete cascade,
  vocabulary_id uuid not null references public.vocabulary(id) on delete cascade,
  sort_order integer not null default 0,
  primary key (lesson_id, vocabulary_id)
);

-- Exercises store structured question data; answer keys stay in the database
-- and are only returned to the learner by the app's lesson workflow.
create table if not exists public.exercises (
  id uuid primary key default gen_random_uuid(),
  lesson_id uuid not null references public.lessons(id) on delete cascade,
  exercise_type text not null
    check (exercise_type in ('multiple_choice', 'translation', 'fill_blank', 'matching', 'ordering', 'true_false', 'short_answer')),
  prompt text not null,
  options jsonb not null default '[]'::jsonb,
  explanation text not null default '',
  sort_order integer not null,
  created_at timestamptz not null default now(),
  unique (lesson_id, sort_order)
);

-- Correct answers are stored separately so ordinary authenticated clients cannot read them.
create table if not exists public.exercise_answer_keys (
  exercise_id uuid primary key references public.exercises(id) on delete cascade,
  answer_key jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

-- Learner-specific progress and XP.
create table if not exists public.user_lesson_progress (
  user_id uuid not null references auth.users(id) on delete cascade,
  lesson_id uuid not null references public.lessons(id) on delete cascade,
  status text not null default 'not_started'
    check (status in ('not_started', 'in_progress', 'completed')),
  attempts integer not null default 0 check (attempts >= 0),
  best_score numeric(5,2),
  xp_earned integer not null default 0 check (xp_earned >= 0),
  started_at timestamptz,
  completed_at timestamptz,
  updated_at timestamptz not null default now(),
  primary key (user_id, lesson_id)
);

create table if not exists public.user_vocabulary (
  user_id uuid not null references auth.users(id) on delete cascade,
  vocabulary_id uuid not null references public.vocabulary(id) on delete cascade,
  familiarity smallint not null default 0 check (familiarity between 0 and 5),
  times_seen integer not null default 0 check (times_seen >= 0),
  times_correct integer not null default 0 check (times_correct >= 0),
  next_review_at timestamptz,
  last_seen_at timestamptz,
  created_at timestamptz not null default now(),
  primary key (user_id, vocabulary_id)
);

create table if not exists public.user_stats (
  user_id uuid primary key references auth.users(id) on delete cascade,
  total_xp integer not null default 0 check (total_xp >= 0),
  current_streak integer not null default 0 check (current_streak >= 0),
  longest_streak integer not null default 0 check (longest_streak >= 0),
  last_activity_date date,
  lessons_completed integer not null default 0 check (lessons_completed >= 0),
  updated_at timestamptz not null default now()
);

create table if not exists public.achievements (
  id uuid primary key default gen_random_uuid(),
  code text not null unique,
  title text not null,
  description text not null default '',
  icon text not null default '🏅',
  xp_reward integer not null default 0 check (xp_reward >= 0)
);

create table if not exists public.user_achievements (
  user_id uuid not null references auth.users(id) on delete cascade,
  achievement_id uuid not null references public.achievements(id) on delete cascade,
  unlocked_at timestamptz not null default now(),
  primary key (user_id, achievement_id)
);

-- Automatically create the learner profile and stats row at sign-up.
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
begin
  insert into public.profiles (id, display_name)
  values (
    new.id,
    coalesce(nullif(new.raw_user_meta_data ->> 'display_name', ''), 'Learner')
  )
  on conflict (id) do nothing;

  insert into public.user_stats (user_id)
  values (new.id)
  on conflict (user_id) do nothing;

  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

-- Enable RLS on every public table.
alter table public.profiles enable row level security;
alter table public.languages enable row level security;
alter table public.courses enable row level security;
alter table public.course_levels enable row level security;
alter table public.units enable row level security;
alter table public.lessons enable row level security;
alter table public.vocabulary enable row level security;
alter table public.lesson_vocabulary enable row level security;
alter table public.exercises enable row level security;
alter table public.exercise_answer_keys enable row level security;
alter table public.user_lesson_progress enable row level security;
alter table public.user_vocabulary enable row level security;
alter table public.user_stats enable row level security;
alter table public.achievements enable row level security;
alter table public.user_achievements enable row level security;

-- Shared curriculum is readable by signed-in learners.
drop policy if exists "Authenticated users can read languages" on public.languages;
create policy "Authenticated users can read languages" on public.languages
  for select to authenticated using (true);
drop policy if exists "Authenticated users can read published courses" on public.courses;
create policy "Authenticated users can read published courses" on public.courses
  for select to authenticated using (is_published = true);
drop policy if exists "Authenticated users can read levels of published courses" on public.course_levels;
create policy "Authenticated users can read levels of published courses" on public.course_levels
  for select to authenticated using (
    exists (select 1 from public.courses c where c.id = course_id and c.is_published = true)
  );
drop policy if exists "Authenticated users can read units of published courses" on public.units;
create policy "Authenticated users can read units of published courses" on public.units
  for select to authenticated using (
    exists (
      select 1 from public.course_levels cl
      join public.courses c on c.id = cl.course_id
      where cl.id = level_id and c.is_published = true
    )
  );
drop policy if exists "Authenticated users can read published lessons" on public.lessons;
create policy "Authenticated users can read published lessons" on public.lessons
  for select to authenticated using (
    is_published = true and exists (
      select 1 from public.units u
      join public.course_levels cl on cl.id = u.level_id
      join public.courses c on c.id = cl.course_id
      where u.id = unit_id and c.is_published = true
    )
  );
drop policy if exists "Authenticated users can read vocabulary" on public.vocabulary;
create policy "Authenticated users can read vocabulary" on public.vocabulary
  for select to authenticated using (true);
drop policy if exists "Authenticated users can read lesson vocabulary" on public.lesson_vocabulary;
create policy "Authenticated users can read lesson vocabulary" on public.lesson_vocabulary
  for select to authenticated using (
    exists (select 1 from public.lessons l where l.id = lesson_id and l.is_published = true)
  );
drop policy if exists "Authenticated users can read exercises for published lessons" on public.exercises;
create policy "Authenticated users can read exercises for published lessons" on public.exercises
  for select to authenticated using (
    exists (select 1 from public.lessons l where l.id = lesson_id and l.is_published = true)
  );
drop policy if exists "Authenticated users can read achievements" on public.achievements;
create policy "Authenticated users can read achievements" on public.achievements
  for select to authenticated using (true);

-- Learners can access only their own profile and progress.
drop policy if exists "Learners can read their profile" on public.profiles;
create policy "Learners can read their profile" on public.profiles
  for select to authenticated using (id = (select auth.uid()));
drop policy if exists "Learners can update their profile" on public.profiles;
create policy "Learners can update their profile" on public.profiles
  for update to authenticated using (id = (select auth.uid())) with check (id = (select auth.uid()));

drop policy if exists "Learners can read their lesson progress" on public.user_lesson_progress;
create policy "Learners can read their lesson progress" on public.user_lesson_progress
  for select to authenticated using (user_id = (select auth.uid()));
drop policy if exists "Learners can insert their lesson progress" on public.user_lesson_progress;
create policy "Learners can insert their lesson progress" on public.user_lesson_progress
  for insert to authenticated with check (user_id = (select auth.uid()));
drop policy if exists "Learners can update their lesson progress" on public.user_lesson_progress;
create policy "Learners can update their lesson progress" on public.user_lesson_progress
  for update to authenticated using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()));

drop policy if exists "Learners can read their vocabulary progress" on public.user_vocabulary;
create policy "Learners can read their vocabulary progress" on public.user_vocabulary
  for select to authenticated using (user_id = (select auth.uid()));
drop policy if exists "Learners can insert their vocabulary progress" on public.user_vocabulary;
create policy "Learners can insert their vocabulary progress" on public.user_vocabulary
  for insert to authenticated with check (user_id = (select auth.uid()));
drop policy if exists "Learners can update their vocabulary progress" on public.user_vocabulary;
create policy "Learners can update their vocabulary progress" on public.user_vocabulary
  for update to authenticated using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()));

drop policy if exists "Learners can read their stats" on public.user_stats;
create policy "Learners can read their stats" on public.user_stats
  for select to authenticated using (user_id = (select auth.uid()));
drop policy if exists "Learners can update their stats" on public.user_stats;
create policy "Learners can update their stats" on public.user_stats
  for update to authenticated using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()));

drop policy if exists "Learners can read their achievements" on public.user_achievements;
create policy "Learners can read their achievements" on public.user_achievements
  for select to authenticated using (user_id = (select auth.uid()));
drop policy if exists "Learners can earn their achievements" on public.user_achievements;
create policy "Learners can earn their achievements" on public.user_achievements
  for insert to authenticated with check (user_id = (select auth.uid()));

-- Helpful indexes for course navigation and review queues.
create index if not exists idx_course_levels_course_order on public.course_levels(course_id, sort_order);
create index if not exists idx_units_level_order on public.units(level_id, sort_order);
create index if not exists idx_lessons_unit_order on public.lessons(unit_id, sort_order);
create index if not exists idx_user_progress_user_status on public.user_lesson_progress(user_id, status);
create index if not exists idx_user_vocabulary_review on public.user_vocabulary(user_id, next_review_at);

-- Starter language and achievement catalogue. No hearts/lives mechanic.
insert into public.languages (code, name, native_name, flag_emoji)
values ('fr', 'French', 'Français', '🇫🇷')
on conflict (code) do nothing;

insert into public.achievements (code, title, description, icon, xp_reward) values
  ('first_lesson', 'First steps', 'Complete your first lesson.', '🌱', 10),
  ('five_lessons', 'Building momentum', 'Complete five lessons.', '📚', 25),
  ('vocabulary_25', 'Word collector', 'Learn 25 vocabulary items.', '🧠', 25),
  ('xp_100', 'Century club', 'Earn 100 XP.', '⭐', 20)
on conflict (code) do nothing;
