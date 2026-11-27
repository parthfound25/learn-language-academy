-- Durable learner activity for the private, manually managed Streamlit accounts.
-- Run once in the Supabase SQL Editor. The app uses the service-role key server-side.
-- Do NOT put the service-role key in client/browser code or commit it to Git.

create table if not exists public.learner_sessions (
  session_id uuid primary key,
  username text not null,
  login_at timestamptz not null default now(),
  last_seen_at timestamptz not null default now(),
  logout_at timestamptz,
  duration_seconds integer not null default 0 check (duration_seconds >= 0),
  status text not null default 'active'
    check (status in ('active', 'logged_out', 'timed_out'))
);

create index if not exists idx_learner_sessions_username_login
  on public.learner_sessions(username, login_at desc);
create index if not exists idx_learner_sessions_status_seen
  on public.learner_sessions(status, last_seen_at desc);

create table if not exists public.learner_progress (
  username text not null,
  language text not null,
  xp integer not null default 0 check (xp >= 0),
  completed_lessons jsonb not null default '[]'::jsonb,
  active_lesson integer not null default 1,
  practice_rounds integer not null default 0 check (practice_rounds >= 0),
  practice_correct integer not null default 0 check (practice_correct >= 0),
  practice_total integer not null default 0 check (practice_total >= 0),
  achievements jsonb not null default '[]'::jsonb,
  updated_at timestamptz not null default now(),
  primary key (username, language),
  check (practice_correct <= practice_total)
);

create table if not exists public.learner_activity_events (
  id bigint generated always as identity primary key,
  username text not null,
  language text not null default '',
  event_type text not null,
  lesson_id integer,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index if not exists idx_learner_events_user_created
  on public.learner_activity_events(username, created_at desc);
create index if not exists idx_learner_events_type_created
  on public.learner_activity_events(event_type, created_at desc);

-- These tables are accessed only by the trusted Streamlit server using the
-- Supabase service-role key. Ordinary anon/authenticated clients get no access.
alter table public.learner_sessions enable row level security;
alter table public.learner_progress enable row level security;
alter table public.learner_activity_events enable row level security;

revoke all on public.learner_sessions from anon, authenticated;
revoke all on public.learner_progress from anon, authenticated;
revoke all on public.learner_activity_events from anon, authenticated;
grant all on public.learner_sessions to service_role;
grant all on public.learner_progress to service_role;
grant all on public.learner_activity_events to service_role;
grant usage, select on sequence public.learner_activity_events_id_seq to service_role;
